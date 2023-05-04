# Approach 1

class Solution:
    def mySqrt(self, x: int) -> int:
        '''
        Given a non-negative integer x, returns the largest integer whose square root is less that or equal to x.

        :param x: The non-negative integer whose square root is to be computed.
        :return: The integer whose square is less than or equal to x.
        '''
        # If x is 1, its square root is 1
        if x == 1:
            return x

        # Set the search range for the square root to be between 2 and x/2
        else:
            left, right = 2, x // 2

            # Use binary search to find the square root
            while left <= right:
                mid = (left + right) // 2
                if mid ** 2 < x:
                    left = mid + 1      # The square root is in the right half
                elif mid ** 2 > x:
                    right = mid - 1     # The square root is in the left half
                else:
                    return mid      # The square root is found

            # If the square root is not found, return the floor of the last value of right
            return right

# Approach 2

class Solution:
    def mySqrt(self, x: int) -> int:
        '''
        Given a non-negative integer x, returns the largest integer whose square root is less that or equal to x.

        :param x: The non-negative integer whose square root is to be computed.
        :return: The integer whose square is less than or equal to x.
        '''
        # If x is 1, its square root is 1
        if x == 1:
            return x
        else:
            # Set the search range for the square root to be between 2 and x/2
            left, right = 2, x//2 + 1

            # Use binary search to find the square root
            while left < right:
                mid = (left + right) // 2
                if mid**2 < x:
                    left = mid + 1      # The square root is in the right half
                elif mid**2 > x:
                    right = mid     # The square root is in the left half
                else:
                    return mid       # The square root is found

            # When left == right, it is the last candidate before crossing the mid-point.
            # So, return the floor of the average of left and right, which is the integer square root of x.
            return (left + right)//2 - 1