class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        result=""
        for i in range(min(len(word1),len(word2))):
            result=result+word1[i]
            result=result+word2[i]
        if(len(word1)>len(word2)):
            for i in range(min(len(word1),len(word2)),len(word1)):
                result=result+""+word1[i]
        elif(len(word1)<len(word2)):
            for i in range(min(len(word1),len(word2)),len(word2)):
                result=result+""+word2[i]
        return result
