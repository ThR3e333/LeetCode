# Approach 1, [left, right]

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        '''
        Search for target value in a sorted list of integers using binary search.

        :param nums: A sorted list of integers.
        :param target: The integer value to search for in the list.
        :return: The index of the target value in the list, if found. Otherwise, return -1.
        '''
        # Initialize search range, closed interval [left, right]
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2
            if nums[mid] < target:  # The target is in the right half, so the closed interval becomes [mid + 1, right]
                left = mid + 1
            elif nums[mid] > target:    # The target is in the left half, so the closed interval becomes [left, mid - 1]
                right = mid - 1
            else:
                return mid      # The target value is found.
        return -1

# Approach 2, [left, right)

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        '''
        Search for target value in a sorted list of integers using binary search.

        :param nums: A sorted list of integers.
        :param target: The integer value to search for in the list.
        :return: The index of the target value in the list, if found. Otherwise, return -1.
        '''
        # Initialize search range, left-open interval [left, right)
        left, right = 0, len(nums)

        while left < right:     # the target is in [left, right), if left == right, the index is out of range
            mid = (left + right) // 2
            if nums[mid] < target:      # The target is in the right half, so the left-open interval becomes [mid + 1, right)
                left = mid + 1
            elif nums[mid] > target:    # The target is in the left half, so the closed interval becomes [left, mid)
                right = mid
            else:
                return mid      # The target value is found
        return -1
