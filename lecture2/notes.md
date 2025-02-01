How do we Analayze the algorithm:

1. Identify the basic operations - determine the operations that most affect the algorithm's run time such as comparisons
2. Count the operation - estimate the number of times the basic operation is executed in terms of input size, n
3. Express growth rate - use big o notation to express how the count of operations grows with N
4. Simplify the expression - drop constants and non-dominant terms to simplify the notation to its highest order term

Examples for complexity:

1. Constant time, O(1)
   example - checking if a number is even or odd

2. Logarithmic time, O(logn)
   example - finding an item in a balanced binary tree search tree

3. Linear Time - O(n)
   example - when you're summing up all the elements of the given array

Importance of Big O Notation:

1. predicts performance
2. compare algorithms
3. optimize resource usage
4. improve scalability

Big O Notation for findMax and FindMin algorithm would be:

- O(n) where n is the number of elements in the list.
  Both findMax(L) and findMin(L) iterate through the list once, making n comparisons in the worst case

Decision making and print operations are O(1), since they involve a constant number of comparisons
Our overall complexity will be O(n)

Summary of Time complexity:

- Splitting user input into a list O(n)
- Finding Maximum or Minimum Value O(n)
- Decision Making and print statements O(1)
- Overall Complexity O(n)

Best Case Analysis: Big Omega Notation
Average Case Analysis: Big Theta Notation
Worst Case Analysis: Big O Notation
