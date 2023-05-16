from enum import Enum


class RegEx(Enum):
    CARD_NUMBER = (
        r'\d{16}',
        [
            'credit card number must have 16 symbols'
        ]
    )

    def __init__(self, pattern: str, msg: str | list[str]):
        self.pattern = pattern
        self.msg = msg