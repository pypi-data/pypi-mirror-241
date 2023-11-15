from django.contrib import admin

from allianceauth.services.hooks import get_extension_logger

from .models import Clear, DriftersConfiguration, Wormhole

logger = get_extension_logger(__name__)


@admin.register(Wormhole)
class WormholeAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'mass', 'lifetime']
    ist_filter = ['mass', 'lifetime', 'bookmarked_k', 'bookmarked_w', 'archived']


@admin.register(Clear)
class ClearAdmin(admin.ModelAdmin):
    list_display = ['__str__',]


@admin.register(DriftersConfiguration)
class DriftersConfigurationAdmin(admin.ModelAdmin):
    list_display = ['id',]
    filter_horizontal = [
        "POI_regions",
        "POI_systems",
        "motd_systems"]
