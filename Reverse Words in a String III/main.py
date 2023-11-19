class Solution:
    def reverseWords(self, s: str) -> str:
        result = ''
        for j in s.split():
            result = result + j[::-1] + ' '
        return result.rstrip()
