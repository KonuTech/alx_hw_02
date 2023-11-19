import logging
from typing import Any, Dict, Union

logging.basicConfig(level=logging.INFO)


def addition(
    collection: Union[list, tuple, set, Dict[Any, Union[int, float]]],
    cast_to_int: bool = False,
) -> Union[int, float]:
    """
    Calculate the sum of numeric elements within the collection.

    Args:
    - collection (Union[list, tuple, set, Dict[Any, Union[int, float]]]):
        Collection of elements.
    - cast_to_int (bool, optional):
        If True, attempts to cast strings to integers. Defaults to False.

    Returns:
    - Union[int, float]: The sum of numeric elements within the collection.
    """
    total_sum = 0

    def is_number(s):
        try:
            float(s)
            return True
        except ValueError:
            return False

    def cast_to_float_or_int(value):
        if cast_to_int and isinstance(value, str) and is_number(value):
            logging.info(f"Attempting to cast '{value}' to int")
            return int(value)
        elif isinstance(value, str) and is_number(value):
            logging.info(f"Attempting to cast '{value}' to float")
            return value
        return value

    if isinstance(collection, dict):
        values = collection.values()
        for value in values:
            value = cast_to_float_or_int(value)
            if isinstance(value, (int, float)):
                total_sum += value
                logging.info(
                    f"""
                Added value: {value}
                Current total: {total_sum}
                """
                )
    else:
        elements = [cast_to_float_or_int(elem) for elem in collection]
        for element in elements:
            if isinstance(element, (int, float)):
                total_sum += element
                logging.info(
                    f"""
                Added element: {element}
                Current total: {total_sum}
                """
                )

    logging.info(f"Final total sum: {total_sum}")
    return total_sum


def test_addition():
    """
    Function to test the 'addition' function.
    """
    assert addition((1, 2, 3)) == 6
    assert addition((1, "2", 3)) == 4
    assert addition([8, 2, 3, 0, 8]) == 21
    assert addition([1, 2, "a"]) == 3
    assert addition({1: 8, 2: 2, 3: 3, 4: 0, 5: 9}) == 22
    assert addition({1: 8, 2: "a", 3: 3, 4: 0, 5: 9}) == 20


def test_addition_with_cast_to_int():
    """
    Function to test the 'addition' function with cast_to_int=True.
    """
    assert addition((1, "2", 3), cast_to_int=True) == 6


# Tests
test_addition()
test_addition_with_cast_to_int()
