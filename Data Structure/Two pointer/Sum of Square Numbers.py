class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        '''
        start a=1
        b=c-1

        l=[0,1,2,....,sqr(c)]

        '''
        
        l,r=0,int(sqrt(c))+1

        while l<=r:
            if l*l+r*r==c:
                return True
            elif l*l+r*r<c:
                l+=1
            else:
                r-=1
        return False
        