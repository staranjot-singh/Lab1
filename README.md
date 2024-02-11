# Lab1
Lab1 repository
def calculate_age():
    try:
        birth_year = int(input("Enter your birth year: "))
        current_year = 2024 
        age = current_year - birth_year
        print("Your age is:", age)
    except ValueError:
        print("Invalid input. Please enter a valid year.")

if __name__ == "__main__":
    calculate_age()
