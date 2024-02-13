class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        for word in words:
            for i in range(len(word)):
                if word[i] != word[-1-i]:
                    break
            else:return word
        return ""
