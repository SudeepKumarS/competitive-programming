# Sliding window problem:
# you have an array of integers: [4, 1, 2, 6, 8, 5] and a window size of 3. 
# The task is to find the maximum sum of any 3 consecutive elements within the array.


def find_max_sum(arr: list, window_size: int) -> int:
    """
    To find the maximum consecutive sum of window_size elements
    in the given array
    """
    # Edge Case
    if not arr:
        return 0
    start = 0  # Starting index
    end = window_size - 1  # As we are using indexing
    max_sum = sum(arr[start:end + 1])

    while end < len(arr) - 1:
        start += 1
        end += 1
        max_sum = max(sum(arr[start:end+1]), max_sum)
    
    return max_sum
    
l = []
win = 6
maxum = find_max_sum(l, win)
print(maxum)
