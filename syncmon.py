#!/usr/bin/env python3
# coding: UTF-8

import datetime
import settings
import argparse
import pathlib
import logging
import signal
import time
import sys

from slickrpc import Proxy
from slickrpc import exc

proxy = Proxy('http://%s:%s@%s' % (settings.rpc_user, settings.rpc_pass, settings.rpc_address))

################################################################################
## SyncMonApp class ############################################################
################################################################################

class SyncMonApp:

	def __init__(self):

		pass

	############################################################################

	def run(self):

		while True:

			info = proxy.getinfo()

			csv = "%d,%d,%d" % (info['connections'], info['headers'], info['blocks'])

			logging.info(csv)

			time.sleep(60)

################################################################################

def terminate(signalNumber, frame):

	sys.exit()

################################################################################
### Main program ###############################################################
################################################################################

def main():

	if sys.version_info[0] < 3:

		raise 'Use Python 3'

	pathlib.Path(settings.coin_symbol).mkdir(parents=True, exist_ok=True)

	logging.basicConfig(filename = settings.coin_symbol + '/{:%Y-%m-%d}.csv'.format(datetime.datetime.now()),
						filemode = 'w',
						level    = logging.INFO,
						format   = '%(asctime)s,%(message)s',
						datefmt  = '%d/%m/%Y %H:%M:%S')

	signal.signal(signal.SIGINT,  terminate)  # keyboard interrupt ^C
	signal.signal(signal.SIGTERM, terminate)  # kill [default -15]

	argparser = argparse.ArgumentParser(description='Simple blockchain sync monitor')

	command_line_args = argparser.parse_args()

	#logging.info('Arguments %s', vars(command_line_args))

	app = SyncMonApp()

	app.run()

################################################################################

if __name__ == '__main__':

	main()

################################################################################
