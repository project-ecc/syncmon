#!/usr/bin/env python3
# coding: UTF-8

import datetime
import settings
import argparse
import pathlib
import logging
import signal
import sys

#from slickrpc import Proxy
#from slickrpc import exc

################################################################################
## SyncMonApp class ############################################################
################################################################################

class SyncMonApp:

	def __init__(self):

		pass

	############################################################################

	def run(self):

		pass

################################################################################

def terminate(signalNumber, frame):

	logging.info('%s received - terminating' % signal.Signals(signalNumber).name)

	raise urwid.ExitMainLoop()

################################################################################
### Main program ###############################################################
################################################################################

def main():

	if sys.version_info[0] < 3:

		raise 'Use Python 3'

	pathlib.Path('data').mkdir(parents=True, exist_ok=True)

	logging.basicConfig(filename = 'data/{:%Y-%m-%d}.csv'.format(datetime.datetime.now()),
						filemode = 'a',
						level    = logging.INFO,
						format   = '%(asctime)s - %(levelname)s : %(message)s',
						datefmt  = '%d/%m/%Y %H:%M:%S')

	logging.info('STARTUP')

	signal.signal(signal.SIGINT,  terminate)  # keyboard interrupt ^C
	signal.signal(signal.SIGTERM, terminate)  # kill [default -15]

	argparser = argparse.ArgumentParser(description='Simply blockchain sync monitor')

	#argparser.add_argument('-n', '--name'  , action='store', help='nickname    (local)' , type=str, default = ''       , required=True)
	#argparser.add_argument('-o', '--other' , action='store', help='nickname    (remote)', type=str, default = '[other]', required=False)
	#argparser.add_argument('-t', '--tag'   , action='store', help='routing tag (remote)', type=str, default = ''       , required=True)

	command_line_args = argparser.parse_args()

	logging.info('Arguments %s', vars(command_line_args))

	app = SyncMonApp()

	app.run()

	logging.info('SHUTDOWN')

################################################################################

if __name__ == '__main__':

	main()

################################################################################
