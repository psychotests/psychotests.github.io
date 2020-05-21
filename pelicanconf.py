#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'PsychoTeam'
SITENAME = 'Psychotests'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Other
## pages
PAGES_URL = "pages/{slug}.html"
PAGE_SAVE_AS = "pages/{slug}.html"

# Blogroll
LINKS = (
    ('Blog', '/blog.html'),
)

# Social widget
SOCIAL = (
    ('github', 'https://github.com/psychotests'),
)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
