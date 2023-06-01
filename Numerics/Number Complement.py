class Solution:
    def findComplement(self, num: int) -> int:
        numbin=list(bin(num)[2:])

        for i in range(len(numbin)):
            numbin[i]='0' if numbin[i]=='1' else '1'

        # print(int("".join(numbin),2))
        result=int("".join(numbin),2)
        return result