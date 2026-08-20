class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # add 1 
        end = len(digits) - 1
        digits[end] += 1

        # adjust
        for i in range(end, 0, -1) :
            print(i)
            while digits[i] > 9 :
                print('bye')
                digits[i] = 0
                digits[i-1] += 1
        
        if digits[0] > 9 :
            digits = [1, 0] + digits[1:]

        return digits
        