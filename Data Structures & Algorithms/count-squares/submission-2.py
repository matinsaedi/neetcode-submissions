class CountSquares:

    def __init__(self):
        self.points = {}

    def add(self, point: List[int]) -> None:
        point = tuple(point)
        if point in self.points:
            self.points[point] += 1

        else:
            self.points[point] = 1
        

    def count(self, point: List[int]) -> int:
        res = 0
        px, py = point

        for p in self.points:
            x, y = p
            if (px == x or 
                py == y or 
                abs(px - x) != abs(py - y)):
                continue
            
            if ((px, y) in self.points and 
                (x, py) in self.points):
                res += (self.points[(x, y)] * 
                        self.points[(px, y)] *
                        self.points[(x, py)]
                )
        
        return res