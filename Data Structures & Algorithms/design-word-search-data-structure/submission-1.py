class Node:
    def __init__(self):
        self.children = {}
        self.is_end = False

class WordDictionary:

    def __init__(self):
        self.root = Node()
        

    def addWord(self, word: str) -> None:
        node = self.root

        for c in word:
            if c not in node.children:
                node.children[c] = Node()

            node = node.children[c]

        node.is_end = True
        

    def search(self, word: str) -> bool:

        def dfs(index, node):
            if index == len(word):
                return node.is_end
            
            char = word[index]
            
            if char == '.':
                for child in node.children.values():
                    if dfs(index + 1, child):
                        return True

                return False

            else:
                if char not in node.children:
                    return False

                child = node.children[char]
                return dfs(index + 1, child)

        return dfs(0, self.root)