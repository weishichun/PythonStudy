import random

print("猜数字,程序随机生成1~100之间一个数,你有5次机会")
target = random.randint(1,100)
total = 5
count = 0
while True:
    n = int(input("输入0~100之间的一个整数: "))
    count += 1
    if count > 5:
        print("5次机会已用完,仍未猜中")
        break
    if target == n:
        print("你猜对了")
        break
    elif target < n:
        print("猜大了,再试试!")
    else:
        print("猜小了,再试试!")
