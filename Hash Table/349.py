class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        '''
        Returns the intersection of two lists of integers.

        :param nums1: List of integers.
        :param nums2: List of integers.
        :return: List of integers representing the intersection of 'nums1' and 'nums2'.
        '''
        num_dict, intersection = {}, []

        # Add the values of num1 to the dictionary
        for num in nums1:
            num_dict[num] = 1

        # Check if each value in nums2 is in the dictionary. If so, add it to the result list and mark it as found
        for num in nums2:
            if num in num_dict.keys() and num_dict[num] == 1:
                intersection.append(num)
                num_dict[num] = 0

        return intersection