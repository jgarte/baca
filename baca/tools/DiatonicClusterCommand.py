import abjad
from .Command import Command


class DiatonicClusterCommand(Command):
    r'''Diatonic cluster command.

    ..  container:: example

        ::

            >>> staff = abjad.Staff("c' d' e' f'")
            >>> command = baca.DiatonicClusterCommand(
            ...     cluster_widths=[4, 6],
            ...     )
            >>> command(staff)
            >>> show(staff) # doctest: +SKIP

        ..  docs::

            >>> f(staff)
            \new Staff {
                <c' d' e' f'>4
                <d' e' f' g' a' b'>4
                <e' f' g' a'>4
                <f' g' a' b' c'' d''>4
            }

    '''

    ### CLASS ATTRIBUTES ###

    __slots__ = (
        '_cluster_widths',
        )

    ### INITIALIZER ###

    def __init__(self, cluster_widths=None, selector=None):
        Command.__init__(self, selector=selector)
        if cluster_widths is not None:
            cluster_widths = abjad.CyclicTuple(
                cluster_widths)
        self._cluster_widths = cluster_widths

    ### SPECIAL METHODS ###

    def __call__(self, argument=None):
        r'''Calls command on `argument`.

        Returns none.
        '''
        if argument is None:
            return
        if self.selector is not None:
            argument = self.selector(argument)
        notes = abjad.select(argument).by_class(abjad.Note)
        for i, note in enumerate(notes):
            cluster_width = self.cluster_widths[i]
            start = note.written_pitch._get_diatonic_pitch_number()
            diatonic_numbers = range(start, start + cluster_width)
            class_ = abjad.PitchClass
            dictionary = \
                class_._diatonic_pitch_class_number_to_pitch_class_number
            chromatic_numbers = [
                (12 * (x // 7)) + dictionary[x % 7] for x in diatonic_numbers
                ]
            chord_pitches = [abjad.NamedPitch(_) for _ in chromatic_numbers]
            chord = abjad.Chord(note)
            chord.note_heads[:] = chord_pitches
            abjad.mutate(note).replace(chord)

    ### PUBLIC PROPERTIES ###

    @property
    def cluster_widths(self):
        r'''Gets cluster widths.

        Defaults to none.

        Set to positive integers or none.

        Returns tuple of positive integers or none.
        '''
        return self._cluster_widths
