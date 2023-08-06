#!/usr/bin/python 
# -*- coding: utf-8 -*-

# This is a set of scripts for aggregating RSS feeds as originally written as "Simpler Syndication" by Dr. Drang some years ago.
# This is NFSyndication's entire file.
# This file is used to proceed initialization.

import argparse
import sys
import logging

from .extras import process_entry, fetch_content
from .config import GetFeedDataPerConfiguration, init

__version_info__ = (0,2,25)
__version__ = '.'.join(map(str,__version_info__))

__base_path__ = 'feeds.txt'

