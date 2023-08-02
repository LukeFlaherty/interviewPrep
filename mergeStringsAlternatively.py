class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        
        result = ""
        i = 0
        while len(word1) > i or len(word2) > i:
            if(len(word1) > i):
                result += word1[i]
            if(len(word2) > i):
                result += word2[i]

            i += 1

        return result


# get a result string
# get a counter for while loop
# while loop through until end or strs
# get a waterfall if statement for appending letters
# increment i
