class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        hash_map = {}
        for i in range(len(s)):
            hash_map[s[i]] = i
        left, right, result = 0, 0, []
        for i in range(len(s)):
            right = max(right, hash_map[s[i]])
            if right == i:
                result.append(right-left+1)
                left = i+1
        return result