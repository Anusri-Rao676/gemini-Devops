import pytest
from app import welcome_message, greet_user

def test_welcome_message():
    """Tests the welcome_message function."""
    assert welcome_message() == "Hello, world!"

def test_greet_user_with_name():
    """Tests that a user is greeted correctly."""
    assert greet_user("Alice") == "Hello, Alice!"

def test_greet_user_without_name():
    """Tests the function with no name provided."""
    assert greet_user("") == "Hello there!"

def test_greet_user_with_invalid_input():
    """Tests the function with non-string input."""
    assert greet_user(123) == "Hello there!"
    assert greet_user(None) == "Hello there!"
