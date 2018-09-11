class Node:
    def __init__(self, d = None):
        self.data = d
        self.children = {}

class MagicDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = Node()

    def buildDict(self, dict):
        """
        Build a dictionary through a list of words
        :type dict: List[str]
        :rtype: void
        """
        for item in dict:
            self.insert_item(self.root, item)

    def search(self, word):
        """
        Returns if there is any word in the trie that equals to the given word after modifying exactly one character
        :type word: str
        :rtype: bool
        """
        counter = 0
        return self.find_possability(self.root, word, counter)
    def insert_item(self, root, str):
        """
        recursevly go down and build try tree
        """
        if not str:
            return
        if str[0] in root.children:
            insert_item(root[str[0]], str[1:])
        root.children[str[0]] = Node(str[0])
        insert_item(root[str[0]], str[1:])
    
    def find_possability(root, str, c):
        if not  str:
            return True
        if str[0] in root.children:
            find_possible(root.children[str[0]], str[1:], c)
        c+= 1
        if c>1:
            return False
        for item in root.children:
            if str[1] in root.children[item].children:
                find_possible(root.children[item], str[1:], c)
            else:
                return False
dct = MagicDictionary()
dct.buildDict(["hello", "leetcode"])

print(dct.buildDict('hello'))

# Your MagicDictionary object will be instantiated and called as such:
# obj = MagicDictionary()
# obj.buildDict(dict)
# param_2 = obj.search(word)