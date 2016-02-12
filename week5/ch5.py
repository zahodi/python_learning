#!/usr/bin/env python

count = 0 
for itervar in [3, 54, 5123, 23, 4123, 33]:
    count = count +1
print 'Count: ', count
total = 0 
for itervar in [3, 54, 5123, 23, 4123, 33]:
    total = total + itervar
print 'Total: ', total 
largest = None
print 'before:', largest
for itervar in [3, 54, 5123, 23, 4123, 33]:
    if largest is None or itervar < largest :
        largest = itervar
    print 'Loop:', itervar, largest
print 'Largest:', largest