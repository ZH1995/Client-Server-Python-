# Created by zh on 2016/3/14.
# -*- coding: UTF-8 -*-


import tornado.web
import tornado.httpserver
import tornado.ioloop
import json
import logging
from model import SQL

class confirmHandler(tornado.web.RequestHandler):

    def initialize(self):
        self.logger = logging.getLogger(name='confirmHandler')

    def get(self):

        self.logger.info("进入confirmHandler")
        # 1.获取用户名、密码，并解析json
        argument = json.loads(self.request.body)
        user_name = argument['user_name']
        user_pass = argument['user_pass']


        # 2.调用confirm_user方法，判断用户是否存在
        self.logger.info("进入confirmHandler")
        if(SQL().confirm_user(user_name, user_pass) == False):
            self.write(json.dumps(
                {
                    'result': 'False'
                }
            ).encode('utf8'))
        # 3.存在返回true，不存在返回false
        else:
            self.write(json.dumps(
                {
                    'result': 'True'
                }
            ).encode('utf8'))

