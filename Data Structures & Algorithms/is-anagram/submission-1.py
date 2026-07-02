class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        alph_dict = {}
        for i in s:
            alph_dict[i] = alph_dict.get(i,0) + 1
        
        for i in t:
            if i not in alph_dict or alph_dict[i] == 0:
                return False
            alph_dict[i] -= 1
        return True