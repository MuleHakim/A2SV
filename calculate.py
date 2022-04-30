class Solution:
    def calculate(self, s: str) -> int:
        inner, outer, result, operator = 0, 0, 0, '+'
        s = s.replace(" ","")
        for i in s + '+':
            if i.isdigit():
                inner = 10 * inner + int(i)
                continue
            if operator == '+':
                result += outer
                outer = inner
            elif operator == '-':
                result += outer
                outer = -inner
            elif operator == '*':
                outer = outer * inner
            elif operator == '/':
                outer = int(outer / inner)
            inner, operator = 0, i
        return result + outer
