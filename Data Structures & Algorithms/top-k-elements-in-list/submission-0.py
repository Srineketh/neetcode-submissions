class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_dict = {}
        for i in nums:
            freq_dict[i] = freq_dict.get(i,0) + 1
        freq_dict = {k: v for k, v in sorted(freq_dict.items(), key=lambda item: item[1], reverse=True)}
        freq_list = list(freq_dict.keys())
        return [freq_list[i] for i in range(k)]