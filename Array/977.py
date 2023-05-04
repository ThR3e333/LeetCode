class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        '''
        Returns a list of squares of the value in the input list, sorted in ascending order.

        :param nums: The input list of integers.
        :return: The list of squares of value in 'nums', sorted in ascending order.
        '''
        n = len(nums)
        left, right, result_index = 0, n-1, n-1
        result = [-1] * n

        # Traverse the list from both ends and populate the result list in descending order
        while left <= right:
            left_square = nums[left]**2
            right_square = nums[right]**2

            # If the squared value pointed to by left is greater than that pointed to by right,
            # store the squared value pointed to by left in the result list
            if left_square > right_square:
                result[result_index] = left_square
                left += 1

            # Store the squared value pointed to by right in the result list
            else:
                result[result_index] = right_square
                right -= 1
            result_index -= 1

        return result