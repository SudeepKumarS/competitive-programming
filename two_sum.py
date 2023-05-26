# Given an array of integer nums and an integer target, return
# indices of the two numbers such that they add up to the target.

# You may assume that each input would have exactly one solution,
# and you may not use the same element twice.


from time_finder import calculate_execution_time


@calculate_execution_time
def two_array_sum(arr: list, target: int) -> list:
    """
    Method returns a list of indexes or an empty list
    """
    for i in range(0, len(arr)):
        for j in range(0, len(arr)):
            if i == j:
                continue
            if arr[i] + arr[j] == target:
                return [i, j]
    
    return []

@calculate_execution_time
def opt_two_sum(arr: list, target: int) -> list:
    """
    Optimised way of doing the above problem
    """
    num_dict = {}
    for i, num in enumerate(arr):
        sub_num = target - num
        if sub_num in num_dict:
            return [i, num_dict[sub_num]]
        num_dict[num] = i

    return []


print(two_array_sum([7,1,5,3,6,4], 9))  # O(n ^ 2)
print(opt_two_sum([7,1,5,3,6,4], 9))  # O(n)