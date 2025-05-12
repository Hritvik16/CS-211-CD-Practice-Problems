class WordList(list):
    def __init__(self, words):
        if not all(isinstance(w, str) for w in words):
            raise ValueError("All elements must be strings")
        super().__init__(words)

    def __str__(self):
        return "-".join(self)

class WordMap:
    def __init__(self, word_list):
        self.mapping = {}
        for word in word_list:
            if not word:
                continue
            first = word[0]
            if first not in self.mapping:
                self.mapping[first] = []
            self.mapping[first].append(word)

if __name__ == "__main__":
    wl = WordList(["apple", "banana", "apricot", "blueberry", "cherry"])
    print(wl)
    wm = WordMap(wl)
    print(wm.mapping["a"])
    print(wm.mapping["b"])
