"""
Given a string, return a string where for every char in the original, there are two chars.
"""
def double_char(str):
    return ''.join([x*2 for x in str])

"""
Return the number of times that the string "hi" appears anywhere in the given string.
"""
def count_hi(str):
    accumulator = 0
    for index in range(len(str)):
        if str[index:index+2] == 'hi':
            accumulator += 1
    return accumulator

"""
Return True if the string "cat" and "dog" appear the same number of times in the given string.
"""
def cat_dog(str):
    cats, dogs = 0, 0
    for index in range(len(str)):
        if str[index:index+3] == 'cat':
            cats += 1
        if str[index:index+3] == 'dog':
            dogs += 1
    return cats == dogs

"""
Return the number of times that the string "code" appears anywhere in the given string, except we'll accept any letter for the 'd', so "cope" and "cooe" count.
"""
def count_code(str):
    accumulator = 0
    code = ['co'+chr(x)+'e' for x in range(97,123)]
    for index in range(len(str)):
        if str[index:index+4] in code:
            accumulator += 1
    return accumulator

"""
Given two strings, return True if either of the strings
appears at the very end of the other string, ignoring upper/lower
case differences (in other words, the computation should not be
"case sensitive"). Note: s.lower() returns the lowercase version of a string.
"""
def end_other(a, b):
    if len(a)<len(b):
        if b[-len(a):].lower() == a.lower():
            return True
    else:
        if a[-len(b):].lower() == b.lower():
            return True
    return False

"""
Return True if the given string contains an appearance of "xyz"
where the xyz is not directly preceeded by a period (.). So "xxyz"
counts but "x.xyz" does not.
"""
def xyz_there(str):
    res = False
    for index in range(len(str)):
        if str[index:index+3] == 'xyz':
            if str[index-1] != '.':
                res = True
            else:
                res = False
    return res
        