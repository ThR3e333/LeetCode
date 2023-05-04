from collections import Counter
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        '''
        Returns the intersection of two arrays as a list of integers.
        The intersection contains only elements that are common to both array.

        :param nums1: A list of integers.
        :param nums2: A list of integers.
        :return: A list of integers representing the intersections of 'nums1' and 'nums2'.
        '''
        # Determine which list is shorter and which is longer
        if len(nums1) > len(nums2):
            shorter, longer = nums2, nums1
        else:
            shorter, longer = nums1, nums2
        # Create a Counter object for the shorter list to count occurrences of each element
        count_shorter = Counter(shorter)
        result = []

        for num in longer:
            # If the current element exists in the Counter object and its count is greater than 0,
            # append the element to the result and subtract 1 from the element's count in the Counter object
            if count_shorter[num] > 0:
                result.append(num)
                count_shorter[num] -= 1

        return result