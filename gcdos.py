# https://github.com/doocs/leetcode/blob/main/solution/1000-1099/1071.Greatest%20Common%20Divisor%20of%20Strings/README_EN.md

class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if str1 + str2 != str2 + str1: return ""

        return str1[:gcd(len(str1), len(str2))]

    # TEST if the strings added togarther are not equal if so ret ""
    # use gcd method on strs
    # return str1 sliced after n
