# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1412956195.811539
_enable_loop = True
_template_filename = u'/web/kzing.net/html/templates/_base.html'
_template_uri = u'_base.html'
_source_encoding = 'utf-8'
_exports = ['Pager', 'head', 'disqus', 'nav', 'footer']



from _base.config import Config


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        __M_writer = context.writer()
        __M_writer(u'\n\n')
        __M_writer(u'\n\n\n')
        __M_writer(u'\n\n\n')
        __M_writer(u'\n\n')
        __M_writer(u'\n\n')
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_Pager(context,total,limit):
    __M_caller = context.caller_stack._push_frame()
    try:
        int = context.get('int', UNDEFINED)
        this = context.get('this', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(u'\n\n    ')

        template = '?p=%s'
        
        now = int(this.get_argument("p", 1))
        _next = _pre = ''
        
        if now * limit < total:
            _next = template % (now + 1)
        
        if now > 1:
            _pre = template % (now - 1)
        
            
        
        __M_writer(u'\n    <ul class="pager">\n')
        if _next:
            __M_writer(u'            <li class="next">\n                <a href="')
            __M_writer(unicode(_next))
            __M_writer(u'">Older Posts &rarr;</a>\n            </li>\n')
        if _pre:
            __M_writer(u'            <li class="next pre">\n                <a href="')
            __M_writer(unicode(_pre))
            __M_writer(u'">&larr; Pre Posts </a>\n            </li>\n')
        __M_writer(u'    </ul>\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_head(context,title):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        __M_writer(u'\n\n<!DOCTYPE html>\n<html lang="en">\n\n<head>\n\n    <meta charset="utf-8">\n    <meta http-equiv="X-UA-Compatible" content="IE=edge">\n    <meta name="viewport" content="width=device-width, initial-scale=1">\n    <meta name="description" content="">\n    <meta name="author" content="">\n\n    <title>')
        __M_writer(unicode(title))
        __M_writer(u'</title>\n\n    <!-- Bootstrap Core CSS -->\n    <link href="../static/css/bootstrap.min.css" rel="stylesheet">\n\n    <!-- Custom CSS -->\n    <link href="../static/css/clean-blog.css" rel="stylesheet">\n\n    <!-- For highlight code -->\n    <!-- <link rel="stylesheet" href="../static/css/github.css"/> -->\n    <link rel="stylesheet" href="../static/css/tomorrow.css"/>\n\n</head>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_disqus(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        __M_writer(u'\n    <div id="disqus_thread"></div>\n    <script type="text/javascript">\n        /* * * CONFIGURATION VARIABLES: EDIT BEFORE PASTING INTO YOUR WEBPAGE * * */\n\n        var disqus_shortname = \'kzing\'; // required: replace example with your forum shortname\n\n        /* * * DON\'T EDIT BELOW THIS LINE * * */\n        (function() {\n            var dsq = document.createElement(\'script\'); dsq.type = \'text/javascript\'; dsq.async = true;\n            dsq.src = \'//\' + disqus_shortname + \'.disqus.com/embed.js\';\n            (document.getElementsByTagName(\'head\')[0] || document.getElementsByTagName(\'body\')[0]).appendChild(dsq);\n        })();\n    </script>\n    <noscript>Please enable JavaScript to view the <a href="http://disqus.com/?ref_noscript">comments powered by Disqus.</a></noscript>\n    <a href="http://disqus.com" class="dsq-brlink">comments powered by <span class="logo-disqus">Disqus</span></a>\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_nav(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        __M_writer(u'\n\n    <!-- Navigation -->\n    <nav class="navbar navbar-default navbar-custom navbar-fixed-top">\n        <div class="container-fluid">\n            <!-- Brand and toggle get grouped for better mobile display -->\n            <div class="navbar-header page-scroll">\n                <button type="button" class="navbar-toggle" data-toggle="collapse" data-target="#bs-example-navbar-collapse-1">\n                    <span class="sr-only">Toggle navigation</span>\n                    <span class="icon-bar"></span>\n                    <span class="icon-bar"></span>\n                    <span class="icon-bar"></span>\n                </button>\n                <a class="navbar-brand" href="')
        __M_writer(unicode(Config.host))
        __M_writer(u'">')
        __M_writer(unicode(Config.host_name))
        __M_writer(u'</a>\n            </div>\n\n            <!-- Collect the nav links, forms, and other content for toggling -->\n            <div class="collapse navbar-collapse" id="bs-example-navbar-collapse-1">\n                <ul class="nav navbar-nav navbar-right">\n                    <li>\n                        <a href="//')
        __M_writer(unicode(Config.host))
        __M_writer(u'">Home</a>\n                    </li>\n                    <li>\n                        <a href="//')
        __M_writer(unicode(Config.host))
        __M_writer(u'/about">About</a>\n                    </li>\n                    <li>\n                        <a href="//')
        __M_writer(unicode(Config.host))
        __M_writer(u'/sample_post">Sample Post</a>\n                    </li>\n                    <!-- <li>\n                        <a href="contact.html">Contact</a>\n                    </li> -->\n                </ul>\n            </div>\n            <!-- /.navbar-collapse -->\n        </div>\n        <!-- /.container -->\n    </nav>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_footer(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        __M_writer(u'\n    <!-- Footer -->\n    <footer>\n        <div class="container">\n            <div class="row">\n                <div class="col-lg-8 col-lg-offset-2 col-md-10 col-md-offset-1">\n                    <ul class="list-inline text-center">\n                        <li>\n                            <a href="#">\n                                <span class="fa-stack fa-lg">\n                                    <i class="fa fa-circle fa-stack-2x"></i>\n                                    <i class="fa fa-twitter fa-stack-1x fa-inverse"></i>\n                                </span>\n                            </a>\n                        </li>\n                        <li>\n                            <a href="#">\n                                <span class="fa-stack fa-lg">\n                                    <i class="fa fa-circle fa-stack-2x"></i>\n                                    <i class="fa fa-facebook fa-stack-1x fa-inverse"></i>\n                                </span>\n                            </a>\n                        </li>\n                        <li>\n                            <a href="#">\n                                <span class="fa-stack fa-lg">\n                                    <i class="fa fa-circle fa-stack-2x"></i>\n                                    <i class="fa fa-github fa-stack-1x fa-inverse"></i>\n                                </span>\n                            </a>\n                        </li>\n                    </ul>\n                    <p class="copyright text-muted">Copyright &copy; kzing.net</p>\n                </div>\n            </div>\n        </div>\n    </footer>\n\n    <!-- jQuery -->\n    <script src="../static/js/jquery.min.js"></script>\n\n    <!-- Bootstrap Core JavaScript -->\n    <script src="../static/js/bootstrap.min.js"></script>\n\n    <!-- Custom Theme JavaScript -->\n    <script src="../static/js/clean-blog.js"></script>\n\n    <!-- Highlight code -->\n    <script src="../static/js/highlight.pack.js"></script>\n    <script >hljs.initHighlightingOnLoad();</script>\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "utf-8", "line_map": {"15": 1, "19": 0, "24": 3, "25": 31, "26": 71, "27": 125, "28": 144, "29": 174, "35": 146, "41": 146, "42": 148, "56": 160, "57": 162, "58": 163, "59": 164, "60": 164, "61": 167, "62": 168, "63": 169, "64": 169, "65": 172, "71": 5, "75": 5, "76": 18, "77": 18, "83": 127, "87": 127, "93": 34, "97": 34, "98": 47, "99": 47, "100": 47, "101": 47, "102": 54, "103": 54, "104": 57, "105": 57, "106": 60, "107": 60, "113": 74, "117": 74, "123": 117}, "uri": "_base.html", "filename": "/web/kzing.net/html/templates/_base.html"}
__M_END_METADATA
"""