
import logging
import importlib.metadata
wdt_logger = logging.getLogger('systemd-watchdog-thread')

__version__ = importlib.metadata.version('systemd-watchdog-thread')
from .watchdogthread import WatchdogThread

