import logging

from aadiscordbot.cogs.utils.decorators import has_perm
from discord import AutocompleteContext, Option
from discord.commands import SlashCommandGroup
from discord.embeds import Embed
from discord.ext import commands
from eveuniverse.models import EveRegion, EveSolarSystem
from rapidfuzz import fuzz, process
from routing.routing import route_length, route_path_gates, systems_range

from django.conf import settings
from django.utils import timezone

from allianceauth.services.modules.discord.models import DiscordUser

from drifters import __version__
from drifters.app_settings import DRIFTERS_JOVE_OBSERVATORIES
from drifters.models import Clear, Wormhole
from drifters.routing import include_drifters_driftercomplexes

logger = logging.getLogger(__name__)


def get_complex_name_from_id(id: int) -> str:
    if id == 31000001:
        return Wormhole.Complexes.SENTINEL
    elif id == 31000002:
        return Wormhole.Complexes.BARBICAN
    elif id == 31000003:
        return Wormhole.Complexes.VIDETTE
    elif id == 31000004:
        return Wormhole.Complexes.CONFLUX
    elif id == 31000005:
        return Wormhole.Complexes.THERA
    elif id == 31000006:
        return Wormhole.Complexes.REDOUBT
    elif id == 30002086:
        return Wormhole.Complexes.TURNUR
    return ""


class Drifters(commands.Cog):
    """
    Drifter Wormhole Mapping and Management
    From AA-Drifters
    """

    def __init__(self, bot):
        self.bot = bot

    drifter_commands = SlashCommandGroup(
        "drifters", "Drifter Wormholes", guild_ids=[int(settings.DISCORD_GUILD_ID)])

    async def search_jove_obervatories(self, ctx: AutocompleteContext) -> list[str]:
        """
        Returns a subset of solar systems, known to have jove observatories, that begin with the characters entered so far

        :param ctx: _description_
        :type ctx: AutocompleteContext
        :return: Fuzzy Searched list of solar systems as a list of strings.
        :rtype: list
        """
        return [i[0] for i in process.extract(ctx.value, DRIFTERS_JOVE_OBSERVATORIES, scorer=fuzz.WRatio, limit=10)]

    async def search_solar_systems(self, ctx: AutocompleteContext) -> list[str]:
        """
        Returns a subset of solar systems, that begin with the characters entered so far

        :param ctx: _description_
        :type ctx: AutocompleteContext
        :return: Fuzzy Searched list of solar systems as a list of strings.
        :rtype: list
        """
        return list(EveSolarSystem.objects.filter(name__icontains=ctx.value).values_list('name', flat=True)[:10])

    async def search_regions(self, ctx: AutocompleteContext) -> list[str]:
        """
        Returns a list of EveSolarSystems that begin with the characters entered so far

        :param ctx: _description_
        :type ctx: AutocompleteContext
        :return: _description_
        :rtype: list
        """
        return list(EveRegion.objects.filter(name__icontains=ctx.value).values_list('name', flat=True)[:10])

    @drifter_commands.command(name="about", description="About the Discord Bot", guild_ids=[int(settings.DISCORD_GUILD_ID)])
    async def about(self, ctx):
        """
        All about the bot
        """
        embed = Embed(title="AA Drifters")
        embed.description = "https://gitlab.com/tactical-supremacy/aa-drifters\nShvo please come back"
        embed.url = "https://gitlab.com/tactical-supremacy/aa-drifters"
        embed.set_thumbnail(url="https://images.evetech.net/types/34495/render?size=128")
        embed.set_footer(
            text="Developed for INIT and publicly available to encourage destruction by Ariel Rin")
        embed.add_field(
            name="Version", value=f"{__version__}", inline=False
        )

        return await ctx.respond(embed=embed)

    @drifter_commands.command(name="clear", description="Report a system as Clear of drifter holes", guild_ids=[int(settings.DISCORD_GUILD_ID)])
    async def clear(
        self, ctx,
        system=Option(str, "Solar System", autocomplete=search_jove_obervatories),
    ):
        """
        Adds a Clear record and optionally tidies up any holes in the system
        """
        archived_holes = 0
        try:
            clear_report, created = Clear.objects.get_or_create(
                system=EveSolarSystem.objects.get(name=system))
            if created is True:
                clear_report.created_at = timezone.now()
                clear_report.created_by = DiscordUser.objects.get(uid=ctx.user.id).user
            else:
                clear_report.updated_at = timezone.now()
                clear_report.updated_by = DiscordUser.objects.get(uid=ctx.user.id).user
            clear_report.save()
        except EveSolarSystem.DoesNotExist as e:
            logger.error(e)
            return await ctx.respond(f"System {system} not found")
        except DiscordUser.DoesNotExist as e:
            logger.error(e)
            return await ctx.respond("User not Found")
        except Exception as e:
            logger.error(e)

        try:
            archived_holes = Wormhole.active_private_holes.filter(system=EveSolarSystem.objects.get(name=system)).update(
                archived=True,
                archived_at=timezone.now(),
                archived_by=DiscordUser.objects.get(uid=ctx.user.id).user)
        except EveSolarSystem.DoesNotExist as e:
            logger.error(e)
            return await ctx.respond(f"System {system} not found")
        except DiscordUser.DoesNotExist as e:
            logger.error(e)
            return await ctx.respond("User not Found")
        except Exception as e:
            logger.error(e)

        if created is True:
            return await ctx.respond(f"{system} Marked as Clear for the first time, {archived_holes} Wormholes archived")
        elif created is False:
            return await ctx.respond(f"{system} Updated as Clear, {archived_holes} Wormholes archived")
        else:
            return await ctx.respond(f"{system} Unable to confirm=, please try again. {archived_holes} Wormholes archived")

    @drifter_commands.command(name="add", description="Add a Drifter wormhole in a K-Space system", guild_ids=[int(settings.DISCORD_GUILD_ID)])
    async def add_wormhole(
        self, ctx,
        system=Option(str, "Solar System", autocomplete=search_jove_obervatories),
        complex=Option(str, "Drifter Complex", choices=Wormhole.Complexes),
        mass=Option(str, "Mass Status", choices=Wormhole.Mass.values),
        lifetime=Option(str, "Life Remaining", choices=Wormhole.Lifetime.values),
        bookmarked_k=Option(bool, "K Space Bookmarked?", default='True', choices=["True", "False"]),
        bookmarked_w=Option(bool, "W Space Bookmarked?", default='True', choices=["True", "False"])
    ):
        """
        Adds a drifter hole record
        """
        await ctx.trigger_typing()

        try:
            Clear.objects.get(EveSolarSystem.objects.get(name=system)).delete()
        except Exception as e:
            logger.error(e)
        try:
            Wormhole.objects.create(
                system=EveSolarSystem.objects.get(name=system),
                complex=complex,
                mass=mass,
                lifetime=lifetime,
                created_at=timezone.now(),
                created_by=DiscordUser.objects.get(uid=ctx.user.id).user,
                bookmarked_k=bookmarked_k,
                bookmarked_w=bookmarked_w,
            )
        except EveSolarSystem.DoesNotExist:
            return await ctx.respond(f"System:{system} not found")
        except DiscordUser.DoesNotExist:
            return await ctx.respond("User not Found")
        except Exception as e:
            logger.error(e)

        return await ctx.respond(f"Saved {complex} hole in {system}, {mass}, {lifetime} <t:{timezone.now():.0}:R>")

    @drifter_commands.command(name="complex_list", description="List wormholes leading to a complex", guild_ids=[int(settings.DISCORD_GUILD_ID)])
    async def list_complex_wormholes(
        self, ctx,
        complex=Option(str, "Drifter Complex", choices=Wormhole.Complexes.values)
    ):
        """
        list_complex_wormholes _summary_

        :param ctx: _description_
        :type ctx: _type_
        :param complex: _description_, defaults to Option(str, "Drifter Complex", choices=Wormhole.Complexes.values)
        :type complex: _type_, optional
        :return: _description_
        :rtype: _type_
        """
        embed = Embed(title=f"AA-Drifters: {complex}")

        for wormhole in Wormhole.active_public_holes.filter(complex=complex):
            embed.add_field(
                name=wormhole.system.name, value=f"Mass {wormhole.mass} Lifetime {wormhole.lifetime}\n Updated:<t:{wormhole.updated_at.timestamp():.0f}:R>", inline=False
            )

        return await ctx.respond(embed=embed)

    @drifter_commands.command(name="system_list", description="List wormholes in a system", guild_ids=[int(settings.DISCORD_GUILD_ID)])
    async def list_system_wormholes(
        self, ctx,
        system=Option(str, "Solar System", autocomplete=search_jove_obervatories),
    ):
        """
        list_system_wormholes _summary_

        :param ctx: _description_
        :type ctx: _type_
        :param system: _description_, defaults to Option(str, "Solar System", autocomplete=search_jove_obervatories)
        :type system: _type_, optional
        :return: _description_
        :rtype: _type_
        """
        evesolarsystem = EveSolarSystem.objects.get(name=system)

        embed = Embed(title=f"AA-Drifters: {system}")

        for wormhole in Wormhole.active_public_holes.filter(system=evesolarsystem):
            embed.add_field(
                name=wormhole.complex, value=f"{wormhole.mass}, {wormhole.formatted_lifetime}\n Updated:<t:{wormhole.updated_at.timestamp():.0f}:R>", inline=False
            )

        return await ctx.respond(embed=embed)

    @drifter_commands.command(name="system_jumps_list", description="List wormholes of wormoles x jumps from system", guild_ids=[int(settings.DISCORD_GUILD_ID)])
    async def list_system_jumps_wormholes(
        self, ctx,
        system=Option(str, "Solar System", autocomplete=search_solar_systems),
        jumps=Option(int, "Jumps", default=5, required=True)
    ):
        """_summary_

        Args:
            ctx (_type_): _description_
            system (_type_, optional): _description_. Defaults to Option(str, "Solar System", autocomplete=search_solar_systems).
            jumps (_type_, optional): _description_. Defaults to Option(int, required=True).
        """
        evesolarsystem = EveSolarSystem.objects.get(name=system)

        embed = Embed(title=f"AA-Drifters: {evesolarsystem}")

        for wormhole in Wormhole.active_public_holes.filter(system__in=systems_range(evesolarsystem.id, jumps)):
            embed.add_field(
                name=wormhole.complex, value=f"{wormhole.mass}, {wormhole.formatted_lifetime}, Updated:<t:{wormhole.updated_at.timestamp():.0f}:R>", inline=False
            )

        return await ctx.respond(embed=embed)

    @drifter_commands.command(name="region_list", description="List wormholes in a Region", guild_ids=[int(settings.DISCORD_GUILD_ID)])
    async def list_region_wormholes(
        self, ctx,
        region=Option(str, "Region", autocomplete=search_regions),
    ):
        """
        list_region_wormholes _summary_

        :param ctx: _description_
        :type ctx: _type_
        :param system: _description_, defaults to Option(str, "Region", autocomplete=search_regions)
        :type system: _type_, optional
        :return: _description_
        :rtype: _type_
        """
        everegion = EveRegion.objects.get(name=region)

        embed = Embed(title=f"AA-Drifters: {region}")

        for wormhole in Wormhole.active_public_holes.filter(system__eve_constellation__eve_region=everegion):
            embed.add_field(
                name=wormhole.complex, value=f"{wormhole.mass}, {wormhole.formatted_lifetime}, Updated:<t:{wormhole.updated_at.timestamp():.0f}:R>", inline=False
            )

        return await ctx.respond(embed=embed)

    @drifter_commands.command(name="region_status", description="Known Jove Observatories in a region and their Status", guild_ids=[int(settings.DISCORD_GUILD_ID)])
    async def status_region(
        self, ctx,
        region=Option(str, "Region", autocomplete=search_regions),
    ):
        """
        list_region_wormholes _summary_

        :param ctx: _description_
        :type ctx: _type_
        :param system: _description_, defaults to Option(str, "Region", autocomplete=search_regions)
        :type system: _type_, optional
        :return: _description_
        :rtype: _type_
        """
        everegion = EveRegion.objects.get(name=region)
        embed = Embed(title=f"AA-Drifters: Status {region}")
        content = ""

        for system in EveSolarSystem.objects.filter(eve_constellation__eve_region=everegion, name__in=DRIFTERS_JOVE_OBSERVATORIES):
            if Wormhole.active_public_holes.filter(system=system):
                for wormhole in Wormhole.active_public_holes.filter(system=system):
                    content += f"{system.name} - {wormhole.complex}, {wormhole.mass}, {wormhole.formatted_lifetime}, Updated:<t:{wormhole.updated_at.timestamp():.0f}:R>) \n"
            elif Clear.objects.filter(system=system):
                for clear in Clear.objects.filter(system=system):
                    content += f"{system.name} - Clear (<t:{clear.updated_at.timestamp():.0f}:R>)\n"
            else:
                content += f"{system.name} - UNKNOWN\n"
        embed.description = content

        return await ctx.respond(embed=embed)

    @drifter_commands.command(name="route", description="Generate a Route with Drifters included", guild_ids=[int(settings.DISCORD_GUILD_ID)])
    async def route(
        self, ctx,
        from_system=Option(str, "Solar System", autocomplete=search_solar_systems),
        to_system=Option(str, "Solar System", autocomplete=search_solar_systems),
        reserved=Option(bool, "K Space Bookmarked?", default='False', choices=["True", "False"])
    ):
        from_evesolarsystem = EveSolarSystem.objects.get(name=from_system)
        to_evesolarsystem = EveSolarSystem.objects.get(name=to_system)

        embed = Embed(title=f"AA-Drifters: Route {from_evesolarsystem} -> {to_evesolarsystem} Jumps:{route_length(from_evesolarsystem.id, to_evesolarsystem.id, edges=include_drifters_driftercomplexes())}")

        if reserved is True and has_perm(ctx.user.id, "drifters.scout_access"):
            wh_filter = Wormhole.active_private_holes
            use_reserved = True
        else:
            wh_filter = Wormhole.active_public_holes
            use_reserved = False

        for step in route_path_gates(from_evesolarsystem.id, to_evesolarsystem.id, edges=include_drifters_driftercomplexes(use_reserved=use_reserved)):
            step_from, step_to, step_type = step
            if step_type == "drifter_k":
                wh = wh_filter.filter(system_id=step_from, complex=get_complex_name_from_id(step_to)).order_by("-created_at").first()
                system, created = EveSolarSystem.objects.get_or_create(id=step_from)
                embed.add_field(name=step_type, value=f"{system} -> {wh.complex}", inline=False)
            elif step_type == "drifter_w":
                wh = wh_filter.filter(system_id=step_to, complex=get_complex_name_from_id(step_from)).order_by("-created_at").first()
                system, created = EveSolarSystem.objects.get_or_create(id=step_to)
                embed.add_field(name=step_type, value=f"{wh.complex} -> {system}", inline=False)
            elif step_type == "jump_bridge":
                wh = wh_filter.filter(system_id=step_to, complex=get_complex_name_from_id(step_from)).order_by("-created_at").first()
                system, created = EveSolarSystem.objects.get_or_create(id=step_to)
                embed.add_field(name=step_type, value=f"{wh.complex} -> {system}", inline=False)
            elif step_type == "Stargate":
                from_system, created = EveSolarSystem.objects.get_or_create(id=step_from)
                to_system, created = EveSolarSystem.objects.get_or_create(id=step_to)
                embed.add_field(name=step_type, value=f"{from_system} -> {to_system}", inline=True)
            else:
                embed.add_field(name="Unknown", value="Unknown -> Unknown", inline=True)

        return await ctx.respond(embed=embed)


def setup(bot):
    bot.add_cog(Drifters(bot))
