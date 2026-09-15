class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        dict_1 = {}

        for i in range(len(nums)):
            if target - nums[i] in dict_1:
                return [dict_1[target-nums[i]]+1,i+1]
            else:
                dict_1[nums[i]] = i

        