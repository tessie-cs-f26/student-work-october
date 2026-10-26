# Hello Counter
# A small sample program: it uses input(), a while loop, and an if statement.

name = input("What is your name? ")
print("Hello, " + name + "!")

count = 0
while count < 3:
    count = count + 1
    print("Counting: " + str(count))

answer = input("Do you like Python? (yes/no) ")
if answer == "yes":
    print("Great, keep coding!")
else:
    print("Give it another try. It gets easier.")
