'''
Amare Diotte
GLAB-340.5.1
Data Engineering 
2024-RTT-107

'''


import random
import typing


words: list[str] = ["Kingdom of the North", "Kingdom of Mountain and Vale", 
         "Kingdom of Isles and the Rivers", "Kingdom of the Stormlands",
         "Kingdom of the Rock", "Kingdom of the Reach", "Principality of Dorne"]

# this function generates a random list that is a subset of the 'words' list
def generate_list() -> None:
    # returns a random list between 2 and 5 elements long
    target = random.sample(words, random.randint(2,5))
    return target

def get_actions(current: list[str]) -> list[str]:
    print("Please select an action from the list:\n",
          "1. Append word to the end of list\n",
          "2. Extend the list with another list\n",
          "3. Concatenate two elements in the list\n",
          "4. Traverse the list and view its elements\n",
          "5. Modify and element in the list\n",
          "6. Pop and element from the list\n",
          "7. Remove element from the list\n",
          "8. Sort list in ascending or descending order\n"
          )
    choice = int(input("Enter a number to choose and action: "))

    # use a switch statement to parse user input
    match choice:
        case 1:
            #append word to the end of the list
            new_word = input("Enter a new string to append to the list")
            return current.append(new_word)
        case 2:
            #extend the list with another list
            new_list: list[str] = input("Enter a list to extend the current list. Please use list format with parenthesis and commas:\n",
                             "Example: (item1, item2, item3, ...)").split(",")
            return current.extend(new_list)
        case 3: 
            # concatenate two elements in the list
            print("3")

        case 4:
            # Traverse the list and view its elements
            print("4")
        case 5: 
            # modify an element in the list.
            print("5")
        case 6:
            # Pop an element from the list
            print("6")
        case 7: 
            # Remove an element from the list
            print("7")
        case 8: 
            # sort list in ascending or descending order.
            print("8")
        case 9:

    
def compare_lists(target: list[str], current: list[str]) -> bool:
    # compare lists
    return True

def main_loop():
    quit_game: bool = False
    current: list[str] = generate_list()
    while not quit_game:
        get_actions(current)

