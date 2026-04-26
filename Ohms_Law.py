# Ohm's Law Calculator

def get_float_input(prompt):
    # Ensures the user enters a valid number, preventing crashes.
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid character. Please input real numbers only.")

def calculate_voltage():
    print("\n--- Calculating Voltage ---")
    i = get_float_input("Current (I) in Amps: ")
    r = get_float_input("Resistance (R) in Ohms: ")
    print(f"Result: {round(i*r, 4)}V")

def calculate_current():
    print("\n--- Calculating Current ---")
    v = get_float_input("Voltage (I) in Volts: ")
    r = get_float_input("Resistance (R) in Ohms: ")
    print(f"Result: {round(v/r, 4)}A")

def calculate_resistance():
    print("\n--- Calculating Resistance ---")
    i = get_float_input("Current (I) in Amps: ")
    v = get_float_input("Voltage (V) in Volts: ")
    print(f"Result: {round(v/i, 4)}Ω")

def main_menu():
    # Main engine of the program
    actions = {
        "1": calculate_voltage,
        "2": calculate_current,
        "3": calculate_resistance
    }
    

    while True:
    # ================ Ohm's Law Calculator =============
        print("\n" + "="*10 + " Ohm's Law Calculator " + "="* 10)
        print("1. Calculate Voltage (V = IR)")
        print("2. Calculate Current (I = V/R)")
        print("3. Calculate Resistance (R = V/I)")
        print("4. Exit")

        choice = input("\nSelect an option > ")

        if choice == "4":
            print("\n" + "="*12 + " Okay. Thank you! " + "="*12)
            break

        elif choice in actions:
            actions[choice]() # Calls specific function for each type of calculation

            repeat = input("\nWould you like to calculate again? (Y/N) > ").lower()
            
            if repeat == "y":
                main_menu()
            
            elif repeat == "n":
                print("\n" + "="*12 + " Okay. Thank you! " + "="*12)
                quit() 
        
        else:
            print("Error. Invalid option. Please try again.")

if __name__ == "__main__":
    main_menu()
