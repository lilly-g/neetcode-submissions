class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre = [1] * len(nums)
        post = [1] * len(nums)
        res = [1] * len(nums)

        # left to right products
        pre[0] = nums[0]

        for i in range(1, len(nums)) :
            print
            pre[i] = nums[i] * pre[i-1]
            post[-i] = nums[-i] * post[-(i+1)]
        
        # right to left products
        post[-1] = nums[-1]

        for i in range(1, len(nums) + 1, 1) :
            post[-i] = nums[-i] * post[-(i-1)]
        

        # final array
        res[0] = post[1]
        res[-1] = pre[-2]
        for i in range(1, len(nums) - 1) :
            res[i] = pre[i-1] * post[i+1]

        return res