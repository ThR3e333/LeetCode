class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        '''
        Moves all zeros in the given list to the end of the list while keeping the relative order of the
        non-zero elements unchanged. The list is modified in-place, and returns nothing.

        :param nums: The list of integers to be modified.
        :return: None.
        '''
        # Use two pointers to traverse the list
        slow, fast = 0, 1
        while fast < len(nums):
            # If the slow pointer is pointing to a 0 and the fast pointer is pointing to a non-zero element,
            # swap the elements at the slow and fast pointers
            if nums[slow] == 0 and nums[fast] != 0:
                nums[slow], nums[fast] = nums[fast], nums[slow]

            # If the slow pointer is pointing to a non-zero element, move the slow pointer to the right
            if nums[slow] != 0:
                slow += 1

            # Move the fast pointer to the right
            fast += 1