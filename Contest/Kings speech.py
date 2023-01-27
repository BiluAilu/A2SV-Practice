num=int(input())
speechs=[]
for i in range(num):
    speechs.append(input())

for i in range(num):
    print(f"{speechs[i][:2]}... {speechs[i]}? ")
