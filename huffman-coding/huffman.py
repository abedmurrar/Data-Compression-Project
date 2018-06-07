from queue import *
import binascii

class TreeNode:
    def __init__(self, symbol=None, left=None, right=None):
        self.symbol = symbol
        self.left = left
        self.right = right

    def setLeft(self, left):
        self.left = left

    def setRight(self, right):
        self.right = right

    def setSymbol(self, symbol):
        self.symbol = symbol

    def getLeft(self):
        return self.left

    def getRight(self):
        return self.right

    def getSymbol(self):
        return self.symbol


class HuffmanTree:
    def __init__(self, rootNode=None):
        self.root = rootNode

    def setRootNode(self, rootNode):
        self.root = rootNode

    def getRootNode(self):
        return self.root


class LinkedListNode:
    def __init__(self, symbol=None, code=None, next=None):
        self.symbol = symbol
        self.code = code
        self.next = next

    def setCode(self, code):
        self.code = code

    def setNext(self, next):
        self.next = next

    def setSymbol(self, symbol):
        self.symbol = symbol

    def getCode(self):
        string = ''
        for binary in self.code:
            if binary is 'z':
                break
            if binary is '1' or binary is '0':
                string += binary
        return string

    def getNext(self):
        return self.next

    def getSymbol(self):
        return self.symbol


class HuffmanTable:
    def __init__(self, first=None, last=None):
        self.first = first
        self.last = last

    def setFirst(self, first):
        self.first = first

    def setLast(self, last):
        self.last = last

    def getFirst(self):
        return self.first

    def getLast(self):
        return self.last


def traverseTree(treeNode, table, k, code):
    if treeNode.getLeft() is None and treeNode.getRight() is None:
        code[k] = 'z'
        aux = LinkedListNode()
        aux.setCode(list(code))
        aux.setSymbol(treeNode.getSymbol())
        aux.setNext(None)
        if table.getFirst() is None:
            table.setFirst(aux)
            table.setLast(aux)
        else:
            table.getLast().setNext(aux)
            table.setLast(aux)

    if treeNode.getLeft() is not None:
        code.insert(k, '0')
        traverseTree(treeNode.getLeft(), table, k + 1, code)

    if treeNode.getRight() is not None:
        code.insert(k, '1')
        traverseTree(treeNode.getRight(), table, k + 1, code)


def buildTable(huffmanTree):
    table = HuffmanTable()
    code = [None] * 256
    k = 0
    traverseTree(huffmanTree.getRootNode(), table, k, code)
    return table


def buildTree(inputString):
    probability = [0] * 256
    for char in inputString:
        if char is not 'z':
            probability[ord(char)] += 1
        else:
            break
    huffmanQueue = PriorityQueue()
    # initPQueue(huffmanQueue)

    for i in range(0, 256):
        if probability[i] is not 0:
            aux = TreeNode()
            aux.setSymbol(chr(i))
            addPQueue(huffmanQueue, aux, probability[i])

    del probability[:]
    del probability

    # 	//We free the array because we don't need it anymore
    # 	free(probability);

    while (huffmanQueue.getSize() is not 1):
        priority = huffmanQueue.getFirst().getPriority()
        priority += huffmanQueue.getFirst().getNext().getPriority()

        left = getPQueue(huffmanQueue)
        right = getPQueue(huffmanQueue)

        newNode = TreeNode()
        newNode.setLeft(left)
        newNode.setRight(right)
        addPQueue(huffmanQueue, newNode, priority)

    tree = HuffmanTree()
    tree.setRootNode(getPQueue(huffmanQueue))
    return tree


def encode(table, stringToEncode):
    print(stringToEncode)
    traversal = LinkedListNode()
    encoded = ''
    print("\nEncoding\nInput String: " + stringToEncode)
    for char in stringToEncode:
        traversal = table.getFirst()
        while (traversal.getSymbol() is not char):
            traversal = traversal.getNext()
        encoded += traversal.getCode()
    encoded = encoded +traversal.getCode()
    print("Encoded : "+encoded)
    #print(' '.join(map(bin,bytearray(stringToEncode))))
    # print(bin(int(binascii.hexlify(stringToEncode),16)))
    print(''.join(format(ord(x),'b') for x in stringToEncode))

def decode(tree, stringToDecode):
    traversal = tree.getRootNode()
    print("\nDecoding\nInput string : " + stringToDecode)


# void decode(htTree *tree, char *stringToDecode)
# {

# 	//For each "bit" of the string to decode
# 	//we take a step to the left for 0
# 	//or ont to the right for 1
# 	for(int i=0; stringToDecode[i]!='z'; i++)
# 	{
# 		if(traversal->left == NULL && traversal->right == NULL)
# 		{
# 			printf("%c",traversal->symbol);
# 			traversal = tree->root;
# 		}

# 		if(stringToDecode[i] == '0')
# 			traversal = traversal->left;

# 		if(stringToDecode[i] == '1')
# 			traversal = traversal->right;

# 		if(stringToDecode[i]!='0'&&stringToDecode[i]!='1')
# 		{
# 			printf("The input string is not coded correctly!\n");
# 			return;
# 		}
# 	}
# 	if(traversal->left == NULL && traversal->right == NULL)
# 	{
# 		printf("%c",traversal->symbol);
# 		traversal = tree->root;
# 	}

# 	printf("\n");
# }
