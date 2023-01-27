def check_numberof_instance(s:str):
    num_of_char={}
    for i in s:
        if i in num_of_char:
            num_of_char[i]+=1
        else:
            num_of_char[i]=1
    # print(dic)
    num_of_char_values=[i for i in num_of_char.values()]
    num_of_char_values.sort()
    if(num_of_char_values[0]==num_of_char_values[-1]):
        return True
    return False


count=0
num_of_name=int(input())
names=input().split()
flagged=input().split()

for n  in  names:
    if(n in flagged):
        continue
    count+= 1 if check_numberof_instance(n) else 0
print(count)