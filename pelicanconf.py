#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Justin Triplett'
SITENAME = u'Justin Triplett'
SITEURL = ''

PATH = 'content'
OUTPUT_PATH = '/var/www'

TIMEZONE = 'America/Detroit'

DEFAULT_LANG = u'en'

THEME = 'pelican-bootstrap3'
BOOTSTRAP_THEME = 'darkly'

#SITELOGO = 'images/jTrip2_cropped.png'
#SITELOGO_SIZE = 40
#HIDE_SITENAME = True

BANNER = 'images/Transistor_banner.jpg'
BANNER_TITLE_FLAG = False
BANNER_TITLE = 'OMGWTFBBQ!?'
BANNER_SUBTITLE = 'words that are coming out of my finger tips'

REVERSE_CATEGORY_ORDER = True


# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None


# Tag Cloud
DISPLAY_TAGS_INLINE = True


# Blogroll
LINKS = (('i3Detroit', 'https://www.i3detroit.org/'),
         ('The Diablonet', 'http://diablonet.net/'),
         ('Running a Hackerspace','http://runningahackerspace.tumblr.com/'),)
# Social widget
SOCIAL = (('Twitter', 'https://twitter.com/jtrip'),
          ('Google+', 'https://plus.google.com/+JustinTriplett/'),
	  ('LinkedIn','http://www.linkedin.com/pub/justin-triplett/13/387/188/'),
	  ('GitHub','https://github.com/jtrip'),
	  ('Tumblr','http://tumblr.justintriplett.com/'),
	  ('Flickr','https://secure.flickr.com/photos/jtrip/'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
