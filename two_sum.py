class Solution:
    def twoSum(self, nums, target):
        for i in range(len(nums)):
            c = nums[i]
            if i == 0:
                for x in range(i+1, len(nums)):
                    if c + nums[x] == target:
                        return [i, x]
            else:
                for x in range(0, i-1):
                    if c + nums[x] == target:
                        return [i, x]
                for y in range(i+1, len(nums)):
                    if c + nums[y] == target:
                        return [i, y]


s = Solution()
print(s.twoSum([1, 0, 2], 3))
