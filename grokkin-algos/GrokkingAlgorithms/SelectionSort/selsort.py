def find_smallest(arr):
    smallest = arr[0]
    smallest_index = 0
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index


def selection_sort(arr):
    sorted_arr = []
    while len(arr):
        index = find_smallest(arr)
        next_element = arr.pop(index)
        sorted_arr.append(next_element)
    return sorted_arr


l = [1, 4, 5, 6, 7, 0, 22, 0.5, -1, -12, 19, 17, 32, 2, 4, 5, 1]
print(selection_sort(l))
