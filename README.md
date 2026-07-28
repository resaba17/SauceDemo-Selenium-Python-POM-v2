# SauceDemo Selenium Python POM Automation

## Project Description
This project automates the SauceDemo E-commerce web application using Selenium WebDriver, Python, Pytest, and the Page Object Model (POM) design pattern.

## Technologies Used
- Python
- Selenium WebDriver
- Pytest
- Page Object Model (POM)
- Allure Reports

## Project Structure

```
EcommerceAutomation/
│── data/
│── pages/
│── reports/
│── tests/
│── utils/
│── pytest.ini
│── README.md
```

## Test Cases
- Valid Login
- Invalid Login
- Logout
- Add Products to Cart
- Random Product Selection
- Sort Products (Low to High)
- Verify Cart Items
- Complete Checkout
- Reset App State

## Features
- Page Object Model (POM)
- Pytest Parameterization
- Explicit Waits
- Allure Report Generation
- Reusable Page Classes

## How to Run

Install dependencies:

```bash
pip install -r requirements.txt
```

Run all test cases:

```bash
pytest
```

Generate Allure Results:

```bash
pytest --alluredir=reports
```

View Allure Report:

```bash
allure serve reports
```

## Expected Result
All test cases should pass successfully and an Allure report should be generated.
