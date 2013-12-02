#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Arnaldo Russo'
SITENAME = u'Ciclotux'
SITEURL = 'ciclotux.org'

TIMEZONE = 'America/Sao_Paulo'

DEFAULT_LANG = u'pt-br'

# Feed generation is usually not desired when developing
FEED_DOMAIN = SITEURL
FEED_ALL_ATOM = ('feeds/all.atom.xml')
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Blogroll
LINKS =  (('DataSounds', 'www.datasounds.org/'),)

# Social widget
SOCIAL = (('github', 'http://github.com/arnaldorusso/'),)
TWITTER_USERNAME = 'russo_arnaldo'

DEFAULT_PAGINATION = 5
STATIC_PATHS = ['images', 'extra/CNAME']
EXTRA_PATH_METADATA = {'extra/CNAME': {'path': 'CNAME'},}

DISQUS_SITENAME = 'ciclotux'

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

### THEME CHUNCK
#THEME = 'theme/pelican-chunk'

#SITESUBTITLE = 'Pedalando Livre'
#FOOTER_TEXT = 'Another blog'
#DISPLAY_CATEGORIES_ON_MENU = True

## PLUGINS
PLUGIN_PATH = '/home/wuah/ciclotux.org/pelican-plugins'
#PLUGIN_PATH = 'pelican-plugins'
#PLUGINS = ['googleplus_comments']

### THEME FLASKY
#THEME = 'theme/flasky'
THEME = '/home/wuah/ciclotux.org/theme/flasky'
SECTIONS = [('Blog', 'index.html'),
        ('Gaveta', 'archives.html'),
        ('Tags', 'tags.html'),
        ('Projetos', 'pages/projetos.html'),
        ('Talks', 'pages/talks.html'),
        ('eu', 'pages/eu.html')]

DEFAULT_CATEGORY = 'Uncategorized'
DATE_FORMAT = {
    'en': '%d %m %Y'
    }
DEFAULT_DATE_FORMAT = '%d %m %Y'

PDF_GENERATOR = True
REVERSE_CATEGORY_ORDER = False

GITHUB_URL = 'http://github.com/arnaldorusso/'
MAIL_USERNAME = 'arnaldorusso'
MAIL_HOST = 'gmail.com'
