class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        def sort(nums):
            nums.sort()
            return len(set(nums[i]-nums[i-1] for i in range(1,len(nums))))==1
        return [sort(nums[i:j+1]) for i,j in zip(l,r)]
      
