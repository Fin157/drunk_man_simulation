from enum import Enum

def clamp(value: float, minimum: float, maximum: float) -> float:
    '''
    Clamps the value between the minimum and maximum.

    Parameters
    ----------
    value: float
        The value to be clamped.
    minimum: float
        The inclusive minimum of the interval value is clamped in.
    maximum: float
        The inclusive maximum of the interval value is clamped in.

    Returns
    -------
    float -> Value clamped inside the interval of minimum and maximum.
    '''

    return max(minimum, min(value, maximum))

class Ending(Enum):
    '''An enum that determines in which state the drunk man is
    at any given point in time.'''
    Home = 0
    Pub = 1
    Asleep = 2
    Walking = 3