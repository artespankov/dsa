# BallsInBuckets:  Move balls in order to create an alternating sequence of empty and full buckets.

"""
There are N buckets arranged in a row. Each bucket either is empty or contains a ball. The buckets are specified as a string buckets consisting of
characters "." (empty bucket) and "B" (bucket with a ball). For example, for buckets = "B.BB.B..B" the row of buckets appears as follows:
[*.**.*..*]
In one move you can take the ball out of any bucket and place it in another (empty) bucket. Your goal is to arrange the balls to create an alternating
sequence of full and empty buckets. In other words, the distance between two consecutive balls should be equal to 2. Note that the sequence may
start at any bucket.
For example, in the figure below, the balls are placed CORRECTLY:
[...*.*.*...]
On the other hand, in both of the figures below, the balls are placed INCORRECTLY:
[..*..*.*...]
[..*..*..*..]
What is the minimum number of moves required to create a correct sequence of balls in buckets?
"""
import math

def solution(s:str):
    balls_count = 0
    evens, odds = 0, 0

    for i, ch in enumerate(s):
        if ch == "B":
            balls_count += 1
            if i % 2 == 0:
                evens += 1
            else:
                odds += 1

    if balls_count <= math.ceil(len(s)/2):
        # 0 1 2 3 4 5  l = 6 even_inx = 3 odd_inx = 3
        # 0 1 2 3 4  l = 5 even_inx = 3 odd_inx = 2
        even_buckets = math.ceil(len(s)/2)
        odd_buckets = len(s) - even_buckets

        # print(balls_count, even_buckets, evens, odd_buckets, odds)

        even_places_ops = math.inf
        if evens and balls_count <= even_buckets:
            even_places_ops = odds

        odd_places_ops = math.inf
        if odds and balls_count <= odd_buckets:
            odd_places_ops = evens

        return min(even_places_ops, odd_places_ops)
    return -1


if __name__ == "__main__":
    print(solution("..B....B.BB"))
    print(solution("BB.B.BBB..."))
    print(solution(".BBB.B"))
    print(solution("......B.B"))
    # print("..BB..B.B")
    print(solution("..BB..B.B"))
