import abjad


class Coat(abjad.AbjadObject):
    """
    Coat.
    """

    ### CLASS VARIABLES ###

    __documentation_section__ = '(5) Utilities'

    __slots__ = (
        '_argument',
        )

    ### INITIALIZER ###

    def __init__(self, argument):
        self._argument = argument

    ### PUBLIC PROPERTIES ###

    @property
    def argument(self):
        """
        Gets argument.
        """
        return self._argument