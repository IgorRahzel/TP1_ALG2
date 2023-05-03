from TrieTree import Node

# create a new TrieTree object
root = Node()

# insert some words into the TrieTree
root.insert("hello")
root.insert("world")
root.insert("hey")
root.insert("hi")

# search for a word in the TrieTree
node = root.search("hello")
if node is not None:
    print("Found word 'hello' in TrieTree")
else:
    print("Word 'hello' not found in TrieTree")