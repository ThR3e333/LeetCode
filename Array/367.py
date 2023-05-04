# Approach 1

class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        '''
        Determine whether a given number is a perfect square.

        :param num: An integer to be checked for perfect squareness.
        :return: A boolean indicating whether 'num' is a perfect square.
        '''
        # Special case: 1 is a perfect square
        if num == 1:
            return True
        # Initialize search range
        left, right = 0, num // 2

        # Binary search for the square root of 'num'
        while left <= right:
            mid = (left + right) // 2
            if mid**2 < num:
                left = mid + 1      # The square root is in the right half
            elif mid**2 > num:
                right = mid - 1     # The square root is in the left half
            else:
                return True     # If the square of the midpoint is equal to the 'num', num is a perfect square

        # The entire range is searched, 'num' is not a perfect square
        return False

# Approach 2

class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num == 1:
            return True
        else:
            left, right = 0, num // 2 + 1
            while left < right:
                mid = (left + right) // 2
                if mid**2 < num:
                    left = mid + 1
                elif mid**2 > num:
                    right = mid
                else:
                    return True
            return False