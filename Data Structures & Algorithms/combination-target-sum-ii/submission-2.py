class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []

        def dfs(i, path):
            s = sum(path)

            if s == target:
                res.append(path)
                return
            elif s < target:
                for j in range(i, len(candidates)):
                    if j > i and candidates[j] == candidates[j - 1]:
                        continue
                    dfs(j + 1, path + [candidates[j]])
            return
        
        dfs(0, [])
        return res
