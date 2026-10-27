# Your Calculator Project
# Name: Ben
# Description: This calculator calculates tip cost
# ================================

# Welcome message
print("=" * 40)
print("Welcome to the Tip Calculator!")
print("=" * 40)

# Your code below:

mc = 0 # Meal Cost
tp = 0 # Tip Percentage
td = 0 # Tip Decimal 
tc = 0 # Tip Cost
cc = 0 # Complete/Total Cost

running = True # Code Running
while running:
    print (" ")
    mc = float (input ("How much does the meal cost?"))
    tp = float (input ("What is the tip percentage?"))
    td = tp * 0.01
    tc = mc * td
    cc = tc + mc
    print (f"The tip cost is ${tc:.2f} and your total cost is ${cc:.2f}.")
    print (" ")
    answer = input ("Would you like to continue? (yes/no)").lower ()
    if answer == "no":
        print ("Goodbye!")
        running = False
        # hi ツ
