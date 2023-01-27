num=int(input())
words=[]
for i in range(num):
    words.append(input())
for w in words:
    if len(w)>10:
        print(str(w[0])+""+str(len(w)-2)+""+w[-1])
    else:
        print(w)