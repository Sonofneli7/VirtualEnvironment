# Identity Operators: 'is' / 'is not'
a, b = 3, 4
print(a is b)  # False (different memory addresses)

# Immutable vs Mutable Types

# Immutable example (int)
print(id(a))  # Memory ID before change
a += 3        # Modifies value
print(a, id(a))  # New value, new memory ID

# Mutable example (list)
numbers = [1, 2, 3]
print(id(numbers))  # Memory ID (unchanged with list modification) # address: 2898739073408
# Adding new value to list
numbers.append(100)
print(numbers)      # [1, 2, 3, 100]
print(id(numbers))  # New memory address: 1712607138176


nums = numbers.copy()
print(nums == numbers)  # True # nums = copy of numbers
print(nums is numbers)  # False # Saved at different addresses

# Notes:
    # Hotkey to create new file: Ctrl + Alt + Insert
    # Mutability vs Immutability
    # Mutability: variable can be changed after created.
    # Immutability: variable can't be changed.
