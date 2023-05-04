class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        '''
        Removes duplicate elements from a sorted list in-place and returns the length of the modified list.

        :param nums: The sorted list of integers
        :return: The length of the modified list with duplicate elements removed
        '''
        # Handle empty and single-element lists
        if not nums or len(nums) == 1:
            return len(nums)

        # Initialize slow and fast pointers point to the first two elements of the list
        slow, fast = 0, 1

        # Loop through the list with the fast pointer
        while fast < len(nums):

            # If the fast pointer points to a duplicate element, move it forward
            if nums[fast] == nums[slow]:
                fast += 1

            # If the fast pointer points to a unique element, move it forward and move the unique element to the next position
            else:
                nums[slow + 1] = nums[fast]
                fast += 1
                slow += 1

        return slow + 1