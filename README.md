# Saucedemo Automation Project

This is a simple automation framework for [saucedemo.com](https://www.saucedemo.com) using **Python**, **Selenium**, and **Pytest**.

## Setup
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/saucedemo-automation.git
   cd saucedemo-automation
   ````

2. Create and activate a virtual environment:
   ```bash
   python -m venv .venv
   # Windows
   .venv\Scripts\activate
   # Linux/Mac
   source .venv/bin/activate
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

## Run Tests

Run all tests:

```bash
pytest
```

Run a specific test:

```bash
pytest tests/test_01_login.py
```

## Reports

After running tests, an HTML report is generated in the **reports/** folder:

```
reports/report.html
```

Open it in a browser to see results.
