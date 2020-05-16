# P.Conc., A2 Q1
# Farzad Rahman
# Truman98 - ICS
# February 27, 2020
# ICS3UI - 03, Ms. Harris
# Modifications:
# February 28: cleaned everything up, added further comments
# February 29: Added intro

# Problem: Create a program that finds the sum of all multiples of 3 and 5
#    between 0 and a user input

print("This program allows you to get the sum of all multiples of 3 and 5 between 0 and your parameter.") # Info on program

limit = int(input("Enter a max number parameter: "))     # Input for the max of the range


list = []      # list is created to store the multiples of 3 and 5


for i in range(1, limit + 1):         # selects multiples of 3 and 5 and stores them in list

    if (i%3 == 0 or i%5 == 0):    # checks if 'i' is a multiple of 3 or 5
        list.append(i)           # Adds i to the list



print(list)                    # displays the list of multiples of 3 and 5
print (sum(list))              # Prints the sum of the list






