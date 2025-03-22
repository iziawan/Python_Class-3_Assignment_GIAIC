# 6. Count how many times the number 5 appears in the list [5, 10, 5, 20, 5, 30].
count_list = [5, 10, 5, 20, 5, 30]
print(count_list.count(5))

# 7. Sort the list [9, 1, 8, 3, 5] in ascending and descending order. 
sort_list = [9, 1, 8, 3, 5]
sort_list.sort()
print(sort_list)
sort_list.sort(reverse=True)
print(sort_list)

# 8. Reverse the list [“apple”, “banana”, “cherry”] using the reverse() method.
fruits = ["apple", "banana", "cherry"]
fruits.reverse()
print(fruits)

# 9. Create a copy of the list [1, 2, 3, 4, 5] and store it in another variable. Modify the 
# copied list and print both lists. 
original_list = [1, 2, 3, 4, 5]
copied_list = original_list.copy()
copied_list.append(6)
print(original_list)
print(copied_list)

# 10. Clear all elements from a list [“hello”, “world”, “python”] using the clear() 
# method. 
clear_list = ["hello", "world", "python"]
clear_list.clear()
print(clear_list)