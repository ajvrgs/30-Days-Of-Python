print("Day 2: 30 days of python programming")
first_name = 'Honney Joy'
last_name = 'Manansala'
full_name = 'Honney Joy Manansala'
country = 'Philippines'
city = 'Tondo'
age = '28'
year = '2026'
isMarried = True
isTrue = True
is_light_on = True
var1, var2, var3, var4, var5 = 0, 1, 'helloo', 'hi', 2

#exercise 2.1
print('first_name: ', type(first_name))
print('last_name: ', type(last_name))
print('full_name: ', type(full_name))
print(type(country))
print(type(city))
print(type(age))
print(type(year))
print(type(isMarried))
print(type(isTrue))
print(type(is_light_on))
print(type(var1))
print(type(var2))
print(type(var3))
print(type(var4))
print(type(var5))

#exercise 2.2
print('first_name len: ', len(first_name))

#exercise 2.3
print('the length of first_name is: ', len(first_name), ' while the length of the last_name is: ', len(last_name))

#exercise 2.4
num_one = 5
num_two = 4

#exercise 2.5
totalSum = num_one + num_two
print('sum: ', totalSum)

#exercise 2.6
totaldiff = num_two - num_one
print('diff: ', totaldiff)

#exercise 2.7
totalMul = num_two * num_one
print('mul: ', totalMul)

#exercise 2.8
totalDiv = num_one / num_two
print('div: ', totalDiv)

#exercise 2.9
totalMod = num_two % num_one
print('mod: ', totalMod)

#exercise 2.10
exp = num_one ** num_two
print('power: ', exp)

#exercise 2.11
floor_division = num_one // num_two
print('fd: ', floor_division)

#exercise 2.12
radInput = input('input radius: ')
area_of_circle = 3.1416 * int(radInput)
circum_of_circle = 2 * 3.1416 * int(radInput)
print('ac: ', area_of_circle)
print('cc: ', circum_of_circle)

#exercise 2.13
first_name = input('first_name: ')
last_name = input('last_name: ')
country = input('country: ')
age = input('age: ')

print('fn: ', str(first_name), ', ln: ', str(last_name), ',country: ', str(country), ', age: ', int(age))


