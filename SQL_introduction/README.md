# SQL - Introduction

## Table of Contents
1. [List databases](#list-databases)
2. [Create a database](#create-a-database)
3. [Delete a database](#delete-a-database)
4. [List tables](#list-tables)
5. [First table](#first-table)
6. [Full description](#full-description)
7. [List all in table](#list-all-in-table)
8. [First add](#first-add)
9. [Count 89](#count-89)
10. [Full creation](#full-creation)
11. [List by best](#list-by-best)
12. [Select the best](#select-the-best)
13. [Cheating is bad](#cheating-is-bad)
14. [Score too low](#score-too-low)
15. [Average](#average)
16. [Number by score](#number-by-score)
17. [Say my name](#say-my-name)

## List databases

### 0-list_databases.sql
Write a script that lists all databases of your MySQL server.

File: [0-list_databases.sql](0-list_databases.sql)

## Create a database

### 1-create_database_if_missing.sql
Write a script that creates the database `hbtn_0c_0` in your MySQL server.
- If the database `hbtn_0c_0` already exists, your script should not fail
- You are not allowed to use the `SELECT` or `SHOW` statements

File: [1-create_database_if_missing.sql](1-create_database_if_missing.sql)

## Delete a database

### 2-remove_database.sql
Write a script that deletes the database `hbtn_0c_0` in your MySQL server.
- If the database `hbtn_0c_0` doesn’t exist, your script should not fail
- You are not allowed to use the `SELECT` or `SHOW` statements

File: [2-remove_database.sql](2-remove_database.sql)

## List tables

### 3-list_tables.sql
Write a script that lists all the tables of a database in your MySQL server.
- The database name will be passed as an argument of the `mysql` command

File: [3-list_tables.sql](3-list_tables.sql)

## First table

### 4-first_table.sql
Write a script that creates a table called `first_table` in the current database in your MySQL server.
- `first_table` description:
  - `id` INT
  - `name` VARCHAR(256)
- The database name will be passed as an argument of the `mysql` command
- If the table `first_table` already exists, your script should not fail
- You are not allowed to use the `SELECT` or `SHOW` statements

File: [4-first_table.sql](4-first_table.sql)

## Full description

### 5-full_table.sql
Write a script that prints the following description of the table `first_table` from the database `hbtn_0c_0` in your MySQL server.
- The database name will be passed as an argument of the `mysql` command
- You are not allowed to use the `DESCRIBE` or `EXPLAIN` statements

File: [5-full_table.sql](5-full_table.sql)

## List all in table

### 6-list_values.sql
Write a script that lists all rows of the table `first_table` from the database `hbtn_0c_0` in your MySQL server.
- All fields should be printed
- The database name will be passed as an argument of the `mysql` command

File: [5-full_table.sql](5-full_table.sql)

## First add

### 7-insert_value.sql
Write a script that inserts a new row in the table `first_table` (database `hbtn_0c_0`) in your MySQL server.
- New row:
  - `id` = 89
  - `name` = Best School
- The database name will be passed as an argument of the `mysql` command

File: [7-insert_value.sql](7-insert_value.sql)

## Count 89

### 8-count_89.sql
Write a script that displays the number of records with `id = 89` in the table `first_table` of the database `hbtn_0c_0` in your MySQL server.
- The database name will be passed as an argument of the `mysql` command

File: [8-count_89.sql](8-count_89.sql)

## Full creation

### 9-full_creation.sql
Write a script that creates a table `second_table` in the database `hbtn_0c_0` in your MySQL server and add multiples rows.
- `second_table` description:
  - `id` INT
  - `name` VARCHAR(256)
  - `score` INT
- The database name will be passed as an argument to the `mysql` command
- If the table `second_table` already exists, your script should not fail
- You are not allowed to use the `SELECT` and `SHOW` statements
- Your script should create these records:
  - `id` = 1, `name` = “John”, `score` = 10
  - `id` = 2, `name` = “Alex”, `score` = 3
  - `id` = 3, `name` = “Bob”, `score` = 14
  - `id` = 4, `name` = “George”, `score` = 8

File: [9-full_creation.sql](9-full_creation.sql)

## List by best

### 10-top_score.sql
Write a script that lists all records of the table `second_table` of the database `hbtn_0c_0` in your MySQL server.
- Results should display both the score and the name (in this order)
- Records should be ordered by score (top first)
- The database name will be passed as an argument of the `mysql` command

File: [10-top_score.sql](10-top_score.sql)

## Select the best

### 11-best_score.sql
Write a script that lists all records with a score >= 10 in the table `second_table` of the database `hbtn_0c_0` in your MySQL server.
- Results should display both the score and the name (in this order)
- Records should be ordered by score (top first)
- The database name will be passed as an argument of the `mysql` command

File: [11-best_score.sql](11-best_score.sql)

## Cheating is bad

### 12-no_cheating.sql
Write a script that updates the score of Bob to 10 in the table `second_table`.
- You are not allowed to use Bob’s id value, only the name field
- The database name will be passed as an argument of the `mysql` command

File: [12-no_cheating.sql](12-no_cheating.sql)

## Score too low

### 13-change_class.sql
Write a script that removes all records with a score <= 5 in the table `second_table` of the database `hbtn_0c_0` in your MySQL server.
- The database name will be passed as an argument of the `mysql` command

File: [13-change_class.sql](13-change_class.sql)

## Average

### 14-average.sql
Write a script that computes the score average of all records in the table `second_table` of the database `hbtn_0c_0` in your MySQL server.
- The result column name should be `average`
- The database name will be passed as an argument of the `mysql` command

File: [14-average.sql](14-average.sql)

## Number by score

### 15-groups.sql
Write a script that lists the number of records with the same score in the table `second_table` of the database `hbtn_0c_0` in your MySQL server.
- The result should display:
  - The `score`
  - The number of records for this score with the label `number`
- The list should be sorted by the number of records (descending)
- The database name will be passed as an argument to the `mysql` command

File: [15-groups.sql](15-groups.sql)

## Say my name

### 16-no_link.sql
Write a script that lists all records of the table `second_table` of the database `hbtn_0c_0` in your MySQL server.
- Don’t list rows without a name value
- Results should display the `score` and the `name` (in this order)
- Records should be listed by descending score
- The database name will be passed as an argument to the `mysql` command

File: [16-no_link.sql](16-no_link.sql)
