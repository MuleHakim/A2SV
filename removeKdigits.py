class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        if len(num) <= k:
            return "0"
        digits = list(num)
        monoStack = []
        while digits and k:
            if not monoStack:
                monoStack.append(digits.pop(0))
            else:
                currDigit = digits.pop(0)
                while k and monoStack and monoStack[-1] > currDigit:
                        monoStack.pop()
                        k -= 1
                monoStack.append(currDigit)

        while k:
            monoStack.pop()
            k-=1
        
        digits = monoStack + digits
        while digits and digits[0] == "0":
            digits.pop(0)
        
        if not digits:
            return "0" 
        else:
            return "".join(digits)
