#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'JIN Lin'
SITENAME = u'JL-Blog | No Bullshit'
SITEURL = 'http://linnus.net'

TIMEZONE = 'Singapore'

DEFAULT_LANG = u'en'

TYPOGRIFY = True

RELATIVE_URLS = True

DEFAULT_PAGINATION = 7

#URL settings

DIRECT_TEMPLATES = ['index','archives','categories','tags']

ARTICLE_URL = 'posts/{date:%Y}/{date:%b}/{date:%d}/{slug}/'
ARTICLE_SAVE_AS = 'posts/{date:%Y}/{date:%b}/{date:%d}/{slug}/index.html'
MONTH_ARCHIVE_SAVE_AS = 'archives/{date:%Y}/{date:%m}/index.html'
YEAR_ARCHIVE_SAVE_AS = 'archives/{date:%Y}/index.html'
PAGE_URL = 'pages/{slug}/'
PAGE_SAVE_AS = 'pages/{slug}/index.html'

#THEME
THEME = 'themes/theme-jakevdp'

STATIC_PATHS = ['images','pages', 'extra/CNAME']

EXTRA_PATH_METADATA = {'extra/CNAME': {'path': 'CNAME'},}

#plug-ins

PLUGIN_PATHS = ['./plugins', './plugins/pelican-plugins']
PLUGINS = ['render_math','sitemap', 'liquid_tags.img','better_codeblock_line_numbering','liquid_tags.youtube','liquid_tags.img','ipynb.liquid','related_posts','clean_summary']

MARKUP = ('md', 'ipynb')

#sitemap
SITEMAP = {
    "format": "xml",
    "priorities": {
        "articles": 0.5,
        "indexes": 0.5,
        "pages": 0.5,
    },
    "changefreqs": {
        "articles": "daily",
        "indexes": "daily",
        "pages": "monthly",
    }
}
#related posts
RELATED_POSTS_MAX = 5

ABOUT_PAGE = '/pages/about.html'
SHOW_ARCHIVES = True

ENABLE_MATHJAX = True

#clean summary 
CLEAN_SUMMARY_MAXIMUM = 0
#CLEAN_SUMMARY_MINIMUM_ONE = False


#md-highlight
MD_EXTENSIONS = ['codehilite(css_class=highlight,linenums=False)','extra', 'toc(permalink=true)']

#SEO SITE DESCRIPTION
SITE_DESCRIPTION = u'My name is JIN Lin(金林). My interest: Python for data analyis;biomedicl research;reading;design;running;more.You can check out anytime.'

DISQUS_SITENAME = 'linnus'
GOOGLE_ANALYTICS = 'UA-64765479-1'

#ignore files 
IGNORE_FILES = ['.DS_Store', '.DS_store']

# Feed generation is usually not desired when developing

#FEED_ATOM = 'feeds/atom.xml'
#FEED_RSS = 'feeds/rss.xml'
#TAG_FEED_ATOM = 'feeds/tags/%s.atom.xml'

# Blogroll
#LINKS = (('Zhihu', 'http://www.zhihu.com/people/forrest-jing'),)
        # ('Python.org', 'http://python.org/'),)
#socoial profile lable
#SOCIAL_PROFILE_LABEL = u'StayInTouch'
# Social widget

#SOCIAL = (('Email','jinlinnus@gmail.com'),)
#            ('Github','http://github.com/danceofdragon')
#            ,('Linkedin','https://www.linkedin.com/profile/view?id=144875458&trk=hp-identity-name'),)
#          (('You can add links in your config file', '#'),
#          ('Another social link', '#'),)