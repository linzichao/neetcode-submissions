class TrieNode:
    def __init__(self):
        self.children = defaultdict(TrieNode)
        self.is_word = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        node = self.root
        for c in word:
            node = node.children[c]
        node.is_word = True

    def search(self, word: str) -> bool:
        self.res = False

        def dfs(node, word):
            if not word:
                if node.is_word:
                    self.res = True
                return 
            if word[0] == ".":
                for n in node.children:
                    dfs(node.children[n], word[1:])
            else:
                n = node.children.get(word[0])
                if not n:
                    return
                dfs(n, word[1:])
        
        dfs(self.root, word)
        return self.res
                


