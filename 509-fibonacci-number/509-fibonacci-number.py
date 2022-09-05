class Solution:
    def fib(self, n: int) -> int:
        if n==1 or n==2:
            return 1
        bot_up = [0 for i in range(n+1)]
        bot_up[1] = 1
        for i in range(2,n+1):
            bot_up[i] = bot_up[i-1]+bot_up[i-2]
        return bot_up[-1]
