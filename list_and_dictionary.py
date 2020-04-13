import timeit

class Dictionary:
    def __init__(self):
        # Hashtable is a list of chained lists, where the size is a prime number.
        self.hashTable = [[] for x in range(997)]
    
    def add(self, key, value):
        '''
        Add a new key/value pair. Does not add if the key already exists.
        '''
        
        if self.contains(key):
            return False
        else:
            hashTableIndex = self.computeHash(key)
            self.hashTable[hashTableIndex].append((key, value))
            return True
        
    def addOrUpdate(self, key, value):
        '''
        If key exists update it, add otherwise.
        '''
        
        isFound, hashTableIndex, chainIndex = self._locate(key)
        
        if isFound:
            self.hashTable[hashTableIndex][chainIndex] = (key, value)
        else:
            self.add(key, value)
        
    def get(self, key):
        '''
        Get an element by key.
        '''
        
        isFound, hashTableIndex, chainIndex = self._locate(key)
        if not isFound:
            raise Exception('Not Found')
        else:
            kv = self.hashTable[hashTableIndex][chainIndex]
            return kv[1]
            
    def remove(self, key):
        '''
        Remove an element by key.
        '''
        
        isFound, hashTableIndex, chainIndex = self._locate(key)
        if not isFound:
            return False
        else:
            del self.hashTable[hashTableIndex][chainIndex]
            return True
    
    def contains(self, key):
        '''
        Check whether the given key exists.
        '''
        
        isFound, hashTableIndex, chainIndex = self._locate(key)
        return isFound
    
    def _locate(self, key):
        hashNumber = self.computeHash(key)
        
        # Find the chain at the index found by hash computation.
        indexChain = self.hashTable[hashNumber]
        
        # Serach for the given key in the chain.
        for i in range(len(indexChain)):
            if indexChain[i][0] == key:
                return True, hashNumber, i 
        return False, None, None
    
    def computeHash(self, key):
        '''
        Compute the hash of a string, with positional weightage to handle anagrams.
        '''
        
        keyString = str(key)
        hashNumber = 0
        for i in range(len(keyString)):
            hashNumber +=  (i+1) * ord(keyString[i])
            
        return hashNumber % len(self.hashTable)


'''
Testing the performance of a List vs the above implementation of dictionary.
'''

dictionary = Dictionary()
aList = []

for i in range(1000):
    dictionary.add(i, i)
    aList.append(i)

dictContains = timeit.Timer("dictionary.contains(678)", "from __main__ import dictionary")
print(f"Dictionary Contains:  {dictContains.timeit(number = 10000)}")

listContains = timeit.Timer("678 in aList", "from __main__ import aList")
print(f"List Contains:  {listContains.timeit(number = 10000)}")