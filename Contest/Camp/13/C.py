import sys, threading

input = lambda: sys.stdin.readline().strip()

def reSum(n,c):
    if len(str(n))==1:
        return c
    else:
        n_s=str(n)
        sum=0
        for i in n_s:
            sum+=int(i)
        c+=1
        return reSum(sum,c)
def main():

    num=int(input())
    
    print(reSum(num,0))
    

    # write your code here

if __name__ == '__main__':
    
    sys.setrecursionlimit(1 << 30)
    threading.stack_size(1 << 27)

    main_thread = threading.Thread(target=main)
    main_thread.start()
    main_thread.join()

    