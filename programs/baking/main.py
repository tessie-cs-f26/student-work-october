# Your Calculator Project
# Name: 
# Description: 
# ================================

# Welcome message
print("Welcome to my calculator!")

# Your code below:
running = True
while running:
    print("Menu Options")
    print("1. Tablespoons to Cups")
    print("2. Cups to Tablespoons")
    print("3. Grams to Ounces")
    print("4. Exit")
    menu_choice = input("Please pick one of the four options above\n")
    if menu_choice == "1":
        number_tablespoons = int(input("How many tablespoons do you have?\n"))
        final_number_ofcups = number_tablespoons/16
        print(f"The total number of cups is {final_number_ofcups}")
        want_to_continue = input("Do you like to continue?(yes/no)\n").lower()
        if want_to_continue == "no":
            print("Thank you for using my calculator!")
            break
    elif menu_choice == "2":
        number_cups = int(input("How many cups do you have?\n"))
        final_number_tablespoon = number_cups * 16
        print(f"Your final number of tablespoons is {final_number_tablespoon}")
        want_to_continue1 = input("Do you like to continue?(yes/no)\n").lower()
        if want_to_continue1 == "no":
            print("Thank you for using my calculator!")
            break
    elif menu_choice == "3":
        grams = float(input("How many grams do you have?\n"))
        total_ounces = grams/28.35
        print(f"The total number ounces is {total_ounces}")
        want_to_continue2 = input("Do you like to continue?(yes/no)\n").lower()
        if want_to_continue2 == "no":
            print("Thank you for using my calculator!")
            break
    elif menu_choice == "4":
        print("Thank you you for using my calculator")
        break
    else:
        print("Invalid Option please try again")
        
            