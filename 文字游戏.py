print("-------我是yhx小可爱-------")
temp = input("猜一下我心里想的是哪个数字：")
#input 返回字符串类型

guess = int(temp)
'''字符串转为整形'''
if guess==8:
    
    '''使用冒号后 自动缩进表示if成立时要执行的语句'''
    
    print("猜对啦！")
else:
    print("猜错啦，想的是8哦！")
print("游戏结束!")
