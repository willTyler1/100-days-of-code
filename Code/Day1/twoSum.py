class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        for i in range(len(nums)): 
            for j in range(i+1, len(nums)):
                if nums[j] == target - nums[i]:
                    return [i,j]

cl = Solution()
print(cl.twoSum([2,7,11,15,32,64,3], 26))
