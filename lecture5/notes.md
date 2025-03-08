## Greedy Algorithm

Approach: If you have $5, $1, and 50 cents coins, you will first pick a $5 bill, then 2 of $1 bills, and finally a 50 cent coin.

Any problem can be solved with Greedy Algorithm if it qualifies 2 properties:

1. Greedy Choice Approach
2. Optical Substructure

## Huffman Coding

- It is a greedy algorithm used for lossless data compression by reducing number of bits required to represent a character.

How: It assigns shorter codes to more frequent characters and longer codes to less frequent ones.

Real World Applications:

- File Compression (zip, png, jpeg)
- Morse Code (Short codes for frequent letters, longer for rare ones)
- Data Encoding in Networks

Why: Standard Character encoding like ASCII - It uses fixed length codes, (e.g. 8 bits per character). However, not all characters appear equally often - some are more frequent

Solution: Huffman coding assigns variable length binary codes, thus minimizes the total number of bits used for encoding.

Step by Step for Huffman Coding:
1. Calculate the frequency of each character in the input text
2. Create a priority queue (min-heap) where each character is a node sorted by frequency
3. Merge the two least frequent nodes
4. Repeat until one/single node remain
5. Assign binary codes (Left child -> 0, Right child -> 1)
6. Generate Huffman Codes by traversing the tree.

