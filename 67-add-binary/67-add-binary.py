class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a = list(a)
        b = list(b)
        extra = 0
        output = ""
        
        while a or b or extra:
            if a:
                extra += int(a.pop())
            if b:
                extra += int(b.pop())

            output += str(extra %2)
            extra //= 2

        return output[::-1]