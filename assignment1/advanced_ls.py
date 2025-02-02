def linear_search(L, T):
  res = []
  for index in range(len(L)):
    if L[index] == T:
      res.append(index)
  return res

# Take User Input for list of elements
user_input = input("Enter a list elements seperated by spaces: ")
L = list(map(int, user_input.split()))

# Take user input for the target element
T = int(input("Enter the target element to search: "))

# Calling the linear_search function and store the result
result = linear_search(L, T)

# Display result
# If length is not zero then the element appeared at least once in the list
if len(result) != 0:
  print(f"Element {T} found at indices {result}")
else:
  print(f"Element {T} not found in the list")