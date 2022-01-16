import os
"""Contains utility functions for use by other modules."""

def clear_screen():
    """Clear the screen of any present output."""
    if os.name == 'nt':
        os.system('cls') # use format for NT-systems if running windows
    else:
        os.system('clear') # use format for linux/osx if not running windows
