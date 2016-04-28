# Created by zh on 2016/3/15.
# -*- coding: UTF-8 -*-

import tornado.web
import tornado.httpserver
import tornado.ioloop


class goRegisterPage(tornado.web.RequestHandler):
    def post(self):
        self.render('register.html');