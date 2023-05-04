class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        '''
        Determine if 'ransomNote' can be constructed from 'magazinea.

        :param ransomNote: A string representing the ransom note.
        :param magazine: A string representing the magazine containing characters to construct the ransom note.
        :return: True if the ransom note can be constructed from magazine, False otherwise.
        '''
        # Create an empty dictionary to store the counts of characters in the magazines
        char_count = dict()

        # Count the occurrences of each character
        for char in magazine:
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1

        for char in ransomNote:
            # If the character is not in the magazine or there are no more instances of it, return False
            if char not in char_count.keys() or char_count[char] <= 0:
                return False
            # Otherwise, decrement the the count of the character in the magazine
            char_count[char] -= 1

        # The ransom note can be constructed
        return True 