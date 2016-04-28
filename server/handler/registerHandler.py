# Created by zh on 2016/3/14.
# -*- coding: UTF-8 -*-


import tornado.web
import tornado.httpserver
import tornado.ioloop
import json
import logging
from model.SQL import SQL


class registerHandler(tornado.web.RequestHandler):

    def initialize(self):
        self.logger = logging.getLogger(name='registerHandler')


    def get(self):

        self.logger.info("进入registerHandler")
        # 1.获取用户名、密码，并解析json
        argument = json.loads(self.request.body)
        self.logger.info(argument)
        user_name = argument['user_name']
        user_pass = argument['user_pass']


        # 2.调用confirm_user方法，判断用户是否存在.存在返回false
        self.logger.info("退出registerHandler")
        if SQL().confirm_user(user_name, user_pass):
            self.write(json.dumps(
                {
                    'result': 'False'
                }
            ).encode('utf8'))

        # 3.不存在则插入数据库并返回true
        else:
            SQL().register_user(user_name, user_pass)
            self.write(json.dumps(
                {
                    'result': 'True'
                }
            ).encode('utf8'))
