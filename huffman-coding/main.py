from queue import *
from huffman import *

codeTree = buildTree("beep boop beer!")

codeTable = buildTable(codeTree)

encode(codeTable, "beep boop beer!")
