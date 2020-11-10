def fact(n):
    if n==1:
        return 1
    else:
        return n* fact(n-1)

number = int(input("输入正整数："))
rel = fact(number)
print("%d 的阶乘是：%d" %(number,rel))
