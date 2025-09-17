def add_card(cards):                      # Function to add cards to the card dictionary
       
    print("Type your question:")     # Ask the user for their palm card question and add it to a variable
    question = input("> ").strip()

    print("Type your answer:")       # Ask the user for their answer and add it to a variable
    answer = input("> ").strip()

    cards[question] = answer        # Return the question and answer as a key value pair so
                                    # that it can be added to the cards variable


def delete_card(cards):              # Function to delete cards from the card dictionary
    print(" | ", end="")
    for x, y in enumerate(cards.keys()):       
        print(f"{x + 1}: {y}", end=" | ")      # Print the cards by their numbers and ask user for the number of the card they want to delete
    print()
    keys = list(cards.keys())
    while True:
        print("Choose a card to delete (q to quit)")        # Ask user what card they want to delete (by number)
        key = input("> ")    
        try:
            if key == "q":          # Quit when the user inputs 'q'
                return
            key = int(key)          # Convert key to an integer and convert it to the item to be deleted from the dictionary
            key = keys[key - 1]
            cards.pop(key)
            print(f"{key} was successfully deleted.")
            return         
        except ValueError:
            print("Please enter a valid number.")     # If the key is not an integer/is out of range retry


def view_cards(cards):
    print(" | ", end="")
    for x, y in enumerate(cards.keys()):       
        print(f"{x + 1}: {y}", end=" | ")      
    print()
    keys = list(cards.keys())
    while True:
        print("Choose a card you want to view (q to quit)")
        key = input("> ")    
        try:
            if key == "q":          # Quit when the user inputs 'q'
                return
            key = int(key)          # Convert key to an integer and convert it to the item to be deleted from the dictionary
            key = keys[key - 1]
            print(f"{key} | {cards[key]}")
        except ValueError:
            print("Please enter a valid number.")     # If the key is not an integer/is out of range retry