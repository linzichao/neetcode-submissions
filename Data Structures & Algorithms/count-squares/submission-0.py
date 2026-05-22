class CountSquares:

    def __init__(self):
        self.point_count = defaultdict(int)
        self.points = []

    def add(self, point: List[int]) -> None:
        self.point_count[tuple(point)] += 1
        self.points.append(point)

    def count(self, point: List[int]) -> int:
        res = 0
        x, y = point

        for dx, dy in self.points:
            if (abs(dx - x) != abs(dy - y)) or x == dx or y == dy:
                continue
            res += self.point_count[x, dy] * self.point_count[dx, y]
        
        return res


