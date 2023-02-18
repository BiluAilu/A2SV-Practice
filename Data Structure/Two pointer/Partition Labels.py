class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        counter={}
        for char in s:
            if char in counter:
                counter[char]+=1
            else:
                counter[char]=1
        prt=[]
        pointer=0
        ans=[]
        for i in range(0,len(s)):
            prt.append(s[i])
            counter[s[i]]-=1
            while counter[prt[pointer]]==0 and pointer <len(prt)-1:
                pointer+=1
            if pointer ==len(prt)-1 and counter[prt[pointer]]==0:
                ans.append(len(prt))
                pointer=0
                prt=[]
        return ans