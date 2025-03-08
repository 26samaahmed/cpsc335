import heapq # Heap Queue for priority queue operations

# Step 1: Define the Huffman Node
class HuffmanNode:
  def __init__(self, char, freq):
    self.char = char
    self.freq = freq
    self.left = None
    self.right = None

  def __lt__(self, other):
    return self.freq < other.freq
  

# Step 2: Build the Huffman Tree
def build_huffman_tree(freq_map):
  heap = [HuffmanNode(char, freq) for char, freq in freq_map.items()]
  heapq.heapify(heap)

  while len(heap) > 1:
    left = heapq.heappop(heap) # Remove smallest frequency node
    right = heapq.heappop(heap) # Remove second smallest frequency node
    new_node = HuffmanNode(None, left.freq + right.freq)
    new_node.left = left
    new_node.right = right
    heapq.heappush(heap, new_node)

  return heap[0] # The root of the Huffman tree


# Step 3: Generate/Assign Huffman Codes
def build_codes(node, prefix="", code_map={}):
  if node is None:
    return

  if node.char is not None:
    code_map[node.char] = prefix

  build_codes(node.left, prefix + "0", code_map) # left child (0)
  build_codes(node.right, prefix + "1", code_map) # right child (1)

  return code_map

# Step 4: Get user input and compute Huffman Encoding
text = input("Enter the text to encode: ")
freq_map = {char: text.count(char) for char in set(text)}

root = build_huffman_tree(freq_map)
codes = build_codes(root)

encoded_text = ''.join(codes[char] for char in text)
print("Huffman Codes: ", codes)
print("Encoded Text: ", encoded_text)