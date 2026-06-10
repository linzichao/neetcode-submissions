class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i = res = 0
        d = defaultdict(int)

        for j, c in enumerate(s):
            if c in d:
                while d[c] > 0 and i < j:
                    d[s[i]] -= 1
                    i += 1
            
            res = max(res, j - i + 1)
            d[c] += 1
        
        return res