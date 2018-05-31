import abjad
import typing
from .SystemSpecifier import SystemSpecifier


class PageSpecifier(abjad.AbjadObject):
    """
    Page specifier.
    """

    ### CLASS VARIABLES ###

    __documentation_section__ = '(5) Utilities'

    __slots__ = (
        '_number',
        '_systems',
        )

    ### INITIALIZER ###

    def __init__(
        self,
        *,
        number: int = None,
        systems: typing.List[typing.Union[list, SystemSpecifier]] = None,
        ) -> None:
        if number is not None:
            assert isinstance(number, int), repr(number)
            assert 1 <= number, repr(number)
        self._number = number
        if systems is not None:
            y_offsets: list = []
            for system in systems:
                if isinstance(system, SystemSpecifier):
                    y_offset = system.y_offset
                elif isinstance(system, list):
                    y_offset = system[1]
                if y_offset in y_offsets:
                    message = f'systems overlap at Y-offset {y_offset}.'
                    raise Exception(message)
                else:
                    y_offsets.append(y_offset)
        self._systems = systems

    ### PUBLIC PROPERTIES ###

    @property
    def number(self) -> typing.Optional[int]:
        """
        Gets page number.
        """
        return self._number

    @property
    def systems(self) -> typing.Optional[
        typing.List[typing.Union[list, SystemSpecifier]]
        ]:
        """
        Gets systems.
        """
        return self._systems