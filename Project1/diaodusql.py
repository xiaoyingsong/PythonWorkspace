import schedule
import pymysql
import time
from pymysql import OperationalError


def _reCon(db):
    """ MySQLdb.OperationalError异常"""
    # self.con.close()
    while True:
        try:
            db.ping()
            break
        except OperationalError:
            db.ping(True)


# def keeptoprice():
#     _reCon(db)
#     with db:
#         sql = "INSERT INTO lastdaydata (id,total,closePrice,date,all_increase) VALUES ('%s', %s, %s, '%s','%s')" % (a,b,c,d,e)
#         cursor.execute(sql)
#         db.commit()



schedule.every().day.at("06:30").do(keeptoprice)
db = pymysql.connect(host='localhost',
                     user='root',
                     password='root',
                     database='rihgtnow')
_reCon(db)
with db:
    cursor = db.cursor()
    cursor.execute("select stock_id,stock_name from selectall")
    lists = cursor.fetchall()
    dic = {list1[0]: list1[1] for list1 in lists}

if __name__ == '__main__':
    while 1:
        schedule.run_pending()
        time.sleep(1)
