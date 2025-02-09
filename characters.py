import items
import game_logic

class Character:
    def __init__(self, name, description):
        # Name of the character
        self.name = name
        # Description of the character
        self.description = description

    # If the player interacts with the character, create an interaction.
    def interact(self, player_backpack):
        pass


# Whispering Spirit Character - explains the basic goal of the game.
class WhisperingSpirit(Character):
    def __init__(self):
        super().__init__(
            name="Whispering Spirit",
            description="An ethereal spirit that offers advice to those who listen."
        )

    def interact(self, player_backpack):
        print("Whispering Spirit: Welcome, traveler. To escape this dungeon, you must find all 5 magical keys.")
        input("\nPress 'Enter' to continue.")


# Deceiving Goblin Character - will ask to see the player's keys, and steals them if the player shows them.
class DeceivingGoblin(Character):
    def __init__(self):
        super().__init__(
            name="Deceiving Goblin",
            description="A small, mischievous goblin with a penchant for shiny things."
        )

    def interact(self, player_backpack):
        response = input("\nDeceiving Goblin: Hello, weary traveller. If you have any keys, I can show you a trick to "
                         "help you escape. (sure/no): ").lower()
        interaction_successful = False
        # If player responds yes.
        while interaction_successful is not True:
            if response == "sure":
                print("\nDeceiving Goblin: Excellent, now let's have a look.")
                if player_backpack.count() == 0:
                    print("\nDeceiving Goblin: That's disappointing, you don't have any keys. Come back to me when you "
                          "have found one, and I will show you the trick.")
                    interaction_successful = True
                else:
                    # Loop to steal all the keys from the player.
                    key_count = player_backpack.count()
                    while key_count > 0:
                        key = player_backpack._backpack[0]
                        player_backpack.remove(key)
                        print(f"{key.name} was removed from your inventory.")
                        key_count = player_backpack.count()
                    print("\nDeceiving Goblin: Yoink!")
                    print("Your keys have been stolen, it is now impossible to win the game.")
                    input("Press any key to continue...")
                    game_logic.game_over() # Force the player to game over.
            elif response == "no":
                print("Deceiving Goblin: Well, I'll be here if you ever want to show me...")
                interaction_successful = True
            else:
                print("Deceiving Goblin: What did you say? Speak clearly!")
                response = input("Deceiving Goblin: So what do you say, will you show me? (sure/no): ")
                interaction_successful = False
        print("Deceiving Goblin: Bye!")
        input("\nPress 'Enter' to continue.")


class TiredGuard(Character):
    def __init__(self, horn_chamber, outside):
        super().__init__(
            name="The Tired Guard",
            description="A mystical insomniac entity guarding the final doorway."
        )
        # Variable that defines if the Tired Guard is asleep
        self.asleep = True
        # Uses the horn_chamber instance to determine if the horn has been used.
        self.horn_chamber = horn_chamber
        # Uses the outside instance to unlock the door.
        self.outside = outside

    def interact(self, player_backpack):
        # Checks if the horn has been used to determine whether the Guard is asleep or not.
        if self.horn_chamber.item.horn_used is True:
            self.asleep = False
        # If the Guard is still asleep...
        if self.asleep:
            print("\nThe Tired Guard is sound asleep...maybe there is a way to wake him up?")
            input("\nPress 'Enter' to continue.")
        # Else, if he is awake...
        else:
            print("\nThe Tired Guard: Huh? Who are you? I was having a good nap until a fool sounded that horn.")
            response = input("The Tired Guard: Oh, you want to escape, huh? Well, you need to collect all 5 magic "
                             "keys. How many do you have? (show keys/walk away): ").lower()
            interaction_successful = False
            while interaction_successful is not True:
                if response == "show keys":
                    # Uses the binary search method in the backpack to count the keys.
                    count = self.check_keys(player_backpack)
                    if count == 5:
                        print("The Tired Guard: You have proven yourself. The door to freedom is now open.")
                        self.outside.unlock_door() # Unlocks the door to the Outside.
                        input("\nPress 'Enter' to continue.")
                        interaction_successful = True
                        continue
                    else:
                        # Informs the player how many more keys they have to collect.
                        print(f"The Tired Guard: You have only collected {count}. You need to find {5 - count} more.")
                        input("\nPress 'Enter' to continue.")
                        interaction_successful = True
                        continue
                if response == 'walk away':
                    print("The Tired Guard: Come back when you are ready.")
                    interaction_successful = True
                else:
                    response = input("The Tired Guard: I don't understand. How many keys do you have? (show keys/walk "
                                     "away): ")

    # Method to check the keys of the player.
    def check_keys(self, player_backpack):
        count = 0
        # Just passing any location in since we don't need to interact with it
        # Uses the binary search method in the backpack
        if player_backpack.in_backpack(items.MagicKeyofBeginnings(self.horn_chamber)):
            count += 1
        if player_backpack.in_backpack(items.MagicKeyOfSecrets(self.horn_chamber)):
            count += 1
        if player_backpack.in_backpack(items.MagicKeyOfDespair()):
            count += 1
        if player_backpack.in_backpack(items.MagicKeyOfKnowledge(self.horn_chamber)):
            count += 1
        if player_backpack.in_backpack(items.MagicKeyOfLostTime()):
            count += 1
        return count

