# 0x0C Python - Almost a Circle

Welcome to the **0x0C Python - Almost a Circle** directory of the **ALX Higher Level Programming** repository. This section contains Python modules, classes, and unit tests related to shapes, geometry, and models.

## Table of Contents

- [Description](#description)
- [Models](#models)
  - [Base](#base)
  - [Rectangle](#rectangle)
  - [Square](#square)
- [Tests](#tests)
- [How to Run Tests](#how-to-run-tests)
- [Contributing](#contributing)
- [License](#license)

## Description

The "Almost a Circle" project is a collection of Python modules and classes that represent geometric shapes like rectangles and squares. It includes unit tests to validate the functionality of these classes.

## Models

### Base

The `Base` class, defined in `base.py`, provides a base class for other geometric shape classes. It includes methods for serialization and deserialization of Python objects to and from JSON files.

### Rectangle

The `Rectangle` class, defined in `rectangle.py`, represents a rectangle shape. It includes methods for calculating the area and perimeter of rectangles, as well as the ability to update dimensions.

### Square

The `Square` class, defined in `square.py`, represents a square shape. It includes methods for calculating the area and perimeter of squares and the ability to update the size of squares.

## How to Use

To use these Python modules and classes, follow these steps:

1. Clone the repository to your local machine:

   ```bash
   git clone https://github.com/iakev/alx-higher_level_programming.git
   ```

2. Navigate to the 0x0C-python-almost_a_circle/models directory:

   ```bash
   cd alx-higher_level_programming/0x0C-python-almost_a_circle/models
   ```

3. You can import the Python modules and classes into your own Python scripts and use them as needed for managing and working with shapes and models.

4. To serialize and deserialize objects to/from JSON files, you can utilize the `Base` class provided in `base.py`.

## Tests

The "tests" directory contains Python unit tests to validate the functionality of the classes and methods defined in the "models" directory.

### Test Descriptions

Below are the Python unit tests in the "tests" directory along with their descriptions:

- [test_base.py](./tests/test_base.py): Test cases for the `Base` class, including serialization and deserialization.
- [test_rectangle.py](./tests/test_rectangle.py): Test cases for the `Rectangle` class, covering area, perimeter, and dimension updates.
- [test_square.py](./tests/test_square.py): Test cases for the `Square` class, including area, perimeter, and size updates.

## How to Run Tests

To run the unit tests in the "tests" directory, follow these steps:

1. Clone the repository to your local machine:

   ```bash
   git clone https://github.com/iakev/alx-higher_level_programming.git
   ```

2. Navigate to the `0x0C-python-almost_a_circle/tests` directory:
  
  ```bash
  cd alx-higher_level_programming/0x0C-python-almost_a_circle/tests
  ```

3. You can run the tests using the `python -m unittest` command followed by the name of the test file:

- To run tests for the `Base` class:

  ```bash
  python -m unittest test_base.py
  ```
- To run tests for the `Rectangle` class:

  ```bash
  python -m unittest test_rectangle.py
  ```
  
- To run tests for the `Square` class:

  ```bash
  python -m unittest test_square.py
  ```

4. The tests will execute, and you'll see the results displayed in the terminal.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
