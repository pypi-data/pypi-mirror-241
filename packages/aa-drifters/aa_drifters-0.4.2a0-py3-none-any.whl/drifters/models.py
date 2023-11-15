from datetime import timedelta

from eveuniverse.models import EveRegion, EveSolarSystem
from solo.models import SingletonModel

from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from drifters.app_settings import DRIFTERS_JOVE_OBSERVATORIES


class General(models.Model):
    """Meta model for app permissions"""

    class Meta:
        managed = False
        default_permissions = ()
        permissions = (
            ("basic_access", "Can view the simple web interface and get read only cogs"),
            ("scout_access", "Can use the management ui and save wormholes via cogs"),
            ("manage_access", "UNUSED"),
        )


class WormholePublicActiveManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(archived=False, reserved=False)


class WormholePrivateActiveManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(archived=False)


class Wormhole(models.Model):

    class Complexes(models.TextChoices):
        """"
        The Various Drifter Complexes that a hole can lead to
        """
        BARBICAN = 'Barbican', _("Barbican")
        CONFLUX = 'Conflux', _("Conflux")
        REDOUBT = 'Redoubt', _("Redoubt")
        SENTINEL = 'Sentinel', _("Sentinel")
        VIDETTE = 'Vidette', _("Vidette")
        THERA = 'Thera', _("Thera")
        TURNUR = "Turnur", _("Turnur")

    class Mass(models.TextChoices):
        """"
        The states of Mass remaining
        """
        FRESH = 'Fresh', _(
            "This wormhole has not yet had its stability significantly disrupted by ships passing through it")  # >50%
        REDUCED = 'Reduced', _(
            "This wormhole has had its stability reduced by ships passing through it, but not to a critical degree yet")  # <50, >10%
        CRIT = 'Critical', _(
            "This wormhole has had its stability critically disrupted by the mass of numerous ships passing through and is on the verge of collapse")  # <10%

    class Lifetime(models.TextChoices):
        """"
        The states of Time Remaining
        """
        FRESH = 'Fresh', _(
            "This wormhole has not yet begun its natural cycle of decay and should last at least another day")   # >24 Hours?
        DECAY = 'Decaying', _(
            "This wormhole is beginning to decay, and probably won't last another day")  # <24h
        EOL = 'EOL', _("This wormhole is reaching the end of its natural lifetime")  # <4h

    system = models.ForeignKey(EveSolarSystem, verbose_name=_("Solar System"), on_delete=models.CASCADE, limit_choices_to={"name__in": DRIFTERS_JOVE_OBSERVATORIES})
    complex = models.CharField(_("Complex"), max_length=50, choices=Complexes.choices)
    mass = models.CharField(_("Mass Remaining"), max_length=50, choices=Mass.choices)
    bookmarked_k = models.BooleanField(_("K Space Bookmarked"))
    bookmarked_w = models.BooleanField(_("W Space Bookmarked"))

    lifetime = models.CharField(_("Lifetime Remaining"), max_length=50, choices=Lifetime.choices)
    eol_changed_at = models.DateTimeField(auto_now=False, auto_now_add=False, blank=True, null=True, help_text="Only set if a user set a hole as EOL")

    created_at = models.DateTimeField(auto_now=False, auto_now_add=True)
    created_by = models.ForeignKey(User, verbose_name=_(
        "Created By User"), on_delete=models.CASCADE, null=True, blank=True, related_name="+")

    updated_at = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated_by = models.ForeignKey(User, verbose_name=_(
        "Update By User"), on_delete=models.CASCADE, null=True, blank=True, related_name="+")

    archived = models.BooleanField(_("Archived"), default=False)
    reserved = models.BooleanField(_("Not Published / Reserved for Fleets and WH Team Usage"), default=False)
    archived_at = models.DateTimeField(blank=True, null=True)
    archived_by = models.ForeignKey(User, verbose_name=_(
        "Archived By User"), on_delete=models.CASCADE, null=True, blank=True, related_name="+")

    active_public_holes = WormholePublicActiveManager()
    active_private_holes = WormholePrivateActiveManager()
    objects = models.Manager()  # Add default manager back in because i made custom ones ^

    class Meta:
        verbose_name = _("Wormhole")
        verbose_name_plural = _("Wormholes")

    def __str__(self):
        return f"{self.system.name} - {self.complex}"

    def set_eol(self, user: User = None) -> bool:
        """
        Set a wormhole as EOL, updating the eol_changed_at timestamp

        :return: Set EOL? False if not set or already EOL
        :rtype: bool
        """
        if self.lifetime == 'Decaying':

            if user is not None:
                self.updated_by = user
                self.updated_at = timezone.now()
                self.eol_changed_at = timezone.now()

            self.lifetime = 'EOL'
            self.save()
            return True
        return False

    def set_archived(self, user: User = None) -> bool:
        """
        Archives a hole, may optionally mark who archive it. if None, System

        :return: Archived? False if not set or already EOL
        :rtype: bool
        """
        self.archived_at = timezone.now()
        if user is not None:
            self.archived_by = user
        else:
            pass
        self.archived = True
        self.save()
        return True

    @property
    def age(self) -> timedelta:
        return timezone.now() - self.created_at

    @property
    def time_since_update(self) -> timedelta:
        return timezone.now() - self.updated_at

    @property
    def time_since_eol(self) -> timedelta:
        return timezone.now() - self.eol_changed_at

    @property
    def formatted_lifetime(self) -> str:
        if self.lifetime in [self.Lifetime.DECAY, self.Lifetime.FRESH]:
            return f"{self.lifetime} {self.age.total_seconds() / timedelta(hours=16).total_seconds():.0%}"
        elif self.eol_changed_at is None and self.lifetime == 'EOL':
            return f"{self.lifetime} {self.age.total_seconds() / timedelta(hours=4).total_seconds():.0%}"
        elif self.eol_changed_at is not None and self.lifetime == 'EOL':
            return f"{self.lifetime} {self.time_since_eol.total_seconds() / timedelta(hours=4).total_seconds():.0%}"
        return "N/A"

    @property
    def formatted_lifetime_motd(self) -> str:
        string = ""
        if self.lifetime in [self.Lifetime.DECAY.value, self.Lifetime.FRESH.value]:
            if self.time_since_update <= timedelta(hours=4):
                string += """<font size="12" color="#ff00ff00">"""
            elif self.time_since_update <= timedelta(hours=8):
                string += """<font size="12" color="#ffffff00">"""
            else:
                string += """<font size="12" color="#ffff0000">"""
            string += f"{self.lifetime} {self.age.total_seconds() / timedelta(hours=16).total_seconds():.0%}</font>"
            return string

        if self.lifetime == self.Lifetime.EOL.value and self.eol_changed_at is None:
            if self.time_since_update <= timedelta(hours=4):
                string += """<font size="12" color="#ff00ff00">"""
            elif self.time_since_update <= timedelta(hours=8):
                string += """<font size="12" color="#ffffff00">"""
            else:
                string += """<font size="12" color="#ffff0000">"""
            string += f"{self.lifetime} {self.age.total_seconds() / timedelta(hours=4).total_seconds():.0%}</font>"
            return string
        else:
            if self.time_since_update <= timedelta(hours=1):
                string += """<font size="12" color="#ff00ff00">"""
            elif self.time_since_update <= timedelta(hours=2):
                string += """<font size="12" color="#ffffff00">"""
            else:
                string += """<font size="12" color="#ffff0000">"""
            string += f"{self.lifetime} {self.time_since_eol.total_seconds() / timedelta(hours=4).total_seconds():.0%}</font>"
            return string

    @property
    def region(self) -> EveRegion:
        return self.system.eve_constellation.eve_region

    @property
    def complex_id(self) -> int:
        if self.complex == 'Sentinel':
            return 31000001
        elif self.complex == 'Barbican':
            return 31000002
        elif self.complex == 'Vidette':
            return 31000003
        elif self.complex == 'Conflux':
            return 31000004
        elif self.complex == 'Thera':
            return 31000005
        elif self.complex == 'Redoubt':
            return 31000006
        return 0


class Clear(models.Model):

    system = models.ForeignKey(EveSolarSystem, verbose_name=_("Solar System"), on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, verbose_name=_(
        "Created By User"), on_delete=models.CASCADE, null=True, blank=True, related_name="+")

    updated_at = models.DateTimeField(auto_now=True)
    updated_by = models.ForeignKey(User, verbose_name=_(
        "Updated By User"), on_delete=models.CASCADE, null=True, blank=True, related_name="+")

    class Meta:
        verbose_name = _("Clear System")
        verbose_name_plural = _("Clear Systems")

    def __str__(self):
        return f"{self.system.name} - CLEAR"

    @property
    def age(self) -> timedelta:
        return self.created_at - timezone.now()

    @property
    def time_since_update(self) -> timedelta:
        return timezone.now() - self.updated_at


class DriftersConfiguration(SingletonModel):
    POI_regions = models.ManyToManyField(EveRegion, verbose_name=_("POI Regions to be highlighted in the Web UI"), related_name="+")
    POI_systems = models.ManyToManyField(EveSolarSystem, verbose_name=_("POI Systems to be highlighted in the Web UI"), related_name="+")
    motd_systems = models.ManyToManyField(EveSolarSystem, verbose_name=_("Systems to be included in the MOTD Generation"), related_name="+")

    def __str__(self):
        return "Drifters Configuration"

    class Meta:
        """
        Meta definitions
        """
        verbose_name = "Drifters Configuration"
        default_permissions = ()
