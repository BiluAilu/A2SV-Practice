class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        l=0
        res=[]
        r=len(skill)-1
        
        while(l<=r):
            
            res.append([skill[l],skill[r]])
            
            l+=1
            r-=1
        
        s=res[0][0]+res[0][1]
        
        for i in range(1,len(res)):
            if res[i][0]+res[i][1]!=s:
                return -1
            
        result=0
        for i in range(len(res)):
            result+=res[i][0]*res[i][1]
        return result

            
