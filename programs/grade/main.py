# Your Calculator Project
# Name: 
# Description: 
# ================================

# Welcome message
print("Welcome to my calculator!")

# Main loop
running = True
while running:
    # Display menu
    print("\nPlease select an option:")
    print("1. Math")
    print("2. Science")
    print("3. English")
    print("4. History")
    print("5. Average score overall")
    print("6. Exit")
    
    # Get user choice
    choice = input("\nEnter your choice (1-6): ")
    
    # TODO: Handle each menu option
    # Use if/elif/else to check the choice
    
    if choice == "1":
        # Ask for math score
        math = int(input("Enter your score for Math out of 100: "))

        print(f"Your average score for math is {math}")
        
    elif choice == "2":
        # Ask for science score
        science = int(input("Enter your score for science out of 100: "))

        print(f"Your average score for science is {science}")
        
    elif choice == "3":
        # Ask for english score
        english = int(input("Enter your score for english out of 100: "))

        print(f"Your average score for english is {english}")
    
    elif choice == "4":
        # Ask for history score
        history = int(input("Enter your score for history out of 100: "))

        print(f"Your average score for history is {history}")

    elif choice == "5":
        # Average all scores
        average = (math + science + english + history)

        average = (average/4)

        print(f"Your average score for all subjects is {average}")
        
        
    elif choice == "6":
        # Exit
        # Set running to False and display goodbye
        print("Goodbye")
        break
        
    else:
        # Invalid choice
        print("Invalid option. Please try again.")

