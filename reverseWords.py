class Solution:
    def reverseWords(self, s: str) -> str:

        return " ".join(s.split()[::-1])

# return space joined by s split into list spliced back ot front
