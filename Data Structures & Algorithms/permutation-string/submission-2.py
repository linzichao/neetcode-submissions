class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        c1 = Counter(s1)

        i = 0
        c2 = defaultdict(int)
        for j, c in enumerate(s2):
            if c1 == c2:
                return True
            if c not in c1:
                c2 = defaultdict(int)
                i = j + 1
                continue
            
            c2[c] += 1

            while c2[c] > c1[c]:
                c2[s2[i]] -= 1
                i += 1


        return c1 == c2