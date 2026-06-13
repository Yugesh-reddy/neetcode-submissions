class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sol = defaultdict(list)
        for s in strs:
            Sorted_s = ''.join(sorted(s))
            sol[Sorted_s].append(s)
        return list(sol.values())

        