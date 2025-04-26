# Naiive String matching
def naive_search(text, pattern):
  positions = [] # store the indices where pattern is found
  n = len(text)
  m = len(pattern)

  # Loop through all possible starting positions
  for i in range(n - m + 1):
    match = True
    for j in range(m): # compare each character
      if text[i + j] != pattern[j]:
        match = False
        break

    if match:
      positions.append(i) # store the index of the match
  return positions


# Example Input
text = "Hello World, this is Computer Science !!"
pattern = "Computer"

#output
print("Naive Search matching found at: ", naive_search(text, pattern))