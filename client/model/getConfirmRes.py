# Created by zh on 2016/3/15.
# -*- coding: UTF-8 -*-
import requests
import json
import logging

class getConfirmRes(object):

    def __init__(self):
        self.logger = logging.getLogger(name='getConfirmRes')

    def confirmRes(self, user_name, user_pass):

        self.logger.info("进入confirmRes方法")

        # 1.将参数转换成json格式
        jsons = json.dumps(
            {
                'user_name': user_name,
                'user_pass': user_pass
            }
        ).encode('utf8')

        # 2.获取json对象并解析
        try:
            r = requests.get('http://localhost:8801%s' % '/confirm_user', data=jsons)
            json_obj = r.json()
            r.close()
            self.logger.info("远程调用getConfirmRes方法成功")
        except Exception:
            self.logger.error("远程调用getConfirmRes方法失败")
            raise Exception("远程调用getConfirmRes方法失败")

        # 3.返回结果字典
        self.logger.info("退出confirmRes方法")
        return json_obj




