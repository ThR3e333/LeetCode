class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        '''
        Reverse the first k characters for every 2k characters.

        :param s: Input string.
        :param k: The number of characters to reverse at a time.
        :return: The modified string with the first k characters reversed for every 2k characters.
        '''
        # Initialize the pointer to 0
        p = 0
        while p < len(s):
            p2 = p + k

            # Reverse the k characters in slice s[p:p2], and concatenate the resulting string with s[p2:]
            s = s[:p] + s[p:p2][::-1] + s[p2:]

            # Increment p by 2k
            p = p + 2*k

        return s