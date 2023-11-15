from typing import Tuple

from drifters.app_settings import DRIFTERS_DRIFTERHOLE_WEIGHT
from drifters.models import Wormhole

# Helper functions for AA Routing


def include_drifters_driftercomplexes(weight: float = DRIFTERS_DRIFTERHOLE_WEIGHT, use_reserved:bool = False) -> list[Tuple]:
    edges = []

    if use_reserved is True:
        wh_filter = Wormhole.active_private_holes
    else:
        wh_filter = Wormhole.active_public_holes

    for complex in Wormhole.Complexes:
        for wh in wh_filter.filter(complex=complex):
            edges.append((
                wh.system.id, wh.complex_id,
                {'p_shortest': weight, 'p_safest': weight, 'p_less_safe': weight, "type": "drifter_k"}))
            edges.append((
                wh.complex_id, wh.system.id,
                {'p_shortest': weight, 'p_safest': weight, 'p_less_safe': weight, "type": "drifter_w"}))
    return edges
