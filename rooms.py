import characters
import items
import os
import game_logic


class Location:
    """
    Location Class
    """
    def __init__(self, name, description, exits, character, item, visited, locked):
        self.name = name
        self.description = description
        self.exits = exits if exits is not None else {}
        self.character = character
        self.item = item
        # To determine whether the player has been there before.
        self.visited = visited
        self.locked = locked

    def __str__(self):
        return f"{self.name}: {self.description}\nExits: {', '.join(self.exits.keys())}"

    # On visit function
    def on_visit(self):
        os.system('cls')
        print("\n" + "=" * 40)
        print(self.name)
        print("-" * 40)
        print(self.description)
        print("\nAvailable Moves")
        print("-" * 40)
        if self.character is not None:
            print(f"Character: {self.character.name} ")
        if self.item is not None:
            print(f"Item: {self.item.name}")
        print("Move")
        print("Backpack")
        print("-" * 40)
        self.set_visited()  # Calls the set_visited method

    # Method to unlock doors
    def unlock_door(self):
        self.locked = False
        print(f"The door to the {self.name} is now unlocked.")

    # Method to remove items from the location
    def remove_item(self):
        self.item = None

    # Method to set the visited variable to True
    def set_visited(self):
        self.visited = True

class EntranceHall(Location):
    def __init__(self):
        super().__init__(
            name="Entrance Hall",
            description="A dimly lit room with a heavy wooden door behind the player. The air is musty, and the sound "
                        "of distant echoes fills the space.",
            exits={"North": "Corridor of Whispers"},
            character=characters.WhisperingSpirit(),
            item=items.MagicKeyofBeginnings(self),
            visited=False,
            locked=False
        )


class CorridorOfWhispers(Location):
    def __init__(self):
        super().__init__(
            name="Corridor of Whispers",
            description="A narrow corridor with eerie whispers echoing off the walls. Mysterious shadows dance as "
                        "torchlight flickers. There are 4 doors in this room; one North, one East, one South and one "
                        "West.",
            exits={"North": "Chasm of Despair", "West": "Goblin's Lair", "East": "Library of Lost Knowledge",
                   "South": "Entrance Hall"},
            character=None,
            item=None,
            visited=False,
            locked=False
        )


class GoblinLair(Location):
    def __init__(self, chasm_of_despair):
        super().__init__(
            name="Goblin's Lair",
            description="A cavernous chamber inhabited by a mischievous goblin. The air is filled with the smell of "
                        "damp earth.",
            exits={"East": "Corridor of Whispers"},
            character=characters.DeceivingGoblin(),
            item=items.Lever(chasm_of_despair),
            visited=False,
            locked=False
        )


class LibraryOfLostKnowledge(Location):
    def __init__(self):
        super().__init__(
            name="Library of Lost Knowledge",
            description="Rows of dusty tomes line the shelves. Strange symbols and ancient languages are engraved on "
                        "the books.",
            exits={"West": "Corridor of Whispers"},
            character=None,
            item=items.MagicKeyOfKnowledge(self),
            visited=False,
            locked=False
        )

class ChasmOfDespair(Location):
    def __init__(self):
        super().__init__(
            name="Chasm of Despair",
            description="A deep chasm with a narrow bridge. The sound of rushing water echoes from below, adding to "
                        "the tension.",
            exits={"North": "Guardian's Chamber", "East": "Horn Chamber", "West": "Cursed Crossroads",
                   "South": "Corridor of Whispers"},
            character=None,
            item=items.Chest(),
            visited=False,
            locked=True
        )


class HornChamber(Location):
    def __init__(self):
        super().__init__(
            name="Horn Chamber",
            description="A room with a horn.",
            exits={"West": "Chasm of Despair"},
            character=None,
            item=items.Horn(),
            visited=False,
            locked=False
        )


class CursedCrossroads(Location):
    def __init__(self, hidden_alcove):
        super().__init__(
            name="Cursed Crossroads",
            description="A junction of pathways with cryptic symbols on the walls. Strange markings seem to guide or "
                        "warn.",
            exits={"North": "Hidden Alcove", "East": "Chasm of Despair"},
            character=None,
            item=items.Button(hidden_alcove),
            visited=False,
            locked=False
        )


class HiddenAlcove(Location):
    def __init__(self):
        super().__init__(
            name="Hidden Alcove",
            description="A small alcove concealed by ivy. A mysterious aura surrounds the space.",
            exits={"East": "Guardian's Chamber", "South": "Cursed Crossroads"},
            character=None,
            item=items.MagicKeyOfSecrets(self), # Pick-up Item
            visited=False,
            locked=True
        )


class GuardiansChamber(Location):
    def __init__(self, horn_chamber, outside):
        super().__init__(
            name="Guardian's Chamber",
            description="A room guarded by a mystical entity. The air is charged with energy, and the guardian awaits.",
            exits={"North": "Outside", "East": "The Lost Room", "South": "Chasm of Despair", "West": "Hidden Alcove"},
            character=characters.TiredGuard(horn_chamber, outside),
            item=None,
            visited=False,
            locked=False
        )


class LostRoom(Location):
    def __init__(self):
        super().__init__(
            name="The Lost Room",
            description="A small forgotten about room.",
            exits={"West": "Guardian's Chamber"},
            character=None,
            item=items.Painting(),
            visited=False,
            locked=False
        )


class Outside(Location):
    def __init__(self):
        super().__init__(
            name="The Outside",
            description="You are free.",
            exits=None,
            character=None,
            item=None,
            visited=False,
            locked=True
        )

    # Custom on visit method for the Outside room to prompt the win message.
    def on_visit(self):
        os.system('cls')
        print("\n" + "=" * 40)
        print(self.name)
        print("-" * 40)
        print(self.description)
        print("-" * 40)
        print("Congrats, you have successfully escaped!")
        game_logic.play_again()

