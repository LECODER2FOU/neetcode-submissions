class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash = {}
        result = []
        for i in range(len(nums)):
            dif = target - nums[i]
            if dif in hash:
                result.append(hash[dif])
                result.append(i)
                return result
            hash[nums[i]] = i