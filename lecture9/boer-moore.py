# Boer-Moore String Matching Algorithm
def build_bad_char_table(pattern):
  table = {}
  for i, char in enumerate(pattern):
    table[char] = i
  
  return table

def boyer_moore(text, pattern):
  bad_char_table = build_bad_char_table(pattern)
  n = len(text)
  m = len(pattern)
  matches = []

  i = 0

  while i <= n - m:
    j = m - 1

    while j >= 0 and pattern[j] == text[i + j]:
      j -= 1

    if j < 0:
      matches.append(i)
      print(f"Pattern found at index {i}")
      i += m
    else:
      bad_char_shift = bad_char_table.get(text[i + j], -1)
      shift = max(1, j - bad_char_shift)
      i += shift
  
  if not matches:
    print("Pattern not found")
  return matches

# Take Input from the user
text = input("Enter the main text: ")
pattern = input("Enter the pattern to search: ")
match_positions = boyer_moore(text, pattern)

if match_positions:
  print(f"\nPattern '{pattern}' found at positions: {match_positions}")
else:
  print(f"\nPattern '{pattern}' was not found in the given text.")