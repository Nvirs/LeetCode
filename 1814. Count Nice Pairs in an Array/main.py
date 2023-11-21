class Solution:
    def countNicePairs(self, nums: List[int]) -> int:
    #nums[i] + rev(nums[j]) == nums[j] + rev(nums[i])   
    #nums[i] - rev(nums[j]) == nums[j] - rev(nums[i])   
        MOD = 10 ** 9 + 7
        def rev(x):
            return int(str(x)[::-1])
        total = 0
        c = collections.Counter()
        for x in nums:
            current = x - rev(x)
            total += c[current]
            total %= MOD
            c[current] += 1
        return total % MOD
