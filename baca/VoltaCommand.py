import abjad
from .Command import Command
from .Selection import Selection


class VoltaCommand(Command):
    """
    Volta command.

    ..  container:: example

        >>> baca.VoltaCommand()
        VoltaCommand()

    """

    ### CLASS VARIABLES ###

    __slots__ = (
        )

    ### SPECIAL METHODS ###

    def __call__(self, argument=None) -> None:
        """
        Applies command to result of selector called on ``argument``.
        """
        if argument is None:
            return
        if self.selector is not None:
            argument = self.selector(argument)
        leaves = Selection(argument).leaves()
        container = abjad.Container()
        abjad.mutate(leaves).wrap(container)
        abjad.attach(abjad.Repeat(), container)
