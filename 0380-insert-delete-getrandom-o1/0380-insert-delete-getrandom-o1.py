import random
class RandomizedSet:

    def __init__(self):
        self.nums = []
        self.pos = {}

    def insert(self, val: int) -> bool:
        if val in self.pos:
            return False
        else:
            self.nums.append(val)
            self.pos[val] = len(self.nums) - 1
            return True

    def remove(self, val: int) -> bool:
        if val not in self.pos:
            return False
        else:
            last_value = self.nums[-1]
            idx = self.pos[val]
            self.nums[idx] = last_value
            self.pos[last_value] = idx
            self.nums.pop()
            del self.pos[val]
            return True

    def getRandom(self) -> int:
        return random.choice(self.nums)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()