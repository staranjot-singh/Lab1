try:
    age = int(input("Enter your age: "))
    print("Your age is:", age)
except TypeError:
    print("Please enter an integer for your age.")
