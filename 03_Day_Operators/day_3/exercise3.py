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

