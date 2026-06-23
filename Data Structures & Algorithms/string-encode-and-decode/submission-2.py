class Solution:

    def encode(self, strs: List[str]) -> str:

        output = ""
        for s in strs:
            output += str(len(s)) + "#" + s

        return output


    def decode(self, s: str) -> List[str]:

        output = []

        i = 0
        while i < len(s):

            length = ""
            while s[i] != "#":
                length += s[i]
                i += 1

            i += 1
            length = int(length)
            string = s[i:i+length]
            output.append(string)
            i += length
        
        return output