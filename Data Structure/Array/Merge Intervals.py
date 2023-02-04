class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        '''
        [1,3]
        '''
        intervals.sort()
        print(intervals)
        k = 1
        output = [intervals[0]]
        while k < len(intervals):
            if intervals[k][0] <= output[-1][1]:
                output[-1][1] = max(output[-1][1], intervals[k][1])
            else:
                output.append(intervals[k])
            k += 1
        return output