'''
Problem:

Implement a file syncing algorithm for two computers over a low-bandwidth network. 
What if we know the files in the two computers are mostly the same?
'''

# library import
from hashlib import sha256

# using the hash function sha256 (other hash functions can be used too)
hash_func = sha256

# Merkle Node class (Parent for file and directory)
class MerkleNode:
    # initialize function
    def __init__(self):
        self.parent = None
        self.node_hash = None
    
    # add to directory function (used for both file and directory to add them as a sub-file/sub-directory)
    def add_to_directory(self, dir_node):
        # adding the node
        self.parent = dir_node
        dir_node.children.add(self)
        dir_node.children_name.add(self.name)

        # recalculating hash
        while dir_node:
            dir_node.recalculate_hash()
            dir_node = dir_node.parent

# Merkle Directory class
class MerkleDirectory(MerkleNode):
    # initialize function
    def __init__(self, name):
        MerkleNode.__init__(self)
        self.children = set()
        self.children_name = set()
        self.is_dir = True
        self.name = name
        # creating a file on directory initialize and recalculating hash
        new_file = MerkleFile('dir_init')
        new_file.add_to_directory(self)

    # display functions (str and repr)
    def __str__(self):
        return f'Name: {self.name}\nChildren: {self.children}'
    
    def __repr__(self):
        return "\n" + self.__str__()

    # function to recalculate hash for the current directory
    def recalculate_hash(self):
        # concatinating all hashes and recalculating on the cumulative hash
        if self.children:
            cumulative_hash = ""
            for child in self.children:
                cumulative_hash += child.node_hash
            self.node_hash = hash_func(cumulative_hash.encode()).hexdigest()
        else:
            self.node_hash = hash_func(''.encode()).hexdigest()
    
    # function to synchronize 2 directories
    def sync(self, other):
        # if the directories have the same hash, they are already synchronized
        if (self.node_hash == other.node_hash):
            return
        
        # copying from self to other
        for node in self.children:
            if (not node in other.children):
                (type(node))(other.children.add(node))
        
        # copying from other to self
        for node in other.children:
            if (not node in self.children):
                (type(node))(self.children.add(node))
        # NOTE: Type-casting is used to get a deep copy instead of a shallow one

# Merkle File class
class MerkleFile(MerkleNode):
    # initialize function
    def __init__(self, name):
        MerkleNode.__init__(self)
        self.node_contents = ''
        self.is_dir = False
        self.name = name
        self.node_hash = hash_func(self.node_contents.encode()).hexdigest()
    
    # display functions (repr)
    def __repr__(self):
        return f'\nName: {self.name}\nContent: {self.node_contents}'

    # function to update the contents of the file
    def update_contents(self, new_contents):
        # contents updated and hash recaculated of all the anscestors of the current file
        self.node_hash = hash_func(new_contents.encode()).hexdigest()
        self.node_contents = new_contents
        if self.parent:
            self.parent.recalculate_hash()

# Computer class
class Computer():
    # initialize function
    def __init__(self):
        self.root = MerkleDirectory('root')
    
    # synchronize function
    def sync(self, new_comp):
        if (type(new_comp) == Computer):
            print("Syncing computers...")
            self.root.sync(new_comp.root)
            print("Sync successful!\n")

# DRIVER CODE
c1 = Computer()
c2 = Computer()

print("COMPUTER 1:")
print(c1.root)
print("COMPUTER 2:")
print(c2.root)
print()

new_file = MerkleFile('check_file')
new_file.update_contents('Check')
new_file.add_to_directory(c1.root)

new_dir = MerkleDirectory('check_dir')
new_dir.add_to_directory(c2.root)

print("COMPUTER 1:")
print(c1.root)
print("COMPUTER 2:")
print(c2.root)
print()

c1.sync(c2)

print("COMPUTER 1:")
print(c1.root)
print("COMPUTER 2:")
print(c2.root)
print()

new_file = MerkleFile('check_file2')
new_file.update_contents('Check Again')
new_file.add_to_directory(c1.root)

print("COMPUTER 1:")
print(c1.root)
print("COMPUTER 2:")
print(c2.root)