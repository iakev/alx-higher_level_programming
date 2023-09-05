# 0x0F Python - Object Relational Mapping

Welcome to the **0x0F Python - Object Relational Mapping** directory of the **ALX Higher Level Programming** repository. In this section, you'll find Python scripts that demonstrate Object-Relational Mapping (ORM) techniques using Python and SQL databases.

## Table of Contents

- [Description](#description)
- [Program Descriptions](#program-descriptions)
- [How to Use](#how-to-use)
- [Contributing](#contributing)
- [License](#license)
- [Resources](#resources)

## Description

This repository contains Python scripts and programs that showcase Object-Relational Mapping (ORM) concepts. ORM is a programming technique for converting data between incompatible type systems, such as Python objects and SQL databases. These scripts demonstrate how to use various ORM libraries, such as SQLAlchemy, to interact with databases.

## Program Descriptions

Below are the program files and their descriptions available in this repository:

### [0-select_states.py](https://github.com/iakev/alx-higher_level_programming/blob/main/0x0F-python-object_relational_mapping/0-select_states.py)

This script lists all states from a database.

### [0-select_states.sql](https://github.com/iakev/alx-higher_level_programming/blob/main/0x0F-python-object_relational_mapping/0-select_states.sql)

This SQL script also lists all states from a database.

### [1-filter_states.py](https://github.com/iakev/alx-higher_level_programming/blob/main/0x0F-python-object_relational_mapping/1-filter_states.py)

This script lists states that start with a specific letter.

### [2-my_filter_states.py](https://github.com/iakev/alx-higher_level_programming/blob/main/0x0F-python-object_relational_mapping/2-my_filter_states.py)

This script lists states with a specific name (safe from SQL injection).

### [3-my_safe_filter_states.py](https://github.com/iakev/alx-higher_level_programming/blob/main/0x0F-python-object_relational_mapping/3-my_safe_filter_states.py)

This script lists states with a specific name (safe from SQL injection).

### [4-cities_by_state.py](https://github.com/iakev/alx-higher_level_programming/blob/main/0x0F-python-object_relational_mapping/4-cities_by_state.py)

This script lists all cities with their states.

### [5-filter_cities.py](https://github.com/iakev/alx-higher_level_programming/blob/main/0x0F-python-object_relational_mapping/5-filter_cities.py)

This script lists cities in a specific state.

### [7-model_state_fetch_all.py](https://github.com/iakev/alx-higher_level_programming/blob/main/0x0F-python-object_relational_mapping/7-model_state_fetch_all.py)

This script fetches all states from a database using SQLAlchemy.

### [8-model_state_fetch_first.py](https://github.com/iakev/alx-higher_level_programming/blob/main/0x0F-python-object_relational_mapping/8-model_state_fetch_first.py)

This script fetches the first state from a database using SQLAlchemy.

### [9-model_state_filter_a.py](https://github.com/iakev/alx-higher_level_programming/blob/main/0x0F-python-object_relational_mapping/9-model_state_filter_a.py)

This script lists all states containing the letter 'a' using SQLAlchemy.

### [10-model_state_my_get.py](https://github.com/iakev/alx-higher_level_programming/blob/main/0x0F-python-object_relational_mapping/10-model_state_my_get.py)

This script retrieves a State object by ID using SQLAlchemy.

### [100-relationship_states_cities.py](https://github.com/iakev/alx-higher_level_programming/blob/main/0x0F-python-object_relational_mapping/100-relationship_states_cities.py)

This script defines a relationship between State and City classes using SQLAlchemy.

### [101-relationship_states_cities_list.py](https://github.com/iakev/alx-higher_level_programming/blob/main/0x0F-python-object_relational_mapping/101-relationship_states_cities_list.py)

This script lists all State objects and their associated City objects using SQLAlchemy.

Please refer to the individual program files for detailed information.

## How to Use

To use these programs, follow these steps:

1. Make sure you have Python installed on your system.
2. Install SQLAlchemy by running `pip install SQLAlchemy`.
3. Create a database using MySQL or another compatible database system.
4. Modify the database connection parameters in the script as needed.
5. Run the desired script using `python script_name.py

# Contributing

Contributions to this repository are welcome. If you'd like to contribute, please follow these guidelines:

1. Fork the repository.

2. Create a new branch for your feature or bug fix:

   ```bash
   git checkout -b my-feature
   ```

3. Make your changes and test them thoroughly.

4. Commit your changes with clear descriptions.

5. Push your branch to your fork:

  ```bash
  git push origin my-feature
  ```

6. Create a pull request with a clear description of your changes.

# License

This project is licensed under the MIT License. See the LICENSE file for details.

# Resources

For further information on Object-Relational Mapping (ORM) in Python and related topics, consider exploring the following resources:

- [Python Object-Relational Mapping (ORM)](https://docs.python.org/3/library/sqlite3.html): Official Python documentation on SQLite, a popular database library used in many Python ORM implementations.

- [Python SQLite Tutorial](https://www.sqlitetutorial.net/sqlite-python/): A comprehensive tutorial on using SQLite with Python.

- [SQLAlchemy](https://www.sqlalchemy.org/): A powerful and widely used Python ORM library for working with relational databases.
