import heapq
from collections import Counter

def top_k_frequent(nums, k):
    """
    Find the top k frequent elements in an array.

    Args:
        nums (list[int]): Input array
        k (int): Number of top frequent elements to find

    Returns:
        list[int]: The top k frequent elements
    """
    # Count the frequency of each element
    count = Counter(nums)

    # Use a heap to find the top k frequent elements
    return heapq.nlargest(k, count.keys(), key=count.get)

# Example usage:
nums = [1, 1, 1, 2, 2, 3]
k = 2
top_k = top_k_frequent(nums, k)
print(f"The top {k} frequent elements are: {top_k}")
