## Project Title: 0x10. Python - Network #0

### Description:
This project is part of the curriculum for the ALX Software Engineering program. It focuses on Python network programming, specifically covering topics such as HTTP, cURL, HTTP methods, and more. The project includes several Bash and Python scripts designed to interact with web servers, send requests, and process responses.

### Learning Objectives:
Upon completion of this project, you should be able to explain the following concepts without relying on external resources:
- Understanding of URLs and HTTP
- Reading and interpreting URLs
- HTTP request and response structures
- HTTP headers and message bodies
- HTTP request methods and response status codes
- Handling HTTP Cookies
- Making requests using cURL
- Application-level behavior when accessing websites

### Requirements:
- **Allowed Editors:** vi, vim, emacs
- A `README.md` file is mandatory.
- All scripts will be tested on Ubuntu 20.04 LTS.
- Bash scripts must be exactly 3 lines long and include necessary comments.
- All files must be executable and end with a new line.
- Bash scripts must start with `#!/bin/bash`.
- Python scripts should be compatible with Python 3.8.5.
- Python scripts should adhere to PEP8 standards.
- Documentation is mandatory for modules, classes, and functions, including detailed explanations of their purpose.

### Tasks:
1. **cURL body size:**
    - Write a Bash script to display the size of the response body from a given URL.
    - Usage: `./0-body_size.sh 0.0.0.0:5000`

2. **cURL to the end:**
    - Write a Bash script to display the body of a response from a URL with a 200 status code.
    - Usage: `./1-body.sh 0.0.0.0:5000/route_1`

3. **cURL Method:**
    - Write a Bash script to send a DELETE request to a given URL and display the response body.
    - Usage: `./2-delete.sh 0.0.0.0:5000/route_3`

4. **cURL only methods:**
    - Write a Bash script to display all HTTP methods accepted by a server for a given URL.
    - Usage: `./3-methods.sh 0.0.0.0:5000/route_4`

5. **cURL headers:**
    - Write a Bash script to send a GET request with a custom header to a URL and display the response body.
    - Usage: `./4-header.sh 0.0.0.0:5000/route_5`

6. **cURL POST parameters:**
    - Write a Bash script to send a POST request with parameters to a URL and display the response body.
    - Usage: `./5-post_params.sh 0.0.0.0:5000/route_6`

7. **Find a peak:**
    - Write a Python function to find a peak in an unsorted list of integers.
    - Prototype: `def find_peak(list_of_integers)`
    - Complexity: O(log(n)), O(n), O(nlog(n)), or O(n2)

8. **Only status code:**
    - Write a Bash script to display only the status code of a response from a given URL.
    - Usage: `./100-status_code.sh 0.0.0.0:5000`

9. **cURL a JSON file:**
    - Write a Bash script to send a JSON POST request to a URL with data from a file and display the response body.
    - Usage: `./101-post_json.sh 0.0.0.0:5000/route_json my_json_file`

10. **Catch me if you can!:**
    - Write a Bash script to make a request to a URL that causes the server to respond with a specific message.
    - Usage: `./102-catch_me.sh`

### Repository Information:
- **GitHub Repository:** [alx-higher_level_programming](https://github.com/paschalugwu/alx-higher_level_programming)
- **Directory:** 0x10-python-network_0
