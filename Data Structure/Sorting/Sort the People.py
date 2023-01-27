class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:

        '''
        Selected Sort
        
        '''
        size=len(names)
        for i in range(size):
            max_idx = i
            for j in range(i + 1, size):
                if heights[max_idx] < heights[j]:
                    max_idx = j
            heights[i], heights[max_idx] = heights[max_idx], heights[i]
            names[i], names[max_idx] = names[max_idx], names[i]
        return	names