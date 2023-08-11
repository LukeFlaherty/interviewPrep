class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        result = ""
        i = 0

        while i < len(word1) or i < len(word2):
            if i < len(word1):
                result += word1[i]
            if i < len(word2):
                result += word2[i]
            i += 1
        return result
# get a result string
# get a counter for while loop
# while loop through until end or strs
# get a waterfall if statement for appending letters
# increment i
