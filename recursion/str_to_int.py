from DataStructures.stack.Stack import Stack

stack = Stack()


def to_str(n, base):
    """
    Coverts number in any base to string
    :param n:
    :param base:
    :return:
    """

    conversion_string = "0123456789ABCDEF"

    while n > 0:
        if n < base:
            stack.push(conversion_string[n])
        else:
            stack.push(conversion_string[n % base])

        n = n // base

    res = ""
    while not stack.is_empty():
        res += str(stack.pop())

    return res


if __name__ == "__main__":
    print(to_str(1453, 16))
