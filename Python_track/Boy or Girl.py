message=input()
numChar={}
for i in message:
    numChar.add(i)
if(len(numChar)%2==0):
    print("CHAT WITH HER!")
else:
    print("IGNORE HIM!")