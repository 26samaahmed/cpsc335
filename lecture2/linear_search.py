# Define function to perform linear search
def linear_search(L, T):
  for index in range(len(L)):
    if L[index] == T:
      return index
  return -1

# Take User Input for list of elements
user_input = input("Enter a list elements seperated by spaces: ")
L = list(map(int, user_input.split()))

# Take user input for the target element
T = int(input("Enter the target element to search: "))

# Calling the linear_search function and store the result
result = linear_search(L, T)

# Display result
if result != -1:
  print(f"Element {T} found at index {result}")
else:
  print(f"Element {T} not found at index {result}")