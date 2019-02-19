"""
2. Write a function named largest() that takes a list parameter and returns the largest element in that list. You can assume the list contents are all positive numbers. For example:
largest([10, 4, 2, 231, 91, 54])  # returns 231
largest([1,2,3,4,0])  # returns 4
"""
def largest(enteredList):
    largestNum = 0
    for i in range(0, len(enteredList)):
        largestNum = enteredList[i] if enteredList[i] > largestNum else largestNum
    print(largestNum, ' this is the largest number in the list')

largest([10, 4, 2, 231, 91, 54])
largest([1,2,3,4,0])