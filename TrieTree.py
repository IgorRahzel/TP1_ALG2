class Node:
    def __init__(self,value=None, label='', children=None, root=None):
        self.value = value if value is not None else []
        self.children = children if children is not None else []
        self.label = label
        self.root = root

    def search(self, word, i=0):
        for child in self.children:
            if child.label == word[i]:
                if i == len(word) - 1:
                    if len(child.value) != 0:
                        return self
                else:
                    for child in self.children:
                        node = child.search(word, i + 1)
                        if node is not None:
                            return node
                return None

    def insert(self, word, i=0,value=None):
        # search for a child node with the same label as the current character
        for child in self.children:
            if child.label == word[i]:
                # if this is the last character of the word, set the value of the node to the word
                if i == len(word) - 1:
                    child.value.append(value)
                else:
                    child.insert(word, i + 1,value)
                return

        # if no child node with the same label exists, create a new one and add it to the children list
        node = Node(label=word[i], root=self.root)
        self.children.append(node)

        # if this is the last character of the word, set the value of the node to the word
        if i == len(word) - 1:
            node.value.append(value)
        else:
            node.insert(word, i + 1,value)