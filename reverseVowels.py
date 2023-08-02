class Solution:
    def reverseVowels(self, s: str) -> str:
        tempVowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O','U']

        stackeroo = []

        strList = list(s)
        print(strList)

        for i in range(len(strList)):
            if strList[i] in tempVowels:
                stackeroo.append(strList[i])
            
        print(stackeroo)

        for i in range(len(strList)):
            if(strList[i] in tempVowels):
                strList[i] = stackeroo[-1]
                stackeroo.pop()

        print(strList)

        strStr = ''.join(strList)
        print(strStr)

        return strStr



# get vowels array 

# initialize stack to store vowels

# make str a list list(str)

# loop through word and add all vowels into stack as they come up LIFO

# loop through again and if [i] is in vowels array than replace with last entry in stored vowels array
