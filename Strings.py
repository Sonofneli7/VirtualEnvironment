# Intro Python Strings
from comments import my_str

# No diff b/t single and double quotes, goal = remain consistent w. whichever you choose
my_str1 = 'I learned python.'
my_str2 = "I learned python."

print(my_str1)

# In PyCharm, can display variable only by calling print() function

# Print quotes: eg., Hi there! I'm Nelson.
print("Hi there! I'm Nelson.")      # for brevity, used double quotes when using a single w.in sentence

print('Hi there! I \'m Nelson.')    # alternate way, use escape character in middle of I'm


# Permitted: using double quotes inside single quotes
message = 'He said: "Go for it!"'
print(message)

print(type(message))                # <class 'str'>

# Mult. Line String  # """ used for creating doc strings or document strings
# """""" way of documenting modules, classes, and functions

languages = """I like Python
Golang                              
and 
Solidity.

"""
print(languages)

# Does same as above but with \n infusion # back-slash "N" = escape sequence
my_language = 'I like Python \nGolang\nand\nSolidity'
print(my_language)

print('a\tb\tc\td\ne')               #  a	b	c	d
                                     #  e
# If want to print back slash literaly
print('\\n')

print('He says: "I \'m 20"')







# Notes
    # Strings = ordered sequence of UTF - 8 encoded characters
    # Concatenate and Slice strings
    # Get user input
    # Convert Types