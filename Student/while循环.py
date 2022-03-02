# import random
#
# person = int(input("请输入你的手势:0 石头 1 剪刀 2布"))
# computer = random.randint(0,2)
# print(person)

# 九九乘法表
# row = 9
# while row >= 1:
#     col = 1
#     while col <= row:
#         print("%dx%d=%d" % (row, col, row * col), end=' ')
#         col += 1
#         pass
#     print(" ")
#     row -= 1
#     pass
# 打印直角三角行
# row = 1
# while row <= 7:
#     col = 1
#     while col <= row:
#         print("*", end=" ")
#         col += 1
#         pass
#     row += 1
#     print("")
#     pass
# 等腰三角形
row = 1
while row <= 10:
    col = 1
    while col <= 10 - row:
        print(" ", end="")
        col += 1
        pass
    i = 1
    while i <= 2 * row - 1:
        print("*", end="")
        i += 1
    row += 1
    print()
    pass
