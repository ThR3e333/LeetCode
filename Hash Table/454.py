class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        '''
        Returns the number of quadruplets (i, j, k, l) such that:
        nums1[i] + nums2[j] + nums3[k] + nums4[l] == 0
        :param nums1: List of integers
        :param nums2: List of integers
        :param nums3: List of integers
        :param nums4: List of integers
        :return: The number of quadruplets
        '''

        sum_count = dict()
        count = 0

        # Compute the counts of sums of all possible pairs of elements from nums1 and nums2
        for i in nums1:
            for j in nums2:
                if (i+j) in sum_count:
                    sum_count[i+j] += 1
                else:
                    sum_count[i+j] = 1


        # Count the number of quadruplets with the desired property by checking all pairs of elements
        # from nums3 and nums4 whose sum is the negation of a sum computed in the previous loop
        for i in nums3:
            for j in nums4:
                if -(i+j) in sum_count:
                    count += sum_count[-(i+j)]

        return count