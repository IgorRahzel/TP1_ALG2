# LZ78 Compression Algorithm

## Introduction

This project involves the implementation of the LZ78 algorithm, developed by Lempel and Ziv in 1978, for compressing and decompressing text files. The goal of the algorithm is to replace repeated sequences of characters with codes representing them, thereby reducing the size of the text. For this project, a Trie tree has been used to store sequences of characters, as opposed to the simpler dictionary-based approach.

## Trie Tree

### How Trie Tree Works

Conceptually, a Trie is an M-ary tree where each node has M possible links for each symbol in the alphabet. The idea is to break the text into words and insert them into the Trie such that each node stores a single character. Thus, words in the same subtree share the same prefix.

### Implementation

The Trie tree was implemented in the file `TrieTree.py`. It has the following attributes:
- `value`: Represents the number associated with that node in the tree.
- `label`: Represents the character corresponding to that node.
- `children`: A list containing the children of that node.

Since the LZ78 algorithm only requires insertions into the Trie, only the `insert()` method was implemented. This method checks if a word has been inserted previously. If it has, the method returns `None`; otherwise, it returns the last character of the word. The insertion process involves traversing from the root and matching characters. If a match is found, the process continues; if not, new nodes are created for the remaining characters of the word.

## LZ78 Algorithm

### Compression

To compress a text file using the LZ78 algorithm, each character of the text is inserted into the Trie. If the current character is already in the Trie, a word is formed by concatenating the current character with the next character in the text. This word is then inserted into the Trie. The process is repeated until the word is inserted or the end of the text is reached. Each insertion results in a code `(index, symbol)`, where `index` is the value of the parent node of the node where the last symbol of the string was inserted, and `symbol` represents the last character of the word.

To achieve significant compression, these codes are converted to binary. The first pass over the file builds the Trie to determine the number of insertions. The maximum number of bits required for each `index` is calculated as $\lceil \log_2(N) \rceil$, where $N$ is the number of insertions. The `symbol` is converted to its UTF-8 bit representation. The first byte of the compressed file contains the number of bytes needed for the `index` representation, which is important for decompression.

### Decompression

During decompression, the first byte of the file is read to determine how many bytes are needed to read the `index`. The subsequent bytes are for the `symbol`'s UTF-8 representation. The process involves reading and decoding the bytes based on their leading bits. Depending on the leading bits, additional bytes may be read.

After decoding the codes, they are inserted into a dictionary, which is initialized with `[None, '']` for key `0`. The code is inserted into the dictionary with a list `[index, code]` where `pos` represents the position of the code in the compressed text. To reconstruct the text, a string is built where the rightmost symbol is the character read from the code, and the left symbol is from the dictionary entry corresponding to the `index`. This process continues until the dictionary entry with key `0` is reached, which indicates that all prefix characters have been read.

## Compression Ratio

The table below shows the compression ratio for 10 `.txt` files using the LZ78 algorithm implementation. The compression ratio is the ratio of the original file size to the compressed file size.

| File .txt            | Original Size | Compressed Size | Compression Ratio |
|----------------------|---------------|-----------------|-------------------|
| Hamlet               | 205.9 kB       | 117.5 kB        | 1.75              |
| Julius Caesar        | 137.1 kB       | 83.7 kB         | 1.63              |
| King Richard         | 197.1 kB       | 115.9 kB        | 1.70              |
| Macbeth              | 125.8 kB       | 79.3 kB         | 1.58              |
| Measure for Measure  | 217.4 kB       | 123.1 kB        | 1.76              |
| Much Ado About Nothing | 143.2 kB    | 86.3 kB         | 1.65              |
| Romeo and Juliet     | 163.6 kB       | 99.1 kB         | 1.65              |
| The Merchant of Venice | 141.9 kB    | 87.1 kB         | 1.62              |
| The Tragedy of King Lear | 176.8 kB  | 106.5 kB        | 1.75              |
| Twelfth Night         | 136.2 kB       | 83.3 kB         | 1.63              |

## Conclusion

This practical work focused on implementing the LZ78 algorithm using a Trie tree as an auxiliary data structure. It provided a better understanding of Trie trees and introduced compression algorithms, which had not been previously covered in the course. The LZ78 algorithm essentially provides a code for each Trie insertion, representing the largest existing prefix in the tree and the last character inserted.

## References

- Wikipedia. (2023, May 9). LZ78. In Wikipedia, The Free Encyclopedia. Retrieved May 9, 2023, from [https://pt.wikipedia.org/wiki/LZ78](https://pt.wikipedia.org/wiki/LZ78)
- Salomon, D. (2012). *Data Compression: The Complete Reference* (4th ed.). Springer.
