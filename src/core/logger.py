##
# Logger
#
# To use this class call setUp() only once at the beginning of program
# execution. Some example code can be found at the bottom of the file.
#
# The logger can log DEBUG, INFO, WARN, ERROR, and CRITICAL messages through
# functions of the same (lower case) name. All messages will be printed to
# the log file, but only INFO, WARN, ERROR, and CRITICAL will be printed to the
# console. The root logger can be accessed through a method call on logger
# (e.g. logger.debug("...")).
#
# Your own logger should be used for each file to denote where the logs come from.
# To begin this process, import logging. NOTE: logger.py need not be imported unless
# you are running startup. The logs should have proper naming when initializing.
# A log for file transport/main should be named "transport.main". The method of creating
# a logger is as follows:
#
#       myLogger = logging.getLogger('transport.main')
#
# The logger can then be used as above (e.g. myLogger.debug("..")).
#
# File logs are in the format:
# 2014/10/22 07:19:45 root         INFO     Booting up...
# 2014/10/22 07:22:34 command.main DEBUG    I just can't do it cap'n. I just don't have the power.
#
# Console logs are in the format:
# root        : INFO     Booting up...
# robot.core  : WARNING  I will probably lose power soon.
##
__author__ = 'Taylor Nightingale'

import logging
import datetime
import os

##
# Sets up the base logger. This method should only be called once per program
# execution.
#
# NOTE: we could add a param to append a name to the log file
##
def setUp():
    ## Constants ##
    LOGGING_FILE_NAME = os.path.dirname(__file__) + '/../../logs/otto-pylot-' + datetime.datetime.today().strftime('%Y-%m-%d-%I:%M:%S') + '.log'
    LOGGING_FORMAT = '%(asctime)s %(name)-12s %(levelname)-8s - %(message)s'
    LOGGING_DATE_FORMAT = '%Y/%m/%d %I:%M:%S %p'
    CONSOLE_FORMAT = '%(name)-12s: %(levelname)-8s %(message)s'
    LOGGING_FILE_MODE = 'a'  # append

    # set the default options for the logger
    logging.basicConfig(
        level=logging.DEBUG,
        format=LOGGING_FORMAT,
        datefmt=LOGGING_DATE_FORMAT,
        filename=LOGGING_FILE_NAME,
        filemode=LOGGING_FILE_MODE)

    # define a Handler which writes INFO messages or higher to the sys.stderr
    console = logging.StreamHandler()
    console.setLevel(logging.INFO)

    # set a format for console use
    formatter = logging.Formatter(CONSOLE_FORMAT)

    # tell the handler to use the console format
    console.setFormatter(formatter)

    # add the handler to the root logger
    logging.getLogger('').addHandler(console)


## Example Code
# logging.debug('debug message')
# logging.info('info message')
# logging.warn('warn message')
# logging.error('error message')
# logging.critical('critical message')
# LOG = logging.getLogger('command.main')
# LOG.info("starting up...")