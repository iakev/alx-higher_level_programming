# SQL Introduction - ALX Higher Level Programming

Welcome to the **0x0D-SQL_introduction** directory of the **ALX Higher Level Programming** repository. In this section, you'll find SQL (Structured Query Language) programs and resources that provide an introduction to working with databases and SQL.

## Table of Contents

- [Description](#description)
- [Program Listings](#program-listings)
- [How to Use](#how-to-use)
- [Contributing](#contributing)
- [License](#license)

## Description

This directory contains SQL programs and resources that introduce you to SQL, a domain-specific language used for managing and querying relational databases. SQL is widely used in web development, data analysis, and many other fields where data manipulation and retrieval are required.

## Program Listings

Below are the SQL programs in this directory:

- [0-list_databases.sql](https://github.com/iakev/alx-higher_level_programming/blob/main/0x0D-SQL_introduction/0-list_databases.sql): This SQL script lists all the databases in the MySQL server.
- [1-create_database_if_missing.sql](https://github.com/iakev/alx-higher_level_programming/blob/main/0x0D-SQL_introduction/1-create_database_if_missing.sql): This SQL script creates a new database only if it doesn't already exist.
- [2-remove_database.sql](https://github.com/iakev/alx-higher_level_programming/blob/main/0x0D-SQL_introduction/2-remove_database.sql): This SQL script removes a database named `hbtn_0c_0`.
- [3-list_tables.sql](https://github.com/iakev/alx-higher_level_programming/blob/main/0x0D-SQL_introduction/3-list_tables.sql): This SQL script lists all the tables in the current database.
- [4-first_table.sql](https://github.com/iakev/alx-higher_level_programming/blob/main/0x0D-SQL_introduction/4-first_table.sql): This SQL script creates a table named `first_table` with specified columns.
- [5-full_table.sql](https://github.com/iakev/alx-higher_level_programming/blob/main/0x0D-SQL_introduction/5-full_table.sql): This SQL script creates a table named `full_table` with specified columns and primary key.
- [6-list_values.sql](https://github.com/iakev/alx-higher_level_programming/blob/main/0x0D-SQL_introduction/6-list_values.sql): This SQL script lists all the values in the table `full_table`.
- [7-insert_value.sql](https://github.com/iakev/alx-higher_level_programming/blob/main/0x0D-SQL_introduction/7-insert_value.sql): This SQL script inserts a new row into a table.
- [8-count_89.sql](https://github.com/iakev/alx-higher_level_programming/blob/main/0x0D-SQL_introduction/8-count_89.sql): This SQL script counts the number of rows with specific conditions.
- [9-full_creation.sql](https://github.com/iakev/alx-higher_level_programming/blob/main/0x0D-SQL_introduction/9-full_creation.sql): This SQL script creates a new table with specified columns and constraints.
- [10-top_score.sql](https://github.com/iakev/alx-higher_level_programming/blob/main/0x0D-SQL_introduction/10-top_score.sql): This SQL script retrieves the top score from a table.
- [11-best_score.sql](https://github.com/iakev/alx-higher_level_programming/blob/main/0x0D-SQL_introduction/11-best_score.sql): This SQL script retrieves the best score from a table.
- [12-no_cheating.sql](https://github.com/iakev/alx-higher_level_programming/blob/main/0x0D-SQL_introduction/12-no_cheating.sql): This SQL script updates records with specific conditions.
- [13-change_class.sql](https://github.com/iakev/alx-higher_level_programming/blob/main/0x0D-SQL_introduction/13-change_class.sql): This SQL script updates records in a table.
- [14-average.sql](https://github.com/iakev/alx-higher_level_programming/blob/main/0x0D-SQL_introduction/14-average.sql): This SQL script calculates the average score from a table.
- [15-groups.sql](https://github.com/iakev/alx-higher_level_programming/blob/main/0x0D-SQL_introduction/15-groups.sql): This SQL script groups records by a specific column.
- [16-no_link.sql](https://github.com/iakev/alx-higher_level_programming/blob/main/0x0D-SQL_introduction/16-no_link.sql): This SQL script retrieves records with specific conditions.
- [100-move_to_utf8.sql](https://github.com/iakev/alx-higher_level_programming/blob/main/0x0D-SQL_introduction/100-move_to_utf8.sql): This SQL script alters a database and its tables to use the UTF-8 character set.
- [101-avg_temperatures.sql](https://github.com/iakev/alx-higher_level_programming/blob/main/0x0D-SQL_introduction/101-avg_temperatures.sql): This SQL script calculates average temperatures from a table.
- [102-top_city.sql](https://github.com/iakev/alx-higher_level_programming/blob/main/0x0D-SQL_introduction/102-top_city.sql): This SQL script retrieves the top city for each state from a table.
- [103-max_state.sql](https://github.com/iakev/alx-higher_level_programming/blob/main/0x0D-SQL_introduction/103-max_state.sql): This SQL script retrieves the maximum state temperature from a table.


## How to Use

To execute the SQL scripts in this directory, you can use a MySQL client or any other tool that supports running SQL commands. Here's an example of how to execute a script using the MySQL command-line client:

```bash
mysql -u username -p < script.sql
```

Replace username with your MySQL username and script.sql with the name of the SQL script you want to run.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
