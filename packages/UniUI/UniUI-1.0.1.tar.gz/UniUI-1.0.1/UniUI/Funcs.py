from typing import Union
from . import Image

def IsRGBColor(color) -> (bool, Union[str, None]):
    # Check if color is a tuple or a list
    if not (isinstance(color, tuple) or isinstance(color, list)):
        return False, "non-tuple-list type."

    # Check if the length of the color is 3 (RGB) or 4 (RGBA)
    if len(color) not in [3, 4]:
        return False, "incorrect number of values, must be either RGB or RGBA."

    # Check if all elements are integers
    if not all(isinstance(channel, int) for channel in color):
        return False, "all values must be of type int."

    # Check if all elements are in the valid range [0, 255]
    if not all(0 <= channel <= 255 for channel in color):
        return False, "one of the values is < 0 or > 255."

    return True, None

def isCorrectSize(value, right_size: int = 2, values_type = int, check_zero_values: bool = False) -> (bool, Union[str, None]):
    if isinstance(value, (tuple, list)):
        if len(value) != right_size:
            return False, f"the number of values for screen_resolution is incorrect, you need {right_size}."

        if all(isinstance(i, values_type) for i in value):
            if all(i == 0 for i in value) and check_zero_values:
                return False, "one of the values is 0."
            return True, None
        else:
            return False, f"one of the values is not of type {values_type.__name__}."
    else:
        return False, "non-tuple-list type."

def isCorrectAnchor(value) -> (bool, Union[str, None]):
    if type(value) not in [tuple, list, set]:
        return False, f"value is not correct type, you need: list, tuple or set."
    value = list(value)

    if len(value) != 2:
        return False, f"incorrect number of values, 2 needed."

    if value[0] not in Image.Anchor.X_ANCHORS:
        return False, f"Anchor : the x anchor is incorrect, should be something from this list: {Image.Anchor.X_ANCHORS}"
    if value[1] not in Image.Anchor.Y_ANCHORS:
        return False, f"Anchor : the y anchor is incorrect, should be something from this list: {Image.Anchor.Y_ANCHORS}"

    return True, None