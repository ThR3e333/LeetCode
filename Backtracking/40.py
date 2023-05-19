# Approach 1

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        '''
        Find all unique combinations of candidates that sum up to the target, considering duplicates.

        :param candidates: A list of candidate integers.
        :param target: The target sum to reach.
        :return: A list of all unique combinations.
        '''
        def backtracking(candidates, target, start_index):
            if sum(path) > target:
                return

            if sum(path) == target:
                return result.append(path[:])

            for i in range(start_index, len(candidates)):
                if sum(path) + candidates[i] > target:
                    return

                # Skip duplicates except for the first occurrence
                if i > start_index and candidates[i] == candidates[i-1]:
                    continue

                # Add the current candidate to the path
                path.append(candidates[i])

                # Explore further combinations
                backtracking(candidates, target, i+1)

                # Remove the current candidate from the path before backtracking
                path.pop()

        path, result = [], []

        candidates.sort()
        backtracking(candidates, target, 0)

        return result

# Approach 2

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        '''
        Find all unique combinations of candidates that sum up to the target, considering duplicates.

        :param candidates: A list of candidate integers.
        :param target: The target sum to reach.
        :return: A list of all unique combinations.
        '''
        def backtracking(candidates, target, start_index):
            # Find a valid combination
            if sum(path) == target:
                return result.append(path[:])
            for i in range(start_index, len(candidates)):
                # Stop iteration if candidates are greater than the remaining target
                if sum(path) + candidates[i] > target:
                    return

                # Skip duplicates to avoid duplicate combinations
                if i > 0 and candidates[i] == candidates[i-1] and usage_list[i-1] is False:
                    continue

                # Add the current candidate to the path
                path.append(candidates[i])

                # Mark the current candidate as used
                usage_list[i] = True

                # Explore further combinations
                backtracking(candidates, target, i+1)

                # Mark the current candidate as unused before backtracking
                usage_list[i] = False

                # Remove the current candidate from the path before backtracking
                path.pop()

        path, result = [], []

        # Track the usage of candidates
        usage_list = [False]*len(candidates)
        candidates.sort()

        backtracking(candidates, target, 0)

        return result