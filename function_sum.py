"""
1.  Write a function named sum_to() that takes a number parameter n and returns the sum of the numbers from 1 to n. For example:
sum_to(6)  # returns 21
sum_to(10) # returns 55
"""

def sum_to(n):
    newSum = 0
    for i in range (1, n + 1):
        newSum += i
    print(newSum, ' this is the final sum.')

sum_to(10)