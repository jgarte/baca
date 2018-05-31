import abjad
import baca


class CommandWrapper(abjad.AbjadObject):
    r"""
    Command wrapper.

    ..  container:: example

        Pitch command wrapped with simple scope:

        >>> command = baca.CommandWrapper(
        ...     command=baca.pitches([7, 1, 3, 4, 5, 11]),
        ...     scope=baca.scope('ViolinMusicVoice', (1, 4)),
        ...     )

        >>> abjad.f(command, strict=89)
        baca.CommandWrapper(
            command=baca.PitchCommand(
                cyclic=True,
                pitches=abjad.CyclicTuple(
                    [
                        abjad.NamedPitch("g'"),
                        abjad.NamedPitch("cs'"),
                        abjad.NamedPitch("ef'"),
                        abjad.NamedPitch("e'"),
                        abjad.NamedPitch("f'"),
                        abjad.NamedPitch("b'"),
                        ]
                    ),
                selector=baca.pleaves(),
                ),
            scope=baca.Scope(
                stages=(1, 4),
                voice_name='ViolinMusicVoice',
                ),
            )

    ..  container:: example

        Pitch command wrapped with timeline scope:

        >>> command = baca.CommandWrapper(
        ...     command=baca.pitches([7, 1, 3, 4, 5, 11]),
        ...     scope=baca.timeline([
        ...         ('ViolinMusicVoice', (1, 4)),
        ...         ('ViolaMusicVoice', (1, 4)),
        ...         ]),
        ...     )

        >>> abjad.f(command, strict=89)
        baca.CommandWrapper(
            command=baca.PitchCommand(
                cyclic=True,
                pitches=abjad.CyclicTuple(
                    [
                        abjad.NamedPitch("g'"),
                        abjad.NamedPitch("cs'"),
                        abjad.NamedPitch("ef'"),
                        abjad.NamedPitch("e'"),
                        abjad.NamedPitch("f'"),
                        abjad.NamedPitch("b'"),
                        ]
                    ),
                selector=baca.pleaves(),
                ),
            scope=baca.TimelineScope(
                scopes=(
                    baca.Scope(
                        stages=(1, 4),
                        voice_name='ViolinMusicVoice',
                        ),
                    baca.Scope(
                        stages=(1, 4),
                        voice_name='ViolaMusicVoice',
                        ),
                    ),
                ),
            )

    """

    ### CLASS VARIABLES ###

    __documentation_section__ = '(4) Commands'

    __slots__ = (
        '_command',
        '_scope',
        )

    _publish_storage_format = True

    ### INITIALIZER ###

    def __init__(
        self,
        *,
        command=None,
        scope=None,
        ):
        if scope is not None:
            prototype = (baca.Scope, baca.TimelineScope)
            assert isinstance(scope, prototype), format(scope)
        self._scope = scope
        if command is not None:
            assert isinstance(command, baca.Command), format(command)
        self._command = command

    ### PUBLIC PROPERTIES ###

    @property
    def command(self):
        """
        Gets command.

        ..  container:: example

            >>> command = baca.CommandWrapper(
            ...     command=baca.pitches([7, 1, 3, 4, 5, 11]),
            ...     scope=baca.scope('ViolinMusicVoice', (1, 4)),
            ...     )

            >>> abjad.f(command.command, strict=89)
            baca.PitchCommand(
                cyclic=True,
                pitches=abjad.CyclicTuple(
                    [
                        abjad.NamedPitch("g'"),
                        abjad.NamedPitch("cs'"),
                        abjad.NamedPitch("ef'"),
                        abjad.NamedPitch("e'"),
                        abjad.NamedPitch("f'"),
                        abjad.NamedPitch("b'"),
                        ]
                    ),
                selector=baca.pleaves(),
                )

        Defaults to none.

        Set to command or none.

        Returns command or none.
        """
        return self._command

    @property
    def scope(self):
        """
        Gets scope.

        ..  container:: example

            Gets scope:

            >>> command = baca.CommandWrapper(
            ...     command=baca.pitches([7, 1, 3, 4, 5, 11]),
            ...     scope=baca.scope('ViolinMusicVoice', (1, 4)),
            ...     )

            >>> abjad.f(command.scope, strict=89)
            baca.Scope(
                stages=(1, 4),
                voice_name='ViolinMusicVoice',
                )

        Defaults to none.

        Set to scope or none.

        Returns scope or none.
        """
        return self._scope