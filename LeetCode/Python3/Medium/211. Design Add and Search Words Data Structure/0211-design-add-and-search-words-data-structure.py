class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False

class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        node = self.root
        for c in word:
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]
        node.is_word = True

    def search(self, word: str) -> bool:
        def search_helper(node, word):
            if not word:
                return node.is_word
            c = word[0]
            if c == '.':
                for child in node.children.values():
                    if search_helper(child, word[1:]):
                        return True
            elif c in node.children:
                return search_helper(node.children[c], word[1:])
            return False
        return search_helper(self.root, word)

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)