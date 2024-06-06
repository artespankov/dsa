def bin_search(numbers, item):
    low = 0
    high = len(numbers) - 1        # mistake 1

    while low <= high:             # mistake 2
        mid = (low + high) // 2    # mistake 3
        guess = numbers[mid]
        if guess == item:
            return mid
        elif item > guess:
            low = mid + 1          # mistake 4
        else:
            high = mid - 1         # mistake 5


some_list = [1, 3, 5, 7, 9]
print(bin_search(some_list, 1))
print(bin_search(some_list, 3))
print(bin_search(some_list, 5))
print(bin_search(some_list, 7))
print(bin_search(some_list, 9))
print(bin_search(some_list, 17))
