class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        out=[]
        for i in arr2:
            for j in range(arr1.count(i)):
                out.append(i)
        rest=sorted([item for item in arr1 if item not in arr2])
        out.extend(rest)
        return out