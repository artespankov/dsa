


def longestSubarray(nums):
    """
    Category: Sliding Window - dynamic size

    Q: Find the length of the longest subarray, with the same value in each position
    (We're looking for the longest sequence of duplicates here)
    Time complexity: O(n)

    arr = [4, 2, 2, 4, 4, 4]
    output: 3 (sequence of 4-s at the end)
    """
    longest = 0
    L = 0
    for R in range(len(nums)):
        if nums[L] != nums[R]:
            L = R
        longest = max(longest, (R - L) + 1)
    return longest



def minSubarray(nums, target):
    """
    Q: Find the minimum length subarray
    where sum is greater than or equal to the target.
    Assume all values are positive


    arr = [11, 0, 1, 2, 4, 2, 3, 4, 4]
    target = 5

    1 + 4 = 5 sub arr of 3 elements (2 in between)
    2 + 3 = 5 sub arr of 2 elements
    """




if __name__ == "__main__":
    ans = longestSubarray([4, 2, 2, 4, 4, 4, 0, 4])
    print(ans)
