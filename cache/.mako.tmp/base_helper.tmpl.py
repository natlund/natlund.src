# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1463693524.0921357
_enable_loop = True
_template_filename = 'themes/lanyon/templates/base_helper.tmpl'
_template_uri = 'base_helper.tmpl'
_source_encoding = 'utf-8'
_exports = ['late_load_js', 'html_feedlinks', 'html_stylesheets', 'html_headstart', 'html_translations']


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        __M_writer = context.writer()
        __M_writer('\n')
        __M_writer('\n\n')
        __M_writer('\n\n')
        __M_writer('\n\n')
        __M_writer('\n\n')
        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_late_load_js(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        social_buttons_code = context.get('social_buttons_code', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n    ')
        __M_writer(str(social_buttons_code))
        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_html_feedlinks(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        len = context.get('len', UNDEFINED)
        rss_link = context.get('rss_link', UNDEFINED)
        generate_rss = context.get('generate_rss', UNDEFINED)
        _link = context.get('_link', UNDEFINED)
        translations = context.get('translations', UNDEFINED)
        generate_atom = context.get('generate_atom', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n')
        if rss_link:
            __M_writer('        ')
            __M_writer(str(rss_link))
            __M_writer('\n')
        elif generate_rss:
            if len(translations) > 1:
                for language in translations:
                    __M_writer('                <link rel="alternate" type="application/rss+xml" title="RSS (')
                    __M_writer(str(language))
                    __M_writer(')" href="')
                    __M_writer(str(_link('rss', None, language)))
                    __M_writer('">\n')
            else:
                __M_writer('            <link rel="alternate" type="application/rss+xml" title="RSS" href="')
                __M_writer(str(_link('rss', None)))
                __M_writer('">\n')
        if generate_atom:
            if len(translations) > 1:
                for language in translations:
                    __M_writer('                <link rel="alternate" type="application/atom+xml" title="Atom (')
                    __M_writer(str(language))
                    __M_writer(')" href="')
                    __M_writer(str(_link('index_atom', None, language)))
                    __M_writer('">\n')
            else:
                __M_writer('            <link rel="alternate" type="application/atom+xml" title="Atom" href="')
                __M_writer(str(_link('index_atom', None)))
                __M_writer('">\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_html_stylesheets(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        has_custom_css = context.get('has_custom_css', UNDEFINED)
        use_bundles = context.get('use_bundles', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n')
        if use_bundles:
            __M_writer('        <link href="/assets/css/all.css" rel="stylesheet" type="text/css">\n')
        else:
            __M_writer('        <link href="/assets/css/rst.css" rel="stylesheet" type="text/css">\n        <link href="/assets/css/poole.css" rel="stylesheet" type="text/css">\n        <link href="/assets/css/lanyon.css" rel="stylesheet" type="text/css">\n        <link href="/assets/css/code.css" rel="stylesheet" type="text/css">\n')
            if has_custom_css:
                __M_writer('            <link href="/assets/css/custom.css" rel="stylesheet" type="text/css">\n')
        __M_writer('    <link rel="stylesheet" href="//fonts.googleapis.com/css?family=PT+Serif:400,400italic,700|PT+Sans:400">\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_html_headstart(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        comment_system = context.get('comment_system', UNDEFINED)
        permalink = context.get('permalink', UNDEFINED)
        extra_head_data = context.get('extra_head_data', UNDEFINED)
        url_replacer = context.get('url_replacer', UNDEFINED)
        def html_feedlinks():
            return render_html_feedlinks(context)
        description = context.get('description', UNDEFINED)
        striphtml = context.get('striphtml', UNDEFINED)
        prevlink = context.get('prevlink', UNDEFINED)
        use_cdn = context.get('use_cdn', UNDEFINED)
        comment_system_id = context.get('comment_system_id', UNDEFINED)
        use_open_graph = context.get('use_open_graph', UNDEFINED)
        def html_stylesheets():
            return render_html_stylesheets(context)
        is_rtl = context.get('is_rtl', UNDEFINED)
        twitter_card = context.get('twitter_card', UNDEFINED)
        mathjax_config = context.get('mathjax_config', UNDEFINED)
        nextlink = context.get('nextlink', UNDEFINED)
        title = context.get('title', UNDEFINED)
        favicons = context.get('favicons', UNDEFINED)
        lang = context.get('lang', UNDEFINED)
        blog_title = context.get('blog_title', UNDEFINED)
        abs_link = context.get('abs_link', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n<!DOCTYPE html>\n<html ')
        __M_writer("prefix='")
        if use_open_graph or (twitter_card and twitter_card['use_twitter_cards']):
            __M_writer('og: http://ogp.me/ns# article: http://ogp.me/ns/article# ')
        if comment_system == 'facebook':
            __M_writer('fb: http://ogp.me/ns/fb#\n')
        __M_writer("' ")
        if use_open_graph or (twitter_card and twitter_card['use_twitter_cards']):
            __M_writer('vocab="http://ogp.me/ns" ')
        if is_rtl:
            __M_writer('dir="rtl" ')
        __M_writer('lang="')
        __M_writer(str(lang))
        __M_writer('">\n<head>\n    <meta charset="utf-8">\n')
        if description:
            __M_writer('    <meta name="description" content="')
            __M_writer(str(description))
            __M_writer('">\n')
        __M_writer('    <meta name="viewport" content="width=device-width">\n    <title>')
        __M_writer(striphtml(str(title)))
        __M_writer(' | ')
        __M_writer(striphtml(str(blog_title)))
        __M_writer('</title>\n\n    ')
        __M_writer(str(html_stylesheets()))
        __M_writer('\n    ')
        __M_writer(str(html_feedlinks()))
        __M_writer('\n')
        if permalink:
            __M_writer('      <link rel="canonical" href="')
            __M_writer(str(abs_link(permalink)))
            __M_writer('">\n')
        __M_writer('\n')
        if favicons:
            for name, file, size in favicons:
                __M_writer('            <link rel="')
                __M_writer(str(name))
                __M_writer('" href="')
                __M_writer(str(file))
                __M_writer('" sizes="')
                __M_writer(str(size))
                __M_writer('"/>\n')
        __M_writer('\n')
        if comment_system == 'facebook':
            __M_writer('        <meta property="fb:app_id" content="')
            __M_writer(str(comment_system_id))
            __M_writer('">\n')
        __M_writer('\n')
        if prevlink:
            __M_writer('        <link rel="prev" href="')
            __M_writer(str(prevlink))
            __M_writer('" type="text/html">\n')
        if nextlink:
            __M_writer('        <link rel="next" href="')
            __M_writer(str(nextlink))
            __M_writer('" type="text/html">\n')
        __M_writer('\n    ')
        __M_writer(str(mathjax_config))
        __M_writer('\n')
        if use_cdn:
            __M_writer('        <!--[if lt IE 9]><script src="//html5shim.googlecode.com/svn/trunk/html5.js"></script><![endif]-->\n')
        else:
            __M_writer('        <!--[if lt IE 9]><script src="')
            __M_writer(str(url_replacer(permalink, '/assets/js/html5.js', lang)))
            __M_writer('"></script><![endif]-->\n')
        __M_writer('\n    ')
        __M_writer(str(extra_head_data))
        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_html_translations(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        messages = context.get('messages', UNDEFINED)
        lang = context.get('lang', UNDEFINED)
        translations = context.get('translations', UNDEFINED)
        _link = context.get('_link', UNDEFINED)
        abs_link = context.get('abs_link', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n    <ul class="translations">\n')
        for langname in translations.keys():
            if langname != lang:
                __M_writer('            <li><a href="')
                __M_writer(str(abs_link(_link("root", None, langname))))
                __M_writer('" rel="alternate" hreflang="')
                __M_writer(str(langname))
                __M_writer('">')
                __M_writer(str(messages("LANGUAGE", langname)))
                __M_writer('</a></li>\n')
        __M_writer('    </ul>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"uri": "base_helper.tmpl", "filename": "themes/lanyon/templates/base_helper.tmpl", "source_encoding": "utf-8", "line_map": {"16": 0, "21": 2, "22": 61, "23": 65, "24": 80, "25": 103, "26": 113, "32": 63, "37": 63, "38": 64, "39": 64, "45": 82, "55": 82, "56": 83, "57": 84, "58": 84, "59": 84, "60": 85, "61": 86, "62": 87, "63": 88, "64": 88, "65": 88, "66": 88, "67": 88, "68": 90, "69": 91, "70": 91, "71": 91, "72": 94, "73": 95, "74": 96, "75": 97, "76": 97, "77": 97, "78": 97, "79": 97, "80": 99, "81": 100, "82": 100, "83": 100, "89": 67, "95": 67, "96": 68, "97": 69, "98": 70, "99": 71, "100": 75, "101": 76, "102": 79, "108": 3, "135": 3, "136": 6, "137": 7, "138": 8, "139": 10, "140": 11, "141": 13, "142": 14, "143": 15, "144": 17, "145": 18, "146": 21, "147": 21, "148": 21, "149": 24, "150": 25, "151": 25, "152": 25, "153": 27, "154": 28, "155": 28, "156": 28, "157": 28, "158": 30, "159": 30, "160": 31, "161": 31, "162": 32, "163": 33, "164": 33, "165": 33, "166": 35, "167": 36, "168": 37, "169": 38, "170": 38, "171": 38, "172": 38, "173": 38, "174": 38, "175": 38, "176": 41, "177": 42, "178": 43, "179": 43, "180": 43, "181": 45, "182": 46, "183": 47, "184": 47, "185": 47, "186": 49, "187": 50, "188": 50, "189": 50, "190": 52, "191": 53, "192": 53, "193": 54, "194": 55, "195": 56, "196": 57, "197": 57, "198": 57, "199": 59, "200": 60, "201": 60, "207": 105, "216": 105, "217": 107, "218": 108, "219": 109, "220": 109, "221": 109, "222": 109, "223": 109, "224": 109, "225": 109, "226": 112, "232": 226}}
__M_END_METADATA
"""
