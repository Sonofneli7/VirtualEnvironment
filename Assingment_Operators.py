# Assignment operators: = , += , -= , *= , /= , **= , %=
# Equals(=) Assign 5 to 'a'
a = 5
print(a)

# Plus Equals(+=) Increment assingment operator
a += 2        # Add 2 to 'a'; shorthand for (a = a + 2)
print(a)      # 5+2 = 7

# Minus Equals(+=) Decrement assingment operator
a -= 3        # Minus 3 to 'a'; (a = a - 3)
print(a)      # 7-3 = 4

# Star Equals(*=) Multiplication assingment operator
a *= 3        # Multiply 3 to 'a'  a = a * 3
print(a)      # 4*3 = 12

# Slash Equals(/=) Multiplication assingment operator
a /= 2        # Divide 2 by a       a = a / 2
print(a)      # 12/2 = 6.0

# Doube Star Equals(**=) power assingment operator
a **= 2       # a = a ** 2
print(a)      # 6 ** 6 = 36

# if want to increment by 1
a += 1
print(a)

# Percent Equals(%=) Modulus assingment operator
a %= 2
print(a)

# divmod()
a, b = divmod(14, 6)  # division and remainder
print(a, b)           # 14/ 6 = 2 with 2 as remainder

# pow()
print(pow(5, 9))      # 1953125

# sum()     calculate sum of items in an iterable datatype
print(sum([1,2,5,6,7,7,9]))     # print sums of list of numbers # sum = 37

# max()   finds & returns max value in an iterable datatype
print(max([1,2,5,6,7,7,9]))     # max_number = 9

# min()   finds & returns min value in an iterable datatype
print(min([1,2,5,6,7,7,9,-6]))  # min_number = -6

# round()   rounds float to a given decimal place
a = 5.666772
print(round(a, 3))              # 5.667
b = round(a, 1)
print(a, b)                     # 5.666772 5.7