'''
Amare Diotte
GLAB-340.5.1
Data Engineering 
2024-RTT-107

'''


import random
import typing




# this function generates a random list that is a subset of the 'words' list
def generate_list(words: list[str]) -> None:
    # returns a random list between 2 and 5 elements long
    target = random.sample(words, random.randint(2,5))
    return target

def traverse_list(current) -> None:
    for x,item in enumerate(current):
        print(x, "|", item, end="    ")
    print()
        


def get_actions(current: list[str]) -> None:
    print("Please select an action from the list:\n",
          "1. Append word to the end of list\n",
          "2. Extend the list with another list\n",
          "3. Concatenate two elements in the list\n",
          "4. Traverse the list and view its elements\n",
          "5. Modify and element in the list\n",
          "6. Pop and element from the list\n",
          "7. Remove element from the list\n",
          "8. Sort list in ascending or descending order\n",
          "9. Exit game"
          )
    choice = int(input("Enter a number to choose and action: "))

    # use a switch statement to parse user input
    match choice:
        case 1:
            #append word to the end of the list
            new_word: str = input("Enter a new string to append to the list")
            current.append(new_word)
            return current
        case 2:
            #extend the list with another list
            print("Please enter a list you would like to add to the current list. Separate elements with commas")
            new_list: list[str] = input("Example: item1, item2, item3, ...").split(",")
            current.extend(new_list)
            return current
        case 3: 
            # concatenate two elements in the list
            traverse_list(current)
            element1: int = int(input("Enter index of first element: "))
            while element1 > len(current):
                element1 = input("Invalid index, please enter a number smaller than", len(current))
            element2: int = int(input("Enter index of second element: "))
            while element2 > len(current):
                element2 = input("Invalid index, please enter a number smaller than", len(current))
            current[element1] += current[element2]
            del current[element2]
            return current
        case 4:
            # Traverse the list and view its elements
            print()
            print("Here is your current list: ")
            traverse_list(current)
            input("Hit enter when you're done viewing")
            return current
        case 5: 
            # modify an element in the list.
            traverse_list(current)
            index: int = int(input("Enter the index of the element you would like to modify: "))
            while index > len(current)-1:
                index = input("Invalid index, please enter a number smaller than", len(index)-1)
            new_word: str = input("Enter the new element name: ")
            current[index] = new_word
            return current
        case 6:
            # Pop an element from the list
            if len(current) > 0:
                popped_word: str = current.pop()
                print(popped_word, "was removed!")
                input("Please hit enter to continue")
            else:
                print("Sorry, this list is empty. No items to pop!")
            return current
        case 7: 
            removed_word = input("Please enter the element you would like to remove: ")
            if removed_word in current:
                current.remove(removed_word)
            else: 
                print("This element was not found in the list")
            return current
        case 8: 
            # sort list in ascending or descending order.
            ascending = input("Sort in ascending order? (y/n)").lower() == "y"
            current.sort(reverse=(not ascending))
            return current
        case 9:
            return []

    
def compare_lists(target: list[str], current: list[str]) -> bool:
    print("This is your current list: ")
    traverse_list(current)
    print("This is your target list: ")
    traverse_list(target)
    if current == target:
        print("These lists are the same, good job!")
        input("Press enter to continue")
        return True
    else:
        input("Press enter to continue")
        return False
    

def main_loop():
    words: list[str] = ["Kingdom of the North", "Kingdom of Mountain and Vale", 
         "Kingdom of Isles and the Rivers", "Kingdom of the Stormlands",
         "Kingdom of the Rock", "Kingdom of the Reach", "Principality of Dorne"]
    target: list[str] = generate_list(words)
    while not compare_lists(target, words):
        words = get_actions(words)
        if not words:
            break
    print("Goodbye!")

main_loop()