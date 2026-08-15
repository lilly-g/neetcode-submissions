class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = 0

        for i in nums :
            res = res ^ i

            print("i: " + str(i))
            print("res: " + str(res))

        return res