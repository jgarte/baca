import abjad


class Matrix(abjad.AbjadObject):
    """A matrix.

    Initializes from rows:

    >>> matrix = baca.Matrix([
    ...     [0, 1, 2, 3],
    ...     [10, 11, 12, 13],
    ...     [20, 21, 22, 23],
    ...     ])

    >>> matrix
    Matrix(3x4)

    >>> matrix[:]
    ((0, 1, 2, 3), (10, 11, 12, 13), (20, 21, 22, 23))

    >>> matrix[2]
    (20, 21, 22, 23)

    >>> matrix[2][0]
    20

    Initializes from columns:

    >>> matrix = baca.Matrix(columns=[
    ...     [0, 10, 20],
    ...     [1, 11, 21],
    ...     [2, 12, 22],
    ...     [3, 13, 23],
    ...     ])

    >>> matrix
    Matrix(3x4)

    >>> matrix[:]
    ((0, 1, 2, 3), (10, 11, 12, 13), (20, 21, 22, 23))

    >>> matrix[2]
    (20, 21, 22, 23)

    >>> matrix[2][0]
    20

    Matrix currently implements only item retrieval.

    Concatenation and division remain to be implemented.

    Standard transforms of linear algebra remain to be implemented.
    """

    ### CLASS VARIABLES ###

    __documentation_section__ = '(5) Utilities'

    ### INITIALIZER ###

    def __init__(self, *arguments, **keywords):
        if len(arguments) == 1:
            assert not keywords
            rows, columns = self._initialize_from_rows(arguments[0])
        elif 'columns' in keywords:
            assert not arguments
            rows, columns = self._initialize_from_columns(keywords['columns'])
        elif len(arguments) == 0:
            rows, columns = self._initialize_from_rows([[0], [0]])
        else:
            message = 'can not initialize {}: {!r}.'
            message = message(type(self).__name__, arguments)
            raise ValueError(message)
        self._rows = rows
        self._columns = columns
        self._n_rows = len(rows)
        self._n_columns = len(columns)

    ### SPECIAL METHODS ###

    def __getitem__(self, argument):
        """
        Gets row ``argument`` from matrix.

        >>> matrix[1]
        (10, 11, 12, 13)

        Returns row.
        """
        return self.rows.__getitem__(argument)

    def __repr__(self):
        """
        Gets interpreter representation of matrix.

        >>> matrix
        Matrix(3x4)

        Returns string.
        """
        return f'{type(self).__name__}({self._n_rows}x{self._n_columns})'

    ### PRIVATE METHODS ###

    def _initialize_from_columns(self, columns):
        columns = tuple([tuple(column) for column in columns])
        assert len(set([len(column) for column in columns])) in (0, 1)
        rows = []
        for row_index in range(len(columns[0])):
            row = tuple([column[row_index] for column in columns])
            rows.append(row)
        rows = tuple(rows)
        return rows, columns

    def _initialize_from_rows(self, rows):
        rows = tuple([tuple(row) for row in rows])
        assert len(set([len(row) for row in rows])) in (0, 1)
        columns = []
        for column_index in range(len(rows[0])):
            column = tuple([row[column_index] for row in rows])
            columns.append(column)
        columns = tuple(columns)
        return rows, columns

    ### PUBLIC PROPERTIES ###

    @property
    def columns(self):
        """
        Columns of matrix.

        >>> matrix = baca.Matrix(
        ...     [[0, 1, 2, 3],
        ...     [10, 11, 12, 13],
        ...     [20, 21, 22, 23],
        ...     ])

        >>> matrix.columns
        ((0, 10, 20), (1, 11, 21), (2, 12, 22), (3, 13, 23))

        Returns tuple.
        """
        return self._columns

    @property
    def rows(self):
        """
        Rows of matrix.

        >>> matrix = baca.Matrix(
        ...     [[0, 1, 2, 3],
        ...     [10, 11, 12, 13],
        ...     [20, 21, 22, 23],
        ...     ])

        >>> matrix.rows
        ((0, 1, 2, 3), (10, 11, 12, 13), (20, 21, 22, 23))

        Returns tuple.
        """
        return self._rows