#!/usr/bin/env python3
# Jacob Rodal (https://www.jrodal.dev) (jr6ff@virginia.edu)

from sys import stderr
from .send_notification import send_notification
from datetime import datetime


def notify_after(wrapped_func):
    """
    Sends a notification when some func finishes execution.
    notify-send must be installed on your system, else it 
    prints a message to stderr.
    """
    def wrapper(*args, **kwargs):
        res = wrapped_func(*args, **kwargs)
        try:
            process = "Python"
            name = wrapped_func.__name__
            if name == "call_from_shell":
                name = process = args[0][1]
            title = f"{process} execution completed"
            message = f"'{name}' has finished executing."
            send_notification(title, message)
        except Exception as e:
            print(str(e), file=stderr)
        finally:
            return res
    return wrapper
