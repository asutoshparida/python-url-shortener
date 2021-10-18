"""
errors.py
~~~~~~~~
Module containing all custom errors
"""

errors = {
    'ServerError': {
        'response': "Some thing went wrong. Please try after some time.",
        'status': 500,
    },
    'BadRequest': {
        'response': "Request must be valid",
        'status': 400
    },
}