class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        anagramMap = {}
        results = []
        for i in strs:
            freqCount = [0] * 26
            for j in i:
                freqCount[ord(j) - ord('a')] += 1 
            anagramMap.setdefault(tuple(freqCount), []).append(i)
        for k,v in anagramMap.items():
            results.append(v)
        return results