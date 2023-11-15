import time

def introduction():
    print("Welcome to the Mysterious Forest Adventure!")
    time.sleep(1)
    print("You find yourself at the entrance of a dark and mysterious forest.")
    time.sleep(1)
    print("Your goal is to reach the other side. Be careful with your decisions!")

def make_choice(choices):
    print("Choose your path:")
    for i, choice in enumerate(choices, start=1):
        print(f"{i}. {choice}")

    while True:
        try:
            user_input = int(input("Enter the number of your choice: "))
            if 1 <= user_input <= len(choices):
                return user_input
            else:
                print("Invalid input. Please enter a valid number.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def forest_path():
    print("You start walking along a narrow path in the forest.")
    time.sleep(1)
    print("Ahead, you see a fork in the road.")

    choices = ["Take the left path", "Take the right path"]
    user_choice = make_choice(choices)

    if user_choice == 1:
        print("You chose to take the left path.")
        time.sleep(1)
        print("As you walk, you encounter a friendly squirrel.")
        time.sleep(1)
        print("The squirrel guides you safely through the forest.")
        return "safe"
    else:
        print("You chose to take the right path.")
        time.sleep(1)
        print("The path becomes darker, and you hear strange noises.")
        time.sleep(1)
        print("You encounter a group of unfriendly creatures.")
        return "dangerous"

def main():
    introduction()

    path_result = forest_path()

    if path_result == "safe":
        print("Congratulations! You safely navigated through the mysterious forest.")
    else:
        print("Oh no! The creatures in the forest pose a threat, and you couldn't make it through.")

if __name__ == "__main__":
    main()
