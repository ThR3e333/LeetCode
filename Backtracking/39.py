class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        '''
        Find all unique combinations of candidates that sum up to the target.

        :param candidates: A list of candidates integers.
        :param target: The target sum to reach.
        :return: A list of all unique combinations.
        '''
        def backtracking(candidates, target):
            '''
            Recursive backtracking function to find all unique combinations.

            :param candidates: The remaining candidates to consider.
            :param target: The remaining target sum.
            '''
            if sum(path) > target:
                return
            if sum(path) == target:
                return result.append(path[:])

            for i in range(len(candidates)):
                if sum(path) + candidates[i] > target:
                    return

                # Add the current candidate to the path
                path.append(candidates[i])

                # Explore further combinations
                backtracking(candidates[i:], target)

                # Remove the current candidate from the path before backtracking
                path.pop()

        path, result = [], []

        candidates.sort()

        backtracking(candidates, target)

        return result