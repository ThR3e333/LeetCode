class Solutions:
    def replaceSpace(self, s: str) -> str:
        count = s.count(' ')
        result = list(s)
        result.extend([' ']*2*count)
        left, right = len(s) - 1, len(result) - 1
        while left >= 0:
            if s[left] != ' ':
                result[right] = s[left]
                right -= 1
            else:
                result[right-2:right+1] = '%20'
                right -= 3
            left -= 1
        return ''.join(result)