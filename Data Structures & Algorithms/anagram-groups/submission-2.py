class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        freq_dict = {}
        for i in strs:
            char_list = [0] * 26
            for j in i:
                char_list[ord(j) - ord('a')] += 1
            char_list = tuple(char_list)
            if freq_dict.get(char_list):
                freq_dict[char_list].append(i)
            else:
                freq_dict[char_list] = [i]
        return [value for key,value in freq_dict.items()]
        