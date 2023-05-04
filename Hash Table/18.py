class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        '''
        Given an array nums of n integers and an integer target,
        returns all unique quadruplets [nums[a], nums[b], nums[c], nums[d]]
        such that a, b, c, and d are distinct indices in nums and
        nums[a] + nums[b] + nums[c] + nums[d] == target.

        :param nums: List of integers.
        :param target: Target of four numbers.
        :return: List of lists, where each list is a unique triplet of integers that sum to 0.
        '''
        nums = sorted(nums)
        quadroplets = []

        # Use two nested loop to fix two numbers and covert the problem to twoSum
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue

            for j in range(i+1, len(nums)):
                if j > i+1 and nums[j] == nums[j-1]:
                    continue

                # Use two pointers to search for the remaining two numbers
                p = j + 1
                q = len(nums) - 1
                while p < q:
                    if nums[i] + nums[j] + nums[p] + nums[q] > target:
                        q -= 1
                    elif nums[i] + nums[j] + nums[p] + nums[q] < target:
                        p += 1
                    else:
                        quadroplets.append([nums[i], nums[j], nums[p], nums[q]])

                        # Skip duplicate elements to avoid duplicate quadroplets
                        while p < q and nums[p] == nums[p+1]:
                            p += 1
                        while p < q and nums[q] == nums[q-1]:
                            q -= 1
                        p += 1
                        q -= 1

        return quadroplets