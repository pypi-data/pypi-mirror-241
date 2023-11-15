import logging
import sys

import pandas as pd

from .ordermanager import OrderManager


def algo(hbt, stat):
    pass



def run():
    broker = LiveBroker()

    # Try/except just keeps ctrl-c from printing an ugly stacktrace
    try:
        broker.run_loop()
    except (KeyboardInterrupt, SystemExit):
        sys.exit()

run()
