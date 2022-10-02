class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dt = {i:nums.index((target - x),i+1) for i,x in enumerate(nums) if ((target-x) in nums and (target - x) != x)}
        return list(dt.items()[0])
