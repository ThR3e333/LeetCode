class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        '''
        Given an array of integers 'nums', returns all the unique triplets '[nums[i], nums[j], nums[k]]' such that
        'i != j != k' and 'nums[i] + nums[j] + nums[k]'.

        :param nums: List of integers.
        :return: List of lists, where each list is a unique triplet of integers that sum to 0.
        '''
        # Sort the input array
        nums = sorted(nums)
        triplets = []

        for i in range(len(nums)):
            left, right = i+1, len(nums)-1

            # If the current number is greater than 0, break out of the loop
            if nums[i] > 0:
                break

            # If the current number is the same as the previous number, skip it to avoid duplicates
            if i > 0 and nums[i] == nums[i-1]:
                continue

            # Use two pointers to find the the other two elements
            while left < right:
                current_sum = nums[i] + nums[left] + nums[right]

                # If the current sum is less than 0, increase the sum by moving the left pointer to the right
                if current_sum < 0:
                    left += 1

                # If the current sum is greater than 0, decrease the sum by moving the right pointer to the left
                elif current_sum > 0:
                    right -= 1

                # One triplet is found, add it the the results list and move the pointers
                else:
                    triplets.append([nums[i], nums[left], nums[right]])

                    # Skip duplicates
                    while left != right and nums[left] == nums[left+1]:
                        left += 1
                    while left != right and nums[right] == nums[right-1]:
                        right -= 1

                    # Move pointers to the next unique value
                    left += 1
                    right -= 1

        return triplets
