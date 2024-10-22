1) Write a program to get the tuple elements and print it.
Sample Input:
3
20
10
30
Sample Output:
(20, 10, 30)
Ans:
#python
lst=[]
n=int(input())
for i in range(0,n):
    ele=int(input())
    lst.append(ele)
print(tuple(lst))

2) Write a program to get the elements of tuple in a single line separated by space and print the tuple values.
Sample Input:
20 10 30
Sample Output:
20, 10, 30
Ans 
a=map(int,input().split())
b=tuple(a)
print(b)

 3) Write a program to get the tuple elements in a single line separated by spaces and print the number of elements in the given tuple.
Sample Input:
10 20 30
Sample Output:
3
  # Get input from the user
input_string = input("Enter tuple elements separated by spaces: ")

# Split the input string into a list and convert it to a tuple
tuple_elements = tuple(input_string.split())

# Print the number of elements in the tuple
print(len(tuple_elements))
  
4) Write a program to get n number of tuple elements from the user in separate lines and print the sum of their values using predefined method.
Sample Input:
3
10
20
30
Sample Output:
60
  # Function to get n number of tuple elements and calculate their sum
def sum_of_tuples():
    # Get the number of elements
    n = int(input("Enter the number of elements: "))
    
    # Initialize an empty tuple
    elements = ()
    
    # Loop to get n elements from the user
    for _ in range(n):
        value = int(input())
        elements += (value,)  # Adding the value to the tuple
    
    # Calculate the sum of the tuple elements
    total_sum = sum(elements)
    
    # Print the sum
    print(total_sum)

# Call the function
sum_of_tuples()


  5) Write a program to get n number of tuple elements from the user in separate line and print the maximum value of the given values.
Sample Input:
3
20
10
30
Sample Output:
30
  # Get the number of elements from the user
n = int(input("Enter the number of tuple elements: "))

# Initialize an empty list to store the elements
elements = []

# Loop to get n elements from the user
for _ in range(n):
    element = int(input())  # Read each element as an integer
    elements.append(element)  # Append the element to the list

# Convert the list to a tuple
tuple_elements = tuple(elements)

# Print the maximum value in the tuple
print(max(tuple_elements))

6) Write a program to get n number of values from user in separate line and print the minimum value of the given tuple.
Sample Input:
3
20
30
10
Sample Output:
10
        # Get the number of elements from the user
n = int(input("Enter the number of values: "))

# Initialize an empty list to store the values
values = []

# Loop to get n values from the user
for _ in range(n):
    value = int(input())  # Read each value as an integer
    values.append(value)  # Append the value to the list

# Convert the list to a tuple
tuple_values = tuple(values)

# Print the minimum value in the tuple
print(min(tuple_values))

7) Write a program to get the tuple values in a single line separated by space and count the nuber of times the given x value is present in the given tuple.
Sample Input:
1 2 3 1 2 3 4 1 2 1
1
Sample Output:
4
        # Get input for tuple elements from the user
input_string = input("Enter tuple elements separated by spaces: ")

# Split the input string into a list and convert it to a tuple
tuple_values = tuple(input_string.split())

# Get the value to count from the user
x = input("Enter the value to count: ")

# Count the occurrences of x in the tuple
count_x = tuple_values.count(x)

# Print the count
print(count_x)

8) Write a program to get tuple elements in a single line separated by spaces and print the sum of the elements without using sum() method.
Sample Input:
10 20 30
Sample Output:
60
# Get input for tuple elements from the user
input_string = input("Enter tuple elements separated by spaces: ")

# Split the input string into a list and convert it to a tuple of integers
tuple_elements = tuple(map(int, input_string.split()))

# Initialize a variable to hold the sum
total = 0

# Loop through the tuple and add each element to the total
for element in tuple_elements:
    total += element

# Print the sum of the elements
print(total)

9) Raju is a 3rd grade kid, he is struggling to find which is "even" number and which is a "odd" number. So, his teacher gave him a task to find how many even numbers and how many odd numbers are there in the given collection of values and print "Even" if even count is more than odd count, else print "Odd", if odd count is more and print "Equal" if both even count and odd count are same. Help Raju to understand the difference of even and odd.
Sample Input:
1 2 3 4 5
Sample Output:
Odd
# Get input for numbers from the user
input_string = input("Enter numbers separated by spaces: ")

# Split the input string into a list of integers
numbers = list(map(int, input_string.split()))

# Initialize counters for even and odd numbers
even_count = 0
odd_count = 0

# Loop through the numbers and count even and odd
for number in numbers:
    if number % 2 == 0:
        even_count += 1
    else:
        odd_count += 1

# Determine which count is greater and print the result
if even_count > odd_count:
    print("Even")
elif odd_count > even_count:
    print("Odd")
else:
    print("Equal")

10) Write the program to count the number of times the given number (x) is present in the given tuple list and print it's factorial value without using factorial() method.
Sample Input:
1 2 3 4 1 5 1
1
Sample Output:
6
# Get input for tuple elements from the user
input_string = input("Enter tuple elements separated by spaces: ")

# Split the input string into a list and convert it to a tuple
tuple_elements = tuple(map(int, input_string.split()))

# Get the value to count from the user
x = int(input("Enter the number to count: "))

# Count the occurrences of x in the tuple
count_x = tuple_elements.count(x)

# Function to calculate factorial without using factorial() method
def calculate_factorial(n):
    if n == 0 or n == 1:
        return 1
    factorial = 1
    for i in range(2, n + 1):
        factorial *= i
    return factorial

# Calculate the factorial of the count
factorial_value = calculate_factorial(count_x)

# Print the count and its factorial
print(factorial_value)


