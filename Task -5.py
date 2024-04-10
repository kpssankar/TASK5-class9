#program to display expected output of given python code
data = [10,501,22,37,100,999,87,351]
result = filter(lambda x: x > 4, data)
print(list(result))

Output:
[10, 501, 22, 37, 100, 999, 87, 351]
================================================================================================================================================
#program using lamda function to check element of list is string or integer

list = [11,22,33,"one", "two",77,"three"]

result = filter(lambda x: isinstance(x, str) or isinstance(x, int),list)

print(result)
==================================================================================================================================================

#program to create fiboncci series from 1 to 50

num = 50
n1, n2 = 0, 1
print("Fibonacci Series:", n1, n2, end=" ")
for i in range(2, num):
    n3 = n1 + n2
    n1 = n2
    n2 = n3
    print(n3, end=" ")

print()

Fibonacci Series: 0 1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987 1597 2584 4181 6765 10946 17711 28657 46368 75025 121393 196418 317811 514229 832040 1346269 2178309 3524578 5702887 9227465 14930352 24157817 39088169 63245986 102334155 165580141 267914296 433494437 701408733 1134903170 1836311903 2971215073 4807526976 7778742049 
==============================================================================================================================================

#python function to validate reqular expression for following
#a. Email address
import re

def validate_email(email):
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    if re.match(pattern, email):
        return True
    else:
        return False

# Example usage
email_address = "example@email.com"
if validate_email(email_address):
    print("Email is valid.")
else:
    print("Email is invalid.")
================================================================================================================================================
#python function to validate reqular expression for following
#Mobile numbers of Bangladesh (+8809102134 )

import re

def validate_MobileNumbers(MobileNumbers):
    pattern = re.compile(r"(\+\d{1,3})\d{1,7}")
    if re.match(pattern, MobileNumbers):
        return True
    else:
        return False

# Example usage
MobileNumbers = "+8809102134"
if validate_MobileNumbers(MobileNumbers):
    print("MobileNumbers is valid.")
else:
    print("MobileNumbers is invalid.")


Output:
=========
MobileNumbers is valid.
===========================================================================================================================================
#python function to validate reqular expression for following
#Telephone numbers of USA (+8809102134 )


import re

def validate_Telephonenumbers(Telephonenumbers):
    pattern = re.compile(r"(\+\-\d{1}\-\d{1,3}\-\d{1,3}\-\{1,4})")
    if re.match(pattern, Telephonenumbers):
        return True
    else:
        return False

# Example usage
Telephonenumbers = "+1-212-456-7890"
if validate_Telephonenumbers(Telephonenumbers):
    print("Telephonenumbers is valid.")
else:
    print("Telephonenumbers is invalid.")

Output:
=========

Telephonenumbers is invalid.
=================================================================================================================================================

#python function to validate reqular expression for following
#Password ("SathurPujam#1234")


import re

def validate_Password(Password):
    pattern = re.compile('^(?=\S{6,16}$)(?=.*?\d)(?=.*?[a-z])(?=.*?[A-Z])(?=.*?[^A-Za-z\s0-9])')
    if re.match(pattern, Password):
        return True
    else:
        return False

# Example usage
Password = "SathurPujam#123456"
if validate_Password(Password):
    print("Password is valid.")
else:
    print("Password is invalid.")

Output:
========

Password is invalid.
===================================================================================================================================================