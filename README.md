# Selenium-Based Web Automation Testing Framework

![Python](https://img.shields.io/badge/Python-3.12-blue)
![Selenium](https://img.shields.io/badge/Selenium-4.43-green)
![Tests](https://img.shields.io/badge/Tests-26%20Passed-brightgreen)
![CI/CD](https://img.shields.io/badge/CI%2FCD-GitHub%20Actions-orange)

## Overview
A production-grade automated browser testing framework built with Selenium and Python,
testing the SauceDemo e-commerce platform with 26 test cases across login, inventory,
cart, and checkout flows.

## Tech Stack
- Python 3.12
- Selenium 4.43
- Pytest + pytest-html
- GitHub Actions (CI/CD)
- Page Object Model (POM) Design Pattern

## Test Coverage
| Module | Test Cases |
|--------|-----------|
| Login | 5 |
| Inventory | 9 |
| Cart & Checkout | 12 |
| **Total** | **26** |

## Project Structure
selenium-framework/
├── pages/              # Page Object Model classes
│   ├── login_page.py
│   ├── inventory_page.py
│   ├── cart_page.py
│   └── checkout_page.py
├── tests/              # Test suites
│   ├── test_login.py
│   ├── test_inventory.py
│   └── test_cart_checkout.py
├── reports/            # HTML test reports
└── .github/workflows/  # CI/CD pipeline

## How to Run

### Install dependencies
```bash
pip install -r requirements.txt
```

### Run all tests
```bash
py -m pytest tests/ -v
```

### Run with HTML report
```bash
py -m pytest tests/ -v --html=reports/test_report.html --self-contained-html
```

## CI/CD
Every push to `main` automatically triggers the full test suite via GitHub Actions.