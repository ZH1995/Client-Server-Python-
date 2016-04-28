# Created by zh on 2016/3/14.
# -*- coding: UTF-8 -*-

import MySQLdb
import logging

class SQL:
    db_config = ['127.0.0.1', 'root', '123456', 'login']
    def __init__(self):
        self.logger = logging.getLogger(name='SQL')


    def confirm_user(self, user_name , user_pass):
        self.logger.info("进入confirm_user方法")
        db = MySQLdb.connect(*SQL.db_config, charset='utf8')
        cursor = db.cursor()
        result = None
        sql = """
            select * from login where user = "%s" and pass = "%s";
        """
        try:
            cursor.execute(sql % (user_name, user_pass))
            result = cursor.fetchall()
            db.commit()
        except:
            self.logger.error("confirm_user方法数据库操作异常")
            db.rollback()
        db.close()
        self.logger.info(result)
        self.logger.info("退出confirm_user方法")
        if len(result) == 0:
            return False
        else:
            return True

    def register_user(self, user_name, user_pass):
        self.logger.info("进入register_user方法")
        db = MySQLdb.connect(*SQL.db_config, charset='utf8')
        cursor = db.cursor()
        sql = """
            insert into login (user , pass) values ("%s", "%s");
        """
        try:
            cursor.execute(sql % (user_name, user_pass))
            db.commit()
        except:
            self.logger.error("register_user方法数据库操作异常")
            db.rollback()
        db.close()
        self.logger.info("退出register_user方法")