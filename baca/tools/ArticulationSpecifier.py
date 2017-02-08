# -*- coding: utf-8 -*-
import abjad


class ArticulationSpecifier(abjad.abctools.AbjadObject):
    r'''Articulation specifier.

    ::

        >>> import abjad
        >>> import baca

    ..  container:: example

        Selects heads of pitched logical ties by default:

        ::

            >>> figure_maker = baca.tools.FigureMaker(
            ...     baca.tools.ArticulationSpecifier(
            ...         articulations=['>'],
            ...         ),
            ...     baca.tools.RhythmSpecifier(
            ...         rhythm_maker=baca.tools.FigureRhythmMaker(
            ...             talea=abjad.rhythmmakertools.Talea(
            ...                 counts=[5, 4, 4, 5, 4, 4, 4],
            ...                 denominator=32,
            ...                 ),
            ...             ),
            ...         ),
            ...     )

        ::

            >>> segments = [[0, 2, 10], [18, 16, 15, 20, 19], [9]]
            >>> contribution = figure_maker('Voice 1', segments)
            >>> lilypond_file = figure_maker.show(contribution)
            >>> show(lilypond_file) # doctest: +SKIP

        ..  doctest::

            >>> f(lilypond_file[abjad.Staff])
            \new Staff <<
                \context Voice = "Voice 1" {
                    \voiceOne
                    {
                        {
                            c'8 -\accent ~ [
                            c'32
                            d'8 -\accent
                            bf'8 -\accent ]
                        }
                        {
                            fs''8 -\accent ~ [
                            fs''32
                            e''8 -\accent
                            ef''8 -\accent
                            af''8 -\accent ~
                            af''32
                            g''8 -\accent ]
                        }
                        {
                            a'8 -\accent ~ [
                            a'32 ]
                        }
                    }
                }
            >>

    '''

    ### CLASS VARIABLES ###

    __documentation_section__ = 'Specifiers'

    __slots__ = (
        '_articulations',
        '_selector',
        )

    ### INITIALIZER ###

    def __init__(
        self,
        articulations=None,
        selector=None,
        ):
        if articulations is not None:
            prototype = (abjad.Articulation, str, tuple, list, type(None))
            assert all(isinstance(_, prototype) for _ in articulations)
        self._articulations = articulations
        if selector is not None:
            assert isinstance(selector, abjad.selectortools.Selector)
        self._selector = selector

    ### SPECIAL METHODS ###

    def __call__(self, selection):
        r'''Calls articulation specifier on `selection`.

        Returns none.
        '''
        tokens = self._get_articulations()
        if not tokens:
            return
        selector = self._get_selector()
        #print(selector)
        selection = selector(selection)
        #print(selections)
        for i, leaf in enumerate(selection):
            assert isinstance(leaf, abjad.scoretools.Leaf), repr(leaf)
            token = tokens[i]
            articulations = self._token_to_articulations(token)
            for articulation in articulations:
                abjad.attach(articulation, leaf)

    ### PRIVATE METHODS ###

    def _get_articulations(self):
        articulations = self.articulations or ()
        articulations = abjad.datastructuretools.CyclicTuple(articulations)
        return articulations

    def _get_selector(self):
        if self.selector is None:
            selector = abjad.selectortools.Selector()
            selector = selector.by_logical_tie(pitched=True, flatten=True)
            selector = selector.get_item(0, apply_to_each=True)
            return selector
        return self.selector

    @staticmethod
    def _token_to_articulations(token):
        result = []
        if not isinstance(token, (tuple, list)):
            token = [token]
        for item in token:
            if item is None:
                continue
            articulation = abjad.Articulation(item)
            result.append(articulation)
        return result

    ### PUBLIC PROPERTIES ###

    @property
    def articulations(self):
        r'''Gets articulations.

        ..  container:: example

            Accents the head of every pitched logical tie:

            ::

                >>> figure_maker = baca.tools.FigureMaker(
                ...     baca.tools.ArticulationSpecifier(
                ...         articulations=['>'],
                ...         ),
                ...     baca.tools.RhythmSpecifier(
                ...         rhythm_maker=baca.tools.FigureRhythmMaker(
                ...             talea=abjad.rhythmmakertools.Talea(
                ...                 counts=[5, 4, 4, 5, 4, 4, 4],
                ...                 denominator=32,
                ...                 ),
                ...             ),
                ...         ),
                ...     )

            ::

                >>> segments = [[0, 2, 10], [18, 16, 15, 20, 19], [9]]
                >>> contribution = figure_maker('Voice 1', segments)
                >>> lilypond_file = figure_maker.show(contribution)
                >>> show(lilypond_file) # doctest: +SKIP

            ..  doctest::

                >>> f(lilypond_file[abjad.Staff])
                \new Staff <<
                    \context Voice = "Voice 1" {
                        \voiceOne
                        {
                            {
                                c'8 -\accent ~ [
                                c'32
                                d'8 -\accent
                                bf'8 -\accent ]
                            }
                            {
                                fs''8 -\accent ~ [
                                fs''32
                                e''8 -\accent
                                ef''8 -\accent
                                af''8 -\accent ~
                                af''32
                                g''8 -\accent ]
                            }
                            {
                                a'8 -\accent ~ [
                                a'32 ]
                            }
                        }
                    }
                >>

        ..  container:: example

            Patterns accents:

            ::

                >>> figure_maker = baca.tools.FigureMaker(
                ...     baca.tools.ArticulationSpecifier(
                ...         articulations=[
                ...             '>', None, None,
                ...             '>', None, None,
                ...             '>', None,
                ...             ],
                ...         ),
                ...     baca.tools.RhythmSpecifier(
                ...         rhythm_maker=baca.tools.FigureRhythmMaker(
                ...             talea=abjad.rhythmmakertools.Talea(
                ...                 counts=[5, 4, 4, 5, 4, 4, 4],
                ...                 denominator=32,
                ...                 ),
                ...             ),
                ...         ),
                ...     )

            ::

                >>> segments = [[0, 2, 10], [18, 16, 15, 20, 19], [9]]
                >>> contribution = figure_maker('Voice 1', segments)
                >>> lilypond_file = figure_maker.show(contribution)
                >>> show(lilypond_file) # doctest: +SKIP

            ..  doctest::

                >>> f(lilypond_file[abjad.Staff])
                \new Staff <<
                    \context Voice = "Voice 1" {
                        \voiceOne
                        {
                            {
                                c'8 -\accent ~ [
                                c'32
                                d'8
                                bf'8 ]
                            }
                            {
                                fs''8 -\accent ~ [
                                fs''32
                                e''8
                                ef''8
                                af''8 -\accent ~
                                af''32
                                g''8 ]
                            }
                            {
                                a'8 -\accent ~ [
                                a'32 ]
                            }
                        }
                    }
                >>

        ..  container:: example

            Patterns accents with staccati:

            ::

                >>> figure_maker = baca.tools.FigureMaker(
                ...     baca.tools.ArticulationSpecifier(
                ...         articulations=[
                ...             '>', '.', '.',
                ...             '>', '.', '.',
                ...             '>', '.',
                ...             ],
                ...         ),
                ...     baca.tools.RhythmSpecifier(
                ...         rhythm_maker=baca.tools.FigureRhythmMaker(
                ...             talea=abjad.rhythmmakertools.Talea(
                ...                 counts=[5, 4, 4, 5, 4, 4, 4],
                ...                 denominator=32,
                ...                 ),
                ...             ),
                ...         ),
                ...     )

            ::

                >>> segments = [[0, 2, 10], [18, 16, 15, 20, 19], [9]]
                >>> contribution = figure_maker('Voice 1', segments)
                >>> lilypond_file = figure_maker.show(contribution)
                >>> show(lilypond_file) # doctest: +SKIP

            ..  doctest::

                >>> f(lilypond_file[abjad.Staff])
                \new Staff <<
                    \context Voice = "Voice 1" {
                        \voiceOne
                        {
                            {
                                c'8 -\accent ~ [
                                c'32
                                d'8 -\staccato
                                bf'8 -\staccato ]
                            }
                            {
                                fs''8 -\accent ~ [
                                fs''32
                                e''8 -\staccato
                                ef''8 -\staccato
                                af''8 -\accent ~
                                af''32
                                g''8 -\staccato ]
                            }
                            {
                                a'8 -\accent ~ [
                                a'32 ]
                            }
                        }
                    }
                >>

        ..  container:: example

            Patterns accented tenuti with staccati:

            ::

                >>> figure_maker = baca.tools.FigureMaker(
                ...     baca.tools.ArticulationSpecifier(
                ...         articulations=[
                ...             ('>', '-'), '.', '.',
                ...             ('>', '-'), '.', '.',
                ...             ('>', '-'), '.',
                ...             ],
                ...         ),
                ...     baca.tools.RhythmSpecifier(
                ...         rhythm_maker=baca.tools.FigureRhythmMaker(
                ...             talea=abjad.rhythmmakertools.Talea(
                ...                 counts=[5, 4, 4, 5, 4, 4, 4],
                ...                 denominator=32,
                ...                 ),
                ...             ),
                ...         ),
                ...     )

            ::

                >>> segments = [[0, 2, 10], [18, 16, 15, 20, 19], [9]]
                >>> contribution = figure_maker('Voice 1', segments)
                >>> lilypond_file = figure_maker.show(contribution)
                >>> show(lilypond_file) # doctest: +SKIP

            ..  doctest::

                >>> f(lilypond_file[abjad.Staff])
                \new Staff <<
                    \context Voice = "Voice 1" {
                        \voiceOne
                        {
                            {
                                c'8 -\accent -\tenuto ~ [
                                c'32
                                d'8 -\staccato
                                bf'8 -\staccato ]
                            }
                            {
                                fs''8 -\accent -\tenuto ~ [
                                fs''32
                                e''8 -\staccato
                                ef''8 -\staccato
                                af''8 -\accent -\tenuto ~
                                af''32
                                g''8 -\staccato ]
                            }
                            {
                                a'8 -\accent -\tenuto ~ [
                                a'32 ]
                            }
                        }
                    }
                >>

        ..  container:: example

            With reiterated dynamics:

            ::

                >>> figure_maker = baca.tools.FigureMaker(
                ...     baca.tools.ArticulationSpecifier(
                ...         articulations=['f'],
                ...         ),
                ...     baca.tools.RhythmSpecifier(
                ...         rhythm_maker=baca.tools.FigureRhythmMaker(
                ...             talea=abjad.rhythmmakertools.Talea(
                ...                 counts=[5, 4, 4, 5, 4, 4, 4],
                ...                 denominator=32,
                ...                 ),
                ...             ),
                ...         ),
                ...     )

            ::

                >>> segments = [[0, 2, 10], [18, 16, 15, 20, 19], [9]]
                >>> contribution = figure_maker('Voice 1', segments)
                >>> lilypond_file = figure_maker.show(contribution)
                >>> show(lilypond_file) # doctest: +SKIP

            ..  doctest::

                >>> f(lilypond_file[abjad.Staff])
                \new Staff <<
                    \context Voice = "Voice 1" {
                        \voiceOne
                        {
                            {
                                c'8 -\f ~ [
                                c'32
                                d'8 -\f
                                bf'8 -\f ]
                            }
                            {
                                fs''8 -\f ~ [
                                fs''32
                                e''8 -\f
                                ef''8 -\f
                                af''8 -\f ~
                                af''32
                                g''8 -\f ]
                            }
                            {
                                a'8 -\f ~ [
                                a'32 ]
                            }
                        }
                    }
                >>

        Defaults to none.

        Set to articulation tokens or none.

        Returns articulation tokens or none.
        '''
        return self._articulations

    @property
    def selector(self):
        r'''Gets selector.

        ..  container:: example

            Selects heads of pitched logical ties by default:

            ::

                >>> figure_maker = baca.tools.FigureMaker(
                ...     baca.tools.ArticulationSpecifier(
                ...         articulations=['>'],
                ...         ),
                ...     baca.tools.RhythmSpecifier(
                ...         rhythm_maker=baca.tools.FigureRhythmMaker(
                ...             talea=abjad.rhythmmakertools.Talea(
                ...                 counts=[5, 4, 4, 5, 4, 4, 4],
                ...                 denominator=32,
                ...                 ),
                ...             ),
                ...         ),
                ...     )

            ::

                >>> segments = [[0, 2, 10], [18, 16, 15, 20, 19], [9]]
                >>> contribution = figure_maker('Voice 1', segments)
                >>> lilypond_file = figure_maker.show(contribution)
                >>> show(lilypond_file) # doctest: +SKIP

            ..  doctest::

                >>> f(lilypond_file[abjad.Staff])
                \new Staff <<
                    \context Voice = "Voice 1" {
                        \voiceOne
                        {
                            {
                                c'8 -\accent ~ [
                                c'32
                                d'8 -\accent
                                bf'8 -\accent ]
                            }
                            {
                                fs''8 -\accent ~ [
                                fs''32
                                e''8 -\accent
                                ef''8 -\accent
                                af''8 -\accent ~
                                af''32
                                g''8 -\accent ]
                            }
                            {
                                a'8 -\accent ~ [
                                a'32 ]
                            }
                        }
                    }
                >>

        Defaults to none.

        Set to selector or none.

        Returns selector or none.
        '''
        return self._selector
