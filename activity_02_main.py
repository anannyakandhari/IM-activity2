"""A client program written to verify correctness of the activity classes.
"""

__author__ = "ACE Faculty"
__version__ = "1.0.0"
__credits__ = ""

from shape import Triangle, Rectangle, Shape  # thanks to __init__.py we can import all at once

def main():
    """Test the functionality of the methods encapsulated in this project.
    """

    # In the statements coded below, ensure that any statement that 
    # could result in an exception is handled.  
    # When exceptions are 'caught', display the exception message to the console.

    # *** PART 1 ***
    print("*************PART 1****************")

    # 1. Create an empty list of Shape objects.
    shapes = []

    # 2. Create an instance of the Triangle class and append to the list.
    try:
        t1 = Triangle("red", 3, 4, 5)
        shapes.append(t1)
    except Exception as e:
        print("Triangle creation error:", e)

    # 3. Create an instance of the Rectangle class and append to the list.
    try:
        r1 = Rectangle("blue", 5, 3)
        shapes.append(r1)
    except Exception as e:
        print("Rectangle creation error:", e)

    # 4. Create 3 additional instances of Triangle or Rectangle.
    try:
        t2 = Triangle("green", 6, 7, 8)
        shapes.append(t2)
    except Exception as e:
        print("Triangle creation error:", e)

    try:
        r2 = Rectangle("yellow", 10, 2)
        shapes.append(r2)
    except Exception as e:
        print("Rectangle creation error:", e)

    try:
        t3 = Triangle("purple", 5, 5, 6)
        shapes.append(t3)
    except Exception as e:
        print("Triangle creation error:", e)

    # 5. Iterate through the list of shapes.
    for shape in shapes:
        try:
            print(shape)  # uses __str__
            print(f"Area: {shape.calculate_area():.2f}")
            print(f"Perimeter: {shape.calculate_perimeter():.2f}")
            print("-" * 40)
        except Exception as e:
            print("Error working with shape:", e)

    # *** END PART 1 ***


if __name__ == "__main__":
    main()
