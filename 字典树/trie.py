# -*- coding: utf-8 -*-
"""
 author: NotOne
 data:2020-08-07 16:06
"""


class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = {}
        self.end_with_word = '#'

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        node = self.root
        for w in word:
            node = node.setdefault(w, {})
        node[self.end_with_word] = self.end_with_word

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        node = self.root
        for w in word:
            if w not in node:
                return False
            node = node[w]
        return self.end_with_word in node

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        node = self.root
        for w in prefix:
            if w not in node:
                return False
            node = node[w]
        return True


if __name__ == '__main__':
    trie = Trie()
    trie.insert('lvsongke')
    print(trie.root)