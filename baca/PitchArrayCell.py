import abjad
import numbers


class PitchArrayCell(abjad.AbjadObject):
    """
    Pitch array cell.

    ..  container:: example

        A pitch array cell:

        >>> array = baca.PitchArray([[1, 2, 1], [2, 1, 1]])
        >>> print(array)
        [ ] [     ] [ ]
        [     ] [ ] [ ]

        >>> cell = array[0][1]

        >>> cell
        PitchArrayCell(width=2)

        >>> cell.column_indices
        (1, 2)

        >>> cell.indices
        (0, (1, 2))

        >>> cell.is_first_in_row
        False

        >>> cell.is_last_in_row
        False

        >>> cell.next
        PitchArrayCell(width=1)

        >>> abjad.f(cell.parent_array, strict=89)
        baca.PitchArray(
            rows=(
                baca.PitchArrayRow(
                    cells=(
                        baca.PitchArrayCell(
                            width=1,
                            ),
                        baca.PitchArrayCell(
                            width=2,
                            ),
                        baca.PitchArrayCell(
                            width=1,
                            ),
                        ),
                    ),
                baca.PitchArrayRow(
                    cells=(
                        baca.PitchArrayCell(
                            width=2,
                            ),
                        baca.PitchArrayCell(
                            width=1,
                            ),
                        baca.PitchArrayCell(
                            width=1,
                            ),
                        ),
                    ),
                ),
            )

        >>> abjad.f(cell.parent_column, strict=89)
        baca.PitchArrayColumn(
            cells=(
                baca.PitchArrayCell(
                    width=2,
                    ),
                baca.PitchArrayCell(
                    width=2,
                    ),
                ),
            )

        >>> abjad.f(cell.parent_row, strict=89)
        baca.PitchArrayRow(
            cells=(
                baca.PitchArrayCell(
                    width=1,
                    ),
                baca.PitchArrayCell(
                    width=2,
                    ),
                baca.PitchArrayCell(
                    width=1,
                    ),
                ),
            )

        >>> cell.pitches is None
        True

        >>> cell.previous
        PitchArrayCell(width=1)

        >>> cell.row_index
        0

        >>> cell.item
        2

        >>> cell.width
        2

    ..  container:: example

        Initializes empty:

        >>> baca.PitchArrayCell()
        PitchArrayCell(width=1)

        Initializes with width:

        >>> baca.PitchArrayCell(width=2)
        PitchArrayCell(width=2)

        Initializes with pitch:

        >>> baca.PitchArrayCell(pitches=[abjad.NamedPitch(0)])
        PitchArrayCell(pitches=[NamedPitch("c'")], width=1)

        Initializes with pitch numbers:

        >>> baca.PitchArrayCell(pitches=[0, 2, 4])
        PitchArrayCell(pitches=[NamedPitch("c'"), NamedPitch("d'"), NamedPitch("e'")], width=1)

        Initializes with pitches:

        >>> pitches = [abjad.NamedPitch(_) for _ in [0, 2, 4]]
        >>> baca.PitchArrayCell(pitches)
        PitchArrayCell(pitches=[NamedPitch("c'"), NamedPitch("d'"), NamedPitch("e'")], width=1)

        Initializes with pitch number and width:

        >>> baca.PitchArrayCell(pitches=0, width=2)
        PitchArrayCell(pitches=[NamedPitch("c'")], width=2)

        Initializes with pitch and width:

        >>> baca.PitchArrayCell(
        ...     pitches=[abjad.NamedPitch(0)], width=2)
        PitchArrayCell(pitches=[NamedPitch("c'")], width=2)

        Initializes with pitch numbers and width:

        >>> baca.PitchArrayCell(pitches=[0, 2, 4], width=2)
        PitchArrayCell(pitches=[NamedPitch("c'"), NamedPitch("d'"), NamedPitch("e'")], width=2)

    """

    ### CLASS VARIABLES ###

    __documentation_section__ = '(5) Utilities'

    __slots__ = (
        '_parent_row',
        '_pitches',
        '_row_parent',
        '_width',
        )

    _publish_storage_format = True

    ### INTIALIZER ###

    def __init__(
        self,
        pitches=None,
        *,
        width=1,
        ):
        self._pitches = None
        if pitches is not None:
            if isinstance(pitches, str):
                pitches = pitches.split()
            if isinstance(pitches, numbers.Number):
                pitches = [pitches]
            assert isinstance(pitches, (tuple, list)), repr(pitches)
            pitches = [abjad.NamedPitch(_) for _ in pitches]
            self._pitches = pitches
        assert isinstance(width, int), repr(width)
        assert 1 <= width, repr(width)
        self._width = width
        self._parent_row = None

    ### SPECIAL METHODS ###

    def __str__(self):
        """
        Gets string representation of pitch array cell.

        Returns string.
        """
        return self._format_string

    ### PRIVATE PROPERTIES ###

    @property
    def _composite_column_width(self):
        composite_column_width = 0
        columns = self.parent_array.columns
        for column_index in self.column_indices:
            composite_column_width += \
                columns[column_index]._column_format_width
        return composite_column_width

    @property
    def _conditional_pitch_string(self):
        if self.pitches:
            return self._pitch_string
        else:
            return ' '

    @property
    def _format_pitch_width_string(self):
        if self.pitches:
            if self.width == 1:
                return self._pitch_string
            else:
                return '%s %s' % (self._pitch_string, self._width_string)
        else:
            return self._width_string

    @property
    def _format_row_column_repr_string(self):
        return self._format_pitch_width_string

    @property
    def _format_string(self):
        if self.parent_column is not None:
            if self._is_last_cell_in_row:
                cell_width = self._composite_column_width - 2
            else:
                cell_width = self._composite_column_width - 3
            return '[%s]' % self._conditional_pitch_string.ljust(cell_width)
        else:
            return '[%s]' % self._conditional_pitch_string

    @property
    def _is_last_cell_in_row(self):
        if self.parent_row is not None:
            if self.column_indices[-1] == (self.parent_row.width - 1):
                return True
            return False
        return True

    @property
    def _pitch_string(self):
        if self.pitches:
            return ' '.join([str(pitch) for pitch in self.pitches])
        else:
            return ''

    @property
    def _width_string(self):
        return 'x%s' % self.width

    ### PRIVATE METHODS ###

    def _parse_cell_token(self, cell_token):
        if cell_token is None:
            pitches, width = [], 1
        elif isinstance(cell_token, int):
            if 0 < cell_token:
                pitches, width = [], cell_token
            else:
                message = 'integer width item must be positive.'
                raise ValueError(message)
        elif isinstance(cell_token, abjad.NamedPitch):
            pitches, width = [cell_token], 1
        elif isinstance(cell_token, list):
            pitch_token, width = cell_token, 1
            pitches = self._parse_pitch_token(pitch_token)
        elif isinstance(cell_token, tuple):
            if not len(cell_token) == 2:
                message = 'tuple item must be of length two.'
                raise ValueError(message)
            if isinstance(cell_token[0], str):
                pitches = self._parse_pitch_token(cell_token)
                width = 1
            else:
                pitch_token, width = cell_token
                pitches = self._parse_pitch_token(pitch_token)
        elif isinstance(cell_token, type(self)):
            pitches, width = cell_token.pitches, cell_token.width
        else:
            message = 'cell item must be integer width, pitch or pair.'
            raise TypeError(message)
        return pitches, width

    def _parse_pitch_token(self, pitch_token):
        pitches = []
        if isinstance(pitch_token, (int, float, abjad.NamedPitch)):
            pitch = abjad.NamedPitch(pitch_token)
            pitches.append(pitch)
        elif isinstance(pitch_token, tuple):
            pitches.append(abjad.NamedPitch(*pitch_token))
        elif isinstance(pitch_token, list):
            for element in pitch_token:
                pitch = abjad.NamedPitch(element)
                pitches.append(pitch)
        else:
            message = 'pitch item must be number, pitch or list.'
            raise TypeError(message)
        return pitches

    def _withdraw(self):
        parent_row = self.parent_row
        parent_row.remove(self)
        return self

    ### PUBLIC PROPERTIES ###

    @property
    def column_indices(self):
        """
        Gets column start and stop indices.

        ..  container:: example

            Gets column start and stop indices of cell in array:

            >>> array = baca.PitchArray([[1, 2, 1], [2, 1, 1]])
            >>> cell = array[0][1]
            >>> cell.column_indices
            (1, 2)

        ..  container:: example

            Gets column start and stop indices of cell outside array:

            >>> cell = baca.PitchArrayCell()
            >>> cell.column_indices is None
            True

        Returns tuple or none.
        """
        if self.parent_row is not None:
            if self.width == 1:
                return (self.column_start_index,)
            elif 1 < self.width:
                return self.column_start_index, self.column_stop_index

    @property
    def column_start_index(self):
        """
        Gets column start index.

        ..  container:: example

            Gets column start index of cell in array:

            >>> array = baca.PitchArray([[1, 2, 1], [2, 1, 1]])
            >>> cell = array[0][1]
            >>> cell.column_start_index
            1

        ..  container:: example

            Gets column start index of cell outside array:

            >>> cell = baca.PitchArrayCell()
            >>> cell.column_start_index is None
            True

        Returns nonnegative integer or none.
        """
        if self.parent_row is None:
            return
        start_index = 0
        for cell in self.parent_row.cells:
            if cell is self:
                return start_index
            start_index += cell.width

    @property
    def column_stop_index(self):
        """
        Gets column stop index.

        ..  container:: example

            Gets column stop index of cell in array:

            >>> array = baca.PitchArray([[1, 2, 1], [2, 1, 1]])
            >>> cell = array[0][1]
            >>> cell.column_stop_index
            2

        ..  container:: example

            Gets column stop index of cell outside array:

            >>> cell = baca.PitchArrayCell()
            >>> cell.column_stop_index is None
            True

        Returns nonnegative integer or none.
        """
        if self.parent_row is not None:
            return self.column_start_index + self.width - 1

    @property
    def indices(self):
        """
        Gets indices.

        ..  container:: example

            >>> array = baca.PitchArray([[1, 2, 1], [2, 1, 1]])

            >>> print(array)
            [ ] [     ] [ ]
            [     ] [ ] [ ]

            >>> for row in array:
            ...     for cell in row:
            ...         cell.indices
            ...
            (0, (0,))
            (0, (1, 2))
            (0, (3,))
            (1, (0, 1))
            (1, (2,))
            (1, (3,))

        Returns pair.
        """
        return self.row_index, self.column_indices

    @property
    def is_first_in_row(self):
        """
        Is true when pitch array cell is first in row.

        ..  container:: example

            >>> array = baca.PitchArray([[1, 2, 1], [2, 1, 1]])

            >>> print(array)
            [ ] [     ] [ ]
            [     ] [ ] [ ]

            >>> for row in array:
            ...     for cell in row:
            ...         cell, cell.is_first_in_row
            ...
            (PitchArrayCell(width=1), True)
            (PitchArrayCell(width=2), False)
            (PitchArrayCell(width=1), False)
            (PitchArrayCell(width=2), True)
            (PitchArrayCell(width=1), False)
            (PitchArrayCell(width=1), False)

        Returns true or false.
        """
        if self.parent_row is not None:
            if self.column_indices[0] == 0:
                return True
        return False

    @property
    def is_last_in_row(self):
        """
        Is true when pitch array cell is last in row.

        ..  container:: example

            >>> array = baca.PitchArray([[1, 2, 1], [2, 1, 1]])

            >>> print(array)
            [ ] [     ] [ ]
            [     ] [ ] [ ]

            >>> for row in array:
            ...     for cell in row:
            ...         cell, cell.is_last_in_row
            ...
            (PitchArrayCell(width=1), False)
            (PitchArrayCell(width=2), False)
            (PitchArrayCell(width=1), True)
            (PitchArrayCell(width=2), False)
            (PitchArrayCell(width=1), False)
            (PitchArrayCell(width=1), True)

        Returns true or false.
        """
        if self.parent_row is not None:
            if self.column_indices[-1] == self.parent_row.width - 1:
                return True
        return False

    @property
    def item(self):
        """
        Gets item.

        Complicated return type.
        """
        if not self.pitches:
            return self.width
        elif len(self.pitches) == 1:
            if self.width == 1:
                return (
                    str(self.pitches[0].pitch_class),
                    self.pitches[0].octave_number,
                    )
            else:
                return (
                    str(self.pitches[0].pitch_class),
                    self.pitches[0].octave_number,
                    self.width,
                    )
        else:
            if self.width == 1:
                return [(str(pitch.pitch_class),
                    pitch.octave_number)
                    for pitch in self.pitches]
            else:
                return (
                    [(str(pitch.pitch_class),
                    pitch.octave_number) for pitch in self.pitches],
                    self.width
                    )

    @property
    def next(self):
        """
        Gets next pitch array cell in row after this pitch array cell.

        ..  container:: example

            >>> array = baca.PitchArray([[1, 2, 1], [2, 1, 1]])

            >>> print(array)
            [ ] [     ] [ ]
            [     ] [ ] [ ]

            >>> for row in array:
            ...     for cell in row.cells[:-1]:
            ...         cell, cell.next
            ...
            (PitchArrayCell(width=1), PitchArrayCell(width=2))
            (PitchArrayCell(width=2), PitchArrayCell(width=1))
            (PitchArrayCell(width=2), PitchArrayCell(width=1))
            (PitchArrayCell(width=1), PitchArrayCell(width=1))

        Returns pitch array cell.
        """
        if self.parent_row is not None:
            if self.is_last_in_row:
                message = 'cell is last in row.'
                raise IndexError(message)
            return self.parent_row[self.column_indices[-1] + 1]
        message = 'cell has no parent row.'
        raise IndexError(message)

    @property
    def parent_array(self):
        """
        Gets parent array.

        Return pitch array.
        """
        parent_row = self.parent_row
        if parent_row is not None:
            return parent_row.parent_array
        return None

    @property
    def parent_column(self):
        """
        Gets parent column.

        Returns pitch array column.
        """
        parent_array = self.parent_array
        if parent_array is not None:
            start_column_index = self.column_indices[0]
            return parent_array.columns[start_column_index]
        return None

    @property
    def parent_row(self):
        """
        Gets parent row.

        Returns pitch array row.
        """
        return self._parent_row

    @property
    def pitches(self):
        """
        Gets and sets pitches of pitch array cell.

        Returns list.
        """
        return self._pitches

    @pitches.setter
    def pitches(self, pitches):
        if pitches is None:
            self._pitches = None
            return
        if isinstance(pitches, str):
            pitches = pitches.split()
        assert isinstance(pitches, (tuple, list)), repr(pitches)
        pitches = [abjad.NamedPitch(_) for _ in pitches]
        self._pitches = pitches

    @property
    def previous(self):
        """
        Gets pitch array cell in row prior to this pitch array cell.

        ..  container:: example

            >>> array = baca.PitchArray([[1, 2, 1], [2, 1, 1]])

            >>> print(array)
            [ ] [     ] [ ]
            [     ] [ ] [ ]

            >>> for row in array:
            ...     for cell in row.cells[1:]:
            ...         cell, cell.previous
            ...
            (PitchArrayCell(width=2), PitchArrayCell(width=1))
            (PitchArrayCell(width=1), PitchArrayCell(width=2))
            (PitchArrayCell(width=1), PitchArrayCell(width=2))
            (PitchArrayCell(width=1), PitchArrayCell(width=1))

        Returns pitch array cell.
        """
        if self.parent_row is not None:
            if self.is_first_in_row:
                message = 'cell is first in row.'
                raise IndexError(message)
            return self.parent_row[self.column_indices[0] - 1]
        message = 'cell has no parent row.'
        raise IndexError(message)

    @property
    def row_index(self):
        """
        Gets row index.

        Returns nonnegative integer or none.
        """
        parent_row = self.parent_row
        if parent_row is not None:
            return parent_row.row_index
        return None

    @property
    def weight(self):
        """
        Gets weight.

        Weight defined equal to number of pitches in cell.

        Returns nonnegative integer.
        """
        return len(self.pitches)

    @property
    def width(self):
        """
        Gets width.

        Width defined equal to number of columns spanned by cell.

        Returns positive integer.
        """
        return self._width

    ### PUBLIC METHODS ###

    def append_pitch(self, pitch):
        """
        Appends ``pitch`` to cell.

        Returns none.
        """
        if self.pitches is None:
            self._pitches = []
        pitch = abjad.NamedPitch(pitch)
        self._pitches.append(pitch)

    def matches_cell(self, argument):
        """
        Is true when pitch array cell matches ``argument``.

        ..  container:: example

            >>> array = baca.PitchArray([[1, 2, 1], [2, 1, 1]])
            >>> array[0].cells[0].append_pitch(0)
            >>> array[0].cells[1].append_pitch(2)
            >>> array[0].cells[1].append_pitch(4)

            >>> print(array)
            [c'] [d' e'    ] [ ]
            [          ] [ ] [ ]

            >>> array[0].cells[0].matches_cell(array[0].cells[0])
            True

            >>> array[0].cells[0].matches_cell(array[0].cells[1])
            False

        Returns true or false.
        """
        if isinstance(argument, type(self)):
            if self.pitches == argument.pitches:
                if self.width == argument.width:
                    return True
        return False