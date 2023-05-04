from TrieTree import Node

# create a new TrieTree object
root = Node(value=-1)

counter = 0

string = 'sir sid eastman easily teases sea sick seals'
n = len(string)
i = 0
while i < n:
    counter = 0
    prefix = root.insert(string[i],value = root.value + 1)
    if prefix == None:
        root.value += 1
        i+=1
    else:
        while prefix != None:
            if i < len(string) -1 :
                new_letter = string[i+1] 
            if counter == 0:
                word = prefix + new_letter
            else:
                word += new_letter
            prefix = root.insert(word,value = root.value + 1)
            counter += 1
            i+=1
        i += 1
        root.value += 1


root.search('s')
# insert some words into the TrieTree
'''
root.insert("hello",value = root.value + 1)
root.value +=1
root.insert("world",value = root.value + 1)
root.value +=1
root.insert("hey",value = root.value + 1)
root.value +=1
root.insert("hi",value = root.value + 1)
root.value +=1
print(root.value)
'''
# search for a word in the TrieTree
node = root.search("h")
if node is not None:
    print("Found word 'hello' in TrieTree")
else:
    print("Word 'hello' not found in TrieTree")