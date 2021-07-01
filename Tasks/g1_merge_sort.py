from typing import List


def sort(container: List[int]) -> List[int]:
    """
    Sort input container with merge sort

    :param container: container of elements to be sorted
    :return: container sorted in ascending order
    """

    def merge(left_part, right_part):


        result = []
        while left_part and right_part:
            if left_part[0] > right_part[0]:
                result.append(right_part.pop(0))
            else:
                result.append(left_part.pop(0))

        if left_part:
            result.extend(left_part)
        elif right_part:
            result.extend(right_part)

        return result

    if len(container) == 1 or not container:
        return container


    left = container[:len(container) // 2]
    right = container[len(container) // 2:]

    left = sort(left)
    right = sort(right)


    return merge(left, right)
