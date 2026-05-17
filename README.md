# Simple Calculator

A basic arithmetic calculator implemented in Python. This project provides a command-line interface for performing common mathematical operations with ease.

## Description

Simple Calculator is a lightweight tool designed to perform fundamental arithmetic operations such as addition, subtraction, multiplication, and division. It includes a modular design with separate files for the core logic (`calculator.py`), the user interface (`main.py`), and a test suite (`tests/test_calculator.py`). Ideal for learning Python basics or as a foundation for more advanced calculator features.

## Features

- Addition, subtraction, multiplication, and division
- Handles division by zero gracefully
- Clear and simple command-line interaction
- Modular code structure for easy extension
- Basic unit tests included

## Tech Stack

- **Language:** Python 3.x
- **Testing:** `unittest` (standard library)

## Installation

1. **Clone the repository** (or download the source files):
   ```bash
   git clone https://github.com/yourusername/simple-calculator.git
   cd simple-calculator
   ```

2. **(Optional) Create a virtual environment** (recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows: venv\Scripts\activate
   ```

3. **No external dependencies are required** – the project uses only Python’s standard library.

## Usage

Run the calculator from the command line:

```bash
python main.py
```

You will be prompted to enter an operation (`+`, `-`, `*`, `/`) and two numbers. Example session:

```
Select operation:
1. Add      (+)
2. Subtract (-)
3. Multiply (*)
4. Divide   (/)

Enter choice (1/2/3/4): 1
Enter first number: 5
Enter second number: 3
5.0 + 3.0 = 8.0
```

To exit, type `exit` when prompted.

## Project Structure

```
simple-calculator/
├── calculator.py          # Core arithmetic functions
├── main.py                # Command-line interface
└── tests/
    └── test_calculator.py # Unit tests for calculator functions
```

- **`calculator.py`** – Contains the functions `add`, `subtract`, `multiply`, and `divide`.
- **`main.py`** – Provides an interactive menu and handles user input/output.
- **`tests/test_calculator.py`** – Unit tests using `unittest` for all arithmetic operations, including edge cases.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.