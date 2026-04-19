#exercise 3.1
age = 28
#exercise 3.2
height = 5.1
#exercise 3.3
comNum = 1 + 1j
#exercise 3.4
b = input("Enter Base: ")
h = input("Enter Height: ")
area = 0.5 * int(b) * int(h)
print("The area of the triangle is: ", int(area))
#exercise 3.5
a = input("Enter side a: ")
b = input("Enter side b: ")
c = input("Enter side c: ")
perimeter = int(a) + int(b) + int(c)
print("The perimeter of the triangle is: ", int(perimeter))
#exercise 3.6
length = input("Enter length of a rectangle: ")
width = input("Enter width of a rectangle: ")
area = float(length) * float(width) 
perimeter = (2 * (float(length) + float(width)))
print("The area of a rectangle is : ", float(area))
print("The perimter of a rectangle is : ", float(perimeter))
#exercise 3.7
radius = input("Enter radius: ")
area = 3.14 * int(radius) * int(radius)
c = 2 * 3.14 * int(radius)
print("The area of a circle is ", float(area))
print("The circumference of a circle is ", float(c))
#exercise 3.8
x = input("Enter x for slope: ")
y = 2* int(x) - 2 
print("slope: ", int(y))
#exercise 3.9
x1 = float(input("x1: "))
y1 = float(input("y1: "))
x2 = float(input("x2: "))
y2 = float(input("y2: "))
m = ((y2 - y1) / (x2 - x1))
print("slope 2: ", float(m))
#exercise 3.10
print("Comparison: ", float(y) == float(m))
#exercise 3.11
x11 = int(input("Enter x value: "))
y11 = (x11^2 + 6*x11 + 9)
print("comparison11: ", y11 == 0)
#exercise 3.12
print("python_dragon comparison: ", len("python") > len("dragon"))
#exercise 3.13
print("on is in python and dragon: ", 'on' in  ("python" and "dragon"))
#exercise 3.14
print("jargon is in I hope this course is not full of jargon:", 'jargon' in "I hope this course is not full of jargon")
#exercise 3.15
print("no on in python and dragon: ", 'on' not in  ("python" and "dragon"))
#exercise 3.16
pyLen = float(len("python"))
print("string convert: ", str(pyLen))
#exercise 3.17
NumVal = int(input("enter number: "))
numtotal = NumVal % 2
print("even?: ", int(numtotal) == 0)
#exercise 3.18
floor_division = 7 // 3
print("fd: ", int(floor_division))
print("comparison_fd: ", int(floor_division) == int(2.7))
#exercise 3.19
print("comparison_10:", type("10") == type(10))
#exercise 3.20
print("3.20: ", int(9.8) == int(10))
#exercise 3.21
hours = float(input("Enter hours: "))
rate = float(input("Enter rate per hour: "))
earnings = hours * rate
print("Your weekly earning is : ", float(earnings))
#exercise 3.22
years = int(input("Enter number of years you have lived: "))
seconds = years * 365 * 24 *  60 * 60 
print("You have lived for ", int(seconds), "seconds.")
#exercise 3.23
print("table:")
print(1, 1, 1**2, 1**3)
print(1, 2, 2**2, 2**3)
print(1, 3, 3**2, 3**3)
print(1, 4, 4**2, 4**3)
print(1, 5, 5**2, 5**3)


