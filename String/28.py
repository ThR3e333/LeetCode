class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        '''
        Find the first occurrence of a substring in a string using KMP algorithm.

        :param haystack: The string to search in.
        :param needle: The string to find.
        :return: The index of the first occurrence of the substring in the string, or -1 if not found.
        '''

        def getNext(needle):
            '''
            Compute the next array used in the KMP algorithm.
            :param needle: The string to find.
            :return: The 'next' array.
            '''

            next_array = [0] * len(needle)
            j = 0
            next_array[0] = j

            for i in range(1, len(needle)):
                # If needle[i] is not equal to needle[j], then move j back to next_array[j-1]
                while j >= 1 and needle[i] != needle[j]:
                    j = next_array[j - 1]
                # If needle[i] is equal to needle[j], the increment j
                if needle[i] == needle[j]:
                    j += 1
                # Store the value of j in next_array[i]
                next_array[i] = j

            return next_array

        # If the needle is empty, then return 0
        if len(needle) == 0:
            return 0

        # Generate the next array
        next_array = getNext(needle)
        j = 0

        for i in range(len(haystack)):
            # If haystack[i] is not equal to needle[j], the move j back to next_array[j-1]
            while j >= 1 and haystack[i] != needle[j]:
                j = next_array[j - 1]

            # If haystack[i] is equal to needle[j], then increment j
            if haystack[i] == needle[j]:
                j += 1

            # If j is equal to the length of the needle, then the needle is found
            if j == len(needle):
                return i - len(needle) + 1

        return -1

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        '''
        Find the first occurrence of a substring in a string using KMP algorithm.

        :param haystack: The string to search in.
        :param needle: The string to find.
        :return: The index of the first occurrence of the substring in the string, or -1 if not found.
        '''

        def getNext(needle):
            '''
            Compute the next array used in the KMP algorithm.
            :param needle: The string to find.
            :return: The 'next' array.
            '''
            next_array = [-1]*len(needle)
            i, j = 0, -1
            while i < len(needle) - 1:
                if j == -1 or needle[i] == needle[j]:
                    i += 1
                    j += 1
                    next_array[i] = j
                else:
                    j = next_array[j]
            return next_array
        i, j = 0, 0
        next_array = getNext(needle)
        while i < len(haystack) and j < len(needle):
            if j == -1 or haystack[i] == needle[j]:
                i += 1
                j += 1
            else:
                j = next_array[j]
        return i-j if j == len(needle) else -1