import time

# Selection Sort Algorithm
def selection_sort(books):
  n = len(books)
  for i in range(n):
    min_index = i

    for j in range(i + 1, n):
      if books[j][1] < books [min_index][1]:
        min_index = j
    books[i], books[min_index] = books[min_index], books[i]


# User Input
num_books = int(input("Enter a number of books: "))
books = []
for _ in range(num_books):
  name = input("Enter a book title: ")
  year = int(input("Enter the publication year for {name}; "))
  books.append((name, year))


# Measure Execution time
start_time = time.time()
selection_sort(books)
end_time = time.time()
print(f"Execution time: {end_time - start_time:.6f} seconds")

print("Books sorted by year", books)
