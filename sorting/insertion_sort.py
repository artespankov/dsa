
def insertion_sort1(nums: list):
    """
    O(1/2*n^2) ~ O(n^2)
    """
    for i in range(1, len(nums)):
        j = i - 1
        while j >= 0 and nums[j+1] < nums[j]:
            # swap current and next
            nums[j], nums[j+1] = nums[j+1], nums[j]
            j -= 1
    return nums


def insertion_sort(l: list):
    for i in range(1, len(l)):
        pos = i
        value = l[pos]
        while pos and l[pos-1] > value:
            l[pos] = l[pos-1]
            pos -= 1

        l[pos] = value

if __name__ == "__main__":

    alist = [54,26,93,17,77,31,44,55,20]
    insertion_sort(alist)
    print(alist)

    alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    insertion_sort1(alist)
    print(alist)