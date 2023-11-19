import os
import threading
from typing import Optional

import sdnotify

from systemd_watchdog_thread import wdt_logger


class WatchdogThread:
    """"Send watchdog notifies in thread"""

    def __init__(self):
        self.notifier = sdnotify.SystemdNotifier()
        watch_usec = os.environ.get('WATCHDOG_USEC')
        self.wd_timeout = int(watch_usec) / 2_000_000 if watch_usec else 3600
        wdt_logger.info(f'notify interval {self.wd_timeout} seconds')
        self._notified = False
        self.flag = threading.Semaphore(value=0)
        self.thread: Optional[threading.Thread] = None

    def ready(self):
        """Set ready. For type=notifier"""
        self.notifier.notify('READY=1')
        wdt_logger.info("notify sent")

    def notify_dog(self):
        """Send we're okay signal to watchdog"""
        self.notifier.notify('WATCHDOG=1')
        wdt_logger.info("process okay sent")

    def run(self) -> threading.Thread:
        """Send notifications in separate daemon thread"""
        if self.thread and self.thread.is_alive():
            wdt_logger.warning(f"{self.thread.name} already running")
        else:
            self.thread = threading.Thread(target=self._ping, daemon=True, name='sdnotify thread')
            self.thread.start()
        return self.thread

    def finish(self):
        """Send signal for thread to exit. Optional call"""
        self.flag.release()
        wdt_logger.debug("released semaphore")

    def _ping(self):
        """Thread payload to continually send notifies"""
        self.ready()
        while True:
            self.notify_dog()
            try:
                if self.flag.acquire(blocking=True, timeout=self.wd_timeout):
                    wdt_logger.info("Thread exiting")
                    return
            except:
                wdt_logger.exception(f"{self.wd_timeout} sleep")
