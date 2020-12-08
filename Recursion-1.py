"""
Given n of 1 or more, return the factorial of n, 
which is n * (n-1) * (n-2) ... 1. Compute the result recursively (without loops).
"""
def factorial(n):
    if n == 1:
        return 1
    return n*factorial(n-1)
"""
We have a number of bunnies and each bunny has two big floppy ears.
We want to compute the total number of ears across all the bunnies recursively (without loops or multiplication).
"""
def bunnyEars(bunnies):
    if bunnies == 0 :
        return 0
    return 2+bunnyEars(bunnies-1)

"""
The fibonacci sequence is a famous bit of mathematics, and it happens to have a recursive definition.
The first two values in the sequence are 0 and 1 (essentially 2 base cases).
Each subsequent value is the sum of the previous two values, so the whole sequence is: 0, 1, 1, 2, 3, 5, 8, 13, 21 and so on.
Define a recursive fibonacci(n) method that returns the nth fibonacci number, with n=0 representing the start of the sequence.
"""
def fibonnaci(n):
    if n==0:
        return 0
    if n==1:
        return 1
    return fibonnaci(n-1)+fibonnaci(n-2)

"""
We have triangle made of blocks. The topmost row has 1 block, the next row down has 2 blocks, the next row has 3 blocks, and so on.
Compute recursively (no loops or multiplication) the total number of blocks in such a triangle with the given number of rows.
"""
def triangle(blocks):
    if blocks == 1:
        return 1
    return blocks+triangle(blocks-1)

"""
Given a non-negative int n, return the sum of its digits recursively (no loops).
Note that mod (%) by 10 yields the rightmost digit (126 % 10 is 6), while divide (/) by 10 removes the rightmost digit (126 / 10 is 12).
"""
def sumDigits(n):
    if n == 0:
        return 0
    return n%10+sumDigits(n//10)

"""
Given a non-negative int n, return the count of the occurrences of 7 as a digit, so for example 717 yields 2. (no loops).
Note that mod (%) by 10 yields the rightmost digit (126 % 10 is 6), while divide (/) by 10 removes the rightmost digit (126 / 10 is 12).
"""
def count7(n):
    total = 0
    if n == 0:
        return 0
    if n%10==7:
        total += 1
    return total+count7(n//10)

"""
Given a non-negative int n, compute recursively (no loops) the count of the occurrences of 8 as a digit, except that an 8 with another
8 immediately to its left counts double, so 8818 yields 4. Note that mod (%) by 10 yields the rightmost digit (126 % 10 is 6),
while divide (/) by 10 removes the rightmost digit (126 / 10 is 12).
"""
def count8(n):
    total = 0
    if n == 0:
        return 0
    if n%10==8:
        total += 1
    return total+count8(n//10)

"""
Given base and n that are both 1 or more, compute recursively (no loops)
the value of base to the n power, so powerN(3, 2) is 9 (3 squared).
"""
def powerN(num, times):
    if times == 1:
        return num
    return num * powerN(num, times - 1)

"""
Given a string, compute recursively (no loops) the
number of lowercase 'x' chars in the string.
"""
def countX(str, count = 0):
    if len(str)==0:
        return count
    if str[0] == 'x':
        count += 1
    return countX(str[1::],count)

"""
Given a string, compute recursively (no loops)
the number of times lowercase "hi" appears in the string.
"""
def countHi(str, count = 0):
    if len(str)==0:
        return count
    if str[0:2] == 'hi':
        count += 1
    return countHi(str[1::],count)

"""
Given a string, compute recursively (no loops) a new
string where all the lowercase 'x' chars have been changed to 'y' chars.
"""
def changeXY(string, myString = ''):
    if len(string) == 0:
        return myString
    if string[0] == 'x':
        myString += 'y'
    else:
        myString += string[0]
    return changeXY(string[1::], myString)

"""
Given a string, compute recursively (no loops) a new string
where all appearances of "pi" have been replaced by "3.14".
"""
def changePi(string, new_string = ''):
    if len(string) == 0:
        return new_string
    if string[0:2] == 'pi':
        new_string += '3.14'
        return changePi(string[2::], new_string)
    else:
        new_string += string[0]
    return changePi(string[1::], new_string)

'''
Given a string, compute recursively a new string where all the 'x' chars have been removed.
'''
def String_noX(my_string, new_string=''):
    if len(my_string) == 0:
        return new_string
    if my_string[0] != 'x':
        new_string +=my_string[0]
    return String_noX(my_string[1::], new_string)