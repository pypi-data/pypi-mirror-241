import logging

from rich import print

from dbtui.loader import SchemaLoader

logger = logging.getLogger(__name__)


def main():
    logging.basicConfig(level=logging.DEBUG)
    logger.info("dbtui: text user interface to popular databases")

    loader = SchemaLoader(url="")
    schema = loader.load()
    print(schema)

