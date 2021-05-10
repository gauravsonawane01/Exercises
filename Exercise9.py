"""
Switch Case:
Case 1 = ""fruit""
Print ""Orange,Apple,Banana""
Case 2 = ""City""
Print ""Pune,Satara,Kolhapur""
Case 3 = ""Month""
Print ""Jan,Feb,March""
Case default
Print ""Incorrect choice""

"""

# Using Switch case in python
def Switch(choice):
    switcher = {
        0: "Orange,Apple,Banana",
        1: "Pune,Satara,Kolhapur",
        2: "Jan,Feb,March",
    }
    return switcher.get(choice, "Incorrect choice")

# Getting choice from user
choice = int(input("""Enter yout choice
0 for fruits
1 for city
2 for month \n"""))

#printing users choice
print (Switch(choice))