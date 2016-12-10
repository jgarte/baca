# -*- coding: utf-8 -*-
import abjad
import baca


class AcciaccaturaSpecifier(abjad.abctools.AbjadObject):
    r'''Acciaccatura specifier.

    ::

        >>> import baca

    ..  container:: example

        Default acciaccatura specifier:

        ::

            >>> rhythm_maker = baca.tools.FigureRhythmMaker(
            ...     acciaccatura_specifiers=[
            ...         baca.tools.AcciaccaturaSpecifier()
            ...         ],
            ...     talea=rhythmmakertools.Talea(
            ...         counts=[1],
            ...         denominator=8,
            ...         ),
            ...     )

        ::

            >>> stage_tokens = [
            ...     [0],
            ...     [2, 10],
            ...     [18, 16, 15],
            ...     [20, 19, 9, 0],
            ...     [2, 10, 18, 16, 15],
            ...     [20, 19, 9, 0, 2, 10],
            ...     ]
            >>> selections, state_manifest = rhythm_maker(stage_tokens)
            >>> durations = sum([_.get_duration() for _ in selections])
            >>> lilypond_file = rhythmmakertools.make_lilypond_file(
            ...     selections,
            ...     [durations],
            ...     pitched_staff=True,
            ...     )
            >>> score = lilypond_file.score_block.items[0]
            >>> override(score).spacing_spanner.strict_grace_spacing = False
            >>> override(score).spacing_spanner.strict_note_spacing = False
            >>> show(lilypond_file) # doctest: +SKIP 

        ..  doctest::

            >>> f(lilypond_file[Staff])
            \new Staff {
                {
                    \time 3/4
                    {
                        c'8
                    }
                    {
                        \acciaccatura {
                            d'16
                        }
                        bf'8
                    }
                    {
                        \acciaccatura {
                            fs''16 [
                            e''16 ]
                        }
                        ef''8
                    }
                    {
                        \acciaccatura {
                            af''16 [
                            g''16
                            a'16 ]
                        }
                        c'8
                    }
                    {
                        \acciaccatura {
                            d'16 [
                            bf'16
                            fs''16
                            e''16 ]
                        }
                        ef''8
                    }
                    {
                        \acciaccatura {
                            af''16 [
                            g''16
                            a'16
                            c'16
                            d'16 ]
                        }
                        bf'8
                    }
                }
            }

    '''

    ### CLASS VARIABLES ###

    __documentation_section__ = 'Specifiers'

    __slots__ = (
        '_durations',
        '_lmr_specifier',
        '_stage_pattern',
        )

    ### INITIALIZER ###

    def __init__(
        self,
        durations=None,
        lmr_specifier=None,
        stage_pattern=None,
        ):
        if durations is not None:
            assert isinstance(durations, list), repr(durations)
            durations = [abjad.durationtools.Duration(_) for _ in durations]
        self._durations = durations
        if lmr_specifier is not None:
            prototype = baca.tools.LMRSpecifier
            assert isinstance(lmr_specifier, prototype)
        self._lmr_specifier = lmr_specifier
        if stage_pattern is not None:
            prototype = (
                abjad.patterntools.Pattern,
                abjad.patterntools.CompoundPattern,
                )
            assert isinstance(stage_pattern, prototype), repr(stage_pattern)
        self._stage_pattern = stage_pattern

    ### SPECIAL METHODS ###

    def __call__(self, stage_token):
        r'''Calls acciaccatura specifier on `stage_token`.

        Returns grace container together with new stage token.
        '''
        assert isinstance(stage_token, list), repr(stage_token)
        stage_length = len(stage_token)
        lmr_specifier = self._get_lmr_specifier()
        stage_parts = lmr_specifier(stage_token)
        stage_parts = [_ for _ in stage_parts if _]
        stage_token = [_[-1] for _ in stage_parts]
        durations = self._get_durations()
        grace_containers = []
        for stage_part in stage_parts:
            if len(stage_part) <= 1:
                grace_containers.append(None)
                continue
            grace_token = list(stage_part[:-1])
            grace_leaves = abjad.scoretools.make_leaves(
                grace_token,
                durations,
                )
            grace_container = abjad.scoretools.GraceContainer(
                grace_leaves,
                kind='acciaccatura',
                )
            if 1 < len(grace_container):
                abjad.attach(abjad.spannertools.Beam(), grace_container[:])
            grace_containers.append(grace_container)
        assert len(grace_containers) == len(stage_token)
        return grace_containers, stage_token

    ### PRIVATE METHODS ###

    def _get_durations(self):
        return self.durations or [abjad.durationtools.Duration(1, 16)]

    def _get_lmr_specifier(self):
        if self.lmr_specifier is not None:
            return self.lmr_specifier
        return baca.tools.LMRSpecifier()

    def _get_stage_pattern(self):
        return self.stage_pattern or abjad.patterntools.select_all()

    ### PUBLIC PROPERTIES ###

    @property
    def durations(self):
        r'''Gets durations.

        ..  container:: example

            Sixteenth-note acciaccaturas:

            ::

                >>> rhythm_maker = baca.tools.FigureRhythmMaker(
                ...     acciaccatura_specifiers=[
                ...         baca.tools.AcciaccaturaSpecifier()
                ...         ],
                ...     talea=rhythmmakertools.Talea(
                ...         counts=[1],
                ...         denominator=8,
                ...         ),
                ...     )

            ::

                >>> stage_tokens = [
                ...     [0],
                ...     [2, 10],
                ...     [18, 16, 15],
                ...     [20, 19, 9, 0],
                ...     [2, 10, 18, 16, 15],
                ...     [20, 19, 9, 0, 2, 10],
                ...     ]
                >>> selections, state_manifest = rhythm_maker(stage_tokens)
                >>> durations = sum([_.get_duration() for _ in selections])
                >>> lilypond_file = rhythmmakertools.make_lilypond_file(
                ...     selections,
                ...     [durations],
                ...     pitched_staff=True,
                ...     )
                >>> score = lilypond_file.score_block.items[0]
                >>> override(score).spacing_spanner.strict_grace_spacing = False
                >>> override(score).spacing_spanner.strict_note_spacing = False
                >>> show(lilypond_file) # doctest: +SKIP

            ..  doctest::

                >>> f(lilypond_file[Staff])
                \new Staff {
                    {
                        \time 3/4
                        {
                            c'8
                        }
                        {
                            \acciaccatura {
                                d'16
                            }
                            bf'8
                        }
                        {
                            \acciaccatura {
                                fs''16 [
                                e''16 ]
                            }
                            ef''8
                        }
                        {
                            \acciaccatura {
                                af''16 [
                                g''16
                                a'16 ]
                            }
                            c'8
                        }
                        {
                            \acciaccatura {
                                d'16 [
                                bf'16
                                fs''16
                                e''16 ]
                            }
                            ef''8
                        }
                        {
                            \acciaccatura {
                                af''16 [
                                g''16
                                a'16
                                c'16
                                d'16 ]
                            }
                            bf'8
                        }
                    }
                }

            This is default behavior.

        ..  container:: example

            Eighth-note acciaccaturas:

            ::

                >>> rhythm_maker = baca.tools.FigureRhythmMaker(
                ...     acciaccatura_specifiers=[
                ...         baca.tools.AcciaccaturaSpecifier(
                ...             durations=[Duration(1, 8)],
                ...             ),
                ...         ],
                ...     talea=rhythmmakertools.Talea(
                ...         counts=[1],
                ...         denominator=8,
                ...         ),
                ...     )

            ::

                >>> stage_tokens = [
                ...     [0],
                ...     [2, 10],
                ...     [18, 16, 15],
                ...     [20, 19, 9, 0],
                ...     [2, 10, 18, 16, 15],
                ...     [20, 19, 9, 0, 2, 10],
                ...     ]
                >>> selections, state_manifest = rhythm_maker(stage_tokens)
                >>> durations = sum([_.get_duration() for _ in selections])
                >>> lilypond_file = rhythmmakertools.make_lilypond_file(
                ...     selections,
                ...     [durations],
                ...     pitched_staff=True,
                ...     )
                >>> score = lilypond_file.score_block.items[0]
                >>> override(score).spacing_spanner.strict_grace_spacing = False
                >>> override(score).spacing_spanner.strict_note_spacing = False
                >>> show(lilypond_file) # doctest: +SKIP

            ..  doctest::

                >>> f(lilypond_file[Staff])
                \new Staff {
                    {
                        \time 3/4
                        {
                            c'8
                        }
                        {
                            \acciaccatura {
                                d'8
                            }
                            bf'8
                        }
                        {
                            \acciaccatura {
                                fs''8 [
                                e''8 ]
                            }
                            ef''8
                        }
                        {
                            \acciaccatura {
                                af''8 [
                                g''8
                                a'8 ]
                            }
                            c'8
                        }
                        {
                            \acciaccatura {
                                d'8 [
                                bf'8
                                fs''8
                                e''8 ]
                            }
                            ef''8
                        }
                        {
                            \acciaccatura {
                                af''8 [
                                g''8
                                a'8
                                c'8
                                d'8 ]
                            }
                            bf'8
                        }
                    }
                }

        Defaults to none.

        Set to durations or none.

        Returns durations or none.
        '''
        return self._durations

    @property
    def lmr_specifier(self):
        r'''Gets LMR specifier.

        ..  container:: example

            As many acciaccaturas as possible per stage:

            ::

                >>> rhythm_maker = baca.tools.FigureRhythmMaker(
                ...     acciaccatura_specifiers=[
                ...         baca.tools.AcciaccaturaSpecifier()
                ...         ],
                ...     talea=rhythmmakertools.Talea(
                ...         counts=[1],
                ...         denominator=8,
                ...         ),
                ...     )

            ::

                >>> stage_tokens = [
                ...     [0],
                ...     [2, 10],
                ...     [18, 16, 15],
                ...     [20, 19, 9, 0],
                ...     [2, 10, 18, 16, 15],
                ...     [20, 19, 9, 0, 2, 10],
                ...     ]
                >>> selections, state_manifest = rhythm_maker(stage_tokens)
                >>> durations = sum([_.get_duration() for _ in selections])
                >>> lilypond_file = rhythmmakertools.make_lilypond_file(
                ...     selections,
                ...     [durations],
                ...     pitched_staff=True,
                ...     )
                >>> score = lilypond_file.score_block.items[0]
                >>> override(score).spacing_spanner.strict_grace_spacing = False
                >>> override(score).spacing_spanner.strict_note_spacing = False
                >>> show(lilypond_file) # doctest: +SKIP

            ..  doctest::

                >>> f(lilypond_file[Staff])
                \new Staff {
                    {
                        \time 3/4
                        {
                            c'8
                        }
                        {
                            \acciaccatura {
                                d'16
                            }
                            bf'8
                        }
                        {
                            \acciaccatura {
                                fs''16 [
                                e''16 ]
                            }
                            ef''8
                        }
                        {
                            \acciaccatura {
                                af''16 [
                                g''16
                                a'16 ]
                            }
                            c'8
                        }
                        {
                            \acciaccatura {
                                d'16 [
                                bf'16
                                fs''16
                                e''16 ]
                            }
                            ef''8
                        }
                        {
                            \acciaccatura {
                                af''16 [
                                g''16
                                a'16
                                c'16
                                d'16 ]
                            }
                            bf'8
                        }
                    }
                }

            This is default behavior.

        ..  container:: example

            At most two acciaccaturas at the beginning of every stage:

            ::

                >>> rhythm_maker = baca.tools.FigureRhythmMaker(
                ...     acciaccatura_specifiers=[
                ...         baca.tools.AcciaccaturaSpecifier(
                ...             lmr_specifier=baca.tools.LMRSpecifier(
                ...                 left_length=3,
                ...                 right_counts=[1],
                ...                 right_cyclic=True,
                ...                 ),
                ...             ),
                ...         ],
                ...     talea=rhythmmakertools.Talea(
                ...         counts=[1],
                ...         denominator=8,
                ...         ),
                ...     )

            ::

                >>> stage_tokens = [
                ...     [0],
                ...     [2, 10],
                ...     [18, 16, 15],
                ...     [20, 19, 9, 0],
                ...     [2, 10, 18, 16, 15],
                ...     [20, 19, 9, 0, 2, 10],
                ...     ]
                >>> selections, state_manifest = rhythm_maker(stage_tokens)
                >>> durations = sum([_.get_duration() for _ in selections])
                >>> lilypond_file = rhythmmakertools.make_lilypond_file(
                ...     selections,
                ...     [durations],
                ...     pitched_staff=True,
                ...     )
                >>> score = lilypond_file.score_block.items[0]
                >>> override(score).spacing_spanner.strict_grace_spacing = False
                >>> override(score).spacing_spanner.strict_note_spacing = False
                >>> show(lilypond_file) # doctest: +SKIP

            ..  doctest::

                >>> f(lilypond_file[Staff])
                \new Staff {
                    {
                        \time 3/2
                        {
                            c'8
                        }
                        {
                            \acciaccatura {
                                d'16
                            }
                            bf'8
                        }
                        {
                            \acciaccatura {
                                fs''16 [
                                e''16 ]
                            }
                            ef''8
                        }
                        {
                            \acciaccatura {
                                af''16 [
                                g''16 ]
                            }
                            a'8 [
                            c'8 ]
                        }
                        {
                            \acciaccatura {
                                d'16 [
                                bf'16 ]
                            }
                            fs''8 [
                            e''8
                            ef''8 ]
                        }
                        {
                            \acciaccatura {
                                af''16 [
                                g''16 ]
                            }
                            a'8 [
                            c'8
                            d'8
                            bf'8 ]
                        }
                    }
                }

        ..  container:: example

            At most two acciaccaturas at the end of every stage:

            ::

                >>> rhythm_maker = baca.tools.FigureRhythmMaker(
                ...     acciaccatura_specifiers=[
                ...         baca.tools.AcciaccaturaSpecifier(
                ...             lmr_specifier=baca.tools.LMRSpecifier(
                ...                 right_length=3,
                ...                 left_counts=[1],
                ...                 left_cyclic=True,
                ...                 ),
                ...             ),
                ...         ],
                ...     talea=rhythmmakertools.Talea(
                ...         counts=[1],
                ...         denominator=8,
                ...         ),
                ...     )

            ::

                >>> stage_tokens = [
                ...     [0],
                ...     [2, 10],
                ...     [18, 16, 15],
                ...     [20, 19, 9, 0],
                ...     [2, 10, 18, 16, 15],
                ...     [20, 19, 9, 0, 2, 10],
                ...     ]
                >>> selections, state_manifest = rhythm_maker(stage_tokens)
                >>> durations = sum([_.get_duration() for _ in selections])
                >>> lilypond_file = rhythmmakertools.make_lilypond_file(
                ...     selections,
                ...     [durations],
                ...     pitched_staff=True,
                ...     )
                >>> score = lilypond_file.score_block.items[0]
                >>> override(score).spacing_spanner.strict_grace_spacing = False
                >>> override(score).spacing_spanner.strict_note_spacing = False
                >>> show(lilypond_file) # doctest: +SKIP

            ..  doctest::

                >>> f(lilypond_file[Staff])
                \new Staff {
                    {
                        \time 3/2
                        {
                            c'8
                        }
                        {
                            \acciaccatura {
                                d'16
                            }
                            bf'8
                        }
                        {
                            \acciaccatura {
                                fs''16 [
                                e''16 ]
                            }
                            ef''8
                        }
                        {
                            af''8 [
                            \acciaccatura {
                                g''16 [
                                a'16 ]
                            }
                            c'8 ]
                        }
                        {
                            d'8 [
                            bf'8
                            \acciaccatura {
                                fs''16 [
                                e''16 ]
                            }
                            ef''8 ]
                        }
                        {
                            af''8 [
                            g''8
                            a'8
                            \acciaccatura {
                                c'16 [
                                d'16 ]
                            }
                            bf'8 ]
                        }
                    }
                }

        ..  container:: example

            At most two acciaccaturas at the beginning of every stage and then
            at most two acciaccaturas at the end of every stage:

            ::

                >>> rhythm_maker = baca.tools.FigureRhythmMaker(
                ...     acciaccatura_specifiers=[
                ...         baca.tools.AcciaccaturaSpecifier(
                ...             lmr_specifier=baca.tools.LMRSpecifier(
                ...                 left_length=3,
                ...                 middle_counts=[1],
                ...                 middle_cyclic=True,
                ...                 right_length=3,
                ...                 ),
                ...             ),
                ...         ],
                ...     talea=rhythmmakertools.Talea(
                ...         counts=[1],
                ...         denominator=8,
                ...         ),
                ...     )

            ::

                >>> stage_tokens = [
                ...     [0],
                ...     [2, 10],
                ...     [18, 16, 15],
                ...     [20, 19, 9, 0],
                ...     [2, 10, 18, 16, 15],
                ...     [20, 19, 9, 0, 2, 10],
                ...     ]
                >>> selections, state_manifest = rhythm_maker(stage_tokens)
                >>> durations = sum([_.get_duration() for _ in selections])
                >>> lilypond_file = rhythmmakertools.make_lilypond_file(
                ...     selections,
                ...     [durations],
                ...     pitched_staff=True,
                ...     )
                >>> score = lilypond_file.score_block.items[0]
                >>> override(score).spacing_spanner.strict_grace_spacing = False
                >>> override(score).spacing_spanner.strict_note_spacing = False
                >>> show(lilypond_file) # doctest: +SKIP

            ..  doctest::

                >>> f(lilypond_file[Staff])
                \new Staff {
                    {
                        \time 9/8
                        {
                            c'8
                        }
                        {
                            \acciaccatura {
                                d'16
                            }
                            bf'8
                        }
                        {
                            \acciaccatura {
                                fs''16 [
                                e''16 ]
                            }
                            ef''8
                        }
                        {
                            \acciaccatura {
                                af''16 [
                                g''16 ]
                            }
                            a'8 [
                            c'8 ]
                        }
                        {
                            \acciaccatura {
                                d'16 [
                                bf'16 ]
                            }
                            fs''8 [
                            \acciaccatura {
                                e''16
                            }
                            ef''8 ]
                        }
                        {
                            \acciaccatura {
                                af''16 [
                                g''16 ]
                            }
                            a'8 [
                            \acciaccatura {
                                c'16 [
                                d'16 ]
                            }
                            bf'8 ]
                        }
                    }
                }

        ..  container:: example

            As many acciaccaturas as possible in the middle of every stage:

            ::

                >>> rhythm_maker = baca.tools.FigureRhythmMaker(
                ...     acciaccatura_specifiers=[
                ...         baca.tools.AcciaccaturaSpecifier(
                ...             lmr_specifier=baca.tools.LMRSpecifier(
                ...                 left_length=1,
                ...                 ),
                ...             ),
                ...         ],
                ...     talea=rhythmmakertools.Talea(
                ...         counts=[1],
                ...         denominator=8,
                ...         ),
                ...     )

            ::

                >>> stage_tokens = [
                ...     [0],
                ...     [2, 10],
                ...     [18, 16, 15],
                ...     [20, 19, 9, 0],
                ...     [2, 10, 18, 16, 15],
                ...     [20, 19, 9, 0, 2, 10],
                ...     ]
                >>> selections, state_manifest = rhythm_maker(stage_tokens)
                >>> durations = sum([_.get_duration() for _ in selections])
                >>> lilypond_file = rhythmmakertools.make_lilypond_file(
                ...     selections,
                ...     [durations],
                ...     pitched_staff=True,
                ...     )
                >>> score = lilypond_file.score_block.items[0]
                >>> override(score).spacing_spanner.strict_grace_spacing = False
                >>> override(score).spacing_spanner.strict_note_spacing = False
                >>> show(lilypond_file) # doctest: +SKIP

            ..  doctest::

                >>> f(lilypond_file[Staff])
                \new Staff {
                    {
                        \time 11/8
                        {
                            c'8
                        }
                        {
                            d'8 [
                            bf'8 ]
                        }
                        {
                            fs''8 [
                            \acciaccatura {
                                e''16
                            }
                            ef''8 ]
                        }
                        {
                            af''8 [
                            \acciaccatura {
                                g''16 [
                                a'16 ]
                            }
                            c'8 ]
                        }
                        {
                            d'8 [
                            \acciaccatura {
                                bf'16 [
                                fs''16
                                e''16 ]
                            }
                            ef''8 ]
                        }
                        {
                            af''8 [
                            \acciaccatura {
                                g''16 [
                                a'16
                                c'16
                                d'16 ]
                            }
                            bf'8 ]
                        }
                    }
                }

        Defaults to none.

        Set to LMR specifier or none.

        Returns LMR specifier or none.
        '''
        return self._lmr_specifier

    @property
    def stage_pattern(self):
        r'''Gets stage pattern.

        ..  container:: example

            Applies to all stages:

            ::

                >>> rhythm_maker = baca.tools.FigureRhythmMaker(
                ...     acciaccatura_specifiers=[
                ...         baca.tools.AcciaccaturaSpecifier()
                ...         ],
                ...     talea=rhythmmakertools.Talea(
                ...         counts=[1],
                ...         denominator=8,
                ...         ),
                ...     )

            ::

                >>> stage_tokens = [
                ...     [0],
                ...     [2, 10],
                ...     [18, 16, 15],
                ...     [20, 19, 9, 0],
                ...     [2, 10, 18, 16, 15],
                ...     [20, 19, 9, 0, 2, 10],
                ...     ]
                >>> selections, state_manifest = rhythm_maker(stage_tokens)
                >>> durations = sum([_.get_duration() for _ in selections])
                >>> lilypond_file = rhythmmakertools.make_lilypond_file(
                ...     selections,
                ...     [durations],
                ...     pitched_staff=True,
                ...     )
                >>> score = lilypond_file.score_block.items[0]
                >>> override(score).spacing_spanner.strict_grace_spacing = False
                >>> override(score).spacing_spanner.strict_note_spacing = False
                >>> show(lilypond_file) # doctest: +SKIP

            ..  doctest::

                >>> f(lilypond_file[Staff])
                \new Staff {
                    {
                        \time 3/4
                        {
                            c'8
                        }
                        {
                            \acciaccatura {
                                d'16
                            }
                            bf'8
                        }
                        {
                            \acciaccatura {
                                fs''16 [
                                e''16 ]
                            }
                            ef''8
                        }
                        {
                            \acciaccatura {
                                af''16 [
                                g''16
                                a'16 ]
                            }
                            c'8
                        }
                        {
                            \acciaccatura {
                                d'16 [
                                bf'16
                                fs''16
                                e''16 ]
                            }
                            ef''8
                        }
                        {
                            \acciaccatura {
                                af''16 [
                                g''16
                                a'16
                                c'16
                                d'16 ]
                            }
                            bf'8
                        }
                    }
                }

            This is default behavior.

        ..  container:: example

            Applies to last stage:

            ::

                >>> rhythm_maker = baca.tools.FigureRhythmMaker(
                ...     acciaccatura_specifiers=[
                ...         baca.tools.AcciaccaturaSpecifier(
                ...             stage_pattern=patterntools.select_last(),
                ...             ),
                ...         ],
                ...     talea=rhythmmakertools.Talea(
                ...         counts=[1],
                ...         denominator=8,
                ...         ),
                ...     )

            ::

                >>> stage_tokens = [
                ...     [0],
                ...     [2, 10],
                ...     [18, 16, 15],
                ...     [20, 19, 9, 0],
                ...     [2, 10, 18, 16, 15],
                ...     [20, 19, 9, 0, 2, 10],
                ...     ]
                >>> selections, state_manifest = rhythm_maker(stage_tokens)
                >>> durations = sum([_.get_duration() for _ in selections])
                >>> lilypond_file = rhythmmakertools.make_lilypond_file(
                ...     selections,
                ...     [durations],
                ...     pitched_staff=True,
                ...     )
                >>> score = lilypond_file.score_block.items[0]
                >>> override(score).spacing_spanner.strict_grace_spacing = False
                >>> override(score).spacing_spanner.strict_note_spacing = False
                >>> show(lilypond_file) # doctest: +SKIP

            ..  doctest::

                >>> f(lilypond_file[Staff])
                \new Staff {
                    {
                        \time 2/1
                        {
                            c'8
                        }
                        {
                            d'8 [
                            bf'8 ]
                        }
                        {
                            fs''8 [
                            e''8
                            ef''8 ]
                        }
                        {
                            af''8 [
                            g''8
                            a'8
                            c'8 ]
                        }
                        {
                            d'8 [
                            bf'8
                            fs''8
                            e''8
                            ef''8 ]
                        }
                        {
                            \acciaccatura {
                                af''16 [
                                g''16
                                a'16
                                c'16
                                d'16 ]
                            }
                            bf'8
                        }
                    }
                }

        ..  container:: example

            Applies to every other stage:

            ::

                >>> rhythm_maker = baca.tools.FigureRhythmMaker(
                ...     acciaccatura_specifiers=[
                ...         baca.tools.AcciaccaturaSpecifier(
                ...             stage_pattern=patterntools.select_every([1], period=2),
                ...             ),
                ...         ],
                ...     talea=rhythmmakertools.Talea(
                ...         counts=[1],
                ...         denominator=8,
                ...         ),
                ...     )

            ::

                >>> stage_tokens = [
                ...     [0],
                ...     [2, 10],
                ...     [18, 16, 15],
                ...     [20, 19, 9, 0],
                ...     [2, 10, 18, 16, 15],
                ...     [20, 19, 9, 0, 2, 10],
                ...     ]
                >>> selections, state_manifest = rhythm_maker(stage_tokens)
                >>> durations = sum([_.get_duration() for _ in selections])
                >>> lilypond_file = rhythmmakertools.make_lilypond_file(
                ...     selections,
                ...     [durations],
                ...     pitched_staff=True,
                ...     )
                >>> score = lilypond_file.score_block.items[0]
                >>> override(score).spacing_spanner.strict_grace_spacing = False
                >>> override(score).spacing_spanner.strict_note_spacing = False
                >>> show(lilypond_file) # doctest: +SKIP

            ..  doctest::

                >>> f(lilypond_file[Staff])
                \new Staff {
                    {
                        \time 3/2
                        {
                            c'8
                        }
                        {
                            \acciaccatura {
                                d'16
                            }
                            bf'8
                        }
                        {
                            fs''8 [
                            e''8
                            ef''8 ]
                        }
                        {
                            \acciaccatura {
                                af''16 [
                                g''16
                                a'16 ]
                            }
                            c'8
                        }
                        {
                            d'8 [
                            bf'8
                            fs''8
                            e''8
                            ef''8 ]
                        }
                        {
                            \acciaccatura {
                                af''16 [
                                g''16
                                a'16
                                c'16
                                d'16 ]
                            }
                            bf'8
                        }
                    }
                }

        Defaults to none.

        Set to pattern or none.

        Returns pattern or none.
        '''
        return self._stage_pattern
