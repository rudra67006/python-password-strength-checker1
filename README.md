# Password Strength Checker

## Project Overview

The Password Strength Checker is a beginner-friendly cybersecurity project that evaluates whether a password meets basic strength requirements. It provides clear feedback and suggestions to help users improve weak passwords through a simple web interface.

## Technologies Used

- **Python** — password validation and strength-checking logic.
- **HTML** — webpage structure and input form.
- **CSS** — styling and responsive user interface.
- **Python Standard Library** — runs the local web server without Flask or other external libraries.

## Features

- Checks whether the password contains at least 8 characters.
- Checks for uppercase letters and lowercase letters.
- Checks for numbers and special characters.
- Displays whether the password is strong or weak.
- Provides suggestions for improving weak passwords.
- Includes an eye icon to show or hide the password.
- Runs locally in a web browser.

## Setup Instructions

### Prerequisites

- Python 3 installed on your computer.
- A web browser such as Google Chrome.
- Visual Studio Code or another code editor (optional).

### 1. Clone the Repository

Replace the example URL below with your actual GitHub repository URL.

```bash
git clone [https://github.com/rudra67006/python-password-strength-checker1]
```

### 2. Open the Project Folder

```bash
cd password-strength-checker
```

### 3. Start the Local Server

Run the following command from the project folder:

```bash
python server.py
```

If your system uses the `py` command, you can run:

```bash
py server.py
```

### 4. Open the Website

Open Google Chrome and visit:

http://localhost:8000

Enter a test password and click **Check password** to view the result and improvement suggestions.

## Password Requirements

The checker evaluates five basic requirements:

1. At least 8 characters.
2. At least one uppercase letter (A–Z).
3. At least one lowercase letter (a–z).
4. At least one number (0–9).
5. At least one special character, such as `@`, `#`, or `!`.

## GitHub Repository

**Repository URL:** (https://github.com/rudra67006/python-password-strength-checker1)
