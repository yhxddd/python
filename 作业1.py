'''name = input("请输入姓名：")
print("你好，"+  name +"!")
print("你好，%s!" % name)'''

'''
for i in range(100):
    if i % 2 == 0:
        print("你妹好漂亮！")
    else:
        print("你大爷好丑！")

        
tem = int(input("请输入 1 - 100 之间一个数字："))
if tem >= 1 and tem <= 100:
    print("你妹号漂亮")
else:
    print("你大爷好丑")



DaysPerYear = 365
HoursPerDay = 24
Minute=60
seconds = 60
Result = DaysPerYear * HoursPerDay *Minute*seconds
print(Result)
'''
'''
number = 5
count = 1
temp = input('猜猜我在想什么数字  只有三次机会哦：\n')
while not temp.isdigit():
    print('输入不合法!')
    temp=input("输入一个整数：")
guess = int(temp)
if guess == number:
    print("猜对啦！")
else:
    while guess != number and count < 3:
        guess = int(input('猜错啦 重新输入把'))
        if guess > number:
            print("大了大了")

        if guess < number:
            print('小了小了')
        count += 1
print('游戏结束')



temp = input("输入一个数进行四舍五入：")
number = float(temp) +0.5
result = int(number)
print(result)
'''



temp = input("输入一个年份：")
while not temp.isdigit():
    print("不合法")
    temp =input ("输入四位数字")
year = int(temp)
if (year % 4 == 0 and year % 100 !=0) or year % 400 == 0:
    print("%d 是闰年" % year)
else:
    print("%d 不是闰年" % year)
