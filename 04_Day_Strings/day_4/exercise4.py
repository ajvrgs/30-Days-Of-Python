#exercise 4.1 
print("Thirty" + " " + "Days" + " " + "of" + " " + "Python")
#exercise 4.2
coding = "Coding"
forStr = "For"
allStr = "All"
print(str(coding) + " " + str(forStr) + " " + str(allStr))
#exercise 4.3
company = str(coding) + " " + str(forStr) + " " + str(allStr)
#exercise 4.4
print(str(company))
#exercise 4.5
print("length: " ,  len(company))
#exercise 4.6
print("Upper:" , str(company).upper())
#exercise 4.7
print("Lower:", str(company).lower())
#exercise 4.8
print("ex 4.8: ")
print("Capitalize: ", str(company).capitalize())
print("Title: ", str(company).title())
print("swapcase: ", str(company).swapcase())
#exercise 4.9
print("Slice: ", str(company[0:6]))
#exercise 4.10
print("Find: ", str(company).find("Coding"))
#exercise 4.11
print("replace: ", str(company).replace("Coding", "Python"))
#exercise 4.12
python = "Python for Everyone"
print("replace 2:", str(python).replace("Everyone", "All"))
#exercise 4.13
print("Split: ", str(company).split(" "))
#exercise 4.14
strToSplit = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
print("Split 2: ", str(strToSplit).split(", "))
#exercise 4.15
print("4.15: ", str(company)[0])
#exercise 4.16
print("4.16: ", str(company)[-1])
#exercie 4.17
print("index 10: ", str(company)[10])
#exercise 4.18
strAcronym = "Python for Everyone"
print("Acronym: ", ''.join(word[0].upper() for word in strAcronym.split()))
#exercise 4.19
print("Acronym2: ", ''.join(acword[0].upper() for acword in str(company).split()))
#exercise 4.20
print("1st occurrence of C: ", str(company).index('C'))
#exercise4.21
print("1st occurence of F: ", str(company).index('F'))
#exercise 4.22
strRfind = "Coding for all people"
print("last occurrence of L: ", str(strRfind).rfind('l'))
#exercise 4.23
strIndex = 'You cannot end a sentence with because because because is a conjunction'
print("because 1st: ", str(strIndex.index("because")))
#exercise 4.24
print("because last: ", str(strIndex.rindex("because")))
#exercise 4.25
startLen = str(strIndex).index("because because because")
endLen = (int(startLen) + len("because because because"))
print("slice: ", str(strIndex)[startLen:endLen])
#exercise 4.26
strIndex = 'You cannot end a sentence with because because because is a conjunction'
print("because 1st: ", str(strIndex.index("because")))
#exercise 4.27
startLen = str(strIndex).index("because because because")
endLen = (int(startLen) + len("because because because"))
print("slice: ", str(strIndex)[startLen:endLen])
#exercise 4.28
print("StartsWith coding? : ", str(company).startswith("Coding"))
#exercise 4.29
print("EndsWith coding? : ", str(company).endswith("Coding"))
#exercise 4.30
strSpaces = '&nbsp;&nbsp; Coding For All &nbsp;&nbsp;&nbsp; &nbsp;'
print(str(strSpaces).replace('&nbsp;', ''))
#exercise 4.31
str1 = "30daysofPython"
str2 = "thirty_days_of_python"
print("30daysofPython: ", str1.isidentifier())
print("thirty_days_of_python", str2.isidentifier())
#exercise 4.32
strToHash = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
print("ToJoin: ", "# ".join(strToHash))
#exercise 4.33
print("I am enjoying this challenge\nI wonder what is next")
#exercise 4.34
print("Name\tAge\tCountry\tCity\nAsabeneh\t250\tFinland\tHelsinki")
#exercise 4.35
print(4.35)
radius = 10
area = 3.14 * int(radius) ** 2
print('The area of a circle with radius {} is {:.2f} meters square'.format(radius, area))
#exercise 4.36
print("4.36:")
a, b = 8, 6
print("{} + {} = {}".format(a, b, a + b))
print("{} - {} = {}".format(a, b, a - b))
print("{} * {} = {}".format(a, b, a * b))
print("{} / {} = {:.2f}".format(a, b, a / b))
print("{} % {} = {}".format(a, b, a % b))
print("{} // {} = {}".format(a, b, a // b))
print("{} ** {} = {}".format(a, b, a ** b))
