class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        "xvzyazhjl"
        # {x: 0, v: 1, z: 2, y: 3, a: 4}
        visited = set()
        length = 0

        left = 0
        for right in range(len(s)):

            while s[right] in visited:
                visited.remove(s[left])
                left += 1

            visited.add(s[right])
            length = max(length, right - left + 1)

        return length


            