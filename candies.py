class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        result = []
        maxCandies = max(candies)

        for i in range(len(candies)):
            if candies[i] + extraCandies >= maxCandies:
                result.append(True)
            else:
                result.append(False)

        return result


#         Find the maximum of the array and store it as maxCandies
# Initialize a boolean result array
# Run a loop from the start of the array to its end:
# If the current number of candies of ith child + extra candies is greater than or equal to maxCandies:
# Set the result of this child as true, false otherwise
# Print the result

# https://tutorialcup.com/leetcode-solutions/kids-with-the-greatest-number-of-candies-leetcode-solution.htm



class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        maxCandies = max(candies)
        result = []

        for i in range(len(candies)):
            if candies[i] + extraCandies >= maxCandies:
                result.append(True)
            else:
                result.append(False)

        return result


#         Find the maximum of the array and store it as maxCandies
# Initialize a boolean result array
# Run a loop from the start of the array to its end:
# If the current number of candies of ith child + extra candies is greater than or equal to maxCandies:
# Set the result of this child as true, false otherwise
# Print the result

# https://tutorialcup.com/leetcode-solutions/kids-with-the-greatest-number-of-candies-leetcode-solution.htm
