"""
FurthestRepeatingDigram

We are given a string S consisting of N lowercase letters.
A sequence of two adjacent letters inside a string is called a digram. The distance between
two digrams is the distance between the first letter of the first digram and the first letter of the second digram.
For example, in string S = "akcmz"
the distance between digrams "kc" and "mz" is 2.
We want to find the distance between the furthest identical digrams inside string S.
Write a function:
def solution(S)
that, given a string S consisting of N letters, returns the distance between the two identical digrams in the string
that lie furthest away from each other. If there are no two identical digrams inside S, your function should return -1.
Examples:
1. Given S = "aakmaakmakda" your function should return 7. The furthest identical digrams are "ak"s, starting in positions 2 and 9 (enumerating
from 1): "aakmaakmakda".
2. Given S = "aaa" your function should return 1. The furthest identical digrams are "aa"s starting at positions 1 and 2.
3. Given S = "codility" your function should return -1. There are no two identical digrams in S.
Write an efficient algorithm for the following assumptions:
N is an integer within the range [2..300,000];
string S is made only of lowercase letters (a−z).
"""



def solution(s):
    ans = -1
    # corner cases, just in case
    if len(s) <= 2:
        return ans
    if not isinstance(s, str):
        s = str(s)

    m = {}
    for i in range(len(s) - 1):
        sub = s[i:i + 2]
        if sub not in m:
            m[sub] = i


    for i in range(len(s) - 1):
        pos = m.get(s[i:i + 2], None)
        if pos is not None and pos != i:
            ans = max(ans, i - pos)
    return ans

#
def solution(s):
    ans = -1
    last_seen = dict()
    # since on each iteration we're testing a pair of elements on positions [current index, current index+1],
    # loop should stop exactly one step before the last index in order not to cross the bounds
    for i in range(len(s) - 1):
        dgram = s[i:i + 2]
        if dgram in last_seen:
            ans = max(ans, i - last_seen[dgram])
        else:
            last_seen[dgram] = i
    return ans

if __name__ == "__main__":
    print(solution("aakmaakmakda"))
    print(solution("codility"))
    print(solution("aaa"))
    ss = "abcdef" * 300000
    print(solution(ss+"bd"))
    print(solution(""))
    print(solution("a"))
    print(solution("aa"))
    print(solution(1))



7
-1
1
1799994
-1
-1
-1
-1








