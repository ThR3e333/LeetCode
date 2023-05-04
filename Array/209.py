class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        '''
        Given a array of positive integers 'nums' and a positive integer 'target', return the minimum length of a contiguous subarray of which the sum is greater than or equal to the 'target'. If there is no such a subarray, return 0.

        :param target: A positive integer representing the target sum.
        :param nums: A list of positive integers.
        :return: The minimum length of a contiguous subarray of which the sum is greater than or equal to the 'target'.
        '''
        min_length = float('inf')       # Start with a value larger than any possible result
        current_sum = 0
        start_index = 0
        for end_index in range(len(nums)):
            current_sum += nums[end_index]

            # While the current sum is greater than or equal to target, increment j
            # and update the result as the minimum length of the subarray that sums to target
            while current_sum >= target:
                min_length = min(min_length, end_index - start_index + 1)
                current_sum -= nums[end_index]
                start_index += 1

        # Return 0 if min_length is still set to its initial value (meaning no subarray sums to target), else return min_length
        return 0 if min_length == float('inf') else min_length