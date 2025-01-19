# by nonetype-123

def error():
    print("""\n
        ╔══════════════════════╗
        ║An error has occurred!║
        ╚══════════════════════╝\n""")

def ascii_interface():

    attempt = 0

    # Example and results field
    x_size_field = len(str(results))

    for _ in range(2):
        
        # Creating a title
        print("        Results:" if attempt == 1 else "\n\n        Example:")

        # Creating a fields
        print("        ╔", end="")
        for _ in range(x_size_field if attempt == 1 else len(example)):
            print("═", end="")
        print("╗", end="")

        print(f"\n        ║{results if attempt == 1 else example}║")

        print("        ╚", end="")
        for _ in range(x_size_field if attempt == 1 else len(example)):
            print("═", end="")
        print("╝", end="")

        print("\n")

        attempt += 1

if __name__ == "__main__":

    # Variables

    cont = False
    number = ""
    operator = ""
    operators = ['+', '-', '*', '/']
    example = ""
    results = 0

# About the program

print("\nAbout the program:\nThis is a simple calculator with ASCII interface\n")

# Commands

print('Commands:\n"reset" - reset previously entered data\n"enter" - solve the compiled example')

while True:
    while True:
        number = input("\nYour number: ")
        
        if number == "reset":
            example = ""
            cont = True
            break
        
        # Checking for number suitability
        
        try:
            number = float(number)
        except Exception as err:
            error()
            continue
            
        example += str(number) 
        break
        
    if cont == True:
        cont = False
        continue
        
    while True:
        operator = input("\nYour operator: ")
        
        if operator == "reset":
            example = ""
            cont = True
            break
            
        elif operator == "enter":
            results = float(eval(example))
            ascii_interface()
            cont = True
            break

        # Operator suitability check
        
        elif operator not in operators:
            error()
            continue
            
        example += operator
        break
        
    if cont == True:
        cont = False
        continue
