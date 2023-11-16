from collective.tileindex.utils import get_tile_types_from_obj
from functools import cached_property
from Products.Five.browser import BrowserView


class TileTypesView(BrowserView):
    @cached_property
    def tile_types(self):
        tiles = get_tile_types_from_obj(self.context)
        if not tiles:
            return
        return sorted(tiles)
