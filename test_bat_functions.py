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
    

