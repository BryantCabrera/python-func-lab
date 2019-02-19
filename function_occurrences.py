"""
3. Write a function named occurances() that takes two string parameters and counts the number of occurrances of the second string inside the first string. For example:
occurances('fleep floop', 'e')   # returns 2
occurances('fleep floop', 'p')   # returns 2
occurances('fleep floop', 'ee')  # returns 1
occurances('fleep floop', 'fe')  # returns 0
"""

def occurrences(str1, str2):
    count = 0
    if len(str2) < len(str1):
        for i in range(0, len(str1)):
            if str1[i] == str2[0]:
                n = i
                for j in range(0, len(str2)):
                    if str1[n] == str2[j]:
                        n +=1
                        if j == len(str2) - 1:
                            count += 1
                    else:
                        break
    print(count)

# def occurrences(str1, str2):
#     count = 0
#     if len(str2) < len(str1):
#         for i in range(0, len(str2)):
#             if str2[i] == str1[0]:
#                 for j in range(1, len(str1)):
#                     if str1[i + 1] == str2[j]:
#                         i += 1
#                 count += 1


occurrences('fleep floop', 'e')   # returns 2
occurrences('fleep floop', 'p')   # returns 2
occurrences('fleep floop', 'ee')  # returns 1
occurrences('fleep floop', 'fe')  # returns 0