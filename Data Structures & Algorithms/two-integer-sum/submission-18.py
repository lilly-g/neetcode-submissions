class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        s = set(nums)

        for i in range(len(nums)) :
            n = target - nums[i]

            if n in s :
                # TODO: skip index if itself
                if nums[i] != n :
                    return [i, nums.index(n)]
                print(n)
                print(nums[i])
                print(len(nums))

                if n in nums[i+1:] :
                    i2 = nums.index(n, i+1, len(nums))
                    if i2 != i :
                        return [i, i2]               
        
        return -1