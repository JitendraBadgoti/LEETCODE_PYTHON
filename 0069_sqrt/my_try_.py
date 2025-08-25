class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x < 2:      
            return x

        lower, upper = 0, x
        ans = 0
        while lower <= upper:
            mid = (lower + upper) // 2
            if mid * mid == x:
                return mid
            elif mid * mid < x:
                ans = mid               
                lower = mid + 1
            else:
                upper = mid - 1
        return ans