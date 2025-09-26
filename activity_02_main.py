"""A client program written to verify correctness of the activity classes."""

__author__ = "ACE Faculty"
__version__ = "1.0.0"
__credits__ = ""

from shape import Triangle, Rectangle, Shape  # thanks to __init__.py we can import all at once

def main():
    """Test the functionality of the methods encapsulated in this project."""

    print("*************PART 1****************")

    # 1. Create an empty list of Shape objects
    shapes = []

    # 2. Create instances of Triangle and Rectangle and append to the list
    for creation in [
        ("Triangle", Triangle, ("red", 3, 4, 5)),
        ("Rectangle", Rectangle, ("blue", 5, 3)),
        ("Triangle", Triangle, ("green", 6, 7, 8)),
        ("Rectangle", Rectangle, ("yellow", 10, 2)),
        ("Triangle", Triangle, ("purple", 5, 5, 6)),
    ]:
        shape_name, cls, args = creation
        try:
            obj = cls(*args)
            shapes.append(obj)
        except Exception as e:
            print(f"{shape_name} creation error:", e)

    # 3. Iterate through the list of shapes
    for shape in shapes:
        try:
            print(shape)  # uses __str__
            print(f"Area: {shape.calculate_area():.2f}")
            print(f"Perimeter: {shape.calculate_perimeter():.2f}")
            print("-" * 40)
        except Exception as e:
            print("Error working with shape:", e)

if __name__ == "__main__":
    main()
