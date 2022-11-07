import pytest 

def check_password(password):
    error = []
    if len(password) < 8:
        error.append('Password must be at least 8 characters')
    
    n_number = 0
    n_upper = 0
    n_special_char = 0
    for element in password:
        if element.isupper():
            n_upper += 1
        if element in list('123456789'):
            n_number += 1
        elif element.lower() not in list('abcdefghijklmnopqrstuvwxyz'):
            n_special_char += 1
    
    if n_number < 2:
        error.append('The password must contain at least 2 numbers')

    if n_upper == 0:
        error.append('password must contain at least one capital letter')

    if n_special_char == 0:
        error.append('password must contain at least one special character')

    return '\n'.join(error)


@pytest.mark.parametrize(
    'given, expected',
    [
        ('Pass22*', 'Password must be at least 8 characters'),
        ('Password2*', 'The password must contain at least 2 numbers'),
        ('Pass2*', 'Password must be at least 8 characters\nThe password must contain at least 2 numbers'), 
        ('password22*', 'password must contain at least one capital letter'),
        ('Password22', 'password must contain at least one special character')
    ]
)

def test_search(given, expected):
    actual_error = check_password(given)
    assert actual_error == expected