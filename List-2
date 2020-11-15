"""
Return the number of even ints in the given array.
Note: the % "mod" operator computes the remainder, e.g. 5 % 2 is 1.
"""
def count_evens(nums):
    return len([x for x in nums if x%2==0])

"""
Given an array length 1 or more of ints, return the difference
between the largest and smallest values in the array. Note: the
built-in min(v1, v2) and max(v1, v2) functions return the smaller
or larger of two values.
"""
def big_diff(nums):
    return max(nums)-min(nums)

"""
Return the sum of the numbers in the array, returning 0 for
an empty array. Except the number 13 is very unlucky, so it
does not count and numbers that come immediately after a 13
also do not count.
"""
def sum13(nums):
    my_list = []
    index = 0
    while index != len(nums):
        if index > len(nums):
            break
        if nums[index]!=13:
            my_list.append(nums[index])
        else:
            index +=1
        index +=1
    return sum(my_list)

"""
Return the sum of the numbers in the array, except ignore
sections of numbers starting with a 6 and extending to the
next 7 (every 6 will be followed by at least one 7).
Return 0 for no numbers.
"""
def sum67(nums):
    index = 0
    new_nums = []
    while index != len(nums):
        if nums[index] == 6:
            while nums[index]!=7:
                index += 1
        else:
            new_nums.append(nums[index])
        index += 1
    return sum(new_nums)

"""
Given an array of ints, return True if the array contains
a 2 next to a 2 somewhere.
"""
def has22(nums):
    for index in range(len(nums)-1):
        if nums[index] == 2 and nums[index+1]==2:
            return True
    return False