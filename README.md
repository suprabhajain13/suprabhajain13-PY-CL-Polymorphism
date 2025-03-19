# PY-CL-Polymorphism

## Overview
This project focuses on illustrating polymorphism in Python. It includes a base class `Shape` and its subclasses `Circle` and `Rectangle`, demonstrating polymorphic behavior through method overriding. The project also includes an entry point script (`app.py`) to test the polymorphic behavior of the classes, along with unit tests (`lab_test.py`) to ensure the correctness of the implemented polymorphism.

## Files

### app.py
The `app.py` file serves as the main entry point for the project. It instantiates objects of different shapes (circles and rectangles) and tests their polymorphic behavior by calling the `area()` method.

### lab.py
The `lab.py` file contains the implementation of the `Shape`, `Circle`, and `Rectangle` classes. It demonstrates polymorphism by having the subclasses `Circle` and `Rectangle` override the `area()` method of the base class `Shape`.

### lab_test.py
The `lab_test.py` file contains unit tests for the classes and methods defined in `lab.py`. It ensures that the polymorphic behavior is correctly implemented by testing the `area()` method of different shape objects.

## Project Structure
- src/
  - main/
    - app.py
    - lab.py
  - test/
    - lab_test.py

## Getting Started
1. Open the `src/main/app.py` file.
2. Run the `app.py` file to test the polymorphic behavior of shape objects.
3. Review the code in `lab.py` to understand the implementation of polymorphism through method overriding.

## Testing
1. Open the `src/test/lab_test.py` file.
2. Run the `lab_test.py` file to execute the unit tests.
3. Ensure that all tests pass, confirming the correctness of the polymorphic behavior.

## Conclusion
This project provides practical experience with polymorphism in Python. By exploring the code in `lab.py` and running the tests in `lab_test.py`, users can deepen their understanding of polymorphic behavior and its importance in object-oriented programming.

Happy Coding!
