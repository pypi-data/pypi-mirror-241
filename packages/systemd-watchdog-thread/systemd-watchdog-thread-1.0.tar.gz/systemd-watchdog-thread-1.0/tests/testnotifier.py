#!/usr/bin/env python3
import argparse
import logging
import os
import time

from systemd_watchdog_thread import wdt_logger,WatchdogThread, __version__

print(f"Version {__version__}")

def main():
    logging.basicConfig()
    parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('-l', '--loglevel', default='WARN', help="Python logging level")
    parser.add_argument('--usec',type=int,help="Set micro-seconds" )
    parser.add_argument('--sleep',type=int,default=5,help="Time of main run in seconds")
    parser.add_argument('--exit',action='store_true',help="Test exit")

    args = parser.parse_args()
    if args.usec:
        os.environ['WATCHDOG_USEC'] = str(args.usec)

    wdt_logger.setLevel(getattr(logging,args.loglevel))
    wdt = WatchdogThread()
    t = wdt.run()
    t2  = wdt.run()
    assert t is t2
    assert t.is_alive()
    time.sleep(args.sleep)
    if args.exit:
        wdt.finish()
        for i in range(20):
            while t.is_alive():
                print("waiting for thread to exit")
                time.sleep(1)
        assert not t.is_alive()

    print("test complete")

if __name__ == "__main__":
    main()
