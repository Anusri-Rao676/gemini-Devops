def welcome_message():
    """Returns a welcome messagse; string."""
    return "Hello, world!"

def greet_user(name):
    """Returns a personalized greeting."""
    if not isinstance(name, str) or not name:
        return "Hello there!"
    return f"Hello, {name}!"
