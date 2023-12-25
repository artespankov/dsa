

def selection_sort(l: list):
    for slot in range(len(l)-1, 0, -1):
        max_pos = 0
        for current_pos in range(1, slot + 1):
            if l[current_pos] > l[max_pos]:
                max_pos = current_pos
        l[slot], l[max_pos] = l[max_pos], l[slot]


if __name__ == "__main__":
    l = [54,26,93,17,77,31,44,55,20]
    selection_sort(l)
    print(l)
