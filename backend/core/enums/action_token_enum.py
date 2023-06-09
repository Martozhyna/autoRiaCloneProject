from datetime import timedelta
from enum import Enum


class ActionEnum(Enum):
    ACTIVATE = ('activate', timedelta(days=1))
    RECOVERY_PASSWORD = ('recovery_password', timedelta(minutes=10))
    PREMIUM_ADD = ('premium_add', timedelta(minutes=10))

    def __init__(self, token_type, exp_time):
        self.token_type = token_type
        self.exp_time = exp_time
