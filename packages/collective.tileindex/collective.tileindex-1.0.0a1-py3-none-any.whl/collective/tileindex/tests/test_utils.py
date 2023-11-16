import unittest


class TestUtils(unittest.TestCase):
    """Test our utility functions.

    These should be plain unit tests without layers, so you can execute them
    with one of these lines, depending on your setup:

    * bin/test -u
    * tox -e py311-Plone60 -- -u
    * .tox/py311-Plone60/bin/test -u
    """

    def test_parse_data_tile(self):
        from collective.tileindex.utils import parse_data_tile

        # These are common ones:
        self.assertEqual(
            parse_data_tile("./@@plone.app.standardtiles.html/some-tile-uid"),
            "plone.app.standardtiles.html",
        )
        self.assertEqual(
            parse_data_tile(
                "./@@plone.app.standardtiles.field?field=IDublinCore-title"
            ),
            "plone.app.standardtiles.field",
        )

        # I can imagine some variants that we want to accept:
        self.assertEqual(
            parse_data_tile("./@@example.tile1/some-tile-uid?field=x"),
            "example.tile1",
        )
        self.assertEqual(
            parse_data_tile("./@@example.tile2/"),
            "example.tile2",
        )
        self.assertEqual(
            parse_data_tile("./@@example.tile3"),
            "example.tile3",
        )
        self.assertEqual(
            parse_data_tile("/@@example.tile4"),
            "example.tile4",
        )
        self.assertEqual(
            parse_data_tile("./example.tile5"),
            "example.tile5",
        )

        # If we cannot parse it, try not to fail.
        self.assertIsNone(parse_data_tile("./@@bad.tile1//"))
        self.assertIsNone(parse_data_tile(""))
        self.assertIsNone(parse_data_tile("./"))
        self.assertIsNone(parse_data_tile("@@bad.tile2/"))

    def test_get_tile_types_from_text(self):
        from collective.tileindex.utils import get_tile_types_from_text

        persistent_tile = """
            <div data-tile="./@@plone.app.standardtiles.html/some-tile-uid"></div>"""
        transient_tile = """
            <div data-tile="./@@plone.app.standardtiles.field?field=IDublinCore-title">
            </div>"""
        self.assertEqual(
            get_tile_types_from_text(persistent_tile),
            {"plone.app.standardtiles.html"},
        )
        self.assertEqual(
            get_tile_types_from_text(transient_tile),
            {"plone.app.standardtiles.field"},
        )

        # get_tile_types_from_text returns a set.  Let's sort this to make it easier to compare.

        def get_tiles(content):
            return sorted(get_tile_types_from_text(content))

        self.assertEqual(
            get_tiles(persistent_tile),
            ["plone.app.standardtiles.html"],
        )
        self.assertEqual(
            get_tiles(transient_tile),
            ["plone.app.standardtiles.field"],
        )
        self.assertEqual(
            get_tiles(persistent_tile + transient_tile),
            [
                "plone.app.standardtiles.field",
                "plone.app.standardtiles.html",
            ],
        )
        self.assertEqual(
            get_tiles(persistent_tile * 10),
            [
                "plone.app.standardtiles.html",
            ],
        )
        # I have a doubt about which beautifulsoup parser we should use.
        # Some parsers fail on non-closing tags.  So try it.
        self.assertEqual(
            get_tiles(persistent_tile + '<br><img src="me.jpeg.">' + transient_tile),
            [
                "plone.app.standardtiles.field",
                "plone.app.standardtiles.html",
            ],
        )
