def bubble_sort(l: list):
    for pass_num in range(len(l) - 1, 0, -1):
        for j in range(pass_num):
            if l[j] > l[j + 1]:
                l[j], l[j + 1] = l[j + 1], l[j]
    return l


def short_bubble_sort(l: list):
    exchanges = True
    pass_num = len(l) - 1

    while pass_num and exchanges:
        exchanges = False
        for j in range(pass_num):
            if l[j] > l[j+1]:
                exchanges = True
                l[j], l[j+1] = l[j+1], l[j]
        pass_num -= 1


if __name__ == "__main__":
    ll = [1, 17, 22, 5, 6, 7, 22, 788, 11, 678, 0, 15, 43, 68, 90, 32]
    print(bubble_sort(ll))
    print(bubble_sort([54, 26, 93, 17, 77, 31, 44, 55, 20]))
