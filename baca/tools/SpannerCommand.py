import abjad
import baca
from .Command import Command


class SpannerCommand(Command):
    r'''Spanner command.

    ..  container:: example

        With music-maker:

        >>> music_maker = baca.MusicMaker(
        ...     baca.SpannerCommand(
        ...         selector=baca.tuplet(1),
        ...         spanner=abjad.Slur(),
        ...         ),
        ...     )

        >>> collections = [[0, 2, 10], [18, 16, 15, 20, 19], [9]]
        >>> contribution = music_maker('Voice 1', collections)
        >>> lilypond_file = music_maker.show(contribution)
        >>> abjad.show(lilypond_file, strict=89) # doctest: +SKIP

        ..  docs::

            >>> abjad.f(lilypond_file[abjad.Staff], strict=89)
            \new Staff <<
                \context Voice = "Voice 1" {
                    \voiceOne
                    {
                        {
                            c'16
                            [
                            d'16
                            bf'16
                            ]
                        }
                        {
                            fs''16
                            [
                            (                                                                        %! SC
                            e''16
                            ef''16
                            af''16
                            g''16
                            ]
                            )                                                                        %! SC
                        }
                        {
                            a'16
                        }
                    }
                }
            >>

    ..  container:: example

        With segment-maker:

        >>> maker = baca.SegmentMaker(
        ...     score_template=baca.SingleStaffScoreTemplate(),
        ...     time_signatures=[(4, 8), (3, 8), (4, 8), (3, 8)],
        ...     )

        >>> maker(
        ...     baca.scope('MusicVoice', 1),
        ...     baca.make_even_runs(),
        ...     baca.pitches('E4 D5 F4 E5 G4 F5'),
        ...     baca.SpannerCommand(
        ...         selector=baca.leaves()[4:7],
        ...         spanner=abjad.Slur(),
        ...         ),
        ...     )

        >>> lilypond_file = maker.run(environment='docs')
        >>> abjad.show(lilypond_file, strict=89) # doctest: +SKIP

        ..  docs::

            >>> abjad.f(lilypond_file[abjad.Score], strict=89)
            \context Score = "Score" <<
                \context GlobalContext = "GlobalContext" <<
                    \context GlobalSkips = "GlobalSkips" {
            <BLANKLINE>
                        % GlobalSkips [measure 1]                                                    %! SM4
                        \once \override TextSpanner.Y-extent = ##f                                   %! SM29
                        \once \override TextSpanner.bound-details.left-broken.text = ##f             %! SM29
                        \once \override TextSpanner.bound-details.left.stencil-align-dir-y = #center %! SM29
                        \once \override TextSpanner.bound-details.right-broken.padding = 0           %! SM29
                        \once \override TextSpanner.bound-details.right-broken.text = ##f            %! SM29
                        \once \override TextSpanner.bound-details.right.padding = 0                  %! SM29
                        \once \override TextSpanner.bound-details.right.stencil-align-dir-y = #center %! SM29
                        \once \override TextSpanner.dash-period = 0                                  %! SM29
                        \time 4/8                                                                    %! EXPLICIT_TIME_SIGNATURE:SM8
                        \bar ""                                                                      %! EMPTY_START_BAR:SM2
                        \once \override Score.TimeSignature.color = #(x11-color 'blue)               %! EXPLICIT_TIME_SIGNATURE_COLOR:SM6
                        s1 * 1/2
                        \startTextSpan                                                               %! SM29
                        ^ \markup {                                                                  %! STAGE_NUMBER_MARKUP:SM3
                            \fontsize                                                                %! STAGE_NUMBER_MARKUP:SM3
                                #-3                                                                  %! STAGE_NUMBER_MARKUP:SM3
                                \with-color                                                          %! STAGE_NUMBER_MARKUP:SM3
                                    #(x11-color 'DarkCyan)                                           %! STAGE_NUMBER_MARKUP:SM3
                                    [1]                                                              %! STAGE_NUMBER_MARKUP:SM3
                            }                                                                        %! STAGE_NUMBER_MARKUP:SM3
            <BLANKLINE>
                        % GlobalSkips [measure 2]                                                    %! SM4
                        \time 3/8                                                                    %! EXPLICIT_TIME_SIGNATURE:SM8
                        \once \override Score.TimeSignature.color = #(x11-color 'blue)               %! EXPLICIT_TIME_SIGNATURE_COLOR:SM6
                        s1 * 3/8
            <BLANKLINE>
                        % GlobalSkips [measure 3]                                                    %! SM4
                        \time 4/8                                                                    %! EXPLICIT_TIME_SIGNATURE:SM8
                        \once \override Score.TimeSignature.color = #(x11-color 'blue)               %! EXPLICIT_TIME_SIGNATURE_COLOR:SM6
                        s1 * 1/2
            <BLANKLINE>
                        % GlobalSkips [measure 4]                                                    %! SM4
                        \time 3/8                                                                    %! EXPLICIT_TIME_SIGNATURE:SM8
                        \once \override Score.TimeSignature.color = #(x11-color 'blue)               %! EXPLICIT_TIME_SIGNATURE_COLOR:SM6
                        s1 * 3/8
                        \stopTextSpan                                                                %! SM29
                        \override Score.BarLine.transparent = ##f                                    %! SM5
                        \bar "|"                                                                     %! SM5
            <BLANKLINE>
                    }
                >>
                \context MusicContext = "MusicContext" <<
                    \context Staff = "MusicStaff" {
                        \context Voice = "MusicVoice" {
                            {
            <BLANKLINE>
                                % MusicVoice [measure 1]                                             %! SM4
                                e'8
                                [
            <BLANKLINE>
                                d''8
            <BLANKLINE>
                                f'8
            <BLANKLINE>
                                e''8
                                ]
                            }
                            {
            <BLANKLINE>
                                % MusicVoice [measure 2]                                             %! SM4
                                g'8
                                [
                                (                                                                    %! SC
            <BLANKLINE>
                                f''8
            <BLANKLINE>
                                e'8
                                ]
                                )                                                                    %! SC
                            }
                            {
            <BLANKLINE>
                                % MusicVoice [measure 3]                                             %! SM4
                                d''8
                                [
            <BLANKLINE>
                                f'8
            <BLANKLINE>
                                e''8
            <BLANKLINE>
                                g'8
                                ]
                            }
                            {
            <BLANKLINE>
                                % MusicVoice [measure 4]                                             %! SM4
                                f''8
                                [
            <BLANKLINE>
                                e'8
            <BLANKLINE>
                                d''8
                                ]
            <BLANKLINE>
                            }
                        }
                    }
                >>
            >>

    ..  container:: example

        >>> baca.SpannerCommand()
        SpannerCommand(selector=baca.tleaves(), site='SC')

    '''

    ### CLASS VARIABLES ###

    __slots__ = (
        # TODO: remove annotation?
        '_annotation',
        '_site',
        '_spanner',
        '_tag',
        )

    ### INITIALIZER ###

    def __init__(
        self,
        selector='baca.tleaves()',
        spanner=None,
        site='SC',
        tag=None,
        ):
        Command.__init__(self, selector=selector)
        self._annotation = None
        if spanner is not None:
            assert isinstance(spanner, abjad.Spanner)
        self._spanner = spanner
        self._site = site
        self._tag = tag

    ### SPECIAL METHODS ###

    def __call__(self, argument=None):
        r'''Calls command on `argument`.

        Returns spanner (for handoff to piecewise command).
        '''
        if argument is None:
            return
        if self.spanner is None:
            return
        if self.selector:
            argument = self.selector(argument)
        leaves = abjad.select(argument).leaves()
        spanner = abjad.new(self.spanner)
        abjad.attach(
            spanner,
            leaves,
            site=self.site,
            tag=self.tag,
            )
        return spanner

    ### PUBLIC PROPERTIES ###

    @property
    def selector(self):
        r'''Gets selector.

        ..  container:: example

            Selects trimmed leaves by default:

            >>> music_maker = baca.MusicMaker(baca.slur())

            >>> collections = [[0, 2, 10], [18, 16, 15, 20, 19], [9]]
            >>> contribution = music_maker('Voice 1', collections)
            >>> lilypond_file = music_maker.show(contribution)
            >>> abjad.show(lilypond_file, strict=89) # doctest: +SKIP

            ..  docs::

                >>> abjad.f(lilypond_file[abjad.Staff], strict=89)
                \new Staff <<
                    \context Voice = "Voice 1" {
                        \voiceOne
                        {
                            {
                                c'16
                                [
                                (                                                                        %! SC
                                d'16
                                bf'16
                                ]
                            }
                            {
                                fs''16
                                [
                                e''16
                                ef''16
                                af''16
                                g''16
                                ]
                            }
                            {
                                a'16
                                )                                                                        %! SC
                            }
                        }
                    }
                >>

        Set to selector or none.

        Returns selector or none.
        '''
        return self._selector

    @property
    def site(self):
        r'''Gets site.

        Set to string or none.
        '''
        return self._site

    @property
    def spanner(self):
        r'''Gets spanner.

        ..  container:: example

            Ties are smart enough to remove existing ties prior to attach:

            >>> music_maker = baca.MusicMaker()

            >>> contribution = music_maker(
            ...     'Voice 1',
            ...     [[14, 14, 14]],
            ...     counts=[5],
            ...     )
            >>> lilypond_file = music_maker.show(contribution)
            >>> abjad.show(lilypond_file, strict=89) # doctest: +SKIP

            ..  docs::

                >>> abjad.f(lilypond_file[abjad.Staff], strict=89)
                \new Staff <<
                    \context Voice = "Voice 1" {
                        \voiceOne
                        {
                            {
                                d''4
                                ~
                                d''16
                                d''4
                                ~
                                d''16
                                d''4
                                ~
                                d''16
                            }
                        }
                    }
                >>

            >>> contribution = music_maker(
            ...     'Voice 1',
            ...     [[14, 14, 14]],
            ...     baca.SpannerCommand(spanner=abjad.Tie()),
            ...     counts=[5],
            ...     )
            >>> lilypond_file = music_maker.show(contribution)
            >>> abjad.show(lilypond_file, strict=89) # doctest: +SKIP

            ..  docs::

                >>> abjad.f(lilypond_file[abjad.Staff], strict=89)
                \new Staff <<
                    \context Voice = "Voice 1" {
                        \voiceOne
                        {
                            {
                                d''4
                                ~                                                                        %! SC
                                d''16
                                ~                                                                        %! SC
                                d''4
                                ~                                                                        %! SC
                                d''16
                                ~                                                                        %! SC
                                d''4
                                ~                                                                        %! SC
                                d''16
                            }
                        }
                    }
                >>

        Set to spanner or none.

        Returns spanner or none.
        '''
        return self._spanner

    @property
    def tag(self):
        r'''Gets tag.

        Set to string or none.
        '''
        return self._tag
