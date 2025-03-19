from lab import Circle, Rectangle

def main():
    # Test polymorphic behavior
    shapes = [Circle(5), Rectangle(4, 6)]

    for shape in shapes:
        if isinstance(shape, Circle):
            print(f"Circle area: {shape.area()}")
        elif isinstance(shape, Rectangle):
            print(f"Rectangle area: {shape.area()}")

if __name__ == "__main__":
    main()
