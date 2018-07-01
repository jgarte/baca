import typing
from abjad.system.AbjadValueObject import AbjadValueObject
from abjad.enums import Up
from abjad.markups import Markup
from abjad.system.LilyPondFormatBundle import LilyPondFormatBundle
from abjad.top.new import new


class Accelerando(AbjadValueObject):
    r"""
    Accelerando.

    ..  container:: example

        >>> staff = abjad.Staff("c'4 d' e' f'")
        >>> score = abjad.Score([staff])
        >>> accelerando = baca.Accelerando()
        >>> abjad.attach(accelerando, staff[0])
        >>> abjad.show(score) # doctest: +SKIP

        ..  docs::

            >>> abjad.f(score)
            \new Score
            <<
                \new Staff
                {
                    c'4
                    ^ \markup {
                        \large
                            \upright
                                accel.
                        }
                    d'4
                    e'4
                    f'4
                }
            >>

    Accelerandi format as LilyPond markup.

    Accelerandi are not followed by any type of dashed line.
    """

    ### CLASS VARIABLES ###

    __slots__ = (
        '_markup',
        )

    _context = 'Score'

    _persistent = 'abjad.MetronomeMark'

    ### INITIALIZER ###

    def __init__(
        self,
        *,
        markup: Markup = None,
        ) -> None:
        if markup is not None:
            assert isinstance(markup, Markup), repr(markup)
        self._markup = markup

    ### SPECIAL METHODS ###

    def __str__(self) -> str:
        r"""
        Gets string representation of accelerando.

        ..  container:: example

            String representation of accelerando with default markup:

            >>> print(str(baca.Accelerando()))
            \markup {
                \large
                    \upright
                        accel.
                }

        ..  container:: example

            String representation of accelerando with custom markup:

            >>> markup = abjad.Markup(r'\bold { \italic { accelerando } }')
            >>> accelerando = baca.Accelerando(markup=markup)
            >>> print(str(accelerando))
            \markup {
                \bold
                    {
                        \italic
                            {
                                accelerando
                            }
                    }
                }

        """
        return str(self._get_markup())

    ### PRIVATE PROPERTIES ###

    @property
    def _contents_repr_string(self):
        return str(self)

    ### PRIVATE METHODS ###

    def _default_markup(self):
        contents = r'\large \upright accel.'
        return Markup(contents=contents)

    def _get_lilypond_format(self):
        return str(self)

    def _get_lilypond_format_bundle(self, component=None):
        bundle = LilyPondFormatBundle()
        markup = self._get_markup()
        markup = new(markup, direction=Up)
        markup_format_pieces = markup._get_format_pieces()
        bundle.after.markup.extend(markup_format_pieces)
        return bundle

    def _get_markup(self):
        if self.markup is not None:
            return self.markup
        return self._default_markup()

    ### PUBLIC PROPERTIES ###

    @property
    def context(self) -> str:
        """
        Gets (historically conventional) context.

        ..  container:: example

            >>> baca.Accelerando().context
            'Score'

        Override with ``abjad.attach(..., context='...')``.
        """
        return self._context

    @property
    def markup(self) -> typing.Optional[Markup]:
        r"""
        Gets markup of accelerando.

        ..  container:: example

            >>> markup = abjad.Markup(r'\bold { \italic { accel. } }')
            >>> accelerando = baca.Accelerando(markup=markup)
            >>> print(str(accelerando.markup))
            \markup {
                \bold
                    {
                        \italic
                            {
                                accel.
                            }
                    }
                }

        """
        return self._markup

    @property
    def persistent(self) -> str:
        """
        Is ``'abjad.MetronomeMark'``.

        ..  container:: example

            >>> baca.Accelerando().persistent
            'abjad.MetronomeMark'

        """
        return self._persistent

    @property
    def tweaks(self) -> None:
        r"""
        Are not implemented on accelerando.
        """
        pass