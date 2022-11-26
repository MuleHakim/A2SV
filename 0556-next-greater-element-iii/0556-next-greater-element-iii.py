class Solution:
    def nextGreaterElement(self, n: int) -> int:
        ans = list(str(n))
        i = j = len(ans)-1
        while i and ans[i] <= ans[i-1]:
            i -= 1
        if i == 0:
            return -1
        while ans[j] <= ans[i-1]:
            j -= 1
        ans[i-1], ans[j] = ans[j], ans[i-1]
        ans[i:] = ans[i:][::-1]
        res = "".join(ans)
        return res if int(res) < 2**31 else -1