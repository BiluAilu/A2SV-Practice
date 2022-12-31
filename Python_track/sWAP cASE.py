def swap_case(s):
    answer="";
    for i in s:
        if(i.isupper()):
            answer=answer+i.lower()
        elif(i.islower()):
            answer=answer+i.upper()
        else:
            answer=answer+i
    return answer

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)