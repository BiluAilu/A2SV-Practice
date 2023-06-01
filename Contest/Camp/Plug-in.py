inp=input()

inp=list(inp)

i=0
while True:
    if inp[i]==inp[i+1]:
        inp.pop()
        inp.pop()
    
