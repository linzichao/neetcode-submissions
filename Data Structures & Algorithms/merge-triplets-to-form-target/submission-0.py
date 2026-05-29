class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        tx, ty, tz = target

        for triple in triplets[:]:
            x, y, z = triple
            if x > tx or y > ty or z > tz:
                triplets.remove(triple)
        
        mx = my = mz = -1
        for triple in triplets:            
            x, y, z = triple
            mx = max(mx, x)
            my = max(my, y)
            mz = max(mz, z)

        return mx == tx and my == ty and mz == tz