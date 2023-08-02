class Solution:
    def reverseVowels(self, s: str) -> str:
        
        stackeroo = []

        result = ""

        for i in s:
            if i in 'aeiouAEIOU':
                stackeroo.append(i)
        
        for i in s:
            if i in 'aeiouAEIOU':
                result += stackeroo.pop()
            else:
                result += i

        return result




# get stack to store vowels in LIFO

# get result initalized

# loop through letters in string

# if the letter is a vowel add it to the stack

# loop through again, if letter is a vowel add it to the result str

# if its not than it still gets added to the result

