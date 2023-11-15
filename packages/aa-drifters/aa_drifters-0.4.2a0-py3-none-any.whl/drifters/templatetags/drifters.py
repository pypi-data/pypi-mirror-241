from eveuniverse.models.universe_2 import EveSolarSystem
from routing.routing import systems_range

from django import template

from drifters.app_settings import DRIFTERS_POI_SEARCH_RANGE
from drifters.models import Wormhole

register = template.Library()


@register.simple_tag()
def find_closest_holes(system: EveSolarSystem, complex: Wormhole.Complexes):
    holes = Wormhole.active_public_holes.filter(system__in=systems_range(system.id, DRIFTERS_POI_SEARCH_RANGE, include_source=True), complex=complex)
    if holes.count() == 0:
        return None
    else:
        return holes
