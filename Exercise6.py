"""
Remove the whitespaces from the string “aaa bbb ccc ddd eee”

"""
# declaring a string variable
str = "aaa bbb ccc ddd eee"

# declaring an empty string variable for storing modified string
str_new = ''

#logic to remove blank spaces
for i in range(0,len(str)) :
    if str[i] == ' ' :
        continue
    else :
        str_new += str[i]

print(str_new)