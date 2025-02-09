# Python file for all the commands needed to initialise the game.
import main
import rooms
import map
import os


# Method to initialise the map
def initialise_map():
    # Create a 3x3 map
    map_width = 5
    map_height = 9
    game_map = map.Map(map_width, map_height)
    # Add locations to the map
    game_map.add_location(2, 8, " ? ")  # Entrance Hall
    game_map.add_location(2, 6, " ? ")  # Corridor of Whispers
    game_map.add_location(0, 6, " ? ")  # Goblin's Lair
    game_map.add_location(4, 6, " ? ")  # Library of Lost Knowledge
    game_map.add_location(4, 4, " ? ")  # Horn Chamber
    game_map.add_location(2, 4, " ? ")  # Chasm of Despair
    game_map.add_location(0, 4, " ? ")  # Cursed Crossroads
    game_map.add_location(0, 2, " ? ")  # Secret Alcove
    game_map.add_location(2, 2, " ? ")  # Guardian's Chamber
    game_map.add_location(4, 2, " ? ")  # The Lost Room

    # Add the directions available from each room
    game_map.add_location(2, 0, " ? ")  # Outside
    game_map.add_location(1, 2, "W/E")  # Direction
    game_map.add_location(3, 2, "E/W")  # Direction
    game_map.add_location(2, 1, "N/S")  # Direction
    game_map.add_location(1, 4, "W/E")  # Direction
    game_map.add_location(3, 4, "E/W")  # Direction
    game_map.add_location(2, 3, "N/S")  # Direction
    game_map.add_location(0, 3, "N/S")  # Direction
    game_map.add_location(1, 6, "W/E")  # Direction
    game_map.add_location(2, 7, "N/S")  # Direction
    game_map.add_location(2, 5, "N/S")  # Direction
    game_map.add_location(3, 6, "E/W")  # Direction

    # Add the filler squares
    game_map.add_location(0, 8, "■■■")  # Filler
    game_map.add_location(1, 8, "■■■")  # Filler
    game_map.add_location(3, 8, "■■■")  # Filler
    game_map.add_location(4, 8, "■■■")  # Filler
    game_map.add_location(0, 7, "■■■")  # Filler
    game_map.add_location(1, 7, "■■■")  # Filler
    game_map.add_location(3, 7, "■■■")  # Filler
    game_map.add_location(4, 7, "■■■")  # Filler
    game_map.add_location(0, 5, "■■■")  # Filler
    game_map.add_location(1, 5, "■■■")  # Filler
    game_map.add_location(3, 5, "■■■")  # Filler
    game_map.add_location(4, 5, "■■■")  # Filler
    game_map.add_location(1, 3, "■■■")  # Filler
    game_map.add_location(3, 3, "■■■")  # Filler
    game_map.add_location(4, 3, "■■■")  # Filler
    game_map.add_location(0, 1, "■■■")  # Filler
    game_map.add_location(1, 1, "■■■")  # Filler
    game_map.add_location(3, 1, "■■■")  # Filler
    game_map.add_location(4, 1, "■■■")  # Filler
    game_map.add_location(0, 0, "■■■")  # Filler
    game_map.add_location(1, 0, "■■■")  # Filler
    game_map.add_location(3, 0, "■■■")  # Filler
    game_map.add_location(4, 0, "■■■")  # Filler
    return game_map


# Method to initialise instances of every room
def initialise_rooms():
    # Initialize all rooms
    entrance_hall = rooms.EntranceHall()
    corridor_of_whispers = rooms.CorridorOfWhispers()
    library_of_lost_knowledge = rooms.LibraryOfLostKnowledge()
    chasm_of_despair = rooms.ChasmOfDespair()

    horn_chamber = rooms.HornChamber()
    hidden_alcove = rooms.HiddenAlcove()
    lost_room = rooms.LostRoom()
    outside = rooms.Outside()
    # Passes the Hidden Alcove instance into the Cursed Crossroads location to unlock with the button.
    cursed_crossroads = rooms.CursedCrossroads(hidden_alcove)
    # Passes the Chasm of Despair instance into the Goblin Lair to unlock with the lever.
    goblin_lair = rooms.GoblinLair(chasm_of_despair)
    # Passes both the Horn Chamber and the Outside instances into the Guardian's Chamber.
    guardians_chamber = rooms.GuardiansChamber(horn_chamber, outside)

    # Dictionary containing the string name and instances for navigation.
    room_instances = {
        "Entrance Hall": entrance_hall,
        "Corridor of Whispers": corridor_of_whispers,
        "Goblin's Lair": goblin_lair,
        "Library of Lost Knowledge": library_of_lost_knowledge,
        "Chasm of Despair": chasm_of_despair,
        "Horn Chamber": horn_chamber,
        "Cursed Crossroads": cursed_crossroads,
        "Hidden Alcove": hidden_alcove,
        "Guardian's Chamber": guardians_chamber,
        "The Lost Room": lost_room,
        "Outside": outside
    }
    return entrance_hall, room_instances


# Game over method.
def game_over():
    print("GAME OVER.")
    print("You have lost the game, better luck next time!")
    play_again()


# Method to check if the player wants to play again
def play_again():
    response = ""
    while response != "yes" or response != "no":
        response = input("Play again? (yes/no): ")
        if response.lower() == "yes":
            print("Roger, reloading the game.")
            input("Press any key to continue...")
            os.system('cls')
            main.main()  # reload the game
        if response.lower() == "no":
            print("Thanks for playing!")
            input("Press any key to continue...")
            quit()  # Quit the console.
        else:
            print("Not a valid option. Try again.")

# Prints the game rules
def game_rules():
    desc = "'Escape the Forbidden Dungeon' is an interactive text-based adventure game set in an ancient and " \
           "mysterious dungeon. Your goal is to navigate through various locations, solve puzzles, and collect magic " \
           "keys to unlock the path to freedom. Along the way, you'll encounter characters, items, and challenges " \
           "that will test your wit and courage. Be cautious, as wrong choices may lead to perilous situations!"
    movement_desc = "\nYou will be given a list of available moves in each room:\nType 'characters' to interact with " \
                    "a character.\nType 'item' to interact with an item.\nType 'move' to move to another location. " \
                    "Type 'backpack' to view your items."
    print(desc)
    print(movement_desc)
    print()
    input("\nPress 'Enter' to continue.")
