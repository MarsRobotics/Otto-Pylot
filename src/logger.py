##
# Logger
# TODO: talk about logger here
# The logger's name is a period-separated hierarchical value. eg. "core.logger" follows the file structure
##
__author__ = 'Taylor Nightingale'

import logging

LOGGING_FILE_NAME   =  'otto-pylot-%(asctime)s.log'
LOGGING_FORMAT      =  '%(levelname)s [%(asctime)s]: %(message)s' ## ex. WARN [12/12/2010 11:46:36 AM]: I moved.
LOGGING_DATE_FORMAT =  '%m/%d/%Y-%I:%M:%S%p' ## ex. 12/12/2010 11:46:36 AM
LOGGING_FILE_MODE   =  'w' ## write only
LOGGING_BASE_LEVEL  =  logging.WARN

def setUp():
    logging.basicConfig(filename =  LOGGING_FILE_NAME,
                        format   =  LOGGING_FORMAT,
                        datefmt  =  LOGGING_DATE_FORMAT,
                        filemode =  LOGGING_FILE_MODE,
                        level    =  LOGGING_BASE_LEVEL
                        )

## Testing stuff
setUp()
logging.warn("")




