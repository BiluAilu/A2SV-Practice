class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        
        """
        self.s=s[::-1]
        s.clear()
        s.extend(self.s)