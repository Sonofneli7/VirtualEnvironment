# Java example

# class Main{
#     public static void main(String[] args){
#         int score;
#         score = 10;

#         System.out.println(score)
#     }
# }


# Python code

score = 10
print(type(score))

# result: <class 'int'>

# declaring another var
a = 5
print(type(a))  # result: <class 'int'>

a = 'python'
print(type(a))  # result: <class 'str'>


# var has ID, what is it and how do we get? # use built-in id function # Lists reference in stored memory
print(id(a))    # result: 2013109451776


my_var = 10

# my_var: reference to an int object containing value of 10 
print(id(my_var))   # result: 140722997889752












# Notes
    # Static typing: var types known before runtime (C, C++, Java, Go)
    # Python = dynamic typing: types linked to values at runtime, not variables
    # Python = values stored in vars have types, not the name of var itself
    # Means that code can be written a little quicker
    # Var = an object/instance of a class = has type of value and an ID & are constant during the var lifetime
    # Static typed languages = better performance at run-time
    # Dynamic typed languages = faster at development/ more flexible
    