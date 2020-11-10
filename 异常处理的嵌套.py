try:
    sum = 1 + '1'
    f = open('我是一个文件.txt')
    print(f.read())
    f.close()


    
    '''或者 写为 下述格式'''
except (OSError,TypeError):
    print("出错啦！")
