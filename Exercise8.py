"""
list 1 = [1,12,3,4,45,6,7,8,9]
list 2 = [76,5,3,5,67,8,9,11,12]
Find out common element from both the list

"""

list1 = [1,12,3,4,45,6,7,8,9]
list2 = [76,5,3,5,67,8,9,11,12]

result = []
# Appending the common element in list result
for element in list1:
    if element in list2:
        result.append(element)

print(result)
