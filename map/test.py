#!/usr/bin/env python3

dict = {  
"key1" : "value1",
"key2" : "value2",
"key3" : "value3",
"key4" : "value4",
"key5" : "value5",
"key6" : "value1",
"key7" : "value2",
"key8" : "value3",
"key9" : "value4",
"key10" : "value5"
}
revdict = {}
for key in dict:
    value = dict[key]
    if not value in revdict:
        revdict[value] = []
    revdict[value].append(key)

print(revdict)
