import datetime
import random
import time

import pymysql


class DataAccess:
    def __init__(self, host='localhost', user='root', password='123456', db='test', port=3306):
        self.host = host
        self.user = user
        self.password = password
        self.db = db
        self.port = port
        self.coon = pymysql.connect(host=self.host, user=self.user, password=self.password, db=self.db,
                                    port=self.port,
                                    charset='utf8')
        self.cursor = self.coon.cursor()

    def get_cursor(self):
        self.coon = pymysql.connect(host=self.host, user=self.user, password=self.password, db=self.db,
                                    port=self.port,
                                    charset='utf8')
        self.cursor = self.coon.cursor()

    def check_cursor(self):
        if self.cursor is None:
            self.get_cursor()

    def select_(self, sql):
        try:
            self.check_cursor()
            self.cursor.execute(sql)
            results = self.cursor.fetchall()
            return results
        except Exception as e:
            print(e)

    def operate_(self, sql):
        try:
            self.check_cursor()
            self.cursor.execute(sql)
            self.coon.commit()
        except Exception as e:
            print(e)

    def insert_action_(self, action, flag):
        current_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        sql = "insert into dzrecord(SJC,ACTION,FLAG)values('{}','{}',{})".format(current_time, action, flag)
        try:
            self.check_cursor()
            self.cursor.execute(sql)
            self.coon.commit()
        except Exception as e:
            print(e)

    def select_oee(self):
        current_date = datetime.datetime.now().strftime('%Y-%m-%d')
        sql = "select * from oee_date where SJC = '{}'".format(current_date)
        data = self.select_(sql)
        hour = time.localtime()[3]
        list_oee = list(data[0][1:hour - 6])
        for i in range(len(list_oee)):
            if list_oee[i] == 0:
                list_oee[i] = random.randint(85, 90)
                self.update_oee_byhour_(i + 8, list_oee[i])
        return list_oee

    def update_oee(self):
        hour = time.localtime()[3]
        current_date = datetime.datetime.now().strftime('%Y-%m-%d')
        if hour in range(8, 19):
            eff = random.randint(85, 90)
            sql = "update oee_date set O" + str(hour) + "=" + str(eff) + ' where SJC="' + current_date + '"'
            self.operate_(sql)

    def update_oee_byhour_(self, hour, eff):
        current_date = datetime.datetime.now().strftime('%Y-%m-%d')
        sql = "update oee_date set O" + str(hour) + "=" + str(eff) + ' where SJC="' + current_date + '"'
        self.operate_(sql)

    def update_loss_(self, action, cost_time):
        current_date = datetime.datetime.now().strftime('%Y-%m-%d')
        old_data = self.select_("select {} from loss where SJ='{}' ".format(action, current_date))
        old_time = old_data[0][0]
        sql = "update loss set {}={} where SJ='{}'".format(action, old_time + cost_time, current_date)
        self.operate_(sql)

    def select_loss(self):
        current_date = datetime.datetime.now().strftime('%Y-%m-%d')
        sql = "select action2,action1,action3,action4 from loss where SJ='{}'".format(current_date)
        data = self.select_(sql)
        return list(data[0])


if __name__ == "__main__":
    da = DataAccess()
    current_date = datetime.datetime.now().strftime('%Y-%m-%d')
    da.operate_("delete from loss where SJ='{}'".format(current_date))
