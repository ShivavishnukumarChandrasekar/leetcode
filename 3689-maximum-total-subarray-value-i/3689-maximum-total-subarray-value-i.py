class Solution:
    def maxTotalValue(self, nums: List[int], k: int) -> int:
        mn = min(nums)

        mx = max(nums)

        best = mx - mn

        return best * k