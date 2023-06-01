class Solution:
    def splitString(self, s: str) -> bool:
        def sol(idx, prv):
            if idx == len(s):
                return True
            for j in range(idx, len(s)):
                val = int(s[idx:j+1])
                if val+1 == prv and sol(j+1, val):
                    return True
        n = len(s)-1
        for i in range(n):
            val = int(s[:i+1])

            if sol(i+1,val):
                return True
        return False
