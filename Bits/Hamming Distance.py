import queue
class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        print(bin(x)[2:])
        print(bin(y)[2:])
        result=0
        for i in range(0,32):
            print("x", x&(1<<i))
            print("y", y&(1<<i))
            if (x&(1<<i)!=0 and y&(1<<i)==0) or (x&(1<<i)==0 and y&(1<<i)!=0):
                result+=1
        print(result)

        return result
