from data import mysqldb

a = mysqldb.pymysqltest(host='10.1.9.124',
                        port=3306,
                        user='root',
                        password='1qaz@WSX'

                        )
sql = """SELECT count(*) as 运营区配置
FROM wq_sod_commodity.t_city_operate_config;
"""
data = a.query(sql)
print(data)
mysqldb.pymysqltest.close(a)
