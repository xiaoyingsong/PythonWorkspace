import pymysql
import pandas as pd
from pandas import Series, DataFrame
from datetime import date

# 打开数据库连接

db = pymysql.connect(host='10.1.9.124',
                     port=3306,
                     user='root',
                     password='1qaz@WSX',
                     )

cursor = db.cursor()
sql = """SELECT t.OPERAREAID,t.OPERAREANAME,t.NOTE FROM wq_sod_erp.operarea t limit 10"""
cursor.execute(sql)
data = cursor.fetchall()
# print(data)
emp = ['001', '002', '003', '004', '005', '006', '007', '008', '009', '010']
sel = Series(data, index=emp)
# for values in sel:
#     print(values)
# for values in sel.keys():
#     print(values)
# for values in sel.items():
#     print(values)
# print(sel[0])
# print(sel[[1,4]])
# print(sel[0:3])
# sel = Series(data,index=emp)
# print(sel)
# print('索引下标',sel[['008','009']])
# print('索引切片',sel['001': '004'])
# print(sel.values)
# print(sel.index.tolist())
# print(list(sel))
# print(sel)
# df = DataFrame(data, columns=['OPERAREAID', 'OPERAREANAME', 'NOTE'])
# print(df)
# print("数据对象是：{}".format(data))
# for i in data:
#     print(i)
#     pass
# print(sel.ndim)
# df = DataFrame(data, index=emp, columns=['OPERAREAID', 'OPERAREANAME', 'NOTE'])
# print(df.head())
# # print(df.tail(3))
# 通过位置索引切片获取一行
# print(df[0:1])
#
# # 通过位置索引切片获取多行
# print(df[0:4])
#
# # 获取多行里面的某几列
# print(df[1:3][['OPERAREAID']])

# 获取DataFrame的列
# print(df[['OPERAREAID']])
#
# # 获取DataFrame的多个列
# print(df[['OPERAREANAME', 'OPERAREANAME']])
df = DataFrame(data, index=emp, columns=['OPERAREAID', 'OPERAREANAME', 'NOTE'])
print(df)
# print(df.loc['001',:])
print(df.iloc[:,1])
# # 按行遍历iterrows()
# for index, row in df.iterrows():
#     print(index, row)
#
# # 按行遍历iteritems()
# print(df)
# for index, row in df.items():
#     print(index, row)