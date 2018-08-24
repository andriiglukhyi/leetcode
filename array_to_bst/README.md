Given a sorted array. Write a program that creates a Balanced Binary Search Tree using array elements. If there are n elements in array, then floor(n/2)'th element should be chosen as root and same should be followed recursively.

Input:

The first line of input contains an integer T denoting the number of test cases.
The first line of each test case is N,N is the size of array.
The second line of each test case contains N input A[].

Output:

Print the preorder traversal of constructed BST.

Constraints:

1 ≤ T ≤ 100
1 ≤ N ≤ 1000
1 ≤ A[] ≤ 10000

Example:

Input:
1
7
1 2 3 4 5 6 7

Output:
4 2 1 3 6 5 7