# test_bat_functions.py

# Import the functions we want to test
from bat_functions import calculate_bat_power, signal_strength, fetch_joker_info # Added fetch_joker_info

import pytest # Import pytest to use markers like parametrize
import time

# --- Exercise 1: Basic Tests and Parametrization ---

# Task 1: Test calculate_bat_power
def test_calculate_bat_power_various_levels():
    """
    Tests if calculate_bat_power returns the correct power (level * 42)
    for different input levels, including zero and negative values.
    """
    # Test with a typical positive level
    assert calculate_bat_power(level=10) == 420, "Test Failed: Level 10"
    # Test with level 1
    assert calculate_bat_power(level=1) == 42, "Test Failed: Level 1"
    # Test with level 0 (edge case)
    assert calculate_bat_power(level=0) == 0, "Test Failed: Level 0"
    # Test with another positive level
    assert calculate_bat_power(level=5) == 210, "Test Failed: Level 5"
    # Optional: Test with a negative level (assuming the logic holds)
    assert calculate_bat_power(level=-2) == -84, "Test Failed: Level -2"


# Task 2: Use pytest parametrization to test signal_strength with various distances.
@pytest.mark.parametrize("test_distance, expected_strength", [
    # Test case 1: 0 km distance, should be full strength
    (0, 100.0),
    # Test case 2: 2.5 km distance, fractional calculation
    (2.5, 75.0),
    # Test case 3: 5 km distance, exactly half strength expected based on formula
    (5, 50.0),
    # Test case 4: 10 km distance, strength should be exactly zero based on formula
    (10, 0.0),
    # Test case 5: 12 km distance, calculated strength is negative (-20), should clamp to 0
    (12, 0.0),
    # Test case 6: 15 km distance, calculated strength is negative (-50), should also clamp to 0
    (15, 0.0),
])
def test_signal_strength_parametrized(test_distance, expected_strength):
    """
    Tests the signal_strength function with various distances using parametrization.

    This test verifies that the strength calculation (100 - distance * 10)
    is performed correctly and, crucially, that the signal strength output
    never drops below 0, clamping at zero for distances >= 10 km.

    Args:
        test_distance (float): The input distance in kilometers passed by pytest.
        expected_strength (float): The expected signal strength output for the given distance.
    """
    # Arrange: Input parameters are provided by pytest's parametrization.
    # Act: Call the function under test.
    calculated_strength = signal_strength(distance=test_distance)

    # Assert: Check if the calculated strength matches the expected strength.
    # Using pytest.approx for float comparison is often good practice, but exact values work here.
    assert calculated_strength == expected_strength, \
           f"Test Failed: For distance {test_distance} km, expected {expected_strength} but got {calculated_strength}"
    

# --- Exercise 3: Mocking External Dependencies ---

# Task 3: Test fetch_joker_info using mocking
def test_fetch_joker_info_mocked(monkeypatch):
    """
    Tests the fetch_joker_info function by mocking its behavior.

    This test uses pytest's monkeypatch fixture to replace the actual
    fetch_joker_info function with a mock version. This allows testing
    code that *calls* fetch_joker_info without incurring the real delay
    and ensures we can control the returned data for the test.

    Args:
        monkeypatch: Pytest fixture for modifying classes, methods, etc. for testing.
    """
    # Arrange: Define the custom data we want the mock to return
    mock_response = {'mischief_level': 0, 'location': 'captured'}

    # Define a simple function that returns our custom data immediately
    def mock_get(*args, **kwargs):
        print("\nCalled MOCK fetch_joker_info!") # Optional: to see it's being called
        return mock_response

    # Use monkeypatch to replace the real function with our mock
    # Syntax: monkeypatch.setattr("module_name.FunctionName", mock_function)
    monkeypatch.setattr("bat_functions.fetch_joker_info", mock_get)

    # Act: Call the function (which is now the mock)
    start_time = time.time()
    result = fetch_joker_info()
    end_time = time.time()

    # Assert: Check that the result matches our mock data and that it ran quickly
    assert result == mock_response, f"Expected {mock_response} but got {result}"
    assert (end_time - start_time) < 0.1, "Test Failed: Mocked function took too long, sleep likely not patched."
