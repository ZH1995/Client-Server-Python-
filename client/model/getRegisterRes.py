# Created by zh on 2016/3/15.
# -*- coding: UTF-8 -*-
import requests
import json
import logging


class getRegisterRes(object):

    def __init__(self):
        self.logger = logging.getLogger(name='getReigsterRes')

    def registerRes(self, user_name, user_pass):

        self.logger.info("进入registerRes方法")
        # 1.将参数转换成json格式
        jsons = json.dumps(
            {
                'user_name': user_name,
                'user_pass': user_pass
            }
        ).encode('utf8')

        # 2.获取json对象并解析
        try:
            r = requests.get('http://localhost:8801%s' % '/register_user', data=jsons)
            json_obj = r.json()
            r.close()
            self.logger.info("远程调用getRegisterRes方法成功")
        except Exception:
            self.logger.error("远程调用getRegisterRes方法失败")
            raise Exception("远程调用getRegisterRes方法失败")

        # 3.返回结果字典
        self.logger.info("退出registerRes方法")
        return json_obj
