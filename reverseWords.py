class Solution:
    def reverseWords(self, s: str) -> str:

        return " ".join(s.split()[::-1])

# reverse string by splitting sliced back to front

# loop through new reversed string and append to stack

# return stack joined with space as the splitter
