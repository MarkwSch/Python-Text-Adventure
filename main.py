import game_logic
from backpack import BackPack
import os

# Initialises the room instances now, useful for unlocking doors with fixed items


def main():
    # Initialising
    entrance_hall, room_instances = game_logic.initialise_rooms()
    player_backpack = BackPack(None)
    current_location = entrance_hall
    new_location_instance = None
    game_map = game_logic.initialise_map()
    # Print the game rules
    game_logic.game_rules()

    while True:  # Game loop

        current_location.on_visit()
        response = input("Please enter your move: ")

        # Allows player to interact with the character
        if current_location.character is not None:
            if response.lower() == current_location.character.name.lower() or response.lower() == "character":
                current_location.character.interact(player_backpack)
                continue

        # Allows player to interact with the item
        if current_location.item is not None:
            if response.lower() == current_location.item.name.lower() or response.lower() == "item":
                print(f"\nYou approach the {current_location.item.name}.")
                print(current_location.item.description)
                response = input("\nWhat did you want to do? (interact/walk away): ")
                if response.lower() == 'interact':
                    current_location.item.interact(player_backpack)
                elif response.lower() == 'walk away':
                    continue
                else:
                    print("Sorry, I didn't understand. Try again.")

        # Displays the backpack to the player
        if response.lower() == "backpack":
            player_backpack.list()

        # Allows player to move
        if response.lower() == "move":
            os.system('cls')
            print("\n" + "=" * 40)
            print(current_location.name)
            print("-" * 40)
            game_map.update_current_location(current_location)  # Sets the current location to the triangle.
            game_map.display_map()  # Displays the map to the player

            # Display exits
            print("\nAvailable Exits:", ", ".join(current_location.exits.keys()))

            # Player input for the next move
            next_move = input("\nEnter your next move: ").lower()
            for direction, room in current_location.exits.items():
                if next_move == direction.lower():
                    # Process the next move
                    new_location_name = current_location.exits[direction]
                    new_location_instance = room_instances\
                        .get(new_location_name)

            if new_location_instance is not None:
                if new_location_instance.locked:  # Check if the room is locked.
                    os.system('cls')  # Clear the console
                    print("\n" + "=" * 40)
                    print(current_location.name)
                    print("-" * 40)
                    print("Door is locked. Maybe there is a way to unlock it?")
                    input("\nPress 'Enter' to continue.")
                    continue
                game_map.update_visited(current_location)  # Update the map.
                current_location = new_location_instance  # Set the current_location to the new instance and restart
                # the loop.

            else:
                print("Invalid move. Try again.")
        else:
            print("Sorry, I didn't understand. Try again.")


if __name__ == "__main__":
    main()