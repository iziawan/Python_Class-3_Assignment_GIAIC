# 11. Create a tuple with 5 different fruits and print the third fruit. 
fruits_tuple = ("apple", "banana", "cherry", "mango", "water melon  ")
print(fruits_tuple[2])

# 12. Convert the tuple (10, 20, 30, 40, 50) into a list, remove the number 30, and convert 
# it back into a tuple. 
tuple_data = (10, 20, 30, 40, 50)
list_data = list(tuple_data)
list_data.remove(30)
tuple_data = tuple(list_data)
print(tuple_data)

# 13. Try to append an element to the tuple (“A”, “B”, “C”). What happens? How can you 
# modify a tuple indirectly? 
tuple_abc = ("A", "B", "C")
# tuple_abc.append("D")  # This will raise an error
# Indirect modification:
modified_tuple = tuple_abc + ("D",)
print(modified_tuple)

# 14. Unpack the tuple (100, 200, 300) into three separate variables and print them.
tuple_unpack = (100, 200, 300)
a, b, c = tuple_unpack
print(a, b, c)

# 15. Count the occurrences of 7 in the tuple (7, 1, 7, 3, 7, 5). 
tuple_count = (7, 1, 7, 3, 7, 5)
print(tuple_count.count(7))