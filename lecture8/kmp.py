# KMP Algorithm
def compute_lps(pattern):
  m = len(pattern)
  lps = [0] * m
  length = 0 # Length of the previous longest prefix suffix
  i = 1

  while i < m:
    if pattern[i] == pattern[length]:
      length += 1
      lps[i] = length
      i += 1
    else:
      if length != 0:
        length = lps[length - 1]
      else:
        lps[i] = 0
        i += 1
  return lps


def kmp_search(text, pattern):
  n, m = len(text), len(pattern)
  lps = compute_lps(pattern) # preprocess the pattern
  positions = []
  i = j = 0

  while i < n:
    if pattern[j] == text[i]:
      i += 1
      j += 1

    if j == m:
      positions.append(i - j) # Match found
      j = lps[j - 1] # Update j using lps

    elif i < n and pattern[j] != text[i]:
      if j != 0:
        j = lps[j - 1]
      else:
        i += 1
  return positions


# Example Input
text = "Hello World, this is Computer Science !!"
pattern = "Computer"

# Output
print("KMP matching found at: ", kmp_search(text, pattern))