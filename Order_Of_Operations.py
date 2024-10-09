# Order Precedence
# 1: Exponentiaton **
# 2: Mult. (*) and Division(/)
# 3: Addition (+) and Subtraction (-)


print(2 + 4  * 2 ** 3)    # 8 * 4 + 2 = 34

# Change order of op by using ()
print((2 + 4)  * 2 ** 3)    # 6 * 8 = 48

print(1_000_000_000)      # use underscores for readability
print(1000 == 1_000)      # True: they equal eachother, parsed the same
