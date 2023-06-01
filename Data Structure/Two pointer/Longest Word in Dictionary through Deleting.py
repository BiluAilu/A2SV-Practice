class Solution:
    def findLongestWord(self, s: str, dictionary: List[str]) -> str:
        result=[]
        for i in range(len(dictionary)):
            p=0
            k=0
            while k<len(dictionary[i]) and p<len(s):
                if s[p]==dictionary[i][k]:
                    p+=1
                    k+=1
                else:
                    p+=1
            if k==len(dictionary[i]):
                if result:
                    if len(result[0])<len(dictionary[i]):
                        result.clear()
                        result.append(dictionary[i])
                    elif len(result[0])==len(dictionary[i]):
                        result.append(dictionary[i])
                else:
                    result.append(dictionary[i])
                    
        result.sort()
        print(result)
        if result:
            return result[0]
        return ""
                
