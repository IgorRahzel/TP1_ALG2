from TrieTree import Node
from math import log2,ceil

def lz78_compression(text,firstLook = False,bitsSize = None):

    with open("myfile.txt", "w") as f:
        f.write('')
    f.close()

    if firstLook == True:
        with open('myfile.txt','w') as f:
            f.write(f'{bitsSize} 8\n')

    # create a new TrieTree object
    root = Node(value=0)
    #auxiliary variable to determine if the number of character is > 0
    counter = 0 
    num_nodes = 0

    with open(text,'r') as file:
        for line in file:
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

    with open(file,'r') as f:
        #read first line of the file
        firstLine = f.readline()
        tokens = firstLine.split()

        #capture the number of bits used in the codification
        num_size = int(tokens[0])
        char_size = int(tokens[1])

        iterations = 0 

        for char in f.read():
            iterations +=1
            if iterations <= num_size + char_size:
                if iterations <= num_size:
                    index += char

                else:
                    character += char
                    
            if iterations == num_size + char_size:
                #converting binary code of index to int
                index = int(index, 2)
                #converting binary code of the character into char
                decimal_number = int(character, 2)
                character = chr(decimal_number)

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
                
                iterations = 0

#PARTE DA COMPRESSÃO
text = 'dom_casmurro.txt'
num_nodes = lz78_compression(text)
num_nodes_log_2 = log2(num_nodes)
num_nodes_log_2 = ceil(num_nodes_log_2)
print(num_nodes_log_2)
lz78_compression(text,firstLook=True,bitsSize = num_nodes_log_2)

#PARTE DA DESCOMPRESSÃO
lz78_decompression('myfile.txt')