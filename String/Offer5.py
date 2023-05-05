class Solutions:
    def replaceSpace(self, s: str) -> str:
        '''
        Replace all spaces in a given string with '%20'.

        :param s: The input string.
        :return: The modified string with all spaces replaced.
        '''
        # Count the number of spaces in the input string
        count = s.count(' ')

        # Convert string to a list of characters
        result = list(s)

        # Extend the list by 2 times of the count of spaces to accommodate '%20'
        result.extend([' ']*2*count)

        # Initialize two pointers to the end of the list
        left, right = len(s) - 1, len(result) - 1

        while left >= 0:
            # If the character is not a space, copy it to the right pointer
            if s[left] != ' ':
                result[right] = s[left]
                right -= 1

            # If the character is a space, replace it with '%20' in the list
            else:
                result[right-2:right+1] = '%20'
                right -= 3

            # Decrement the left pointer
            left -= 1

        return ''.join(result)