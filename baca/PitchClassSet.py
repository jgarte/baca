import abjad
import baca


class PitchClassSet(abjad.PitchClassSet):
    r"""
    Pitch-class set.

    ..  container:: example

        Initializes set:

        ..  container:: example

            >>> items = [-2, -1.5, 6, 7, -1.5, 7]
            >>> setting = baca.pitch_class_set(items=items)
            >>> abjad.show(setting, strict=89) # doctest: +SKIP

            ..  docs::

                >>> lilypond_file = setting.__illustrate__()
                >>> abjad.f(lilypond_file[abjad.Voice], strict=89)
                \new Voice
                {
                    <fs' g' bf' bqf'>1
                }

    """

    ### CLASS VARIABLES ###

    __documentation_section__ = '(5) Utilities'

    __slots__ = (
        )

    ### SPECIAL METHODS ###

    def __eq__(self, argument):
        """
        Is true when segment equals ``argument``.

        ..  container:: example

            Works with Abjad pitch-class sets:

            >>> set_1 = abjad.PitchClassSet([0, 1, 2, 3])
            >>> set_2 = baca.PitchClassSet([0, 1, 2, 3])

            >>> set_1 == set_2
            True

            >>> set_2 == set_1
            True

        """
        if (not issubclass(type(argument), type(self)) and
            not issubclass(type(self), type(argument))):
            return False
        return self._collection == argument._collection

    ### PUBLIC METHODS ###

    def to_pitch_classes(self):
        """
        Makes new pitch-class set.

        ..  container:: example

            >>> setting = baca.pitch_class_set([-2, -1.5, 6, 7, -1.5, 7])
            >>> setting
            PitchClassSet([6, 7, 10, 10.5])

            >>> setting.to_pitch_classes()
            PitchClassSet([6, 7, 10, 10.5])

        Returns new pitch-class set.
        """
        return abjad.new(self)

    def to_pitches(self):
        """
        Makes pitch set.

        ..  container:: example

            >>> setting = baca.pitch_class_set([-2, -1.5, 6, 7, -1.5, 7])
            >>> setting
            PitchClassSet([6, 7, 10, 10.5])

            >>> setting.to_pitches()
            PitchSet([6, 7, 10, 10.5])

        Returns pitch set.
        """
        if self.item_class is abjad.NamedPitchClass:
            item_class = abjad.NamedPitch
        elif self.item_class is abjad.NumberedPitchClass:
            item_class = abjad.NumberedPitch
        else:
            raise TypeError(self.item_class)
        return baca.PitchSet(
            items=self,
            item_class=item_class,
            )


def _pitch_class_set(items=None, **keywords):
    if items:
        return PitchClassSet(items=items, **keywords)
    name = keywords.pop('name', None)
    expression = baca.Expression(name=name)
    callback = expression._make_initializer_callback(
        PitchClassSet,
        module_names=['baca'],
        string_template='{}',
        **keywords
        )
    expression = expression.append_callback(callback)
    return abjad.new(expression, proxy_class=PitchClassSet)