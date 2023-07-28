# loop through word1
# after iteration -> s1 = s1[:x] + 's2[x]' + s1[x:] 


class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i=0
        result =""
        while (i < len(word1)) or (i < len(word2)):

            if(i < len(word1)):
                result += word1[i]

            if(i < len(word2)):
                result += word2[i]
                
            i+=1

        print(result)
        return result
