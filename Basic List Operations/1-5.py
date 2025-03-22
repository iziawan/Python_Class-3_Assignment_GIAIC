# 1. Create a list of five numbers and append a new number to it. Print the updated list.
numbers = [10, 20, 30, 40, 50]
numbers.append(60)
print(numbers)

# 2. Extend a list [1, 2, 3] with another list [4, 5, 6]. Print the result. 
list1 = [1, 2, 3]
list2 = [4, 5, 6]
list1.extend(list2)
print(list1)

# 3. Insert the string "Python" at index 2 in the list ["Java", "C++", "JavaScript", 
# "Ruby"]. 
languages = ["Java", "C++", "JavaScript", "Ruby"]
languages.insert(2, "Python")
print(languages)

# 4. Remove the first occurrence of the number 10 from the list [10, 20, 30, 10, 40].
num_list = [10, 20, 30, 10, 40]
num_list.remove(10)
print(num_list)

# 5. Use the pop() method to remove the last element from [100, 200, 300, 400] and 
# print the modified list. 
pop_list = [100, 200, 300, 400]
pop_list.pop()
print(pop_list)
