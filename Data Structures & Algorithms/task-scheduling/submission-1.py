class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counter = Counter(tasks)
        max_frequency = max(counter.values())
        res = (max_frequency - 1) * (n + 1)

        for task in counter:
            if counter[task] == max_frequency:
                res += 1
        
        return max(res, sum(counter.values()))