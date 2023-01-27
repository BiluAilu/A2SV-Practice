class Solution:
    def isPalindrome(self, s: str) -> bool:
        filtered= ''.join(filter(str.isalnum, s)).lower()
        reverse=filtered[::-1]
        print(filtered)
        print(reverse)

        return reverse==filtered