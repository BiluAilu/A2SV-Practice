
class Solution:
    def printVertically(self, s: str) -> List[str]:
        """
        "HOW ARE YOU"
        ["HOW, ARE,  YOU"]
        """
        arr = s.split(' ')
        k = 1
        result = []
        i = 0
        while i < k:
            l = []
            for word in arr:
                k = max(k, len(word))
                l.append(word[i] if i < len(word) else ' ')
                print(l)
            result.append(''.join(l).rstrip())
            print(result)
            i += 1