# -*- coding: utf-8 -*-
from lektor.pluginsystem import Plugin
from werkzeug.urls import url_parse
from markupsafe import escape

NOFOLLOW_LINK_PREFIX = '!'

class NofollowMixin(object):
    def link(self, link, title, text):
        nofollow = link.startswith(NOFOLLOW_LINK_PREFIX)
        link = link.lstrip(NOFOLLOW_LINK_PREFIX)
        
        if self.record is not None:
            url = url_parse(link)
            if not url.scheme:
                link = self.record.url_to('!' + link,
                                          base_url=get_ctx().base_url)
        link = escape(link)
        if not title:
            if nofollow:
                return '<a href="%s" rel="nofollow">%s</a>' % (link, text) 
            else:
                return '<a href="%s">%s</a>' % (link, text)
        title = escape(title)
        if nofollow:
            return '<a href="%s" title="%s" rel="nofollow">%s</a>' % (link, title, text)
        else:
            return '<a href="%s" title="%s">%s</a>' % (link, title, text)

class NofollowPlugin(Plugin):
    name = u'nofollow'
    description = u'Adds nofollow links to markdown'

    def on_markdown_config(self, config, **extra):
        config.renderer_mixins.append(NofollowMixin)