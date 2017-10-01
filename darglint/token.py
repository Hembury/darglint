"""Defines the tokens that result from lexing, as well as their types."""

from enum import Enum


class TokenType(Enum):
    """The possible types of tokens."""

    WORD = 1
    COLON = 2
    DOCTERM = 3  # """
    NEWLINE = 4
    INDENT = 5  # Assumed to always be 4 spaces


class Token(object):
    """A token representing anything which can appear in a docstring."""

    def __init__(self, value: str, token_type: TokenType):
        """Create a new Token."""
        self.value = value
        self.token_type = token_type

    def __str__(self):
        """Return readable representation for debugging."""
        return '<Token {} {}>'.format(self.value, self.token_type)

    def __repr__(self):
        """Return readable representation for debugging."""
        return str(self)