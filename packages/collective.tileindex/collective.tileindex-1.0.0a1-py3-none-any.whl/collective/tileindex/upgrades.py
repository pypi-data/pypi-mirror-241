from Products.CMFCore.utils import getToolByName

import logging


logger = logging.getLogger(__name__)


def add_indexes(context):
    """Add indexes."""
    catalog = getToolByName(context, "portal_catalog")
    indexes = catalog.indexes()

    wanted_indexes = [
        ("tile_types", "KeywordIndex"),
    ]

    indexables = []
    for index_name, index_type in wanted_indexes:
        if index_name not in indexes:
            catalog.addIndex(index_name, index_type)
            indexables.append(index_name)
            logger.info("Added {} for {}.".format(index_type, index_name))
    if len(indexables) > 0:
        logger.info("Indexing new indexes %s.", ", ".join(indexables))
        # I was pretty sure this also updated the catalog brains, but
        # it does not...
        catalog.manage_reindexIndex(ids=indexables)
