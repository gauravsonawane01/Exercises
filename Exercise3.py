"""
Input : ""aaaassgbttijjsssnhsssggg""

1. Replace All  ""s"" with ""n""
2. Replace third character with ""h""

"""
# declaring a string variable
str = "aaaassgbttijjsssnhsssggg"

# declaring an empty string variable for storing modified string
str_new = ''

# iterating over the string
for char in range(0, len(str)):
    # checking if the character at char index is equivalent to 'a'
    if (str[char] == 's'):
        # append $ to modified string
        str_new += 'n'
    else:
        # append original string character
        str_new += str[char]

print("Original String : ")
print(str)
print("Modified string 1 : ")
print(str_new)

# index pointing to 3 rd position
i = 2
replace = 'h'
#replacing char at position 3
str_new = str_new[:i] + replace + str_new[i+1:]

print("Modified string 2 : ")
print(str_new)