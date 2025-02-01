# Create Algorithm to find Max
# Input: a list of numbers L
# Output: the maximum number in the list  L
# maxValue <- L[0]
  # for each number n in L starting from second element
  #     if n > maxValue   then
  #         maxValue <- n
  # end for
  # return maxValue

def maxValue(L):
    maxValue = L[0]
    for n in L[1:]:
        if n > maxValue:
            maxValue = n
    return maxValue

numbers = [17, 2, 8, 117, 1008]
print("The maximum value is:", maxValue(numbers))