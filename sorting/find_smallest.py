import time
from random import randrange





def find_smallest(l):
    smallest = l[0]
    for i, n1 in enumerate(l):
        smallest_in_pair = n1
        for j, n2 in enumerate(l):
            if i != j:
                if n2 < n1:
                    smallest_in_pair = n2
        if smallest_in_pair < smallest:
            smallest = smallest_in_pair
    return smallest



def find_smallest_linear(l):
    minimum = l[0]
    for n in l[1:]:
        if n < minimum:
            minimum = n
    return minimum





if __name__ == "__main__":
    l = [1, 8, 22, 3, 1, 5, 8]

    # for list_size in range(1000, 10001, 1000):
    #     alist = [randrange(10000) for x in range(list_size)]
    #     start = time.time()
    #     print(find_smallest(alist))
    #     end = time.time()
    #     print(f"Size: {list_size}. Time: {end - start}")

    for list_size in range(1000, 10001, 1000):
        start = time.time()
        print(find_smallest_linear(l))
        end = time.time()
        print(f"Size: {list_size}. Time: {end - start}")
