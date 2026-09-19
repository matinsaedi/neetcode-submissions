class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        if len(s1) > len(s2):
            return False

        count1 = [0] * 26
        count2 = [0] * 26

        for s in s1:
            count1[ord(s) - ord('a')] += 1

        l = 0
        substring = s2[l : l + len(s1)]
        for s in substring:
            count2[ord(s) - ord('a')] += 1

        if count1 == count2:
            return True

        for l in range(len(s1), len(s2)):
            count2[ord(s2[l]) - ord('a')] += 1
            count2[ord(s2[l - len(s1)]) - ord('a')] -= 1

            if count1 == count2:
                return True

        return False