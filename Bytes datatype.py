# This Program create a byte type array and display the item elements.
# Elements in byte type array cannot be modified.

elements_list =[12, 15, 9, 61, 95]           # Create/Initialise the list of elements.

numbers = bytes(elements_list)               # Convert the list into byte type array.

for i in numbers: print(i)                   # Display the elements of array.
