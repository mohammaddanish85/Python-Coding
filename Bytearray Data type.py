# This Program demonstrate the bytearray data type and retrieve elements from array.
# Bytetype array is similar to bytes data type. Major difference is that byte data type array cannot be modified and bytearray data type can be modified.


elements= [15, 2, 8, 89, 5]                        # create a list of byte numbers.

var=bytearray(elements)                            # convert the list into bytearray type array

var[1]= 79                                         # modification in first element of var.
var[3]= 27                                         # modification in third element of var.

for i in var: print(i)                             # Display the elements of array using For loop.
















