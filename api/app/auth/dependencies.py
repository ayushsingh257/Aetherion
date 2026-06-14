from fastapi import Depends


def get_current_user():
    return {
        "message": "Authentication Foundation Ready"
    }