class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        start, end, n = 1, 1, len(nums)
        result = [1]*n 
        for i in range(n):
            result[i] *= start
            start *= nums[i]
            result[~i] *= end
            end *= nums[~i]
        return result

# https://zhenyu0519.github.io/2020/02/25/lc238/

# init start end and n values where n = len of nums

# init result 

#  loop through range n
