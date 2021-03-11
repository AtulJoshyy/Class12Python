
def main():

    print('''
    1.AREA
    2.PERIMETER''')
    
    c = int(input("Enter your choice"))
    if c == 1:
        area()
    elif c == 2:
        perimeter()

def area():
    r=int(input("enter radius of circle"))
    A=3.14*r*r 
    print(f"the area of the circle is {A}")
def perimeter():
    r=int(input("enter radius of circle"))
    P=2*3.14*r
    print (f"tthe perimeter is {P}")



main()
