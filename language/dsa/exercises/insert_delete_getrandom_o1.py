import random

class RandomizedSet:

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
    
if __name__ == "__main__":
    solution = RandomizedSet()