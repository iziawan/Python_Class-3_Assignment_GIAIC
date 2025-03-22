# 16. Write a function that takes a list and returns a new list with all even numbers removed.
def remove_evens(lst):
    return [num for num in lst if num % 2 != 0]

print(remove_evens([1, 2, 3, 4, 5, 6]))

# 17. Create a function that accepts a list and returns a new list with elements sorted in 
# descending order without using the sort() method. 
def sort_descending(lst):
    return sorted(lst, reverse=True)

print(sort_descending([3, 1, 4, 1, 5, 9]))

# 18. Given a list of numbers, write a program to remove all duplicate elements and print the 
# unique elements. 
def remove_duplicates(lst):
    return list(set(lst))

print(remove_duplicates([1, 2, 2, 3, 4, 4, 5]))

# 19. Given a tuple of names (“Alice”, “Bob”, “Charlie”, “Alice”, “David”), convert 
# it into a list, remove duplicates, and convert it back to a tuple. 
names_tuple = ("Alice", "Bob", "Charlie", "Alice", "David")
names_list = list(set(names_tuple))
names_tuple = tuple(names_list)
print(names_tuple)

# # 20. Create a program that takes a list of mixed data types (int, str, float) and separates 
# integers into one list, strings into another, and floats into another. 
def separate_types(lst):
    ints = [x for x in lst if isinstance(x, int)]
    strs = [x for x in lst if isinstance(x, str)]
    floats = [x for x in lst if isinstance(x, float)]
    return ints, strs, floats

mixed_list = [1, "hello", 2.5, 3, "world", 4.0, "Python"]
print(separate_types(mixed_list))
