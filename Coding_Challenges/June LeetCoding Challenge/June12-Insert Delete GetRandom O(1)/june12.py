class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.present = {}
        self.elements = []


    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if val not in self.present or self.present[val] == 0:
            self.elements.append(val)
            self.present[val] = 1
            return  True

        return False


    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if val not in self.present or self.present[val] == 0:
            return False
        self.present[val] = 0
        index = self.elements.index(val)
        if index!=len(self.elements)-1:
            temp = self.elements[-1]
            self.elements[-1] = val
            self.elements[index]=temp
        self.elements.pop()
        return True


    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        return random.choice(self.elements)



# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
