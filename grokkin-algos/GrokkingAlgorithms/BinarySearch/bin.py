def binary_search(item, my_list: list):
    low, i = 0, 0
    high = len(my_list) - 1
    while low <= high:
        i += 1
        mid = (low + high) // 2  # floor division
        guess = my_list[mid]
        if guess == item:
            print(f"Iterations: {i}")
            return mid
        if guess < item:
            low = mid + 1  # watch out this, you've checked the mid element already
        else:
            high = mid - 1
    print(f"Iterations: {i}")
    return None

some_list = [1, 3, 5, 7, 9]
print(binary_search(7, some_list))
print(binary_search(11, some_list))

