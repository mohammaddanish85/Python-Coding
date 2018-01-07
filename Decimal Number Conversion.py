# This program demonstrates the conversion of data types explicitly.
# We have shown the conversion of Octal, Binary and Hexadecimal number to decimal number.


n1=0o17                              # n1 variable is assigned a OCTAL number value.
n2=0B1110010                         # n2 variable is assigned a BINARY number value.
n3=0X1c2                             # n3 variable is assigned a HEXADECIMAL number value.

n= int(n1)                           # Here value of n1 (Octal value) is converting to integer data type.
print('Octal 17=',n)                 # Octal 17 is converted to 15.

n= int(n2)                           # Here value of n2 (Binary value) is converting to integer data type.
print('Binary 1110010=',n)           # Binary 1110010 is converted to 114.

n= int(n3)                           # Here value of n3 (Hexadecimal value) is converting to integer data type.
print('Hexadecimal 1c2=',n)          # Hexadecimal 1c2 is converted to 450.


