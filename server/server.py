# Created by zh on 2016/3/14.
# -*- coding: UTF-8 -*-

import os
import sys
import tornado.web
import tornado.ioloop
import logging.config
from handler import *

sys.path.append(os.getcwd())

logging.config.fileConfig(r"config/logging.conf")

handlers = [
    (r'/confirm_user', confirmHandler),
    (r'/register_user', registerHandler)
]

settings = {
    'debug': True
}

if __name__ == "__main__":
    application = tornado.web.Application(handlers=handlers, **settings)
    application.listen(8801)
    tornado.ioloop.IOLoop.instance().start()