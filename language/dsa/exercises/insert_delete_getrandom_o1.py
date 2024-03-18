import random

class RandomizedSet2:

    def __init__(self):
        self.set = []
        

    def insert(self, val: int) -> bool:
        if self.set.__contains__(val):
            return False
        
        self.set.append(val)
        return True
        

    def remove(self, val: int) -> bool:
        if not self.set.__contains__(val):
            return False
        
        self.set.remove(val)
        return True
        

    def getRandom(self) -> int:
        return random.choice(self.set)
    
class RandomizedSet:

    def __init__(self):
        self.set = set()
        self.val_to_index = {}
        self.val_to_list = []
        

    def insert(self, val: int) -> bool:
        if val in self.set:
            return False
        
        self.set.add(val)
        self.val_to_list.append(val)
        self.val_to_index[val] = len(self.val_to_list) - 1
        return True
        

    def remove(self, val: int) -> bool:
        if val not in self.set:
            return False
        
        idx = self.val_to_index[val]
        last_val = self.val_to_list[-1]
        self.val_to_list[idx] = last_val
        self.val_to_index[last_val] = idx
        self.val_to_list.pop()
        del self.val_to_index[val]
        self.set.remove(val)
        return True
        

    def getRandom(self) -> int:
        return random.choice(self.val_to_list)
    
if __name__ == "__main__":
    solution = RandomizedSet()