# Approach 1 [left, right]

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        '''
        Find the index of the target element in the sorted array or the index at which the target element ca be inserted.

        :param nums: A sorted list of integers.
        :param target: The integer to search for in the list.
        :return: The index of the target element or the index at which the element can be inserted.
        '''
        # Initialize left and right pointers to the start and end of the list
        left, right = 0, len(nums) - 1

        # Use binary search to find the target element
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] < target:
                left = mid + 1      # Target is in the right half
            elif nums[mid] > target:
                right = mid - 1     # Target is in the left half
            else:
                return mid      # Target is found at index mid

        # If the target is not found, return the index where it should be inserted
        return left

# Approach 2 [left, right)

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        '''
        Find the index of the target element in the sorted array or the index at which the target element ca be inserted.
        :param nums: A sorted list of integers.
        :param target: The integer to search for in the list.
        :return: The index of the target element or the index at which the element can be inserted.
        '''
        # Initialize left and right pointers to the start and end of the list
        left, right = 0, len(nums)

        # Use binary search to find the target element
        while left < right:
            mid = (left + right) // 2
            if nums[mid] < target:
                left = mid + 1      # Target is in the right half
            elif nums[mid] > target:
                right = mid     # Target is in the left half
            else:
                return mid      # Target is found

        # If the target is not found, return the index where it should be inserted
        return left
