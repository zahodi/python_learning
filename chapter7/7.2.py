#!/usr/bin/env python3

 #7.2 Write a program that prompts for a file name, then opens that file and 
 #reads through the file, looking for lines of the form:
###########
##X-DSPAM-Confidence:    0.8475
###########
#Count these lines and extract the floating point values from each of the lines 
#and compute the average of those values and produce an output as shown below. 
#Do not use the sum() function or a variable named sum in your solution.
#You can download the sample data at http://www.pythonlearn.com/code/mbox-short.txt 
#when you are testing below enter mbox-short.txt as the file name.


fname = raw_input("Enter file name: ")
fh = open(fname)
my_list = []
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : continue
    num = filter(str.isdigit, line)
    floating_num = float(num)
    print floating_num
    float_num = float(int(filter(str.isdigit, line)))
    my_list.append(float_num)
    
    #print(my_list)
    #print(line)
print(my_list)
print("Done")
