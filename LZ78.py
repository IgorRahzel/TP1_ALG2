from TrieTree import Node

def lz78_compression(string):

    with open("myfile.txt", "w") as f:
        f.write('')
    f.close()

    # create a new TrieTree object
    root = Node(value=0)

    counter = 0
    num_nodes = 0

    n = len(string)
    i = 0
    while i < n:
        counter = 0
        aux = root.insert(string[i],value = num_nodes + 1)
        if aux == None:
            num_nodes += 1
            i+=1
        else:
            while aux != None:
                if i < len(string) -1 :
                    new_letter = string[i+1] 
                else:
                    new_letter = '\0'
                if counter == 0:
                    word = aux + new_letter
                else:
                    word += new_letter
                aux = root.insert(word,value = num_nodes + 1)
                counter += 1
                i+=1
            i += 1
            num_nodes += 1

def lz78_decompression(file):
    dictionary = {0:[0,'']}
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
                while i != 0:
                    list = dictionary.get(i)
                    seq = list[1] + seq
                    i = list[0]
                seq += char
                with open('output_file.txt','a') as f2:
                    f2.write(seq)
                    f2.close()
                index = ''
                seq = ''

#PARTE DA COMPRESSÃO
string = 'ABCDABCABCDAABCABCE'
lz78_compression(string)

#PARTE DA DESCOMPRESSÃO
lz78_decompression('myfile.txt')
