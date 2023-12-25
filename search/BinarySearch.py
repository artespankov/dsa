import math

def bin_search(l: list, item: int):
    # works only on sorted DS
    # consideration, as algo works only on sorted collections, it's npot worth sorting overhead + binsearch
    # for collections with small number of items

    if not l:
        return False

    if len(l) == 1:
        return True
    left = 0
    right = len(l) - 1
    while left <= right:

        mid = (right + left) // 2
        print(left, right, mid, item)
        if l[mid] == item:
            return True
        if item > l[mid]:
            left = mid + 1
        else:
            right = mid - 1
    return False


def bin_search_recursive(l: list, item: int):
    if not l:
        return False

    mid = (len(l) - 1) // 2

    if l[mid] == item:
        return True

    if item > l[mid]:
        # slicing makes it not O(logN) algorithm. to remedy this - pass also start, end indexes into recursive call
        return bin_search_recursive(l[mid+1:], item)
    else:
        return bin_search_recursive(l[:mid-1], item)


if __name__ == "__main__":
    l1 = [50, 99, 110, 125, 315, 345, 360, 799, 2500]

    l2 = [1,2,3,4,5,6,7,8]

    print(bin_search(l1, 799))
    print(bin_search(l2, 10))

    print(bin_search_recursive(l1, 799))
    print(bin_search_recursive(l2, 10))







