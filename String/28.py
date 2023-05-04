class Solution:
    def strStr(self, haystack: str, needle: str) -> int:

        def getNext(needle):
            next = [0] * len(needle)
            j = 0
            next[0] = j
            for i in range(1, len(needle)):
                while j >= 1 and needle[i] != needle[j]:
                    j = next[j - 1]
                if needle[i] == needle[j]:
                    j += 1
                next[i] = j
            return next

        if len(needle) == 0:
            return 0
        next = getNext(needle)
        j = 0
        for i in range(len(haystack)):
            while j >= 1 and haystack[i] != needle[j]:
                j = next[j - 1]
            if haystack[i] == needle[j]:
                j += 1
            if j == len(needle):
                return i - len(needle) + 1
        return -1

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        def getNext(needle):
            next = [-1]*len(needle)
            i, j = 0, -1
            while i < len(needle) - 1:
                if j == -1 or needle[i] == needle[j]:
                    i += 1
                    j += 1
                    next[i] = j
                else:
                    j = next[j]
            return next
        i, j = 0, 0
        next = getNext(needle)
        while i < len(haystack) and j < len(needle):
            if j == -1 or haystack[i] == needle[j]:
                i += 1
                j += 1
            else:
                j = next[j]
        return i-j if j == len(needle) else -1