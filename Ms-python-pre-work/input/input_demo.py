print("What is your name?")
name = input()

print("How old are you?")
age = int(input())

print(name)
print(age)


import sys

name = sys.argv[1]

print("How old are you?")
age = int(input())

print(name)
print(age)

height = 74 # The unit is inches
if height > 70 :
    print("You are really tall")


height = 54 # inches
if height > 70 :
    print("You are really tall")
else:
    print("You are really short")

height = 68 # inches
if height > 70 :
    print("You are really tall")
elif height > 60:
    print("You are of average height")

else:
    print("You are really short")

my_list = []
my_other_list =list()

list_a = ["a","b","c","d"] # list of strings
list_b = [1,2,3,4,5,6] # list of numbers
list_c = [1,"west",34,"longitude"] # mixed list
list_d = [ ["a","b","c","d"],[1,2,3,4,5,6],[1,"west",34,"longitude"]] # nested list
