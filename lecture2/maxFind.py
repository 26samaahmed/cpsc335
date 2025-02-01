# Write a program that can give user to insert positive integers (numbers) that our program will
# will form an array at the backend. We are taking user input. We gave our user the option to choose
# whether user wants to find a max or min value out of those inserted numbers

# Function to find max value in the list
def findMax(L):
  maxValue = L[0]
  for x in L[1:]:
    if x > maxValue:
      maxValue = x
  return maxValue

# Function to find min value in the list
def findMin(L):
  minValue = L[0]
  for x in L[1:]:
    if x < minValue:
      minValue = x
  return minValue


# Take Input from user to create the list of numbers L
user_input = input("Enter numbers seperated by spaces ")
L = list(map(int, user_input.split()))

# Ask user to choose between finding the highest and lower number
choice = input("Type 'max to find the highest number or 'min' to find the lowest number ").strip().lower()

# decision making based on user input
if choice == 'max':
  print("The maximum value in the list is: ", findMax(L))

elif choice == 'min':
  print("The minimum value in the list is: ", findMin(L))

else:
  print("Invalid choice, please type 'max' or 'min' only")



# How do we Analayze the algorithm:
# 1. Identify the basic operations - determine the operations that most affect the algorithm's run time such as comparisons
# 2. Count the operation - estimate the number of times the basic operation is executed in terms of input size, n
# 3. Express growth rate - use big o notation to express how the count of operations grows with N
# 4. Simplify the expression - drop constants and non-dominant terms to simplify the notation to its highest order term

# Exam