# coding=utf-8 
__version__ = '0.1.2'

import logging

logging.basicConfig()
logger = logging.getLogger('dt-foobar')
logger.setLevel(logging.DEBUG)

logger.info('duckietown_foobar %s' % __version__)

from .algo import *

