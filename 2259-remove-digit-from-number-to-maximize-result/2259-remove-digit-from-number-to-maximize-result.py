class Solution:
    def removeDigit(self, number: str, digit: str) -> str:
        if not number or not digit:
            return -1
        if digit not in number:
            return -1
        output = 0
        for i in range(len(number)):
            if number[i] == digit:
                output = max(output, int(number[:i]+number[i+1:]))
        return str(output)