class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:

        first, second = math.inf, math.inf

        for i in nums:
            if i <= first:
                first = i
            elif i <= second:
                second = i
            else:
                return True
        return False

# init two counters set to the highest number

# loop over entries of nums

# if current <= counterOne assign new val
    # first one always works to get a start

# else if current <= counterTwo assign new val

# else return True
    # because if you ever get to here than you have counterOne
    # which is icounter 2 which is j
    # and the next number is greater than both of them

# if loop finishes return False
