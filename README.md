# OrangeHRM Automation Testing using Selenium + Pytest

---
This is an automated testing suite for the OrangeHRM demo website. The project is built using the **Page Object Model (POM)** design pattern to ensure scalability, maintainability, and clean code structure.

### You can find this website here - https://opensource-demo.orangehrmlive.com/web/index.php

## Tech Stack:
- **Language**: Python
- **Framework**: Pytest
- **Automation**: Selenium Webdriver
- **Design Pattern**: Page Object Model (POM)

## Project Structure
The project is organized to separate test logic from page-specific interactions:
- `pages/` — Contains Page Objects. Each file represents a web page with its specific locators and interaction methods.
- `tests/` — Contains Test Suites. High-level scripts that execute test scenarios and verify outcomes.
- `conftest.py` — Pytest configuration file managing Fixtures (e.g., WebDriver initialization and teardown).
- `pytest.ini` — Configuration file for registering custom test markers and CLI defaults.

## Installation

#### Environment Setup
Ensure you have Python installed. It is recommended to use a virtual environment:

```bash
python -m venv .venv
```

#### Activate the environment
For Windows:
```bash
.venv\Scripts\activate
```

For macOs/Linux:
```bash
source .venv/bin/activate
```

Install required dependencies
```bash
pip install -r requirements.txt
```

## Execution
You can run the tests using various commands depending on your needs:

- Run all tests:
```bash
pytest
```

- Run critical tests only (Smoke):
```bash
pytest -m smoke
```

- Run stable regression tests:
```bash
pytest -m regression
```

- Run with detailed logs (Verbose):
```bash
pytest -v
```

## Implemented Test Scenarios
1. **Login Functionality**: Verifies successful authentication with valid credentials.
2. **User Management**: Creates user and successfully ensures deletion
3. **Logout**: Ensures the user session is terminated correctly and redirects to the login page.