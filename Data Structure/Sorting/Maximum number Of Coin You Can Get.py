class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        '''
        [2 4 1 2 7 8]
        
        '''
        sum=0
        piles.sort()
        lp,rp=0,len(piles)-1
        while(lp<rp):
            sum+=piles[rp-1]
            rp-=2
            lp+=1
        return sum
