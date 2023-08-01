class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:

        if n == 0: return True

        flowerbed = [0] + flowerbed + [0]

        for i in range(1, len(flowerbed)-1):
            if flowerbed[i] == 1:
                continue
            elif flowerbed[i - 1] == flowerbed[i + 1] == 0: 
                n -= 1
                flowerbed[i] = 1 
                if n == 0: return True
        
        return False
            

# [1 0 0 1 1 0 0 1]
# availableSpots >= n

# If n is 0, then return true. 

# We wrap 2 available plots to original flowerbed in case if the first plot is available. 
        # bc if the first is available we cant check in front of it making us loop twice?

# We iterate the flowerbed. Minus the added plots

# If the current plot is planted then we skip. 

# Otherwise we compare last and next plot. 
# Otherwise we see if last and next are equal

# If one of the them are not planted then we plant the flower and update the n, once n reach to 0, return true.
