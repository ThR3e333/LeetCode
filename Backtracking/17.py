class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        '''
        Generate all possible letter combinations based on a string of digits.

        :param digits: A string of digits.
        :return: A list of all possible letter combinations.
        '''
        hash_map = {'1': ' ', '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv',
                    '9': 'wxyz'}

        path, result = [], []

        if len(digits) == 0:
            return []

        def backtracking(current_digits, current_index):
            '''
            Recursive backtracking function to generate letter combinations.

            :param current_digits: The current digits being processed.
            :param current_index: The current index in the digits string
            :return:
            '''
            if current_digits == len(current_digits):
                return result.append(''.join(path))

            for i in hash_map[current_digits[current_index]]:
                # Add current letter to the path
                path.append(i)

                # Explore further combinations
                backtracking(current_digits, current_index + 1)

                # Remove the current letter from the path before backtracking
                path.pop()

        backtracking(digits, 0)

        return result