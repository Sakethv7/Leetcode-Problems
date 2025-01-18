class TrieNode:
    def __init__(self):
        self.children = {}  # Dictionary to store child nodes
        self.is_end_of_word = False  # Flag to mark the end of a word
class Trie:
    def __init__(self):
        self.root = TrieNode()  # Root node of the trie

    def insert(self, word: str) -> None:
        node = self.root
        for char in word:
            # If the character is not already in the current node's children, add it
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True  # Mark the end of the word

    def search(self, word: str) -> bool:
        node = self.root
        for char in word:
            # If the character is not in the current node's children, return False
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_end_of_word  # Return True only if it's the end of a word

    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for char in prefix:
            # If the character is not in the current node's children, return False
            if char not in node.children:
                return False
            node = node.children[char]
        return True  # Return True as long as the prefix is found
