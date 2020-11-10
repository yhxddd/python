score = int (input ("请输入一个分数："))
if 100 <= score <= 90:
    print("A")
if 90 < score <= 80:
    print("B")
if 80 < score <=60:
    print("C")
if  score < 60:
    print("D")
else:
    print("输入错误!")



score = int (input ("请输入一个分数："))
if 100 <= score <= 90:
    print("A")
elif 90 < score <= 80:
    print("B")
elif 80 < score <=60:
    print("C")
elif  score < 60:
    print("D")
else:
    print("输入错误!")
