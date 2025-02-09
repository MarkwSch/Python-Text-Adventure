import backpack
import rooms
import items
import game_logic

# General Item class with the name and description
class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def interact(self, player_backpack):
        pass


# Class defining the PickupItems and the on_pickup method
class PickupItem(Item):
    def __init__(self, name, description):
        super().__init__(name, description)

    def interact(self, player_backpack):
        print(f"\nYou've picked up the {self.name}.")
        player_backpack.add(self)
        input("\nPress 'Enter' to continue.")


# Class defining the FixedItems and the interact method
class FixedItem(Item):
    def __init__(self, name, description):
        super().__init__(name, description)

    def interact(self, player_backpack):
        print(f"You interact with the {self.name}.")
        # Add specific interactions based on the object item


# Below defines the PickUp Items
class MagicKeyofBeginnings(PickupItem):
    def __init__(self, location):
        super().__init__(
            name="Magic Key of Beginnings",
            description="A shimmering key that radiates a sense of new possibilities, found in the dimly lit Entrance "
                        "Hall of the ancient dungeon."
        )
        self.location = location

    def interact(self, player_backpack):
        print(f"\nYou've picked up the {self.name}.")
        player_backpack.add(self)
        input("\nPress 'Enter' to continue.")
        self.location.remove_item()  # Removes the item from the location it is in


class MagicKeyOfKnowledge(PickupItem):
    def __init__(self, location):
        super().__init__(
            name="Magic Key of Knowledge",
            description="An ancient key adorned with intricate symbols, emanating wisdom and unlocking the secrets "
                        "hidden within the dusty tomes of the Library of Lost Knowledge."
        )

        self.location = location

    def interact(self, player_backpack):
        print(f"\nYou've picked up the {self.name}.")
        player_backpack.add(self)
        input("\nPress 'Enter' to continue.")
        self.location.remove_item()  # Removes the item from the location it is in


class MagicKeyOfDespair(PickupItem):
    def __init__(self):
        super().__init__(
            name="Magic Key of Despair",
            description="A foreboding key with dark engravings, discovered in the ominous Chasm of Despair, "
                        "capable of unlocking the mysteries veiled in the depths."
        )


class MagicKeyOfSecrets(PickupItem):
    def __init__(self, location):
        super().__init__(
            name="Magic Key of Secrets",
            description="A mysterious key concealed within a Hidden Alcove, exuding an aura of secrecy and promising "
                        "to unveil concealed truths."
        )
        self.location = location

    def interact(self, player_backpack):
        print(f"\nYou've picked up the {self.name}.")
        player_backpack.add(self)
        input("\nPress 'Enter' to continue.")
        self.location.remove_item()  # Removes the item from the location it is in


class MagicKeyOfLostTime(PickupItem):
    def __init__(self):
        super().__init__(
            name="Magic Key of Lost Time",
            description="A weathered key with a nostalgic touch, discovered in The Lost Room, unlocking doors that "
                        "transcend the echoes of forgotten moments."
        )


# Below defines the Fixed Items
class Lever(FixedItem):
    def __init__(self, chasm_of_despair):
        super().__init__(
            name="Lever",
            description="A sturdy mechanism within the Goblin's Lair, beckoning interaction."
        )
        self.chasm_of_despair = chasm_of_despair

    def interact(self, player_backpack):
        print("\nYou pull the lever, and you hear a door in the Corridor of Whispers unlock.")
        self.chasm_of_despair.unlock_door() # Unlocks the door to the Chasm of Despair
        input("\nPress 'Enter' to continue.")


class Chest(FixedItem):
    def __init__(self):
        super().__init__(
            name="Chest",
            description="A mysterious container hidden in the Chasm of Despair, awaiting discovery."
        )
        self.item = items.MagicKeyOfDespair()

    def interact(self, player_backpack):
        # If the key is still in the chest
        if self.item is not None:
            print("\nYou open the chest and find a key inside.")
            interaction_successful = False

            # Loop asking what the player wants to do.
            while interaction_successful is not True:
                response = input("Do you want to pick up the key? (pick up/leave): ")
                if response.lower() == 'pick up':
                    self.item.interact(player_backpack)
                    self.item = None  # Sets to None so player can't pick it up again
                    interaction_successful = True
                elif response.lower() == 'leave':
                    print("You shut the chest door and leave the key.")
                    interaction_successful = True
                    input("\nPress 'Enter' to continue.")
                else:
                    print("Sorry, I didn't understand. Try again.")
        # Else if the key is not in the chest
        else:
            print("You open the chest where you found the key and there is nothing inside.")
            input("\nPress 'Enter' to continue.")


class Button(FixedItem):
    def __init__(self, hidden_alcove):
        super().__init__(
            name="Button",
            description="A small button mounted on a pedestal on the other side of the room."
        )
        self.left_bridge = True
        self.right_bridge = True
        self.hidden_alcove = hidden_alcove

    def interact(self, player_backpack):
        # If both the left bridge and right bridge still exist
        if self.left_bridge and self.right_bridge:
            print("\nYou carefully examine the room and notice two bridges leading to the button.")
            print("There is a Left Bridge and a Right Bridge.")
            # Player chooses a bridge
            response = input("Which bridge will you choose? (left/right/walk away): ").lower()
            interaction_successful = False
            # Loop asking the player what they want to do. Exited upon a successful interaction.
            while interaction_successful is not True:
                if response == "left":
                    print("\nYou cautiously step onto the Left Bridge and start crossing.")
                    print("As you step onto the Left Bridge, it gives way, and you fall into the abyss.")
                    print("You have met a tragic fate.")
                    input("\nPress 'Enter' to continue.")
                    game_logic.game_over()  # Run the game_over method
                elif response == "right":
                    print("\nYou decide to take the Right Bridge and carefully make your way across.")
                    print("The Right Bridge supports your weight, and you successfully reach the other side.")
                    print("You press the Button, and you hear a distant mechanism unlocking a passage.")
                    input("\nPress 'Enter' to continue.")
                    self.hidden_alcove.unlock_door() # Unlock the door to the Hidden Alcove.
                    interaction_successful = True
                elif response == 'walk away':
                    print("You walk away from the bridges.")
                    interaction_successful = True
                    input("\nPress 'Enter' to continue.")
                else:
                    response = input("Not a valid option. Try again. (left/right/walk away): ")



class Painting(FixedItem):
    def __init__(self):
        super().__init__(
            name="Painting",
            description="A neglected artwork in The Lost Room, concealing a secret."
        )
        self.item = items.MagicKeyOfLostTime()  # Creates an instance of the magic key inside the painting

    def interact(self, player_backpack):
        if self.item is not None:
            print("\nYou notice the painting is at an angle and push it to the side.")
            interaction_successful = False
            while interaction_successful is not True:
                response = input("Do you put your hand inside? (reach inside/leave): ")
                if response.lower() == 'reach inside':
                    self.item.interact(player_backpack)
                    self.item = None  # Sets to None so player can't pick it up again
                    interaction_successful = True
                elif response.lower() == 'leave':
                    print("You decide to leave and walk away from the hole.")
                    interaction_successful = True
                    input("\nPress 'Enter' to continue.")
                else:
                    print("Sorry, I didn't understand. Try again.")
        else:
            print("\nYou push the painting aside to reveal the hole where you found the key.")
            input("\nPress 'Enter' to continue.")


class Horn(FixedItem):
    def __init__(self):
        super().__init__(
            name="Horn",
            description="An enigmatic instrument in the Horn Chamber, sparking curiosity with its presence."
        )
        self.horn_used = False

    def interact(self, player_backpack):
        print("\nYou interact with the horn, and its sound reverberates through the chamber.")
        self.horn_used = True # Sets horn_used to true so it can be identified by the Tired Guard.
        input("\nPress 'Enter' to continue.")