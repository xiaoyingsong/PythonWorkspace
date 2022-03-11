import pymysql
from pymysql.cursors import DictCursor


class pymysqltest:

    def __init__(self, host,
                 port,
                 user,
                 password
                 ):
        # 连接数据库
        self.db = pymysql.connect(host=host,
                                  port=port,
                                  user=user,
                                  password=password
                                  )
        # 创建游标对象cursor
        self.cursor = self.db.cursor(pymysql.cursors.DictCursor)

    def query(self, sql, one=True):
        # 使用execute 执行sql语句
        self.cursor.execute(sql)
        if one:
            # 如果为one ，使用 fetchone() 方法获取单条数据
            return self.cursor.fetchone()
        else:
            # 使用 fetchall() 方法获取所有数据
            return self.cursor.fetchall()

    def updateAnddelete(self, sql):
        try:
            # 使用execute 执行sql语句
            self.cursor.execute(sql)
            # 提交到数据库执行
            self.db.commit()
        except:
            # 如果发生错误回滚数据
            self.db.rollback()

    def close(self):
        # 关闭游标
        self.cursor.close()
        # 关闭数据库
        self.db.close()


if __name__ == '__main__':
    pass
