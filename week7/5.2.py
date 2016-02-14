#!/usr/bin/env python3 

# 5.2 Write a program that repeatedly prompts a user for integer numbers until the user
#enters 'done'. Once 'done' is entered, print out the largest and smallest of the numbers. 
# If the user enters anything other than a valid number catch it with a try/except and put
#out an appropriate message and ignore the number. Enter the numbers from the book for
#problem 5.1 and Match the desired output as shown. 

def large_smallest():
    largest = None
    smallest = None
    array_of_num = []
    while True:
        response = raw_input("Enter a number:")
        if response == "done" : break
        try:
            num = int(response)
            array_of_num.append(num) 
            largest = max(array_of_num)
            smallest = min(array_of_num)
        except:
            print "Invalid Input"
            pass
    print "Maximum is", largest
    print "Smallest is", smallest

large_smallest()