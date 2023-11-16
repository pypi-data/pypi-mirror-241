from bs4 import BeautifulSoup
from plone.app.blocks.layoutbehavior import ILayoutAware


try:
    from plone.base.utils import base_hasattr
except ImportError:
    # BBB Plone 5.2
    from Products.CMFPlone.utils import base_hasattr


def parse_data_tile(dt):
    """Parse a data-tile attribute.

    Persistent tiles look like this:

        ./@@plone.app.standardtiles.html/some-tile-uid

    Transient tiles look like this:

        ./@@plone.app.standardtiles.field?field=IDublinCore-title

    We return a string like this, so without the "@@":

        plone.app.standardtiles.html
    """
    items = dt.split("/")
    if len(items) == 3:
        tile = items[1]
    elif len(items) == 2:
        tile = items[1].split("?")[0]
    else:
        return
    return tile.strip("@") or None


def get_tile_types_from_text(text):
    soup = BeautifulSoup(text, features="lxml")
    # We search for content like this.
    # Persistent tile:
    # <div data-tile="./@@plone.app.standardtiles.html/some-tile-uid"></div>
    # Transient tile:
    # <div data-tile="./@@plone.app.standardtiles.field?field=IDublinCore-title"></div>
    divs = soup.find_all(attrs={"data-tile": True})
    tile_types = set()
    for dt in [d["data-tile"] for d in divs]:
        tile = parse_data_tile(dt)
        if tile:
            tile_types.add(tile)
    return tile_types


def get_tile_types_from_obj(obj):
    if not base_hasattr(obj, "__annotations__"):
        return
    if obj.getProperty("layout", "") != "layout_view":
        return

    # Get the tiles from the content layout.
    layout = ILayoutAware(obj)
    content_layout = layout.content_layout()
    if not content_layout:
        return
    return get_tile_types_from_text(content_layout)
