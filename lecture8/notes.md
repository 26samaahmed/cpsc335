# Text Searching Algorithms

Requirements:
Text - T
Length of the text - n
Pattern - P
Length of Pattern - m
Find all the positions of P within given T

There are 4 basic algorithms covering text searching functionality:

1. Naive String Matching
2. Rabin Karp Algorithm
3. KMP (Knuth-Morris-Pratt)
4. Boyer-Moore Algorithm

## Naive Search Matching Algorithm

- Let n be the length of the text and m be the length of the pattern
- For every index i, from 0 to n -m, we will compare substring T to the pattern P
- If all the characters of pattern matches, we print position of i.

Real World Applications:

- Searching in small documents or strings
- Embedded Systems with limited processing powers

## Rabin Karp - Hash Based Pattern Matching
- It computes the hash value of the pattern and substrings of the text.
- If hash matchm it then confirms by comparing the characters.

Real World Application
- Plagiarism Detection
- Large Scale document searching
- Virus Signature scanning
- DNA sequence analysis

Core Idea: given a text (T) and a pattern (P), Rabin Karp computes:
- A hash of pattern
- A rolling hash for each substring of the text
- If the hashes match, algorithm confirms the match
- d is the base (e.g. 256 ASCII characters)
- q is a large prime number (to reduce hash collisions)


## KMP (Knuth-Morris-Pratt): Pattern Guided Matching
Real World Application:
- Spell checking enginers
- Genome sequence alignment
- Word Processors for real time search/replace
- IDEs for live syntax checking

Core Idea is to build a longest prefix suffix (LPS) array
