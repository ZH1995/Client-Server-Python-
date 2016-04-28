# Created by zh on 2016/3/15.
# -*- coding: UTF-8 -*-
import tornado.web
import tornado.httpserver
import tornado.ioloop
import logging
from model import getConfirmRes

class confirmHandler(tornado.web.RequestHandler):

    def initialize(self):
        self.logger = logging.getLogger(name='confirmHandler')

    def post(self):

        self.logger.info("进入confirmHandler")
        # 1.获取用户输入的用户名、密码
        user_name = self.get_argument('user_name')
        user_pass = self.get_argument('user_pass')

        # 2.调用confimRes方法，传入用户名、密码，获取结果信息
        res = getConfirmRes().confirmRes(user_name, user_pass)

        #res = {'result': 'False'}

        # 3.渲染result页面
        self.logger.info("退出confirmHandler")
        if res['result'] == 'True':
            self.render('result.html', user_name=user_name)
        else:
            self.render('index.html')
