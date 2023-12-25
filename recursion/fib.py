# n = 3

#    fib(3)
#   /      \
#  fib(2) fib(1)
# /    \
# fib(1) fib(0)


#       2
#   /      \
#   1   +   1
# /    \
# 1  +  0


class Solution:
    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        memo = (0, 1)
        for _ in range(2, n + 1):
            # on each step we calculate the current as
            # fib(n-1) + fib(n-2)
            fib_n_prev = memo[-1]
            fib_n = memo[-1] + memo[-2]
            # on the next step, current is going to be fib(n-1)
            # and we also need to rewrite current fib(n-2) with fib(n-1)
            # as on the next step, current fib(n-1) will be fin(n-2)
            memo = (fib_n_prev, fib_n)
        return memo[-1]

    # def fib(self, n: int) -> int:
    #     if n == 0:
    #         return 0
    #     memo = (0, 1)
    #     for _ in range(2, n+1):
    #         memo = (memo[-1], memo[-1] + memo[-2])
    #     return memo[-1]

    def fib_rec(self, n: int):
        if n == 0: return 0
        if n == 1: return 1
        return self.fib_rec(n-1) + self.fib_rec(n-2)

