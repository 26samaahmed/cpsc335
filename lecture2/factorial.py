# Calculate the factorial of a number
def factorial(n):
  if n < 0:
    return "Factorial is not defined for negative numbers"
  res = 1
  for i in range(2, n + 1):
    res *= i
  return res

# Take user input
num = int(input('Enter a number: '))
print(f"Factorial of {num} {Iterative} is: {factorial(num)}")