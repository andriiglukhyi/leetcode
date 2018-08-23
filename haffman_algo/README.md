Algorithm Huffman(X):
Input: String X of length n with d distinct characters
Output: Coding tree for X
Compute the frequency f (c) of each character c of X.
Initialize a priority queue Q.
for each character c in X do
Create a single-node binary tree T storing c.
Insert T into Q with key f (c).
while len(Q) > 1 do
( f1,T1) = Q.remove min()
( f2,T2) = Q.remove min()
Create a new binary tree T with left subtree T1 and right subtree T2.
Insert T into Q with key f1+ f2.
( f ,T) = Q.remove min()
return tree T