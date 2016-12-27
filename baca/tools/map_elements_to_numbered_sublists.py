# -*- coding: utf-8 -*-
import abjad


def map_elements_to_numbered_sublists(sequence):
    '''Maps `sequence` elements to numbered sublists.

    ::

        >>> import abjad
        >>> import baca

    ::

        >>> list_ = [1, 2, -3, -4, 5]
        >>> baca.tools.map_elements_to_numbered_sublists(list_)
        [[1], [2, 3], [-4, -5, -6], [-7, -8, -9, -10], [11, 12, 13, 14, 15]]

    ::

        >>> list_ = [1, 0, -3, -4, 5]
        >>> baca.tools.map_elements_to_numbered_sublists(list_)
        [[1], [], [-2, -3, -4], [-5, -6, -7, -8], [9, 10, 11, 12, 13]]

    Starts numbering at ``1``.

    Returns newly constructed list of lists.
    '''
    if not isinstance(sequence, list):
        raise TypeError
    if not all(isinstance(x, int) for x in sequence):
        raise ValueError
    result = []
    current = 1
    for length in sequence:
        abs_length = abs(length)
        part = range(current, current + abs_length)
        part = [abjad.mathtools.sign(length) * x for x in part]
        result.append(part)
        current += abs_length
    return result
