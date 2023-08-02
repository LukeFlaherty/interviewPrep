class Solution:
    def reverseWords(self, s: str) -> str:

        s = s.split()[::-1]

        stackeroo = []

        for i in s:
            stackeroo.append(i)

        return (" ".join(stackeroo))


# reverse string by splitting sliced back to front

# loop through new reversed string and append to stack

# return stack joined with space as the splitter



