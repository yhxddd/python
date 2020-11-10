try:
    f = open('我是一个文件.txt')
    print(f.read())
    f.close()
except OSError :
    print("文件不存在！")
