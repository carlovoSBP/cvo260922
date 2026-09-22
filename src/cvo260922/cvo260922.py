"""cvo260922 module."""

import logging

LOGGER = logging.getLogger('cvo260922')
LOGGER.addHandler(logging.NullHandler())


def hello(greeting: str = 'Hello', someone: str = 'you') -> str:
    """Greet someone.

    Args:
        greeting: The greeting message.
        someone: The name of the person to greet.

    Returns:
        A greeting message.
    """
    return f'{greeting} {someone} from cvo260922!'
