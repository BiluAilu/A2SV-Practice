s=input()
u=0
l=0
t=list(s)
c=0
for i in t:
    if i.isupper():
        c+=1
    else:
        l+=1
if c>l:
    print(s.upper())
else:
    print(s.lower())
