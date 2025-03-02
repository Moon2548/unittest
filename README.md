# Unit Tests with 100% Coverage

This repository contains unit tests for various Python functions, achieving 100% code coverage.

## Code Coverage Report

The following table shows the coverage report for the implemented functions and their corresponding tests:

| Name                                | Stmts | Miss | Cover |
| ----------------------------------- | ----- | ---- | ----- |
| functions\FIZZBUZZ.py               | 8     | 0    | 100%  |
| functions\alternating_characters.py | 4     | 0    | 100%  |
| functions\caesar_cipher.py          | 8     | 0    | 100%  |
| functions\funny_string.py           | 9     | 0    | 100%  |
| functions\grid_challenge.py         | 15    | 0    | 100%  |
| functions\number_utils.py           | 6     | 0    | 100%  |
| functions\staircase.py              | 7     | 0    | 100%  |
| functions\two_charactes.py          | 9     | 0    | 100%  |
| test\test_FIZZBUZZ.py               | 67    | 0    | 100%  |
| test\test_alternating_characters.py | 78    | 0    | 100%  |
| test\test_caesar_cipher.py          | 75    | 0    | 100%  |
| test\test_funny_string.py           | 58    | 0    | 100%  |
| test\test_grid_challenge.py         | 73    | 0    | 100%  |
| test\test_number_utils.py           | 23    | 0    | 100%  |
| test\test_staircase.py              | 24    | 0    | 100%  |
| test\test_two_characters.py         | 168   | 0    | 100%  |
| **TOTAL** | **632** | **0** | **100%** |

## Usage

To run the unit tests and generate a coverage report, use the following commands:

```bash
# Install required packages
pip install nose2

# Run all tests with coverage
nose2 -v --with-coverage