#!/usr/bin/env python

from sys import argv
from os import makedirs, unlink, sep
from os.path import dirname, exists, isdir, splitext
#from string import replace, find, lower
from htmllib import HTMLParser
from urllib import urlretrieve
from urlparse import urlparse, urljoin
#from formatter import DumbWriter, AbstractFormatter
#from cStringIO import StringIO
