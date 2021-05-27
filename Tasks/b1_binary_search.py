from typing import Sequence, Optional


def binary_search(elem: int, arr: Sequence) -> Optional[int]:
    """
    Performs binary search of given element inside of array

    :param elem: element to be found
    :param arr: array where element is to be found
    :return: Index of element if it's presented in the arr, None otherwise
    """

    left_border = 0
    right_border = len(arr)

    while left_border < right_border:
        middle_index = (left_border + right_border) // 2
        middle_elem = arr[middle_index]
        if middle_elem == elem:
            while arr[middle_index-1] == elem:
                middle_index -= 1
            return middle_index

        if elem < middle_elem:
            right_border = middle_index - 1
        elif elem > middle_elem:
            left_border = middle_index + 1
    print(elem, arr)
    return None
