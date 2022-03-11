from data.mysqldb import pymysqltest


class DataSource:
    def __init__(self):
        self.a = pymysqltest('10.1.9.124', 3306, 'root', '1qaz@WSX')  # 测试环境
        # self.b = pymysqltest('', '', '', '')

    def production(self):
        sql = """SELECT count(*) as 运营区配置 FROM wq_sod_commodity.t_city_operate_config;"""

        data = self.a.query(sql)
        return data



data = DataSource().production()
print(data)
pymysqltest.close(data)
