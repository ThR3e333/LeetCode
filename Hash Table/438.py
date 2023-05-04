from collections import Counter
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        '''
        Find all the starting indices of p's anagrams in s.
        :param s: A string in which to search for anagrams of p.
        :param p: A string for which to find anagrams in s.
        :return: A list of starting indices of p's anagrams in s.
        '''
        # If s is shorter than p, in which case no anagrams can exist
        if len(s) < len(p):
            return []
        s_count = Counter()
        p_count = Counter(p)
        result = []
        for i in range(len(s)):
            s_count[s[i]] += 1

            # If the length of the window is greater than p, remove the leftmost element from s_count
            if i >= len(p):
                if s_count[s[i-len(p)]] == 1:
                    del s_count[s[i-len(p)]]
                else:
                    s_count[s[i-len(p)]] -= 1

            # If s_count matches p_count, and anagram of p is found, append the starting index to result
            if s_count == p_count:
                result.append(i-len(p)+1)

        return result