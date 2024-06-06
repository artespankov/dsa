
def sum_recursive(arr):
    if not arr:
        return 0
    return arr[0] + sum_recursive(arr[1:])


def count_recursive(arr):
    if not arr:
        return 0
    return 1 + count_recursive(arr[1:])


def find_max(arr):
    if len(arr) == 0:
        return 0
    if len(arr) == 1:
        return arr[0]
    if arr[0] > arr[-1]:
        return find_max(arr[:-1])
    return find_max(arr[1:])


if __name__ == "__main__":
    s = sum_recursive([12, 14, 22, 10])
    print(s)

    c = count_recursive([12, 14, 22, 10, 11, 1, 0, 2, 15, 10, 12, 17, 32, 11, 1, 321])
    print(c)

    m = find_max([12, 14, 1111122, 1110, 11, 1, 0, 2, 15, 1110, 111112, 17, 32, 11, 1, 321])
    print(m)
