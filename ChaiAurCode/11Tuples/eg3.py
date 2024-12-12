nested_tuple = ((1, 2, 3), ("a", "b", "c"), (4.5, 5.5, 6.5))

inner_tuple = nested_tuple[0]
print(inner_tuple)   # (1, 2, 3)

element = nested_tuple[0][1]
print(element)      # 2