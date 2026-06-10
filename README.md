# Affinsys QA Automation Assignment

## Overview

This project automates an end-to-end e-commerce user flow using Playwright with Python and Pytest.

The automated scenario performs the following actions:

1. Launches the browser.
2. Opens the Sauce Demo Shopify website.
3. Selects the first available product.
4. Captures the selected product name.
5. Adds the product to the cart.
6. Navigates to the cart page.
7. Verifies that the selected product is successfully added to the cart.
8. Closes the browser.

---

## Technology Stack

* Python 3.14
* Playwright
* Pytest
* Visual Studio Code

---

## Project Structure

```text
Affinsys_Assignment
│
├── Tests
│   └── test_cart.py
│
├── README.md
├── requirements.txt
└── .gitignore
```

---

## Prerequisites

Ensure the following are installed on your machine:

* Python 3.x
* Visual Studio Code (optional)
* Git (optional)

---

## Installation

### Step 1: Clone the Repository

```bash
git clone <repository-url>
cd Affinsys_Assignment
```

### Step 2: Create Virtual Environment

```bash
python -m venv venv
```

### Step 3: Activate Virtual Environment

Windows:

```bash
venv\Scripts\activate
```

### Step 4: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 5: Install Playwright Browsers

```bash
playwright install
```

---

## Test Execution

Run the test using:

```bash
pytest Tests/test_cart.py -v -s
```

Expected Result:

```text
Selected Product: Grey jacket
Product successfully added to cart
PASSED
```

---

## Test Scenario

### Scenario: Add Product to Cart

Steps:

1. Open Sauce Demo Shopify website.
2. Click on the first available product.
3. Retrieve the product name.
4. Click the "Add to Cart" button.
5. Navigate to the Cart page.
6. Validate that the selected product is present in the cart.

---

## Assertion Used

```python
assert product_name in cart_text
```

This assertion verifies that the selected product has been successfully added to the cart.

## Author

Nishanthini S

QA Automation Assignment Submission
