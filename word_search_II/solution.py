# class Node:
#     def __init__(self, letter=None):
#         self.val = letter
#         self.kids = {}

# class Solution:
#     def findWords(self, board, words):
#         """
#         :type board: List[List[str]]
#         :type words: List[str]
#         :rtype: List[str]
#         """
#         # lest build the tree for fast search
#         def build_tree(node, word):
#             if word  == "":
#                 return
#             if word[0] in node.kids:
#                 build_tree(node[word[0]], word[1:])
#             else:
#                 node[word[0]] = Node(word[0])
#                 build_tree(node[word[0]], word[1:])
#         # create root
#         root = Node()
#         # add all possible words to the tree
#         for word in words:
#             build_tree(root, word)
        
#         # function for bord traversing
#         def traverse(letter, ) 



class Solution:
    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        end_words = set()
        def traverse(i, j, word, letter, visited):
            non local end_words
            if letter == len(word) - 1:
                end_words.add(word)
            if i < 0 or j < 0 or i > len(board[0] - 1) or j > len(board) - 1 or (i,j) in visited or board[i][j] != word[letter]:
                return 
            visited.add((i,j))
            traverse(i + 1, j, word, letter+1, visited)
            traverse(i - 1, j, word, letter+1, visited)
            traverse(i, j-1, word, letter+1, visited)
            traverse(i, j+1, word, letter+1, visited)
        letterrs = {}
        for i if range(len(board[0])):
            for j in range(len(board)):
                if board[i][j] in letterrs:
                    letterrs[board[i][j]] += [(i,j)]
                else:
                    letterrs[board[i][j]] = [(i,j)]
        for word in words:
            if word[0] in letterrs:
                for tuples in letterrs[word[0]]:
                    visited = set()
                    traverse(tuples[0], tuples[1], word, 0, visited)
        return list(end_words)


# Input: 
# words = ["oath","pea","eat","rain"] and board =
# [
#   ['o','a','a','n'],
#   ['e','t','a','e'],
#   ['i','h','k','r'],
#   ['i','f','l','v']
# ]

# Output: ["eat","oath"]