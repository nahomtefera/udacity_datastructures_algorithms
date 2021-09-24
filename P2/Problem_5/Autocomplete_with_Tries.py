## Represents a single node in the Trie
class TrieNode:
    def __init__(self):
        ## Initialize this node in the Trie
        self.is_word = False
        self.children = {}

    def insert(self, char):
        ## Add a child node in this Trie
        if char in self.children:
            return
        self.children[char] = TrieNode()

    def suffixes(self, suffix='', list=[]):
        ## Recursive function that collects the suffix for
        ## all complete words below this point
        for char in self.children:
            if self.children[char].is_word:
                list.append(suffix + char)
            self.children[char].suffixes(suffix + char, list)

        return list


## The Trie itself containing the root node and insert/find functions
class Trie:
    def __init__(self):
        ## Initialize this Trie (add a root node)
        self.root = TrieNode()

    def insert(self, word):
        ## Add a word to the Trie
        node = self.root

        for char in word:
            if not char in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_word = True

    def find(self, prefix):
        ## Find the Trie node that represents this prefix
        if prefix == '' or prefix is None:
          return 'Enter non-empty prefix'

        node = self.root
        for char in prefix:
            if not char in node.children:
                return 'Not Found'
            node = node.children[char]

        return node


# Testing it all out

# Run the following code to add some words to your trie and then use the interactive search box to see what your code returns.

MyTrie = Trie()
wordList = [
    "ant", "anthology", "antagonist", "antonym", "fun", "function", "factory",
    "trie", "trigger", "trigonometry", "tripod"
]
for word in wordList:
    MyTrie.insert(word)



# Aditional Test cases

# Null value
find_word = MyTrie.find(None)
print(find_word)
# Returns 'Enter non-empty prefix'

# Empty string
find_word = MyTrie.find('')
print(find_word)
# Returns 'Enter non-empty prefix'

# Testing suffix method
suffix = MyTrie.find('a')
print(suffix.suffixes())
#['nt', 'ntagonist', 'nthology', 'ntonym'] 
