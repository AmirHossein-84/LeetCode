class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict = {}
        for i in strs:
            key = tuple(sorted(i))
            if key not in dict:
                dict[key] = []
            dict[key].append(i)
        return list(dict.values())