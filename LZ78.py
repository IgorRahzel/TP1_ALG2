from TrieTree import Node
from math import log2,ceil

def lz78_compression(string,firstLook = False,bitsSize = None):

    with open("myfile.txt", "w") as f:
        f.write('')
    f.close()

    if firstLook == True:
        with open('myfile.txt','w') as f:
            f.write(f'{bitsSize} 7\n')

    # create a new TrieTree object
    root = Node(value=0)
    #auxiliary variable to determine if the number of character is > 0
    counter = 0 
    num_nodes = 0

    n = len(string)
    i = 0

    while i < n:
        counter = 0
        aux = root.insert(string[i],value = num_nodes + 1, firstLook = firstLook,bitSize = bitsSize)
        #character wasn't a child of the root node
        if aux == None:
            num_nodes += 1
            i+=1
        #character was a child of the root node
        else:
            while aux != None:
                if i < len(string) -1 :
                    new_letter = string[i+1] 
                else:
                    new_letter = '\0'
                #current charater and next
                if counter == 0:
                    word = aux + new_letter
                #multiple characters
                else:
                    word += new_letter
                aux = root.insert(word,value = num_nodes + 1,firstLook = firstLook, bitSize = bitsSize)
                counter += 1
                i+=1
            i += 1
            num_nodes += 1
    
    if firstLook == False:
        return num_nodes

def lz78_decompression(file):
    #create dictiory containg them empty string
    dictionary = {0:[None,'']}

    index = ''
    seq = ''
    counter = 0

    with open(file,'r') as f:
        for char in f.read():
            if char.isdigit():
                index += char
            else:
                counter += 1
                index = int(index)
                dictionary[counter] = [index,char]

                i = index

                #create sequence of characters
                while i != 0:
                    list = dictionary.get(i)
                    seq = list[1] + seq
                    i = list[0]
                #add the current text character to the sequence
                seq += char
                #write sequence in the file
                with open('output_file.txt','a') as f2:
                    f2.write(seq)
                    f2.close()
                index = ''
                seq = ''

#PARTE DA COMPRESSÃO
string = 'sir sid eastman easily teases sea sick seals'
num_nodes = lz78_compression(string)
num_nodes_log_2 = log2(num_nodes)
num_nodes_log_2 = ceil(num_nodes_log_2)
print(num_nodes_log_2)
lz78_compression(string,firstLook=True,bitsSize = num_nodes_log_2)

#PARTE DA DESCOMPRESSÃO
lz78_decompression('myfile.txt')
