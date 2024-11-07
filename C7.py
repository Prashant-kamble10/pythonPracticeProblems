#  find the 2nd largest number from the list

def find_second_largest(numbers):
     numbers.sort(reverse=True)
     print(numbers[1])

# Test cases
find_second_largest([12, 35, 1, 10, 34, 1])  # Should return 34
find_second_largest([10, 5, 10])  # Should return 5
