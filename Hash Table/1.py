class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        '''
        Given a array of integers 'nums' and an integer 'target', return indices of two numbers such that they add up to the 'target'.
        Assumue that there are exactly two numbers in 'nums' that add up to 'target'.

        :param nums: List of integer.
        :param target: Target of two numbers.
        :return: List of two integer, representing the indices of the two numbers in 'nums' that add up to 'target'.
        '''
        # Create a dictionary to store each number in 'nums' and its index
        num_indices = dict()
        for index, num in enumerate(nums):
            # If the difference between 'target' and the current number exists in the dictionary
            # Return the indices of the two numbers that add up to 'target'
            if target - num in num_indices:
                return [num_indices[target - num], index]

            # Otherwise, add the current number to the dictionary with its index as the value
            else:
                num_indices[num] = index

        # If no two numbers in 'nums' add up to 'target', return empty list
        return []