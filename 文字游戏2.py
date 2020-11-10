import random
secret = random.randint(1,10)

print("-------我是yhx小可爱-------")

temp = input("猜一下我心里想的是哪个数字：")
guess = int(temp)
while guess !=secret:
    temp = input("猜错啦 重新输入叭：")
    guess = int(temp)
    if guess==secret:
        print("猜对啦！")
    else:
        if guess > secret:
            print("大了啦！")
        else:
            print("小了哦！")
print("游戏结束!")
