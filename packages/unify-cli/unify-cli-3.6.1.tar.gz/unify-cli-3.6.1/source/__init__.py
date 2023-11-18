from ._version import __version__
import logging.config

def start_logging(level):
    try:
        logging.basicConfig(
            format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
            level=level)

        root = logging.getLogger()
        root.debug("loging configuration was loaded")

    except Exception as error:
        print("logging configuration with {0} traces couldn't be loaded: {1}".format(level, error))
