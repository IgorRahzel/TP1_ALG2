import numpy as np
class Node:
    def __init__(self,value=None, label='', children=None):
        self.value = value if value is not None else None
        self.children = children if children is not None else []
        self.label = label
        

    def search(self, word, i=0):
        for child in self.children:
            if child.label == word[i]:
                if i == len(word) - 1:
                    if child.value != None:
                        return self
                else:
                    for child in self.children:
                        node = child.search(word, i + 1)
                        if node is not None:
                            return node
                return None

    def insert(self, word, i=0,value=None,firstLook = False,bitSize = None):
        #checks if word is only a single character
        if len(word) == 1:
            for child in self.children:
                if child.label == word:
                    return word
        else:
            # search for a child node with the same label as the current character
            for child in self.children:
                if child.label == word[i]:
                    # if this is the last character of the word, set the value of the node to the word
                    if i == len(word) - 1:
                        return child.label
                    else:
                        return child.insert(word, i + 1,value,firstLook,bitSize)
                    

        # if no child node with the same label exists, create a new one and add it to the children list
        if len(word) == 1:
            node = Node(label=word)
            self.children.append(node)
        else:
            node = Node(label=word[i])
            self.children.append(node)

        # if this is the last character of the word, set the value of the node to the word
        if i == len(word) - 1 or len(word) == 1:
            node.value = value
            if firstLook == True:
                with open("myfile.txt", "a") as f:
                            code = np.binary_repr(self.value, width=bitSize)
                            code = code.zfill(bitSize)
                            ascii_value = ord(node.label)
                            binary_string = bin(ascii_value)[2:]  # Convert to binary string, removing the '0b' prefix
                            binary_string = binary_string.zfill(8) 
                            f.write(str(code)+binary_string)
        else:
            node.insert(word, i + 1,value,firstLook,bitSize)
