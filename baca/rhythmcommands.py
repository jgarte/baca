"""
Rhythm library.
"""
import abjad
import collections
import inspect
import math
import typing
from abjadext import rmakers
from . import classes
from . import divisionclasses
from . import const
from . import overrides
from . import scoping
from . import typings


RhythmMakerTyping = typing.Union[
    str,
    rmakers.RhythmMaker,
    abjad.Selection,
    typing.Sequence["DivisionAssignment"],
]

### CLASSES ###


class DivisionAssignment(object):
    """
    Division assignment.
    """

    ### CLASS VARIABLES ###

    __slots__ = ("_pattern", "_rhythm_maker")

    ### INITIALIZER ###

    def __init__(
        self,
        pattern: abjad.Pattern,
        rhythm_maker: typing.Union[rmakers.RhythmMaker, "RhythmCommand"],
    ) -> None:
        assert isinstance(pattern, abjad.Pattern), repr(pattern)
        self._pattern = pattern
        prototype = (rmakers.RhythmMaker, RhythmCommand)
        assert isinstance(rhythm_maker, prototype), repr(rhythm_maker)
        self._rhythm_maker = rhythm_maker

    ### PUBLIC PROPERTIES ###

    @property
    def pattern(self) -> abjad.Pattern:
        """
        Gets pattern.
        """
        return self._pattern

    @property
    def rhythm_maker(
        self
    ) -> typing.Union[rmakers.RhythmMaker, "RhythmCommand"]:
        """
        Gets rhythm-maker.
        """
        return self._rhythm_maker


class DurationMultiplierCommand(scoping.Command):
    """
    Duration multiplier command.

    ..  container:: example

        >>> baca.DurationMultiplierCommand()
        DurationMultiplierCommand(selector=baca.leaf(0))

    """

    ### CLASS VARIABLES ###

    __slots__ = ("_written_duration",)

    ### INITIALIZER ###

    def __init__(
        self,
        *,
        map: abjad.SelectorTyping = None,
        match: typings.Indices = None,
        measures: typings.SliceTyping = None,
        scope: scoping.ScopeTyping = None,
        selector: abjad.SelectorTyping = "baca.leaf(0)",
        written_duration: abjad.DurationTyping = None,
    ) -> None:
        scoping.Command.__init__(
            self,
            map=map,
            match=match,
            measures=measures,
            scope=scope,
            selector=selector,
        )
        written_duration_ = None
        if written_duration is not None:
            written_duration_ = abjad.Duration(written_duration)
        self._written_duration = written_duration_

    ### SPECIAL METHODS ###

    def _call(self, argument=None) -> None:
        """
        Applies ``DurationMultiplierCommand`` to result of selector called on
        ``argument``.
        """
        if argument is None:
            return
        if self.selector is not None:
            argument = self.selector(argument)
        leaves = classes.Selection(argument).leaves()
        assert isinstance(leaves, classes.Selection)
        for leaf in leaves:
            self._set_multiplied_duration(leaf, self.written_duration)

    ### PRIVATE METHODS ###

    @staticmethod
    def _set_multiplied_duration(leaf, written_duration):
        if written_duration is None:
            return
        old_duration = abjad.inspect(leaf).duration()
        if written_duration == old_duration:
            return
        leaf.written_duration = written_duration
        multiplier = old_duration / written_duration
        leaf.multiplier = multiplier

    ### PUBLIC PROPERTIES ###

    @property
    def written_duration(self) -> typing.Optional[abjad.Duration]:
        """
        Gets written duration.
        """
        return self._written_duration


class RhythmCommand(scoping.Command):
    r"""
    Rhythm command.

    >>> from abjadext import rmakers

    ..  container:: example

        >>> maker = baca.SegmentMaker(
        ...     score_template=baca.SingleStaffScoreTemplate(),
        ...     spacing=baca.minimum_duration((1, 12)),
        ...     time_signatures=[(3, 8), (4, 8), (3,8), (4, 8)],
        ...     )

        >>> command = baca.RhythmCommand(
        ...     rhythm_maker=rmakers.EvenDivisionRhythmMaker(
        ...         rmakers.BeamSpecifier(
        ...             selector=baca.tuplets(),
        ...         ),
        ...         rmakers.TupletSpecifier(
        ...             extract_trivial=True,
        ...             ),
        ...     ),
        ... )

        >>> maker(
        ...     'Music_Voice',
        ...     command,
        ...     )

        >>> lilypond_file = maker.run(environment='docs')
        >>> abjad.show(lilypond_file, strict=89) # doctest: +SKIP

        ..  docs::

            >>> abjad.f(lilypond_file[abjad.Score], strict=89)
            <BLANKLINE>
            \context Score = "Score"                                                                 %! baca.SingleStaffScoreTemplate.__call__
            <<                                                                                       %! baca.SingleStaffScoreTemplate.__call__
            <BLANKLINE>
                \context GlobalContext = "Global_Context"                                            %! abjad.ScoreTemplate._make_global_context
                <<                                                                                   %! abjad.ScoreTemplate._make_global_context
            <BLANKLINE>
                    \context GlobalSkips = "Global_Skips"                                            %! abjad.ScoreTemplate._make_global_context
                    {                                                                                %! abjad.ScoreTemplate._make_global_context
            <BLANKLINE>
                        % [Global_Skips measure 1]                                                   %! _comment_measure_numbers
                        \baca-new-spacing-section #1 #12                                             %! HorizontalSpacingSpecifier(1):SPACING_COMMAND
                        \time 3/8                                                                    %! EXPLICIT_TIME_SIGNATURE:_set_status_tag:_make_global_skips(2)
                        \baca-time-signature-color #'blue                                            %! EXPLICIT_TIME_SIGNATURE_COLOR:_attach_color_literal(2)
                        s1 * 3/8                                                                     %! _make_global_skips(1)
            <BLANKLINE>
                        % [Global_Skips measure 2]                                                   %! _comment_measure_numbers
                        \baca-new-spacing-section #1 #12                                             %! HorizontalSpacingSpecifier(1):SPACING_COMMAND
                        \time 4/8                                                                    %! EXPLICIT_TIME_SIGNATURE:_set_status_tag:_make_global_skips(2)
                        \baca-time-signature-color #'blue                                            %! EXPLICIT_TIME_SIGNATURE_COLOR:_attach_color_literal(2)
                        s1 * 1/2                                                                     %! _make_global_skips(1)
            <BLANKLINE>
                        % [Global_Skips measure 3]                                                   %! _comment_measure_numbers
                        \baca-new-spacing-section #1 #12                                             %! HorizontalSpacingSpecifier(1):SPACING_COMMAND
                        \time 3/8                                                                    %! EXPLICIT_TIME_SIGNATURE:_set_status_tag:_make_global_skips(2)
                        \baca-time-signature-color #'blue                                            %! EXPLICIT_TIME_SIGNATURE_COLOR:_attach_color_literal(2)
                        s1 * 3/8                                                                     %! _make_global_skips(1)
            <BLANKLINE>
                        % [Global_Skips measure 4]                                                   %! _comment_measure_numbers
                        \baca-new-spacing-section #1 #12                                             %! HorizontalSpacingSpecifier(1):SPACING_COMMAND
                        \time 4/8                                                                    %! EXPLICIT_TIME_SIGNATURE:_set_status_tag:_make_global_skips(2)
                        \baca-time-signature-color #'blue                                            %! EXPLICIT_TIME_SIGNATURE_COLOR:_attach_color_literal(2)
                        s1 * 1/2                                                                     %! _make_global_skips(1)
                        \baca-bar-line-visible                                                       %! _attach_final_bar_line
                        \bar "|"                                                                     %! _attach_final_bar_line
            <BLANKLINE>
                        % [Global_Skips measure 5]                                                   %! PHANTOM:_style_phantom_measures(1):_comment_measure_numbers
                        \baca-new-spacing-section #1 #4                                              %! PHANTOM:_style_phantom_measures(1):HorizontalSpacingSpecifier(1):SPACING_COMMAND
                        \time 1/4                                                                    %! PHANTOM:_style_phantom_measures(1):EXPLICIT_TIME_SIGNATURE:_set_status_tag:_make_global_skips(3)
                        \baca-time-signature-transparent                                             %! PHANTOM:_style_phantom_measures(2)
                        s1 * 1/4                                                                     %! PHANTOM:_make_global_skips(3)
                        \once \override Score.BarLine.transparent = ##t                              %! PHANTOM:_style_phantom_measures(3)
                        \once \override Score.SpanBar.transparent = ##t                              %! PHANTOM:_style_phantom_measures(3)
            <BLANKLINE>
                    }                                                                                %! abjad.ScoreTemplate._make_global_context
            <BLANKLINE>
                >>                                                                                   %! abjad.ScoreTemplate._make_global_context
            <BLANKLINE>
                \context MusicContext = "Music_Context"                                              %! baca.SingleStaffScoreTemplate.__call__
                <<                                                                                   %! baca.SingleStaffScoreTemplate.__call__
            <BLANKLINE>
                    \context Staff = "Music_Staff"                                                   %! baca.SingleStaffScoreTemplate.__call__
                    {                                                                                %! baca.SingleStaffScoreTemplate.__call__
            <BLANKLINE>
                        \context Voice = "Music_Voice"                                               %! baca.SingleStaffScoreTemplate.__call__
                        {                                                                            %! baca.SingleStaffScoreTemplate.__call__
            <BLANKLINE>
                            % [Music_Voice measure 1]                                                %! _comment_measure_numbers
                            \baca-unpitched-music-warning                                            %! _color_unpitched_notes
                            c'8
                            [
            <BLANKLINE>
                            \baca-unpitched-music-warning                                            %! _color_unpitched_notes
                            c'8
            <BLANKLINE>
                            \baca-unpitched-music-warning                                            %! _color_unpitched_notes
                            c'8
                            ]
            <BLANKLINE>
                            % [Music_Voice measure 2]                                                %! _comment_measure_numbers
                            \baca-unpitched-music-warning                                            %! _color_unpitched_notes
                            c'8
                            [
            <BLANKLINE>
                            \baca-unpitched-music-warning                                            %! _color_unpitched_notes
                            c'8
            <BLANKLINE>
                            \baca-unpitched-music-warning                                            %! _color_unpitched_notes
                            c'8
            <BLANKLINE>
                            \baca-unpitched-music-warning                                            %! _color_unpitched_notes
                            c'8
                            ]
            <BLANKLINE>
                            % [Music_Voice measure 3]                                                %! _comment_measure_numbers
                            \baca-unpitched-music-warning                                            %! _color_unpitched_notes
                            c'8
                            [
            <BLANKLINE>
                            \baca-unpitched-music-warning                                            %! _color_unpitched_notes
                            c'8
            <BLANKLINE>
                            \baca-unpitched-music-warning                                            %! _color_unpitched_notes
                            c'8
                            ]
            <BLANKLINE>
                            % [Music_Voice measure 4]                                                %! _comment_measure_numbers
                            \baca-unpitched-music-warning                                            %! _color_unpitched_notes
                            c'8
                            [
            <BLANKLINE>
                            \baca-unpitched-music-warning                                            %! _color_unpitched_notes
                            c'8
            <BLANKLINE>
                            \baca-unpitched-music-warning                                            %! _color_unpitched_notes
                            c'8
            <BLANKLINE>
                            \baca-unpitched-music-warning                                            %! _color_unpitched_notes
                            c'8
                            ]
            <BLANKLINE>
                            <<                                                                       %! PHANTOM:_make_multimeasure_rest_container
            <BLANKLINE>
                                \context Voice = "Music_Voice"                                       %! PHANTOM:_make_multimeasure_rest_container
                                {                                                                    %! PHANTOM:_make_multimeasure_rest_container
            <BLANKLINE>
                                    % [Music_Voice measure 5]                                        %! PHANTOM:_style_phantom_measures(5):_comment_measure_numbers
                                    \baca-invisible-music                                            %! PHANTOM:_style_phantom_measures(5):_make_multimeasure_rest_container
                                    c'1 * 1/4                                                        %! PHANTOM:_make_multimeasure_rest_container
            <BLANKLINE>
                                }                                                                    %! PHANTOM:_make_multimeasure_rest_container
            <BLANKLINE>
                                \context Voice = "Rest_Voice"                                        %! PHANTOM:_make_multimeasure_rest_container
                                {                                                                    %! PHANTOM:_make_multimeasure_rest_container
            <BLANKLINE>
                                    % [Rest_Voice measure 5]                                         %! PHANTOM:_style_phantom_measures(5):_comment_measure_numbers
                                    \once \override Score.TimeSignature.X-extent = ##f               %! PHANTOM:_style_phantom_measures(6)
                                    \once \override MultiMeasureRest.transparent = ##t               %! PHANTOM:_style_phantom_measures(7)
                                    \stopStaff                                                       %! PHANTOM:_style_phantom_measures(8)
                                    \once \override Staff.StaffSymbol.transparent = ##t              %! PHANTOM:_style_phantom_measures(8)
                                    \startStaff                                                      %! PHANTOM:_style_phantom_measures(8)
                                    R1 * 1/4                                                         %! PHANTOM:_make_multimeasure_rest_container
            <BLANKLINE>
                                }                                                                    %! PHANTOM:_make_multimeasure_rest_container
            <BLANKLINE>
                            >>                                                                       %! PHANTOM:_make_multimeasure_rest_container
            <BLANKLINE>
                        }                                                                            %! baca.SingleStaffScoreTemplate.__call__
            <BLANKLINE>
                    }                                                                                %! baca.SingleStaffScoreTemplate.__call__
            <BLANKLINE>
                >>                                                                                   %! baca.SingleStaffScoreTemplate.__call__
            <BLANKLINE>
            >>                                                                                       %! baca.SingleStaffScoreTemplate.__call__

    """

    ### CLASS ATTRIBUTES ###

    __slots__ = (
        "_annotate_unpitched_music",
        "_divisions",
        "_left_broken",
        "_persist",
        "_reference_meters",
        "_rhythm_maker",
        "_right_broken",
        "_state",
    )

    _publish_storage_format = True

    ### INITIALIZER ###

    def __init__(
        self,
        *,
        annotate_unpitched_music: bool = None,
        divisions: abjad.Expression = None,
        left_broken: bool = None,
        match: typings.Indices = None,
        measures: typings.SliceTyping = None,
        persist: str = None,
        reference_meters: typing.Iterable[abjad.Meter] = None,
        rhythm_maker: RhythmMakerTyping = None,
        right_broken: bool = None,
        scope: scoping.ScopeTyping = None,
    ) -> None:
        scoping.Command.__init__(
            self, match=match, measures=measures, scope=scope
        )
        if annotate_unpitched_music is not None:
            annotate_unpitched_music = bool(annotate_unpitched_music)
        self._annotate_unpitched_music = annotate_unpitched_music
        if divisions is not None:
            assert isinstance(divisions, abjad.Expression)
        self._divisions = divisions
        if left_broken is not None:
            left_broken = bool(left_broken)
        self._left_broken = left_broken
        if persist is not None:
            assert isinstance(persist, str), repr(persist)
        self._persist = persist
        if reference_meters is not None:
            assert isinstance(reference_meters, collections.abc.Iterable)
            assert all(isinstance(_, abjad.Meter) for _ in reference_meters)
        self._reference_meters = reference_meters
        self._check_rhythm_maker_input(rhythm_maker)
        self._rhythm_maker = rhythm_maker
        if right_broken is not None:
            right_broken = bool(right_broken)
        self._right_broken = right_broken
        self._state: typing.Optional[abjad.OrderedDict] = None

    ### SPECIAL METHODS ###

    def _call(
        self,
        runtime: abjad.OrderedDict = None,
        start_offset: abjad.Offset = None,
        time_signatures: typing.Iterable[abjad.TimeSignature] = None,
    ) -> abjad.AnnotatedTimespan:
        """
        Calls ``RhythmCommand`` on ``start_offset`` and ``time_signatures``.
        """
        self._runtime = runtime or abjad.OrderedDict()
        selection, start_offset = self._make_rhythm(
            start_offset, time_signatures
        )
        assert isinstance(selection, abjad.Selection), repr(selection)
        timespan = abjad.AnnotatedTimespan(
            start_offset=start_offset, annotation=selection
        )
        return timespan

    ### PRIVATE METHODS ###

    @staticmethod
    def _annotate_unpitched_music_(argument):
        rest_prototype = (abjad.MultimeasureRest, abjad.Rest, abjad.Skip)
        for leaf in abjad.iterate(argument).leaves():
            if isinstance(leaf, abjad.Chord):
                message = f"rhythm-makers make only notes and rests: {leaf!r}."
                raise Exception(message)
            elif isinstance(leaf, abjad.Note):
                abjad.attach(abjad.tags.NOT_YET_PITCHED, leaf, tag=None)
            elif isinstance(leaf, rest_prototype):
                pass
            else:
                raise TypeError(leaf)

    def _apply_division_expression(
        self, divisions
    ) -> typing.Optional[divisionclasses.DivisionSequence]:
        if self.divisions is not None:
            divisions_ = self.divisions(divisions)
            if not isinstance(divisions_, abjad.Sequence):
                message = "division expression must return sequence:\n"
                message += f"  Input divisions:\n"
                message += f"    {divisions}\n"
                message += f"  Division expression:\n"
                message += f"    {self.divisions}\n"
                message += f"  Output divisions:\n"
                message += f"    {divisions_}"
                raise Exception(message)
            divisions = divisions_
        divisions = divisionclasses.DivisionSequence(divisions)
        return divisions

    def _check_rhythm_maker_input(self, rhythm_maker):
        if rhythm_maker is None:
            return
        prototype = (abjad.Selection, rmakers.RhythmMaker)
        if isinstance(rhythm_maker, prototype):
            return
        if all(isinstance(_, DivisionAssignment) for _ in rhythm_maker):
            return
        message = '\n  Input parameter "rhythm_maker" accepts:'
        message += "\n    rhythm-maker"
        message += "\n    selection"
        message += "\n    sequence of division assignment objects"
        message += "\n    none"
        message += '\n  Input parameter "rhythm_maker" received:'
        message += f"\n    {format(rhythm_maker)}"
        raise Exception(message)

    # TODO: simplify with DivisionSequence
    @staticmethod
    def _durations_to_divisions(durations, start_offset):
        divisions = [divisionclasses.Division(_) for _ in durations]
        durations = [_.duration for _ in divisions]
        start_offset = abjad.Offset(start_offset)
        durations.insert(0, start_offset)
        start_offsets = abjad.mathtools.cumulative_sums(durations)[1:-1]
        assert len(divisions) == len(start_offsets)
        divisions_ = []
        for division, start_offset in zip(divisions, start_offsets):
            division_ = divisionclasses.Division(
                division, start_offset=start_offset
            )
            divisions_.append(division_)
        assert not any(_.start_offset is None for _ in divisions_)
        return divisions_

    def _make_rhythm(self, start_offset, time_signatures):
        rhythm_maker = self.rhythm_maker
        assert rhythm_maker is not None
        if isinstance(rhythm_maker, abjad.Selection):
            selection = rhythm_maker
            if self.annotate_unpitched_music:
                self._annotate_unpitched_music_(selection)
            return selection, start_offset
        if isinstance(rhythm_maker, rmakers.RhythmMaker):
            assignment = DivisionAssignment(abjad.index([0], 1), rhythm_maker)
            assignments = [assignment]
        else:
            assignments = list(rhythm_maker)
        assert all(isinstance(_, DivisionAssignment) for _ in assignments)
        divisions = self._durations_to_divisions(time_signatures, start_offset)
        divisions = classes.Sequence(divisions).flatten(depth=-1)
        divisions = self._apply_division_expression(divisions)
        assert isinstance(divisions, divisionclasses.DivisionSequence), repr(
            divisions
        )
        divisions = divisions.flatten(depth=-1)
        division_count = len(divisions)
        time_signatures_ = [abjad.TimeSignature(_) for _ in divisions]
        start_offset = divisions[0].start_offset
        labelled_divisions = []
        for i, division in enumerate(divisions):
            for assignment in assignments:
                if assignment.pattern is True:
                    raise Exception("use abjad.index([0], 1) instead.")
                if isinstance(assignment.pattern, list):
                    raise Exception("use pattern instead.")
                elif isinstance(assignment.pattern, tuple):
                    raise Exception("use slice-pattern instead.")
                if assignment.pattern.matches_index(i, division_count):
                    # TODO: use class insted of tuple:
                    pair = (division, assignment.rhythm_maker)
                    labelled_divisions.append(pair)
                    break
            else:
                raise Exception(f"no rhythm-maker for division {i}.")
        assert len(labelled_divisions) == len(divisions)
        labelled_divisions = classes.Sequence(labelled_divisions)
        labelled_divisions = labelled_divisions.group_by(lambda pair: pair[1])
        components = []
        previous_segment_stop_state = self._previous_segment_stop_state()
        maker_to_state = abjad.OrderedDict()
        for subsequence in labelled_divisions:
            # TODO: use class insted of tuple:
            divisions_ = [pair[0] for pair in subsequence]
            rhythm_maker = subsequence[0][1]
            if isinstance(rhythm_maker, type(self)):
                rhythm_maker = rhythm_maker.rhythm_maker
                assert isinstance(rhythm_maker, rmakers.RhythmMaker)
            # TODO: eventually allow previous segment stop state
            #       and local stop state to work together
            if previous_segment_stop_state is None:
                previous_state = maker_to_state.get(rhythm_maker, None)
            else:
                previous_state = previous_segment_stop_state
            list_ = rhythm_maker(divisions_, previous_state=previous_state)
            assert isinstance(list_, list), repr(list_)
            assert len(list_) == 1, repr(list_)
            assert isinstance(list_[0], abjad.Selection), repr(list_)
            components.extend(list_[0])
            maker_to_state[rhythm_maker] = rhythm_maker.state
        self._state = rhythm_maker.state
        selection = abjad.select(components)
        self._annotate_unpitched_music_(selection)
        return selection, start_offset

    def _previous_segment_stop_state(self):
        previous_segment_stop_state = None
        dictionary = self.runtime.get("previous_segment_voice_metadata")
        if dictionary:
            previous_segment_stop_state = dictionary.get(const.RHYTHM)
            if (
                previous_segment_stop_state is not None
                and previous_segment_stop_state.get("name") != self.persist
            ):
                previous_segment_stop_state = None
        return previous_segment_stop_state

    def _tag_broken_ties(self, staff):
        if self.left_broken and self.rhythm_maker.previous_state.get(
            "incomplete_final_note"
        ):
            if not self.repeat_ties:
                raise Exception("left-broken ties must be repeat ties.")
            first_leaf = abjad.select(staff).leaf(0)
            if isinstance(first_leaf, abjad.Note):
                abjad.attach(const.LEFT_BROKEN_REPEAT_TIE_TO, first_leaf)
        if self.right_broken and self.rhythm_maker.state.get(
            "incomplete_final_note"
        ):
            if self.repeat_ties:
                raise Exception("right-broken ties must be conventional.")
            final_leaf = abjad.select(staff).leaf(-1)
            if isinstance(final_leaf, abjad.Note):
                abjad.attach(abjad.tags.RIGHT_BROKEN_TIE_FROM, final_leaf)

    ### PUBLIC PROPERTIES ###

    @property
    def annotate_unpitched_music(self) -> typing.Optional[bool]:
        """
        Is true when command annotates unpitched music.
        """
        return self._annotate_unpitched_music

    @property
    def divisions(self) -> typing.Optional[abjad.Expression]:
        r"""
        Gets division expression.

        ..  container:: example

            Sums divisions:

            >>> maker = baca.SegmentMaker(
            ...     score_template=baca.SingleStaffScoreTemplate(),
            ...     spacing=baca.minimum_duration((1, 12)),
            ...     time_signatures=[(3, 8), (4, 8), (3, 8), (4, 8)],
            ...     )

            >>> command = baca.RhythmCommand(
            ...     divisions=abjad.sequence().sum().sequence(),
            ...     rhythm_maker=rmakers.EvenDivisionRhythmMaker(
            ...         rmakers.BeamSpecifier(
            ...             selector=baca.tuplets(),
            ...         ),
            ...         rmakers.TupletSpecifier(
            ...             extract_trivial=True,
            ...             ),
            ...     ),
            ... )

            >>> maker(
            ...     'Music_Voice',
            ...     command,
            ...     )

            >>> lilypond_file = maker.run(environment='docs')
            >>> abjad.show(lilypond_file, strict=89) # doctest: +SKIP

            ..  docs::

                >>> abjad.f(lilypond_file[abjad.Score], strict=89)
                <BLANKLINE>
                \context Score = "Score"                                                                 %! baca.SingleStaffScoreTemplate.__call__
                <<                                                                                       %! baca.SingleStaffScoreTemplate.__call__
                <BLANKLINE>
                    \context GlobalContext = "Global_Context"                                            %! abjad.ScoreTemplate._make_global_context
                    <<                                                                                   %! abjad.ScoreTemplate._make_global_context
                <BLANKLINE>
                        \context GlobalSkips = "Global_Skips"                                            %! abjad.ScoreTemplate._make_global_context
                        {                                                                                %! abjad.ScoreTemplate._make_global_context
                <BLANKLINE>
                            % [Global_Skips measure 1]                                                   %! _comment_measure_numbers
                            \baca-new-spacing-section #1 #12                                             %! HorizontalSpacingSpecifier(1):SPACING_COMMAND
                            \time 3/8                                                                    %! EXPLICIT_TIME_SIGNATURE:_set_status_tag:_make_global_skips(2)
                            \baca-time-signature-color #'blue                                            %! EXPLICIT_TIME_SIGNATURE_COLOR:_attach_color_literal(2)
                            s1 * 3/8                                                                     %! _make_global_skips(1)
                <BLANKLINE>
                            % [Global_Skips measure 2]                                                   %! _comment_measure_numbers
                            \baca-new-spacing-section #1 #12                                             %! HorizontalSpacingSpecifier(1):SPACING_COMMAND
                            \time 4/8                                                                    %! EXPLICIT_TIME_SIGNATURE:_set_status_tag:_make_global_skips(2)
                            \baca-time-signature-color #'blue                                            %! EXPLICIT_TIME_SIGNATURE_COLOR:_attach_color_literal(2)
                            s1 * 1/2                                                                     %! _make_global_skips(1)
                <BLANKLINE>
                            % [Global_Skips measure 3]                                                   %! _comment_measure_numbers
                            \baca-new-spacing-section #1 #12                                             %! HorizontalSpacingSpecifier(1):SPACING_COMMAND
                            \time 3/8                                                                    %! EXPLICIT_TIME_SIGNATURE:_set_status_tag:_make_global_skips(2)
                            \baca-time-signature-color #'blue                                            %! EXPLICIT_TIME_SIGNATURE_COLOR:_attach_color_literal(2)
                            s1 * 3/8                                                                     %! _make_global_skips(1)
                <BLANKLINE>
                            % [Global_Skips measure 4]                                                   %! _comment_measure_numbers
                            \baca-new-spacing-section #1 #12                                             %! HorizontalSpacingSpecifier(1):SPACING_COMMAND
                            \time 4/8                                                                    %! EXPLICIT_TIME_SIGNATURE:_set_status_tag:_make_global_skips(2)
                            \baca-time-signature-color #'blue                                            %! EXPLICIT_TIME_SIGNATURE_COLOR:_attach_color_literal(2)
                            s1 * 1/2                                                                     %! _make_global_skips(1)
                            \baca-bar-line-visible                                                       %! _attach_final_bar_line
                            \bar "|"                                                                     %! _attach_final_bar_line
                <BLANKLINE>
                            % [Global_Skips measure 5]                                                   %! PHANTOM:_style_phantom_measures(1):_comment_measure_numbers
                            \baca-new-spacing-section #1 #4                                              %! PHANTOM:_style_phantom_measures(1):HorizontalSpacingSpecifier(1):SPACING_COMMAND
                            \time 1/4                                                                    %! PHANTOM:_style_phantom_measures(1):EXPLICIT_TIME_SIGNATURE:_set_status_tag:_make_global_skips(3)
                            \baca-time-signature-transparent                                             %! PHANTOM:_style_phantom_measures(2)
                            s1 * 1/4                                                                     %! PHANTOM:_make_global_skips(3)
                            \once \override Score.BarLine.transparent = ##t                              %! PHANTOM:_style_phantom_measures(3)
                            \once \override Score.SpanBar.transparent = ##t                              %! PHANTOM:_style_phantom_measures(3)
                <BLANKLINE>
                        }                                                                                %! abjad.ScoreTemplate._make_global_context
                <BLANKLINE>
                    >>                                                                                   %! abjad.ScoreTemplate._make_global_context
                <BLANKLINE>
                    \context MusicContext = "Music_Context"                                              %! baca.SingleStaffScoreTemplate.__call__
                    <<                                                                                   %! baca.SingleStaffScoreTemplate.__call__
                <BLANKLINE>
                        \context Staff = "Music_Staff"                                                   %! baca.SingleStaffScoreTemplate.__call__
                        {                                                                                %! baca.SingleStaffScoreTemplate.__call__
                <BLANKLINE>
                            \context Voice = "Music_Voice"                                               %! baca.SingleStaffScoreTemplate.__call__
                            {                                                                            %! baca.SingleStaffScoreTemplate.__call__
                <BLANKLINE>
                                % [Music_Voice measure 1]                                                %! _comment_measure_numbers
                                \baca-unpitched-music-warning                                            %! _color_unpitched_notes
                                c'8
                                [
                <BLANKLINE>
                                \baca-unpitched-music-warning                                            %! _color_unpitched_notes
                                c'8
                <BLANKLINE>
                                \baca-unpitched-music-warning                                            %! _color_unpitched_notes
                                c'8
                <BLANKLINE>
                                % [Music_Voice measure 2]                                                %! _comment_measure_numbers
                                \baca-unpitched-music-warning                                            %! _color_unpitched_notes
                                c'8
                <BLANKLINE>
                                \baca-unpitched-music-warning                                            %! _color_unpitched_notes
                                c'8
                <BLANKLINE>
                                \baca-unpitched-music-warning                                            %! _color_unpitched_notes
                                c'8
                <BLANKLINE>
                                \baca-unpitched-music-warning                                            %! _color_unpitched_notes
                                c'8
                <BLANKLINE>
                                % [Music_Voice measure 3]                                                %! _comment_measure_numbers
                                \baca-unpitched-music-warning                                            %! _color_unpitched_notes
                                c'8
                <BLANKLINE>
                                \baca-unpitched-music-warning                                            %! _color_unpitched_notes
                                c'8
                <BLANKLINE>
                                \baca-unpitched-music-warning                                            %! _color_unpitched_notes
                                c'8
                <BLANKLINE>
                                % [Music_Voice measure 4]                                                %! _comment_measure_numbers
                                \baca-unpitched-music-warning                                            %! _color_unpitched_notes
                                c'8
                <BLANKLINE>
                                \baca-unpitched-music-warning                                            %! _color_unpitched_notes
                                c'8
                <BLANKLINE>
                                \baca-unpitched-music-warning                                            %! _color_unpitched_notes
                                c'8
                <BLANKLINE>
                                \baca-unpitched-music-warning                                            %! _color_unpitched_notes
                                c'8
                                ]
                <BLANKLINE>
                                <<                                                                       %! PHANTOM:_make_multimeasure_rest_container
                <BLANKLINE>
                                    \context Voice = "Music_Voice"                                       %! PHANTOM:_make_multimeasure_rest_container
                                    {                                                                    %! PHANTOM:_make_multimeasure_rest_container
                <BLANKLINE>
                                        % [Music_Voice measure 5]                                        %! PHANTOM:_style_phantom_measures(5):_comment_measure_numbers
                                        \baca-invisible-music                                            %! PHANTOM:_style_phantom_measures(5):_make_multimeasure_rest_container
                                        c'1 * 1/4                                                        %! PHANTOM:_make_multimeasure_rest_container
                <BLANKLINE>
                                    }                                                                    %! PHANTOM:_make_multimeasure_rest_container
                <BLANKLINE>
                                    \context Voice = "Rest_Voice"                                        %! PHANTOM:_make_multimeasure_rest_container
                                    {                                                                    %! PHANTOM:_make_multimeasure_rest_container
                <BLANKLINE>
                                        % [Rest_Voice measure 5]                                         %! PHANTOM:_style_phantom_measures(5):_comment_measure_numbers
                                        \once \override Score.TimeSignature.X-extent = ##f               %! PHANTOM:_style_phantom_measures(6)
                                        \once \override MultiMeasureRest.transparent = ##t               %! PHANTOM:_style_phantom_measures(7)
                                        \stopStaff                                                       %! PHANTOM:_style_phantom_measures(8)
                                        \once \override Staff.StaffSymbol.transparent = ##t              %! PHANTOM:_style_phantom_measures(8)
                                        \startStaff                                                      %! PHANTOM:_style_phantom_measures(8)
                                        R1 * 1/4                                                         %! PHANTOM:_make_multimeasure_rest_container
                <BLANKLINE>
                                    }                                                                    %! PHANTOM:_make_multimeasure_rest_container
                <BLANKLINE>
                                >>                                                                       %! PHANTOM:_make_multimeasure_rest_container
                <BLANKLINE>
                            }                                                                            %! baca.SingleStaffScoreTemplate.__call__
                <BLANKLINE>
                        }                                                                                %! baca.SingleStaffScoreTemplate.__call__
                <BLANKLINE>
                    >>                                                                                   %! baca.SingleStaffScoreTemplate.__call__
                <BLANKLINE>
                >>                                                                                       %! baca.SingleStaffScoreTemplate.__call__

        """
        return self._divisions

    @property
    def left_broken(self) -> typing.Optional[bool]:
        """
        Is true when rhythm is left-broken.

        Talea rhythm-maker knows how to tag incomplete last notes.
        """
        return self._left_broken

    @property
    def parameter(self) -> str:
        """
        Gets persistence parameter.

        ..  container:: example

            >>> baca.RhythmCommand().parameter
            'RHYTHM'

        """
        return const.RHYTHM

    @property
    def persist(self) -> typing.Optional[str]:
        """
        Gets persist name.
        """
        return self._persist

    @property
    def reference_meters(
        self
    ) -> typing.Optional[typing.Iterable[abjad.Meter]]:
        """
        Gets reference meters.

        Only used to rewrite meters.
        """
        return self._reference_meters

    # TODO: remove in favor of dedicated TieSpecifier objects passed to
    #       every command that should accept a TieSpecifier
    @property
    def repeat_ties(
        self
    ) -> typing.Union[bool, abjad.DurationInequality, None]:
        """
        Is true when rhythm command uses repeat ties.
        """
        tie_specifier = getattr(self.rhythm_maker, "tie_specifier", None)
        if tie_specifier is not None:
            return tie_specifier.repeat_ties
        assert isinstance(self.rhythm_maker, rmakers.RhythmMaker)
        for specifier in self.rhythm_maker.specifiers or []:
            if isinstance(specifier, rmakers.TieSpecifier):
                tie_specifier = specifier
                break
        if tie_specifier is None:
            return False
        return tie_specifier.repeat_ties

    @property
    def rhythm_maker(self) -> typing.Optional[RhythmMakerTyping]:
        r"""
        Gets rhythm-maker-or-selection or (rhythm-maker-or-selection, pattern)
        pairs.

        ..  container:: example

            Talea rhythm-maker remembers previous state across divisions:

            >>> maker = baca.SegmentMaker(
            ...     score_template=baca.SingleStaffScoreTemplate(),
            ...     spacing=baca.minimum_duration((1, 12)),
            ...     time_signatures=5 * [(4, 8)],
            ...     )

            >>> rhythm_maker_1 = rmakers.NoteRhythmMaker(
            ...     rmakers.SilenceMask(selector=baca.lts()),
            ...     rmakers.BeamSpecifier(
            ...         selector=baca.plts(),
            ...     ),
            ... )
            >>> rhythm_maker_2 = rmakers.TaleaRhythmMaker(
            ...     rmakers.BeamSpecifier(
            ...         selector=baca.tuplets(),
            ...     ),
            ...     rmakers.TupletSpecifier(
            ...         extract_trivial=True,
            ...     ),
            ...     talea=rmakers.Talea(
            ...         counts=[3, 4],
            ...         denominator=16,
            ...         ),
            ...     )
            >>> command = baca.RhythmCommand(
            ...     rhythm_maker=[
            ...         baca.DivisionAssignment(
            ...             abjad.index([2]), rhythm_maker_1
            ...         ),
            ...         baca.DivisionAssignment(
            ...             abjad.index([0], 1), rhythm_maker_2
            ...         ),
            ...     ],
            ... )

            >>> label = abjad.label().with_durations(
            ...     direction=abjad.Down,
            ...     denominator=16,
            ...     )
            >>> maker(
            ...     'Music_Voice',
            ...     baca.label(label),
            ...     baca.text_script_font_size(-2),
            ...     baca.text_script_staff_padding(5),
            ...     command,
            ...     )

            >>> lilypond_file = maker.run(environment='docs')
            >>> abjad.show(lilypond_file, strict=89) # doctest: +SKIP

            ..  docs::

                >>> abjad.f(lilypond_file[abjad.Score], strict=89)
                <BLANKLINE>
                \context Score = "Score"                                                                 %! baca.SingleStaffScoreTemplate.__call__
                <<                                                                                       %! baca.SingleStaffScoreTemplate.__call__
                <BLANKLINE>
                    \context GlobalContext = "Global_Context"                                            %! abjad.ScoreTemplate._make_global_context
                    <<                                                                                   %! abjad.ScoreTemplate._make_global_context
                <BLANKLINE>
                        \context GlobalSkips = "Global_Skips"                                            %! abjad.ScoreTemplate._make_global_context
                        {                                                                                %! abjad.ScoreTemplate._make_global_context
                <BLANKLINE>
                            % [Global_Skips measure 1]                                                   %! _comment_measure_numbers
                            \baca-new-spacing-section #1 #16                                             %! HorizontalSpacingSpecifier(1):SPACING_COMMAND
                            \time 4/8                                                                    %! EXPLICIT_TIME_SIGNATURE:_set_status_tag:_make_global_skips(2)
                            \baca-time-signature-color #'blue                                            %! EXPLICIT_TIME_SIGNATURE_COLOR:_attach_color_literal(2)
                            s1 * 1/2                                                                     %! _make_global_skips(1)
                <BLANKLINE>
                            % [Global_Skips measure 2]                                                   %! _comment_measure_numbers
                            \baca-new-spacing-section #1 #12                                             %! HorizontalSpacingSpecifier(1):SPACING_COMMAND
                            s1 * 1/2                                                                     %! _make_global_skips(1)
                <BLANKLINE>
                            % [Global_Skips measure 3]                                                   %! _comment_measure_numbers
                            \baca-new-spacing-section #1 #12                                             %! HorizontalSpacingSpecifier(1):SPACING_COMMAND
                            s1 * 1/2                                                                     %! _make_global_skips(1)
                <BLANKLINE>
                            % [Global_Skips measure 4]                                                   %! _comment_measure_numbers
                            \baca-new-spacing-section #1 #16                                             %! HorizontalSpacingSpecifier(1):SPACING_COMMAND
                            s1 * 1/2                                                                     %! _make_global_skips(1)
                <BLANKLINE>
                            % [Global_Skips measure 5]                                                   %! _comment_measure_numbers
                            \baca-new-spacing-section #1 #16                                             %! HorizontalSpacingSpecifier(1):SPACING_COMMAND
                            s1 * 1/2                                                                     %! _make_global_skips(1)
                            \baca-bar-line-visible                                                       %! _attach_final_bar_line
                            \bar "|"                                                                     %! _attach_final_bar_line
                <BLANKLINE>
                            % [Global_Skips measure 6]                                                   %! PHANTOM:_style_phantom_measures(1):_comment_measure_numbers
                            \baca-new-spacing-section #1 #4                                              %! PHANTOM:_style_phantom_measures(1):HorizontalSpacingSpecifier(1):SPACING_COMMAND
                            \time 1/4                                                                    %! PHANTOM:_style_phantom_measures(1):EXPLICIT_TIME_SIGNATURE:_set_status_tag:_make_global_skips(3)
                            \baca-time-signature-transparent                                             %! PHANTOM:_style_phantom_measures(2)
                            s1 * 1/4                                                                     %! PHANTOM:_make_global_skips(3)
                            \once \override Score.BarLine.transparent = ##t                              %! PHANTOM:_style_phantom_measures(3)
                            \once \override Score.SpanBar.transparent = ##t                              %! PHANTOM:_style_phantom_measures(3)
                <BLANKLINE>
                        }                                                                                %! abjad.ScoreTemplate._make_global_context
                <BLANKLINE>
                    >>                                                                                   %! abjad.ScoreTemplate._make_global_context
                <BLANKLINE>
                    \context MusicContext = "Music_Context"                                              %! baca.SingleStaffScoreTemplate.__call__
                    <<                                                                                   %! baca.SingleStaffScoreTemplate.__call__
                <BLANKLINE>
                        \context Staff = "Music_Staff"                                                   %! baca.SingleStaffScoreTemplate.__call__
                        {                                                                                %! baca.SingleStaffScoreTemplate.__call__
                <BLANKLINE>
                            \context Voice = "Music_Voice"                                               %! baca.SingleStaffScoreTemplate.__call__
                            {                                                                            %! baca.SingleStaffScoreTemplate.__call__
                <BLANKLINE>
                                % [Music_Voice measure 1]                                                %! _comment_measure_numbers
                                \override TextScript.font-size = #-2                                     %! baca.text_script_font_size:OverrideCommand(1)
                                \override TextScript.staff-padding = #5                                  %! baca.text_script_staff_padding:OverrideCommand(1)
                                \baca-unpitched-music-warning                                            %! _color_unpitched_notes
                                c'8.
                                _ \markup {
                                    \fraction
                                        3
                                        16
                                    }
                <BLANKLINE>
                                \baca-unpitched-music-warning                                            %! _color_unpitched_notes
                                c'4
                                _ \markup {
                                    \fraction
                                        4
                                        16
                                    }
                <BLANKLINE>
                                \baca-unpitched-music-warning                                            %! _color_unpitched_notes
                                c'16
                                _ \markup {
                                    \fraction
                                        3
                                        16
                                    }
                                ~
                <BLANKLINE>
                                % [Music_Voice measure 2]                                                %! _comment_measure_numbers
                                \baca-unpitched-music-warning                                            %! _color_unpitched_notes
                                c'8
                <BLANKLINE>
                                \baca-unpitched-music-warning                                            %! _color_unpitched_notes
                                c'4
                                _ \markup {
                                    \fraction
                                        4
                                        16
                                    }
                <BLANKLINE>
                                \baca-unpitched-music-warning                                            %! _color_unpitched_notes
                                c'8
                                _ \markup {
                                    \fraction
                                        2
                                        16
                                    }
                <BLANKLINE>
                                % [Music_Voice measure 3]                                                %! _comment_measure_numbers
                                r2
                                _ \markup {
                                    \fraction
                                        8
                                        16
                                    }
                <BLANKLINE>
                                % [Music_Voice measure 4]                                                %! _comment_measure_numbers
                                \baca-unpitched-music-warning                                            %! _color_unpitched_notes
                                c'16
                                _ \markup {
                                    \fraction
                                        1
                                        16
                                    }
                <BLANKLINE>
                                \baca-unpitched-music-warning                                            %! _color_unpitched_notes
                                c'4
                                _ \markup {
                                    \fraction
                                        4
                                        16
                                    }
                <BLANKLINE>
                                \baca-unpitched-music-warning                                            %! _color_unpitched_notes
                                c'8.
                                _ \markup {
                                    \fraction
                                        3
                                        16
                                    }
                <BLANKLINE>
                                % [Music_Voice measure 5]                                                %! _comment_measure_numbers
                                \baca-unpitched-music-warning                                            %! _color_unpitched_notes
                                c'4
                                _ \markup {
                                    \fraction
                                        4
                                        16
                                    }
                <BLANKLINE>
                                \baca-unpitched-music-warning                                            %! _color_unpitched_notes
                                c'8.
                                _ \markup {
                                    \fraction
                                        3
                                        16
                                    }
                                [
                <BLANKLINE>
                                \baca-unpitched-music-warning                                            %! _color_unpitched_notes
                                c'16
                                _ \markup {
                                    \fraction
                                        1
                                        16
                                    }
                                ]
                                \revert TextScript.font-size                                             %! baca.text_script_font_size:OverrideCommand(2)
                                \revert TextScript.staff-padding                                         %! baca.text_script_staff_padding:OverrideCommand(2)
                <BLANKLINE>
                                <<                                                                       %! PHANTOM:_make_multimeasure_rest_container
                <BLANKLINE>
                                    \context Voice = "Music_Voice"                                       %! PHANTOM:_make_multimeasure_rest_container
                                    {                                                                    %! PHANTOM:_make_multimeasure_rest_container
                <BLANKLINE>
                                        % [Music_Voice measure 6]                                        %! PHANTOM:_style_phantom_measures(5):_comment_measure_numbers
                                        \baca-invisible-music                                            %! PHANTOM:_style_phantom_measures(5):_make_multimeasure_rest_container
                                        c'1 * 1/4                                                        %! PHANTOM:_make_multimeasure_rest_container
                <BLANKLINE>
                                    }                                                                    %! PHANTOM:_make_multimeasure_rest_container
                <BLANKLINE>
                                    \context Voice = "Rest_Voice"                                        %! PHANTOM:_make_multimeasure_rest_container
                                    {                                                                    %! PHANTOM:_make_multimeasure_rest_container
                <BLANKLINE>
                                        % [Rest_Voice measure 6]                                         %! PHANTOM:_style_phantom_measures(5):_comment_measure_numbers
                                        \once \override Score.TimeSignature.X-extent = ##f               %! PHANTOM:_style_phantom_measures(6)
                                        \once \override MultiMeasureRest.transparent = ##t               %! PHANTOM:_style_phantom_measures(7)
                                        \stopStaff                                                       %! PHANTOM:_style_phantom_measures(8)
                                        \once \override Staff.StaffSymbol.transparent = ##t              %! PHANTOM:_style_phantom_measures(8)
                                        \startStaff                                                      %! PHANTOM:_style_phantom_measures(8)
                                        R1 * 1/4                                                         %! PHANTOM:_make_multimeasure_rest_container
                <BLANKLINE>
                                    }                                                                    %! PHANTOM:_make_multimeasure_rest_container
                <BLANKLINE>
                                >>                                                                       %! PHANTOM:_make_multimeasure_rest_container
                <BLANKLINE>
                            }                                                                            %! baca.SingleStaffScoreTemplate.__call__
                <BLANKLINE>
                        }                                                                                %! baca.SingleStaffScoreTemplate.__call__
                <BLANKLINE>
                    >>                                                                                   %! baca.SingleStaffScoreTemplate.__call__
                <BLANKLINE>
                >>                                                                                       %! baca.SingleStaffScoreTemplate.__call__

        ..  container:: example exception

            Raises exception on invalid input:

            >>> command = baca.RhythmCommand(
            ...     rhythm_maker='text',
            ...     )
            Traceback (most recent call last):
                ...
            Exception:
              Input parameter "rhythm_maker" accepts:
                rhythm-maker
                selection
                sequence of division assignment objects
                none
              Input parameter "rhythm_maker" received:
                text

        """
        return self._rhythm_maker

    @property
    def right_broken(self) -> typing.Optional[bool]:
        """
        Is true when rhythm is right-broken.

        Talea rhythm-maker knows how to tag incomplete last notes.
        """
        return self._right_broken

    @property
    def state(self) -> typing.Optional[abjad.OrderedDict]:
        """
        Gets postcall state of rhythm command.

        Populated by segment-maker.
        """
        return self._state


class SkipRhythmMaker(rmakers.RhythmMaker):
    r"""
    Skip rhythm-maker.

    ..  container:: example

        Makes skips.

        >>> rhythm_maker = baca.SkipRhythmMaker()

        >>> divisions = [(1, 4), (3, 16), (5, 8), (1, 3)]
        >>> selections = rhythm_maker(divisions)
        >>> lilypond_file = abjad.LilyPondFile.rhythm(
        ...     selections,
        ...     divisions,
        ...     )
        >>> abjad.show(lilypond_file) # doctest: +SKIP

        ..  docs::

            >>> abjad.f(lilypond_file[abjad.Score])
            \new Score
            <<
                \new GlobalContext
                {
                    \time 1/4
                    s1 * 1/4
                    \time 3/16
                    s1 * 3/16
                    \time 5/8
                    s1 * 5/8
                    #(ly:expect-warning "strange time signature found")
                    \time 1/3
                    s1 * 1/3
                }
                \new RhythmicStaff
                {
                    s1 * 1/4
                    s1 * 3/16
                    s1 * 5/8
                    s1 * 1/3
                }
            >>

    ..  container:: example

        Makes multimeasure rests.

        >>> rhythm_maker = baca.SkipRhythmMaker(use_multimeasure_rests=True)

        >>> divisions = [(1, 4), (3, 16), (5, 8), (1, 3)]
        >>> selections = rhythm_maker(divisions)
        >>> lilypond_file = abjad.LilyPondFile.rhythm(
        ...     selections,
        ...     divisions,
        ...     )
        >>> abjad.show(lilypond_file) # doctest: +SKIP

        ..  docs::

            >>> abjad.f(lilypond_file[abjad.Score])
            \new Score
            <<
                \new GlobalContext
                {
                    \time 1/4
                    s1 * 1/4
                    \time 3/16
                    s1 * 3/16
                    \time 5/8
                    s1 * 5/8
                    #(ly:expect-warning "strange time signature found")
                    \time 1/3
                    s1 * 1/3
                }
                \new RhythmicStaff
                {
                    R1 * 1/4
                    R1 * 3/16
                    R1 * 5/8
                    R1 * 1/3
                }
            >>

    Usage follows the two-step configure-once / call-repeatedly pattern shown
    here.
    """

    ### CLASS VARIABLES ###

    __slots__ = ("_use_multimeasure_rests",)

    ### INITIALIZER ###

    def __init__(
        self,
        *specifiers: rmakers.SpecifierTyping,
        divisions: abjad.Expression = None,
        tag: str = None,
        use_multimeasure_rests: bool = None,
    ) -> None:
        rmakers.RhythmMaker.__init__(
            self, *specifiers, divisions=divisions, tag=tag
        )
        if use_multimeasure_rests is not None:
            use_multimeasure_rests = bool(use_multimeasure_rests)
        self._use_multimeasure_rests = use_multimeasure_rests

    ### SPECIAL METHODS ###

    def __call__(
        self,
        divisions: typing.Sequence[abjad.IntegerPair],
        previous_state: abjad.OrderedDict = None,
    ) -> typing.List[abjad.Selection]:
        """
        Calls skip rhythm-maker on ``divisions``.
        """
        return rmakers.RhythmMaker.__call__(
            self, divisions, previous_state=previous_state
        )

    def __format__(self, format_specification="") -> str:
        """
        Formats skip rhythm-maker.

        Set ``format_specification`` to ``''`` or ``'storage'``.

        ..  container:: example

            >>> rhythm_maker = baca.SkipRhythmMaker()
            >>> abjad.f(rhythm_maker)
            baca.SkipRhythmMaker()

        """
        return super().__format__(format_specification=format_specification)

    ### PRIVATE METHODS ###

    def _make_music(self, divisions) -> typing.List[abjad.Selection]:
        selections = []
        component: typing.Union[abjad.MultimeasureRest, abjad.Skip]
        for division in divisions:
            assert isinstance(division, abjad.NonreducedFraction)
            if self.use_multimeasure_rests is True:
                component = abjad.MultimeasureRest(
                    1, multiplier=division, tag=self.tag
                )
            else:
                component = abjad.Skip(1, multiplier=division, tag=self.tag)
            selection = abjad.select(component)
            selections.append(selection)
        return selections

    ### PUBLIC PROPERTIES ###

    @property
    def use_multimeasure_rests(self) -> typing.Optional[bool]:
        r"""
        Is true when rhythm-maker makes multimeasure rests instead of skips.
        """
        return self._use_multimeasure_rests


# TODO: replace with just baca.tie(), baca.repeat_tie() functions
class TieCorrectionCommand(scoping.Command):
    """
    Tie correction command.

    ..  container:: example

        >>> baca.TieCorrectionCommand()
        TieCorrectionCommand(selector=baca.pleaf(-1))

    """

    ### CLASS VARIABLES ###

    __slots__ = ("_allow_rest", "_direction", "_repeat", "_untie")

    ### INITIALIZER ###

    def __init__(
        self,
        *,
        allow_rest: bool = None,
        direction: abjad.HorizontalAlignment = None,
        map: abjad.SelectorTyping = None,
        match: typings.Indices = None,
        measures: typings.SliceTyping = None,
        repeat: bool = None,
        scope: scoping.ScopeTyping = None,
        selector: abjad.SelectorTyping = "baca.pleaf(-1)",
        untie: bool = None,
    ) -> None:
        scoping.Command.__init__(
            self,
            map=map,
            match=match,
            measures=measures,
            scope=scope,
            selector=selector,
        )
        if allow_rest is not None:
            allow_rest = bool(allow_rest)
        self._allow_rest = allow_rest
        if direction is not None:
            assert direction in (abjad.Right, abjad.Left, None)
        self._direction = direction
        if repeat is not None:
            repeat = bool(repeat)
        self._repeat = repeat
        if untie is not None:
            untie = bool(untie)
        self._untie = untie

    ### SPECIAL METHODS ###

    def _call(self, argument=None) -> None:
        """
        Applies ``TieCorrectionCommand`` to result of selector called on
        ``argument``.
        """
        if argument is None:
            return
        if self.selector is not None:
            argument = self.selector(argument)
        leaves = classes.Selection(argument).leaves()
        assert isinstance(leaves, classes.Selection)
        for leaf in leaves:
            if self.untie is True:
                self._sever_tie(leaf, self.direction)
            else:
                self._add_tie(leaf, self.direction, self.repeat)

    ### PRIVATE METHODS ###

    def _add_tie(self, current_leaf, direction, repeat):
        assert direction in (abjad.Left, abjad.Right, None), repr(direction)
        tag_ = "TieCorrectionCommand"
        left_broken, right_broken = None, None
        if direction is None:
            direction = abjad.Right
        if direction == abjad.Right:
            next_leaf = abjad.inspect(current_leaf).leaf(1)
            if next_leaf is None:
                right_broken = True
            else:
                pass
        else:
            assert direction == abjad.Left
            previous_leaf = abjad.inspect(current_leaf).leaf(-1)
            if previous_leaf is None:
                left_broken = True
            else:
                pass
        if direction == abjad.Left:
            if repeat:
                repeat_tie = abjad.RepeatTie(left_broken=left_broken)
                abjad.attach(
                    repeat_tie,
                    current_leaf,
                    do_not_test=self.allow_rest,
                    tag=tag_,
                )
            else:
                tie = abjad.TieIndicator(right_broken=right_broken)
                abjad.attach(
                    tie, previous_leaf, do_not_test=self.allow_rest, tag=tag_
                )
        else:
            assert direction == abjad.Right
            if not repeat:
                tie = abjad.TieIndicator(right_broken=right_broken)
                abjad.attach(
                    tie, current_leaf, do_not_test=self.allow_rest, tag=tag_
                )
            else:
                repeat_tie = abjad.RepeatTie(left_broken=left_broken)
                abjad.attach(
                    repeat_tie,
                    next_leaf,
                    do_not_test=self.allow_rest,
                    tag=tag_,
                )

    @staticmethod
    def _sever_tie(current_leaf, direction):
        if direction in (abjad.Right, None):
            abjad.detach(abjad.TieIndicator, current_leaf)
            next_leaf = abjad.inspect(current_leaf).leaf(1)
            if next_leaf is not None:
                abjad.detach(abjad.RepeatTie, next_leaf)
        else:
            assert direction == abjad.Left
            abjad.detach(abjad.RepeatTie, current_leaf)
            previous_leaf = abjad.inspect(current_leaf).leaf(-1)
            if previous_leaf is not None:
                abjad.detach(abjad.TieIndicator, previous_leaf)

    ### PUBLIC PROPERTIES ###

    @property
    def allow_rest(self) -> typing.Optional[bool]:
        """
        Is true when tie is allowed to connect to rest.
        """
        return self._allow_rest

    @property
    def direction(self) -> typing.Optional[abjad.HorizontalAlignment]:
        """
        Gets direction.

        Interprets none equal to right.
        """
        return self._direction

    @property
    def repeat(self) -> typing.Optional[bool]:
        """
        Is true when newly created ties should be repeat ties.
        """
        return self._repeat

    @property
    def untie(self) -> typing.Optional[bool]:
        """
        Is true when command severs tie instead of creating tie.
        """
        return self._untie


### FACTORY FUNCTIONS ###


def beam_divisions(*, stemlets: abjad.Number = None) -> rmakers.BeamSpecifier:
    r"""
    Beams divisions.

    ..  container:: example

        Beams divisions:

        >>> music_maker = baca.MusicMaker()
        >>> contribution = music_maker(
        ...     'Voice_1',
        ...     [[0, 2, 10], [18, 16, 15, 20, 19], [9]],
        ...     baca.beam_divisions(),
        ...     baca.rests_around([2], [2]),
        ...     )
        >>> lilypond_file = music_maker.show(contribution)
        >>> abjad.show(lilypond_file, strict=89) # doctest: +SKIP

        ..  docs::

            >>> abjad.f(lilypond_file[abjad.Staff], strict=89)
            \new Staff
            <<
                \context Voice = "Voice_1"
                {
                    \voiceOne
                    {
                        \scaleDurations #'(1 . 1) {
                            r8
                            c'16
                            [
                            d'16
                            bf'16
                            ]
                        }
                        \scaleDurations #'(1 . 1) {
                            fs''16
                            [
                            e''16
                            ef''16
                            af''16
                            g''16
                            ]
                        }
                        \scaleDurations #'(1 . 1) {
                            a'16
                            r8
                        }
                    }
                }
            >>

    ..  container:: example

        Beams divisions with stemlets:

        >>> music_maker = baca.MusicMaker()
        >>> contribution = music_maker(
        ...     'Voice_1',
        ...     [[0, 2, 10], [18, 16, 15, 20, 19], [9]],
        ...     baca.beam_divisions(stemlets=2),
        ...     baca.rests_around([2], [2]),
        ...     )
        >>> lilypond_file = music_maker.show(contribution)
        >>> abjad.show(lilypond_file, strict=89) # doctest: +SKIP

        ..  docs::

            >>> abjad.f(lilypond_file[abjad.Staff], strict=89)
            \new Staff
            <<
                \context Voice = "Voice_1"
                {
                    \voiceOne
                    {
                        \scaleDurations #'(1 . 1) {
                            \override Staff.Stem.stemlet-length = 2
                            r8
                            [
                            c'16
                            d'16
                            \revert Staff.Stem.stemlet-length
                            bf'16
                            ]
                        }
                        \scaleDurations #'(1 . 1) {
                            \override Staff.Stem.stemlet-length = 2
                            fs''16
                            [
                            e''16
                            ef''16
                            af''16
                            \revert Staff.Stem.stemlet-length
                            g''16
                            ]
                        }
                        \scaleDurations #'(1 . 1) {
                            \override Staff.Stem.stemlet-length = 2
                            a'16
                            [
                            \revert Staff.Stem.stemlet-length
                            r8
                            ]
                        }
                    }
                }
            >>

    """
    return rmakers.BeamSpecifier(
        beam_rests=bool(stemlets),
        selector=classes._select().tuplets(),
        stemlet_length=stemlets,
    )


def beam_everything(*, stemlets: abjad.Number = None) -> rmakers.BeamSpecifier:
    r"""
    Beams everything.

    ..  container:: example

        Beams everything:

        >>> music_maker = baca.MusicMaker()
        >>> contribution = music_maker(
        ...     'Voice_1',
        ...     [[0, 2, 10], [18, 16, 15, 20, 19], [9]],
        ...     baca.beam_everything(),
        ...     baca.rests_around([2], [2]),
        ...     )
        >>> lilypond_file = music_maker.show(contribution)
        >>> abjad.show(lilypond_file, strict=89) # doctest: +SKIP

        ..  docs::

            >>> abjad.f(lilypond_file[abjad.Staff], strict=89)
            \new Staff
            <<
                \context Voice = "Voice_1"
                {
                    \voiceOne
                    {
                        \scaleDurations #'(1 . 1) {
                            r8
                            [
                            \set stemLeftBeamCount = 1
                            \set stemRightBeamCount = 2
                            c'16
                            \set stemLeftBeamCount = 2
                            \set stemRightBeamCount = 2
                            d'16
                            \set stemLeftBeamCount = 2
                            \set stemRightBeamCount = 1
                            bf'16
                        }
                        \scaleDurations #'(1 . 1) {
                            \set stemLeftBeamCount = 1
                            \set stemRightBeamCount = 2
                            fs''16
                            \set stemLeftBeamCount = 2
                            \set stemRightBeamCount = 2
                            e''16
                            \set stemLeftBeamCount = 2
                            \set stemRightBeamCount = 2
                            ef''16
                            \set stemLeftBeamCount = 2
                            \set stemRightBeamCount = 2
                            af''16
                            \set stemLeftBeamCount = 2
                            \set stemRightBeamCount = 1
                            g''16
                        }
                        \scaleDurations #'(1 . 1) {
                            \set stemLeftBeamCount = 1
                            \set stemRightBeamCount = 2
                            a'16
                            r8
                            ]
                        }
                    }
                }
            >>

    ..  container:: example

        Beams everything with stemlets:

        >>> music_maker = baca.MusicMaker()
        >>> contribution = music_maker(
        ...     'Voice_1',
        ...     [[0, 2, 10], [18, 16, 15, 20, 19], [9]],
        ...     baca.beam_everything(stemlets=2),
        ...     baca.rests_around([2], [2]),
        ...     )
        >>> lilypond_file = music_maker.show(contribution)
        >>> abjad.show(lilypond_file, strict=89) # doctest: +SKIP

        ..  docs::

            >>> abjad.f(lilypond_file[abjad.Staff], strict=89)
            \new Staff
            <<
                \context Voice = "Voice_1"
                {
                    \voiceOne
                    {
                        \scaleDurations #'(1 . 1) {
                            \override Staff.Stem.stemlet-length = 2
                            r8
                            [
                            \set stemLeftBeamCount = 1
                            \set stemRightBeamCount = 2
                            c'16
                            \set stemLeftBeamCount = 2
                            \set stemRightBeamCount = 2
                            d'16
                            \set stemLeftBeamCount = 2
                            \set stemRightBeamCount = 1
                            bf'16
                        }
                        \scaleDurations #'(1 . 1) {
                            \set stemLeftBeamCount = 1
                            \set stemRightBeamCount = 2
                            fs''16
                            \set stemLeftBeamCount = 2
                            \set stemRightBeamCount = 2
                            e''16
                            \set stemLeftBeamCount = 2
                            \set stemRightBeamCount = 2
                            ef''16
                            \set stemLeftBeamCount = 2
                            \set stemRightBeamCount = 2
                            af''16
                            \set stemLeftBeamCount = 2
                            \set stemRightBeamCount = 1
                            g''16
                        }
                        \scaleDurations #'(1 . 1) {
                            \set stemLeftBeamCount = 1
                            \set stemRightBeamCount = 2
                            a'16
                            \revert Staff.Stem.stemlet-length
                            r8
                            ]
                        }
                    }
                }
            >>

    """
    return rmakers.BeamSpecifier(
        beam_divisions_together=True, beam_rests=True, stemlet_length=stemlets
    )


def beam_runs() -> rmakers.BeamSpecifier:
    r"""
    Beams PLT runs.

    ..  container:: example

        Beams PLT runs:

        >>> music_maker = baca.MusicMaker()
        >>> contribution = music_maker(
        ...     'Voice_1',
        ...     [[0, 2, 10], [18, 16, 15, 20, 19], [9]],
        ...     baca.beam_runs(),
        ...     baca.rests_around([2], [2]),
        ...     baca.tuplet_bracket_staff_padding(5),
        ...     counts=[1, 1, 5, -1],
        ...     time_treatments=[-1],
        ...     )
        >>> lilypond_file = music_maker.show(contribution)
        >>> abjad.show(lilypond_file, strict=89) # doctest: +SKIP

        ..  docs::

            >>> abjad.f(lilypond_file[abjad.Staff], strict=89)
            \new Staff
            <<
                \context Voice = "Voice_1"
                {
                    \voiceOne
                    {
                        \tweak text #tuplet-number::calc-fraction-text
                        \times 9/10 {
                            \override TupletBracket.staff-padding = #5                               %! baca.tuplet_bracket_staff_padding:OverrideCommand(1)
                            r8
                            \set stemLeftBeamCount = 0
                            \set stemRightBeamCount = 2
                            c'16
                            [
                            \set stemLeftBeamCount = 2
                            \set stemRightBeamCount = 0
                            d'16
                            ]
                            bf'4
                            ~
                            \set stemLeftBeamCount = 2
                            \set stemRightBeamCount = 2
                            bf'16
                            r16
                        }
                        \tweak text #tuplet-number::calc-fraction-text
                        \times 9/10 {
                            \set stemLeftBeamCount = 1
                            \set stemRightBeamCount = 2
                            fs''16
                            [
                            \set stemLeftBeamCount = 2
                            \set stemRightBeamCount = 0
                            e''16
                            ]
                            ef''4
                            ~
                            \set stemLeftBeamCount = 2
                            \set stemRightBeamCount = 2
                            ef''16
                            r16
                            \set stemLeftBeamCount = 0
                            \set stemRightBeamCount = 2
                            af''16
                            [
                            \set stemLeftBeamCount = 2
                            \set stemRightBeamCount = 1
                            g''16
                        }
                        \times 2/3 {
                            \set stemLeftBeamCount = 1
                            \set stemRightBeamCount = 2
                            a'16
                            ]
                            r8
                            \revert TupletBracket.staff-padding                                      %! baca.tuplet_bracket_staff_padding:OverrideCommand(2)
                        }
                    }
                }
            >>

    """
    return rmakers.BeamSpecifier(
        beam_divisions_together=True, beam_rests=False
    )


def do_not_beam() -> rmakers.BeamSpecifier:
    r"""
    Does not beam music.

    ..  container:: example

        Does not beam music:

        >>> music_maker = baca.MusicMaker()
        >>> contribution = music_maker(
        ...     'Voice_1',
        ...     [[0, 2, 10], [18, 16, 15, 20, 19], [9]],
        ...     baca.do_not_beam(),
        ...     baca.rests_around([2], [4]),
        ...     baca.tuplet_bracket_staff_padding(5),
        ...     counts=[1, 1, 5, -1],
        ...     time_treatments=[-1],
        ...     )
        >>> lilypond_file = music_maker.show(contribution)
        >>> abjad.show(lilypond_file, strict=89) # doctest: +SKIP

        ..  docs::

            >>> abjad.f(lilypond_file[abjad.Staff], strict=89)
            \new Staff
            <<
                \context Voice = "Voice_1"
                {
                    \voiceOne
                    {
                        \tweak text #tuplet-number::calc-fraction-text
                        \times 9/10 {
                            \override TupletBracket.staff-padding = #5                               %! baca.tuplet_bracket_staff_padding:OverrideCommand(1)
                            r8
                            c'16
                            d'16
                            bf'4
                            ~
                            bf'16
                            r16
                        }
                        \tweak text #tuplet-number::calc-fraction-text
                        \times 9/10 {
                            fs''16
                            e''16
                            ef''4
                            ~
                            ef''16
                            r16
                            af''16
                            g''16
                        }
                        \times 4/5 {
                            a'16
                            r4
                            \revert TupletBracket.staff-padding                                      %! baca.tuplet_bracket_staff_padding:OverrideCommand(2)
                        }
                    }
                }
            >>

    """
    return rmakers.BeamSpecifier(beam_divisions_together=False)


def make_even_divisions(
    *,
    measures: typings.SliceTyping = None,
    tag: str = "baca.make_even_divisions",
) -> RhythmCommand:
    """
    Makes even divisions.
    """
    return RhythmCommand(
        measures=measures,
        rhythm_maker=rmakers.EvenDivisionRhythmMaker(
            rmakers.BeamSpecifier(selector=classes._select().tuplets()),
            rmakers.TupletSpecifier(extract_trivial=True),
            tag=tag,
        ),
    )


def make_fused_tuplet_monads(
    *,
    measures: typings.SliceTyping = None,
    tag: str = "baca.make_fused_tuplet_monads",
    tuplet_ratio: typing.Tuple[int] = None,
) -> RhythmCommand:
    """
    Makes fused tuplet monads.
    """
    tuplet_ratios = []
    if tuplet_ratio is None:
        tuplet_ratios.append((1,))
    else:
        tuplet_ratios.append(tuplet_ratio)
    return RhythmCommand(
        divisions=abjad.sequence().sum().sequence(),
        measures=measures,
        rhythm_maker=rmakers.TupletRhythmMaker(
            rmakers.BeamSpecifier(selector=classes._select().tuplets()),
            rmakers.TupletSpecifier(
                extract_trivial=True, rewrite_rest_filled=True, trivialize=True
            ),
            rmakers.TieSpecifier(repeat_ties=True),
            tag=tag,
            tuplet_ratios=tuplet_ratios,
        ),
    )


def make_monads(fractions: str,) -> RhythmCommand:
    r"""
    Makes monads.

    ..  container:: example

        >>> maker = baca.SegmentMaker(
        ...     score_template=baca.SingleStaffScoreTemplate(),
        ...     spacing=baca.minimum_duration((1, 12)),
        ...     time_signatures=[(4, 4)],
        ...     )

        >>> maker(
        ...     'Music_Voice',
        ...     baca.make_monads('2/5 2/5 1/5'),
        ...     )

        >>> lilypond_file = maker.run(environment='docs')
        >>> abjad.show(lilypond_file, strict=89) # doctest: +SKIP

        ..  docs::

            >>> abjad.f(lilypond_file[abjad.Score], strict=89)
            <BLANKLINE>
            \context Score = "Score"                                                                 %! baca.SingleStaffScoreTemplate.__call__
            <<                                                                                       %! baca.SingleStaffScoreTemplate.__call__
            <BLANKLINE>
                \context GlobalContext = "Global_Context"                                            %! abjad.ScoreTemplate._make_global_context
                <<                                                                                   %! abjad.ScoreTemplate._make_global_context
            <BLANKLINE>
                    \context GlobalSkips = "Global_Skips"                                            %! abjad.ScoreTemplate._make_global_context
                    {                                                                                %! abjad.ScoreTemplate._make_global_context
            <BLANKLINE>
                        % [Global_Skips measure 1]                                                   %! _comment_measure_numbers
                        \baca-new-spacing-section #1 #12                                             %! HorizontalSpacingSpecifier(1):SPACING_COMMAND
                        \time 4/4                                                                    %! EXPLICIT_TIME_SIGNATURE:_set_status_tag:_make_global_skips(2)
                        \baca-time-signature-color #'blue                                            %! EXPLICIT_TIME_SIGNATURE_COLOR:_attach_color_literal(2)
                        s1 * 1                                                                       %! _make_global_skips(1)
                        \baca-bar-line-visible                                                       %! _attach_final_bar_line
                        \bar "|"                                                                     %! _attach_final_bar_line
            <BLANKLINE>
                        % [Global_Skips measure 2]                                                   %! PHANTOM:_style_phantom_measures(1):_comment_measure_numbers
                        \baca-new-spacing-section #1 #4                                              %! PHANTOM:_style_phantom_measures(1):HorizontalSpacingSpecifier(1):SPACING_COMMAND
                        \time 1/4                                                                    %! PHANTOM:_style_phantom_measures(1):EXPLICIT_TIME_SIGNATURE:_set_status_tag:_make_global_skips(3)
                        \baca-time-signature-transparent                                             %! PHANTOM:_style_phantom_measures(2)
                        s1 * 1/4                                                                     %! PHANTOM:_make_global_skips(3)
                        \once \override Score.BarLine.transparent = ##t                              %! PHANTOM:_style_phantom_measures(3)
                        \once \override Score.SpanBar.transparent = ##t                              %! PHANTOM:_style_phantom_measures(3)
            <BLANKLINE>
                    }                                                                                %! abjad.ScoreTemplate._make_global_context
            <BLANKLINE>
                >>                                                                                   %! abjad.ScoreTemplate._make_global_context
            <BLANKLINE>
                \context MusicContext = "Music_Context"                                              %! baca.SingleStaffScoreTemplate.__call__
                <<                                                                                   %! baca.SingleStaffScoreTemplate.__call__
            <BLANKLINE>
                    \context Staff = "Music_Staff"                                                   %! baca.SingleStaffScoreTemplate.__call__
                    {                                                                                %! baca.SingleStaffScoreTemplate.__call__
            <BLANKLINE>
                        \context Voice = "Music_Voice"                                               %! baca.SingleStaffScoreTemplate.__call__
                        {                                                                            %! baca.SingleStaffScoreTemplate.__call__
            <BLANKLINE>
                            \tweak edge-height #'(0.7 . 0)
                            \times 4/5 {
            <BLANKLINE>
                                % [Music_Voice measure 1]                                            %! _comment_measure_numbers
                                \baca-unpitched-music-warning                                        %! _color_unpitched_notes
                                c'2
            <BLANKLINE>
                            }
            <BLANKLINE>
                            \tweak edge-height #'(0.7 . 0)
                            \times 4/5 {
            <BLANKLINE>
                                \baca-unpitched-music-warning                                        %! _color_unpitched_notes
                                c'2
            <BLANKLINE>
                            }
            <BLANKLINE>
                            \tweak edge-height #'(0.7 . 0)
                            \times 4/5 {
            <BLANKLINE>
                                \baca-unpitched-music-warning                                        %! _color_unpitched_notes
                                c'4
            <BLANKLINE>
                            }
            <BLANKLINE>
                            <<                                                                       %! PHANTOM:_make_multimeasure_rest_container
            <BLANKLINE>
                                \context Voice = "Music_Voice"                                       %! PHANTOM:_make_multimeasure_rest_container
                                {                                                                    %! PHANTOM:_make_multimeasure_rest_container
            <BLANKLINE>
                                    % [Music_Voice measure 2]                                        %! PHANTOM:_style_phantom_measures(5):_comment_measure_numbers
                                    \baca-invisible-music                                            %! PHANTOM:_style_phantom_measures(5):_make_multimeasure_rest_container
                                    c'1 * 1/4                                                        %! PHANTOM:_make_multimeasure_rest_container
            <BLANKLINE>
                                }                                                                    %! PHANTOM:_make_multimeasure_rest_container
            <BLANKLINE>
                                \context Voice = "Rest_Voice"                                        %! PHANTOM:_make_multimeasure_rest_container
                                {                                                                    %! PHANTOM:_make_multimeasure_rest_container
            <BLANKLINE>
                                    % [Rest_Voice measure 2]                                         %! PHANTOM:_style_phantom_measures(5):_comment_measure_numbers
                                    \once \override Score.TimeSignature.X-extent = ##f               %! PHANTOM:_style_phantom_measures(6)
                                    \once \override MultiMeasureRest.transparent = ##t               %! PHANTOM:_style_phantom_measures(7)
                                    \stopStaff                                                       %! PHANTOM:_style_phantom_measures(8)
                                    \once \override Staff.StaffSymbol.transparent = ##t              %! PHANTOM:_style_phantom_measures(8)
                                    \startStaff                                                      %! PHANTOM:_style_phantom_measures(8)
                                    R1 * 1/4                                                         %! PHANTOM:_make_multimeasure_rest_container
            <BLANKLINE>
                                }                                                                    %! PHANTOM:_make_multimeasure_rest_container
            <BLANKLINE>
                            >>                                                                       %! PHANTOM:_make_multimeasure_rest_container
            <BLANKLINE>
                        }                                                                            %! baca.SingleStaffScoreTemplate.__call__
            <BLANKLINE>
                    }                                                                                %! baca.SingleStaffScoreTemplate.__call__
            <BLANKLINE>
                >>                                                                                   %! baca.SingleStaffScoreTemplate.__call__
            <BLANKLINE>
            >>                                                                                       %! baca.SingleStaffScoreTemplate.__call__

    """
    components: typing.List[abjad.Component] = []
    maker = abjad.LeafMaker()
    pitch = 0
    for fraction in fractions.split():
        leaves = maker([pitch], [fraction])
        components.extend(leaves)
    rhythm_maker = abjad.select(components)
    return RhythmCommand(
        annotate_unpitched_music=True, rhythm_maker=rhythm_maker
    )


def make_multimeasure_rests(
    *,
    measures: typings.SliceTyping = None,
    tag: str = "baca.make_multimeasure_rests",
) -> RhythmCommand:
    """
    Makes multimeasure rests.
    """
    return RhythmCommand(
        measures=measures,
        rhythm_maker=SkipRhythmMaker(tag=tag, use_multimeasure_rests=True),
    )


def make_notes(
    *specifiers,
    measures: typings.SliceTyping = None,
    repeat_ties: bool = False,
    tag: str = "baca.make_notes",
) -> RhythmCommand:
    """
    Makes notes; rewrites meter.
    """
    if repeat_ties:
        repeat_tie_specifier = [rmakers.TieSpecifier(repeat_ties=True)]
    else:
        repeat_tie_specifier = []
    return RhythmCommand(
        measures=measures,
        rhythm_maker=rmakers.NoteRhythmMaker(
            *specifiers,
            rmakers.BeamSpecifier(selector=classes._select().plts()),
            rmakers.RewriteMeterCommand(),
            *repeat_tie_specifier,
            tag=tag,
        ),
    )


def make_repeat_tied_notes(
    *specifiers: rmakers.SpecifierTyping,
    do_not_rewrite_meter: bool = None,
    measures: typings.SliceTyping = None,
    tag: str = "baca.make_repeat_tied_notes",
) -> RhythmCommand:
    r"""
    Makes repeat-tied notes; rewrites meter.

    ..  container:: example

        REGRESSION. All notes below are tagged unpitched (and colored
        gold), even tied notes resulting from meter rewriting:

        >>> maker = baca.SegmentMaker(
        ...     score_template=baca.SingleStaffScoreTemplate(),
        ...     spacing=baca.minimum_duration((1, 12)),
        ...     time_signatures=[(10, 8)],
        ...     )

        >>> maker(
        ...     'Music_Voice',
        ...     baca.make_repeat_tied_notes(),
        ...     )

        >>> lilypond_file = maker.run(environment='docs')
        >>> abjad.show(lilypond_file, strict=89) # doctest: +SKIP

        ..  docs::

            >>> abjad.f(lilypond_file[abjad.Score], strict=89)
            <BLANKLINE>
            \context Score = "Score"                                                                 %! baca.SingleStaffScoreTemplate.__call__
            <<                                                                                       %! baca.SingleStaffScoreTemplate.__call__
            <BLANKLINE>
                \context GlobalContext = "Global_Context"                                            %! abjad.ScoreTemplate._make_global_context
                <<                                                                                   %! abjad.ScoreTemplate._make_global_context
            <BLANKLINE>
                    \context GlobalSkips = "Global_Skips"                                            %! abjad.ScoreTemplate._make_global_context
                    {                                                                                %! abjad.ScoreTemplate._make_global_context
            <BLANKLINE>
                        % [Global_Skips measure 1]                                                   %! _comment_measure_numbers
                        \baca-new-spacing-section #1 #12                                             %! HorizontalSpacingSpecifier(1):SPACING_COMMAND
                        \time 10/8                                                                   %! EXPLICIT_TIME_SIGNATURE:_set_status_tag:_make_global_skips(2)
                        \baca-time-signature-color #'blue                                            %! EXPLICIT_TIME_SIGNATURE_COLOR:_attach_color_literal(2)
                        s1 * 5/4                                                                     %! _make_global_skips(1)
                        \baca-bar-line-visible                                                       %! _attach_final_bar_line
                        \bar "|"                                                                     %! _attach_final_bar_line
            <BLANKLINE>
                        % [Global_Skips measure 2]                                                   %! PHANTOM:_style_phantom_measures(1):_comment_measure_numbers
                        \baca-new-spacing-section #1 #4                                              %! PHANTOM:_style_phantom_measures(1):HorizontalSpacingSpecifier(1):SPACING_COMMAND
                        \time 1/4                                                                    %! PHANTOM:_style_phantom_measures(1):EXPLICIT_TIME_SIGNATURE:_set_status_tag:_make_global_skips(3)
                        \baca-time-signature-transparent                                             %! PHANTOM:_style_phantom_measures(2)
                        s1 * 1/4                                                                     %! PHANTOM:_make_global_skips(3)
                        \once \override Score.BarLine.transparent = ##t                              %! PHANTOM:_style_phantom_measures(3)
                        \once \override Score.SpanBar.transparent = ##t                              %! PHANTOM:_style_phantom_measures(3)
            <BLANKLINE>
                    }                                                                                %! abjad.ScoreTemplate._make_global_context
            <BLANKLINE>
                >>                                                                                   %! abjad.ScoreTemplate._make_global_context
            <BLANKLINE>
                \context MusicContext = "Music_Context"                                              %! baca.SingleStaffScoreTemplate.__call__
                <<                                                                                   %! baca.SingleStaffScoreTemplate.__call__
            <BLANKLINE>
                    \context Staff = "Music_Staff"                                                   %! baca.SingleStaffScoreTemplate.__call__
                    {                                                                                %! baca.SingleStaffScoreTemplate.__call__
            <BLANKLINE>
                        \context Voice = "Music_Voice"                                               %! baca.SingleStaffScoreTemplate.__call__
                        {                                                                            %! baca.SingleStaffScoreTemplate.__call__
            <BLANKLINE>
                            % [Music_Voice measure 1]                                                %! _comment_measure_numbers
                            \baca-unpitched-music-warning                                            %! _color_unpitched_notes
                            c'4.
            <BLANKLINE>
                            \baca-unpitched-music-warning                                            %! _color_unpitched_notes
                            c'4
                            \repeatTie
            <BLANKLINE>
                            \baca-unpitched-music-warning                                            %! _color_unpitched_notes
                            c'4.
                            \repeatTie
            <BLANKLINE>
                            \baca-unpitched-music-warning                                            %! _color_unpitched_notes
                            c'4                                                                      %! baca.make_repeat_tied_notes
                            \repeatTie
            <BLANKLINE>
                            <<                                                                       %! PHANTOM:_make_multimeasure_rest_container
            <BLANKLINE>
                                \context Voice = "Music_Voice"                                       %! PHANTOM:_make_multimeasure_rest_container
                                {                                                                    %! PHANTOM:_make_multimeasure_rest_container
            <BLANKLINE>
                                    % [Music_Voice measure 2]                                        %! PHANTOM:_style_phantom_measures(5):_comment_measure_numbers
                                    \baca-invisible-music                                            %! PHANTOM:_style_phantom_measures(5):_make_multimeasure_rest_container
                                    c'1 * 1/4                                                        %! PHANTOM:_make_multimeasure_rest_container
            <BLANKLINE>
                                }                                                                    %! PHANTOM:_make_multimeasure_rest_container
            <BLANKLINE>
                                \context Voice = "Rest_Voice"                                        %! PHANTOM:_make_multimeasure_rest_container
                                {                                                                    %! PHANTOM:_make_multimeasure_rest_container
            <BLANKLINE>
                                    % [Rest_Voice measure 2]                                         %! PHANTOM:_style_phantom_measures(5):_comment_measure_numbers
                                    \once \override Score.TimeSignature.X-extent = ##f               %! PHANTOM:_style_phantom_measures(6)
                                    \once \override MultiMeasureRest.transparent = ##t               %! PHANTOM:_style_phantom_measures(7)
                                    \stopStaff                                                       %! PHANTOM:_style_phantom_measures(8)
                                    \once \override Staff.StaffSymbol.transparent = ##t              %! PHANTOM:_style_phantom_measures(8)
                                    \startStaff                                                      %! PHANTOM:_style_phantom_measures(8)
                                    R1 * 1/4                                                         %! PHANTOM:_make_multimeasure_rest_container
            <BLANKLINE>
                                }                                                                    %! PHANTOM:_make_multimeasure_rest_container
            <BLANKLINE>
                            >>                                                                       %! PHANTOM:_make_multimeasure_rest_container
            <BLANKLINE>
                        }                                                                            %! baca.SingleStaffScoreTemplate.__call__
            <BLANKLINE>
                    }                                                                                %! baca.SingleStaffScoreTemplate.__call__
            <BLANKLINE>
                >>                                                                                   %! baca.SingleStaffScoreTemplate.__call__
            <BLANKLINE>
            >>                                                                                       %! baca.SingleStaffScoreTemplate.__call__

    """
    specifier: rmakers.SpecifierTyping
    specifiers_ = list(specifiers)
    specifier = rmakers.BeamSpecifier(selector=classes._select().plts())
    specifiers_.append(specifier)
    specifier = rmakers.TieSpecifier(
        attach_repeat_ties=True, selector=classes._select().pheads()[1:]
    )
    specifiers_.append(specifier)
    if not do_not_rewrite_meter:
        specifier = rmakers.RewriteMeterCommand()
        specifiers_.append(specifier)
    specifier = rmakers.TieSpecifier(repeat_ties=True)
    specifiers_.append(specifier)
    return RhythmCommand(
        measures=measures,
        rhythm_maker=rmakers.NoteRhythmMaker(*specifiers_, tag=tag),
    )


def make_repeated_duration_notes(
    durations: typing.Sequence[abjad.DurationTyping],
    *specifiers: rmakers.SpecifierTyping,
    do_not_rewrite_meter: bool = None,
    measures: typings.SliceTyping = None,
    tag: str = "baca.make_repeated_duration_notes",
) -> RhythmCommand:
    """
    Makes repeated-duration notes; rewrites meter.
    """
    if isinstance(durations, abjad.Duration):
        durations = [durations]
    elif isinstance(durations, tuple):
        assert len(durations) == 2
        durations = [abjad.Duration(durations)]
    divisions = divisionclasses._divisions().fuse()
    divisions = divisions.split(durations, cyclic=True)
    rewrite_specifiers: typing.List[rmakers.SpecifierTyping] = []
    if not do_not_rewrite_meter:
        rewrite_specifiers.append(rmakers.RewriteMeterCommand())
    return RhythmCommand(
        measures=measures,
        rhythm_maker=rmakers.NoteRhythmMaker(
            *specifiers,
            *rewrite_specifiers,
            rmakers.TieSpecifier(repeat_ties=True),
            divisions=divisions,
            tag=tag,
        ),
    )


def make_rests(
    *, measures: typings.SliceTyping = None, tag: str = "baca.make_rests"
) -> RhythmCommand:
    """
    Makes rests.
    """
    return RhythmCommand(
        measures=measures,
        rhythm_maker=rmakers.NoteRhythmMaker(
            rmakers.SilenceMask(selector=classes._select().lts()), tag=tag
        ),
    )


def make_single_attack(
    duration,
    *,
    measures: typings.SliceTyping = None,
    tag: str = "baca.make_single_attack",
) -> RhythmCommand:
    """
    Makes single attacks with ``duration``.
    """
    duration = abjad.Duration(duration)
    numerator, denominator = duration.pair
    rhythm_maker = rmakers.IncisedRhythmMaker(
        rmakers.BeamSpecifier(selector=classes._select().tuplets()),
        rmakers.TupletSpecifier(extract_trivial=True),
        incise_specifier=rmakers.InciseSpecifier(
            fill_with_rests=True,
            outer_divisions_only=True,
            prefix_talea=[numerator],
            prefix_counts=[1],
            talea_denominator=denominator,
        ),
        tag=tag,
    )
    return RhythmCommand(measures=measures, rhythm_maker=rhythm_maker)


def make_skips(
    *, measures: typings.SliceTyping = None, tag: str = "baca.make_skips"
) -> RhythmCommand:
    """
    Makes skips.
    """
    return RhythmCommand(measures=measures, rhythm_maker=SkipRhythmMaker())


def make_tied_notes(
    *, measures: typings.SliceTyping = None, tag: str = "baca.make_tied_notes"
) -> RhythmCommand:
    """
    Makes tied notes; rewrites meter.
    """
    return RhythmCommand(
        measures=measures,
        rhythm_maker=rmakers.NoteRhythmMaker(
            rmakers.BeamSpecifier(selector=classes._select().plts()),
            rmakers.TieSpecifier(
                attach_ties=True, selector=classes._select().ptails()[:-1]
            ),
            rmakers.RewriteMeterCommand(),
            tag=tag,
        ),
    )


def make_tied_repeated_durations(
    durations: typing.Sequence[abjad.DurationTyping],
    *,
    measures: typings.SliceTyping = None,
    tag: str = "baca.make_tied_repeated_durations",
) -> RhythmCommand:
    """
    Makes tied repeated durations; does not rewrite meter.
    """
    specifiers = []
    if isinstance(durations, abjad.Duration):
        durations = [durations]
    elif isinstance(durations, tuple):
        assert len(durations) == 2
        durations = [abjad.Duration(durations)]
    tie_specifier = rmakers.TieSpecifier(
        attach_repeat_ties=True, selector=classes._select().pheads()[1:]
    )
    specifiers.append(tie_specifier)
    tie_specifier = rmakers.TieSpecifier(repeat_ties=True)
    specifiers.append(tie_specifier)
    divisions = divisionclasses._divisions().fuse()
    divisions = divisions.split(durations, cyclic=True)
    return RhythmCommand(
        divisions=divisions,
        measures=measures,
        rhythm_maker=rmakers.NoteRhythmMaker(*specifiers, tag=tag),
    )


def repeat_tie_from(
    *,
    allow_rest: bool = None,
    selector: abjad.SelectorTyping = "baca.pleaf(-1)",
) -> TieCorrectionCommand:
    r"""
    Repeat-ties from leaf.

    ..  container:: example

        >>> maker = baca.SegmentMaker(
        ...     do_not_color_unpitched_music=True,
        ...     score_template=baca.SingleStaffScoreTemplate(),
        ...     spacing=baca.minimum_duration((1, 12)),
        ...     time_signatures=[(4, 8), (3, 8), (4, 8), (3, 8)],
        ...     )

        >>> maker(
        ...     'Music_Voice',
        ...     baca.make_notes(),
        ...     baca.repeat_tie_from(selector=baca.leaf(1)),
        ...     )

        >>> lilypond_file = maker.run(environment='docs')
        >>> abjad.show(lilypond_file, strict=89) # doctest: +SKIP

        ..  docs::

            >>> abjad.f(lilypond_file[abjad.Score], strict=89)
            <BLANKLINE>
            \context Score = "Score"                                                                 %! baca.SingleStaffScoreTemplate.__call__
            <<                                                                                       %! baca.SingleStaffScoreTemplate.__call__
            <BLANKLINE>
                \context GlobalContext = "Global_Context"                                            %! abjad.ScoreTemplate._make_global_context
                <<                                                                                   %! abjad.ScoreTemplate._make_global_context
            <BLANKLINE>
                    \context GlobalSkips = "Global_Skips"                                            %! abjad.ScoreTemplate._make_global_context
                    {                                                                                %! abjad.ScoreTemplate._make_global_context
            <BLANKLINE>
                        % [Global_Skips measure 1]                                                   %! _comment_measure_numbers
                        \baca-new-spacing-section #1 #12                                             %! HorizontalSpacingSpecifier(1):SPACING_COMMAND
                        \time 4/8                                                                    %! EXPLICIT_TIME_SIGNATURE:_set_status_tag:_make_global_skips(2)
                        \baca-time-signature-color #'blue                                            %! EXPLICIT_TIME_SIGNATURE_COLOR:_attach_color_literal(2)
                        s1 * 1/2                                                                     %! _make_global_skips(1)
            <BLANKLINE>
                        % [Global_Skips measure 2]                                                   %! _comment_measure_numbers
                        \baca-new-spacing-section #1 #12                                             %! HorizontalSpacingSpecifier(1):SPACING_COMMAND
                        \time 3/8                                                                    %! EXPLICIT_TIME_SIGNATURE:_set_status_tag:_make_global_skips(2)
                        \baca-time-signature-color #'blue                                            %! EXPLICIT_TIME_SIGNATURE_COLOR:_attach_color_literal(2)
                        s1 * 3/8                                                                     %! _make_global_skips(1)
            <BLANKLINE>
                        % [Global_Skips measure 3]                                                   %! _comment_measure_numbers
                        \baca-new-spacing-section #1 #12                                             %! HorizontalSpacingSpecifier(1):SPACING_COMMAND
                        \time 4/8                                                                    %! EXPLICIT_TIME_SIGNATURE:_set_status_tag:_make_global_skips(2)
                        \baca-time-signature-color #'blue                                            %! EXPLICIT_TIME_SIGNATURE_COLOR:_attach_color_literal(2)
                        s1 * 1/2                                                                     %! _make_global_skips(1)
            <BLANKLINE>
                        % [Global_Skips measure 4]                                                   %! _comment_measure_numbers
                        \baca-new-spacing-section #1 #12                                             %! HorizontalSpacingSpecifier(1):SPACING_COMMAND
                        \time 3/8                                                                    %! EXPLICIT_TIME_SIGNATURE:_set_status_tag:_make_global_skips(2)
                        \baca-time-signature-color #'blue                                            %! EXPLICIT_TIME_SIGNATURE_COLOR:_attach_color_literal(2)
                        s1 * 3/8                                                                     %! _make_global_skips(1)
                        \baca-bar-line-visible                                                       %! _attach_final_bar_line
                        \bar "|"                                                                     %! _attach_final_bar_line
            <BLANKLINE>
                        % [Global_Skips measure 5]                                                   %! PHANTOM:_style_phantom_measures(1):_comment_measure_numbers
                        \baca-new-spacing-section #1 #4                                              %! PHANTOM:_style_phantom_measures(1):HorizontalSpacingSpecifier(1):SPACING_COMMAND
                        \time 1/4                                                                    %! PHANTOM:_style_phantom_measures(1):EXPLICIT_TIME_SIGNATURE:_set_status_tag:_make_global_skips(3)
                        \baca-time-signature-transparent                                             %! PHANTOM:_style_phantom_measures(2)
                        s1 * 1/4                                                                     %! PHANTOM:_make_global_skips(3)
                        \once \override Score.BarLine.transparent = ##t                              %! PHANTOM:_style_phantom_measures(3)
                        \once \override Score.SpanBar.transparent = ##t                              %! PHANTOM:_style_phantom_measures(3)
            <BLANKLINE>
                    }                                                                                %! abjad.ScoreTemplate._make_global_context
            <BLANKLINE>
                >>                                                                                   %! abjad.ScoreTemplate._make_global_context
            <BLANKLINE>
                \context MusicContext = "Music_Context"                                              %! baca.SingleStaffScoreTemplate.__call__
                <<                                                                                   %! baca.SingleStaffScoreTemplate.__call__
            <BLANKLINE>
                    \context Staff = "Music_Staff"                                                   %! baca.SingleStaffScoreTemplate.__call__
                    {                                                                                %! baca.SingleStaffScoreTemplate.__call__
            <BLANKLINE>
                        \context Voice = "Music_Voice"                                               %! baca.SingleStaffScoreTemplate.__call__
                        {                                                                            %! baca.SingleStaffScoreTemplate.__call__
            <BLANKLINE>
                            % [Music_Voice measure 1]                                                %! _comment_measure_numbers
                            c'2                                                                      %! baca.make_notes
            <BLANKLINE>
                            % [Music_Voice measure 2]                                                %! _comment_measure_numbers
                            c'4.                                                                     %! baca.make_notes
            <BLANKLINE>
                            % [Music_Voice measure 3]                                                %! _comment_measure_numbers
                            c'2                                                                      %! baca.make_notes
                            \repeatTie                                                               %! TieCorrectionCommand
            <BLANKLINE>
                            % [Music_Voice measure 4]                                                %! _comment_measure_numbers
                            c'4.                                                                     %! baca.make_notes
            <BLANKLINE>
                            <<                                                                       %! PHANTOM:_make_multimeasure_rest_container
            <BLANKLINE>
                                \context Voice = "Music_Voice"                                       %! PHANTOM:_make_multimeasure_rest_container
                                {                                                                    %! PHANTOM:_make_multimeasure_rest_container
            <BLANKLINE>
                                    % [Music_Voice measure 5]                                        %! PHANTOM:_style_phantom_measures(5):_comment_measure_numbers
                                    \baca-invisible-music                                            %! PHANTOM:_style_phantom_measures(5):_make_multimeasure_rest_container
                                    c'1 * 1/4                                                        %! PHANTOM:_make_multimeasure_rest_container
            <BLANKLINE>
                                }                                                                    %! PHANTOM:_make_multimeasure_rest_container
            <BLANKLINE>
                                \context Voice = "Rest_Voice"                                        %! PHANTOM:_make_multimeasure_rest_container
                                {                                                                    %! PHANTOM:_make_multimeasure_rest_container
            <BLANKLINE>
                                    % [Rest_Voice measure 5]                                         %! PHANTOM:_style_phantom_measures(5):_comment_measure_numbers
                                    \once \override Score.TimeSignature.X-extent = ##f               %! PHANTOM:_style_phantom_measures(6)
                                    \once \override MultiMeasureRest.transparent = ##t               %! PHANTOM:_style_phantom_measures(7)
                                    \stopStaff                                                       %! PHANTOM:_style_phantom_measures(8)
                                    \once \override Staff.StaffSymbol.transparent = ##t              %! PHANTOM:_style_phantom_measures(8)
                                    \startStaff                                                      %! PHANTOM:_style_phantom_measures(8)
                                    R1 * 1/4                                                         %! PHANTOM:_make_multimeasure_rest_container
            <BLANKLINE>
                                }                                                                    %! PHANTOM:_make_multimeasure_rest_container
            <BLANKLINE>
                            >>                                                                       %! PHANTOM:_make_multimeasure_rest_container
            <BLANKLINE>
                        }                                                                            %! baca.SingleStaffScoreTemplate.__call__
            <BLANKLINE>
                    }                                                                                %! baca.SingleStaffScoreTemplate.__call__
            <BLANKLINE>
                >>                                                                                   %! baca.SingleStaffScoreTemplate.__call__
            <BLANKLINE>
            >>                                                                                       %! baca.SingleStaffScoreTemplate.__call__

    """
    return TieCorrectionCommand(
        allow_rest=allow_rest, repeat=True, selector=selector
    )


def repeat_tie_to(
    *,
    allow_rest: bool = None,
    selector: abjad.SelectorTyping = "baca.pleaf(0)",
) -> TieCorrectionCommand:
    r"""
    Repeat-ties to leaf.

    ..  container:: example

        >>> maker = baca.SegmentMaker(
        ...     do_not_color_unpitched_music=True,
        ...     score_template=baca.SingleStaffScoreTemplate(),
        ...     spacing=baca.minimum_duration((1, 12)),
        ...     time_signatures=[(4, 8), (3, 8), (4, 8), (3, 8)],
        ...     )

        >>> maker(
        ...     'Music_Voice',
        ...     baca.make_notes(),
        ...     baca.repeat_tie_to(selector=baca.leaf(2)),
        ...     )

        >>> lilypond_file = maker.run(environment='docs')
        >>> abjad.show(lilypond_file, strict=89) # doctest: +SKIP

        ..  docs::

            >>> abjad.f(lilypond_file[abjad.Score], strict=89)
            <BLANKLINE>
            \context Score = "Score"                                                                 %! baca.SingleStaffScoreTemplate.__call__
            <<                                                                                       %! baca.SingleStaffScoreTemplate.__call__
            <BLANKLINE>
                \context GlobalContext = "Global_Context"                                            %! abjad.ScoreTemplate._make_global_context
                <<                                                                                   %! abjad.ScoreTemplate._make_global_context
            <BLANKLINE>
                    \context GlobalSkips = "Global_Skips"                                            %! abjad.ScoreTemplate._make_global_context
                    {                                                                                %! abjad.ScoreTemplate._make_global_context
            <BLANKLINE>
                        % [Global_Skips measure 1]                                                   %! _comment_measure_numbers
                        \baca-new-spacing-section #1 #12                                             %! HorizontalSpacingSpecifier(1):SPACING_COMMAND
                        \time 4/8                                                                    %! EXPLICIT_TIME_SIGNATURE:_set_status_tag:_make_global_skips(2)
                        \baca-time-signature-color #'blue                                            %! EXPLICIT_TIME_SIGNATURE_COLOR:_attach_color_literal(2)
                        s1 * 1/2                                                                     %! _make_global_skips(1)
            <BLANKLINE>
                        % [Global_Skips measure 2]                                                   %! _comment_measure_numbers
                        \baca-new-spacing-section #1 #12                                             %! HorizontalSpacingSpecifier(1):SPACING_COMMAND
                        \time 3/8                                                                    %! EXPLICIT_TIME_SIGNATURE:_set_status_tag:_make_global_skips(2)
                        \baca-time-signature-color #'blue                                            %! EXPLICIT_TIME_SIGNATURE_COLOR:_attach_color_literal(2)
                        s1 * 3/8                                                                     %! _make_global_skips(1)
            <BLANKLINE>
                        % [Global_Skips measure 3]                                                   %! _comment_measure_numbers
                        \baca-new-spacing-section #1 #12                                             %! HorizontalSpacingSpecifier(1):SPACING_COMMAND
                        \time 4/8                                                                    %! EXPLICIT_TIME_SIGNATURE:_set_status_tag:_make_global_skips(2)
                        \baca-time-signature-color #'blue                                            %! EXPLICIT_TIME_SIGNATURE_COLOR:_attach_color_literal(2)
                        s1 * 1/2                                                                     %! _make_global_skips(1)
            <BLANKLINE>
                        % [Global_Skips measure 4]                                                   %! _comment_measure_numbers
                        \baca-new-spacing-section #1 #12                                             %! HorizontalSpacingSpecifier(1):SPACING_COMMAND
                        \time 3/8                                                                    %! EXPLICIT_TIME_SIGNATURE:_set_status_tag:_make_global_skips(2)
                        \baca-time-signature-color #'blue                                            %! EXPLICIT_TIME_SIGNATURE_COLOR:_attach_color_literal(2)
                        s1 * 3/8                                                                     %! _make_global_skips(1)
                        \baca-bar-line-visible                                                       %! _attach_final_bar_line
                        \bar "|"                                                                     %! _attach_final_bar_line
            <BLANKLINE>
                        % [Global_Skips measure 5]                                                   %! PHANTOM:_style_phantom_measures(1):_comment_measure_numbers
                        \baca-new-spacing-section #1 #4                                              %! PHANTOM:_style_phantom_measures(1):HorizontalSpacingSpecifier(1):SPACING_COMMAND
                        \time 1/4                                                                    %! PHANTOM:_style_phantom_measures(1):EXPLICIT_TIME_SIGNATURE:_set_status_tag:_make_global_skips(3)
                        \baca-time-signature-transparent                                             %! PHANTOM:_style_phantom_measures(2)
                        s1 * 1/4                                                                     %! PHANTOM:_make_global_skips(3)
                        \once \override Score.BarLine.transparent = ##t                              %! PHANTOM:_style_phantom_measures(3)
                        \once \override Score.SpanBar.transparent = ##t                              %! PHANTOM:_style_phantom_measures(3)
            <BLANKLINE>
                    }                                                                                %! abjad.ScoreTemplate._make_global_context
            <BLANKLINE>
                >>                                                                                   %! abjad.ScoreTemplate._make_global_context
            <BLANKLINE>
                \context MusicContext = "Music_Context"                                              %! baca.SingleStaffScoreTemplate.__call__
                <<                                                                                   %! baca.SingleStaffScoreTemplate.__call__
            <BLANKLINE>
                    \context Staff = "Music_Staff"                                                   %! baca.SingleStaffScoreTemplate.__call__
                    {                                                                                %! baca.SingleStaffScoreTemplate.__call__
            <BLANKLINE>
                        \context Voice = "Music_Voice"                                               %! baca.SingleStaffScoreTemplate.__call__
                        {                                                                            %! baca.SingleStaffScoreTemplate.__call__
            <BLANKLINE>
                            % [Music_Voice measure 1]                                                %! _comment_measure_numbers
                            c'2                                                                      %! baca.make_notes
            <BLANKLINE>
                            % [Music_Voice measure 2]                                                %! _comment_measure_numbers
                            c'4.                                                                     %! baca.make_notes
            <BLANKLINE>
                            % [Music_Voice measure 3]                                                %! _comment_measure_numbers
                            c'2                                                                      %! baca.make_notes
                            \repeatTie                                                               %! TieCorrectionCommand
            <BLANKLINE>
                            % [Music_Voice measure 4]                                                %! _comment_measure_numbers
                            c'4.                                                                     %! baca.make_notes
            <BLANKLINE>
                            <<                                                                       %! PHANTOM:_make_multimeasure_rest_container
            <BLANKLINE>
                                \context Voice = "Music_Voice"                                       %! PHANTOM:_make_multimeasure_rest_container
                                {                                                                    %! PHANTOM:_make_multimeasure_rest_container
            <BLANKLINE>
                                    % [Music_Voice measure 5]                                        %! PHANTOM:_style_phantom_measures(5):_comment_measure_numbers
                                    \baca-invisible-music                                            %! PHANTOM:_style_phantom_measures(5):_make_multimeasure_rest_container
                                    c'1 * 1/4                                                        %! PHANTOM:_make_multimeasure_rest_container
            <BLANKLINE>
                                }                                                                    %! PHANTOM:_make_multimeasure_rest_container
            <BLANKLINE>
                                \context Voice = "Rest_Voice"                                        %! PHANTOM:_make_multimeasure_rest_container
                                {                                                                    %! PHANTOM:_make_multimeasure_rest_container
            <BLANKLINE>
                                    % [Rest_Voice measure 5]                                         %! PHANTOM:_style_phantom_measures(5):_comment_measure_numbers
                                    \once \override Score.TimeSignature.X-extent = ##f               %! PHANTOM:_style_phantom_measures(6)
                                    \once \override MultiMeasureRest.transparent = ##t               %! PHANTOM:_style_phantom_measures(7)
                                    \stopStaff                                                       %! PHANTOM:_style_phantom_measures(8)
                                    \once \override Staff.StaffSymbol.transparent = ##t              %! PHANTOM:_style_phantom_measures(8)
                                    \startStaff                                                      %! PHANTOM:_style_phantom_measures(8)
                                    R1 * 1/4                                                         %! PHANTOM:_make_multimeasure_rest_container
            <BLANKLINE>
                                }                                                                    %! PHANTOM:_make_multimeasure_rest_container
            <BLANKLINE>
                            >>                                                                       %! PHANTOM:_make_multimeasure_rest_container
            <BLANKLINE>
                        }                                                                            %! baca.SingleStaffScoreTemplate.__call__
            <BLANKLINE>
                    }                                                                                %! baca.SingleStaffScoreTemplate.__call__
            <BLANKLINE>
                >>                                                                                   %! baca.SingleStaffScoreTemplate.__call__
            <BLANKLINE>
            >>                                                                                       %! baca.SingleStaffScoreTemplate.__call__

    """
    return TieCorrectionCommand(
        allow_rest=allow_rest,
        direction=abjad.Left,
        repeat=True,
        selector=selector,
    )


def rhythm(
    rhythm_maker: RhythmMakerTyping,
    *,
    annotate_unpitched_music: bool = None,
    divisions: abjad.Expression = None,
    left_broken: bool = None,
    measures: typings.SliceTyping = None,
    persist: str = None,
    reference_meters: typing.Iterable[abjad.Meter] = None,
    right_broken: bool = None,
    tag: str = None,
) -> RhythmCommand:
    """
    Makes rhythm command.
    """
    # TODO: implement a way to tag parsed strings:
    if isinstance(rhythm_maker, str):
        string = f"{{ {rhythm_maker} }}"
        container = abjad.parse(string)
        selection = abjad.mutate(container).eject_contents()
        rhythm_maker = selection
    if tag is not None:
        # TODO: implement a way to tag already-initialized components:
        if not isinstance(rhythm_maker, rmakers.RhythmMaker):
            raise Exception("can only tag rhythm-makers.")
        rhythm_maker = abjad.new(rhythm_maker, tag=tag)
    return RhythmCommand(
        annotate_unpitched_music=annotate_unpitched_music,
        divisions=divisions,
        left_broken=left_broken,
        measures=measures,
        persist=persist,
        reference_meters=reference_meters,
        rhythm_maker=rhythm_maker,
        right_broken=right_broken,
    )


def set_duration_multiplier(
    *,
    selector: abjad.SelectorTyping = "baca.leaf(0)",
    written_duration: abjad.DurationTyping = None,
) -> DurationMultiplierCommand:
    r"""
    Sets duration multiplier.

    ..  container:: example

        Does nothing when ``written_duration`` is none:

        >>> maker = baca.SegmentMaker(
        ...     do_not_color_unpitched_music=True,
        ...     score_template=baca.SingleStaffScoreTemplate(),
        ...     spacing=baca.minimum_duration((1, 12)),
        ...     time_signatures=[(4, 8), (3, 8), (4, 8), (3, 8)],
        ...     )

        >>> maker(
        ...     'Music_Voice',
        ...     baca.make_repeated_duration_notes([(1, 8)]),
        ...     baca.set_duration_multiplier(
        ...         selector=baca.leaves(),
        ...         written_duration=None,
        ...         ),
        ...     )

        >>> lilypond_file = maker.run(environment='docs')
        >>> abjad.show(lilypond_file, strict=89) # doctest: +SKIP

        ..  docs::

            >>> abjad.f(lilypond_file[abjad.Score], strict=89)
            <BLANKLINE>
            \context Score = "Score"                                                                 %! baca.SingleStaffScoreTemplate.__call__
            <<                                                                                       %! baca.SingleStaffScoreTemplate.__call__
            <BLANKLINE>
                \context GlobalContext = "Global_Context"                                            %! abjad.ScoreTemplate._make_global_context
                <<                                                                                   %! abjad.ScoreTemplate._make_global_context
            <BLANKLINE>
                    \context GlobalSkips = "Global_Skips"                                            %! abjad.ScoreTemplate._make_global_context
                    {                                                                                %! abjad.ScoreTemplate._make_global_context
            <BLANKLINE>
                        % [Global_Skips measure 1]                                                   %! _comment_measure_numbers
                        \baca-new-spacing-section #1 #12                                             %! HorizontalSpacingSpecifier(1):SPACING_COMMAND
                        \time 4/8                                                                    %! EXPLICIT_TIME_SIGNATURE:_set_status_tag:_make_global_skips(2)
                        \baca-time-signature-color #'blue                                            %! EXPLICIT_TIME_SIGNATURE_COLOR:_attach_color_literal(2)
                        s1 * 1/2                                                                     %! _make_global_skips(1)
            <BLANKLINE>
                        % [Global_Skips measure 2]                                                   %! _comment_measure_numbers
                        \baca-new-spacing-section #1 #12                                             %! HorizontalSpacingSpecifier(1):SPACING_COMMAND
                        \time 3/8                                                                    %! EXPLICIT_TIME_SIGNATURE:_set_status_tag:_make_global_skips(2)
                        \baca-time-signature-color #'blue                                            %! EXPLICIT_TIME_SIGNATURE_COLOR:_attach_color_literal(2)
                        s1 * 3/8                                                                     %! _make_global_skips(1)
            <BLANKLINE>
                        % [Global_Skips measure 3]                                                   %! _comment_measure_numbers
                        \baca-new-spacing-section #1 #12                                             %! HorizontalSpacingSpecifier(1):SPACING_COMMAND
                        \time 4/8                                                                    %! EXPLICIT_TIME_SIGNATURE:_set_status_tag:_make_global_skips(2)
                        \baca-time-signature-color #'blue                                            %! EXPLICIT_TIME_SIGNATURE_COLOR:_attach_color_literal(2)
                        s1 * 1/2                                                                     %! _make_global_skips(1)
            <BLANKLINE>
                        % [Global_Skips measure 4]                                                   %! _comment_measure_numbers
                        \baca-new-spacing-section #1 #12                                             %! HorizontalSpacingSpecifier(1):SPACING_COMMAND
                        \time 3/8                                                                    %! EXPLICIT_TIME_SIGNATURE:_set_status_tag:_make_global_skips(2)
                        \baca-time-signature-color #'blue                                            %! EXPLICIT_TIME_SIGNATURE_COLOR:_attach_color_literal(2)
                        s1 * 3/8                                                                     %! _make_global_skips(1)
                        \baca-bar-line-visible                                                       %! _attach_final_bar_line
                        \bar "|"                                                                     %! _attach_final_bar_line
            <BLANKLINE>
                        % [Global_Skips measure 5]                                                   %! PHANTOM:_style_phantom_measures(1):_comment_measure_numbers
                        \baca-new-spacing-section #1 #4                                              %! PHANTOM:_style_phantom_measures(1):HorizontalSpacingSpecifier(1):SPACING_COMMAND
                        \time 1/4                                                                    %! PHANTOM:_style_phantom_measures(1):EXPLICIT_TIME_SIGNATURE:_set_status_tag:_make_global_skips(3)
                        \baca-time-signature-transparent                                             %! PHANTOM:_style_phantom_measures(2)
                        s1 * 1/4                                                                     %! PHANTOM:_make_global_skips(3)
                        \once \override Score.BarLine.transparent = ##t                              %! PHANTOM:_style_phantom_measures(3)
                        \once \override Score.SpanBar.transparent = ##t                              %! PHANTOM:_style_phantom_measures(3)
            <BLANKLINE>
                    }                                                                                %! abjad.ScoreTemplate._make_global_context
            <BLANKLINE>
                >>                                                                                   %! abjad.ScoreTemplate._make_global_context
            <BLANKLINE>
                \context MusicContext = "Music_Context"                                              %! baca.SingleStaffScoreTemplate.__call__
                <<                                                                                   %! baca.SingleStaffScoreTemplate.__call__
            <BLANKLINE>
                    \context Staff = "Music_Staff"                                                   %! baca.SingleStaffScoreTemplate.__call__
                    {                                                                                %! baca.SingleStaffScoreTemplate.__call__
            <BLANKLINE>
                        \context Voice = "Music_Voice"                                               %! baca.SingleStaffScoreTemplate.__call__
                        {                                                                            %! baca.SingleStaffScoreTemplate.__call__
            <BLANKLINE>
                            % [Music_Voice measure 1]                                                %! _comment_measure_numbers
                            c'8                                                                      %! baca.make_repeated_duration_notes
            <BLANKLINE>
                            c'8                                                                      %! baca.make_repeated_duration_notes
            <BLANKLINE>
                            c'8                                                                      %! baca.make_repeated_duration_notes
            <BLANKLINE>
                            c'8                                                                      %! baca.make_repeated_duration_notes
            <BLANKLINE>
                            % [Music_Voice measure 2]                                                %! _comment_measure_numbers
                            c'8                                                                      %! baca.make_repeated_duration_notes
            <BLANKLINE>
                            c'8                                                                      %! baca.make_repeated_duration_notes
            <BLANKLINE>
                            c'8                                                                      %! baca.make_repeated_duration_notes
            <BLANKLINE>
                            % [Music_Voice measure 3]                                                %! _comment_measure_numbers
                            c'8                                                                      %! baca.make_repeated_duration_notes
            <BLANKLINE>
                            c'8                                                                      %! baca.make_repeated_duration_notes
            <BLANKLINE>
                            c'8                                                                      %! baca.make_repeated_duration_notes
            <BLANKLINE>
                            c'8                                                                      %! baca.make_repeated_duration_notes
            <BLANKLINE>
                            % [Music_Voice measure 4]                                                %! _comment_measure_numbers
                            c'8                                                                      %! baca.make_repeated_duration_notes
            <BLANKLINE>
                            c'8                                                                      %! baca.make_repeated_duration_notes
            <BLANKLINE>
                            c'8                                                                      %! baca.make_repeated_duration_notes
            <BLANKLINE>
                            <<                                                                       %! PHANTOM:_make_multimeasure_rest_container
            <BLANKLINE>
                                \context Voice = "Music_Voice"                                       %! PHANTOM:_make_multimeasure_rest_container
                                {                                                                    %! PHANTOM:_make_multimeasure_rest_container
            <BLANKLINE>
                                    % [Music_Voice measure 5]                                        %! PHANTOM:_style_phantom_measures(5):_comment_measure_numbers
                                    \baca-invisible-music                                            %! PHANTOM:_style_phantom_measures(5):_make_multimeasure_rest_container
                                    c'1 * 1/4                                                        %! PHANTOM:_make_multimeasure_rest_container
            <BLANKLINE>
                                }                                                                    %! PHANTOM:_make_multimeasure_rest_container
            <BLANKLINE>
                                \context Voice = "Rest_Voice"                                        %! PHANTOM:_make_multimeasure_rest_container
                                {                                                                    %! PHANTOM:_make_multimeasure_rest_container
            <BLANKLINE>
                                    % [Rest_Voice measure 5]                                         %! PHANTOM:_style_phantom_measures(5):_comment_measure_numbers
                                    \once \override Score.TimeSignature.X-extent = ##f               %! PHANTOM:_style_phantom_measures(6)
                                    \once \override MultiMeasureRest.transparent = ##t               %! PHANTOM:_style_phantom_measures(7)
                                    \stopStaff                                                       %! PHANTOM:_style_phantom_measures(8)
                                    \once \override Staff.StaffSymbol.transparent = ##t              %! PHANTOM:_style_phantom_measures(8)
                                    \startStaff                                                      %! PHANTOM:_style_phantom_measures(8)
                                    R1 * 1/4                                                         %! PHANTOM:_make_multimeasure_rest_container
            <BLANKLINE>
                                }                                                                    %! PHANTOM:_make_multimeasure_rest_container
            <BLANKLINE>
                            >>                                                                       %! PHANTOM:_make_multimeasure_rest_container
            <BLANKLINE>
                        }                                                                            %! baca.SingleStaffScoreTemplate.__call__
            <BLANKLINE>
                    }                                                                                %! baca.SingleStaffScoreTemplate.__call__
            <BLANKLINE>
                >>                                                                                   %! baca.SingleStaffScoreTemplate.__call__
            <BLANKLINE>
            >>                                                                                       %! baca.SingleStaffScoreTemplate.__call__

    ..  container:: example

        Sets duration multiplier to achieve ``written_duration`` equal to 3/32:

        >>> maker = baca.SegmentMaker(
        ...     do_not_color_unpitched_music=True,
        ...     score_template=baca.SingleStaffScoreTemplate(),
        ...     spacing=baca.minimum_duration((1, 12)),
        ...     time_signatures=[(4, 8), (3, 8), (4, 8), (3, 8)],
        ...     )

        >>> maker(
        ...     'Music_Voice',
        ...     baca.make_repeated_duration_notes([(1, 8)]),
        ...     baca.set_duration_multiplier(
        ...         selector=baca.leaves(),
        ...         written_duration=(3, 32),
        ...         ),
        ...     )

        >>> lilypond_file = maker.run(environment='docs')
        >>> abjad.show(lilypond_file, strict=89) # doctest: +SKIP

        ..  docs::

            >>> abjad.f(lilypond_file[abjad.Score], strict=89)
            <BLANKLINE>
            \context Score = "Score"                                                                 %! baca.SingleStaffScoreTemplate.__call__
            <<                                                                                       %! baca.SingleStaffScoreTemplate.__call__
            <BLANKLINE>
                \context GlobalContext = "Global_Context"                                            %! abjad.ScoreTemplate._make_global_context
                <<                                                                                   %! abjad.ScoreTemplate._make_global_context
            <BLANKLINE>
                    \context GlobalSkips = "Global_Skips"                                            %! abjad.ScoreTemplate._make_global_context
                    {                                                                                %! abjad.ScoreTemplate._make_global_context
            <BLANKLINE>
                        % [Global_Skips measure 1]                                                   %! _comment_measure_numbers
                        \baca-new-spacing-section #1 #12                                             %! HorizontalSpacingSpecifier(1):SPACING_COMMAND
                        \time 4/8                                                                    %! EXPLICIT_TIME_SIGNATURE:_set_status_tag:_make_global_skips(2)
                        \baca-time-signature-color #'blue                                            %! EXPLICIT_TIME_SIGNATURE_COLOR:_attach_color_literal(2)
                        s1 * 1/2                                                                     %! _make_global_skips(1)
            <BLANKLINE>
                        % [Global_Skips measure 2]                                                   %! _comment_measure_numbers
                        \baca-new-spacing-section #1 #12                                             %! HorizontalSpacingSpecifier(1):SPACING_COMMAND
                        \time 3/8                                                                    %! EXPLICIT_TIME_SIGNATURE:_set_status_tag:_make_global_skips(2)
                        \baca-time-signature-color #'blue                                            %! EXPLICIT_TIME_SIGNATURE_COLOR:_attach_color_literal(2)
                        s1 * 3/8                                                                     %! _make_global_skips(1)
            <BLANKLINE>
                        % [Global_Skips measure 3]                                                   %! _comment_measure_numbers
                        \baca-new-spacing-section #1 #12                                             %! HorizontalSpacingSpecifier(1):SPACING_COMMAND
                        \time 4/8                                                                    %! EXPLICIT_TIME_SIGNATURE:_set_status_tag:_make_global_skips(2)
                        \baca-time-signature-color #'blue                                            %! EXPLICIT_TIME_SIGNATURE_COLOR:_attach_color_literal(2)
                        s1 * 1/2                                                                     %! _make_global_skips(1)
            <BLANKLINE>
                        % [Global_Skips measure 4]                                                   %! _comment_measure_numbers
                        \baca-new-spacing-section #1 #12                                             %! HorizontalSpacingSpecifier(1):SPACING_COMMAND
                        \time 3/8                                                                    %! EXPLICIT_TIME_SIGNATURE:_set_status_tag:_make_global_skips(2)
                        \baca-time-signature-color #'blue                                            %! EXPLICIT_TIME_SIGNATURE_COLOR:_attach_color_literal(2)
                        s1 * 3/8                                                                     %! _make_global_skips(1)
                        \baca-bar-line-visible                                                       %! _attach_final_bar_line
                        \bar "|"                                                                     %! _attach_final_bar_line
            <BLANKLINE>
                        % [Global_Skips measure 5]                                                   %! PHANTOM:_style_phantom_measures(1):_comment_measure_numbers
                        \baca-new-spacing-section #1 #4                                              %! PHANTOM:_style_phantom_measures(1):HorizontalSpacingSpecifier(1):SPACING_COMMAND
                        \time 1/4                                                                    %! PHANTOM:_style_phantom_measures(1):EXPLICIT_TIME_SIGNATURE:_set_status_tag:_make_global_skips(3)
                        \baca-time-signature-transparent                                             %! PHANTOM:_style_phantom_measures(2)
                        s1 * 1/4                                                                     %! PHANTOM:_make_global_skips(3)
                        \once \override Score.BarLine.transparent = ##t                              %! PHANTOM:_style_phantom_measures(3)
                        \once \override Score.SpanBar.transparent = ##t                              %! PHANTOM:_style_phantom_measures(3)
            <BLANKLINE>
                    }                                                                                %! abjad.ScoreTemplate._make_global_context
            <BLANKLINE>
                >>                                                                                   %! abjad.ScoreTemplate._make_global_context
            <BLANKLINE>
                \context MusicContext = "Music_Context"                                              %! baca.SingleStaffScoreTemplate.__call__
                <<                                                                                   %! baca.SingleStaffScoreTemplate.__call__
            <BLANKLINE>
                    \context Staff = "Music_Staff"                                                   %! baca.SingleStaffScoreTemplate.__call__
                    {                                                                                %! baca.SingleStaffScoreTemplate.__call__
            <BLANKLINE>
                        \context Voice = "Music_Voice"                                               %! baca.SingleStaffScoreTemplate.__call__
                        {                                                                            %! baca.SingleStaffScoreTemplate.__call__
            <BLANKLINE>
                            % [Music_Voice measure 1]                                                %! _comment_measure_numbers
                            c'16. * 4/3                                                              %! baca.make_repeated_duration_notes
            <BLANKLINE>
                            c'16. * 4/3                                                              %! baca.make_repeated_duration_notes
            <BLANKLINE>
                            c'16. * 4/3                                                              %! baca.make_repeated_duration_notes
            <BLANKLINE>
                            c'16. * 4/3                                                              %! baca.make_repeated_duration_notes
            <BLANKLINE>
                            % [Music_Voice measure 2]                                                %! _comment_measure_numbers
                            c'16. * 4/3                                                              %! baca.make_repeated_duration_notes
            <BLANKLINE>
                            c'16. * 4/3                                                              %! baca.make_repeated_duration_notes
            <BLANKLINE>
                            c'16. * 4/3                                                              %! baca.make_repeated_duration_notes
            <BLANKLINE>
                            % [Music_Voice measure 3]                                                %! _comment_measure_numbers
                            c'16. * 4/3                                                              %! baca.make_repeated_duration_notes
            <BLANKLINE>
                            c'16. * 4/3                                                              %! baca.make_repeated_duration_notes
            <BLANKLINE>
                            c'16. * 4/3                                                              %! baca.make_repeated_duration_notes
            <BLANKLINE>
                            c'16. * 4/3                                                              %! baca.make_repeated_duration_notes
            <BLANKLINE>
                            % [Music_Voice measure 4]                                                %! _comment_measure_numbers
                            c'16. * 4/3                                                              %! baca.make_repeated_duration_notes
            <BLANKLINE>
                            c'16. * 4/3                                                              %! baca.make_repeated_duration_notes
            <BLANKLINE>
                            c'16. * 4/3                                                              %! baca.make_repeated_duration_notes
            <BLANKLINE>
                            <<                                                                       %! PHANTOM:_make_multimeasure_rest_container
            <BLANKLINE>
                                \context Voice = "Music_Voice"                                       %! PHANTOM:_make_multimeasure_rest_container
                                {                                                                    %! PHANTOM:_make_multimeasure_rest_container
            <BLANKLINE>
                                    % [Music_Voice measure 5]                                        %! PHANTOM:_style_phantom_measures(5):_comment_measure_numbers
                                    \baca-invisible-music                                            %! PHANTOM:_style_phantom_measures(5):_make_multimeasure_rest_container
                                    c'1 * 1/4                                                        %! PHANTOM:_make_multimeasure_rest_container
            <BLANKLINE>
                                }                                                                    %! PHANTOM:_make_multimeasure_rest_container
            <BLANKLINE>
                                \context Voice = "Rest_Voice"                                        %! PHANTOM:_make_multimeasure_rest_container
                                {                                                                    %! PHANTOM:_make_multimeasure_rest_container
            <BLANKLINE>
                                    % [Rest_Voice measure 5]                                         %! PHANTOM:_style_phantom_measures(5):_comment_measure_numbers
                                    \once \override Score.TimeSignature.X-extent = ##f               %! PHANTOM:_style_phantom_measures(6)
                                    \once \override MultiMeasureRest.transparent = ##t               %! PHANTOM:_style_phantom_measures(7)
                                    \stopStaff                                                       %! PHANTOM:_style_phantom_measures(8)
                                    \once \override Staff.StaffSymbol.transparent = ##t              %! PHANTOM:_style_phantom_measures(8)
                                    \startStaff                                                      %! PHANTOM:_style_phantom_measures(8)
                                    R1 * 1/4                                                         %! PHANTOM:_make_multimeasure_rest_container
            <BLANKLINE>
                                }                                                                    %! PHANTOM:_make_multimeasure_rest_container
            <BLANKLINE>
                            >>                                                                       %! PHANTOM:_make_multimeasure_rest_container
            <BLANKLINE>
                        }                                                                            %! baca.SingleStaffScoreTemplate.__call__
            <BLANKLINE>
                    }                                                                                %! baca.SingleStaffScoreTemplate.__call__
            <BLANKLINE>
                >>                                                                                   %! baca.SingleStaffScoreTemplate.__call__
            <BLANKLINE>
            >>                                                                                       %! baca.SingleStaffScoreTemplate.__call__

    ..  container:: example

        Sets duration multiplier automatically to achieve ``written_duration``
        equal to 1:

        >>> maker = baca.SegmentMaker(
        ...     do_not_color_unpitched_music=True,
        ...     score_template=baca.SingleStaffScoreTemplate(),
        ...     spacing=baca.minimum_duration((1, 12)),
        ...     time_signatures=[(4, 8), (3, 8), (4, 8), (3, 8)],
        ...     )

        >>> maker(
        ...     'Music_Voice',
        ...     baca.make_repeated_duration_notes([(1, 8)]),
        ...     baca.set_duration_multiplier(
        ...         selector=baca.leaves(),
        ...         written_duration=(1,),
        ...         ),
        ...     )

        >>> lilypond_file = maker.run(environment='docs')
        >>> abjad.show(lilypond_file, strict=89) # doctest: +SKIP

        ..  docs::

            >>> abjad.f(lilypond_file[abjad.Score], strict=89)
            <BLANKLINE>
            \context Score = "Score"                                                                 %! baca.SingleStaffScoreTemplate.__call__
            <<                                                                                       %! baca.SingleStaffScoreTemplate.__call__
            <BLANKLINE>
                \context GlobalContext = "Global_Context"                                            %! abjad.ScoreTemplate._make_global_context
                <<                                                                                   %! abjad.ScoreTemplate._make_global_context
            <BLANKLINE>
                    \context GlobalSkips = "Global_Skips"                                            %! abjad.ScoreTemplate._make_global_context
                    {                                                                                %! abjad.ScoreTemplate._make_global_context
            <BLANKLINE>
                        % [Global_Skips measure 1]                                                   %! _comment_measure_numbers
                        \baca-new-spacing-section #1 #12                                             %! HorizontalSpacingSpecifier(1):SPACING_COMMAND
                        \time 4/8                                                                    %! EXPLICIT_TIME_SIGNATURE:_set_status_tag:_make_global_skips(2)
                        \baca-time-signature-color #'blue                                            %! EXPLICIT_TIME_SIGNATURE_COLOR:_attach_color_literal(2)
                        s1 * 1/2                                                                     %! _make_global_skips(1)
            <BLANKLINE>
                        % [Global_Skips measure 2]                                                   %! _comment_measure_numbers
                        \baca-new-spacing-section #1 #12                                             %! HorizontalSpacingSpecifier(1):SPACING_COMMAND
                        \time 3/8                                                                    %! EXPLICIT_TIME_SIGNATURE:_set_status_tag:_make_global_skips(2)
                        \baca-time-signature-color #'blue                                            %! EXPLICIT_TIME_SIGNATURE_COLOR:_attach_color_literal(2)
                        s1 * 3/8                                                                     %! _make_global_skips(1)
            <BLANKLINE>
                        % [Global_Skips measure 3]                                                   %! _comment_measure_numbers
                        \baca-new-spacing-section #1 #12                                             %! HorizontalSpacingSpecifier(1):SPACING_COMMAND
                        \time 4/8                                                                    %! EXPLICIT_TIME_SIGNATURE:_set_status_tag:_make_global_skips(2)
                        \baca-time-signature-color #'blue                                            %! EXPLICIT_TIME_SIGNATURE_COLOR:_attach_color_literal(2)
                        s1 * 1/2                                                                     %! _make_global_skips(1)
            <BLANKLINE>
                        % [Global_Skips measure 4]                                                   %! _comment_measure_numbers
                        \baca-new-spacing-section #1 #12                                             %! HorizontalSpacingSpecifier(1):SPACING_COMMAND
                        \time 3/8                                                                    %! EXPLICIT_TIME_SIGNATURE:_set_status_tag:_make_global_skips(2)
                        \baca-time-signature-color #'blue                                            %! EXPLICIT_TIME_SIGNATURE_COLOR:_attach_color_literal(2)
                        s1 * 3/8                                                                     %! _make_global_skips(1)
                        \baca-bar-line-visible                                                       %! _attach_final_bar_line
                        \bar "|"                                                                     %! _attach_final_bar_line
            <BLANKLINE>
                        % [Global_Skips measure 5]                                                   %! PHANTOM:_style_phantom_measures(1):_comment_measure_numbers
                        \baca-new-spacing-section #1 #4                                              %! PHANTOM:_style_phantom_measures(1):HorizontalSpacingSpecifier(1):SPACING_COMMAND
                        \time 1/4                                                                    %! PHANTOM:_style_phantom_measures(1):EXPLICIT_TIME_SIGNATURE:_set_status_tag:_make_global_skips(3)
                        \baca-time-signature-transparent                                             %! PHANTOM:_style_phantom_measures(2)
                        s1 * 1/4                                                                     %! PHANTOM:_make_global_skips(3)
                        \once \override Score.BarLine.transparent = ##t                              %! PHANTOM:_style_phantom_measures(3)
                        \once \override Score.SpanBar.transparent = ##t                              %! PHANTOM:_style_phantom_measures(3)
            <BLANKLINE>
                    }                                                                                %! abjad.ScoreTemplate._make_global_context
            <BLANKLINE>
                >>                                                                                   %! abjad.ScoreTemplate._make_global_context
            <BLANKLINE>
                \context MusicContext = "Music_Context"                                              %! baca.SingleStaffScoreTemplate.__call__
                <<                                                                                   %! baca.SingleStaffScoreTemplate.__call__
            <BLANKLINE>
                    \context Staff = "Music_Staff"                                                   %! baca.SingleStaffScoreTemplate.__call__
                    {                                                                                %! baca.SingleStaffScoreTemplate.__call__
            <BLANKLINE>
                        \context Voice = "Music_Voice"                                               %! baca.SingleStaffScoreTemplate.__call__
                        {                                                                            %! baca.SingleStaffScoreTemplate.__call__
            <BLANKLINE>
                            % [Music_Voice measure 1]                                                %! _comment_measure_numbers
                            c'1 * 1/8                                                                %! baca.make_repeated_duration_notes
            <BLANKLINE>
                            c'1 * 1/8                                                                %! baca.make_repeated_duration_notes
            <BLANKLINE>
                            c'1 * 1/8                                                                %! baca.make_repeated_duration_notes
            <BLANKLINE>
                            c'1 * 1/8                                                                %! baca.make_repeated_duration_notes
            <BLANKLINE>
                            % [Music_Voice measure 2]                                                %! _comment_measure_numbers
                            c'1 * 1/8                                                                %! baca.make_repeated_duration_notes
            <BLANKLINE>
                            c'1 * 1/8                                                                %! baca.make_repeated_duration_notes
            <BLANKLINE>
                            c'1 * 1/8                                                                %! baca.make_repeated_duration_notes
            <BLANKLINE>
                            % [Music_Voice measure 3]                                                %! _comment_measure_numbers
                            c'1 * 1/8                                                                %! baca.make_repeated_duration_notes
            <BLANKLINE>
                            c'1 * 1/8                                                                %! baca.make_repeated_duration_notes
            <BLANKLINE>
                            c'1 * 1/8                                                                %! baca.make_repeated_duration_notes
            <BLANKLINE>
                            c'1 * 1/8                                                                %! baca.make_repeated_duration_notes
            <BLANKLINE>
                            % [Music_Voice measure 4]                                                %! _comment_measure_numbers
                            c'1 * 1/8                                                                %! baca.make_repeated_duration_notes
            <BLANKLINE>
                            c'1 * 1/8                                                                %! baca.make_repeated_duration_notes
            <BLANKLINE>
                            c'1 * 1/8                                                                %! baca.make_repeated_duration_notes
            <BLANKLINE>
                            <<                                                                       %! PHANTOM:_make_multimeasure_rest_container
            <BLANKLINE>
                                \context Voice = "Music_Voice"                                       %! PHANTOM:_make_multimeasure_rest_container
                                {                                                                    %! PHANTOM:_make_multimeasure_rest_container
            <BLANKLINE>
                                    % [Music_Voice measure 5]                                        %! PHANTOM:_style_phantom_measures(5):_comment_measure_numbers
                                    \baca-invisible-music                                            %! PHANTOM:_style_phantom_measures(5):_make_multimeasure_rest_container
                                    c'1 * 1/4                                                        %! PHANTOM:_make_multimeasure_rest_container
            <BLANKLINE>
                                }                                                                    %! PHANTOM:_make_multimeasure_rest_container
            <BLANKLINE>
                                \context Voice = "Rest_Voice"                                        %! PHANTOM:_make_multimeasure_rest_container
                                {                                                                    %! PHANTOM:_make_multimeasure_rest_container
            <BLANKLINE>
                                    % [Rest_Voice measure 5]                                         %! PHANTOM:_style_phantom_measures(5):_comment_measure_numbers
                                    \once \override Score.TimeSignature.X-extent = ##f               %! PHANTOM:_style_phantom_measures(6)
                                    \once \override MultiMeasureRest.transparent = ##t               %! PHANTOM:_style_phantom_measures(7)
                                    \stopStaff                                                       %! PHANTOM:_style_phantom_measures(8)
                                    \once \override Staff.StaffSymbol.transparent = ##t              %! PHANTOM:_style_phantom_measures(8)
                                    \startStaff                                                      %! PHANTOM:_style_phantom_measures(8)
                                    R1 * 1/4                                                         %! PHANTOM:_make_multimeasure_rest_container
            <BLANKLINE>
                                }                                                                    %! PHANTOM:_make_multimeasure_rest_container
            <BLANKLINE>
                            >>                                                                       %! PHANTOM:_make_multimeasure_rest_container
            <BLANKLINE>
                        }                                                                            %! baca.SingleStaffScoreTemplate.__call__
            <BLANKLINE>
                    }                                                                                %! baca.SingleStaffScoreTemplate.__call__
            <BLANKLINE>
                >>                                                                                   %! baca.SingleStaffScoreTemplate.__call__
            <BLANKLINE>
            >>                                                                                       %! baca.SingleStaffScoreTemplate.__call__

    """
    return DurationMultiplierCommand(
        selector=selector, written_duration=written_duration
    )


def tacet(
    color: str = "green",
    *,
    measures: typings.SliceTyping = None,
    selector: abjad.SelectorTyping = "baca.mmrests()",
) -> overrides.OverrideCommand:
    """
    Colors multimeasure rests.
    """
    command = overrides.mmrest_color(
        color, selector=selector, tag=f"{const.TACET}:baca_tacet"
    )
    command_ = scoping.new(command, measures=measures)
    assert isinstance(command_, overrides.OverrideCommand)
    return command_


def tie_from(
    *,
    allow_rest: bool = None,
    selector: abjad.SelectorTyping = "baca.pleaf(-1)",
) -> TieCorrectionCommand:
    r"""
    Ties from leaf.

    ..  container:: example

        >>> maker = baca.SegmentMaker(
        ...     do_not_color_unpitched_music=True,
        ...     score_template=baca.SingleStaffScoreTemplate(),
        ...     time_signatures=[(4, 8), (3, 8), (4, 8), (3, 8)],
        ...     )

        >>> maker(
        ...     'Music_Voice',
        ...     baca.make_notes(),
        ...     baca.tie_from(selector=baca.leaf(1)),
        ...     )

        >>> lilypond_file = maker.run(environment='docs')
        >>> abjad.show(lilypond_file, strict=89) # doctest: +SKIP

        ..  docs::

            >>> abjad.f(lilypond_file[abjad.Score], strict=89)
            <BLANKLINE>
            \context Score = "Score"                                                                 %! baca.SingleStaffScoreTemplate.__call__
            <<                                                                                       %! baca.SingleStaffScoreTemplate.__call__
            <BLANKLINE>
                \context GlobalContext = "Global_Context"                                            %! abjad.ScoreTemplate._make_global_context
                <<                                                                                   %! abjad.ScoreTemplate._make_global_context
            <BLANKLINE>
                    \context GlobalSkips = "Global_Skips"                                            %! abjad.ScoreTemplate._make_global_context
                    {                                                                                %! abjad.ScoreTemplate._make_global_context
            <BLANKLINE>
                        % [Global_Skips measure 1]                                                   %! _comment_measure_numbers
                        \time 4/8                                                                    %! EXPLICIT_TIME_SIGNATURE:_set_status_tag:_make_global_skips(2)
                        \baca-time-signature-color #'blue                                            %! EXPLICIT_TIME_SIGNATURE_COLOR:_attach_color_literal(2)
                        s1 * 1/2                                                                     %! _make_global_skips(1)
            <BLANKLINE>
                        % [Global_Skips measure 2]                                                   %! _comment_measure_numbers
                        \time 3/8                                                                    %! EXPLICIT_TIME_SIGNATURE:_set_status_tag:_make_global_skips(2)
                        \baca-time-signature-color #'blue                                            %! EXPLICIT_TIME_SIGNATURE_COLOR:_attach_color_literal(2)
                        s1 * 3/8                                                                     %! _make_global_skips(1)
            <BLANKLINE>
                        % [Global_Skips measure 3]                                                   %! _comment_measure_numbers
                        \time 4/8                                                                    %! EXPLICIT_TIME_SIGNATURE:_set_status_tag:_make_global_skips(2)
                        \baca-time-signature-color #'blue                                            %! EXPLICIT_TIME_SIGNATURE_COLOR:_attach_color_literal(2)
                        s1 * 1/2                                                                     %! _make_global_skips(1)
            <BLANKLINE>
                        % [Global_Skips measure 4]                                                   %! _comment_measure_numbers
                        \time 3/8                                                                    %! EXPLICIT_TIME_SIGNATURE:_set_status_tag:_make_global_skips(2)
                        \baca-time-signature-color #'blue                                            %! EXPLICIT_TIME_SIGNATURE_COLOR:_attach_color_literal(2)
                        s1 * 3/8                                                                     %! _make_global_skips(1)
                        \baca-bar-line-visible                                                       %! _attach_final_bar_line
                        \bar "|"                                                                     %! _attach_final_bar_line
            <BLANKLINE>
                        % [Global_Skips measure 5]                                                   %! PHANTOM:_style_phantom_measures(1):_comment_measure_numbers
                        \time 1/4                                                                    %! PHANTOM:_style_phantom_measures(1):EXPLICIT_TIME_SIGNATURE:_set_status_tag:_make_global_skips(3)
                        \baca-time-signature-transparent                                             %! PHANTOM:_style_phantom_measures(2)
                        s1 * 1/4                                                                     %! PHANTOM:_make_global_skips(3)
                        \once \override Score.BarLine.transparent = ##t                              %! PHANTOM:_style_phantom_measures(3)
                        \once \override Score.SpanBar.transparent = ##t                              %! PHANTOM:_style_phantom_measures(3)
            <BLANKLINE>
                    }                                                                                %! abjad.ScoreTemplate._make_global_context
            <BLANKLINE>
                >>                                                                                   %! abjad.ScoreTemplate._make_global_context
            <BLANKLINE>
                \context MusicContext = "Music_Context"                                              %! baca.SingleStaffScoreTemplate.__call__
                <<                                                                                   %! baca.SingleStaffScoreTemplate.__call__
            <BLANKLINE>
                    \context Staff = "Music_Staff"                                                   %! baca.SingleStaffScoreTemplate.__call__
                    {                                                                                %! baca.SingleStaffScoreTemplate.__call__
            <BLANKLINE>
                        \context Voice = "Music_Voice"                                               %! baca.SingleStaffScoreTemplate.__call__
                        {                                                                            %! baca.SingleStaffScoreTemplate.__call__
            <BLANKLINE>
                            % [Music_Voice measure 1]                                                %! _comment_measure_numbers
                            c'2                                                                      %! baca.make_notes
            <BLANKLINE>
                            % [Music_Voice measure 2]                                                %! _comment_measure_numbers
                            c'4.                                                                     %! baca.make_notes
                            ~                                                                        %! TieCorrectionCommand
            <BLANKLINE>
                            % [Music_Voice measure 3]                                                %! _comment_measure_numbers
                            c'2                                                                      %! baca.make_notes
            <BLANKLINE>
                            % [Music_Voice measure 4]                                                %! _comment_measure_numbers
                            c'4.                                                                     %! baca.make_notes
            <BLANKLINE>
                            <<                                                                       %! PHANTOM:_make_multimeasure_rest_container
            <BLANKLINE>
                                \context Voice = "Music_Voice"                                       %! PHANTOM:_make_multimeasure_rest_container
                                {                                                                    %! PHANTOM:_make_multimeasure_rest_container
            <BLANKLINE>
                                    % [Music_Voice measure 5]                                        %! PHANTOM:_style_phantom_measures(5):_comment_measure_numbers
                                    \baca-invisible-music                                            %! PHANTOM:_style_phantom_measures(5):_make_multimeasure_rest_container
                                    c'1 * 1/4                                                        %! PHANTOM:_make_multimeasure_rest_container
            <BLANKLINE>
                                }                                                                    %! PHANTOM:_make_multimeasure_rest_container
            <BLANKLINE>
                                \context Voice = "Rest_Voice"                                        %! PHANTOM:_make_multimeasure_rest_container
                                {                                                                    %! PHANTOM:_make_multimeasure_rest_container
            <BLANKLINE>
                                    % [Rest_Voice measure 5]                                         %! PHANTOM:_style_phantom_measures(5):_comment_measure_numbers
                                    \once \override Score.TimeSignature.X-extent = ##f               %! PHANTOM:_style_phantom_measures(6)
                                    \once \override MultiMeasureRest.transparent = ##t               %! PHANTOM:_style_phantom_measures(7)
                                    \stopStaff                                                       %! PHANTOM:_style_phantom_measures(8)
                                    \once \override Staff.StaffSymbol.transparent = ##t              %! PHANTOM:_style_phantom_measures(8)
                                    \startStaff                                                      %! PHANTOM:_style_phantom_measures(8)
                                    R1 * 1/4                                                         %! PHANTOM:_make_multimeasure_rest_container
            <BLANKLINE>
                                }                                                                    %! PHANTOM:_make_multimeasure_rest_container
            <BLANKLINE>
                            >>                                                                       %! PHANTOM:_make_multimeasure_rest_container
            <BLANKLINE>
                        }                                                                            %! baca.SingleStaffScoreTemplate.__call__
            <BLANKLINE>
                    }                                                                                %! baca.SingleStaffScoreTemplate.__call__
            <BLANKLINE>
                >>                                                                                   %! baca.SingleStaffScoreTemplate.__call__
            <BLANKLINE>
            >>                                                                                       %! baca.SingleStaffScoreTemplate.__call__

    """
    return TieCorrectionCommand(
        allow_rest=allow_rest, repeat=False, selector=selector
    )


def tie_to(
    *,
    allow_rest: bool = None,
    selector: abjad.SelectorTyping = "baca.pleaf(0)",
) -> TieCorrectionCommand:
    r"""
    Ties to leaf.

    ..  container:: example

        >>> maker = baca.SegmentMaker(
        ...     do_not_color_unpitched_music=True,
        ...     score_template=baca.SingleStaffScoreTemplate(),
        ...     time_signatures=[(4, 8), (3, 8), (4, 8), (3, 8)],
        ...     )

        >>> maker(
        ...     'Music_Voice',
        ...     baca.make_notes(),
        ...     baca.tie_to(selector=baca.leaf(1)),
        ...     )

        >>> lilypond_file = maker.run(environment='docs')
        >>> abjad.show(lilypond_file, strict=89) # doctest: +SKIP

        ..  docs::

            >>> abjad.f(lilypond_file[abjad.Score], strict=89)
            <BLANKLINE>
            \context Score = "Score"                                                                 %! baca.SingleStaffScoreTemplate.__call__
            <<                                                                                       %! baca.SingleStaffScoreTemplate.__call__
            <BLANKLINE>
                \context GlobalContext = "Global_Context"                                            %! abjad.ScoreTemplate._make_global_context
                <<                                                                                   %! abjad.ScoreTemplate._make_global_context
            <BLANKLINE>
                    \context GlobalSkips = "Global_Skips"                                            %! abjad.ScoreTemplate._make_global_context
                    {                                                                                %! abjad.ScoreTemplate._make_global_context
            <BLANKLINE>
                        % [Global_Skips measure 1]                                                   %! _comment_measure_numbers
                        \time 4/8                                                                    %! EXPLICIT_TIME_SIGNATURE:_set_status_tag:_make_global_skips(2)
                        \baca-time-signature-color #'blue                                            %! EXPLICIT_TIME_SIGNATURE_COLOR:_attach_color_literal(2)
                        s1 * 1/2                                                                     %! _make_global_skips(1)
            <BLANKLINE>
                        % [Global_Skips measure 2]                                                   %! _comment_measure_numbers
                        \time 3/8                                                                    %! EXPLICIT_TIME_SIGNATURE:_set_status_tag:_make_global_skips(2)
                        \baca-time-signature-color #'blue                                            %! EXPLICIT_TIME_SIGNATURE_COLOR:_attach_color_literal(2)
                        s1 * 3/8                                                                     %! _make_global_skips(1)
            <BLANKLINE>
                        % [Global_Skips measure 3]                                                   %! _comment_measure_numbers
                        \time 4/8                                                                    %! EXPLICIT_TIME_SIGNATURE:_set_status_tag:_make_global_skips(2)
                        \baca-time-signature-color #'blue                                            %! EXPLICIT_TIME_SIGNATURE_COLOR:_attach_color_literal(2)
                        s1 * 1/2                                                                     %! _make_global_skips(1)
            <BLANKLINE>
                        % [Global_Skips measure 4]                                                   %! _comment_measure_numbers
                        \time 3/8                                                                    %! EXPLICIT_TIME_SIGNATURE:_set_status_tag:_make_global_skips(2)
                        \baca-time-signature-color #'blue                                            %! EXPLICIT_TIME_SIGNATURE_COLOR:_attach_color_literal(2)
                        s1 * 3/8                                                                     %! _make_global_skips(1)
                        \baca-bar-line-visible                                                       %! _attach_final_bar_line
                        \bar "|"                                                                     %! _attach_final_bar_line
            <BLANKLINE>
                        % [Global_Skips measure 5]                                                   %! PHANTOM:_style_phantom_measures(1):_comment_measure_numbers
                        \time 1/4                                                                    %! PHANTOM:_style_phantom_measures(1):EXPLICIT_TIME_SIGNATURE:_set_status_tag:_make_global_skips(3)
                        \baca-time-signature-transparent                                             %! PHANTOM:_style_phantom_measures(2)
                        s1 * 1/4                                                                     %! PHANTOM:_make_global_skips(3)
                        \once \override Score.BarLine.transparent = ##t                              %! PHANTOM:_style_phantom_measures(3)
                        \once \override Score.SpanBar.transparent = ##t                              %! PHANTOM:_style_phantom_measures(3)
            <BLANKLINE>
                    }                                                                                %! abjad.ScoreTemplate._make_global_context
            <BLANKLINE>
                >>                                                                                   %! abjad.ScoreTemplate._make_global_context
            <BLANKLINE>
                \context MusicContext = "Music_Context"                                              %! baca.SingleStaffScoreTemplate.__call__
                <<                                                                                   %! baca.SingleStaffScoreTemplate.__call__
            <BLANKLINE>
                    \context Staff = "Music_Staff"                                                   %! baca.SingleStaffScoreTemplate.__call__
                    {                                                                                %! baca.SingleStaffScoreTemplate.__call__
            <BLANKLINE>
                        \context Voice = "Music_Voice"                                               %! baca.SingleStaffScoreTemplate.__call__
                        {                                                                            %! baca.SingleStaffScoreTemplate.__call__
            <BLANKLINE>
                            % [Music_Voice measure 1]                                                %! _comment_measure_numbers
                            c'2                                                                      %! baca.make_notes
                            ~                                                                        %! TieCorrectionCommand
            <BLANKLINE>
                            % [Music_Voice measure 2]                                                %! _comment_measure_numbers
                            c'4.                                                                     %! baca.make_notes
            <BLANKLINE>
                            % [Music_Voice measure 3]                                                %! _comment_measure_numbers
                            c'2                                                                      %! baca.make_notes
            <BLANKLINE>
                            % [Music_Voice measure 4]                                                %! _comment_measure_numbers
                            c'4.                                                                     %! baca.make_notes
            <BLANKLINE>
                            <<                                                                       %! PHANTOM:_make_multimeasure_rest_container
            <BLANKLINE>
                                \context Voice = "Music_Voice"                                       %! PHANTOM:_make_multimeasure_rest_container
                                {                                                                    %! PHANTOM:_make_multimeasure_rest_container
            <BLANKLINE>
                                    % [Music_Voice measure 5]                                        %! PHANTOM:_style_phantom_measures(5):_comment_measure_numbers
                                    \baca-invisible-music                                            %! PHANTOM:_style_phantom_measures(5):_make_multimeasure_rest_container
                                    c'1 * 1/4                                                        %! PHANTOM:_make_multimeasure_rest_container
            <BLANKLINE>
                                }                                                                    %! PHANTOM:_make_multimeasure_rest_container
            <BLANKLINE>
                                \context Voice = "Rest_Voice"                                        %! PHANTOM:_make_multimeasure_rest_container
                                {                                                                    %! PHANTOM:_make_multimeasure_rest_container
            <BLANKLINE>
                                    % [Rest_Voice measure 5]                                         %! PHANTOM:_style_phantom_measures(5):_comment_measure_numbers
                                    \once \override Score.TimeSignature.X-extent = ##f               %! PHANTOM:_style_phantom_measures(6)
                                    \once \override MultiMeasureRest.transparent = ##t               %! PHANTOM:_style_phantom_measures(7)
                                    \stopStaff                                                       %! PHANTOM:_style_phantom_measures(8)
                                    \once \override Staff.StaffSymbol.transparent = ##t              %! PHANTOM:_style_phantom_measures(8)
                                    \startStaff                                                      %! PHANTOM:_style_phantom_measures(8)
                                    R1 * 1/4                                                         %! PHANTOM:_make_multimeasure_rest_container
            <BLANKLINE>
                                }                                                                    %! PHANTOM:_make_multimeasure_rest_container
            <BLANKLINE>
                            >>                                                                       %! PHANTOM:_make_multimeasure_rest_container
            <BLANKLINE>
                        }                                                                            %! baca.SingleStaffScoreTemplate.__call__
            <BLANKLINE>
                    }                                                                                %! baca.SingleStaffScoreTemplate.__call__
            <BLANKLINE>
                >>                                                                                   %! baca.SingleStaffScoreTemplate.__call__
            <BLANKLINE>
            >>                                                                                       %! baca.SingleStaffScoreTemplate.__call__

    """
    return TieCorrectionCommand(
        allow_rest=allow_rest,
        direction=abjad.Left,
        repeat=False,
        selector=selector,
    )


def untie_to(
    *, selector: abjad.SelectorTyping = "baca.pleaf(0)"
) -> TieCorrectionCommand:
    r"""
    Unties to leaf.

    ..  container:: example

        >>> maker = baca.SegmentMaker(
        ...     do_not_color_unpitched_music=True,
        ...     score_template=baca.SingleStaffScoreTemplate(),
        ...     time_signatures=[(4, 8), (3, 8), (4, 8), (3, 8)],
        ...     )

        >>> maker(
        ...     'Music_Voice',
        ...     baca.make_tied_notes(),
        ...     baca.untie_to(selector=baca.leaf(2)),
        ...     )

        >>> lilypond_file = maker.run(environment='docs')
        >>> abjad.show(lilypond_file, strict=89) # doctest: +SKIP

        ..  docs::

            >>> abjad.f(lilypond_file[abjad.Score], strict=89)
            <BLANKLINE>
            \context Score = "Score"                                                                 %! baca.SingleStaffScoreTemplate.__call__
            <<                                                                                       %! baca.SingleStaffScoreTemplate.__call__
            <BLANKLINE>
                \context GlobalContext = "Global_Context"                                            %! abjad.ScoreTemplate._make_global_context
                <<                                                                                   %! abjad.ScoreTemplate._make_global_context
            <BLANKLINE>
                    \context GlobalSkips = "Global_Skips"                                            %! abjad.ScoreTemplate._make_global_context
                    {                                                                                %! abjad.ScoreTemplate._make_global_context
            <BLANKLINE>
                        % [Global_Skips measure 1]                                                   %! _comment_measure_numbers
                        \time 4/8                                                                    %! EXPLICIT_TIME_SIGNATURE:_set_status_tag:_make_global_skips(2)
                        \baca-time-signature-color #'blue                                            %! EXPLICIT_TIME_SIGNATURE_COLOR:_attach_color_literal(2)
                        s1 * 1/2                                                                     %! _make_global_skips(1)
            <BLANKLINE>
                        % [Global_Skips measure 2]                                                   %! _comment_measure_numbers
                        \time 3/8                                                                    %! EXPLICIT_TIME_SIGNATURE:_set_status_tag:_make_global_skips(2)
                        \baca-time-signature-color #'blue                                            %! EXPLICIT_TIME_SIGNATURE_COLOR:_attach_color_literal(2)
                        s1 * 3/8                                                                     %! _make_global_skips(1)
            <BLANKLINE>
                        % [Global_Skips measure 3]                                                   %! _comment_measure_numbers
                        \time 4/8                                                                    %! EXPLICIT_TIME_SIGNATURE:_set_status_tag:_make_global_skips(2)
                        \baca-time-signature-color #'blue                                            %! EXPLICIT_TIME_SIGNATURE_COLOR:_attach_color_literal(2)
                        s1 * 1/2                                                                     %! _make_global_skips(1)
            <BLANKLINE>
                        % [Global_Skips measure 4]                                                   %! _comment_measure_numbers
                        \time 3/8                                                                    %! EXPLICIT_TIME_SIGNATURE:_set_status_tag:_make_global_skips(2)
                        \baca-time-signature-color #'blue                                            %! EXPLICIT_TIME_SIGNATURE_COLOR:_attach_color_literal(2)
                        s1 * 3/8                                                                     %! _make_global_skips(1)
                        \baca-bar-line-visible                                                       %! _attach_final_bar_line
                        \bar "|"                                                                     %! _attach_final_bar_line
            <BLANKLINE>
                        % [Global_Skips measure 5]                                                   %! PHANTOM:_style_phantom_measures(1):_comment_measure_numbers
                        \time 1/4                                                                    %! PHANTOM:_style_phantom_measures(1):EXPLICIT_TIME_SIGNATURE:_set_status_tag:_make_global_skips(3)
                        \baca-time-signature-transparent                                             %! PHANTOM:_style_phantom_measures(2)
                        s1 * 1/4                                                                     %! PHANTOM:_make_global_skips(3)
                        \once \override Score.BarLine.transparent = ##t                              %! PHANTOM:_style_phantom_measures(3)
                        \once \override Score.SpanBar.transparent = ##t                              %! PHANTOM:_style_phantom_measures(3)
            <BLANKLINE>
                    }                                                                                %! abjad.ScoreTemplate._make_global_context
            <BLANKLINE>
                >>                                                                                   %! abjad.ScoreTemplate._make_global_context
            <BLANKLINE>
                \context MusicContext = "Music_Context"                                              %! baca.SingleStaffScoreTemplate.__call__
                <<                                                                                   %! baca.SingleStaffScoreTemplate.__call__
            <BLANKLINE>
                    \context Staff = "Music_Staff"                                                   %! baca.SingleStaffScoreTemplate.__call__
                    {                                                                                %! baca.SingleStaffScoreTemplate.__call__
            <BLANKLINE>
                        \context Voice = "Music_Voice"                                               %! baca.SingleStaffScoreTemplate.__call__
                        {                                                                            %! baca.SingleStaffScoreTemplate.__call__
            <BLANKLINE>
                            % [Music_Voice measure 1]                                                %! _comment_measure_numbers
                            c'2                                                                      %! baca.make_tied_notes
                            ~
            <BLANKLINE>
                            % [Music_Voice measure 2]                                                %! _comment_measure_numbers
                            c'4.                                                                     %! baca.make_tied_notes
            <BLANKLINE>
                            % [Music_Voice measure 3]                                                %! _comment_measure_numbers
                            c'2                                                                      %! baca.make_tied_notes
                            ~
            <BLANKLINE>
                            % [Music_Voice measure 4]                                                %! _comment_measure_numbers
                            c'4.                                                                     %! baca.make_tied_notes
            <BLANKLINE>
                            <<                                                                       %! PHANTOM:_make_multimeasure_rest_container
            <BLANKLINE>
                                \context Voice = "Music_Voice"                                       %! PHANTOM:_make_multimeasure_rest_container
                                {                                                                    %! PHANTOM:_make_multimeasure_rest_container
            <BLANKLINE>
                                    % [Music_Voice measure 5]                                        %! PHANTOM:_style_phantom_measures(5):_comment_measure_numbers
                                    \baca-invisible-music                                            %! PHANTOM:_style_phantom_measures(5):_make_multimeasure_rest_container
                                    c'1 * 1/4                                                        %! PHANTOM:_make_multimeasure_rest_container
            <BLANKLINE>
                                }                                                                    %! PHANTOM:_make_multimeasure_rest_container
            <BLANKLINE>
                                \context Voice = "Rest_Voice"                                        %! PHANTOM:_make_multimeasure_rest_container
                                {                                                                    %! PHANTOM:_make_multimeasure_rest_container
            <BLANKLINE>
                                    % [Rest_Voice measure 5]                                         %! PHANTOM:_style_phantom_measures(5):_comment_measure_numbers
                                    \once \override Score.TimeSignature.X-extent = ##f               %! PHANTOM:_style_phantom_measures(6)
                                    \once \override MultiMeasureRest.transparent = ##t               %! PHANTOM:_style_phantom_measures(7)
                                    \stopStaff                                                       %! PHANTOM:_style_phantom_measures(8)
                                    \once \override Staff.StaffSymbol.transparent = ##t              %! PHANTOM:_style_phantom_measures(8)
                                    \startStaff                                                      %! PHANTOM:_style_phantom_measures(8)
                                    R1 * 1/4                                                         %! PHANTOM:_make_multimeasure_rest_container
            <BLANKLINE>
                                }                                                                    %! PHANTOM:_make_multimeasure_rest_container
            <BLANKLINE>
                            >>                                                                       %! PHANTOM:_make_multimeasure_rest_container
            <BLANKLINE>
                        }                                                                            %! baca.SingleStaffScoreTemplate.__call__
            <BLANKLINE>
                    }                                                                                %! baca.SingleStaffScoreTemplate.__call__
            <BLANKLINE>
                >>                                                                                   %! baca.SingleStaffScoreTemplate.__call__
            <BLANKLINE>
            >>                                                                                       %! baca.SingleStaffScoreTemplate.__call__

    """
    return TieCorrectionCommand(
        direction=abjad.Left, selector=selector, untie=True
    )
