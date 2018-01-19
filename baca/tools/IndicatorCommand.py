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
            \new Staff <<
                \context Voice = "Voice 1" {
                    \voiceOne
                    {
                        {
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
                        {
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
                        {
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
            \context Score = "Score" <<
                \context GlobalContext = "GlobalContext" <<
                    \context GlobalSkips = "GlobalSkips" {
            <BLANKLINE>
                        % GlobalSkips [measure 1]                                                    %! SM4
                        \time 4/8                                                                    %! EXPLICIT_TIME_SIGNATURE:SM8
                        \once \override Score.TimeSignature.color = #(x11-color 'blue)               %! EXPLICIT_TIME_SIGNATURE_COLOR:SM6
                        s1 * 1/2
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
                                % MusicVoice [measure 2]                                             %! SM4
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
                                % MusicVoice [measure 3]                                             %! SM4
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
                                % MusicVoice [measure 4]                                             %! SM4
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
        '_document',
        '_indicators',
        '_site',
        '_tags',
        )

    ### INITIALIZER ###

    def __init__(
        self,
        context=None,
        deactivate=None,
        indicators=None,
        selector='baca.pheads()',
        site='IC',
        tags=None,
        ):
        Command.__init__(self, deactivate=deactivate, selector=selector)
        self._document = None
        if context is not None:
            assert isinstance(context, str), repr(context)
        self._context = context
        if indicators is not None:
            if isinstance(indicators, collections.Iterable):
                indicators = abjad.CyclicTuple(indicators)
            else:
                indicators = abjad.CyclicTuple([indicators])
        self._indicators = indicators
        if site is not None:
            assert isinstance(site, str), repr(site)
        self._site = site
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
        #deactivate = None
        tag = self.tag
        if self.document is not None:
            assert self.document[0] in ('+', '-'), repr(self.document)
            if self.tag:
                tag = f'{self.document}:{self.tag}'
            else:
                tag = f'{self.document}'
            #if tag.startswith('+'):
            #    deactivate = True
        for i, leaf in enumerate(baca.select(argument).leaves()):
            indicators = self.indicators[i]
            indicators = self._token_to_indicators(indicators)
            for indicator in indicators:
                reapplied_indicator = self._remove_reapplied_indicator(
                    leaf,
                    indicator,
                    )
                abjad.attach(
                    indicator,
                    leaf,
                    context=self.context,
                    #deactivate=deactivate,
                    deactivate=self.deactivate,
                    site=self.site,
                    tag=tag,
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
        tags_to_remove = []
        if isinstance(indicator, abjad.Instrument):
            prototype = abjad.Instrument
        else:
            prototype = type(indicator)
        wrappers = abjad.inspect(leaf).wrappers(prototype)
        if not wrappers:
            return
        if wrappers:
            assert len(wrappers) == 1, repr(wrappers)
        wrapper = wrappers[0]
        if not wrapper.tag:
            return
        if not (wrapper.tag.startswith('REAPPLIED') or
            wrapper.tag.startswith('DEFAULT')):
            return
        reapplied_indicator = wrapper.indicator
        reapplied_substring = '_'.join(wrapper.tag.split('_')[:2])
        for wrapper in abjad.inspect(leaf).wrappers():
            if wrapper.tag and reapplied_substring in wrapper.tag:
                abjad.detach(wrapper.indicator, leaf)
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
    def document(self):
        r'''Gets document.

        Set to string or none.

        Returns string or none.
        '''
        document = self._document
        if document is not None:
            assert self._is_signed_document_name(document), repr(document)
        return document

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
                \new Staff <<
                    \context Voice = "Voice 1" {
                        \voiceOne
                        {
                            {
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
                            {
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
                            {
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
                \new Staff <<
                    \context Voice = "Voice 1" {
                        \voiceOne
                        {
                            {
                                c'8
                                \fermata                                                                 %! IC
                                ~
                                [
                                c'32
                                d'8
                                bf'8
                                ]
                            }
                            {
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
                            {
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

    @property
    def site(self):
        r'''Gets site.

        Returns string or none.
        '''
        return self._site

    @property
    def tag(self):
        r'''Gets tag.

        Returns string or none.
        '''
        if self.tags:
            return ':'.join(self.tags)
