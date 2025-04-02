# Unit_Testing_Python

* This repo is made for educational purposes

# Repo's Info

For the university subject, Software Engineering In Practice,
performed by Professor Diomidis Spinellis, we execute the second
subject's labatory exercises, targeted on unit testing.

# Bat-Tech Testing Assignment

This repository contains unit tests for the `bat_functions.py` module, designed to ensure the reliability of critical Bat-Tech systems. The tests are written using the `pytest` framework and cover various testing techniques including basic assertions, parametrization, mocking, and Continuous Integration setup.

## Files in this Repository

* `bat_functions.py`: The core Python module containing the functions to be tested.
* `test_bat_functions.py`: The `pytest` test suite containing all the unit tests.
* `.github/workflows/pytest.yml`: The GitHub Actions workflow definition for automating test execution.
* `README.md`: This documentation file.

## Testing Approach & Tasks Completed

Here's a breakdown of the testing tasks performed:

### Exercise 1: Basic Tests and Parametrization

* **Task 1: Testing `calculate_bat_power`**
    * **Goal:** Verify that `calculate_bat_power` returns the correct power (`level * 42`).
    * **Implementation:** A test function (`test_calculate_bat_power_various_levels`) was created using basic `pytest` conventions. It uses `assert` statements to check the output for several different input `level` values (positive, zero, negative) to ensure correctness across various simple cases.

* **Task 2: Testing `signal_strength`**
    * **Goal:** Verify `signal_strength` calculates strength based on distance (`100 - distance * 10`) and correctly clamps the minimum strength at 0.
    * **Implementation:** The `@pytest.mark.parametrize` decorator was used on the test function `test_signal_strength_parametrized`. This allowed running the same test logic with multiple sets of inputs (`test_distance`) and expected outputs (`expected_strength`), covering the required distances (0, 5, 10, 12 km) and other edge cases efficiently, including where the strength calculation drops below zero.

### Exercise 3: Mocking External Dependencies

* **Task 3: Testing `Workspace_joker_info`**
    * **Goal:** Test code that *uses* `Workspace_joker_info` without actually experiencing the built-in 1-second delay and while controlling the returned data for predictable testing.
    * **Implementation:** Mocking was used via `pytest`'s built-in `monkeypatch` fixture within the `test_fetch_joker_info_mocked` function.
        1.  A simple mock function (`mock_get`) was defined to return a specific, custom dictionary (`{'mischief_level': 0, 'location': 'captured'}`) instantly.
        2.  `monkeypatch.setattr()` was used to temporarily replace the `Workspace_joker_info` function *as it exists in the test module's namespace* (`test_bat_functions.fetch_joker_info`) with `mock_get`. This addressed the specific way the function was imported (`from bat_functions import fetch_joker_info`).
        3.  Assertions confirmed that the test received the custom dictionary and executed quickly, proving the mock was successful and the `time.sleep` was bypassed.

### Exercise 4: Continuous Integration

* **Task 4: Setting up GitHub Actions**
    * **Goal:** Automatically run the entire `pytest` suite whenever changes are pushed to the GitHub repository, ensuring new code doesn't break existing functionality.
    * **Implementation:** A GitHub Actions workflow file was created at `.github/workflows/pytest.yml`.
        1.  The workflow is configured to trigger `on: [push]`.
        2.  It runs on an `ubuntu-latest` runner.
        3.  It uses a matrix strategy to test across multiple Python versions (`3.9`, `3.10`, `3.11`).
        4.  The workflow steps include: checking out the repository code, setting up the specified Python version, installing dependencies (`pip install pytest`), and finally, running the tests using the `pytest -v` command. Failed tests will cause the workflow run to fail, alerting developers to issues.

## How to Run Tests Locally

1.  Clone this repository to your local machine.
2.  Ensure you have Python 3.x and `pip` installed.
3.  Install the necessary testing library:
    ```bash
    pip install pytest
    ```
4.  Navigate to the root directory of the cloned repository in your terminal.
5.  Execute `pytest`:
    ```bash
    pytest
    ```
    Or, for more detailed output:
    ```bash
    pytest -v
    ```

## Special Thanks 
The Lab's tasks were carefully made by Konstantinos Kyprianou 
 (**GitHub Username: `Konstantinos-10`**)