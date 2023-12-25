from DS.stack.Stack import Stack


def to_base_two(decimal_num: int):
    s = Stack()
    ans = ""
    while decimal_num:

        s.push(decimal_num % 2)
        decimal_num //= 2

    while not s.is_empty():
        e = s.pop()
        print(e)
        ans += str(e)
    return ans


def to_base_n(decimal_num: int, base_n: int):
    conversions = "0123456789ABCDEF"

    s = Stack()
    ans = ""
    while decimal_num:

        s.push(decimal_num % base_n)
        decimal_num //= base_n

    while not s.is_empty():
        e = s.pop()
        print(conversions[e])
        ans += conversions[e]
    return ans

a = [1, 2 ,3 , 4, 5]


t = 7


if __name__ == "__main__":
    # print(to_base_two(12))
    print(to_base_two(111))
    print(to_base_n(111, 16))
    print(to_base_n(111, 8))
    print(to_base_n(25, 8))
    print(to_base_n(256, 16))
