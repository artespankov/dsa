# Given an array,
# return true if there are two equal elements
# within the window of size K

# properties of sliding window
# it should be AT MOST of the length k
# two elements can't be on the same index position (i.e. i != j)

# ex a = [1 2 3 2 3 3], k = 2

def closeDuplicatesBruteForce(nums, k):
    """
    Category: Sliding Window - fixed size

    check if array has a pair of duplicate values,
    where 2 duplicates are no farther than k positions from each other
    i.e. arr[i]==arr[j] and abs(i - j) <= k

    Time complexity: O(n * k)
    for small window sizes k it might be ok
    but for larger - it's going to be O(n^2) complexity
    """

    for L in range(len(nums)):
        # common sliding window technique to not let slow pointer get out of bounds
        # choose what is lesser - the needed window size or the space left till the end of array
        for R in range(L+1, min(len(nums), L + k)):
            if nums[L] == nums[R]:
                return True
    return False


def closeDuplicates(nums, k):
    """
    Category: Sliding Window - fixed size

    Optimized version with hashset
    Instead of comparing each element to every other element in window
    we can use rolling hashset and check if current element is in hashset (i.e. arr[i] in hashset)
    """
    

if __name__ == "__main__":
    print(closeDuplicatesBruteForce([1, 2, 3, 2, 3, 2], k=2))



