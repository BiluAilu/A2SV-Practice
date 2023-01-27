inp=input()
numInp=inp.split("+")
# print(numInp)
numInp.sort()
out=[]
for i in range(len(numInp)-1):
    out.append(f'{numInp[i]}+')
out.append(f'{numInp[-1]}')
print(*out,sep='')
