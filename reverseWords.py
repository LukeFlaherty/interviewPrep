class Solution:
    def reverseWords(self, s: str) -> str:

        s = s.split()[::-1]

        stackeroo = []

        for i in s:
            stackeroo.append(i)

        return (" ".join(stackeroo))


        # stackeroo = s.split(" ")
        # print(stackeroo)

        # return (" ".join(stackeroo[::-1])).strip()


# split string into list (stackeroo) at spaces

# join list in reverse order using 
# (''.join(reversed(stackeroo)))

