import math
def Delta():
    d = b*b-4*a*c
    if d >= 0:
       Equation() 
    else:
        print("The equation has no real root")
def Equation():
    x1 = (-b-math.sqrt(b*b-4*a*c))/2*a
    x2 = (-b+math.sqrt(b*b-4*a*c))/2*a 
    print("x1 =", x1 , "x2 =", x2)

while True:
    f = input("If you want to solve your desired quadratic equation(a(x*x)+b(x)+c=0) enter s if not enter q =")

    if f == "q":
        print("End")
        break

    if f =="s":
        a = float(input("Enter a (Note: a can not be zero) = "))
        b = float(input("Enter b =")) 
        c = float(input("Enter c =")) 

        Delta()
    
                


