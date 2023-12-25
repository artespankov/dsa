def fact_rec(n: int):
    """
    5! = 5 * 4 * 3 * 2 * 1 = 120
    """
    if n <= 1:
        return 1
    return n * fact_rec(n-1)


def fact(n):
    ans = 1
    while n > 1:
        ans *= n
        n -= 1
    return ans

print(fact_rec(5))
print(fact(5))
