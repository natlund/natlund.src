# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1463687541.5047035
_enable_loop = True
_template_filename = 'themes/lanyon/templates/base_helper.tmpl'
_template_uri = 'base_helper.tmpl'
_source_encoding = 'utf-8'
_exports = ['late_load_js', 'html_translations', 'html_stylesheets', 'html_headstart', 'html_feedlinks']


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


def render_html_translations(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        lang = context.get('lang', UNDEFINED)
        _link = context.get('_link', UNDEFINED)
        translations = context.get('translations', UNDEFINED)
        messages = context.get('messages', UNDEFINED)
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


def render_html_stylesheets(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        use_bundles = context.get('use_bundles', UNDEFINED)
        has_custom_css = context.get('has_custom_css', UNDEFINED)
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
        nextlink = context.get('nextlink', UNDEFINED)
        mathjax_config = context.get('mathjax_config', UNDEFINED)
        title = context.get('title', UNDEFINED)
        def html_feedlinks():
            return render_html_feedlinks(context)
        permalink = context.get('permalink', UNDEFINED)
        comment_system = context.get('comment_system', UNDEFINED)
        abs_link = context.get('abs_link', UNDEFINED)
        twitter_card = context.get('twitter_card', UNDEFINED)
        comment_system_id = context.get('comment_system_id', UNDEFINED)
        use_open_graph = context.get('use_open_graph', UNDEFINED)
        lang = context.get('lang', UNDEFINED)
        url_replacer = context.get('url_replacer', UNDEFINED)
        is_rtl = context.get('is_rtl', UNDEFINED)
        striphtml = context.get('striphtml', UNDEFINED)
        favicons = context.get('favicons', UNDEFINED)
        description = context.get('description', UNDEFINED)
        blog_title = context.get('blog_title', UNDEFINED)
        use_cdn = context.get('use_cdn', UNDEFINED)
        prevlink = context.get('prevlink', UNDEFINED)
        extra_head_data = context.get('extra_head_data', UNDEFINED)
        def html_stylesheets():
            return render_html_stylesheets(context)
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


def render_html_feedlinks(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        len = context.get('len', UNDEFINED)
        _link = context.get('_link', UNDEFINED)
        translations = context.get('translations', UNDEFINED)
        generate_atom = context.get('generate_atom', UNDEFINED)
        generate_rss = context.get('generate_rss', UNDEFINED)
        rss_link = context.get('rss_link', UNDEFINED)
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


"""
__M_BEGIN_METADATA
{"line_map": {"16": 0, "21": 2, "22": 61, "23": 65, "24": 80, "25": 103, "26": 113, "32": 63, "37": 63, "38": 64, "39": 64, "45": 105, "54": 105, "55": 107, "56": 108, "57": 109, "58": 109, "59": 109, "60": 109, "61": 109, "62": 109, "63": 109, "64": 112, "70": 67, "76": 67, "77": 68, "78": 69, "79": 70, "80": 71, "81": 75, "82": 76, "83": 79, "89": 3, "116": 3, "117": 6, "118": 7, "119": 8, "120": 10, "121": 11, "122": 13, "123": 14, "124": 15, "125": 17, "126": 18, "127": 21, "128": 21, "129": 21, "130": 24, "131": 25, "132": 25, "133": 25, "134": 27, "135": 28, "136": 28, "137": 28, "138": 28, "139": 30, "140": 30, "141": 31, "142": 31, "143": 32, "144": 33, "145": 33, "146": 33, "147": 35, "148": 36, "149": 37, "150": 38, "151": 38, "152": 38, "153": 38, "154": 38, "155": 38, "156": 38, "157": 41, "158": 42, "159": 43, "160": 43, "161": 43, "162": 45, "163": 46, "164": 47, "165": 47, "166": 47, "167": 49, "168": 50, "169": 50, "170": 50, "171": 52, "172": 53, "173": 53, "174": 54, "175": 55, "176": 56, "177": 57, "178": 57, "179": 57, "180": 59, "181": 60, "182": 60, "188": 82, "198": 82, "199": 83, "200": 84, "201": 84, "202": 84, "203": 85, "204": 86, "205": 87, "206": 88, "207": 88, "208": 88, "209": 88, "210": 88, "211": 90, "212": 91, "213": 91, "214": 91, "215": 94, "216": 95, "217": 96, "218": 97, "219": 97, "220": 97, "221": 97, "222": 97, "223": 99, "224": 100, "225": 100, "226": 100, "232": 226}, "source_encoding": "utf-8", "uri": "base_helper.tmpl", "filename": "themes/lanyon/templates/base_helper.tmpl"}
__M_END_METADATA
"""
