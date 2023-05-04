class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        '''
        Removes all instances of a given value from a list in-place, and returns the length of the updated list.

        :param nums: The list of integers from which the instances of the given value are to be removed.
        :param val: The value to ba removed from the list.
        :return: The length of the updated list after removing all instances of the given value.
        '''
        # Use two pointers to traverse the list
        slow, fast = 0, 0
        while fast < len(nums):

            # If the current element is not the value to be removed, move it to the slow index and increment slow
            if nums[fast] != val:
                nums[slow] = nums[fast]
                slow += 1

            # Increment fast to continue traversing the list
            fast += 1

        return slow