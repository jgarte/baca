import abjad


class SpacingIndication(abjad.AbjadValueObject):
    """
    Spacing indication.

    LilyPond ``Score.proportionalNotationDuration`` will equal
    ``proportional_notation_duration`` when tempo equals ``tempo_indication``.

    Initialize from tempo and proportional notation duration:

    >>> tempo = abjad.MetronomeMark((1, 8), 44)
    >>> indication = baca.SpacingIndication(tempo, abjad.Duration(1, 68))

    >>> indication
    SpacingIndication(MetronomeMark(reference_duration=Duration(1, 8), units_per_minute=44), Duration(1, 68))

    Initialize from constants:

    >>> baca.SpacingIndication(((1, 8), 44), (1, 68))
    SpacingIndication(MetronomeMark(reference_duration=Duration(1, 8), units_per_minute=44), Duration(1, 68))

    Initialize from other spacing indication:

    >>> baca.SpacingIndication(indication)
    SpacingIndication(MetronomeMark(reference_duration=Duration(1, 8), units_per_minute=44), Duration(1, 68))

    Spacing indications are immutable.
    """

    ### CLASS VARIABLES ###

    __documentation_section__ = '(5) Utilities'

    __slots__ = (
        '_proportional_notation_duration',
        '_tempo_indication',
        )

    ### INITIALIZER ###

    def __init__(self, *arguments):
        if len(arguments) == 1 and isinstance(arguments[0], type(self)):
            self._tempo_indication = arguments[0].tempo_indication
            self._proportional_notation_duration = \
                arguments[0].proportional_notation_duration
        elif len(arguments) == 2:
            tempo = arguments[0]
            if isinstance(tempo, tuple):
                tempo = abjad.MetronomeMark(*tempo)
            tempo_indication = tempo
            proportional_notation_duration = abjad.Duration(arguments[1])
            self._tempo_indication = tempo_indication
            self._proportional_notation_duration = \
                proportional_notation_duration
        elif len(arguments) == 0:
            tempo = abjad.MetronomeMark()
            proportional_notation_duration = abjad.Duration(1, 68)
            self._tempo_indication = tempo
            self._proportional_notation_duration = \
                proportional_notation_duration
        else:
            raise ValueError(
                f'bad spacing indication arguments: {arguments!r}.'
                )

    ### SPECIAL METHODS ###

    def __eq__(self, argument):
        """
        Spacing indications compare equal when normalized
        spacing durations compare equal.
        """
        if isinstance(argument, SpacingIndication):
            if self.normalized_spacing_duration == \
                argument.normalized_spacing_duration:
                return True
        return False

    def __hash__(self):
        """
        Hashes spacing indication.

        Required to be explicitly redefined on Python 3 if __eq__ changes.

        Returns integer.
        """
        return super(SpacingIndication, self).__hash__()

    ### PRIVATE METHODS ###

    def _get_format_specification(self):
        return abjad.FormatSpecification(
            client=self,
            repr_is_indented=False,
            storage_format_args_values=[
                self._tempo_indication,
                self._proportional_notation_duration,
                ],
            )

    ### PUBLIC PROPERTIES ###

    @property
    def normalized_spacing_duration(self):
        """
        Proportional notation duration normalized to 60 MM.

        Returns duration.
        """
        indication = self.tempo_indication
        scalar = indication.reference_duration / indication.units_per_minute * \
            60 / abjad.Duration(1, 4)
        return scalar * self.proportional_notation_duration

    @property
    def proportional_notation_duration(self):
        """
        LilyPond proportional notation duration of spacing indication.

        Returns duration.
        """
        return self._proportional_notation_duration

    @property
    def tempo_indication(self):
        """
        MetronomeMark of spacing indication.

        Returns tempo.
        """
        return self._tempo_indication