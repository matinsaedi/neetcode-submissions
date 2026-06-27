class Solution:
    def isValid(self, s: str) -> bool:

        stack = []
        hash_map = {")": "(", "]": "[", "}": "{"}

        for c in s:
            if c in "([{":
                stack.append(c)

            elif c in ")]}":
                if not stack or stack[-1] != hash_map[c]:
                    return False

                stack.pop()

        return not stack