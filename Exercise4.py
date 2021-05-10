"""
List is [1234512243153864319]
Remove duplicates from above list.

"""

list = [1,2,3,4,5,1,2,2,4,3,1,5,3,8,6,4,3,1,9]
print("The original list is : ")
print(list)

result = []

#appending only if the element occured fir the first time
for x in list :
    if x not in result :
        result.append(x)

# printing list after removal of duplicates
print("The list after removing duplicates : " )
print(result)