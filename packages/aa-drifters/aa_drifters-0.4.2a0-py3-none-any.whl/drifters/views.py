from eveuniverse.models.universe_2 import EveRegion, EveSolarSystem
from routing.routing import route_length, systems_range

from django.contrib.auth.decorators import login_required, permission_required
from django.forms import modelformset_factory
from django.http import HttpResponse
from django.shortcuts import render
from django.template.loader import render_to_string
from django.utils import timezone

from allianceauth.services.hooks import get_extension_logger

from drifters.app_settings import (
    DRIFTERS_BOOKMARK_FOLDER_ID, DRIFTERS_BOOKMARK_FOLDER_NAME,
    DRIFTERS_JOVE_OBSERVATORIES, DRIFTERS_MOTD_CHANNEL_LINK,
    DRIFTERS_MOTD_CHANNEL_NAME, DRIFTERS_MOTD_SYSTEM_SEARCH_RANGE,
)
from drifters.forms import WormholeForm
from drifters.models import DriftersConfiguration, Wormhole

logger = get_extension_logger(__name__)


def render_complex(request, complex: Wormhole.Complexes) -> str:
    context = {
        "complex": complex,
        "wormholes": Wormhole.active_public_holes.filter(complex=complex),
        "poi_regions": DriftersConfiguration.get_solo().POI_regions.all(),
        "poi_systems": DriftersConfiguration.get_solo().POI_systems.all(),
    }
    return render_to_string("drifters/blocks/complex.html", context, request)


@login_required
@permission_required("drifters.basic_access")
def index(request) -> HttpResponse:
    context = {'complex_renders': []}
    for complex in Wormhole.Complexes:
        context['complex_renders'].append(render_complex(request, complex))
    return render(request, "drifters/index.html", context)


def generate_channel_motd_1() -> str:
    # Generate an ingame channel MOTD with links as needed
    return f"""<font size="13" color="#ff6868e1"><a href="{DRIFTERS_MOTD_CHANNEL_LINK}">{DRIFTERS_MOTD_CHANNEL_NAME}</a></font><font size="13" color="#bfffffff"> (this service will not be available 24/7)<br></font>
<font size="10" color="#ffff0000">--TRAVELs WITH THE WH METRO ONLY AT YOUR OWN RISK!--<br></font>
<font size="12" color="#ffffffff"><b><u>Instructions & Safety Advice:</b></u>
- online & connect to</font><font size="12" color="#ff00a99d"> <a href="bookmarkFolder:{DRIFTERS_BOOKMARK_FOLDER_ID}">{DRIFTERS_BOOKMARK_FOLDER_NAME}</a></font><font size="12" color="#ffffffff">
- burn to entry/exit location and jump through the correct wormhole!<br>- small & fast travel ships with MWD,MJD and cloak are highly recommended!
- Drifter Battleship spawn on the outside of the wormholes and you need to be careful and avoid them at all cost!
- Check the time since last update at the bottom!<br></font>
<font size="10" color="#ff00ff00">Less than 4h, Reliable</font>
<font size="10" color="#ffffff00">More than 4h, Possible/Unconfirmed</font>
<font size="10" color="#ffff0000">More Than 8H Ago, Less Likely<br></font>
<font size="10" color="#ffffffff">% is remaining theoretical max life</font>
<font size="12" color="#ffffffff"><b><u>Active Metro Lines:</b></u></font>
"""


def generate_channel_motd_2() -> str:
    # Generate an ingame channel MOTD with links as needed

    motd_lines = ""

    for complex in Wormhole.Complexes:
        # These three reset to ensure we only post a Complex with >1 System with >= 1 Hole
        motd_lines_per_complex = ""
        valid_hole_count = 0
        valid_system_count = 0
        if Wormhole.active_public_holes.filter(complex=complex).exists():  # Exit early if we have no Wormholes belonging to a Complex
            motd_lines_per_complex += f"""<br><font size="12" color="#ffffffff"><b>{complex}</b></font>"""
            for motd_system in DriftersConfiguration.get_solo().motd_systems.all():
                # Reset here to only add a System with >0 Holes
                motd_lines_per_complex_per_system = ""
                valid_hole_count = 0
                motd_lines_per_complex_per_system += f"""<br><font size="12" color="#ffffffff"><b>{motd_system}</b><br></font>"""
                for hole in Wormhole.active_public_holes.filter(system__in=systems_range(motd_system.id, DRIFTERS_MOTD_SYSTEM_SEARCH_RANGE, include_source=True), complex=complex):
                    motd_lines_per_complex_per_system += f"""<font size="12" color="#ffd98d00"><a href="showinfo:5//{hole.system.id}">{hole.system}</a></font><font size="12" color="#ffffffff"> {route_length(motd_system.id, hole.system.id)}J</font> {hole.formatted_lifetime_motd}<br>"""
                    valid_hole_count += 1
                if valid_hole_count >= 1:
                    motd_lines_per_complex += motd_lines_per_complex_per_system
                    valid_system_count += 1

        if valid_system_count > 1:
            motd_lines += motd_lines_per_complex

    return f"""{ motd_lines }<font size="12" color="#bfffffff"><i>Updated {timezone.now()}<br></i></font>"""


@login_required
@permission_required("drifters.basic_access")
def motd(request) -> HttpResponse:
    context = {
        'motd_1': generate_channel_motd_1(),
        'motd_2': generate_channel_motd_2()
    }

    return render(request, "drifters/motd.html", context)


def scout_region_render(request, region: EveRegion) -> str:
    four_hours_ago = timezone.datetime.now() - timezone.timedelta(hours=4)
    eight_hours_ago = timezone.datetime.now() - timezone.timedelta(hours=8)
    twelve_hours_ago = timezone.datetime.now() - timezone.timedelta(hours=12)
    count = Wormhole.active_private_holes.filter(system__eve_constellation__eve_region=region).count()
    update_older_than_4h = Wormhole.active_private_holes.filter(system__eve_constellation__eve_region=region).exclude(updated_at__range=(four_hours_ago,timezone.now())).count()
    update_older_than_8h = Wormhole.active_private_holes.filter(system__eve_constellation__eve_region=region).exclude(updated_at__range=(eight_hours_ago,timezone.now())).count()
    update_older_than_12h = Wormhole.active_private_holes.filter(system__eve_constellation__eve_region=region).exclude(updated_at__range=(twelve_hours_ago,timezone.now())).count()

    context = {
        'region': region,
        'count': count,
        'update_older_than_4h': update_older_than_4h,
        'update_older_than_8h': update_older_than_8h,
        'update_older_than_12h': update_older_than_12h,
    }
    return render_to_string("drifters/scout/blocks/scout_region.html", context, request)


def scout_complex_render(request, complex: Wormhole.Complexes) -> str:

    four_hours_ago = timezone.datetime.now() - timezone.timedelta(hours=4)
    eight_hours_ago = timezone.datetime.now() - timezone.timedelta(hours=8)
    twelve_hours_ago = timezone.datetime.now() - timezone.timedelta(hours=12)
    count = Wormhole.active_private_holes.filter(complex=complex).count()
    update_older_than_4h = Wormhole.active_private_holes.filter(complex=complex,).exclude(updated_at__range=(four_hours_ago,timezone.now())).count()
    update_older_than_8h = Wormhole.active_private_holes.filter(complex=complex,).exclude(updated_at__range=(eight_hours_ago,timezone.now())).count()
    update_older_than_12h = Wormhole.active_private_holes.filter(complex=complex,).exclude(updated_at__range=(twelve_hours_ago,timezone.now())).count()
    context = {
        'complex': complex,
        'count': count,
        'update_older_than_4h': update_older_than_4h,
        'update_older_than_8h': update_older_than_8h,
        'update_older_than_12h': update_older_than_12h,
    }
    return render_to_string("drifters/scout/blocks/scout_complex.html", context, request)


@login_required
@permission_required("drifters.scout_access")
def scout(request) -> HttpResponse:
    context = {
        'scout_region_renders': [],
        "scout_complex_renders": []}

    for region in EveRegion.objects.filter(id__lt="11000000"):
        context['scout_region_renders'].append(scout_region_render(request, region))

    for complex in Wormhole.Complexes:
        context['scout_complex_renders'].append(scout_complex_render(request, complex))

    return render(request, "drifters/scout/index.html", context)


def scout_system_render(request, system: EveSolarSystem) -> str:
    WormholeFormSet = modelformset_factory(Wormhole, fields=["system", "complex", "mass", "lifetime", "bookmarked_k", "bookmarked_w"], extra=1, form=WormholeForm)
    formset = WormholeFormSet(queryset=Wormhole.active_private_holes.filter(system=system), initial=[{"system": system}], prefix=system.id, form_kwargs={'system': system})

    context = {
        'system': system,
        'formset': formset
    }
    return render_to_string("drifters/scout/blocks/scout_system.html", context, request)


@login_required
@permission_required("drifters.scout_access")
def scout_region(request, region_id) -> HttpResponse:
    region = EveRegion.objects.get(id=region_id)
    context = {'scout_system_renders': []}

    WormholeFormSet = modelformset_factory(Wormhole, fields=["system", "complex", "mass", "lifetime", "bookmarked_k", "bookmarked_w"], extra=1, form=WormholeForm)

    if request.method == "POST":
        for system in EveSolarSystem.objects.filter(eve_constellation__eve_region=region, name__in=DRIFTERS_JOVE_OBSERVATORIES):
            formset = WormholeFormSet(request.POST, queryset=Wormhole.active_private_holes.filter(system=system), initial=[{"system": system}], prefix=system.id, form_kwargs={'region': region})
            if formset.is_valid():
                formset.save()

    for system in EveSolarSystem.objects.filter(eve_constellation__eve_region=region, name__in=DRIFTERS_JOVE_OBSERVATORIES):
        context['scout_system_renders'].append(scout_system_render(request, system))
    return render(request, "drifters/scout/scout_region.html", context)


@login_required
@permission_required("drifters.scout_access")
def scout_complex(request, complex) -> HttpResponse:
    WormholeFormSet = modelformset_factory(Wormhole, fields=["system", "complex", "mass", "lifetime", "bookmarked_k", "bookmarked_w"], extra=1, form=WormholeForm)

    if request.method == "POST":
        formset = WormholeFormSet(request.POST, queryset=Wormhole.active_private_holes.filter(complex=complex), initial=[{"complex": complex}])
        if formset.is_valid():
            formset.save()
    else:
        formset = WormholeFormSet(queryset=Wormhole.active_private_holes.filter(complex=complex), initial=[{"complex": complex}])

    context = {
        'complex': complex,
        'formset': formset
    }
    return render(request, "drifters/scout/scout_complex.html", context)
