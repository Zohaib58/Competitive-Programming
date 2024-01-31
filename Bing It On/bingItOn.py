from sys import stdin

lines = stdin.read().splitlines()


class TrieNode:
     
    # Trie node class
    def __init__(self):
        self.children = [None]*26
 
        # Count is True if node represent the end of the word
        self.Count = 0


class Trie:
     
    # Trie data structure class
    def __init__(self):
        self.root = self.getNode()
 
    def getNode(self):
     
        # Returns new trie node (initialized to NULLs)
        return TrieNode()
 
    def _charToIndex(self,ch):
         
        # private helper function
        # Converts key current character into index
        # use only 'a' through 'z' and lower case
         
        return ord(ch)-ord('a')
 
 
    def insert(self,key):
         
        # If not present, inserts key into trie
        # If the key is prefix of trie node, 
        # just marks leaf node
        pCrawl = self.root
        length = len(key)
        for level in range(length):
            index = self._charToIndex(key[level])
 
            # if current character is not present
            if not pCrawl.children[index]:
                pCrawl.children[index] = self.getNode()
            pCrawl = pCrawl.children[index]
 
        # mark last node as leaf
        pCrawl.Count += 1
 
    def search(self, key):
         
        # Search key in the trie
        # Returns true if key presents 
        # in trie, else false
        pCrawl = self.root
        length = len(key)
        for level in range(length):
            index = self._charToIndex(key[level])
            if not pCrawl.children[index]:
                return None
            pCrawl = pCrawl.children[index]
 
        return pCrawl

l = len(lines)

t = Trie()
result = [0] * (l - 1)



def dfs(pCrawl):

    count = 0
    if pCrawl.Count > 0:
        count += pCrawl.Count
    for i in range(0, 25):

        if pCrawl.children[i] != None:
            count += dfs(pCrawl.children[i])

    return count

i = 0
for ln in lines[1:]:
    
    key = ln
    res = t.search(key)

    

    if res != None:
        count = 0
        count = dfs(res)
        result[i] = count

    t.insert(key)
    i+=1

for res in result:
    print(res)