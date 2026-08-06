class Solution:
    def isValid(self, s: str) -> bool:
        # init stack
        stack = deque()

        # dict to map brackets
        brackets = {
            '[' : ']',
            '(' : ')',
            '{' : '}'
        }

        for c in s :
            if c in brackets:
                stack.append(c)
            else :
                if not stack :
                    return False

                c2 = stack.pop()
                if (brackets[c2] != c) :
                    return False
        
        if len(stack) != 0 :
            return False # unmatched brackets

        return True