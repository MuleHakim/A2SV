class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        pow2 = []
        for i in range(31):
            tmp1 = sorted(list(str(2**i)))
            pow2.append("".join(tmp1))
        tmp2 = sorted(list(str(n)))
        if "".join(tmp2) in pow2:
            return True
        return False