# Python - Object-relational mapping

## Table of Contents
1. [Get all states](#get-all-states)
2. [Filter states](#filter-states)
3. [Filter states by user input](#filter-states-by-user-input)
4. [SQL Injection...](#sql-injection)
5. [Cities by states](#cities-by-states)
6. [All cities by state](#all-cities-by-state)
7. [First state model](#first-state-model)
8. [All states via SQLAlchemy](#all-states-via-sqlalchemy)
9. [First state](#first-state)
10. [Contains `a`](#contains-a)
11. [Get a state](#get-a-state)
12. [Add a new state](#add-a-new-state)
13. [Update a state](#update-a-state)
14. [Delete states](#delete-states)
15. [Cities in state](#cities-in-state)

## Get all states

### 0-select_states.py
Write a script that lists all states from the database `hbtn_0e_0_usa`:

- Your script should take 3 arguments: mysql username, mysql password, and database name (no argument validation needed)
- You must use the module `MySQLdb` (import `MySQLdb`)
- Your script should connect to a MySQL server running on `localhost` at port `3306`
- Results must be sorted in ascending order by `states.id`
- Results must be displayed as they are in the example below
- Your code should not be executed when imported

File: [0-select_states.py](0-select_states.py)

## Filter states

### 1-filter_states.py
Write a script that lists all states with a name starting with N (upper N) from the database `hbtn_0e_0_usa`:

- Your script should take 3 arguments: mysql username, mysql password, and database name (no argument validation needed)
- You must use the module `MySQLdb` (import `MySQLdb`)
- Your script should connect to a MySQL server running on `localhost` at port `3306`
- Results must be sorted in ascending order by `states.id`
- Results must be displayed as they are in the example below
- Your code should not be executed when imported

File: [1-filter_states.py](1-filter_states.py)

## Filter states by user input

### 2-my_filter_states.py
Write a script that takes in an argument and displays all values in the `states` table of `hbtn_0e_0_usa` where `name` matches the argument.

- Your script should take 4 arguments: mysql username, mysql password, database name, and state name searched (no argument validation needed)
- You must use the module `MySQLdb` (import `MySQLdb`)
- Your script should connect to a MySQL server running on `localhost` at port `3306`
- You must use `format` to create the SQL query with the user input
- Results must be sorted in ascending order by `states.id`
- Results must be displayed as they are in the example below
- Your code should not be executed when imported

File: [2-my_filter_states.py](2-my_filter_states.py)

## SQL Injection...

### 3-my_safe_filter_states.py
Write a script that takes in arguments and displays all values in the `states` table of `hbtn_0e_0_usa` where `name` matches the argument. But this time, write one that is safe from MySQL injections!

- Your script should take 4 arguments: mysql username, mysql password, database name, and state name searched (safe from MySQL injection)
- You must use the module `MySQLdb` (import `MySQLdb`)
- Your script should connect to a MySQL server running on `localhost` at port `3306`
- Results must be sorted in ascending order by `states.id`
- Results must be displayed as they are in the example below
- Your code should not be executed when imported

File: [3-my_safe_filter_states.py](3-my_safe_filter_states.py)

## Cities by states

### 4-cities_by_state.py
Write a script that lists all cities from the database `hbtn_0e_4_usa`.

- Your script should take 3 arguments: mysql username, mysql password, and database name
- You must use the module `MySQLdb` (import `MySQLdb`)
- Your script should connect to a MySQL server running on `localhost` at port `3306`
- Results must be sorted in ascending order by `cities.id`
- You can use only `execute()` once
- Results must be displayed as they are in the example below
- Your code should not be executed when imported

File: [4-cities_by_state.py](4-cities_by_state.py)

## All cities by state

### 5-filter_cities.py
Write a script that takes in the name of a state as an argument and lists all cities of that state, using the database `hbtn_0e_4_usa`.

- Your script should take 4 arguments: mysql username, mysql password, database name, and state name (SQL injection free!)
- You must use the module `MySQLdb` (import `MySQLdb`)
- Your script should connect to a MySQL server running on `localhost` at port `3306`
- Results must be sorted in ascending order by `cities.id`
- You can use only `execute()` once
- The results must be displayed as they are in the example below
- Your code should not be executed when imported

File: [5-filter_cities.py](5-filter_cities.py)

## First state model

### model_state.py
Write a python file that contains the class definition of a `State` and an instance `Base = declarative_base()`:

- `State` class:
  - Inherits from `Base`
  - Links to the MySQL table `states`
  - Class attribute `id` that represents a column of an auto-generated, unique integer, can’t be null and is a primary key
  - Class attribute `name` that represents a column of a string with maximum 128 characters and can’t be null
- You must use the module `SQLAlchemy`
- Your script should connect to a MySQL server running on `localhost` at port `3306`
- **WARNING:** All classes who inherit from `Base` must be imported before calling `Base.metadata.create_all(engine)`

File: [model_state.py](model_state.py)

## All states via SQLAlchemy

### 7-model_state_fetch_all.py
Write a script that lists all `State` objects from the database `hbtn_0e_6_usa`.

- Your script should take 3 arguments: mysql username, mysql password, and database name
- You must use the module `SQLAlchemy`
- You must import `State` and `Base` from `model_state` - `from model_state import Base, State`
- Your script should connect to a MySQL server running on `localhost` at port `3306`
- Results must be sorted in ascending order by `states.id`
- The results must be displayed as they are in the example below
- Your code should not be executed when imported

File: [7-model_state_fetch_all.py](7-model_state_fetch_all.py)

## First state

### 8-model_state_fetch_first.py
Write a script that prints the first `State` object from the database `hbtn_0e_6_usa`.

- Your script should take 3 arguments: mysql username, mysql password, and database name
- You must use the module `SQLAlchemy`
- You must import `State` and `Base` from `model_state` - `from model_state import Base, State`
- Your script should connect to a MySQL server running on `localhost` at port `3306`
- The state you display must be the first in `states.id`
- You are not allowed to fetch all states from the database before displaying the result
- The results must be displayed as they are in the example below
- If the table `states` is empty, print `Nothing` followed by a new line
- Your code should not be executed when imported

File: [8-model_state_fetch_first.py](8-model_state_fetch_first.py)

## Contains `a`

### 9-model_state_filter_a.py
Write a script that lists all `State` objects that contain the letter `a` from the database `hbtn_0e_6_usa`.

- Your script should take 3 arguments: mysql username, mysql password, and database name
- You must use the module `SQLAlchemy`
- You must import `State` and `Base` from `model_state` - `from model_state import Base, State`
- Your script should connect to a MySQL server running on `localhost` at port `3306`
- Results must be sorted in ascending order by `states.id`
- The results must be displayed as they are in the example below
- Your code should not be executed when imported

File: [9-model_state_filter_a.py](9-model_state_filter_a.py)

## Get a state

### 10-model_state_my_get.py
Write a script that prints the `State` object with the name passed as an argument from the database `hbtn_0e_6_usa`.

- Your script should take 4 arguments: mysql username, mysql password, database name, and state name to search (SQL injection free)
- You must use the module `SQLAlchemy`
- You must import `State` and `Base` from `model_state` - `from model_state import Base, State`
- Your script should connect to a MySQL server running on `localhost` at port `3306`
- You can assume you have one record with the state name to search
- Results must display the `states.id`
- If no state has the name you searched for, display `Not found`
- Your code should not be executed when imported

File: [10-model_state_my_get.py](10-model_state_my_get.py)

## Add a new state

### 11-model_state_insert.py
Write a script that adds the `State` object “Louisiana” to the database `hbtn_0e_6_usa`.

- Your script should take 3 arguments: mysql username, mysql password, and database name
- You must use the module `SQLAlchemy`
- You must import `State` and `Base` from `model_state` - `from model_state import Base, State`
- Your script should connect to a MySQL server running on `localhost` at port `3306`
- Print the new `states.id` after creation
- Your code should not be executed when imported

File: [11-model_state_insert.py](11-model_state_insert.py)

## Update a state

### 12-model_state_update_id_2.py
Write a script that changes the name of a `State` object from the database `hbtn_0e_6_usa`.

- Your script should take 3 arguments: mysql username, mysql password, and database name
- You must use the module `SQLAlchemy`
- You must import `State` and `Base` from `model_state` - `from model_state import Base, State`
- Your script should connect to a MySQL server running on `localhost` at port `3306`
- Change the name of the `State` where `id = 2` to `New Mexico`
- Your code should not be executed when imported

File: [12-model_state_update_id_2.py](12-model_state_update_id_2.py)

## Delete states

### 13-model_state_delete_a.py
Write a script that deletes all `State` objects with a name containing the letter `a` from the database `hbtn_0e_6_usa`.

- Your script should take 3 arguments: mysql username, mysql password, and database name
- You must use the module `SQLAlchemy`
- You must import `State` and `Base` from `model_state` - `from model_state import Base, State`
- Your script should connect to a MySQL server running on `localhost` at port `3306`
- Your code should not be executed when imported

File: [13-model_state_delete_a.py](13-model_state_delete_a.py)

## Cities in state

### model_city.py
Write a Python file similar to `model_state.py` named `model_city.py` that contains the class definition of a `City`.

- `City` class:
  - Inherits from `Base` (imported from `model_state`)
  - Links to the MySQL table `cities`
  - Class attribute `id` that represents a column of an auto-generated, unique integer, can’t be null and is a primary key
  - Class attribute `name` that represents a column of a string of 128 characters and can’t be null
  - Class attribute `state_id` that represents a column of an integer, can’t be null and is a foreign key to `states.id`
- You must use the module `SQLAlchemy`

File: [model_city.py](model_city.py)

### 14-model_city_fetch_by_state.py
Write a script that prints all `City` objects from the database `hbtn_0e_14_usa`.

- Your script should take 3 arguments: mysql username, mysql password, and database name
- You must use the module `SQLAlchemy`
- You must import `State` and `Base` from `model_state` - `from model_state import Base, State`
- Your script should connect to a MySQL server running on `localhost` at port `3306`
- Results must be sorted in ascending order by `cities.id`
- Results must be displayed as they are in the example below (`<state name>: (<city id>) <city name>`)
- Your code should not be executed when imported

File: [14-model_city_fetch_by_state.py](14-model_city_fetch_by_state.py)
