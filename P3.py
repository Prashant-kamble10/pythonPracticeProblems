# list == array

# append in list
fruits = ["apple", "banana", "cherry"]
fruits.append("lichi")
print(fruits)

# insert in list
# list_name.insert(index, item)
fruits.insert(2, "orange")
print(fruits)

# remove element in list
fruits1 = ["apple", "banana", "cherry"]
fruits1.remove("banana")
print(fruits1)

# sort in list
numbers = [3, 1, 4, 1, 5, 9]
numbers.sort()
print(numbers)

numbers.sort(reverse=True)
print(numbers)

words = ["bananaaaaaaaaaaa", "apple", "cherryyyy"]
words.sort(key=len)
print(words)