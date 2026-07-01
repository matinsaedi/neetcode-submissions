class TimeMap:

    def __init__(self):
        self.map = dict()
        
    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.map:
            entry = (timestamp, value)
            self.map[key].append(entry)

        else:
            self.map[key] = [(timestamp, value)]
        

    def get(self, key: str, timestamp: int) -> str:

        if key not in self.map:
            return ""
            
        data = self.map[key]
        stamps = [t for t, _ in data]
        values = [v for _, v in data]

        l, r = 0, len(stamps) - 1

        index = -1
        while l <= r:
            m = (l + r) // 2

            if stamps[m] == timestamp:
                return values[m]

            elif stamps[m] < timestamp:
                index = m
                l = m + 1

            else:
                r = m - 1

        
        return "" if index == -1 else values[index]

 # [(1, "math"), (4, "cs"), (10, "ai")]