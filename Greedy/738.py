class Solution:
    def monotoneIncreasingDigits(self, n: int) -> int:
        s = list(str(n))
        for i in range(len(s)-1, 0, -1):
            if int(s[i-1]) > int(s[i]):
                s[i-1] = str(int(s[i-1])-1)
                s[i:] = '9'*(len(s)-i)
        return int(''.join(s))