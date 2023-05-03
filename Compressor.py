from TrieTree import Node

# create a new TrieTree object
root = Node(value=-1)

# insert some words into the TrieTree
root.insert("hello",value = root.value + 1)
root.value +=1
root.insert("world",value = root.value + 1)
root.value +=1
root.insert("hey",value = root.value + 1)
root.value +=1
root.insert("hi",value = root.value + 1)
root.value +=1
print(root.value)

# search for a word in the TrieTree
node = root.search("hi")
if node is not None:
    print("Found word 'hello' in TrieTree")
else:
    print("Word 'hello' not found in TrieTree")