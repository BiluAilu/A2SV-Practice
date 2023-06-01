start=input()
end=input()

start=[ord(start[0]), int(start[1])]
end=[ord(end[0]), int(end[1])]


number_of_steps=0
#or 
#number_of_steps=max(abs(start[0]-end[0]), abs(end[1]-start[1]))


steps=[]
while start!=end:
    step=""
    if start[0]>end[0]:
        step+="L"
        start[0]-=1
    elif start[0]<end[0]:
        step+="R"
        start[0]+=1
    if start[1]>end[1]:
        step+="D"
        start[1]-=1
    elif start[1]<end[1]:
        step+="U"
        start[1]+=1
    number_of_steps+=1
    steps.append(step)
print(number_of_steps)
print(*steps,sep="\n")



