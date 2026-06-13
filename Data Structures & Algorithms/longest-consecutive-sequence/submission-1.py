class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums: return 0
        nums_set = set(nums)
        res = 0

        for n in nums_set:
            if n - 1 not in nums_set:
                curr = n
                count = 1
                while curr + 1 in nums_set:
                    curr += 1
                    count += 1
                res = max(res, count)

        return res
