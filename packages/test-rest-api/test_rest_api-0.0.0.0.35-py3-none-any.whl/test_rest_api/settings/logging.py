from dataclasses import dataclass


@dataclass(frozen=True)
class Logging:
    sub_point: str = '*'
    key_val_sep: str = ':'


logging = Logging()
