# 5. Default Parameter Value
# Problem: Write a function that greets a user. If no name is provided, it should greet with a default name.

def greet(namaate="Namaste"):
    return f"good morning, {namaate}"

print(greet("prashant"))
print(greet())