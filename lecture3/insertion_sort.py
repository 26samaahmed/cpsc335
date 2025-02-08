import time
# Insertion Sort Algorithm

def insertion_sort(cards):
  for i in range(1, len(cards)):
    key = cards[i] # The card to be placed in the correct position
    j = i - 1 # Index of the last card in the sorted position

    # Move elements of the sorted portion
    while j >= 0 and key < cards[j]:
      cards[j + 1] = cards[j] # shift the elements to the right
      j -= 1 # move one step to the left

    cards[j + 1] = key # Place key in its correct position


# Taking user input
cards = list(map(int, input("Enter card numbers sepearted by space: ").split()))

# Measure the execution time
start_time = time.time()
insertion_sort(cards)
end_time = time.time()

# Print sorted cards and execution time
print("Sorted cards: ", cards)
print(f"Execution time: {end_time - start_time:.6f} seconds")