from TrieTree import Node
from math import log2,ceil

def lz78_compression(text,firstLook = False,bitsSize = None):

    with open("myfile.txt", "w") as f:
        f.write('')
    f.close()

    if firstLook == True:
        with open('myfile.txt','wb') as f:
            bit_size_bytes = bitsSize.to_bytes(1, byteorder='big',signed=False)
            # Write the bit_size of integers in binary
            f.write(bit_size_bytes)


    # create a new TrieTree object
    root = Node(value=0)
    # Auxiliary variable to determine if the number of character is > 0
    counter = 0 
    num_nodes = 0

    with open(text,'r') as file:
        input = file.read()
        n = len(input)
        i = 0
        while i < n:
            endOfLine = False
            counter = 0
            aux = root.insert(input[i],value = num_nodes + 1, firstLook = firstLook,bitSize = bitsSize)
            #character wasn't a child of the root node
            if aux == None:
                num_nodes += 1
                i+=1
            #character was a child of the root node
            else:
                while aux != None:
                    if i < len(input) -1 :
                        new_letter = input[i+1]
                    else:
                        new_letter = '\0'
                    if new_letter == '\x00':
                        endOfLine = True
                    #current charater and next
                    else:
                        if counter == 0:
                            word = aux + new_letter
                        #multiple characters
                        else:
                            word += new_letter
                    aux = root.insert(word,value = num_nodes + 1,firstLook = firstLook, bitSize = bitsSize,endOfLine=endOfLine)
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
    character = ''
    counter = 0

    with open(file,'rb') as f:
        # Read the first two bytes and interpret as an integer (big-endian)
        num_size = int.from_bytes(f.read(1), 'big')

        iterations = 0 

        while True:
            #Reading the index part of the codification
            index = int.from_bytes(f.read(num_size),'big')
            character = f.read(1)

            if index == b'' or character ==b'':
                break

            aux_decode = ord(character)
            aux_decode = bin(aux_decode)[2:].rjust(8,'0')

            if aux_decode[0:3] == '110':
                character += f.read(1)
            elif aux_decode[0:4] == '1110':
                character += f.read(2)
            elif aux_decode [0:5] == '11110':
                character += f.read(3)
            
            character = character.decode('utf-8')

            counter += 1
            dictionary[counter] = [index,character]

            i = index

            #create sequence of characters
            while i != 0:
                list = dictionary.get(i)
                seq = list[1] + seq
                i = list[0]
            #add the current text character to the sequence
            seq += character
            #write sequence in the file
            with open('output_file.txt','a') as f2:
                f2.write(seq)
                f2.close()
            index = ''
            seq = ''
            character = ''
            

#PARTE DA COMPRESSÃO
text = 'dom_casmurro.txt'
num_nodes = lz78_compression(text)
num_nodes_log_2 = log2(num_nodes)
num_nodes_log_2 = ceil(num_nodes_log_2)
bit_size_bytes = (num_nodes_log_2 + 7)//8
print(num_nodes_log_2)
lz78_compression(text,firstLook=True,bitsSize = bit_size_bytes)

#PARTE DA DESCOMPRESSÃO
lz78_decompression('myfile.txt')