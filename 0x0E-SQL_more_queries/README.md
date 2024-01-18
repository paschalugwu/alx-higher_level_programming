# Project Title: SQL - More queries

## Table of Contents
- [Description](#description)
- [Files](#files)
- [Requirements](#requirements)
- [Usage](#usage)
- [Installation](#installation)
- [Credits](#credits)

## Description
This project, "SQL - More queries," is part of the ALX Higher Level Programming curriculum. The main focus of this project is to reinforce SQL concepts and skills. The tasks involve creating and managing MySQL users, databases, and tables, as well as executing various SQL queries to retrieve and manipulate data.

## Files
1. **0-privileges.sql**
   - Task: Write a script that lists all privileges of the MySQL users user_0d_1 and user_0d_2 on your server (in localhost).

2. **1-create_user.sql**
   - Task: Write a script that creates the MySQL server user user_0d_1.

3. **2-create_read_user.sql**
   - Task: Write a script that creates the database hbtn_0d_2 and the user user_0d_2.

4. **3-force_name.sql**
   - Task: Write a script that creates the table force_name on your MySQL server.

5. **4-never_empty.sql**
   - Task: Write a script that creates the table id_not_null on your MySQL server.

6. **5-unique_id.sql**
   - Task: Write a script that creates the table unique_id on your MySQL server.

7. **6-states.sql**
   - Task: Write a script that creates the database hbtn_0d_usa and the table states on your MySQL server.

8. **7-cities.sql**
   - Task: Write a script that creates the database hbtn_0d_usa and the table cities on your MySQL server.

9. **8-cities_of_california_subquery.sql**
   - Task: Write a script that lists all the cities of California that can be found in the database hbtn_0d_usa.

10. **9-cities_by_state_join.sql**
    - Task: Write a script that lists all cities contained in the database hbtn_0d_usa.

11. **10-genre_id_by_show.sql**
    - Task: Write a script that lists all shows contained in hbtn_0d_tvshows that have at least one genre linked.

12. **11-genre_id_all_shows.sql**
    - Task: Write a script that lists all shows contained in the database hbtn_0d_tvshows.

13. **12-no_genre.sql**
    - Task: Write a script that lists all shows contained in hbtn_0d_tvshows without a genre linked.

14. **13-count_shows_by_genre.sql**
    - Task: Write a script that lists all genres from hbtn_0d_tvshows and displays the number of shows linked to each.

15. **14-my_genres.sql**
    - Task: Write a script that uses the hbtn_0d_tvshows database to lists all genres of the show Dexter.

16. **15-comedy_only.sql**
    - Task: Write a script that lists all Comedy shows in the database hbtn_0d_tvshows.

17. **16-shows_by_genre.sql**
    - Task: Write a script that lists all shows, and all genres linked to that show, from the database hbtn_0d_tvshows.

18. **17-not_my_genre.sql**
    - Task (Advanced): Write a script that uses the hbtn_0d_tvshows database to list all genres not linked to the show Dexter.

## Requirements
- Allowed editors: vi, vim, emacs
- Files executed on Ubuntu 20.04 LTS using MySQL 8.0 (version 8.0.25)
- All files should end with a new line
- All SQL queries should have a comment just before (i.e. syntax above)
- All files should start with a comment describing the task
- All SQL keywords should be in uppercase (SELECT, WHERE, etc.)
- A README.md file at the root of the project folder is mandatory
- The length of your files will be tested using wc

## Usage
To run the scripts, follow the instructions provided in each task description. Generally, you will need to execute the SQL files on a MySQL server. Make sure you have the appropriate permissions and access to the MySQL server.

## Installation
To install MySQL 8.0 on Ubuntu 20.04 LTS:

```bash
$ sudo apt update
$ sudo apt install mysql-server
...
$ mysql --version
mysql  Ver 8.0.25-0ubuntu0.20.04.1 for Linux on x86_64 ((Ubuntu))
$ sudo mysql
Welcome to the MySQL monitor.  Commands end with ; or \g.
Your MySQL connection id is 11
Server version: 8.0.25-0ubuntu0.20.04.1 (Ubuntu)
...
mysql> quit
Bye
```

For running in a container, use "container-on

-demand" to set up a MySQL container:

```bash
$ docker run -d -e MYSQL_ROOT_PASSWORD=root -e MYSQL_DATABASE=test -p 3306:3306 --name=mysql_container mysql:8.0
```

## Credits
This project is part of the ALX Higher Level Programming curriculum. The tasks were designed by the ALX team.
