import abjad
import baca
import typing
from .Command import Command
from .Typing import Selector


class PartAssignmentCommand(Command):
    r'''Part assignment command.
    '''

    ### CLASS VARIABLES ###

    __slots__ = (
        '_part_assignment',
        )

    ### INITIALIZER ###

    def __init__(
        self,
        part_assignment: abjad.PartAssignment = None,
        selector: Selector = 'baca.leaves()',
        ) -> None:
        Command.__init__(self, selector=selector)
        if part_assignment is not None:
            if not isinstance(part_assignment, abjad.PartAssignment):
                message = 'part_assignment must be part assignment'
                message += f' (not {part_assignment!r}).'
                raise Exception(message)
        self._part_assignment: abjad.PartAssignment = part_assignment

    ### SPECIAL METHODS ###

    def __call__(self, argument=None) -> None:
        r'''Inserts ``selector`` output in container and sets part assignment.
        '''
        if argument is None:
            return
        if self.selector is not None:
            argument = self.selector(argument)
        if not self.score_template.allows_part_assignment(
            self.voice_name,
            self.part_assignment,
            ):
            message = f'{self.voice_name} does not allow part assignment:\n'
            message += f'  {self.part_assignment}'
            raise Exception(message)
        identifier = f'%*% {self.part_assignment!s}'
        container = abjad.Container(identifier=identifier)
        components = baca.select(argument).leaves().top()
        abjad.mutate(components).wrap(container)

    ### PUBLIC PROPERTIES ###

    @property
    def part_assignment(self) -> abjad.PartAssignment:
        r'''Gets part assignment.
        '''
        return self._part_assignment
