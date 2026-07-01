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

        l, r = 0, len(data) - 1

        index = -1
        while l <= r:
            m = (l + r) // 2

            if data[m][0] == timestamp:
                return data[m][1]

            elif data[m][0] < timestamp:
                index = m
                l = m + 1

            else:
                r = m - 1

        
        return "" if index == -1 else data[index][1]