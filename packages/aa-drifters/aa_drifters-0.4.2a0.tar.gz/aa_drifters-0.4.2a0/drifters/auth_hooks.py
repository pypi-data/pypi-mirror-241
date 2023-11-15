from django.utils.translation import gettext_lazy as _

from allianceauth import hooks
from allianceauth.services.hooks import MenuItemHook, UrlHook

from . import urls


@hooks.register('discord_cogs_hook')
def register_cogs():
    return ["drifters.cogs.drifters"]


class DriftersMenuItem(MenuItemHook):
    """This class ensures only authorized users will see the menu entry"""

    def __init__(self):
        # setup menu entry for sidebar
        MenuItemHook.__init__(
            self,
            _("Drifters"),
            "fas fa-car fa-fw",
            "drifters:index",
            navactive=["drifters:"],
        )

    def render(self, request):
        if request.user.has_perm("drifters.basic_access"):
            return MenuItemHook.render(self, request)
        return ""


@hooks.register("menu_item_hook")
def register_menu() -> DriftersMenuItem:
    return DriftersMenuItem()


@hooks.register("url_hook")
def register_urls() -> UrlHook:
    return UrlHook(urls, "drifters", r"^drifters/")
