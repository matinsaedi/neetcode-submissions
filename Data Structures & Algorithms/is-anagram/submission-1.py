class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        dict_s = {}
        dict_t = {}

        for char in s:
            if char in dict_s:
                dict_s[char] += 1
            else:
                dict_s[char] = 1

        for char in t:
            if char in dict_t:
                dict_t[char] += 1
            else:
                dict_t[char] = 1

        if len(dict_s) != len(dict_s):
            return False

        else:
            for char in dict_s:
                if char not in dict_t or dict_s[char] != dict_t[char]:
                    return False

            for char in dict_t:
                if char not in dict_s or dict_s[char] != dict_t[char]:
                    return False
            
        
        return True

            