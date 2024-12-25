import random


class RandomizedSet:
    def __init__(self):
        self.values = []  # List to store elements
        self.index_map = {}  # Hash map to store value -> index mapping

    def insert(self, val: int) -> bool:
        if val in self.index_map:
            return False
        self.index_map[val] = len(self.values)
        self.values.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.index_map:
            return False
        # Get the index of the element to remove
        idx_to_remove = self.index_map[val]
        # Swap the element with the last one in the list
        last_element = self.values[-1]
        self.values[idx_to_remove] = last_element
        self.index_map[last_element] = idx_to_remove
        # Remove the last element
        self.values.pop()
        del self.index_map[val]
        return True

    def getRandom(self) -> int:
        return random.choice(self.values)


if __name__ == "__main__":
    obj = RandomizedSet()
    print(obj.insert(1))  # True
    print(obj.remove(2))  # False
    print(obj.insert(2))  # True
    print(obj.getRandom())
    print(obj.remove(1))  # True
    print(obj.insert(2))  # False
    print(obj.getRandom())
