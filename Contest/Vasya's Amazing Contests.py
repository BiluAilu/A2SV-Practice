####################################
########Others solution


num= int(input())
x=input().split()

max=x[0]
min=x[0]
count=0

for i in x:
    if int(i)>int(max):
        max=i
        count+=1
    elif int(i)<int(min):
        min=i
        count+=1
print(count)