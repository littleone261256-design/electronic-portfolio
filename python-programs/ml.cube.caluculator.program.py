# Mary Lucas
# Cube Calculator Program
# This program asks the user for the length, width, and height of a cube.
# It calculates the volume and surface area using functions.
# The program repeats until the user decides to quit.


def get_positive_float(prompt):
    # Ask the user for a positive number and keep asking until they enter one
    value = float(input(prompt))
    while value <= 0:
        print("Error: please enter a positive number.")
        value = float(input(prompt))
    return value

def calc_volume(length, width, height):
    # Volume formula
    return length * width * height

def calc_surface_area(length, width, height):
    # Surface area formula for a rectangular cube
    return 2 * (length * width + length * height + width * height)

def main():
    keep_going = "y"

    while keep_going.lower() == "y":
        print("\nCube Calculator")

        length = get_positive_float("Enter length: ")
        width = get_positive_float("Enter width: ")
        height = get_positive_float("Enter height: ")

        volume = calc_volume(length, width, height)
        surface_area = calc_surface_area(length, width, height)

        print("\nResults:")
        print("Volume:", volume)
        print("Surface Area:", surface_area)

        keep_going = input("\nWould you like to run the program again? (y/n): ")

    print("\nThanks for using the program.")

main()

