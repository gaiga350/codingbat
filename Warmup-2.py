"""
Given a string and a non-negative int n, return a larger string that is n copies of the original string.
"""
def string_times(str, n):
    return str*n

"""
Given a string and a non-negative int n, we'll say that the front of the string is the first 3 chars,
or whatever is there if the string is less than length 3. Return n copies of the front
"""
def front_times(str, n):
    return str[0:3]*n

"""
Given a string, return a new string made of every other char starting with the first, so "Hello" yields "Hlo".
"""
def string_bits(str):
    return str[0::2]

"""
Given a non-empty string like "Code" return a string like "CCoCodCode".
"""
def string_splosion(str):
    string = ''
    for i in range(len(str)+1):
        string+=str[0:i]
    return string

"""
Given an array of ints, return the number of 9's in the array.
"""
def array_count9(nums):
    return nums.count(9)

"""
Given an array of ints, return True if one of the first 4 elements
in the array is a 9. The array length may be less than 4.
"""
def array_front9(nums):
    return 9 in nums[0:4]

"""
Given an array of ints, return True if the sequence of numbers 1, 2, 3 appears in the array somewhere.
"""
def array123(nums):
    for i in range(len(nums)-2):
        if nums[i] == 1 and nums[i+1] == 2 and nums[i+2] == 3:
            return True
    return False
    
"""
Given 2 strings, a and b, return the number of the positions where they
contain the same length 2 substring. So "xxcaazz" and "xxbaaz" yields 3,
since the "xx", "aa", and "az" substrings appear in the same place in both strings.
"""
def string_match(a, b):
    result = 0
    for index in range(len(a)-1):
        if a[index:index+2] ==b[index:index+2]:
            result+=1
    return result