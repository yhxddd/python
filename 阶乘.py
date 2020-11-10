def jiecheng(n):
    result= n
    for i in range(1,n):
        result *= i
    return result

number = int (input("输入一个整数："))
rel = jiecheng(number)
print("%d 的阶乘是：%d" %(number,rel))
