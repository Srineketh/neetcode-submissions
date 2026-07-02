class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for i in strs:
            encoded = encoded + "".join(str(len(i)) + '#' + i)
        return encoded

    def decode(self, s: str) -> List[str]:
        decodes = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            cur_len = int(s[i:j])
            start = j + 1
            i = start + cur_len
            decodes.append(s[start:i])
        return decodes
