class TimeMap:

    def __init__(self):
        self.map = {}
        
    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.map:
            self.map[key] = []

        
        self.map[key].append((timestamp, value))
        

    def get(self, key: str, timestamp: int) -> str:

        if key not in self.map:
            return ""

        data = self.map[key]

        l, r = 0, len(data) - 1

        result = ""
        while l <= r:
            m = (l + r) // 2

            if data[m][0] == timestamp:
                return data[m][1]

            elif data[m][0] < timestamp:
                result = data[m][1]
                l = m + 1

            else:
                r = m - 1

        
        return result