try:
    f = open('我是一个文件.txt')
    print(f.read())
    f.close()
except OSError as reason:
    print("文件出错啦\n 错误的原因是："+ str(reason))
