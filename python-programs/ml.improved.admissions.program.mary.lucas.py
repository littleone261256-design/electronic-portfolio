# Mary Lucas
# Improved Admissions Program
# This program asks for student information, validates the inputs,
# and determines whether the student is accepted or rejected.
# The program repeats until the user chooses to stop.

# Constants for admission rules
MIN_GPA = 3.0
MIN_TEST_SCORE_HIGH_GPA = 60
MIN_TEST_SCORE_LOW_GPA = 80

def ask_name(prompt="Enter name: "):
    # Ask for a non-empty name
    while True:
        name = input(prompt).strip()
        if name:
            return name
        print("Invalid input — name cannot be empty.\n")

def ask_float_in_range(prompt, min_exclusive, max_inclusive):
    # Ask for a float within a valid range
    while True:
        raw = input(prompt)
        try:
            value = float(raw)
        except ValueError:
            print("Invalid input — please enter a number.\n")
            continue

        if not (value > min_exclusive and value <= max_inclusive):
            print(f"Out of range — enter a number greater than {min_exclusive} and up to {max_inclusive}.\n")
            continue

        return value

def ask_int_in_range(prompt, min_value, max_value):
    # Ask for an integer within a valid range
    while True:
        raw = input(prompt)
        try:
            value = int(raw)
        except ValueError:
            print("Invalid input — please enter an integer.\n")
            continue

        if value < min_value or value > max_value:
            print(f"Out of range — enter an integer between {min_value} and {max_value}.\n")
            continue

        return value

def main():
    keep_going = "y"

    while keep_going.lower() == "y":
        print("\n--- Admissions Check ---")

        first_name = ask_name("Enter the student's first name: ")
        last_name = ask_name("Enter the student's last name: ")

        # GPA: must be > 0 and <= 5 (some schools use 5.0 scale)
        gpa = ask_float_in_range("Enter the student's GPA (0 < GPA <= 5): ", 0.0, 5.0)

        # Test score: must be between 0 and 100
        test_score = ask_int_in_range("Enter the student's admission test score (0–100): ", 0, 100)

        # Decision logic
        if (gpa >= MIN_GPA and test_score >= MIN_TEST_SCORE_HIGH_GPA) or \
           (gpa < MIN_GPA and test_score >= MIN_TEST_SCORE_LOW_GPA):
            message = "Congratulations, you have been accepted."
        else:
            message = "Sorry, you have been rejected."

        print(f"\nResult for {first_name} {last_name}: {message}")

        keep_going = input("\nEnter another student? (y/n): ")

    print("\nProgram finished.")

main()
