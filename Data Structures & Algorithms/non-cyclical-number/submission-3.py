class Solution:
    def isHappy(self, n: int) -> bool:
        cache = set()
        
        while n != 1 :
            if n in cache :
                return False
                
            cache.add(n)
            # temp = n
            # n = 0

            '''
            for d in str(temp) :
                print(d)
                n += int(d) ** 2
                print(n)
            '''
            output = 0
            while n : 
                digit = n % 10
                digit = digit ** 2
                output += digit
                n = n // 10
            n = output

        
        return True
