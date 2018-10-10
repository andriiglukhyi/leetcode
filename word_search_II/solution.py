class Node:
    def __init__(self, letter=None):
        self.val = letter
        self.kids = {}

class Solution:
    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        # lest build the tree for fast search
        def build_tree(node, word):
            if word  == "":
                return
            if word[0] in node.kids:
                build_tree(node[word[0]], word[1:])
            else:
                node[word[0]] = Node(word[0])
                build_tree(node[word[0]], word[1:])
        # create root
        root = Node()
        # add all possible words to the tree
        for word in words:
            build_tree(root, word)
        
        # function for bord traversing
        def traverse(letter, ) 


