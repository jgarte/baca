import abjad
import baca
import collections
from .Command import Command


class IndicatorCommand(Command):
    r'''Indicator command.

    >>> from abjad import rhythmmakertools as rhythmos

    ..  container:: example

        With music-maker:

        >>> music_maker = baca.MusicMaker(
        ...     baca.IndicatorCommand(indicators=[abjad.Fermata()]),
        ...     baca.PitchFirstRhythmCommand(
        ...         rhythm_maker=baca.PitchFirstRhythmMaker(
        ...             talea=rhythmos.Talea(
        ...                 counts=[5, 4, 4, 5, 4, 4, 4],
        ...                 denominator=32,
        ...                 ),
        ...             ),
        ...         ),
        ...     )

        >>> collections = [[0, 2, 10], [18, 16, 15, 20, 19], [9]]
        >>> contribution = music_maker('Voice 1', collections)
        >>> lilypond_file = music_maker.show(contribution)
        >>> abjad.show(lilypond_file, strict=89) # doctest: +SKIP

        ..  docs::

            >>> abjad.f(lilypond_file[abjad.Staff], strict=89)
            \new Staff
            <<
                \context Voice = "Voice 1"
                {
                    \voiceOne
                    {
                        \scaleDurations #'(1 . 1) {
                            c'8
                            \fermata                                                                 %! IC
                            ~
                            [
                            c'32
                            d'8
                            \fermata                                                                 %! IC
                            bf'8
                            \fermata                                                                 %! IC
                            ]
                        }
                        \scaleDurations #'(1 . 1) {
                            fs''8
                            \fermata                                                                 %! IC
                            ~
                            [
                            fs''32
                            e''8
                            \fermata                                                                 %! IC
                            ef''8
                            \fermata                                                                 %! IC
                            af''8
                            \fermata                                                                 %! IC
                            ~
                            af''32
                            g''8
                            \fermata                                                                 %! IC
                            ]
                        }
                        \scaleDurations #'(1 . 1) {
                            a'8
                            \fermata                                                                 %! IC
                            ~
                            [
                            a'32
                            ]
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
        ...     baca.IndicatorCommand(indicators=[abjad.Fermata()]),
        ...     )

        >>> lilypond_file = maker.run(environment='docs')
        >>> abjad.show(lilypond_file, strict=89) # doctest: +SKIP

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
                        \time 4/8                                                                    %! SM1:EXPLICIT_TIME_SIGNATURE:SM8
                        \once \override Score.TimeSignature.color = #(x11-color 'blue)               %! SM1:EXPLICIT_TIME_SIGNATURE_COLOR:SM6
                        s1 * 1/2
            <BLANKLINE>
                        % [GlobalSkips measure 2]                                                    %! SM4
                        \time 3/8                                                                    %! SM1:EXPLICIT_TIME_SIGNATURE:SM8
                        \once \override Score.TimeSignature.color = #(x11-color 'blue)               %! SM1:EXPLICIT_TIME_SIGNATURE_COLOR:SM6
                        s1 * 3/8
            <BLANKLINE>
                        % [GlobalSkips measure 3]                                                    %! SM4
                        \time 4/8                                                                    %! SM1:EXPLICIT_TIME_SIGNATURE:SM8
                        \once \override Score.TimeSignature.color = #(x11-color 'blue)               %! SM1:EXPLICIT_TIME_SIGNATURE_COLOR:SM6
                        s1 * 1/2
            <BLANKLINE>
                        % [GlobalSkips measure 4]                                                    %! SM4
                        \time 3/8                                                                    %! SM1:EXPLICIT_TIME_SIGNATURE:SM8
                        \once \override Score.TimeSignature.color = #(x11-color 'blue)               %! SM1:EXPLICIT_TIME_SIGNATURE_COLOR:SM6
                        s1 * 3/8
                        \override Score.BarLine.transparent = ##f                                    %! SM5
                        \bar "|"                                                                     %! SM5
            <BLANKLINE>
                    }
                >>
                \context MusicContext = "MusicContext"
                <<
                    \context Staff = "MusicStaff"
                    {
                        \context Voice = "MusicVoice"
                        {
                            {
            <BLANKLINE>
                                % [MusicVoice measure 1]                                             %! SM4
                                e'8
                                \fermata                                                             %! IC
                                [
            <BLANKLINE>
                                d''8
                                \fermata                                                             %! IC
            <BLANKLINE>
                                f'8
                                \fermata                                                             %! IC
            <BLANKLINE>
                                e''8
                                \fermata                                                             %! IC
                                ]
                            }
                            {
            <BLANKLINE>
                                % [MusicVoice measure 2]                                             %! SM4
                                g'8
                                \fermata                                                             %! IC
                                [
            <BLANKLINE>
                                f''8
                                \fermata                                                             %! IC
            <BLANKLINE>
                                e'8
                                \fermata                                                             %! IC
                                ]
                            }
                            {
            <BLANKLINE>
                                % [MusicVoice measure 3]                                             %! SM4
                                d''8
                                \fermata                                                             %! IC
                                [
            <BLANKLINE>
                                f'8
                                \fermata                                                             %! IC
            <BLANKLINE>
                                e''8
                                \fermata                                                             %! IC
            <BLANKLINE>
                                g'8
                                \fermata                                                             %! IC
                                ]
                            }
                            {
            <BLANKLINE>
                                % [MusicVoice measure 4]                                             %! SM4
                                f''8
                                \fermata                                                             %! IC
                                [
            <BLANKLINE>
                                e'8
                                \fermata                                                             %! IC
            <BLANKLINE>
                                d''8
                                \fermata                                                             %! IC
                                ]
            <BLANKLINE>
                            }
                        }
                    }
                >>
            >>

    '''

    ### CLASS VARIABLES ###

    __slots__ = (
        '_context',
        '_indicators',
        '_tags',
        )

    ### INITIALIZER ###

    def __init__(
        self,
        context=None,
        deactivate=None,
        indicators=None,
        selector='baca.pheads()',
        tags=None,
        ):
        Command.__init__(self, deactivate=deactivate, selector=selector)
        if context is not None:
            assert isinstance(context, str), repr(context)
        self._context = context
        if indicators is not None:
            if isinstance(indicators, collections.Iterable):
                indicators = abjad.CyclicTuple(indicators)
            else:
                indicators = abjad.CyclicTuple([indicators])
        self._indicators = indicators
        tags = tags or []
        assert self._are_valid_tags(tags), repr(tags)
        self._tags = tags

    ### SPECIAL METHODS ###

    def __call__(self, argument=None):
        r'''Calls command on `argument`.

        Returns none.
        '''
        if argument is None:
            return
        if self.indicators is None:
            return
        if self.selector:
            argument = self.selector(argument)
        if not argument:
            return
        for i, leaf in enumerate(baca.select(argument).leaves()):
            indicators = self.indicators[i]
            indicators = self._token_to_indicators(indicators)
            for indicator in indicators:
                reapplied_indicator = self._remove_reapplied_indicator(
                    leaf,
                    indicator,
                    )
                if self.tag:
                    tag = self.tag.append('IC')
                else:
                    tag = abjad.Tag('IC')
                abjad.attach(
                    indicator,
                    leaf,
                    context=self.context,
                    deactivate=self.deactivate,
                    tag=str(tag),
                    )
                if indicator == reapplied_indicator:
                    if (isinstance(indicator, abjad.Dynamic) and
                        indicator.sforzando):
                        status = 'explicit'
                    else:
                        status = 'redundant'
                    wrapper = abjad.inspect(leaf).wrapper(type(indicator))
                    context = wrapper._find_correct_effective_context()
                    baca.SegmentMaker._categorize_persistent_indicator(
                        self._manifests,
                        context,
                        leaf,
                        indicator,
                        status,
                        )

    ### PRIVATE METHODS ###

    @staticmethod
    def _remove_reapplied_indicator(leaf, indicator):
        if not getattr(indicator, 'persistent', False):
            return
        if abjad.inspect(leaf).get_timespan().start_offset != 0:
            return
        if isinstance(indicator, abjad.Instrument):
            prototype = abjad.Instrument
        else:
            prototype = type(indicator)
        wrappers = abjad.inspect(leaf).wrappers(prototype)
        if not wrappers:
            return
        for wrapper in wrappers:
            if not wrapper.tag:
                continue
            if not (abjad.Tag(wrapper.tag).has_reapplied_tag() or
                abjad.Tag(wrapper.tag).has_default_tag()):
                continue
            reapplied_indicator = wrapper.indicator
            reapplied_tags = [
                _ for _ in abjad.Tag(wrapper.tag)
                if _.startswith('REAPPLIED') or _.startswith('DEFAULT')
                ]
            assert len(reapplied_tags) == 1, repr(wrapper.tag)
            reapplied_tag = reapplied_tags[0]
            reapplied_substring = '_'.join(reapplied_tag.split('_')[:2])
            for wrapper_ in abjad.inspect(leaf).wrappers():
                if bool(wrapper_.tag) and reapplied_substring in wrapper_.tag:
                    abjad.detach(wrapper_.indicator, leaf)
            return reapplied_indicator

    @staticmethod
    def _token_to_indicators(token):
        result = []
        if not isinstance(token, (tuple, list)):
            token = [token]
        for item in token:
            if item is None:
                continue
            result.append(item)
        return result

    ### PUBLIC PROPERTIES ###

    @property
    def context(self):
        r'''Gets context name.

        Returns string or none.
        '''
        return self._context

    @property
    def indicators(self):
        r'''Gets indicators.

        ..  container:: example

            Attaches fermata to head of every pitched logical tie:

            >>> music_maker = baca.MusicMaker(
            ...     baca.IndicatorCommand(indicators=[abjad.Fermata()]),
            ...     baca.PitchFirstRhythmCommand(
            ...         rhythm_maker=baca.PitchFirstRhythmMaker(
            ...             talea=rhythmos.Talea(
            ...                 counts=[5, 4, 4, 5, 4, 4, 4],
            ...                 denominator=32,
            ...                 ),
            ...             ),
            ...         ),
            ...     )

            >>> collections = [[0, 2, 10], [18, 16, 15, 20, 19], [9]]
            >>> contribution = music_maker('Voice 1', collections)
            >>> lilypond_file = music_maker.show(contribution)
            >>> abjad.show(lilypond_file, strict=89) # doctest: +SKIP

            ..  docs::

                >>> abjad.f(lilypond_file[abjad.Staff], strict=89)
                \new Staff
                <<
                    \context Voice = "Voice 1"
                    {
                        \voiceOne
                        {
                            \scaleDurations #'(1 . 1) {
                                c'8
                                \fermata                                                                 %! IC
                                ~
                                [
                                c'32
                                d'8
                                \fermata                                                                 %! IC
                                bf'8
                                \fermata                                                                 %! IC
                                ]
                            }
                            \scaleDurations #'(1 . 1) {
                                fs''8
                                \fermata                                                                 %! IC
                                ~
                                [
                                fs''32
                                e''8
                                \fermata                                                                 %! IC
                                ef''8
                                \fermata                                                                 %! IC
                                af''8
                                \fermata                                                                 %! IC
                                ~
                                af''32
                                g''8
                                \fermata                                                                 %! IC
                                ]
                            }
                            \scaleDurations #'(1 . 1) {
                                a'8
                                \fermata                                                                 %! IC
                                ~
                                [
                                a'32
                                ]
                            }
                        }
                    }
                >>

        ..  container:: example

            Patterns fermatas:

            >>> music_maker = baca.MusicMaker(
            ...     baca.IndicatorCommand(
            ...         indicators=[
            ...             abjad.Fermata(), None, None,
            ...             abjad.Fermata(), None, None,
            ...             abjad.Fermata(), None,
            ...             ],
            ...         ),
            ...     baca.PitchFirstRhythmCommand(
            ...         rhythm_maker=baca.PitchFirstRhythmMaker(
            ...             talea=rhythmos.Talea(
            ...                 counts=[5, 4, 4, 5, 4, 4, 4],
            ...                 denominator=32,
            ...                 ),
            ...             ),
            ...         ),
            ...     )

            >>> collections = [[0, 2, 10], [18, 16, 15, 20, 19], [9]]
            >>> contribution = music_maker('Voice 1', collections)
            >>> lilypond_file = music_maker.show(contribution)
            >>> abjad.show(lilypond_file, strict=89) # doctest: +SKIP

            ..  docs::

                >>> abjad.f(lilypond_file[abjad.Staff], strict=89)
                \new Staff
                <<
                    \context Voice = "Voice 1"
                    {
                        \voiceOne
                        {
                            \scaleDurations #'(1 . 1) {
                                c'8
                                \fermata                                                                 %! IC
                                ~
                                [
                                c'32
                                d'8
                                bf'8
                                ]
                            }
                            \scaleDurations #'(1 . 1) {
                                fs''8
                                \fermata                                                                 %! IC
                                ~
                                [
                                fs''32
                                e''8
                                ef''8
                                af''8
                                \fermata                                                                 %! IC
                                ~
                                af''32
                                g''8
                                ]
                            }
                            \scaleDurations #'(1 . 1) {
                                a'8
                                \fermata                                                                 %! IC
                                ~
                                [
                                a'32
                                ]
                            }
                        }
                    }
                >>

        Defaults to none.

        Set to indicators or none.

        Returns indicators or none.
        '''
        return self._indicators
