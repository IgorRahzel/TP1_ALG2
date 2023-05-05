from TrieTree import Node

with open("myfile.txt", "w") as f:
    f.write('')
f.close()

# create a new TrieTree object
root = Node(value=0)

counter = 0
num_nodes = 0

string = 'sir sid eastman easily teases sea sick seals'
n = len(string)
i = 0
while i < n:
    counter = 0
    prefix = root.insert(string[i],value = num_nodes + 1)
    if prefix == None:
        num_nodes += 1
        i+=1
    else:
        while prefix != None:
            if i < len(string) -1 :
                new_letter = string[i+1] 
            else:
                new_letter = '\0'
            if counter == 0:
                word = prefix + new_letter
            else:
                word += new_letter
            prefix = root.insert(word,value = num_nodes + 1)
            counter += 1
            i+=1
        i += 1
        num_nodes += 1


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
node = root.search(" ")
if node is not None:
    print("Found word 'hello' in TrieTree")
else:
    print("Word 'hello' not found in TrieTree")