from functools import cached_property
from plone import api
from Products.Five.browser import BrowserView


class TileTypesOverview(BrowserView):
    @cached_property
    def tile_index(self):
        catalog = api.portal.get_tool(name="portal_catalog")
        return catalog.Indexes.get("tile_types")

    @cached_property
    def numObjects(self):
        return self.tile_index.numObjects()

    @cached_property
    def alphabetical(self):
        return sorted(self.tile_index.uniqueValues())

    @cached_property
    def numerical(self):
        items = sorted(
            [(len(value), key) for (key, value) in self.tile_index.items()],
            reverse=True,
        )
        result = []
        for item in items:
            result.append({"number": item[0], "tile": item[1]})
        return result

    @cached_property
    def search_results(self):
        tile = self.request.get("tile")
        if not tile:
            return
        return api.content.find(tile_types=tile)
