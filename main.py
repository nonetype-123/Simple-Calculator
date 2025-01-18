import os

def cls():
    os.system("cls")

def interface():

    attempt = 0

    # Example and results field
    x_size_field = (len(str(results)) + 3) if results == 0 else (len(str(results)) + 2)

    for _ in range(2):
        
        # Creating a title
        print("Results:" if attempt == 1 else "\nExample:")

        # Creating a fields
        for _ in range(x_size_field if attempt == 1 else (len(example) + 2)):
            print("_", end="")

        print(f"\n[{results if attempt == 1 else example}]")

        for _ in range(x_size_field if attempt == 1 else (len(example) + 2)):
            print("-", end="")

        print("\n")

        attempt += 1

if __name__ == "__main__":

    # Variables

    example = ""
    results = 0

# About the program

print("\nAbout the program:\nThis is a simple calculator with ASCII interface\n")

# Commands

print('Commands:\n"exit" - to close the program\n"cls" - to clean the console\n')

while True:

    example = input("Your mathematical example: ")

    # Checking commands

    if example == "exit":
        break

    elif example == "cls":
        cls()
        continue

    # Error checking

    try:
        results = float(eval(example))

    except Exception as err:
        print("\nAn unknown error has occurred!\n")
        continue

    interface()

input("\nPress Enter to Continue...")