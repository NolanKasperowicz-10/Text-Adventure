import re
#takes the word you inputted
lettercount = input()
#prints a the number of times a given char occurs in the word
print(len(re.findall(input(), lettercount)))

#it can also take any number of letters and numbers in an order and find them
#for instance, I can ask it how many times "12a" occurs in a string

def letterCount():
  lettercount = input():
  print(len(re.findall(input(), letterCount)))
