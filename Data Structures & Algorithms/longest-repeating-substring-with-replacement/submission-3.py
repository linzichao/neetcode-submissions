class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counter = Counter()
        start = res = 0

        for end, c in enumerate(s):
            counter[c] += 1
            most_frequent = counter.most_common(1)[0][1]
            while end - start + 1 - most_frequent > k:
                counter[s[start]] -= 1
                start += 1
            res = max(res, end - start + 1)
        
        return res
