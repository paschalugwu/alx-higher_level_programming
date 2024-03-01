# Project README

## Curriculum - SE Foundations Average: 149.05%

Welcome to the Python Networking Project (0x11) - Network #1!

### Project Overview

- **Project Name:** PythonScriptingBack-endAPI
- **By:** Guillaume, CTO at Holberton School
- **Weight:** 1
- **Project Start:** Mar 1, 2024 6:00 AM
- **Project End:** Mar 2, 2024 6:00 AM
- **Checker Release:** Mar 1, 2024 12:00 PM
- **Auto Review:** Will be launched at the deadline

### Learning Objectives

By the end of this project, you will be able to:

- Explain how to fetch internet resources with the Python package urllib.
- Decode urllib body response.
- Use the Python package requests for making HTTP requests.
- Make HTTP GET, POST, PUT, etc. requests.
- Fetch JSON resources and manipulate data from an external service.

### Copyright - Plagiarism

- You are expected to come up with solutions for the tasks independently.
- Plagiarism is strictly forbidden and will result in removal from the program.
- Do not publish any content from this project.

### Requirements

#### General

- **Allowed Editors:** vi, vim, emacs
- **Interpreted/Compiled on:** Ubuntu 20.04 LTS using Python3 (version 3.8.5)
- **File Endings:** All files should end with a new line.
- **First Line:** The first line of all your files should be exactly `#!/usr/bin/python3`.
- **README:** A README.md file at the root of the repo is mandatory.
- **Code Style:** Your code should use pycodestyle (version 2.8.*).
- **File Execution:** All your files must be executable.
- **File Length:** The length of your files will be tested using wc.
- **Module Documentation:** All your modules should have documentation (python3 -c 'print(__import__("my_module").__doc__)').
- **Dictionary Access:** Use `get` to access dictionary values by key.
- **Documentation:** A documentation is not a simple word; it’s a real sentence explaining the purpose of the module, class, or method.
- **Code Execution:** Your code should not be executed when imported (by using `if __name__ == "__main__":`).

### Tasks

#### 0. What's my status? #0

**Objective:** Fetch the status from https://alx-intranet.hbtn.io/status using the urllib package.

```bash
./0-hbtn_status.py | cat -e
```

**Repo:**
- [alx-higher_level_programming/0x11-python-network_1/0-hbtn_status.py](https://github.com/paschalugwu/alx-higher_level_programming/blob/main/0x11-python-network_1/0-hbtn_status.py)

#### 1. Response header value #0

**Objective:** Send a request to a given URL and display the value of the X-Request-Id variable from the header.

```bash
./1-hbtn_header.py https://alx-intranet.hbtn.io
```

**Repo:**
- [alx-higher_level_programming/0x11-python-network_1/1-hbtn_header.py](https://github.com/paschalugwu/alx-higher_level_programming/blob/main/0x11-python-network_1/1-hbtn_header.py)

#### 2. POST an email #0

**Objective:** Send a POST request with an email parameter to a given URL and display the body of the response.

```bash
./2-post_email.py http://0.0.0.0:5000/post_email hr@holbertonschool.com
```

**Repo:**
- [alx-higher_level_programming/0x11-python-network_1/2-post_email.py](https://github.com/paschalugwu/alx-higher_level_programming/blob/main/0x11-python-network_1/2-post_email.py)

#### 3. Error code #0

**Objective:** Handle urllib.error.HTTPError exceptions and print the HTTP status code.

```bash
./3-error_code.py http://0.0.0.0:5000
./3-error_code.py http://0.0.0.0:5000/status_401
./3-error_code.py http://0.0.0.0:5000/doesnt_exist
./3-error_code.py http://0.0.0.0:5000/status_500
```

**Repo:**
- [alx-higher_level_programming/0x11-python-network_1/3-error_code.py](https://github.com/paschalugwu/alx-higher_level_programming/blob/main/0x11-python-network_1/3-error_code.py)

#### 4. What's my status? #1

**Objective:** Fetch the status from https://alx-intranet.hbtn.io/status using the requests package.

```bash
./4-hbtn_status.py | cat -e
```

**Repo:**
- [alx-higher_level_programming/0x11-python-network_1/4-hbtn_status.py](https://github.com/paschalugwu/alx-higher_level_programming/blob/main/0x11-python-network_1/4-hbtn_status.py)

#### 5. Response header value #1

**Objective:** Send a request to a given URL and display the value of the X-Request-Id variable from the header using the requests package.

```bash
./5-hbtn_header.py https://alx-intranet.hbtn.io
```

**Repo:**
- [alx-higher_level_programming/0x11-python-network_1/5-hbtn_header.py](https://github.com/paschalugwu/alx-higher_level_programming/blob/main/0x11-python-network_1/5-hbtn_header.py)

#### 6. POST an email #1

**Objective:** Send a POST request with an email parameter to a given URL and display the body of the response using the requests package.

```bash
./6-post_email.py http://0.0.0.0:5000/post_email hr@holbertonschool.com
```

**Repo:**
- [alx-higher_level_programming/0x11-python-network_1/6-post_email.py](https://github.com/paschalugwu/alx-higher_level_programming/blob/main/0x11-python-network_1/6-post_email.py)

#### 7. Error code #1

**Objective:** Send a request to a given URL and display the body of the response. If the HTTP status code is greater than or equal to 400, print an error message.

```bash
./7-error_code.py http://0.0.0.0:5000
./7-error_code.py http://0.0.0.0:5000/status_401
./7-error_code.py http://0.0.0.0:5000/doesnt_exist
./7-error_code.py http://0.0.0.0:5000/status_500
```

**Repo:**
- [alx-higher_level_programming/0x11-python

-network_1/7-error_code.py](https://github.com/paschalugwu/alx-higher_level_programming/blob/main/0x11-python-network_1/7-error_code.py)

#### 8. Search API

**Objective:** Send a POST request with a letter parameter to http://0.0.0.0:5000/search_user and display the response.

```bash
./8-json_api.py
./8-json_api.py a
./8-json_api.py 2
./8-json_api.py b
```

**Repo:**
- [alx-higher_level_programming/0x11-python-network_1/8-json_api.py](https://github.com/paschalugwu/alx-higher_level_programming/blob/main/0x11-python-network_1/8-json_api.py)

#### 9. My GitHub!

**Objective:** Use the GitHub API to display your GitHub id using Basic Authentication.

```bash
./10-my_github.py papamuziko cisfun
./10-my_github.py papamuziko wrong_pwd
```

**Repo:**
- [alx-higher_level_programming/0x11-python-network_1/10-my_github.py](https://github.com/paschalugwu/alx-higher_level_programming/blob/main/0x11-python-network_1/10-my_github.py)

#### 10. Time for an interview! (Advanced)

**Objective:** List 10 commits (from most recent to oldest) of the repository “rails” by the user “rails” using the GitHub API.

```bash
./100-github_commits.py rails rails
```

**Repo:**
# Project README

## Curriculum - SE Foundations Average: 149.05%

Welcome to the Python Networking Project (0x11) - Network #1!

### Project Overview

- **Project Name:** PythonScriptingBack-endAPI
- **By:** Guillaume, CTO at Holberton School
- **Weight:** 1
- **Project Start:** Mar 1, 2024 6:00 AM
- **Project End:** Mar 2, 2024 6:00 AM
- **Checker Release:** Mar 1, 2024 12:00 PM
- **Auto Review:** Will be launched at the deadline

### Learning Objectives

By the end of this project, you will be able to:

- Explain how to fetch internet resources with the Python package urllib.
- Decode urllib body response.
- Use the Python package requests for making HTTP requests.
- Make HTTP GET, POST, PUT, etc. requests.
- Fetch JSON resources and manipulate data from an external service.

### Copyright - Plagiarism

- You are expected to come up with solutions for the tasks independently.
- Plagiarism is strictly forbidden and will result in removal from the program.
- Do not publish any content from this project.

### Requirements

#### General

- **Allowed Editors:** vi, vim, emacs
- **Interpreted/Compiled on:** Ubuntu 20.04 LTS using Python3 (version 3.8.5)
- **File Endings:** All files should end with a new line.
- **First Line:** The first line of all your files should be exactly `#!/usr/bin/python3`.
- **README:** A README.md file at the root of the repo is mandatory.
- **Code Style:** Your code should use pycodestyle (version 2.8.*).
- **File Execution:** All your files must be executable.
- **File Length:** The length of your files will be tested using wc.
- **Module Documentation:** All your modules should have documentation (python3 -c 'print(__import__("my_module").__doc__)').
- **Dictionary Access:** Use `get` to access dictionary values by key.
- **Documentation:** A documentation is not a simple word; it’s a real sentence explaining the purpose of the module, class, or method.
- **Code Execution:** Your code should not be executed when imported (by using `if __name__ == "__main__":`).

### Tasks

#### 0. What's my status? #0

**Objective:** Fetch the status from https://alx-intranet.hbtn.io/status using the urllib package.

```bash
./0-hbtn_status.py | cat -e
```

**Repo:**
- [alx-higher_level_programming/0x11-python-network_1/0-hbtn_status.py](https://github.com/paschalugwu/alx-higher_level_programming/blob/main/0x11-python-network_1/0-hbtn_status.py)

#### 1. Response header value #0

**Objective:** Send a request to a given URL and display the value of the X-Request-Id variable from the header.

```bash
./1-hbtn_header.py https://alx-intranet.hbtn.io
```

**Repo:**
- [alx-higher_level_programming/0x11-python-network_1/1-hbtn_header.py](https://github.com/paschalugwu/alx-higher_level_programming/blob/main/0x11-python-network_1/1-hbtn_header.py)

#### 2. POST an email #0

**Objective:** Send a POST request with an email parameter to a given URL and display the body of the response.

```bash
./2-post_email.py http://0.0.0.0:5000/post_email hr@holbertonschool.com
```

**Repo:**
- [alx-higher_level_programming/0x11-python-network_1/2-post_email.py](https://github.com/paschalugwu/alx-higher_level_programming/blob/main/0x11-python-network_1/2-post_email.py)

#### 3. Error code #0

**Objective:** Handle urllib.error.HTTPError exceptions and print the HTTP status code.

```bash
./3-error_code.py http://0.0.0.0:5000
./3-error_code.py http://0.0.0.0:5000/status_401
./3-error_code.py http://0.0.0.0:5000/doesnt_exist
./3-error_code.py http://0.0.0.0:5000/status_500
```

**Repo:**
- [alx-higher_level_programming/0x11-python-network_1/3-error_code.py](https://github.com/paschalugwu/alx-higher_level_programming/blob/main/0x11-python-network_1/3-error_code.py)

#### 4. What's my status? #1

**Objective:** Fetch the status from https://alx-intranet.hbtn.io/status using the requests package.

```bash
./4-hbtn_status.py | cat -e
```

**Repo:**
- [alx-higher_level_programming/0x11-python-network_1/4-hbtn_status.py](https://github.com/paschalugwu/alx-higher_level_programming/blob/main/0x11-python-network_1/4-hbtn_status.py)

#### 5. Response header value #1

**Objective:** Send a request to a given URL and display the value of the X-Request-Id variable from the header using the requests package.

```bash
./5-hbtn_header.py https://alx-intranet.hbtn.io
```

**Repo:**
- [alx-higher_level_programming/0x11-python-network_1/5-hbtn_header.py](https://github.com/paschalugwu/alx-higher_level_programming/blob/main/0x11-python-network_1/5-hbtn_header.py)

#### 6. POST an email #1

**Objective:** Send a POST request with an email parameter to a given URL and display the body of the response using the requests package.

```bash
./6-post_email.py http://0.0.0.0:5000/post_email hr@holbertonschool.com
```

**Repo:**
- [alx-higher_level_programming/0x11-python-network_1/6-post_email.py](https://github.com/paschalugwu/alx-higher_level_programming/blob/main/0x11-python-network_1/6-post_email.py)

#### 7. Error code #1

**Objective:** Send a request to a given URL and display the body of the response. If the HTTP status code is greater than or equal to 400, print an error message.

```bash
./7-error_code.py http://0.0.0.0:5000
./7-error_code.py http://0.0.0.0:5000/status_401
./7-error_code.py http://0.0.0.0:5000/doesnt_exist
./7-error_code.py http://0.0.0.0:5000/status_500
```

**Repo:**
- [alx-higher_level_programming/0x11-python

-network_1/7-error_code.py](https://github.com/paschalugwu/alx-higher_level_programming/blob/main/0x11-python-network_1/7-error_code.py)

#### 8. Search API

**Objective:** Send a POST request with a letter parameter to http://0.0.0.0:5000/search_user and display the response.

```bash
./8-json_api.py
./8-json_api.py a
./8-json_api.py 2
./8-json_api.py b
```

**Repo:**
- [alx-higher_level_programming/0x11-python-network_1/8-json_api.py](https://github.com/paschalugwu/alx-higher_level_programming/blob/main/0x11-python-network_1/8-json_api.py)

#### 9. My GitHub!

**Objective:** Use the GitHub API to display your GitHub id using Basic Authentication.

```bash
./10-my_github.py papamuziko cisfun
./10-my_github.py papamuziko wrong_pwd
```

**Repo:**
- [alx-higher_level_programming/0x11-python-network_1/10-my_github.py](https://github.com/paschalugwu/alx-higher_level_programming/blob/main/0x11-python-network_1/10-my_github.py)

#### 10. Time for an interview! (Advanced)

**Objective:** List 10 commits (from most recent to oldest) of the repository “rails” by the user “rails” using the GitHub API.

```bash
./100-github_commits.py rails rails
```

**Repo:**
- [alx-higher_level_programming/0x11-python-network_1/100-github_commits.py](https://github.com/paschalugwu/alx-higher_level_programming/blob/main/0x11-python-network_1/100-github_commits.py)

### Important Note

Please be aware of the GitHub API rate limit (only 60 requests per hour by IP for unauthenticated requests). Make sure to avoid exceeding this limit.

---

**Copyright © 2024 ALX, All rights reserved.**- [alx-higher_level_programming/0x11-python-network_1/100-github_commits.py](https://github.com/paschalugwu/alx-higher_level_programming/blob/main/0x11-python-network_1/100-github_commits.py)

### Important Note

Please be aware of the GitHub API rate limit (only 60 requests per hour by IP for unauthenticated requests). Make sure to avoid exceeding this limit.
