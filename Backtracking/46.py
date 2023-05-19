# Approach 1

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        '''
        Generate all permutations of a list of integers.

        :param nums: A list of integers.
        :return: A list of all permutations.
        '''
        def backtracking(nums):
            '''
            Recursive backtracking function to find all permutations.

            :param nums:
            :return:
            '''
            # Found a valid permutation
            if len(path) == len(nums):
                return result.append(path[:])

            for i in nums:
                # Skip if the current number is already in the current path
                if i in path:
                    continue

                # Add the current number to the path
                path.append(i)

                # Explore further permutations
                backtracking(nums)

                # Remove the current number from the path before backtracking
                path.pop()

        path, result = [], []
        backtracking(nums)

        return result

# Approach 2

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        '''
        Generate all permutations of a list of integers.

        :param nums: A list of integers.
        :return: A list of all permutaions.
        '''
        path, result = [], []
        usage_list = [False] * len(nums)
        def backtracking(nums):
            if len(path) == len(nums):
                return result.append(path[:])
            for i in range(len(nums)):
                if usage_list[i] == True:
                    continue
                usage_list[i] = True
                path.append(nums[i])
                backtracking(nums)
                path.pop()
                usage_list[i] = False
        backtracking(nums)
        return result