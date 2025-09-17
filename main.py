if __name__ == "__main__":
    import json
    import functions





    is_running = True      # Set the game to running

    cards = {}    # Initialize the variable for cards
    try:
        with open("data.json", "r") as f:
            cards = json.load(f)            # Get previous save data if a save file was created previously
    except FileNotFoundError:
        with open("data.json", "w") as f:   
            json.dump({}, f)                # Create a new save file if one wasn't previously created


    while is_running:
        print("Flashcards")
        print("> Add card [1]")
        print("> Delete card [2]")       # Show the user options and allow them to input
        print("> View cards [3]")
        print("> Quit [4]")
        options = input("> ").strip()

        match options:
            case "1":
                functions.add_card(cards)   # Call the add cards function to add the user's input to the dictionary
            case "2":
                if len(cards) == 0:
                    print("You don't have any cards yet!")   # Say if the user has no cards to delete yet instead if it doesn't
                else:
                    functions.delete_card(cards)
            case "3":
                if len(cards) == 0:
                    print("You don't have any cards yet!")   # Say if the user has no cards to view yet instead if it doesn't
                else:
                    functions.view_cards(cards)
            case "4":
                print("Saving...")
                with open("data.json", "w") as f:
                    json.dump(cards, f)
                is_running = False
                print("Goodbye")
                break
            case _:
                print("Please pick a valid option")
