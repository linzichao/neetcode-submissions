class PrefixTree:

    def __init__(self):
        self.word_dict = {}

    def insert(self, word: str) -> None:
        d = self.word_dict
        for c in word:
            d = d.setdefault(c, {})
        d['\0'] = True

    def search(self, word: str) -> bool:
        d = self.word_dict
        for c in word:
            if c not in d:
                return False
            d = d[c]
        return d.get('\0', False)

    def startsWith(self, prefix: str) -> bool:
        d = self.word_dict
        for c in prefix:
            if c not in d:
                return False
            d = d[c]
        return True