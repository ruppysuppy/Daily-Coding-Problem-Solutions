"""
Problem:

Implement the singleton pattern with a twist. First, instead of storing one instance, store two instances. 
And in every even call of getInstance(), return the first instance and in every odd call of getInstance(), return the second instance.
"""

# class to handle the operations
class Twisted_Singleton:
    # instances store the two Twisted_Singleton instances
    # is odd stores the whether the last call was odd
    # flag stores if the data can be initialized
    instances = []
    is_odd = False
    flag = True

    # default initialize function
    def __init__(self, instance_num):
        self.instance_num = instance_num

    # initialize function to create all necessary data
    @staticmethod
    def initialize():
        # only if the flag is set, will the data be initialized (used to ensure it cannot be reinitialized)
        if Twisted_Singleton.flag:
            Twisted_Singleton.instances.append(Twisted_Singleton(1))
            Twisted_Singleton.instances.append(Twisted_Singleton(2))
            Twisted_Singleton.flag = False

    # FUNCTION TO PERFORM THE OPERATION
    @staticmethod
    def getInstance():
        # getting the current is odd
        Twisted_Singleton.is_odd = not Twisted_Singleton.is_odd

        # returning the necessary data
        if Twisted_Singleton.is_odd:
            return Twisted_Singleton.instances[0].instance_num

        return Twisted_Singleton.instances[1].instance_num


# DRIVER CODE
Twisted_Singleton.initialize()

print(Twisted_Singleton.getInstance())
print(Twisted_Singleton.getInstance())
print(Twisted_Singleton.getInstance())
print(Twisted_Singleton.getInstance())
print(Twisted_Singleton.getInstance())
print(Twisted_Singleton.getInstance())
