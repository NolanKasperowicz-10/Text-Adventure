import re
#takes the word you inputted
my_string = input()
#prints a the number of times a given char occurs in the word
print(len(re.findall(input(), my_string)))