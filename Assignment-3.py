#Python Programming Assignment 3
#Checking if a triangle is right angled or not

a=int(input("Enter length of base of triangle: "))
b=int(input("Enter length of height of triangle: "))
c=int(input("Enter length of hypotenuse of triangle: "))

def rightangletriangle(a,b,c):
    if c**2==(a**2+b**2):
        print("It is a right angled triangle")
    else:
        print("It is not a right angled triangle")

rightangletriangle(a,b,c)
