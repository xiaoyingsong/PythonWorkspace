# # sum = 0
# # for i in range(1, 101):
# #     if sum > 50:
# #         print("循环到这")
# #         break
# #     sum += i
# # print(sum)
#
# #九九乘法口诀表
# # for i in range(1,10):
# #     for j in range(1,i+1):
# #         print("{}x{}={}".format(i,j,i*j),end=" ")
# #         pass
# #     print("")
# #     pass
#
# # for else
# acount = "sxy"
# password = "123456"
# for i in range(3):
#     zh = input("请输入账号：")
#     mm = input("请输入密码：")
#     if zh==acount and mm==password:
#         print("登录成功！")
#         break
#         pass
#     else:
#         print("账号或密码不正确，剩余尝试次数：{}".format(len(range(3))-(i+1)))
#     pass
# else:
#     print("您已被系统锁定。。。")
# 猜年龄小游戏
# 1.最多允许3次
# 2.每3次问是否继续，回答y继续，n退出
# 3.如果猜对了，就直接推出
age = "18"
for i in range(3):
    age1 = input("请输入年龄：")
    if age1 == age:
        print("恭喜答对了")
        break
        pass
    else:
        print("答错了,还剩下{}次".format(len(range(3))-(i+1)))
else:
    print("你3次机会已经用完啦")
