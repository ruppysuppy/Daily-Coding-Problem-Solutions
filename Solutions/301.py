"""
Problem:

Implement a data structure which carries out the following operations without resizing
the underlying array:
* add(value): Add a value to the set of values.
* check(value): Check whether a value is in the set.

The check method may return occasional false positives (in other words, incorrectly
identifying an element as part of the set), but should always correctly identify a true
element.
"""

# this is an improvised version of the method available at:
# https://www.geeksforgeeks.org/bloom-filters-introduction-and-python-implementation/

from bitarray import bitarray
from math import log
from random import shuffle


class BloomFilter:

    """ 
    Class for Bloom filter, using murmur3 hash function 
    """

    def __init__(self, items_count: int, fp_prob: float) -> None:
        """ 
        items_count : int 
            Number of items expected to be stored in bloom filter 
        fp_prob : float 
            False Positive probability in decimal 
        """
        # False posible probability in decimal
        self.fp_prob = fp_prob

        # Size of bit array to use
        self.size = BloomFilter.get_size(items_count, fp_prob)

        # number of hash functions to use
        self.hash_count = BloomFilter.get_hash_count(self.size, items_count)

        # Bit array of given size
        self.bit_array = bitarray(self.size)

        # initialize all bits as 0
        self.bit_array.setall(0)

    def add(self, item: str) -> None:
        """ 
        Add an item in the filter 
        """
        digests = []
        for _ in range(self.hash_count):

            # create digest for given item.
            # i work as seed to mmh3.hash() function
            # With different seed, digest created is different
            digest = hash(item) % self.size
            digests.append(digest)

            # set the bit True in bit_array
            self.bit_array[digest] = True

    def check(self, item: str) -> bool:
        """ 
        Check for existence of an item in filter 
        """
        for _ in range(self.hash_count):
            digest = hash(item) % self.size
            if self.bit_array[digest] == False:

                # if any of bit is False then,its not present
                # in filter
                # else there is probability that it exist
                return False
        return True

    @staticmethod
    def get_size(n: int, p: float) -> int:
        """ 
        Return the size of bit array(m) to used using 
        following formula 
        m = -(n * lg(p)) / (lg(2)^2) 
        n : int 
            number of items expected to be stored in filter 
        p : float 
            False Positive probability in decimal 
        """
        m = -(n * log(p)) / (log(2) ** 2)
        return int(m)

    @staticmethod
    def get_hash_count(m: int, n: int) -> int:
        """ 
        Return the hash function(k) to be used using 
        following formula 
        k = (m/n) * lg(2) 
  
        m : int 
            size of bit array 
        n : int 
            number of items expected to be stored in filter 
        """
        k = (m / n) * log(2)
        return int(k)


if __name__ == "__main__":
    n = 20  # no of items to add
    p = 0.05  # false positive probability

    bloomf = BloomFilter(n, p)
    print("Size of bit array:{}".format(bloomf.size))
    print("False positive Probability:{}".format(bloomf.fp_prob))
    print("Number of hash functions:{}\n".format(bloomf.hash_count))

    # words to be added
    word_present = [
        "abound",
        "abounds",
        "abundance",
        "abundant",
        "accessable",
        "bloom",
        "blossom",
        "bolster",
        "bonny",
        "bonus",
        "bonuses",
        "coherent",
        "cohesive",
        "colorful",
        "comely",
        "comfort",
        "gems",
        "generosity",
        "generous",
        "generously",
        "genial",
    ]

    # word not added
    word_absent = [
        "bluff",
        "cheater",
        "hate",
        "war",
        "humanity",
        "racism",
        "hurt",
        "nuke",
        "gloomy",
        "facebook",
        "geeksforgeeks",
        "twitter",
    ]

    for item in word_present:
        bloomf.add(item)

    shuffle(word_present)
    shuffle(word_absent)

    test_words = word_present[:10] + word_absent
    shuffle(test_words)
    for word in test_words:
        if bloomf.check(word):
            if word in word_absent:
                print("'{}' is a false positive!".format(word))
            else:
                print("'{}' is probably present!".format(word))
        else:
            print("'{}' is definitely not present!".format(word))
