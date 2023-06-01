import sys, threading

input = lambda: sys.stdin.readline().strip()

def main():

    nums=input().split("+")
    nums.sort()
    for i in range(len(nums)):
        if i==len(nums)-1:
            print(nums[i])
        else:
            print(f"{nums[i]}+",end="")
    

    # write your code here

if __name__ == '__main__':
    
    sys.setrecursionlimit(1 << 30)
    threading.stack_size(1 << 27)

    main_thread = threading.Thread(target=main)
    main_thread.start()
    main_thread.join()