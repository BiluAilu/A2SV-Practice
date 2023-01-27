inp1=input()
inp2=input()

if(inp1.upper()==inp2.upper()):
    print("0")
else:
    for i in range(len(inp1)):
        if(inp1[i].upper()>inp2[i].upper()):
            print('1')
            break
        elif(inp1[i].upper()<inp2[i].upper()):
            print(-1)
            break
