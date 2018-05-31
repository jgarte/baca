import abjad
import baca
import copy
from abjadext import rmakers
from .Command import Command


class ImbricationCommand(Command):
    r"""
    Imbrication command.

    >>> from abjadext import rmakers

    ..  container:: example

        Defaults:

        >>> music_maker = baca.MusicMaker(
        ...     rmakers.BeamSpecifier(
        ...         beam_divisions_together=True,
        ...         ),
        ...     )

        >>> collections = [
        ...     [0, 2, 10, 18, 16],
        ...     [15, 20, 19, 9, 0],
        ...     [2, 10, 18, 16, 15],
        ...     ]
        >>> contribution = music_maker(
        ...     'Voice 2',
        ...     collections,
        ...     baca.ImbricationCommand(
        ...         'Voice 1',
        ...         [2, 19, 9, 18, 16],
        ...         ),
        ...     )
        >>> lilypond_file = music_maker.show(contribution)
        >>> abjad.show(lilypond_file, strict=89) # doctest: +SKIP

        ..  docs::

            >>> abjad.f(lilypond_file[abjad.Score], strict=89)
            \new Score
            <<
                \new GlobalContext
                {
                    {   % measure
                        \time 15/16
                        s1 * 15/16
                    }   % measure
                }
                \new Staff
                <<
                    \context Voice = "Voice 1"
                    {
                        \voiceOne
                        {
                            \override TupletBracket.stencil = ##f
                            \override TupletNumber.stencil = ##f
                            \scaleDurations #'(1 . 1) {
                                s16
                                d'16
                                s16
                                s16
                                s16
                            }
                            \scaleDurations #'(1 . 1) {
                                s16
                                s16
                                g''16
                                [
                                a'16
                                ]
                                s16
                            }
                            \scaleDurations #'(1 . 1) {
                                s16
                                s16
                                fs''16
                                [
                                e''16
                                ]
                                s16
                            }
                            \revert TupletBracket.stencil
                            \revert TupletNumber.stencil
                        }
                    }
                    \context Voice = "Voice 2"
                    {
                        \voiceTwo
                        {
                            \scaleDurations #'(1 . 1) {
                                \set stemLeftBeamCount = 0
                                \set stemRightBeamCount = 2
                                c'16
                                [
                                \set stemLeftBeamCount = 2
                                \set stemRightBeamCount = 2
                                d'16
                                \set stemLeftBeamCount = 2
                                \set stemRightBeamCount = 2
                                bf'16
                                \set stemLeftBeamCount = 2
                                \set stemRightBeamCount = 2
                                fs''16
                                \set stemLeftBeamCount = 2
                                \set stemRightBeamCount = 1
                                e''16
                            }
                            \scaleDurations #'(1 . 1) {
                                \set stemLeftBeamCount = 1
                                \set stemRightBeamCount = 2
                                ef''16
                                \set stemLeftBeamCount = 2
                                \set stemRightBeamCount = 2
                                af''16
                                \set stemLeftBeamCount = 2
                                \set stemRightBeamCount = 2
                                g''16
                                \set stemLeftBeamCount = 2
                                \set stemRightBeamCount = 2
                                a'16
                                \set stemLeftBeamCount = 2
                                \set stemRightBeamCount = 1
                                c'16
                            }
                            \scaleDurations #'(1 . 1) {
                                \set stemLeftBeamCount = 1
                                \set stemRightBeamCount = 2
                                d'16
                                \set stemLeftBeamCount = 2
                                \set stemRightBeamCount = 2
                                bf'16
                                \set stemLeftBeamCount = 2
                                \set stemRightBeamCount = 2
                                fs''16
                                \set stemLeftBeamCount = 2
                                \set stemRightBeamCount = 2
                                e''16
                                \set stemLeftBeamCount = 2
                                \set stemRightBeamCount = 0
                                ef''16
                                ]
                            }
                        }
                    }
                >>
            >>

    ..  container:: example

        Multiple imbricated voices:

        >>> music_maker = baca.MusicMaker(
        ...     rmakers.BeamSpecifier(
        ...         beam_divisions_together=True,
        ...         ),
        ...     )

        >>> collections = [
        ...     [0, 2, 10, 18, 16],
        ...     [15, 20, 19, 9, 0],
        ...     [2, 10, 18, 16, 15],
        ...     ]
        >>> contribution = music_maker(
        ...     'Voice 2',
        ...     collections,
        ...     baca.ImbricationCommand(
        ...         'Voice 1',
        ...         [2, 19, 9],
        ...         baca.beam_everything(),
        ...         baca.staccato(selector=baca.pheads()),
        ...         ),
        ...     baca.ImbricationCommand(
        ...         'Voice 3',
        ...         [16, 10, 18],
        ...         baca.beam_everything(),
        ...         baca.accent(selector=baca.pheads()),
        ...         ),
        ...     )
        >>> lilypond_file = music_maker.show(contribution)
        >>> abjad.show(lilypond_file, strict=89) # doctest: +SKIP

        ..  docs::

            >>> abjad.f(lilypond_file[abjad.Score], strict=89)
            \new Score
            <<
                \new GlobalContext
                {
                    {   % measure
                        \time 15/16
                        s1 * 15/16
                    }   % measure
                }
                \new Staff
                <<
                    \context Voice = "Voice 1"
                    {
                        \voiceOne
                        {
                            \override TupletBracket.stencil = ##f
                            \override TupletNumber.stencil = ##f
                            \scaleDurations #'(1 . 1) {
                                s16
                                [
                                \set stemLeftBeamCount = 2
                                \set stemRightBeamCount = 2
                                d'16
                                -\staccato                                                           %! IC
                                s16
                                s16
                                s16
                            }
                            \scaleDurations #'(1 . 1) {
                                s16
                                s16
                                \set stemLeftBeamCount = 2
                                \set stemRightBeamCount = 2
                                g''16
                                -\staccato                                                           %! IC
                                \set stemLeftBeamCount = 2
                                \set stemRightBeamCount = 2
                                a'16
                                -\staccato                                                           %! IC
                                s16
                            }
                            \scaleDurations #'(1 . 1) {
                                s16
                                s16
                                s16
                                s16
                                s16
                                ]
                            }
                            \revert TupletBracket.stencil
                            \revert TupletNumber.stencil
                        }
                    }
                    \context Voice = "Voice 2"
                    {
                        \voiceTwo
                        {
                            \scaleDurations #'(1 . 1) {
                                \set stemLeftBeamCount = 0
                                \set stemRightBeamCount = 2
                                c'16
                                [
                                \set stemLeftBeamCount = 2
                                \set stemRightBeamCount = 2
                                d'16
                                \set stemLeftBeamCount = 2
                                \set stemRightBeamCount = 2
                                bf'16
                                \set stemLeftBeamCount = 2
                                \set stemRightBeamCount = 2
                                fs''16
                                \set stemLeftBeamCount = 2
                                \set stemRightBeamCount = 1
                                e''16
                            }
                            \scaleDurations #'(1 . 1) {
                                \set stemLeftBeamCount = 1
                                \set stemRightBeamCount = 2
                                ef''16
                                \set stemLeftBeamCount = 2
                                \set stemRightBeamCount = 2
                                af''16
                                \set stemLeftBeamCount = 2
                                \set stemRightBeamCount = 2
                                g''16
                                \set stemLeftBeamCount = 2
                                \set stemRightBeamCount = 2
                                a'16
                                \set stemLeftBeamCount = 2
                                \set stemRightBeamCount = 1
                                c'16
                            }
                            \scaleDurations #'(1 . 1) {
                                \set stemLeftBeamCount = 1
                                \set stemRightBeamCount = 2
                                d'16
                                \set stemLeftBeamCount = 2
                                \set stemRightBeamCount = 2
                                bf'16
                                \set stemLeftBeamCount = 2
                                \set stemRightBeamCount = 2
                                fs''16
                                \set stemLeftBeamCount = 2
                                \set stemRightBeamCount = 2
                                e''16
                                \set stemLeftBeamCount = 2
                                \set stemRightBeamCount = 0
                                ef''16
                                ]
                            }
                        }
                    }
                    \context Voice = "Voice 3"
                    {
                        \voiceThree
                        {
                            \override TupletBracket.stencil = ##f
                            \override TupletNumber.stencil = ##f
                            \scaleDurations #'(1 . 1) {
                                s16
                                [
                                s16
                                s16
                                s16
                                \set stemLeftBeamCount = 2
                                \set stemRightBeamCount = 1
                                e''16
                                -\accent                                                             %! IC
                            }
                            \scaleDurations #'(1 . 1) {
                                s16
                                s16
                                s16
                                s16
                                s16
                            }
                            \scaleDurations #'(1 . 1) {
                                s16
                                \set stemLeftBeamCount = 2
                                \set stemRightBeamCount = 2
                                bf'16
                                -\accent                                                             %! IC
                                \set stemLeftBeamCount = 2
                                \set stemRightBeamCount = 2
                                fs''16
                                -\accent                                                             %! IC
                                s16
                                s16
                                ]
                            }
                            \revert TupletBracket.stencil
                            \revert TupletNumber.stencil
                        }
                    }
                >>
            >>

    ..  container:: example

        Hides tuplet brackets above imbricated voice:

        >>> music_maker = baca.MusicMaker(
        ...     rmakers.BeamSpecifier(
        ...         beam_divisions_together=True,
        ...         beam_rests=True,
        ...         ),
        ...     baca.staccato(selector=baca.pheads()),
        ...     baca.PitchFirstRhythmCommand(
        ...         rhythm_maker=baca.PitchFirstRhythmMaker(
        ...             talea=rmakers.Talea(
        ...                 counts=[1],
        ...                 denominator=16,
        ...                 ),
        ...             time_treatments=[1],
        ...             ),
        ...         ),
        ...     )

        >>> collections = [
        ...     [0, 2, 10, 18, 16],
        ...     [15, 20, 19, 9, 0],
        ...     [2, 10, 18, 16, 15],
        ...     ]
        >>> contribution = music_maker(
        ...     'Voice 2',
        ...     collections,
        ...     baca.ImbricationCommand(
        ...         'Voice 1',
        ...         [2, 19, 9, 18, 16],
        ...         baca.accent(selector=baca.pheads()),
        ...         baca.beam_everything(),
        ...         ),
        ...     )
        >>> lilypond_file = music_maker.show(contribution)
        >>> abjad.show(lilypond_file, strict=89) # doctest: +SKIP

        ..  docs::

            >>> abjad.f(lilypond_file[abjad.Score], strict=89)
            \new Score
            <<
                \new GlobalContext
                {
                    {   % measure
                        \time 9/8
                        s1 * 9/8
                    }   % measure
                }
                \new Staff
                <<
                    \context Voice = "Voice 1"
                    {
                        \voiceOne
                        {
                            \override TupletBracket.stencil = ##f
                            \override TupletNumber.stencil = ##f
                            \tweak text #tuplet-number::calc-fraction-text
                            \times 6/5 {
                                s16
                                [
                                \set stemLeftBeamCount = 2
                                \set stemRightBeamCount = 2
                                d'16
                                -\accent                                                             %! IC
                                s16
                                s16
                                s16
                            }
                            \tweak text #tuplet-number::calc-fraction-text
                            \times 6/5 {
                                s16
                                s16
                                \set stemLeftBeamCount = 2
                                \set stemRightBeamCount = 2
                                g''16
                                -\accent                                                             %! IC
                                \set stemLeftBeamCount = 2
                                \set stemRightBeamCount = 2
                                a'16
                                -\accent                                                             %! IC
                                s16
                            }
                            \tweak text #tuplet-number::calc-fraction-text
                            \times 6/5 {
                                s16
                                s16
                                \set stemLeftBeamCount = 2
                                \set stemRightBeamCount = 2
                                fs''16
                                -\accent                                                             %! IC
                                \set stemLeftBeamCount = 2
                                \set stemRightBeamCount = 2
                                e''16
                                -\accent                                                             %! IC
                                s16
                                ]
                            }
                            \revert TupletBracket.stencil
                            \revert TupletNumber.stencil
                        }
                    }
                    \context Voice = "Voice 2"
                    {
                        \voiceTwo
                        {
                            \tweak text #tuplet-number::calc-fraction-text
                            \times 6/5 {
                                \set stemLeftBeamCount = 0
                                \set stemRightBeamCount = 2
                                c'16
                                -\staccato                                                           %! IC
                                [
                                \set stemLeftBeamCount = 2
                                \set stemRightBeamCount = 2
                                d'16
                                -\staccato                                                           %! IC
                                \set stemLeftBeamCount = 2
                                \set stemRightBeamCount = 2
                                bf'16
                                -\staccato                                                           %! IC
                                \set stemLeftBeamCount = 2
                                \set stemRightBeamCount = 2
                                fs''16
                                -\staccato                                                           %! IC
                                \set stemLeftBeamCount = 2
                                \set stemRightBeamCount = 1
                                e''16
                                -\staccato                                                           %! IC
                            }
                            \tweak text #tuplet-number::calc-fraction-text
                            \times 6/5 {
                                \set stemLeftBeamCount = 1
                                \set stemRightBeamCount = 2
                                ef''16
                                -\staccato                                                           %! IC
                                \set stemLeftBeamCount = 2
                                \set stemRightBeamCount = 2
                                af''16
                                -\staccato                                                           %! IC
                                \set stemLeftBeamCount = 2
                                \set stemRightBeamCount = 2
                                g''16
                                -\staccato                                                           %! IC
                                \set stemLeftBeamCount = 2
                                \set stemRightBeamCount = 2
                                a'16
                                -\staccato                                                           %! IC
                                \set stemLeftBeamCount = 2
                                \set stemRightBeamCount = 1
                                c'16
                                -\staccato                                                           %! IC
                            }
                            \tweak text #tuplet-number::calc-fraction-text
                            \times 6/5 {
                                \set stemLeftBeamCount = 1
                                \set stemRightBeamCount = 2
                                d'16
                                -\staccato                                                           %! IC
                                \set stemLeftBeamCount = 2
                                \set stemRightBeamCount = 2
                                bf'16
                                -\staccato                                                           %! IC
                                \set stemLeftBeamCount = 2
                                \set stemRightBeamCount = 2
                                fs''16
                                -\staccato                                                           %! IC
                                \set stemLeftBeamCount = 2
                                \set stemRightBeamCount = 2
                                e''16
                                -\staccato                                                           %! IC
                                \set stemLeftBeamCount = 2
                                \set stemRightBeamCount = 0
                                ef''16
                                -\staccato                                                           %! IC
                                ]
                            }
                        }
                    }
                >>
            >>

    """

    ### CLASS VARIABLES ###

    __slots__ = (
        '_allow_unused_pitches',
        '_by_pitch_class',
        '_extend_beam',
        '_hocket',
        '_segment',
        '_selector',
        '_specifiers',
        '_truncate_ties',
        '_voice_name',
        )

    ### INITIALIZER ###

    def __init__(
        self,
        voice_name=None,
        segment=None,
        *specifiers,
        allow_unused_pitches=None,
        by_pitch_class=None,
        extend_beam=None,
        hocket=None,
        selector=None,
        truncate_ties=None
        ):
        if voice_name is not None:
            assert isinstance(voice_name, str), repr(voice_name)
        self._voice_name = voice_name
        self._segment = segment
        self._specifiers = specifiers
        if allow_unused_pitches is not None:
            allow_unused_pitches = bool(allow_unused_pitches)
        self._allow_unused_pitches = allow_unused_pitches
        if by_pitch_class is not None:
            by_pitch_class = bool(by_pitch_class)
        self._by_pitch_class = by_pitch_class
        if extend_beam is not None:
            extend_beam = bool(extend_beam)
        self._extend_beam = extend_beam
        if hocket is not None:
            hocket = bool(hocket)
        self._hocket = hocket
        if selector is not None:
            if not isinstance(selector, abjad.Expression):
                raise TypeError(f'selector or none only: {selector!r}.')
        self._selector = selector
        if truncate_ties is not None:
            truncate_ties = bool(truncate_ties)
        self._truncate_ties = truncate_ties

    ### SPECIAL METHODS ###

    def __call__(self, container=None):
        r"""
        Calls command on ``container``.

        ..  container:: example

            Works with pitch-classes:

            >>> music_maker = baca.MusicMaker(
            ...     baca.PitchFirstRhythmCommand(
            ...         rhythm_maker=baca.PitchFirstRhythmMaker(
            ...             talea=rmakers.Talea(
            ...                 counts=[3],
            ...                 denominator=16,
            ...                 ),
            ...             ),
            ...         ),
            ...     )

            >>> collections = [[0, 2, 10], [18, 16, 15, 20, 19], [9]]
            >>> segment = [
            ...     abjad.NumberedPitchClass(10),
            ...     abjad.NumberedPitchClass(6),
            ...     abjad.NumberedPitchClass(4),
            ...     abjad.NumberedPitchClass(3),
            ...     ]
            >>> contribution = music_maker(
            ...     'Voice 2',
            ...     collections,
            ...     baca.ImbricationCommand(
            ...         'Voice 1',
            ...         segment,
            ...         baca.accent(selector=baca.pheads()),
            ...         baca.beam_everything(),
            ...         ),
            ...     )
            >>> lilypond_file = music_maker.show(contribution)
            >>> abjad.show(lilypond_file, strict=89) # doctest: +SKIP

            ..  docs::

                >>> abjad.f(lilypond_file[abjad.Score], strict=89)
                \new Score
                <<
                    \new GlobalContext
                    {
                        {   % measure
                            \time 27/16
                            s1 * 27/16
                        }   % measure
                    }
                    \new Staff
                    <<
                        \context Voice = "Voice 1"
                        {
                            \voiceOne
                            {
                                \override TupletBracket.stencil = ##f
                                \override TupletNumber.stencil = ##f
                                \scaleDurations #'(1 . 1) {
                                    s8.
                                    [
                                    s8.
                                    \set stemLeftBeamCount = 1
                                    \set stemRightBeamCount = 1
                                    bf'8.
                                    -\accent                                                             %! IC
                                }
                                \scaleDurations #'(1 . 1) {
                                    \set stemLeftBeamCount = 1
                                    \set stemRightBeamCount = 1
                                    fs''8.
                                    -\accent                                                             %! IC
                                    \set stemLeftBeamCount = 1
                                    \set stemRightBeamCount = 1
                                    e''8.
                                    -\accent                                                             %! IC
                                    \set stemLeftBeamCount = 1
                                    \set stemRightBeamCount = 1
                                    ef''8.
                                    -\accent                                                             %! IC
                                    s8.
                                    s8.
                                }
                                \scaleDurations #'(1 . 1) {
                                    s8.
                                    ]
                                }
                                \revert TupletBracket.stencil
                                \revert TupletNumber.stencil
                            }
                        }
                        \context Voice = "Voice 2"
                        {
                            \voiceTwo
                            {
                                \scaleDurations #'(1 . 1) {
                                    c'8.
                                    [
                                    d'8.
                                    bf'8.
                                    ]
                                }
                                \scaleDurations #'(1 . 1) {
                                    fs''8.
                                    [
                                    e''8.
                                    ef''8.
                                    af''8.
                                    g''8.
                                    ]
                                }
                                \scaleDurations #'(1 . 1) {
                                    a'8.
                                }
                            }
                        }
                    >>
                >>

        ..  container:: example

            Skips wrapped pitches:

            >>> music_maker = baca.MusicMaker()

            >>> collections = [
            ...     [0, 2, 10, 18, 16], [15, 20, 19, 9],
            ...     [0, 2, 10, 18, 16], [15, 20, 19, 9],
            ...     ]
            >>> segment = [
            ...     0,
            ...     baca.coat(10),
            ...     baca.coat(18),
            ...     10, 18,
            ...     ]
            >>> contribution = music_maker(
            ...     'Voice 2',
            ...     collections,
            ...     baca.ImbricationCommand(
            ...         'Voice 1',
            ...         segment,
            ...         baca.accent(selector=baca.pheads()),
            ...         baca.beam_everything(),
            ...         ),
            ...     )
            >>> lilypond_file = music_maker.show(contribution)
            >>> abjad.show(lilypond_file, strict=89) # doctest: +SKIP

            ..  docs::

                >>> abjad.f(lilypond_file[abjad.Score], strict=89)
                \new Score
                <<
                    \new GlobalContext
                    {
                        {   % measure
                            \time 9/8
                            s1 * 9/8
                        }   % measure
                    }
                    \new Staff
                    <<
                        \context Voice = "Voice 1"
                        {
                            \voiceOne
                            {
                                \override TupletBracket.stencil = ##f
                                \override TupletNumber.stencil = ##f
                                \scaleDurations #'(1 . 1) {
                                    \set stemLeftBeamCount = 0
                                    \set stemRightBeamCount = 2
                                    c'16
                                    -\accent                                                             %! IC
                                    [
                                    s16
                                    s16
                                    s16
                                    s16
                                }
                                \scaleDurations #'(1 . 1) {
                                    s16
                                    s16
                                    s16
                                    s16
                                }
                                \scaleDurations #'(1 . 1) {
                                    s16
                                    s16
                                    \set stemLeftBeamCount = 2
                                    \set stemRightBeamCount = 2
                                    bf'16
                                    -\accent                                                             %! IC
                                    \set stemLeftBeamCount = 2
                                    \set stemRightBeamCount = 2
                                    fs''16
                                    -\accent                                                             %! IC
                                    s16
                                }
                                \scaleDurations #'(1 . 1) {
                                    s16
                                    s16
                                    s16
                                    s16
                                    ]
                                }
                                \revert TupletBracket.stencil
                                \revert TupletNumber.stencil
                            }
                        }
                        \context Voice = "Voice 2"
                        {
                            \voiceTwo
                            {
                                \scaleDurations #'(1 . 1) {
                                    c'16
                                    [
                                    d'16
                                    bf'16
                                    fs''16
                                    e''16
                                    ]
                                }
                                \scaleDurations #'(1 . 1) {
                                    ef''16
                                    [
                                    af''16
                                    g''16
                                    a'16
                                    ]
                                }
                                \scaleDurations #'(1 . 1) {
                                    c'16
                                    [
                                    d'16
                                    bf'16
                                    fs''16
                                    e''16
                                    ]
                                }
                                \scaleDurations #'(1 . 1) {
                                    ef''16
                                    [
                                    af''16
                                    g''16
                                    a'16
                                    ]
                                }
                            }
                        }
                    >>
                >>

        ..  container:: example

            Segment-maker allows for beam extension.

            Extends beam across figures:

                >>> music_maker = baca.MusicMaker(
                ...     rmakers.BeamSpecifier(
                ...         beam_divisions_together=True,
                ...         ),
                ...     )

            >>> voice_1_selections = []
            >>> voice_2_selections = []
            >>> time_signatures = []
            >>> contribution = music_maker(
            ...     'Voice 2',
            ...     [[0, 2, 10, 18], [16, 15, 23]],
            ...     baca.ImbricationCommand(
            ...         'Voice 1',
            ...         [2, 10],
            ...         baca.staccato(selector=baca.pheads()),
            ...         baca.beam_everything(),
            ...         extend_beam=True,
            ...         ),
            ...     )
            >>> dictionary = contribution.selections
            >>> voice_1_selections.append(dictionary['Voice 1'])
            >>> voice_2_selections.append(dictionary['Voice 2'])
            >>> time_signatures.append(contribution.time_signature)
            >>> contribution = music_maker(
            ...     'Voice 2',
            ...     [[19, 13, 9, 8]],
            ...     baca.ImbricationCommand(
            ...         'Voice 1',
            ...         [13, 9],
            ...         baca.staccato(selector=baca.pheads()),
            ...         baca.beam_everything(),
            ...         ),
            ...     )
            >>> dictionary = contribution.selections
            >>> voice_1_selections.append(dictionary['Voice 1'])
            >>> voice_2_selections.append(dictionary['Voice 2'])
            >>> time_signatures.append(contribution.time_signature)

            >>> maker = baca.SegmentMaker(
            ...     ignore_repeat_pitch_classes=True,
            ...     measures_per_stage=[1, 1],
            ...     score_template=baca.TwoVoiceStaffScoreTemplate(),
            ...     spacing=baca.HorizontalSpacingSpecifier(
            ...         minimum_duration=abjad.Duration(1, 24),
            ...         ),
            ...     time_signatures=time_signatures,
            ...     )
            >>> maker(
            ...     ('MusicVoiceTwo', 1),
            ...     baca.RhythmCommand(
            ...         rhythm_maker=voice_2_selections[0],
            ...         ),
            ...     )
            >>> maker(
            ...     ('MusicVoiceTwo', 2),
            ...     baca.RhythmCommand(
            ...         rhythm_maker=voice_2_selections[1],
            ...         ),
            ...     )
            >>> maker(
            ...     ('MusicVoiceOne', 1),
            ...     baca.RhythmCommand(
            ...         rhythm_maker=voice_1_selections[0],
            ...         ),
            ...     )
            >>> maker(
            ...     ('MusicVoiceOne', 2),
            ...     baca.RhythmCommand(
            ...         rhythm_maker=voice_1_selections[1],
            ...         ),
            ...     )

            >>> lilypond_file = maker.run(environment='docs')

            ..  docs::

                >>> abjad.f(lilypond_file[abjad.Score], strict=89)
                \context Score = "Score"
                <<
                    \context GlobalContext = "GlobalContext"
                    <<
                        \context GlobalSkips = "GlobalSkips"
                        {
                <BLANKLINE>
                            % [GlobalSkips measure 1]                                                    %! SM4
                            \newSpacingSection                                                           %! HSS1:SPACING
                            \set Score.proportionalNotationDuration = #(ly:make-moment 1 24)             %! HSS1:SPACING
                            \time 7/16                                                                   %! SM8:EXPLICIT_TIME_SIGNATURE:SM1
                            \once \override Score.TimeSignature.color = #(x11-color 'blue)               %! SM6:EXPLICIT_TIME_SIGNATURE_COLOR:SM1
                            s1 * 7/16
                <BLANKLINE>
                            % [GlobalSkips measure 2]                                                    %! SM4
                            \newSpacingSection                                                           %! HSS1:SPACING
                            \set Score.proportionalNotationDuration = #(ly:make-moment 1 24)             %! HSS1:SPACING
                            \time 1/4                                                                    %! SM8:EXPLICIT_TIME_SIGNATURE:SM1
                            \once \override Score.TimeSignature.color = #(x11-color 'blue)               %! SM6:EXPLICIT_TIME_SIGNATURE_COLOR:SM1
                            s1 * 1/4
                            \override Score.BarLine.transparent = ##f                                    %! SM5
                            \bar "|"                                                                     %! SM5
                <BLANKLINE>
                        }
                    >>
                    \context MusicContext = "MusicContext"
                    <<
                        \context MusicStaff = "MusicStaff"
                        <<
                            \context MusicVoiceOne = "MusicVoiceOne"
                            {
                                {
                                    \override TupletBracket.stencil = ##f
                                    \override TupletNumber.stencil = ##f
                                    \scaleDurations #'(1 . 1) {
                <BLANKLINE>
                                        % [MusicVoiceOne measure 1]                                      %! SM4
                                        s16
                                        [                                                                %! SM35
                <BLANKLINE>
                                        \set stemLeftBeamCount = 2                                       %! SM35
                                        \set stemRightBeamCount = 2                                      %! SM35
                                        d'16
                                        -\staccato                                                       %! IC
                <BLANKLINE>
                                        \set stemLeftBeamCount = 2                                       %! SM35
                                        \set stemRightBeamCount = 2                                      %! SM35
                                        bf'!16
                                        -\staccato                                                       %! IC
                <BLANKLINE>
                                        s16
                                    }
                                    \scaleDurations #'(1 . 1) {
                <BLANKLINE>
                                        s16
                <BLANKLINE>
                                        s16
                <BLANKLINE>
                                        s16
                                    }
                                    \revert TupletBracket.stencil
                                    \revert TupletNumber.stencil
                                }
                                {
                                    \override TupletBracket.stencil = ##f
                                    \override TupletNumber.stencil = ##f
                                    \scaleDurations #'(1 . 1) {
                <BLANKLINE>
                                        % [MusicVoiceOne measure 2]                                      %! SM4
                                        s16
                <BLANKLINE>
                                        \set stemLeftBeamCount = 2                                       %! SM35
                                        \set stemRightBeamCount = 2                                      %! SM35
                                        cs''!16
                                        -\staccato                                                       %! IC
                <BLANKLINE>
                                        \set stemLeftBeamCount = 2                                       %! SM35
                                        \set stemRightBeamCount = 2                                      %! SM35
                                        a'16
                                        -\staccato                                                       %! IC
                <BLANKLINE>
                                        s16
                                        ]                                                                %! SM35
                <BLANKLINE>
                                    }
                                    \revert TupletBracket.stencil
                                    \revert TupletNumber.stencil
                                }
                            }
                            \context MusicVoiceTwo = "MusicVoiceTwo"
                            {
                                {
                                    \scaleDurations #'(1 . 1) {
                <BLANKLINE>
                                        % [MusicVoiceTwo measure 1]                                      %! SM4
                                        \set stemLeftBeamCount = 0
                                        \set stemRightBeamCount = 2
                                        c'16
                                        [
                <BLANKLINE>
                                        \set stemLeftBeamCount = 2
                                        \set stemRightBeamCount = 2
                                        d'16
                <BLANKLINE>
                                        \set stemLeftBeamCount = 2
                                        \set stemRightBeamCount = 2
                                        bf'!16
                <BLANKLINE>
                                        \set stemLeftBeamCount = 2
                                        \set stemRightBeamCount = 1
                                        fs''!16
                                    }
                                    \scaleDurations #'(1 . 1) {
                <BLANKLINE>
                                        \set stemLeftBeamCount = 1
                                        \set stemRightBeamCount = 2
                                        e''16
                <BLANKLINE>
                                        \set stemLeftBeamCount = 2
                                        \set stemRightBeamCount = 2
                                        ef''!16
                <BLANKLINE>
                                        \set stemLeftBeamCount = 2
                                        \set stemRightBeamCount = 0
                                        b''16
                                        ]
                                    }
                                }
                                {
                                    \scaleDurations #'(1 . 1) {
                <BLANKLINE>
                                        % [MusicVoiceTwo measure 2]                                      %! SM4
                                        \set stemLeftBeamCount = 0
                                        \set stemRightBeamCount = 2
                                        g''16
                                        [
                <BLANKLINE>
                                        \set stemLeftBeamCount = 2
                                        \set stemRightBeamCount = 2
                                        cs''!16
                <BLANKLINE>
                                        \set stemLeftBeamCount = 2
                                        \set stemRightBeamCount = 2
                                        a'16
                <BLANKLINE>
                                        \set stemLeftBeamCount = 2
                                        \set stemRightBeamCount = 0
                                        af'!16
                                        ]
                <BLANKLINE>
                                    }
                                }
                            }
                        >>
                    >>
                >>

        ..  container:: example

            Works with chords:

            >>> music_maker = baca.MusicMaker(
            ...     rmakers.BeamSpecifier(
            ...         beam_divisions_together=True,
            ...         ),
            ...     )

            >>> collections = [
            ...     {0, 2, 10, 18, 16},
            ...     [15, 20, 19, 9, 0],
            ...     [2, 10, 18, 16, 15],
            ...     ]
            >>> contribution = music_maker(
            ...     'Voice 2',
            ...     collections,
            ...     baca.ImbricationCommand(
            ...         'Voice 1',
            ...         [2, 19, 9, 18, 16],
            ...         ),
            ...     )
            >>> lilypond_file = music_maker.show(contribution)
            >>> abjad.show(lilypond_file, strict=89) # doctest: +SKIP

            ..  docs::

                >>> abjad.f(lilypond_file[abjad.Score], strict=89)
                \new Score
                <<
                    \new GlobalContext
                    {
                        {   % measure
                            \time 11/16
                            s1 * 11/16
                        }   % measure
                    }
                    \new Staff
                    <<
                        \context Voice = "Voice 1"
                        {
                            \voiceOne
                            {
                                \override TupletBracket.stencil = ##f
                                \override TupletNumber.stencil = ##f
                                \scaleDurations #'(1 . 1) {
                                    d'16
                                }
                                \scaleDurations #'(1 . 1) {
                                    s16
                                    s16
                                    g''16
                                    [
                                    a'16
                                    ]
                                    s16
                                }
                                \scaleDurations #'(1 . 1) {
                                    s16
                                    s16
                                    fs''16
                                    [
                                    e''16
                                    ]
                                    s16
                                }
                                \revert TupletBracket.stencil
                                \revert TupletNumber.stencil
                            }
                        }
                        \context Voice = "Voice 2"
                        {
                            \voiceTwo
                            {
                                \scaleDurations #'(1 . 1) {
                                    \set stemLeftBeamCount = 0
                                    \set stemRightBeamCount = 2
                                    <c' d' bf' e'' fs''>16
                                    [
                                }
                                \scaleDurations #'(1 . 1) {
                                    \set stemLeftBeamCount = 1
                                    \set stemRightBeamCount = 2
                                    ef''16
                                    \set stemLeftBeamCount = 2
                                    \set stemRightBeamCount = 2
                                    af''16
                                    \set stemLeftBeamCount = 2
                                    \set stemRightBeamCount = 2
                                    g''16
                                    \set stemLeftBeamCount = 2
                                    \set stemRightBeamCount = 2
                                    a'16
                                    \set stemLeftBeamCount = 2
                                    \set stemRightBeamCount = 1
                                    c'16
                                }
                                \scaleDurations #'(1 . 1) {
                                    \set stemLeftBeamCount = 1
                                    \set stemRightBeamCount = 2
                                    d'16
                                    \set stemLeftBeamCount = 2
                                    \set stemRightBeamCount = 2
                                    bf'16
                                    \set stemLeftBeamCount = 2
                                    \set stemRightBeamCount = 2
                                    fs''16
                                    \set stemLeftBeamCount = 2
                                    \set stemRightBeamCount = 2
                                    e''16
                                    \set stemLeftBeamCount = 2
                                    \set stemRightBeamCount = 0
                                    ef''16
                                    ]
                                }
                            }
                        }
                    >>
                >>

        ..  container:: example

            Works with rests:

            >>> music_maker = baca.MusicMaker(
            ...     rmakers.BeamSpecifier(
            ...         beam_divisions_together=True,
            ...         ),
            ...     )

            >>> collections = [
            ...     [0, 2, 10, 18, 16],
            ...     [15, 20, 19, 9, 0],
            ...     [2, 10, 18, 16, 15],
            ...     ]
            >>> contribution = music_maker(
            ...     'Voice 2',
            ...     collections,
            ...     baca.ImbricationCommand(
            ...         'Voice 1',
            ...         [2, 19, 9, 18, 16],
            ...         ),
            ...     baca.rests_around([2], [2]),
            ...     )
            >>> lilypond_file = music_maker.show(contribution)
            >>> abjad.show(lilypond_file, strict=89) # doctest: +SKIP

            ..  docs::

                >>> abjad.f(lilypond_file[abjad.Score], strict=89)
                \new Score
                <<
                    \new GlobalContext
                    {
                        {   % measure
                            \time 19/16
                            s1 * 19/16
                        }   % measure
                    }
                    \new Staff
                    <<
                        \context Voice = "Voice 1"
                        {
                            \voiceOne
                            {
                                \override TupletBracket.stencil = ##f
                                \override TupletNumber.stencil = ##f
                                \scaleDurations #'(1 . 1) {
                                    s8
                                    s16
                                    d'16
                                    s16
                                    s16
                                    s16
                                }
                                \scaleDurations #'(1 . 1) {
                                    s16
                                    s16
                                    g''16
                                    [
                                    a'16
                                    ]
                                    s16
                                }
                                \scaleDurations #'(1 . 1) {
                                    s16
                                    s16
                                    fs''16
                                    [
                                    e''16
                                    ]
                                    s16
                                    s8
                                }
                                \revert TupletBracket.stencil
                                \revert TupletNumber.stencil
                            }
                        }
                        \context Voice = "Voice 2"
                        {
                            \voiceTwo
                            {
                                \scaleDurations #'(1 . 1) {
                                    r8
                                    \set stemLeftBeamCount = 2
                                    \set stemRightBeamCount = 2
                                    c'16
                                    [
                                    \set stemLeftBeamCount = 2
                                    \set stemRightBeamCount = 2
                                    d'16
                                    \set stemLeftBeamCount = 2
                                    \set stemRightBeamCount = 2
                                    bf'16
                                    \set stemLeftBeamCount = 2
                                    \set stemRightBeamCount = 2
                                    fs''16
                                    \set stemLeftBeamCount = 2
                                    \set stemRightBeamCount = 1
                                    e''16
                                }
                                \scaleDurations #'(1 . 1) {
                                    \set stemLeftBeamCount = 1
                                    \set stemRightBeamCount = 2
                                    ef''16
                                    \set stemLeftBeamCount = 2
                                    \set stemRightBeamCount = 2
                                    af''16
                                    \set stemLeftBeamCount = 2
                                    \set stemRightBeamCount = 2
                                    g''16
                                    \set stemLeftBeamCount = 2
                                    \set stemRightBeamCount = 2
                                    a'16
                                    \set stemLeftBeamCount = 2
                                    \set stemRightBeamCount = 1
                                    c'16
                                }
                                \scaleDurations #'(1 . 1) {
                                    \set stemLeftBeamCount = 1
                                    \set stemRightBeamCount = 2
                                    d'16
                                    \set stemLeftBeamCount = 2
                                    \set stemRightBeamCount = 2
                                    bf'16
                                    \set stemLeftBeamCount = 2
                                    \set stemRightBeamCount = 2
                                    fs''16
                                    \set stemLeftBeamCount = 2
                                    \set stemRightBeamCount = 2
                                    e''16
                                    \set stemLeftBeamCount = 2
                                    \set stemRightBeamCount = 2
                                    ef''16
                                    ]
                                    r8
                                }
                            }
                        }
                    >>
                >>

        Returns new container.
        """
        original_container = container
        container = copy.deepcopy(container)
        abjad.override(container).tuplet_bracket.stencil = False
        abjad.override(container).tuplet_number.stencil = False
        segment = baca.sequence(self.segment).flatten(depth=-1)
        if self.by_pitch_class:
            segment = [abjad.NumberedPitchClass(_) for _ in segment]
        cursor = baca.Cursor(
            singletons=True,
            source=segment,
            suppress_exception=True,
            )
        pitch_number = cursor.next()
        if self.selector is not None:
            selection = self.selector(original_container)
        selected_logical_ties = None
        if self.selector is not None:
            selection = self.selector(container)
            agent = abjad.iterate(selection)
            selected_logical_ties = agent.logical_ties(pitched=True)
            selected_logical_ties = list(selected_logical_ties)
        selector = abjad.select(original_container)
        original_logical_ties = selector.logical_ties()
        logical_ties = abjad.select(container).logical_ties()
        pairs = zip(logical_ties, original_logical_ties)
        for logical_tie, original_logical_tie in pairs:
            if (selected_logical_ties is not None and
                logical_tie not in selected_logical_ties):
                for leaf in logical_tie:
                    duration = leaf.written_duration
                    skip = abjad.Skip(duration)
                    abjad.mutate(leaf).replace([skip])
            elif isinstance(logical_tie.head, abjad.Rest):
                for leaf in logical_tie:
                    duration = leaf.written_duration
                    skip = abjad.Skip(duration)
                    abjad.mutate(leaf).replace([skip])
            elif isinstance(logical_tie.head, abjad.Skip):
                pass
            elif self._matches_pitch(logical_tie.head, pitch_number):
                if isinstance(pitch_number, baca.Coat):
                    for leaf in logical_tie:
                        duration = leaf.written_duration
                        skip = abjad.Skip(duration)
                        abjad.mutate(leaf).replace([skip])
                    pitch_number = cursor.next()
                    continue
                self._trim_matching_chord(logical_tie, pitch_number)
                pitch_number = cursor.next()
                if self.truncate_ties:
                    for leaf in logical_tie[1:]:
                        duration = leaf.written_duration
                        skip = abjad.Skip(duration)
                        abjad.mutate(leaf).replace([skip])
                if self.hocket:
                    for leaf in original_logical_tie:
                        duration = leaf.written_duration
                        skip = abjad.Skip(duration)
                        abjad.mutate(leaf).replace([skip])
            else:
                for leaf in logical_tie:
                    duration = leaf.written_duration
                    skip = abjad.Skip(duration)
                    abjad.mutate(leaf).replace([skip])
        if not self.allow_unused_pitches and not cursor.is_exhausted:
            current, total = cursor.position - 1, len(cursor)
            message = f'{cursor!r} used only {current} of {total} pitches.'
            raise Exception(message)
        self._apply_specifiers(container)
        if self.extend_beam:
            last_leaf = abjad.select(container).leaf(-1)
            abjad.attach(abjad.tags.RIGHT_BROKEN_BEAM, last_leaf)
        selection = abjad.select(container)
        if not self.hocket:
            for pleaf in baca.select(container).pleaves():
                abjad.attach(abjad.tags.ALLOW_OCTAVE, pleaf)
        return {self.voice_name: selection}

    ### PRIVATE METHODS ###

    def _apply_specifiers(self, container):
        assert isinstance(container, abjad.Container), repr(container)
        nested_selections = None
        specifiers = self.specifiers or []
        selections = container[:]
        for specifier in specifiers:
            if isinstance(specifier, baca.PitchFirstRhythmCommand):
                continue
            if isinstance(specifier, baca.RhythmCommand):
                continue
            if isinstance(specifier, baca.ImbricationCommand):
                continue
            if isinstance(specifier, rmakers.BeamSpecifier):
                specifier._detach_all_beams(selections)
            if isinstance(specifier, baca.NestingCommand):
                nested_selections = specifier(selections)
            else:
                specifier(selections)
        if nested_selections is not None:
            return nested_selections
        return selections

    @staticmethod
    def _matches_pitch(pitched_leaf, pitch_object):
        if isinstance(pitch_object, baca.Coat):
            pitch_object = pitch_object.argument
        if pitch_object is None:
            return False
        if isinstance(pitched_leaf, abjad.Note):
            written_pitches = [pitched_leaf.written_pitch]
        elif isinstance(pitched_leaf, abjad.Chord):
            written_pitches = pitched_leaf.written_pitches
        else:
            raise TypeError(pitched_leaf)
        if isinstance(pitch_object, (int, float)):
            source = [_.number for _ in written_pitches]
        elif isinstance(pitch_object, abjad.NamedPitch):
            source = written_pitches
        elif isinstance(pitch_object, abjad.NumberedPitch):
            source = [abjad.NumberedPitch(_) for _ in written_pitches]
        elif isinstance(pitch_object, abjad.NamedPitchClass):
            source = [abjad.NamedPitchClass(_) for _ in written_pitches]
        elif isinstance(pitch_object, abjad.NumberedPitchClass):
            source = [abjad.NumberedPitchClass(_) for _ in written_pitches]
        else:
            raise TypeError(f'unknown pitch object: {pitch_object!r}.')
        if not type(source[0]) is type(pitch_object):
            raise TypeError(f'{source!r} type must match {pitch_object!r}.')
        return pitch_object in source

    @staticmethod
    def _trim_matching_chord(logical_tie, pitch_object):
        if isinstance(logical_tie.head, abjad.Note):
            return
        assert isinstance(logical_tie.head, abjad.Chord), repr(logical_tie)
        if isinstance(pitch_object, abjad.PitchClass):
            raise NotImplementedError(logical_tie, pitch_object)
        for chord in logical_tie:
            duration = chord.written_duration
            note = abjad.Note(pitch_object, duration)
            abjad.mutate(chord).replace([note])

    ### PUBLIC PROPERTIES ###

    @property
    def allow_unused_pitches(self):
        r"""
        Is true when specifier allows unused pitches.

        ..  container:: example

            Allows unused pitches:

            >>> music_maker = baca.MusicMaker(
            ...     rmakers.BeamSpecifier(
            ...         beam_divisions_together=True,
            ...         beam_rests=True,
            ...         ),
            ...     baca.staccato(selector=baca.pheads()),
            ...     )

            >>> collections = [
            ...     [0, 2, 10, 18, 16],
            ...     [15, 20, 19, 9, 0],
            ...     ]
            >>> contribution = music_maker(
            ...     'Voice 2',
            ...     collections,
            ...     baca.ImbricationCommand(
            ...         'Voice 1',
            ...         [2, 19, 9, 18, 16],
            ...         baca.accent(selector=baca.pheads()),
            ...         baca.beam_everything(),
            ...         allow_unused_pitches=True,
            ...         ),
            ...     )
            >>> lilypond_file = music_maker.show(contribution)
            >>> abjad.show(lilypond_file, strict=89) # doctest: +SKIP

            ..  docs::

                >>> abjad.f(lilypond_file[abjad.Score], strict=89)
                \new Score
                <<
                    \new GlobalContext
                    {
                        {   % measure
                            \time 5/8
                            s1 * 5/8
                        }   % measure
                    }
                    \new Staff
                    <<
                        \context Voice = "Voice 1"
                        {
                            \voiceOne
                            {
                                \override TupletBracket.stencil = ##f
                                \override TupletNumber.stencil = ##f
                                \scaleDurations #'(1 . 1) {
                                    s16
                                    [
                                    \set stemLeftBeamCount = 2
                                    \set stemRightBeamCount = 2
                                    d'16
                                    -\accent                                                             %! IC
                                    s16
                                    s16
                                    s16
                                }
                                \scaleDurations #'(1 . 1) {
                                    s16
                                    s16
                                    \set stemLeftBeamCount = 2
                                    \set stemRightBeamCount = 2
                                    g''16
                                    -\accent                                                             %! IC
                                    \set stemLeftBeamCount = 2
                                    \set stemRightBeamCount = 2
                                    a'16
                                    -\accent                                                             %! IC
                                    s16
                                    ]
                                }
                                \revert TupletBracket.stencil
                                \revert TupletNumber.stencil
                            }
                        }
                        \context Voice = "Voice 2"
                        {
                            \voiceTwo
                            {
                                \scaleDurations #'(1 . 1) {
                                    \set stemLeftBeamCount = 0
                                    \set stemRightBeamCount = 2
                                    c'16
                                    -\staccato                                                           %! IC
                                    [
                                    \set stemLeftBeamCount = 2
                                    \set stemRightBeamCount = 2
                                    d'16
                                    -\staccato                                                           %! IC
                                    \set stemLeftBeamCount = 2
                                    \set stemRightBeamCount = 2
                                    bf'16
                                    -\staccato                                                           %! IC
                                    \set stemLeftBeamCount = 2
                                    \set stemRightBeamCount = 2
                                    fs''16
                                    -\staccato                                                           %! IC
                                    \set stemLeftBeamCount = 2
                                    \set stemRightBeamCount = 1
                                    e''16
                                    -\staccato                                                           %! IC
                                }
                                \scaleDurations #'(1 . 1) {
                                    \set stemLeftBeamCount = 1
                                    \set stemRightBeamCount = 2
                                    ef''16
                                    -\staccato                                                           %! IC
                                    \set stemLeftBeamCount = 2
                                    \set stemRightBeamCount = 2
                                    af''16
                                    -\staccato                                                           %! IC
                                    \set stemLeftBeamCount = 2
                                    \set stemRightBeamCount = 2
                                    g''16
                                    -\staccato                                                           %! IC
                                    \set stemLeftBeamCount = 2
                                    \set stemRightBeamCount = 2
                                    a'16
                                    -\staccato                                                           %! IC
                                    \set stemLeftBeamCount = 2
                                    \set stemRightBeamCount = 0
                                    c'16
                                    -\staccato                                                           %! IC
                                    ]
                                }
                            }
                        }
                    >>
                >>

        ..  container:: example

            Raises exception on unused pitches:

            >>> music_maker = baca.MusicMaker(
            ...     rmakers.BeamSpecifier(
            ...         beam_divisions_together=True,
            ...         beam_rests=True,
            ...         ),
            ...     baca.staccato(selector=baca.pheads()),
            ...     )

            >>> collections = [
            ...     [0, 2, 10, 18, 16],
            ...     [15, 20, 19, 9, 0],
            ...     ]
            >>> result = music_maker(
            ...     'Voice 2',
            ...     collections,
            ...     baca.ImbricationCommand(
            ...         'Voice 1',
            ...         [2, 19, 9, 18, 16],
            ...         baca.accent(selector=baca.pheads()),
            ...         baca.beam_everything(),
            ...         ),
            ...     )
            Traceback (most recent call last):
                ...
            Exception: Cursor(source=Sequence(items=(2, 19, 9, 18, 16)),
            position=4, singletons=True, suppress_exception=True) used only 3
            of 5 pitches.

        ..  container:: example

            Defaults to none:

            >>> specifier = baca.ImbricationCommand()
            >>> specifier.allow_unused_pitches is None
            True

        Set to true, false or none.

        Returns true, false or none.
        """
        return self._allow_unused_pitches

    @property
    def by_pitch_class(self):
        """
        Is true when specifier matches on pitch-class rather than pitch.

        Set to true, false or none.

        Defaults to none.

        Returns true, false or none.
        """
        return self._by_pitch_class

    @property
    def extend_beam(self):
        """
        Is true when specifier extends beam.

        Set to true, false or none.

        Returns true, false or none.
        """
        return self._extend_beam

    @property
    def hocket(self):
        r"""
        Is true when specifier hockets voices.

        ..  container:: example

            Hockets voices:

            >>> music_maker = baca.MusicMaker(
            ...     rmakers.BeamSpecifier(
            ...         beam_divisions_together=True,
            ...         beam_rests=True,
            ...         ),
            ...     baca.staccato(selector=baca.pheads()),
            ...     )

            >>> collections = [
            ...     [0, 2, 10, 18, 16],
            ...     [15, 20, 19, 9, 0],
            ...     [2, 10, 18, 16, 15],
            ...     ]
            >>> contribution = music_maker(
            ...     'Voice 2',
            ...     collections,
            ...     baca.ImbricationCommand(
            ...         'Voice 1',
            ...         [2, 19, 9, 18, 16],
            ...         baca.accent(selector=baca.pheads()),
            ...         baca.beam_everything(),
            ...         hocket=True,
            ...         ),
            ...     )
            >>> lilypond_file = music_maker.show(contribution)
            >>> abjad.show(lilypond_file, strict=89) # doctest: +SKIP

            ..  docs::

                >>> abjad.f(lilypond_file[abjad.Score], strict=89)
                \new Score
                <<
                    \new GlobalContext
                    {
                        {   % measure
                            \time 15/16
                            s1 * 15/16
                        }   % measure
                    }
                    \new Staff
                    <<
                        \context Voice = "Voice 1"
                        {
                            \voiceOne
                            {
                                \override TupletBracket.stencil = ##f
                                \override TupletNumber.stencil = ##f
                                \scaleDurations #'(1 . 1) {
                                    s16
                                    [
                                    \set stemLeftBeamCount = 2
                                    \set stemRightBeamCount = 2
                                    d'16
                                    -\accent                                                             %! IC
                                    s16
                                    s16
                                    s16
                                }
                                \scaleDurations #'(1 . 1) {
                                    s16
                                    s16
                                    \set stemLeftBeamCount = 2
                                    \set stemRightBeamCount = 2
                                    g''16
                                    -\accent                                                             %! IC
                                    \set stemLeftBeamCount = 2
                                    \set stemRightBeamCount = 2
                                    a'16
                                    -\accent                                                             %! IC
                                    s16
                                }
                                \scaleDurations #'(1 . 1) {
                                    s16
                                    s16
                                    \set stemLeftBeamCount = 2
                                    \set stemRightBeamCount = 2
                                    fs''16
                                    -\accent                                                             %! IC
                                    \set stemLeftBeamCount = 2
                                    \set stemRightBeamCount = 2
                                    e''16
                                    -\accent                                                             %! IC
                                    s16
                                    ]
                                }
                                \revert TupletBracket.stencil
                                \revert TupletNumber.stencil
                            }
                        }
                        \context Voice = "Voice 2"
                        {
                            \voiceTwo
                            {
                                \scaleDurations #'(1 . 1) {
                                    \set stemLeftBeamCount = 0
                                    \set stemRightBeamCount = 2
                                    c'16
                                    -\staccato                                                           %! IC
                                    [
                                    s16
                                    \set stemLeftBeamCount = 2
                                    \set stemRightBeamCount = 2
                                    bf'16
                                    -\staccato                                                           %! IC
                                    \set stemLeftBeamCount = 2
                                    \set stemRightBeamCount = 2
                                    fs''16
                                    -\staccato                                                           %! IC
                                    \set stemLeftBeamCount = 2
                                    \set stemRightBeamCount = 1
                                    e''16
                                    -\staccato                                                           %! IC
                                }
                                \scaleDurations #'(1 . 1) {
                                    \set stemLeftBeamCount = 1
                                    \set stemRightBeamCount = 2
                                    ef''16
                                    -\staccato                                                           %! IC
                                    \set stemLeftBeamCount = 2
                                    \set stemRightBeamCount = 2
                                    af''16
                                    -\staccato                                                           %! IC
                                    s16
                                    s16
                                    \set stemLeftBeamCount = 2
                                    \set stemRightBeamCount = 1
                                    c'16
                                    -\staccato                                                           %! IC
                                }
                                \scaleDurations #'(1 . 1) {
                                    \set stemLeftBeamCount = 1
                                    \set stemRightBeamCount = 2
                                    d'16
                                    -\staccato                                                           %! IC
                                    \set stemLeftBeamCount = 2
                                    \set stemRightBeamCount = 2
                                    bf'16
                                    -\staccato                                                           %! IC
                                    s16
                                    s16
                                    \set stemLeftBeamCount = 2
                                    \set stemRightBeamCount = 0
                                    ef''16
                                    -\staccato                                                           %! IC
                                    ]
                                }
                            }
                        }
                    >>
                >>

        ..  container:: example

            Defaults to none:

            >>> specifier = baca.ImbricationCommand()
            >>> specifier.hocket is None
            True

        Set to true, false or none.

        Returns true, false or none.
        """
        return self._hocket

    @property
    def segment(self):
        """
        Gets to-be-imbricated segment.

        Returns pitch or pitch-class segment.
        """
        return self._segment

    @property
    def selector(self):
        r"""
        Gets selector.

        ..  container:: example

            Selects last nine notes:

            >>> music_maker = baca.MusicMaker(
            ...     rmakers.BeamSpecifier(
            ...         beam_divisions_together=True,
            ...         beam_rests=True,
            ...         ),
            ...     baca.staccato(selector=baca.pheads()),
            ...     )

            >>> collections = [
            ...     [0, 2, 10, 18, 16], [15, 20, 19, 9],
            ...     [0, 2, 10, 18, 16], [15, 20, 19, 9],
            ...     ]
            >>> contribution = music_maker(
            ...     'Voice 2',
            ...     collections,
            ...     baca.ImbricationCommand(
            ...         'Voice 1',
            ...         [2, 18, 16, 15],
            ...         baca.accent(selector=baca.pheads()),
            ...         baca.beam_everything(),
            ...         selector=baca.plts()[-9:],
            ...         ),
            ...     )
            >>> lilypond_file = music_maker.show(contribution)
            >>> abjad.show(lilypond_file, strict=89) # doctest: +SKIP

            ..  docs::

                >>> abjad.f(lilypond_file[abjad.Score], strict=89)
                \new Score
                <<
                    \new GlobalContext
                    {
                        {   % measure
                            \time 9/8
                            s1 * 9/8
                        }   % measure
                    }
                    \new Staff
                    <<
                        \context Voice = "Voice 1"
                        {
                            \voiceOne
                            {
                                \override TupletBracket.stencil = ##f
                                \override TupletNumber.stencil = ##f
                                \scaleDurations #'(1 . 1) {
                                    s16
                                    [
                                    s16
                                    s16
                                    s16
                                    s16
                                }
                                \scaleDurations #'(1 . 1) {
                                    s16
                                    s16
                                    s16
                                    s16
                                }
                                \scaleDurations #'(1 . 1) {
                                    s16
                                    \set stemLeftBeamCount = 2
                                    \set stemRightBeamCount = 2
                                    d'16
                                    -\accent                                                             %! IC
                                    s16
                                    \set stemLeftBeamCount = 2
                                    \set stemRightBeamCount = 2
                                    fs''16
                                    -\accent                                                             %! IC
                                    \set stemLeftBeamCount = 2
                                    \set stemRightBeamCount = 1
                                    e''16
                                    -\accent                                                             %! IC
                                }
                                \scaleDurations #'(1 . 1) {
                                    \set stemLeftBeamCount = 1
                                    \set stemRightBeamCount = 2
                                    ef''16
                                    -\accent                                                             %! IC
                                    s16
                                    s16
                                    s16
                                    ]
                                }
                                \revert TupletBracket.stencil
                                \revert TupletNumber.stencil
                            }
                        }
                        \context Voice = "Voice 2"
                        {
                            \voiceTwo
                            {
                                \scaleDurations #'(1 . 1) {
                                    \set stemLeftBeamCount = 0
                                    \set stemRightBeamCount = 2
                                    c'16
                                    -\staccato                                                           %! IC
                                    [
                                    \set stemLeftBeamCount = 2
                                    \set stemRightBeamCount = 2
                                    d'16
                                    -\staccato                                                           %! IC
                                    \set stemLeftBeamCount = 2
                                    \set stemRightBeamCount = 2
                                    bf'16
                                    -\staccato                                                           %! IC
                                    \set stemLeftBeamCount = 2
                                    \set stemRightBeamCount = 2
                                    fs''16
                                    -\staccato                                                           %! IC
                                    \set stemLeftBeamCount = 2
                                    \set stemRightBeamCount = 1
                                    e''16
                                    -\staccato                                                           %! IC
                                }
                                \scaleDurations #'(1 . 1) {
                                    \set stemLeftBeamCount = 1
                                    \set stemRightBeamCount = 2
                                    ef''16
                                    -\staccato                                                           %! IC
                                    \set stemLeftBeamCount = 2
                                    \set stemRightBeamCount = 2
                                    af''16
                                    -\staccato                                                           %! IC
                                    \set stemLeftBeamCount = 2
                                    \set stemRightBeamCount = 2
                                    g''16
                                    -\staccato                                                           %! IC
                                    \set stemLeftBeamCount = 2
                                    \set stemRightBeamCount = 1
                                    a'16
                                    -\staccato                                                           %! IC
                                }
                                \scaleDurations #'(1 . 1) {
                                    \set stemLeftBeamCount = 1
                                    \set stemRightBeamCount = 2
                                    c'16
                                    -\staccato                                                           %! IC
                                    \set stemLeftBeamCount = 2
                                    \set stemRightBeamCount = 2
                                    d'16
                                    -\staccato                                                           %! IC
                                    \set stemLeftBeamCount = 2
                                    \set stemRightBeamCount = 2
                                    bf'16
                                    -\staccato                                                           %! IC
                                    \set stemLeftBeamCount = 2
                                    \set stemRightBeamCount = 2
                                    fs''16
                                    -\staccato                                                           %! IC
                                    \set stemLeftBeamCount = 2
                                    \set stemRightBeamCount = 1
                                    e''16
                                    -\staccato                                                           %! IC
                                }
                                \scaleDurations #'(1 . 1) {
                                    \set stemLeftBeamCount = 1
                                    \set stemRightBeamCount = 2
                                    ef''16
                                    -\staccato                                                           %! IC
                                    \set stemLeftBeamCount = 2
                                    \set stemRightBeamCount = 2
                                    af''16
                                    -\staccato                                                           %! IC
                                    \set stemLeftBeamCount = 2
                                    \set stemRightBeamCount = 2
                                    g''16
                                    -\staccato                                                           %! IC
                                    \set stemLeftBeamCount = 2
                                    \set stemRightBeamCount = 0
                                    a'16
                                    -\staccato                                                           %! IC
                                    ]
                                }
                            }
                        }
                    >>
                >>

        ..  container:: example

            Defaults to none:

            >>> specifier = baca.ImbricationCommand()
            >>> specifier.selector is None
            True

        Set to selector or none.

        Returns selector or none.
        """
        return self._selector

    @property
    def specifiers(self):
        r"""
        Gets specifiers.

        ..  container:: example

            Beams nothing:

            >>> music_maker = baca.MusicMaker(
            ...     rmakers.BeamSpecifier(
            ...         beam_divisions_together=True,
            ...         ),
            ...     )

            >>> collections = [
            ...     [0, 2, 10, 18, 16],
            ...     [15, 20, 19, 9, 0],
            ...     [2, 10, 18, 16, 15],
            ...     ]
            >>> contribution = music_maker(
            ...     'Voice 2',
            ...     collections,
            ...     baca.ImbricationCommand(
            ...         'Voice 1',
            ...         [2, 19, 9, 18, 16],
            ...         rmakers.BeamSpecifier(
            ...             beam_each_division=False,
            ...             ),
            ...         ),
            ...     )
            >>> lilypond_file = music_maker.show(contribution)
            >>> abjad.show(lilypond_file, strict=89) # doctest: +SKIP

            ..  docs::

                >>> abjad.f(lilypond_file[abjad.Score], strict=89)
                \new Score
                <<
                    \new GlobalContext
                    {
                        {   % measure
                            \time 15/16
                            s1 * 15/16
                        }   % measure
                    }
                    \new Staff
                    <<
                        \context Voice = "Voice 1"
                        {
                            \voiceOne
                            {
                                \override TupletBracket.stencil = ##f
                                \override TupletNumber.stencil = ##f
                                \scaleDurations #'(1 . 1) {
                                    s16
                                    d'16
                                    s16
                                    s16
                                    s16
                                }
                                \scaleDurations #'(1 . 1) {
                                    s16
                                    s16
                                    g''16
                                    a'16
                                    s16
                                }
                                \scaleDurations #'(1 . 1) {
                                    s16
                                    s16
                                    fs''16
                                    e''16
                                    s16
                                }
                                \revert TupletBracket.stencil
                                \revert TupletNumber.stencil
                            }
                        }
                        \context Voice = "Voice 2"
                        {
                            \voiceTwo
                            {
                                \scaleDurations #'(1 . 1) {
                                    \set stemLeftBeamCount = 0
                                    \set stemRightBeamCount = 2
                                    c'16
                                    [
                                    \set stemLeftBeamCount = 2
                                    \set stemRightBeamCount = 2
                                    d'16
                                    \set stemLeftBeamCount = 2
                                    \set stemRightBeamCount = 2
                                    bf'16
                                    \set stemLeftBeamCount = 2
                                    \set stemRightBeamCount = 2
                                    fs''16
                                    \set stemLeftBeamCount = 2
                                    \set stemRightBeamCount = 1
                                    e''16
                                }
                                \scaleDurations #'(1 . 1) {
                                    \set stemLeftBeamCount = 1
                                    \set stemRightBeamCount = 2
                                    ef''16
                                    \set stemLeftBeamCount = 2
                                    \set stemRightBeamCount = 2
                                    af''16
                                    \set stemLeftBeamCount = 2
                                    \set stemRightBeamCount = 2
                                    g''16
                                    \set stemLeftBeamCount = 2
                                    \set stemRightBeamCount = 2
                                    a'16
                                    \set stemLeftBeamCount = 2
                                    \set stemRightBeamCount = 1
                                    c'16
                                }
                                \scaleDurations #'(1 . 1) {
                                    \set stemLeftBeamCount = 1
                                    \set stemRightBeamCount = 2
                                    d'16
                                    \set stemLeftBeamCount = 2
                                    \set stemRightBeamCount = 2
                                    bf'16
                                    \set stemLeftBeamCount = 2
                                    \set stemRightBeamCount = 2
                                    fs''16
                                    \set stemLeftBeamCount = 2
                                    \set stemRightBeamCount = 2
                                    e''16
                                    \set stemLeftBeamCount = 2
                                    \set stemRightBeamCount = 0
                                    ef''16
                                    ]
                                }
                            }
                        }
                    >>
                >>

        ..  container:: example

            Beams divisions together but excludes skips:

            >>> music_maker = baca.MusicMaker(
            ...     rmakers.BeamSpecifier(
            ...         beam_divisions_together=True,
            ...         ),
            ...     )

            >>> collections = [
            ...     [0, 2, 10, 18, 16],
            ...     [15, 20, 19, 9, 0],
            ...     [2, 10, 18, 16, 15],
            ...     ]
            >>> contribution = music_maker(
            ...     'Voice 2',
            ...     collections,
            ...     baca.ImbricationCommand(
            ...         'Voice 1',
            ...         [2, 19, 9, 18, 16],
            ...         rmakers.BeamSpecifier(
            ...             beam_divisions_together=True,
            ...             ),
            ...         ),
            ...     )
            >>> lilypond_file = music_maker.show(contribution)
            >>> abjad.show(lilypond_file, strict=89) # doctest: +SKIP

            ..  docs::

                >>> abjad.f(lilypond_file[abjad.Score], strict=89)
                \new Score
                <<
                    \new GlobalContext
                    {
                        {   % measure
                            \time 15/16
                            s1 * 15/16
                        }   % measure
                    }
                    \new Staff
                    <<
                        \context Voice = "Voice 1"
                        {
                            \voiceOne
                            {
                                \override TupletBracket.stencil = ##f
                                \override TupletNumber.stencil = ##f
                                \scaleDurations #'(1 . 1) {
                                    s16
                                    \set stemLeftBeamCount = 2
                                    \set stemRightBeamCount = 2
                                    d'16
                                    [
                                    ]
                                    s16
                                    s16
                                    s16
                                }
                                \scaleDurations #'(1 . 1) {
                                    s16
                                    s16
                                    \set stemLeftBeamCount = 2
                                    \set stemRightBeamCount = 2
                                    g''16
                                    [
                                    \set stemLeftBeamCount = 2
                                    \set stemRightBeamCount = 2
                                    a'16
                                    ]
                                    s16
                                }
                                \scaleDurations #'(1 . 1) {
                                    s16
                                    s16
                                    \set stemLeftBeamCount = 2
                                    \set stemRightBeamCount = 2
                                    fs''16
                                    [
                                    \set stemLeftBeamCount = 2
                                    \set stemRightBeamCount = 2
                                    e''16
                                    ]
                                    s16
                                }
                                \revert TupletBracket.stencil
                                \revert TupletNumber.stencil
                            }
                        }
                        \context Voice = "Voice 2"
                        {
                            \voiceTwo
                            {
                                \scaleDurations #'(1 . 1) {
                                    \set stemLeftBeamCount = 0
                                    \set stemRightBeamCount = 2
                                    c'16
                                    [
                                    \set stemLeftBeamCount = 2
                                    \set stemRightBeamCount = 2
                                    d'16
                                    \set stemLeftBeamCount = 2
                                    \set stemRightBeamCount = 2
                                    bf'16
                                    \set stemLeftBeamCount = 2
                                    \set stemRightBeamCount = 2
                                    fs''16
                                    \set stemLeftBeamCount = 2
                                    \set stemRightBeamCount = 1
                                    e''16
                                }
                                \scaleDurations #'(1 . 1) {
                                    \set stemLeftBeamCount = 1
                                    \set stemRightBeamCount = 2
                                    ef''16
                                    \set stemLeftBeamCount = 2
                                    \set stemRightBeamCount = 2
                                    af''16
                                    \set stemLeftBeamCount = 2
                                    \set stemRightBeamCount = 2
                                    g''16
                                    \set stemLeftBeamCount = 2
                                    \set stemRightBeamCount = 2
                                    a'16
                                    \set stemLeftBeamCount = 2
                                    \set stemRightBeamCount = 1
                                    c'16
                                }
                                \scaleDurations #'(1 . 1) {
                                    \set stemLeftBeamCount = 1
                                    \set stemRightBeamCount = 2
                                    d'16
                                    \set stemLeftBeamCount = 2
                                    \set stemRightBeamCount = 2
                                    bf'16
                                    \set stemLeftBeamCount = 2
                                    \set stemRightBeamCount = 2
                                    fs''16
                                    \set stemLeftBeamCount = 2
                                    \set stemRightBeamCount = 2
                                    e''16
                                    \set stemLeftBeamCount = 2
                                    \set stemRightBeamCount = 0
                                    ef''16
                                    ]
                                }
                            }
                        }
                    >>
                >>

        ..  container:: example

            Beams divisions together and includes skips:

            >>> music_maker = baca.MusicMaker(
            ...     rmakers.BeamSpecifier(
            ...         beam_divisions_together=True,
            ...         ),
            ...     )

            >>> collections = [
            ...     [0, 2, 10, 18, 16],
            ...     [15, 20, 19, 9, 0],
            ...     [2, 10, 18, 16, 15],
            ...     ]
            >>> contribution = music_maker(
            ...     'Voice 2',
            ...     collections,
            ...     baca.ImbricationCommand(
            ...         'Voice 1',
            ...         [2, 19, 9, 18, 16],
            ...         baca.beam_everything(),
            ...         ),
            ...     )
            >>> lilypond_file = music_maker.show(contribution)
            >>> abjad.show(lilypond_file, strict=89) # doctest: +SKIP

            ..  docs::

                >>> abjad.f(lilypond_file[abjad.Score], strict=89)
                \new Score
                <<
                    \new GlobalContext
                    {
                        {   % measure
                            \time 15/16
                            s1 * 15/16
                        }   % measure
                    }
                    \new Staff
                    <<
                        \context Voice = "Voice 1"
                        {
                            \voiceOne
                            {
                                \override TupletBracket.stencil = ##f
                                \override TupletNumber.stencil = ##f
                                \scaleDurations #'(1 . 1) {
                                    s16
                                    [
                                    \set stemLeftBeamCount = 2
                                    \set stemRightBeamCount = 2
                                    d'16
                                    s16
                                    s16
                                    s16
                                }
                                \scaleDurations #'(1 . 1) {
                                    s16
                                    s16
                                    \set stemLeftBeamCount = 2
                                    \set stemRightBeamCount = 2
                                    g''16
                                    \set stemLeftBeamCount = 2
                                    \set stemRightBeamCount = 2
                                    a'16
                                    s16
                                }
                                \scaleDurations #'(1 . 1) {
                                    s16
                                    s16
                                    \set stemLeftBeamCount = 2
                                    \set stemRightBeamCount = 2
                                    fs''16
                                    \set stemLeftBeamCount = 2
                                    \set stemRightBeamCount = 2
                                    e''16
                                    s16
                                    ]
                                }
                                \revert TupletBracket.stencil
                                \revert TupletNumber.stencil
                            }
                        }
                        \context Voice = "Voice 2"
                        {
                            \voiceTwo
                            {
                                \scaleDurations #'(1 . 1) {
                                    \set stemLeftBeamCount = 0
                                    \set stemRightBeamCount = 2
                                    c'16
                                    [
                                    \set stemLeftBeamCount = 2
                                    \set stemRightBeamCount = 2
                                    d'16
                                    \set stemLeftBeamCount = 2
                                    \set stemRightBeamCount = 2
                                    bf'16
                                    \set stemLeftBeamCount = 2
                                    \set stemRightBeamCount = 2
                                    fs''16
                                    \set stemLeftBeamCount = 2
                                    \set stemRightBeamCount = 1
                                    e''16
                                }
                                \scaleDurations #'(1 . 1) {
                                    \set stemLeftBeamCount = 1
                                    \set stemRightBeamCount = 2
                                    ef''16
                                    \set stemLeftBeamCount = 2
                                    \set stemRightBeamCount = 2
                                    af''16
                                    \set stemLeftBeamCount = 2
                                    \set stemRightBeamCount = 2
                                    g''16
                                    \set stemLeftBeamCount = 2
                                    \set stemRightBeamCount = 2
                                    a'16
                                    \set stemLeftBeamCount = 2
                                    \set stemRightBeamCount = 1
                                    c'16
                                }
                                \scaleDurations #'(1 . 1) {
                                    \set stemLeftBeamCount = 1
                                    \set stemRightBeamCount = 2
                                    d'16
                                    \set stemLeftBeamCount = 2
                                    \set stemRightBeamCount = 2
                                    bf'16
                                    \set stemLeftBeamCount = 2
                                    \set stemRightBeamCount = 2
                                    fs''16
                                    \set stemLeftBeamCount = 2
                                    \set stemRightBeamCount = 2
                                    e''16
                                    \set stemLeftBeamCount = 2
                                    \set stemRightBeamCount = 0
                                    ef''16
                                    ]
                                }
                            }
                        }
                    >>
                >>

        ..  container:: example

            Beams each division and includes skips:

            >>> music_maker = baca.MusicMaker(
            ...     rmakers.BeamSpecifier(
            ...         beam_divisions_together=True,
            ...         ),
            ...     )

            >>> collections = [
            ...     [0, 2, 10, 18, 16],
            ...     [15, 20, 19, 9, 0],
            ...     [2, 10, 18, 16, 15],
            ...     ]
            >>> contribution = music_maker(
            ...     'Voice 2',
            ...     collections,
            ...     baca.ImbricationCommand(
            ...         'Voice 1',
            ...         [2, 19, 9, 18, 16],
            ...         rmakers.BeamSpecifier(
            ...             beam_rests=True,
            ...             ),
            ...         ),
            ...     )
            >>> lilypond_file = music_maker.show(contribution)
            >>> abjad.show(lilypond_file, strict=89) # doctest: +SKIP

            ..  docs::

                >>> abjad.f(lilypond_file[abjad.Score], strict=89)
                \new Score
                <<
                    \new GlobalContext
                    {
                        {   % measure
                            \time 15/16
                            s1 * 15/16
                        }   % measure
                    }
                    \new Staff
                    <<
                        \context Voice = "Voice 1"
                        {
                            \voiceOne
                            {
                                \override TupletBracket.stencil = ##f
                                \override TupletNumber.stencil = ##f
                                \scaleDurations #'(1 . 1) {
                                    s16
                                    [
                                    d'16
                                    s16
                                    s16
                                    s16
                                    ]
                                }
                                \scaleDurations #'(1 . 1) {
                                    s16
                                    [
                                    s16
                                    g''16
                                    a'16
                                    s16
                                    ]
                                }
                                \scaleDurations #'(1 . 1) {
                                    s16
                                    [
                                    s16
                                    fs''16
                                    e''16
                                    s16
                                    ]
                                }
                                \revert TupletBracket.stencil
                                \revert TupletNumber.stencil
                            }
                        }
                        \context Voice = "Voice 2"
                        {
                            \voiceTwo
                            {
                                \scaleDurations #'(1 . 1) {
                                    \set stemLeftBeamCount = 0
                                    \set stemRightBeamCount = 2
                                    c'16
                                    [
                                    \set stemLeftBeamCount = 2
                                    \set stemRightBeamCount = 2
                                    d'16
                                    \set stemLeftBeamCount = 2
                                    \set stemRightBeamCount = 2
                                    bf'16
                                    \set stemLeftBeamCount = 2
                                    \set stemRightBeamCount = 2
                                    fs''16
                                    \set stemLeftBeamCount = 2
                                    \set stemRightBeamCount = 1
                                    e''16
                                }
                                \scaleDurations #'(1 . 1) {
                                    \set stemLeftBeamCount = 1
                                    \set stemRightBeamCount = 2
                                    ef''16
                                    \set stemLeftBeamCount = 2
                                    \set stemRightBeamCount = 2
                                    af''16
                                    \set stemLeftBeamCount = 2
                                    \set stemRightBeamCount = 2
                                    g''16
                                    \set stemLeftBeamCount = 2
                                    \set stemRightBeamCount = 2
                                    a'16
                                    \set stemLeftBeamCount = 2
                                    \set stemRightBeamCount = 1
                                    c'16
                                }
                                \scaleDurations #'(1 . 1) {
                                    \set stemLeftBeamCount = 1
                                    \set stemRightBeamCount = 2
                                    d'16
                                    \set stemLeftBeamCount = 2
                                    \set stemRightBeamCount = 2
                                    bf'16
                                    \set stemLeftBeamCount = 2
                                    \set stemRightBeamCount = 2
                                    fs''16
                                    \set stemLeftBeamCount = 2
                                    \set stemRightBeamCount = 2
                                    e''16
                                    \set stemLeftBeamCount = 2
                                    \set stemRightBeamCount = 0
                                    ef''16
                                    ]
                                }
                            }
                        }
                    >>
                >>

        Returns specifiers or none.
        """
        return list(self._specifiers)

    @property
    def truncate_ties(self):
        r"""
        Is true when specifier truncates ties.

        ..  container:: example

            Truncates ties:

            >>> music_maker = baca.MusicMaker(
            ...     baca.PitchFirstRhythmCommand(
            ...         rhythm_maker=baca.PitchFirstRhythmMaker(
            ...             talea=rmakers.Talea(
            ...                 counts=[5],
            ...                 denominator=32,
            ...                 ),
            ...             ),
            ...         ),
            ...     )

            >>> collections = [[0, 2, 10], [18, 16, 15, 20, 19], [9]]
            >>> contribution = music_maker(
            ...     'Voice 2',
            ...     collections,
            ...     baca.ImbricationCommand(
            ...         'Voice 1',
            ...         [2, 10, 18, 19, 9],
            ...         baca.beam_everything(),
            ...         truncate_ties=True,
            ...         ),
            ...     )
            >>> lilypond_file = music_maker.show(contribution)
            >>> abjad.show(lilypond_file, strict=89) # doctest: +SKIP

            ..  docs::

                >>> abjad.f(lilypond_file[abjad.Score], strict=89)
                \new Score
                <<
                    \new GlobalContext
                    {
                        {   % measure
                            \time 45/32
                            s1 * 45/32
                        }   % measure
                    }
                    \new Staff
                    <<
                        \context Voice = "Voice 1"
                        {
                            \voiceOne
                            {
                                \override TupletBracket.stencil = ##f
                                \override TupletNumber.stencil = ##f
                                \scaleDurations #'(1 . 1) {
                                    s8
                                    [
                                    s32
                                    \set stemLeftBeamCount = 1
                                    \set stemRightBeamCount = 1
                                    d'8
                                    s32
                                    \set stemLeftBeamCount = 1
                                    \set stemRightBeamCount = 1
                                    bf'8
                                    s32
                                }
                                \scaleDurations #'(1 . 1) {
                                    \set stemLeftBeamCount = 1
                                    \set stemRightBeamCount = 1
                                    fs''8
                                    s32
                                    s8
                                    s32
                                    s8
                                    s32
                                    s8
                                    s32
                                    \set stemLeftBeamCount = 1
                                    \set stemRightBeamCount = 1
                                    g''8
                                    s32
                                }
                                \scaleDurations #'(1 . 1) {
                                    \set stemLeftBeamCount = 1
                                    \set stemRightBeamCount = 1
                                    a'8
                                    s32
                                    ]
                                }
                                \revert TupletBracket.stencil
                                \revert TupletNumber.stencil
                            }
                        }
                        \context Voice = "Voice 2"
                        {
                            \voiceTwo
                            {
                                \scaleDurations #'(1 . 1) {
                                    c'8
                                    ~
                                    [
                                    c'32
                                    d'8
                                    ~
                                    d'32
                                    bf'8
                                    ~
                                    bf'32
                                    ]
                                }
                                \scaleDurations #'(1 . 1) {
                                    fs''8
                                    ~
                                    [
                                    fs''32
                                    e''8
                                    ~
                                    e''32
                                    ef''8
                                    ~
                                    ef''32
                                    af''8
                                    ~
                                    af''32
                                    g''8
                                    ~
                                    g''32
                                    ]
                                }
                                \scaleDurations #'(1 . 1) {
                                    a'8
                                    ~
                                    [
                                    a'32
                                    ]
                                }
                            }
                        }
                    >>
                >>

        ..  container:: example

            Defaults to none:

            >>> specifier = baca.ImbricationCommand()
            >>> specifier.truncate_ties is None
            True

        Set to true, false or none.

        Returns true, false or none.
        """
        return self._truncate_ties

    @property
    def voice_name(self):
        """
        Gets voice name.

        Returns string.
        """
        return self._voice_name