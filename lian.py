'''
print("--------------文字小游戏----------------")

temp = input("猜猜我想的是数字几(3次机会哦！)：")
guss = int(temp)
if guss == 8:
    print("对咯！")
else:
    for content in range(0,3):
        content = 3
        temp = input("猜错了 重新输入吧！")
        guss = int(temp)
        if guss == 8:
             print("对咯！")
        else:
            if guss > 8:
                print("大了！")
            else:
                print("小了！")
        content -= 1
print("游戏结束")
'''
x = 6
y = 22

a = x if x > y else y
print(a)
