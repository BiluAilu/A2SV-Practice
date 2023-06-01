import sys, threading


input = lambda: sys.stdin.readline().strip()

def whiteWalker(n):
    if n==0 or n==1:
        return n
    else:
        n1=n//2
        n2=n%2
        n=[n]
        n.pop()
        n1=whiteWalker(n1)
        n2=whiteWalker(n2)
        n.extend((n1,n2,n1))
        return n

output=[]             
def reemovNestings(l):
    for i in l:
        if type(i) == list:
            reemovNestings(i)
        else:
            output.append(i)

def main():
    counter=0
    num,l,r=map(int,input().split())
    myS=whiteWalker(num)
    reemovNestings(myS)


    for i in range(l-1,r):
        if output[i]==1:
            counter+=1
    print(counter)

    # write your code here

if __name__ == '__main__':
    
    sys.setrecursionlimit(1 << 30)
    threading.stack_size(1 << 27)

    main_thread = threading.Thread(target=main)
    main_thread.start()
    main_thread.join()

    