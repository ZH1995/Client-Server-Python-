# Created by zh on 2016/3/15.
# -*- coding: UTF-8 -*-


import tornado.web
import tornado.httpserver
import tornado.ioloop
import logging


class indexHandler(tornado.web.RequestHandler):

    def initialize(self):
        self.logger = logging.getLogger(name='indexHandler')

    def get(self):
        self.logger.info("进入indexHandler")
        self.logger.info("退出indexHandler")
        self.render('index.html')

