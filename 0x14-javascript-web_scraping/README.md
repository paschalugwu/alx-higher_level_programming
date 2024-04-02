# Project Title: JavaScript Web Scraping

## Overview

This project is part of the curriculum focusing on JavaScript web scraping. It consists of a series of scripts designed to perform various tasks related to web scraping and API interaction. Each script serves a specific purpose, such as reading and writing files, making HTTP requests, and retrieving data from the Star Wars API. The project emphasizes learning objectives related to JavaScript programming, JSON manipulation, and utilizing modules like request.

## Learning Objectives

Upon completion of this project, you should be able to:

- Understand the basics of JavaScript programming and its application in web scraping.
- Manipulate JSON data and access its attributes.
- Utilize request and fetch APIs for making HTTP requests.
- Read and write files using the fs module.

## Requirements

### General

- Allowed editors: vi, vim, emacs
- Files interpreted on Ubuntu 20.04 LTS using Node.js (version 14.x)
- All files should end with a new line
- The first line of all files should be exactly `#!/usr/bin/node`
- Mandatory README.md file at the root of the project folder
- Code should be semistandard compliant (Standard rules + semicolons)
- All files must be executable
- Avoid using `var` keyword

### Installation Instructions

- Install Node.js 14:
  ```
  $ curl -sL https://deb.nodesource.com/setup_14.x | sudo -E bash -
  $ sudo apt-get install -y nodejs
  ```

- Install semi-standard:
  ```
  $ sudo npm install semistandard --global
  ```

- Install request module:
  ```
  $ sudo npm install request --global
  $ export NODE_PATH=/usr/lib/node_modules
  ```

## Tasks

### 0. Readme
- Script to read and print the content of a file.

### 1. Write me
- Script to write a string to a file.

### 2. Status code
- Script to display the status code of a GET request.

### 3. Star wars movie title
- Script to print the title of a Star Wars movie based on the episode number.

### 4. Star wars Wedge Antilles
- Script to print the number of movies where the character "Wedge Antilles" is present.

### 5. Loripsum
- Script to get the contents of a webpage and store it in a file.

### 6. How many completed?
- Script to compute the number of tasks completed by user id.

### 7. Who was playing in this movie? (Advanced)
- Script to print all characters of a Star Wars movie based on the movie ID.

### 8. Right order (Advanced)
- Script to print all characters of a Star Wars movie based on the movie ID in the correct order.

## Copyright and Plagiarism

- Solutions for the tasks should be developed independently to meet the learning objectives.
- Plagiarism is strictly forbidden and will result in removal from the program.

## Repository Information

- GitHub repository: [alx-higher_level_programming](https://github.com/paschalugwu/alx-higher_level_programming)
- Directory: 0x14-javascript-web_scraping

## License

- Copyright © 2024 ALX, All rights reserved.
