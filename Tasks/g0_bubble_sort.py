from typing import List


def sort(container: List[int]) -> List[int]:
    """
    Sort input container with bubble sort

    :param container: container of elements to be sorted
    :return: container sorted in ascending order
    """
    def swap(left_index: int, right_index: int):
        left_value = container[left_index]
        right_value = container[right_index]

        if left_value > right_value:
            container[right_index] = left_value
            container[left_index] = right_value

    for j in range(len(container)):
        for i in range(len(container) - 1 - j):
            swap(i, i+1)

    return container
