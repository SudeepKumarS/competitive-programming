# Given an integer array nums, return true if any value appears at
# least twice in the array, and return false if every element is
# distinct.


from time_finder import calculate_execution_time


@calculate_execution_time
def contains_duplicates(nums: list) -> bool:
    """
    To check if an array contains duplicates or not
    """
    num_set = set()
    
    for num in nums:
        if num in num_set:
            return True
        num_set.add(num)

    return False


print(contains_duplicates([1,2,3,1]))