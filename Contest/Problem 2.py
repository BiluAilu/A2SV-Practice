st=[]
st.append(input())
st.append(input())
equal=True

for i in range(len(st[0])):
    if(st[0][i].upper()>st[1][i].upper()):
        equal=False
        print(1)
        break
    elif(st[0][i].upper()<st[1][i].upper()):
        print(-1)
        equal=False
        break
if(equal):
    print(0)