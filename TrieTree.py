import numpy as np
class Node:
    def __init__(self,value=None, label='', children=None):
        self.value = value if value is not None else None
        self.children = children if children is not None else []
        self.label = label
        
    def insert(self,file,word, i=0, value=None, firstLook=False, bitSize=None):
        current_node = self

        while i < len(word):
            current_char = word[i]

            # Search for a child node with the same label as the current character
            child_node = None
            for child in current_node.children:
                if child.label == current_char:
                    child_node = child
                    break

            # If a child node exists, move to that node
            if child_node is not None:
                parent_value = current_node.value
                current_node = child_node
                i += 1

                if i == len(word):
                    return current_node.label
            else:
                break

        # Create new nodes for the remaining characters in the word
        while i < len(word):
            new_node = Node(label=word[i])
            current_node.children.append(new_node)
            parent_value = current_node.value
            current_node = new_node
            i += 1

        # Set the value of the last node to the word
        current_node.value = value

        # Write the binary representation to the file if firstLook is True
        if firstLook:
            with open(file, "ab") as f:
                # Convert parent_value to binary representation
                parent_value_bytes = parent_value.to_bytes(bitSize, byteorder='big',signed = False)
                # Convert current_node.label to binary representation
                label_byte = current_node.label.encode('utf-8','strict')

                f.write(parent_value_bytes + label_byte)