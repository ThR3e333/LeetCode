class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        '''
        Given an array of strings, group anagrams together.

        :param strs: List of strings.
        :return: List of grouped anagrams.
        '''
        anagrams = dict()
        for word in strs:
            # Sort the current word alphabetically
            sorted_word = ''.join(sorted(word))

            # If the sorted string is not in the dictionary, add it with an empty list as its value
            if sorted_word not in anagrams.keys():
                anagrams[sorted_word] = []

            # Add the current string to the list of its anagrams in the dictionary
            anagrams[sorted_word].append(word)

        return list(anagrams.values())