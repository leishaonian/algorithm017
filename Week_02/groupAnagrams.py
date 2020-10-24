class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}
        for w in strs:
            chs = tuple(sorted(w))
            d[chs] = d.get(chs, []) + [w]
            
        return sorted(d.values())
