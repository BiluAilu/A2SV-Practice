class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        letter={}
        result=[]
        for word in words:
            for ch in word:
                if ch in letter:
                    letter[ch]+=1
                else:
                    letter[ch]=1
        print(letter)
        for i in letter:
            if letter[i]>=len(words):
                result.append(i)
        print(result)
