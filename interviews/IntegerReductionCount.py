"""IntegerReductionCount
Given a number N and two reduction operations, count the number of operations required to reduce
N to 0.

You are given a string S of length N which encodes a non-negative number V in a binary form. Two types of operations may be performed on it to
modify its value:
if V is odd, subtract 1 from it;
if V is even, divide it by 2.
These operations are performed until the value of V becomes 0.
For example, if string S = "011100", its value V initially is 28. The value of V would change as follows:
V = 28, which is even: divide by 2 to obtain 14;
V = 14, which is even: divide by 2 to obtain 7;
V = 7, which is odd: subtract 1 to obtain 6;
V = 6, which is even: divide by 2 to obtain 3;
V = 3, which is odd: subtract 1 to obtain 2;
V = 2, which is even: divide by 2 to obtain 1;
V = 1, which is odd: subtract 1 to obtain 0.
Seven operations were required to reduce the value of V to 0.

that, given a string S consisting of N characters containing a binary representation of the initial value V, returns the number of operations after
which its value will become 0.
Examples:
1. Given S = "011100", the function should return 7. String S represents the number 28, which becomes 0 after seven operations, as explained
above.
2. Given S = "111", the function should return 5. String S encodes the number V = 7. Its value will change over the following ve operations:
V = 7, which is odd: subtract 1 to obtain 6;
V = 6, which is even: divide by 2 to obtain 3;
V = 3, which is odd: subtract 1 to obtain 2;
V = 2, which is even: divide by 2 to obtain 1;
V = 1, which is odd: subtract 1 to obtain 0.
3. Given S = "1111010101111", the function should return 22.
4. Given string S consisting of "1" repeated 400,000 times, the function should return 799,999.
Write an efficient algorithm for the following assumptions:
string S consists only of the characters "0" and/or "1";
N, which is the length of string S, is an integer within the range [1..1,000,000];
the binary representation is big-endian, i.e. the rst character of string S corresponds to the most significant bit
"""
# the binary representation may contain leading zeros.


def solution(s):
    # num = int(s, 2)
    count = 0
    while num:
        # means it's odd (wecheck if the rightmost bit is 1 by and-ing with ..00001)
        if num & 1:
            num -= 1
        else:
            # getting rid of the rightmost bit, which is equivalent of dividing by 2
            num = num >> 1
        count += 1
    return count


if __name__ == "__main__":
    print(solution("011100")) # 28 # 7
    print(solution("111")) # 7 # 5
    print(solution("1111010101111")) #7855 # 22
    print(solution("1" * 400000)) # 799999
    print(solution("1" * 1000000))
