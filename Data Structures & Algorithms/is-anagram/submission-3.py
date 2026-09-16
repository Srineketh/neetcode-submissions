class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False

        string_1 = dict()
        string_2 = dict()

        for i in s:
            string_1[i] = string_1.get(i,0) + 1     

        for i in t:
            string_2[i] = string_2.get(i,0) + 1

        if string_1 == string_2:
            return True
        return False