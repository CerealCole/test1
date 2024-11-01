"""Volume and area of cylinder, with exceptions.
This is the starter version, without exceptions.
The functions return a negative value if the height is negative.

TPRG 2131 Fall 202x Test 1
"""from math import pi

def volume_cylinder(diameter, height):
    """Volume of a cylinder given diameter and height."""
    if height < 0:
        raise ValueError("Height must be a positive value.")
    return pi * (diameter / 2.0) ** 2 * height

def area_cylinder(diameter, height):
    """Surface area of a cylinder given diameter and height."""
    if height < 0:
        raise ValueError("Height must be a positive value.")
    radius = diameter / 2.0
    return 2.0 * pi * radius * (height + radius)

if __name__ == "__main__":
    try:
        while True:
            try:
                dia = float(input("\nDiameter? "))
                high = float(input("Height? "))
                # Using round() to limit the output to 4 decimal places
                print("The volume is", round(volume_cylinder(dia, high), 4))
                print("The area is", round(area_cylinder(dia, high), 4))
            except ValueError as e:
                print(e)  # Print the error message for negative height
    except KeyboardInterrupt:
        print("\nGoodbye")  # Print goodbye message when CTRL-C is pressed
