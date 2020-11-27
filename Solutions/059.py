"""
Problem:

Implement a file syncing algorithm for two computers over a low-bandwidth network.
What if we know the files in the two computers are mostly the same?
"""

from __future__ import annotations
from hashlib import sha256

hash_func = sha256


class MerkleNode:
    def __init__(self, name: str) -> None:
        self.parent = None
        self.node_hash = None
        self.name = name

    def __hash__(self) -> int:
        return hash(self.name)

    def __eq__(self, other: MerkleNode) -> bool:
        if type(other) != MerkleNode:
            return False
        return self.node_hash == other.node_hash


class MerkleDirectory(MerkleNode):
    def __init__(self, name: str) -> None:
        MerkleNode.__init__(self, name)
        self.children = set()
        self.is_dir = True
        # creating a file on directory initialize and calculating hash
        new_file = MerkleFile("dir_init")
        new_file.add_to_directory(self)

    def __repr__(self) -> str:
        return f"Name: {self.name}, Children: {self.children}, Hash: {self.node_hash}"

    def add_to_directory(self, directory: MerkleDirectory) -> None:
        # adding the node
        self.parent = directory
        directory.children.add(self)
        # recalculating hash for all anscestors
        while directory is not None:
            directory.recalculate_hash()
            directory = directory.parent

    def recalculate_hash(self) -> None:
        # concatinating all hashes and recalculating on the cumulative hash
        cumulative_hash = ""
        for child in self.children:
            cumulative_hash += child.node_hash
        self.node_hash = hash_func(cumulative_hash.encode()).hexdigest()

    def synchronize(self, other: MerkleDirectory) -> None:
        # if the directories have the same hash, they are already synchronized
        if self.node_hash == other.node_hash:
            return
        # updating other using self
        for node in self.children:
            if not node in other.children:
                type(node)(node.add_to_directory(other))
        # updating self using other
        for node in other.children:
            if not node in self.children:
                type(node)(node.add_to_directory(self))


class MerkleFile(MerkleNode):
    def __init__(self, name: str) -> None:
        MerkleNode.__init__(self, name)
        self.node_contents = ""
        self.is_dir = False
        self.node_hash = hash_func(self.node_contents.encode()).hexdigest()

    def __repr__(self) -> str:
        return (
            f"[ Name: {self.name}, Content: "
            + f"{self.node_contents if self.node_contents else 'null'}, "
            + f"Hash: {self.node_hash} ]"
        )

    def add_to_directory(self, directory: MerkleDirectory) -> None:
        # adding the node
        self.parent = directory
        directory.children.add(self)
        # recalculating hash for all anscestors
        while directory is not None:
            directory.recalculate_hash()
            directory = directory.parent

    def update_contents(self, new_contents: str) -> None:
        # contents updated and hash recaculated
        self.node_hash = hash_func(new_contents.encode()).hexdigest()
        self.node_contents = new_contents
        if self.parent:
            self.parent.recalculate_hash()


class Computer:
    def __init__(self):
        self.root = MerkleDirectory("root")

    def __repr__(self) -> str:
        return str(self.root)

    def synchronize(self, new_comp: Computer) -> None:
        print("Syncing computers...")
        self.root.synchronize(new_comp.root)
        print("Sync successful!\n")


if __name__ == "__main__":
    c1 = Computer()
    c2 = Computer()

    print("COMPUTER 1:")
    print(c1)
    print("COMPUTER 2:")
    print(c2)
    print()

    new_file = MerkleFile("check_file")
    new_file.update_contents("Check")
    new_file.add_to_directory(c1.root)

    new_dir = MerkleDirectory("check_dir")
    new_dir.add_to_directory(c2.root)

    print("COMPUTER 1:")
    print(c1)
    print("COMPUTER 2:")
    print(c2)
    print()

    c1.synchronize(c2)

    print("COMPUTER 1:")
    print(c1)
    print("COMPUTER 2:")
    print(c2)
    print()
