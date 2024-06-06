import math
def solution(A):
    # Implement your solution here
    res = 1
    if len(A) == 1:
        res = A[0]
    elif len(A) > 1:
        A.sort()
        found_in_middle = False
        if A[0] > 0 and A[-1] > 0:
            for i in range(len(A)-1):
                if A[i+1] - A[i] != 1:
                    res = A[i] + 1
                    found_in_middle = True
            if not found_in_middle:
                res = A[-1] + 1
    return res if res > 0 else 1



if __name__ == "__main__":
    a = [1, 2, 3] # 4
    b = [-1, -3] # 1
    c = [1, 3, 6, 4, 1, 2] #5
    d = []
    e = [2]
    f = [-2, 0]

    print(solution(a))
    print(solution(b))
    print(solution(c))
    print(solution(d))
    print(solution(e))
    print(solution(f))

