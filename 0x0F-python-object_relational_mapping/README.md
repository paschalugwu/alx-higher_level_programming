# Python Object Relational Mapping

This repository contains scripts and classes for working with databases in Python, particularly focusing on object-relational mapping (ORM) using SQLAlchemy. Below is a summary of the tasks and their corresponding files in this repository.

## Task 0: Get all states

**File:** `0x0F-python-object_relational_mapping/0-select_states.py`

This script retrieves and lists all states from the database `hbtn_0e_0_usa`.

## Task 1: Filter states

**File:** `0x0F-python-object_relational_mapping/1-filter_states.py`

This script filters and lists states whose names start with the letter 'N' from the database `hbtn_0e_0_usa`.

## Task 2: Filter states by user input

**File:** `0x0F-python-object_relational_mapping/2-my_filter_states.py`

This script takes a state name as user input and displays all states matching that name from the database `hbtn_0e_0_usa`.

## Task 3: SQL Injection...

**File:** `0x0F-python-object_relational_mapping/3-my_safe_filter_states.py`

This script is an improved version of Task 2 script, making it safe from SQL injection attacks.

## Task 4: Cities by states

**File:** `0x0F-python-object_relational_mapping/4-cities_by_state.py`

This script lists all cities along with their respective states from the database `hbtn_0e_4_usa`.

## Task 5: All cities by state

**File:** `0x0F-python-object_relational_mapping/5-filter_cities.py`

This script lists all cities of a given state from the database `hbtn_0e_4_usa`.

## Task 6: First state model

**Files:** `0x0F-python-object_relational_mapping/model_state.py`, `0x0F-python-object_relational_mapping/6-model_state.py`

This task involves creating a State class and defining its schema using SQLAlchemy.

## Task 7: All states via SQLAlchemy

**File:** `0x0F-python-object_relational_mapping/7-model_state_fetch_all.py`

This script lists all State objects from the database `hbtn_0e_6_usa` using SQLAlchemy.

## Task 8: First state

**File:** `0x0F-python-object_relational_mapping/8-model_state_fetch_first.py`

This script prints the first State object from the database `hbtn_0e_6_usa`.

## Task 9: Contains 'a'

**File:** `0x0F-python-object_relational_mapping/9-model_state_filter_a.py`

This script lists all State objects containing the letter 'a' from the database `hbtn_0e_6_usa`.

## Task 10: Get a state

**File:** `0x0F-python-object_relational_mapping/10-model_state_my_get.py`

This script prints the State object with the name passed as an argument from the database `hbtn_0e_6_usa`.

## Task 11: Add a new state

**File:** `0x0F-python-object_relational_mapping/11-model_state_insert.py`

This script adds a new State object "Louisiana" to the database `hbtn_0e_6_usa`.

## Task 12: Update a state

**File:** `0x0F-python-object_relational_mapping/12-model_state_update_id_2.py`

This script changes the name of a State object with id 2 to "New Mexico" in the database `hbtn_0e_6_usa`.

## Task 13: Delete states

**File:** `0x0F-python-object_relational_mapping/13-model_state_delete_a.py`

This script deletes all State objects with a name containing the letter 'a' from the database `hbtn_0e_6_usa`.

## Task 14: City relationship

**Files:** `0x0F-python-object_relational_mapping/model_city.py`, `0x0F-python-object_relational_mapping/14-model_city_fetch_by_state.py`

This task involves creating a City class and listing all City objects along with their corresponding State objects.

## Task 15: City relationship

**Files:** `0x0F-python-object_relational_mapping/relationship_city.py`, `0x0F-python-object_relational_mapping/relationship_state.py`, `0x0F-python-object_relational_mapping/100-relationship_states_cities.py`

This task improves the previous task by establishing a relationship between City and State objects.

## Task 16: List relationship

**File:** `0x0F-python-object_relational_mapping/101-relationship_states_cities_list.py`

This script lists all State objects and their corresponding City objects from the database `hbtn_0e_101_usa` while maintaining the relationship between them.

