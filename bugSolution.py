def calculate_average(numbers):
    if not numbers:
        return 0
    # Input validation: Check if all elements are numbers
    if not all(isinstance(num, (int, float)) for num in numbers):
        raise ValueError("List must contain only numbers.")
    total = sum(numbers)
    average = total / len(numbers)
    return average

my_list = []
result = calculate_average(my_list)
print(f"The average is: {result}")

my_list = [1,2,3,4,5]
result = calculate_average(my_list)
print(f"The average is: {result}")

my_list = [1,2,3,4,'a']
try:
    result = calculate_average(my_list)
    print(f"The average is: {result}")
except ValueError as e:
    print(f"Error: {e}") #This will print the ValueError