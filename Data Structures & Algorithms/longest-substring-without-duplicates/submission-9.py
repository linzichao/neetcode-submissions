class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        index = {}
        start = res = 0

        for i, c in enumerate(s):
            if c in index and start <= index[c]:
                start = index[c] + 1
            res = max(res, i - start + 1)
            index[c] = i
        
        return res 