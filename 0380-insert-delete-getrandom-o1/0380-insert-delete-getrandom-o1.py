import random
class RandomizedSet:

    def __init__(self):
        self.set = set()

    def insert(self, val: int) -> bool:
        if val in self.set:
            return False
        else:
            self.set.add(val)
            return True

    def remove(self, val: int) -> bool:
        if val in self.set:
            self.set.remove(val)
            return True
        else:
            return False

    def getRandom(self) -> int:
        my_list = list(self.set)
        random_index = random.randint(0, len(my_list) - 1)
        random_element = my_list[random_index]
        return random_element
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()