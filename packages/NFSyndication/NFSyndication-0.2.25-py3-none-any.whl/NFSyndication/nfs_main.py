#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
from os.path import abspath, realpath, split, dirname
import collections
from datetime import datetime, timedelta
import time

import jinja2
import json
import logging
import pytz
import shutil
import sys
import logging

from jinja2.exceptions import UndefinedError
from .core import args
from .extras import parseFeedURL, fetch_content, templateContent, process_entry
from .styles import cssTextDecoded

from .__main__ import logFile

#argsFilename = args.filename
standardPath = os.getcwd()

# Get a list of feed URLs
try:
 with open('feeds.txt') as f:
     SUBSCRIPTIONS = list(f)
     print('Loading feeds.txt')
except FileNotFoundError:   # If you don't have 'feeds.txt' in specified path, you can specify one (nfsyndication-src --filename=sample.txt)
 try:
  for documentList in args.filename:
   parent_location = os.getcwd()
   with open(documentList) as f:
     SUBSCRIPTIONS = list(f)
     print("Loading file: {} from '{}'".format(documentList, os.path.join(parent_location)))
 except TypeError:
   raise Exception('NFSyndication [ERROR]: feeds.txt not found. See `nfsyndication-src --help` for more.')

posts = []
outJSONFeed= []

try:
 for url in SUBSCRIPTIONS:
    try:
        feed = parseFeedURL(url)
        blog = feed['feed']['title']
    except KeyError:
        if args.verbose and feed.bozo:
            logging.error("Feed data summary on URL {}".format(url))
            logging.error("Failed command: {} ".format(sys.argv[0:]))
            logging.error("Exception [{bozo_exception}]: {bozo_message}".format(bozo_exception=str(feed.bozo_exception.__class__.__name__), bozo_message=str(feed.bozo_exception)))
            logging.error('Response code is: {}'.format(feed.status))
            if (hasattr(feed.bozo_exception, 'getLineNumber') and hasattr(feed.bozo_exception, 'getMessage')):
                line = feed.bozo_exception.getLineNumber()
                logging.error('Line %d: %s', line, feed.bozo_exception.getMessage())
            logging.error('[NFSyndication] Writing output logs to {}'.format(os.path.join(standardPath, logFile)))    
        raise Exception(f"[{feed.bozo_exception}] (code {feed.status}) \n{(f'Could not fetch URL(s): {url}')}")
        sys.exit(-1)
        continue
    for entry in feed['entries']:
        post = process_entry(entry, blog, comp_field=args.comparator_filter)
        if post:
            posts.append(post)
            outJSONFeed.append(feed)
    try:
     fetch_content(url)
    except:
     raise SystemExit
except NameError:
  pass

if args.outputJSON:
    with open(args.outputJSON, 'w+', encoding='utf8') as outf:
       json.dump(outJSONFeed, outf, ensure_ascii=False, indent=4)
      
  
# Get the template, and drop in the posts
dir_path = os.path.split(os.path.realpath(__file__))[0]

try:
 with open(f'{dir_path}/templates/template.html', encoding='utf8') as f:
    print("\nChecking original template file...")
    template = jinja2.Template(f.read())
 with open(f'output/index.html', 'w', encoding='utf8') as f:
      f.write(template.render(posts=posts, time=datetime.now()))
      print('Successful.')   
 with open("output/style.css", 'w') as f:
    f.write(cssTextDecoded)

except FileNotFoundError:
    template = jinja2.Template(templateContent)
# When done, it converts to HTML
    with open(f'output/index.html', 'w', encoding='utf8') as f:
      f.write(template.render(cssText=cssTextDecoded, posts=posts, time=datetime.now()))
      print('Successful.')
