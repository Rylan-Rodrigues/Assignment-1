#Python Programming Assignment 2
#Finding largest of 3 Numbers

a=int(input("Enter 1st Number: "))
b=int(input("Enter 2nd Number: "))
c=int(input("Enter 3rd Number: "))

if a>=b and a>=c:
    print("1st Number is the largest")
elif b>=a and b>=c:
    print("2nd Number is the largest")
else:
    print("3rd Number is the largest")
