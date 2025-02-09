import items
class BackPack:
    """
    BackPack Class
    ToDo: [X] Instantiate backpack
    ToDo: [X] Add Item
    ToDo: [X] Remove Item
    ToDo: [X] List Items
    ToDo: [X] Count items
    ToDo: [X] in backpack (Search for Item - Student to do)
    ToDo: [X] Sort Items
    """

    def __init__(self, items):
        self._backpack = []
        if items is None:
            items = []
        if type(items) != "<class 'list'>":
            items = []
        for item in items:
            self._backpack.append(item)
        self.sort()

    # Method to sort by name
    def sort(self):
        # Since I'm appending Objects to the list, I need to write this function to define the sort function by the name
        # of the Objects.
        self._backpack = sorted(self._backpack, key=lambda item: item.name)

    # Method to count the number of items in the backpack
    def count(self):
        return len(self._backpack)

    # Method to list the items in the backpack for the player
    def list(self):
        print("\n" + "=" * 40)
        print("Backpack:")
        for item in self._backpack:
            print(item.name)
        print("=" * 40)
        input("\nPress 'Enter' to continue.")
        pass

    # Method for adding an item to the backpack
    def add(self, item):
        if item is not None:
            self._backpack.append(item)
            self.sort()

    # Method for removing an item from the backpack
    def remove(self, item):
        if item is not None:
            self._backpack.remove(item)
            self.sort()

    # Binary searches through the backpack
    def in_backpack(self, item):
        low = 0
        high = len(self._backpack) - 1
        while low <= high:
            mid = (low + high) // 2
            current_item = self._backpack[mid]
            if current_item.name == item.name:
                return True  # Found the item, return its position
            elif current_item.name < item.name:
                low = mid + 1
            else:
                high = mid - 1
        return False
