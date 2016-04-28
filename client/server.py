# Created by zh on 2016/3/15.
# -*- coding: UTF-8 -*-


import os
import sys
import tornado.web
import tornado.ioloop
import logging.config
from handler import *

sys.path.append(os.getcwd())

logging.config.fileConfig(r"config/logging.conf")

settings = {
    'template_path': os.path.join(os.path.dirname(__file__), 'template'),
    'debug': True
}

handlers = [
    (r'/', indexHandler),
    (r'/confirm_user', confirmHandler),
    (r'/register_page', goRegisterPage),
    (r'/register_user', registerHandler),
    (r"/template/(.*)", tornado.web.StaticFileHandler, {"path": settings['template_path']})
]

if __name__ == "__main__":
    application = tornado.web.Application(handlers=handlers, **settings)
    application.listen(8802)
    tornado.ioloop.IOLoop.instance().start()