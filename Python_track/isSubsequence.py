class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        current=0
        is_subsequence=True
        if(len(t)==0 and len(s)!=0):
            return False
        for index,i in enumerate(s):
            for j in range(max(current,0),len(t)):
                if(index<(len(s)-1) and i==t[current] and j==len(t)-1):
                    return False
                if(i==t[current]):
                    current+=1
                    break
                elif(current==(len(t)-1) ):
                    is_subsequence=False
                else:
                    current+=1
                    continue
            
        return is_subsequence  