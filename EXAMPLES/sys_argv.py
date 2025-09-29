import sys

print(f"{sys.argv = }")

print(f"{sys.argv[0] = }")

if len(sys.argv) > 1:
    print(f"{sys.argv[1] = }")  # First command line argument
else:
    print("no command line args")

DEBUG = True
color = "red" if DEBUG else "blue"

#   A ? B : C      C and friends
#   B if A else C  Python

#  == != > < >= <= 



#  and 
#  or 
#  not

# A and B 

# A or B

x = 30
b = 10
if (x > 5) and (b == 10):
    print("wahoooo")

