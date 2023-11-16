from collective.tileindex.utils import get_tile_types_from_obj
from plone.app.blocks.layoutbehavior import ILayoutBehaviorAdaptable
from plone.indexer.decorator import indexer


@indexer(ILayoutBehaviorAdaptable)
def tile_types(obj):
    """Calculate and return the value for the indexer"""
    return get_tile_types_from_obj(obj)
