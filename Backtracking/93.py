class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        global path, result
        path, result = [], []
        def backtracking(s, startIndex):
            if startIndex == len(s) and len(path) == 4:
                return result.append('.'.join(path))
            for i in range(startIndex, len(s)):
                temp = s[startIndex:i+1]
                if len(path) > 3:
                    break
                if (int(temp)<256 and int(temp)>0 and temp[0]!='0') or (temp == '0'):
                    path.append(temp)
                    backtracking(s, i+1)
                    path.pop()
        backtracking(s, 0)
        return result