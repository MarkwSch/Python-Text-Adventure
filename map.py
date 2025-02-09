class Map:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.grid = [['   ' for _ in range(width)] for _ in range(height)]

    # Method to add locations to the grid.
    def add_location(self, x, y, location_name):
        self.grid[y][x] = location_name

    # Method to display the map.
    def display_map(self):
        print("Key:\n? - Undiscovered Location\n△ - Current Location\nX - Discovered Location\nN/S - North or "
              "South\nW/E - West or East\n") # Provides a key to the player.
        for row in self.grid:
            print(row)

    # Updates the visited locations.
    def update_visited(self, current_location):
        if current_location.name == 'Entrance Hall':
            self.add_location(2, 8, " X ")  # Entrance Hall
        elif current_location.name == 'Corridor of Whispers':
            self.add_location(2, 6, " X ")  # Corridor of Whispers
        elif current_location.name == "Library of Lost Knowledge":
            self.add_location(4, 6, " X ")  # L o L K
        elif current_location.name == "Goblin's Lair":
            self.add_location(0, 6, " X ")  # G Lair
        elif current_location.name == "Chasm of Despair":
            self.add_location(2, 4, " X ")  # Chasm of Despair
        elif current_location.name == "Horn Chamber":
            self.add_location(4, 4, " X ")  # Horn Chamber
        elif current_location.name == "Cursed Crossroads":
            self.add_location(0, 4, " X ")  # Cursed Crossroads
        elif current_location.name == "Hidden Alcove":
            self.add_location(0, 2, " X ")  # Secret Alcove
        elif current_location.name == "Guardian's Chamber":
            self.add_location(2, 2, " X ")  # Guardian's Chamber
        elif current_location.name == "The Lost Room":
            self.add_location(4, 2, " X ")  # The Lost Room

    # Updates the current location.
    def update_current_location(self, current_location):
        if current_location.name == 'Entrance Hall':
            self.add_location(2, 8, " △ ")  # Entrance Hall
        elif current_location.name == 'Corridor of Whispers':
            self.add_location(2, 6, " △ ")  # Corridor of Whispers
        elif current_location.name == "Library of Lost Knowledge":
            self.add_location(4, 6, " △ ")  # L o L K
        elif current_location.name == "Goblin's Lair":
            self.add_location(0, 6, " △ ")  # G Lair
        elif current_location.name == "Chasm of Despair":
            self.add_location(2, 4, " △ ")  # Chasm of Despair
        elif current_location.name == "Horn Chamber":
            self.add_location(4, 4, " △ ")  # Horn Chamber
        elif current_location.name == "Cursed Crossroads":
            self.add_location(0, 4, " △ ")  # Cursed Crossroads
        elif current_location.name == "Hidden Alcove":
            self.add_location(0, 2, " △ ")  # Secret Alcove
        elif current_location.name == "Guardian's Chamber":
            self.add_location(2, 2, " △ ")  # Guardian's Chamber
        elif current_location.name == "The Lost Room":
            self.add_location(4, 2, " △ ")  # The Lost Room
