# obj == dict

ages = {"Alice": 25, "Bob": 30, "Charlie": 22}

# access key value pair in dict 
print(ages["Alice"])

# Accessing all keys in dict
key = ages.keys()
print(key)

# Accessing all values in dict
value = ages.values()
print(value)

# Accessing all key values pairs together
item = ages.items()
print(item)


# update in dict

ages["Bob"] = 32
print(ages)

ages["prashant"] = 25
print(ages)

# Example dictionary
person = {"name": "Alice", "age": 30, "city": "New York"}

# Updating with another dictionary using |=
person |= {"age": 34, "city": "San Francisco"}
print(person)  # Output: {'name': 'Alice', 'age': 34, 'city': 'San Francisco'}


# Original dictionaries
person = {"name": "Alice", "age": 30}
contact_info = {"email": "alice@example.com", "phone": "123-456-7890"}

# Combining into a new dictionary |
updated_person = person | contact_info
print(updated_person)  # Output: {'name': 'Alice', 'age': 30, 'email': 'alice@example.com', 'phone': '123-456-7890'}


