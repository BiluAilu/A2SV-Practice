class Solution:
    # def largestMerge(self, word1: str, word2: str) -> str:
    #     def lexicalGreater(w1,w2):
    #         u=0
    #         d=0
    #         while u<len(w1) and d<len(w2):
    #             if w1[u]==w2[d]:
    #                 u+=1
    #                 d+=1
    #             elif w1[u]>w2[d]:
    #                 return True
    #             else:
    #                 return False




        w1=0
        w2=0
        word1=list(word1)
        word2=list(word2)
        merge=[]
        while word1 and word2:
            if word1[0:]>=word2[0:]:
                merge.append(word1[0])
                word1.pop(0)
            # elif word1[0]==word2[0]:
            #     e=lexicalGreater(word1,word2)
            #     if e:
            #         merge.append(word1[0])
            #         word1.pop(0)
            #     else:
            #         merge.append(word2[0])
            #         word2.pop(0)

            else:
                merge.append(word2[0])
                word2.pop(0)
        while word1:            
                merge.append(word1[0])
                word1.pop(0)
        while word2:
                merge.append(word2[0])
                word2.pop(0)
        
        return "".join(merge)


