def mode(nums):
    """Return most-common number in list.

    For this function, there will always be a single-most-common value;
    you do not need to worry about handling cases where more than one item
    occurs the same number of times.

        >>> mode([1, 2, 1])
        1

        >>> mode([2, 2, 3, 3, 2])
        2
    """

    dict = {}

    for num in nums:
        if num in dict:
            dict[num] += 1
        else:
            dict[num] = 1

    max_count = max(dict.values())

    for (num, count) in dict.items():
        if count == max_count:
            return num