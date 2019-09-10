#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
import sys

AUTHOR = 'DM'
SITENAME = 'Standards'
SITEURL = 'https://standardrepertoire.com'

if '8082' in sys.argv: # Hacky, but == devserver
    SITEURL = 'http://localhost:8082'

PATH = 'content'

TIMEZONE = 'Europe/London'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
THEME = 'themes/rep'
DISPLAY_CATEGORIES_ON_MENU = False

PLUGIN_PATHS = [
    "plugins",
    "/Users/david/src/proj/pelican-plugins"
]

PLUGINS = [
    "metatags",
    "jinja2content",
    "sitemap"
]

SITEMAP = {
    'format': 'xml',
}
