import abjad
import collections
import typing
from . import classes
from . import commandclasses
from . import const
from . import indicators
from . import indicatorcommands
from . import overrides
from . import pitchcommands
from . import rhythmcommands
from . import scoping
from . import typings


### FACTORY FUNCTIONS ###


def allow_octaves(
    *, selector: abjad.SelectorTyping = "baca.leaves()"
) -> commandclasses.IndicatorCommand:
    """
    Attaches ALLOW_OCTAVE tag.
    """
    return commandclasses.IndicatorCommand(
        indicators=[abjad.tags.ALLOW_OCTAVE], selector=selector
    )


def bcps(
    bcps,
    *tweaks: abjad.IndexedTweakManager,
    bow_change_tweaks: abjad.IndexedTweakManagers = None,
    final_spanner: bool = None,
    helper: typing.Callable = None,
    selector: abjad.SelectorTyping = "baca.leaves()",
    tag: typing.Optional[str] = "baca.bcps",
) -> commandclasses.BCPCommand:
    r"""
    Makes bow contact point command.

        ..  container:: example

            >>> maker = baca.SegmentMaker(
            ...     score_template=baca.SingleStaffScoreTemplate(),
            ...     spacing=baca.minimum_duration((1, 16)),
            ...     time_signatures=[(4, 8), (3, 8), (4, 8), (3, 8)],
            ...     )

            >>> maker(
            ...     'Music_Voice',
            ...     baca.make_even_divisions(),
            ...     baca.bcps(
            ...         [(1, 5), (3, 5), (2, 5), (4, 5), (5, 5)],
            ...         ),
            ...     baca.pitches('E4 F4'),
            ...     baca.script_staff_padding(5.5),
            ...     baca.text_spanner_staff_padding(2.5),
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
                            % [Global_Skips measure 1]                                                   %! baca.SegmentMaker._comment_measure_numbers()
                            \baca-new-spacing-section #1 #16                                             %! HorizontalSpacingSpecifier(1):SPACING_COMMAND
                            \time 4/8                                                                    %! EXPLICIT_TIME_SIGNATURE:_set_status_tag:baca.SegmentMaker._make_global_skips(2)
                            \baca-time-signature-color #'blue                                            %! EXPLICIT_TIME_SIGNATURE_COLOR:baca.SegmentMaker._attach_color_literal(2)
                            s1 * 1/2                                                                     %! baca.SegmentMaker._make_global_skips(1)
                <BLANKLINE>
                            % [Global_Skips measure 2]                                                   %! baca.SegmentMaker._comment_measure_numbers()
                            \baca-new-spacing-section #1 #16                                             %! HorizontalSpacingSpecifier(1):SPACING_COMMAND
                            \time 3/8                                                                    %! EXPLICIT_TIME_SIGNATURE:_set_status_tag:baca.SegmentMaker._make_global_skips(2)
                            \baca-time-signature-color #'blue                                            %! EXPLICIT_TIME_SIGNATURE_COLOR:baca.SegmentMaker._attach_color_literal(2)
                            s1 * 3/8                                                                     %! baca.SegmentMaker._make_global_skips(1)
                <BLANKLINE>
                            % [Global_Skips measure 3]                                                   %! baca.SegmentMaker._comment_measure_numbers()
                            \baca-new-spacing-section #1 #16                                             %! HorizontalSpacingSpecifier(1):SPACING_COMMAND
                            \time 4/8                                                                    %! EXPLICIT_TIME_SIGNATURE:_set_status_tag:baca.SegmentMaker._make_global_skips(2)
                            \baca-time-signature-color #'blue                                            %! EXPLICIT_TIME_SIGNATURE_COLOR:baca.SegmentMaker._attach_color_literal(2)
                            s1 * 1/2                                                                     %! baca.SegmentMaker._make_global_skips(1)
                <BLANKLINE>
                            % [Global_Skips measure 4]                                                   %! baca.SegmentMaker._comment_measure_numbers()
                            \baca-new-spacing-section #1 #16                                             %! HorizontalSpacingSpecifier(1):SPACING_COMMAND
                            \time 3/8                                                                    %! EXPLICIT_TIME_SIGNATURE:_set_status_tag:baca.SegmentMaker._make_global_skips(2)
                            \baca-time-signature-color #'blue                                            %! EXPLICIT_TIME_SIGNATURE_COLOR:baca.SegmentMaker._attach_color_literal(2)
                            s1 * 3/8                                                                     %! baca.SegmentMaker._make_global_skips(1)
                            \baca-bar-line-visible                                                       %! baca.SegmentMaker._attach_final_bar_line()
                            \bar "|"                                                                     %! baca.SegmentMaker._attach_final_bar_line()
                <BLANKLINE>
                            % [Global_Skips measure 5]                                                   %! PHANTOM:baca.SegmentMaker._style_phantom_measures(1):baca.SegmentMaker._comment_measure_numbers()
                            \baca-new-spacing-section #1 #4                                              %! PHANTOM:baca.SegmentMaker._style_phantom_measures(1):HorizontalSpacingSpecifier(1):SPACING_COMMAND
                            \time 1/4                                                                    %! PHANTOM:baca.SegmentMaker._style_phantom_measures(1):EXPLICIT_TIME_SIGNATURE:_set_status_tag:baca.SegmentMaker._make_global_skips(3)
                            \baca-time-signature-transparent                                             %! PHANTOM:baca.SegmentMaker._style_phantom_measures(2)
                            s1 * 1/4                                                                     %! PHANTOM:baca.SegmentMaker._make_global_skips(3)
                            \once \override Score.BarLine.transparent = ##t                              %! PHANTOM:baca.SegmentMaker._style_phantom_measures(3)
                            \once \override Score.SpanBar.transparent = ##t                              %! PHANTOM:baca.SegmentMaker._style_phantom_measures(3)
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
                                % [Music_Voice measure 1]                                                %! baca.SegmentMaker._comment_measure_numbers()
                                \override Script.staff-padding = #5.5                                    %! baca.script_staff_padding():OverrideCommand(1)
                                \override TextSpanner.staff-padding = #2.5                               %! baca.text_spanner_staff_padding():OverrideCommand(1)
                                e'8                                                                      %! baca.make_even_divisions
                                - \downbow                                                               %! baca.bcps:BCPCommand(6)
                                [                                                                        %! baca.make_even_divisions
                                - \abjad-solid-line-with-arrow                                           %! baca.bcps:BCPCommand(2)
                                - \baca-bcp-spanner-left-text #1 #5                                      %! baca.bcps:BCPCommand(2)
                                \bacaStartTextSpanBCP                                                    %! baca.bcps:BCPCommand(2)
                <BLANKLINE>
                                f'8                                                                      %! baca.make_even_divisions
                                - \upbow                                                                 %! baca.bcps:BCPCommand(7)
                                \bacaStopTextSpanBCP                                                     %! baca.bcps:BCPCommand(3)
                                - \abjad-solid-line-with-arrow                                           %! baca.bcps:BCPCommand(2)
                                - \baca-bcp-spanner-left-text #3 #5                                      %! baca.bcps:BCPCommand(2)
                                \bacaStartTextSpanBCP                                                    %! baca.bcps:BCPCommand(2)
                <BLANKLINE>
                                e'8                                                                      %! baca.make_even_divisions
                                - \downbow                                                               %! baca.bcps:BCPCommand(8)
                                \bacaStopTextSpanBCP                                                     %! baca.bcps:BCPCommand(3)
                                - \abjad-solid-line-with-arrow                                           %! baca.bcps:BCPCommand(2)
                                - \baca-bcp-spanner-left-text #2 #5                                      %! baca.bcps:BCPCommand(2)
                                \bacaStartTextSpanBCP                                                    %! baca.bcps:BCPCommand(2)
                <BLANKLINE>
                                f'8                                                                      %! baca.make_even_divisions
                                \bacaStopTextSpanBCP                                                     %! baca.bcps:BCPCommand(3)
                                ]                                                                        %! baca.make_even_divisions
                                - \abjad-solid-line-with-arrow                                           %! baca.bcps:BCPCommand(2)
                                - \baca-bcp-spanner-left-text #4 #5                                      %! baca.bcps:BCPCommand(2)
                                \bacaStartTextSpanBCP                                                    %! baca.bcps:BCPCommand(2)
                <BLANKLINE>
                                % [Music_Voice measure 2]                                                %! baca.SegmentMaker._comment_measure_numbers()
                                e'8                                                                      %! baca.make_even_divisions
                                - \upbow                                                                 %! baca.bcps:BCPCommand(7)
                                \bacaStopTextSpanBCP                                                     %! baca.bcps:BCPCommand(3)
                                [                                                                        %! baca.make_even_divisions
                                - \abjad-solid-line-with-arrow                                           %! baca.bcps:BCPCommand(2)
                                - \baca-bcp-spanner-left-text #5 #5                                      %! baca.bcps:BCPCommand(2)
                                \bacaStartTextSpanBCP                                                    %! baca.bcps:BCPCommand(2)
                <BLANKLINE>
                                f'8                                                                      %! baca.make_even_divisions
                                - \downbow                                                               %! baca.bcps:BCPCommand(8)
                                \bacaStopTextSpanBCP                                                     %! baca.bcps:BCPCommand(3)
                                - \abjad-solid-line-with-arrow                                           %! baca.bcps:BCPCommand(2)
                                - \baca-bcp-spanner-left-text #1 #5                                      %! baca.bcps:BCPCommand(2)
                                \bacaStartTextSpanBCP                                                    %! baca.bcps:BCPCommand(2)
                <BLANKLINE>
                                e'8                                                                      %! baca.make_even_divisions
                                - \upbow                                                                 %! baca.bcps:BCPCommand(7)
                                \bacaStopTextSpanBCP                                                     %! baca.bcps:BCPCommand(3)
                                ]                                                                        %! baca.make_even_divisions
                                - \abjad-solid-line-with-arrow                                           %! baca.bcps:BCPCommand(2)
                                - \baca-bcp-spanner-left-text #3 #5                                      %! baca.bcps:BCPCommand(2)
                                \bacaStartTextSpanBCP                                                    %! baca.bcps:BCPCommand(2)
                <BLANKLINE>
                                % [Music_Voice measure 3]                                                %! baca.SegmentMaker._comment_measure_numbers()
                                f'8                                                                      %! baca.make_even_divisions
                                - \downbow                                                               %! baca.bcps:BCPCommand(8)
                                \bacaStopTextSpanBCP                                                     %! baca.bcps:BCPCommand(3)
                                [                                                                        %! baca.make_even_divisions
                                - \abjad-solid-line-with-arrow                                           %! baca.bcps:BCPCommand(2)
                                - \baca-bcp-spanner-left-text #2 #5                                      %! baca.bcps:BCPCommand(2)
                                \bacaStartTextSpanBCP                                                    %! baca.bcps:BCPCommand(2)
                <BLANKLINE>
                                e'8                                                                      %! baca.make_even_divisions
                                \bacaStopTextSpanBCP                                                     %! baca.bcps:BCPCommand(3)
                                - \abjad-solid-line-with-arrow                                           %! baca.bcps:BCPCommand(2)
                                - \baca-bcp-spanner-left-text #4 #5                                      %! baca.bcps:BCPCommand(2)
                                \bacaStartTextSpanBCP                                                    %! baca.bcps:BCPCommand(2)
                <BLANKLINE>
                                f'8                                                                      %! baca.make_even_divisions
                                - \upbow                                                                 %! baca.bcps:BCPCommand(7)
                                \bacaStopTextSpanBCP                                                     %! baca.bcps:BCPCommand(3)
                                - \abjad-solid-line-with-arrow                                           %! baca.bcps:BCPCommand(2)
                                - \baca-bcp-spanner-left-text #5 #5                                      %! baca.bcps:BCPCommand(2)
                                \bacaStartTextSpanBCP                                                    %! baca.bcps:BCPCommand(2)
                <BLANKLINE>
                                e'8                                                                      %! baca.make_even_divisions
                                - \downbow                                                               %! baca.bcps:BCPCommand(8)
                                \bacaStopTextSpanBCP                                                     %! baca.bcps:BCPCommand(3)
                                ]                                                                        %! baca.make_even_divisions
                                - \abjad-solid-line-with-arrow                                           %! baca.bcps:BCPCommand(2)
                                - \baca-bcp-spanner-left-text #1 #5                                      %! baca.bcps:BCPCommand(2)
                                \bacaStartTextSpanBCP                                                    %! baca.bcps:BCPCommand(2)
                <BLANKLINE>
                                % [Music_Voice measure 4]                                                %! baca.SegmentMaker._comment_measure_numbers()
                                f'8                                                                      %! baca.make_even_divisions
                                - \upbow                                                                 %! baca.bcps:BCPCommand(7)
                                \bacaStopTextSpanBCP                                                     %! baca.bcps:BCPCommand(3)
                                [                                                                        %! baca.make_even_divisions
                                - \abjad-solid-line-with-arrow                                           %! baca.bcps:BCPCommand(2)
                                - \baca-bcp-spanner-left-text #3 #5                                      %! baca.bcps:BCPCommand(2)
                                \bacaStartTextSpanBCP                                                    %! baca.bcps:BCPCommand(2)
                <BLANKLINE>
                                e'8                                                                      %! baca.make_even_divisions
                                - \downbow                                                               %! baca.bcps:BCPCommand(8)
                                \bacaStopTextSpanBCP                                                     %! baca.bcps:BCPCommand(3)
                                - \abjad-solid-line-with-arrow                                           %! baca.bcps:BCPCommand(2)
                                - \baca-bcp-spanner-left-text #2 #5                                      %! baca.bcps:BCPCommand(2)
                                - \baca-bcp-spanner-right-text #4 #5                                     %! baca.bcps:BCPCommand(2)
                                \bacaStartTextSpanBCP                                                    %! baca.bcps:BCPCommand(2)
                <BLANKLINE>
                                f'8                                                                      %! baca.make_even_divisions
                                \bacaStopTextSpanBCP                                                     %! baca.bcps:BCPCommand(1)
                                ]                                                                        %! baca.make_even_divisions
                                \revert Script.staff-padding                                             %! baca.script_staff_padding():OverrideCommand(2)
                                \revert TextSpanner.staff-padding                                        %! baca.text_spanner_staff_padding():OverrideCommand(2)
                <BLANKLINE>
                                <<                                                                       %! PHANTOM:baca.SegmentMaker._make_multimeasure_rest_container()
                <BLANKLINE>
                                    \context Voice = "Music_Voice"                                       %! PHANTOM:baca.SegmentMaker._make_multimeasure_rest_container()
                                    {                                                                    %! PHANTOM:baca.SegmentMaker._make_multimeasure_rest_container()
                <BLANKLINE>
                                        % [Music_Voice measure 5]                                        %! PHANTOM:baca.SegmentMaker._style_phantom_measures(5):baca.SegmentMaker._comment_measure_numbers()
                                        \baca-invisible-music                                            %! PHANTOM:baca.SegmentMaker._style_phantom_measures(5):baca.SegmentMaker._make_multimeasure_rest_container()
                                        c'1 * 1/4                                                        %! PHANTOM:baca.SegmentMaker._make_multimeasure_rest_container()
                <BLANKLINE>
                                    }                                                                    %! PHANTOM:baca.SegmentMaker._make_multimeasure_rest_container()
                <BLANKLINE>
                                    \context Voice = "Rest_Voice"                                        %! PHANTOM:baca.SegmentMaker._make_multimeasure_rest_container()
                                    {                                                                    %! PHANTOM:baca.SegmentMaker._make_multimeasure_rest_container()
                <BLANKLINE>
                                        % [Rest_Voice measure 5]                                         %! PHANTOM:baca.SegmentMaker._style_phantom_measures(5):baca.SegmentMaker._comment_measure_numbers()
                                        \once \override Score.TimeSignature.X-extent = ##f               %! PHANTOM:baca.SegmentMaker._style_phantom_measures(6)
                                        \once \override MultiMeasureRest.transparent = ##t               %! PHANTOM:baca.SegmentMaker._style_phantom_measures(7)
                                        \stopStaff                                                       %! PHANTOM:baca.SegmentMaker._style_phantom_measures(8)
                                        \once \override Staff.StaffSymbol.transparent = ##t              %! PHANTOM:baca.SegmentMaker._style_phantom_measures(8)
                                        \startStaff                                                      %! PHANTOM:baca.SegmentMaker._style_phantom_measures(8)
                                        R1 * 1/4                                                         %! PHANTOM:baca.SegmentMaker._make_multimeasure_rest_container()
                <BLANKLINE>
                                    }                                                                    %! PHANTOM:baca.SegmentMaker._make_multimeasure_rest_container()
                <BLANKLINE>
                                >>                                                                       %! PHANTOM:baca.SegmentMaker._make_multimeasure_rest_container()
                <BLANKLINE>
                            }                                                                            %! baca.SingleStaffScoreTemplate.__call__
                <BLANKLINE>
                        }                                                                                %! baca.SingleStaffScoreTemplate.__call__
                <BLANKLINE>
                    >>                                                                                   %! baca.SingleStaffScoreTemplate.__call__
                <BLANKLINE>
                >>                                                                                       %! baca.SingleStaffScoreTemplate.__call__

    """
    if final_spanner is not None:
        final_spanner = bool(final_spanner)
    return commandclasses.BCPCommand(
        bcps=bcps,
        bow_change_tweaks=bow_change_tweaks,
        final_spanner=final_spanner,
        helper=helper,
        selector=selector,
        tags=[tag],
        tweaks=tweaks,
    )


def close_volta(
    selector: abjad.SelectorTyping = "baca.leaf(0)",
    *,
    format_slot: str = "before",
) -> scoping.Suite:
    """
    Attaches bar line and overrides bar line X-extent.
    """
    assert format_slot in ("after", "before"), repr(format_slot)
    after = format_slot == "after"
    # does not require not_mol() tagging, just only_mol() tagging:
    return scoping.suite(
        indicatorcommands.bar_line(":|.", selector, format_slot=format_slot),
        scoping.only_mol(
            overrides.bar_line_x_extent((0, 1.5), selector, after=after)
        ),
    )


def color(
    selector: abjad.SelectorTyping = "baca.leaves()"
) -> commandclasses.ColorCommand:
    r"""
    Makes color command.

    :param selector: selector.

    ..  container:: example

        Colors leaves:

        >>> stack = baca.stack(
        ...     baca.figure(
        ...         [1, 1, 5, -1],
        ...         16,
        ...         affix=baca.rests_around([2], [4]),
        ...         restart_talea=True,
        ...         treatments=[-1],
        ...     ),
        ...     rmakers.beam(),
        ...     baca.color(),
        ...     rmakers.unbeam(),
        ...     baca.tuplet_bracket_staff_padding(2),
        ... )
        >>> selection = stack([[0, 2, 10], [18, 16, 15, 20, 19], [9]])
        >>> lilypond_file = abjad.LilyPondFile.rhythm(selection)
        >>> abjad.show(lilypond_file, strict=89) # doctest: +SKIP

        ..  docs::

            >>> abjad.f(lilypond_file[abjad.Score], strict=89)
            \new Score
            <<
                \new GlobalContext
                {
                    \time 11/8
                    s1 * 11/8
                }
                \new Staff
                {
                    \tweak text #tuplet-number::calc-fraction-text
                    \times 9/10 {
                        \override TupletBracket.staff-padding = #2                                   %! baca.tuplet_bracket_staff_padding():OverrideCommand(1)
                        \abjad-color-music #'red
                        r8
                        \abjad-color-music #'blue
                        c'16
                        \abjad-color-music #'red
                        d'16
                        \abjad-color-music #'blue
                        bf'4
                        ~
                        \abjad-color-music #'red
                        bf'16
                        \abjad-color-music #'blue
                        r16
                    }
                    \tweak text #tuplet-number::calc-fraction-text
                    \times 9/10 {
                        \abjad-color-music #'red
                        fs''16
                        \abjad-color-music #'blue
                        e''16
                        \abjad-color-music #'red
                        ef''4
                        ~
                        \abjad-color-music #'blue
                        ef''16
                        \abjad-color-music #'red
                        r16
                        \abjad-color-music #'blue
                        af''16
                        \abjad-color-music #'red
                        g''16
                    }
                    \times 4/5 {
                        \abjad-color-music #'blue
                        a'16
                        \abjad-color-music #'red
                        r4
                        \revert TupletBracket.staff-padding                                          %! baca.tuplet_bracket_staff_padding():OverrideCommand(2)
                    }
                }
            >>

    ..  container:: example

        Colors leaves in tuplet 1:

        >>> stack = baca.stack(
        ...     baca.figure(
        ...         [1, 1, 5, -1],
        ...         16,
        ...         affix=baca.rests_around([2], [4]),
        ...         restart_talea=True,
        ...         treatments=[-1],
        ...     ),
        ...     rmakers.beam(),
        ...     baca.color(baca.tuplets()[1:2].leaves()),
        ...     rmakers.unbeam(),
        ...     baca.tuplet_bracket_staff_padding(2),
        ... )
        >>> selection = stack([[0, 2, 10], [18, 16, 15, 20, 19], [9]])
        >>> lilypond_file = abjad.LilyPondFile.rhythm(selection)
        >>> abjad.show(lilypond_file, strict=89) # doctest: +SKIP

        ..  docs::

            >>> abjad.f(lilypond_file[abjad.Score], strict=89)
            \new Score
            <<
                \new GlobalContext
                {
                    \time 11/8
                    s1 * 11/8
                }
                \new Staff
                {
                    \tweak text #tuplet-number::calc-fraction-text
                    \times 9/10 {
                        \override TupletBracket.staff-padding = #2                                   %! baca.tuplet_bracket_staff_padding():OverrideCommand(1)
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
                        \abjad-color-music #'red
                        fs''16
                        \abjad-color-music #'blue
                        e''16
                        \abjad-color-music #'red
                        ef''4
                        ~
                        \abjad-color-music #'blue
                        ef''16
                        \abjad-color-music #'red
                        r16
                        \abjad-color-music #'blue
                        af''16
                        \abjad-color-music #'red
                        g''16
                    }
                    \times 4/5 {
                        a'16
                        r4
                        \revert TupletBracket.staff-padding                                          %! baca.tuplet_bracket_staff_padding():OverrideCommand(2)
                    }
                }
            >>

    """
    return commandclasses.ColorCommand(selector=selector)


def container(
    identifier: str = None, *, selector: abjad.SelectorTyping = "baca.leaves()"
) -> commandclasses.ContainerCommand:
    r"""
    Makes container with ``identifier`` and extends container with
    ``selector`` output.

    ..  container:: example

        >>> maker = baca.SegmentMaker(
        ...     score_template=baca.SingleStaffScoreTemplate(),
        ...     time_signatures=[(4, 8), (3, 8), (4, 8), (3, 8)],
        ...     )

        >>> maker(
        ...     'Music_Voice',
        ...     baca.container('ViolinI', selector=baca.leaves()[:2]),
        ...     baca.container('ViolinII', selector=baca.leaves()[2:]),
        ...     baca.make_notes(repeat_ties=True),
        ...     baca.pitches('E4 F4'),
        ...     )

        >>> lilypond_file = maker.run(environment='docs')

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
                    % [Global_Skips measure 1]                                                   %! baca.SegmentMaker._comment_measure_numbers()
                    \time 4/8                                                                    %! EXPLICIT_TIME_SIGNATURE:_set_status_tag:baca.SegmentMaker._make_global_skips(2)
                    \baca-time-signature-color #'blue                                            %! EXPLICIT_TIME_SIGNATURE_COLOR:baca.SegmentMaker._attach_color_literal(2)
                    s1 * 1/2                                                                     %! baca.SegmentMaker._make_global_skips(1)
        <BLANKLINE>
                    % [Global_Skips measure 2]                                                   %! baca.SegmentMaker._comment_measure_numbers()
                    \time 3/8                                                                    %! EXPLICIT_TIME_SIGNATURE:_set_status_tag:baca.SegmentMaker._make_global_skips(2)
                    \baca-time-signature-color #'blue                                            %! EXPLICIT_TIME_SIGNATURE_COLOR:baca.SegmentMaker._attach_color_literal(2)
                    s1 * 3/8                                                                     %! baca.SegmentMaker._make_global_skips(1)
        <BLANKLINE>
                    % [Global_Skips measure 3]                                                   %! baca.SegmentMaker._comment_measure_numbers()
                    \time 4/8                                                                    %! EXPLICIT_TIME_SIGNATURE:_set_status_tag:baca.SegmentMaker._make_global_skips(2)
                    \baca-time-signature-color #'blue                                            %! EXPLICIT_TIME_SIGNATURE_COLOR:baca.SegmentMaker._attach_color_literal(2)
                    s1 * 1/2                                                                     %! baca.SegmentMaker._make_global_skips(1)
        <BLANKLINE>
                    % [Global_Skips measure 4]                                                   %! baca.SegmentMaker._comment_measure_numbers()
                    \time 3/8                                                                    %! EXPLICIT_TIME_SIGNATURE:_set_status_tag:baca.SegmentMaker._make_global_skips(2)
                    \baca-time-signature-color #'blue                                            %! EXPLICIT_TIME_SIGNATURE_COLOR:baca.SegmentMaker._attach_color_literal(2)
                    s1 * 3/8                                                                     %! baca.SegmentMaker._make_global_skips(1)
                    \baca-bar-line-visible                                                       %! baca.SegmentMaker._attach_final_bar_line()
                    \bar "|"                                                                     %! baca.SegmentMaker._attach_final_bar_line()
        <BLANKLINE>
                    % [Global_Skips measure 5]                                                   %! PHANTOM:baca.SegmentMaker._style_phantom_measures(1):baca.SegmentMaker._comment_measure_numbers()
                    \time 1/4                                                                    %! PHANTOM:baca.SegmentMaker._style_phantom_measures(1):EXPLICIT_TIME_SIGNATURE:_set_status_tag:baca.SegmentMaker._make_global_skips(3)
                    \baca-time-signature-transparent                                             %! PHANTOM:baca.SegmentMaker._style_phantom_measures(2)
                    s1 * 1/4                                                                     %! PHANTOM:baca.SegmentMaker._make_global_skips(3)
                    \once \override Score.BarLine.transparent = ##t                              %! PHANTOM:baca.SegmentMaker._style_phantom_measures(3)
                    \once \override Score.SpanBar.transparent = ##t                              %! PHANTOM:baca.SegmentMaker._style_phantom_measures(3)
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
                        {   %*% ViolinI
        <BLANKLINE>
                            % [Music_Voice measure 1]                                            %! baca.SegmentMaker._comment_measure_numbers()
                            e'2                                                                  %! baca.make_notes
        <BLANKLINE>
                            % [Music_Voice measure 2]                                            %! baca.SegmentMaker._comment_measure_numbers()
                            f'4.                                                                 %! baca.make_notes
        <BLANKLINE>
                        }   %*% ViolinI
        <BLANKLINE>
                        {   %*% ViolinII
        <BLANKLINE>
                            % [Music_Voice measure 3]                                            %! baca.SegmentMaker._comment_measure_numbers()
                            e'2                                                                  %! baca.make_notes
        <BLANKLINE>
                            % [Music_Voice measure 4]                                            %! baca.SegmentMaker._comment_measure_numbers()
                            f'4.                                                                 %! baca.make_notes
        <BLANKLINE>
                        }   %*% ViolinII
        <BLANKLINE>
                        <<                                                                       %! PHANTOM:baca.SegmentMaker._make_multimeasure_rest_container()
        <BLANKLINE>
                            \context Voice = "Music_Voice"                                       %! PHANTOM:baca.SegmentMaker._make_multimeasure_rest_container()
                            {                                                                    %! PHANTOM:baca.SegmentMaker._make_multimeasure_rest_container()
        <BLANKLINE>
                                % [Music_Voice measure 5]                                        %! PHANTOM:baca.SegmentMaker._style_phantom_measures(5):baca.SegmentMaker._comment_measure_numbers()
                                \baca-invisible-music                                            %! PHANTOM:baca.SegmentMaker._style_phantom_measures(5):baca.SegmentMaker._make_multimeasure_rest_container()
                                c'1 * 1/4                                                        %! PHANTOM:baca.SegmentMaker._make_multimeasure_rest_container()
        <BLANKLINE>
                            }                                                                    %! PHANTOM:baca.SegmentMaker._make_multimeasure_rest_container()
        <BLANKLINE>
                            \context Voice = "Rest_Voice"                                        %! PHANTOM:baca.SegmentMaker._make_multimeasure_rest_container()
                            {                                                                    %! PHANTOM:baca.SegmentMaker._make_multimeasure_rest_container()
        <BLANKLINE>
                                % [Rest_Voice measure 5]                                         %! PHANTOM:baca.SegmentMaker._style_phantom_measures(5):baca.SegmentMaker._comment_measure_numbers()
                                \once \override Score.TimeSignature.X-extent = ##f               %! PHANTOM:baca.SegmentMaker._style_phantom_measures(6)
                                \once \override MultiMeasureRest.transparent = ##t               %! PHANTOM:baca.SegmentMaker._style_phantom_measures(7)
                                \stopStaff                                                       %! PHANTOM:baca.SegmentMaker._style_phantom_measures(8)
                                \once \override Staff.StaffSymbol.transparent = ##t              %! PHANTOM:baca.SegmentMaker._style_phantom_measures(8)
                                \startStaff                                                      %! PHANTOM:baca.SegmentMaker._style_phantom_measures(8)
                                R1 * 1/4                                                         %! PHANTOM:baca.SegmentMaker._make_multimeasure_rest_container()
        <BLANKLINE>
                            }                                                                    %! PHANTOM:baca.SegmentMaker._make_multimeasure_rest_container()
        <BLANKLINE>
                        >>                                                                       %! PHANTOM:baca.SegmentMaker._make_multimeasure_rest_container()
        <BLANKLINE>
                    }                                                                            %! baca.SingleStaffScoreTemplate.__call__
        <BLANKLINE>
                }                                                                                %! baca.SingleStaffScoreTemplate.__call__
        <BLANKLINE>
            >>                                                                                   %! baca.SingleStaffScoreTemplate.__call__
        <BLANKLINE>
        >>                                                                                       %! baca.SingleStaffScoreTemplate.__call__

    """
    if identifier is not None:
        if not isinstance(identifier, str):
            message = f"identifier must be string (not {identifier!r})."
            raise Exception(message)
    return commandclasses.ContainerCommand(
        identifier=identifier, selector=selector
    )


def cross_staff(
    *,
    selector: abjad.SelectorTyping = "baca.phead(0)",
    tag: typing.Optional[str] = "baca.cross_staff",
) -> commandclasses.IndicatorCommand:
    r"""
    Attaches cross-staff command.

    ..  container:: example

        Attaches cross-staff command to last two pitched leaves:

        >>> score_template = baca.StringTrioScoreTemplate()
        >>> accumulator = baca.Accumulator(score_template=score_template)
        >>> commands = [
        ...     baca.figure([1], 8, signature=8),
        ...     rmakers.beam(),
        ... ]
        >>> accumulator(
        ...     'Violin_Music_Voice',
        ...     [[9, 11, 12, 14, 16]],
        ...     *commands,
        ...     rmakers.unbeam(),
        ...     baca.stem_up(),
        ...     figure_name='vn.1',
        ... )
        >>> accumulator(
        ...     'Viola_Music_Voice',
        ...     [[0, 2, 4, 5, 7]],
        ...     *commands,
        ...     baca.cross_staff(selector=baca.pleaves()[-2:]),
        ...     rmakers.unbeam(),
        ...     baca.stem_up(),
        ...     anchor=baca.anchor('Violin_Music_Voice'),
        ...     figure_name='va.1',
        ... )
        >>> accumulator(
        ...     'Violin_Music_Voice',
        ...     [[15]],
        ...     *commands,
        ...     rmakers.unbeam(),
        ...     figure_name='vn.2',
        ... )

        >>> maker = baca.SegmentMaker(
        ...     ignore_repeat_pitch_classes=True,
        ...     do_not_color_unregistered_pitches=True,
        ...     score_template=accumulator.score_template,
        ...     spacing=baca.minimum_duration((1, 12)),
        ...     time_signatures=accumulator.time_signatures,
        ...     )
        >>> accumulator.populate_segment_maker(maker)
        >>> lilypond_file = maker.run(environment='docs')
        >>> abjad.show(lilypond_file, strict=89) # doctest: +SKIP

        ..  docs::

            >>> abjad.f(lilypond_file[abjad.Score], strict=89)
            <BLANKLINE>
            \context Score = "Score"                                                                 %! baca.StringTrioScoreTemplate.__call__
            <<                                                                                       %! baca.StringTrioScoreTemplate.__call__
            <BLANKLINE>
                \context GlobalContext = "Global_Context"                                            %! abjad.ScoreTemplate._make_global_context
                <<                                                                                   %! abjad.ScoreTemplate._make_global_context
            <BLANKLINE>
                    \context GlobalSkips = "Global_Skips"                                            %! abjad.ScoreTemplate._make_global_context
                    {                                                                                %! abjad.ScoreTemplate._make_global_context
            <BLANKLINE>
                        % [Global_Skips measure 1]                                                   %! baca.SegmentMaker._comment_measure_numbers()
                        \baca-new-spacing-section #1 #12                                             %! HorizontalSpacingSpecifier(1):SPACING_COMMAND
                        \time 5/8                                                                    %! EXPLICIT_TIME_SIGNATURE:_set_status_tag:baca.SegmentMaker._make_global_skips(2)
                        \baca-time-signature-color #'blue                                            %! EXPLICIT_TIME_SIGNATURE_COLOR:baca.SegmentMaker._attach_color_literal(2)
                        s1 * 5/8                                                                     %! baca.SegmentMaker._make_global_skips(1)
            <BLANKLINE>
                        % [Global_Skips measure 2]                                                   %! baca.SegmentMaker._comment_measure_numbers()
                        \baca-new-spacing-section #1 #12                                             %! HorizontalSpacingSpecifier(1):SPACING_COMMAND
                        \time 1/8                                                                    %! EXPLICIT_TIME_SIGNATURE:_set_status_tag:baca.SegmentMaker._make_global_skips(2)
                        \baca-time-signature-color #'blue                                            %! EXPLICIT_TIME_SIGNATURE_COLOR:baca.SegmentMaker._attach_color_literal(2)
                        s1 * 1/8                                                                     %! baca.SegmentMaker._make_global_skips(1)
                        \baca-bar-line-visible                                                       %! baca.SegmentMaker._attach_final_bar_line()
                        \bar "|"                                                                     %! baca.SegmentMaker._attach_final_bar_line()
            <BLANKLINE>
                        % [Global_Skips measure 3]                                                   %! PHANTOM:baca.SegmentMaker._style_phantom_measures(1):baca.SegmentMaker._comment_measure_numbers()
                        \baca-new-spacing-section #1 #4                                              %! PHANTOM:baca.SegmentMaker._style_phantom_measures(1):HorizontalSpacingSpecifier(1):SPACING_COMMAND
                        \time 1/4                                                                    %! PHANTOM:baca.SegmentMaker._style_phantom_measures(1):EXPLICIT_TIME_SIGNATURE:_set_status_tag:baca.SegmentMaker._make_global_skips(3)
                        \baca-time-signature-transparent                                             %! PHANTOM:baca.SegmentMaker._style_phantom_measures(2)
                        s1 * 1/4                                                                     %! PHANTOM:baca.SegmentMaker._make_global_skips(3)
                        \once \override Score.BarLine.transparent = ##t                              %! PHANTOM:baca.SegmentMaker._style_phantom_measures(3)
                        \once \override Score.SpanBar.transparent = ##t                              %! PHANTOM:baca.SegmentMaker._style_phantom_measures(3)
            <BLANKLINE>
                    }                                                                                %! abjad.ScoreTemplate._make_global_context
            <BLANKLINE>
                >>                                                                                   %! abjad.ScoreTemplate._make_global_context
            <BLANKLINE>
                \context MusicContext = "Music_Context"                                              %! baca.StringTrioScoreTemplate.__call__
                <<                                                                                   %! baca.StringTrioScoreTemplate.__call__
            <BLANKLINE>
                    \context StringSectionStaffGroup = "String_Section_Staff_Group"                  %! baca.StringTrioScoreTemplate.__call__
                    <<                                                                               %! baca.StringTrioScoreTemplate.__call__
            <BLANKLINE>
                        \tag Violin                                                                  %! baca.ScoreTemplate._attach_liypond_tag
                        \context ViolinMusicStaff = "Violin_Music_Staff"                             %! baca.StringTrioScoreTemplate.__call__
                        {                                                                            %! baca.StringTrioScoreTemplate.__call__
            <BLANKLINE>
                            \context ViolinMusicVoice = "Violin_Music_Voice"                         %! baca.StringTrioScoreTemplate.__call__
                            {                                                                        %! baca.StringTrioScoreTemplate.__call__
            <BLANKLINE>
                                {
            <BLANKLINE>
                                    \scaleDurations #'(1 . 1) {
            <BLANKLINE>
                                        % [Violin_Music_Voice measure 1]                             %! baca.SegmentMaker._comment_measure_numbers()
                                        \override Stem.direction = #up                               %! baca.stem_up():OverrideCommand(1)
                                        \clef "treble"                                               %! DEFAULT_CLEF:_set_status_tag:abjad.ScoreTemplate.attach_defaults
                                        \once \override ViolinMusicStaff.Clef.color = #(x11-color 'DarkViolet) %! DEFAULT_CLEF_COLOR:baca.SegmentMaker._attach_color_literal(2)
                                    %@% \override ViolinMusicStaff.Clef.color = ##f                  %! DEFAULT_CLEF_COLOR_CANCELLATION:baca.SegmentMaker._attach_color_literal(1)
                                        \set ViolinMusicStaff.forceClef = ##t                        %! DEFAULT_CLEF:_set_status_tag:baca.SegmentMaker._treat_persistent_wrapper(2):abjad.ScoreTemplate.attach_defaults
                                        a'8
                                        ^ \baca-default-indicator-markup "(Violin)"                  %! DEFAULT_INSTRUMENT_ALERT:baca.SegmentMaker._attach_latent_indicator_alert()
                                        \override ViolinMusicStaff.Clef.color = #(x11-color 'violet) %! DEFAULT_CLEF_REDRAW_COLOR:baca.SegmentMaker._attach_color_literal(2)
            <BLANKLINE>
                                        b'8
            <BLANKLINE>
                                        c''8
            <BLANKLINE>
                                        d''8
            <BLANKLINE>
                                        e''8
                                        \revert Stem.direction                                       %! baca.stem_up():OverrideCommand(2)
            <BLANKLINE>
                                    }
            <BLANKLINE>
                                }
            <BLANKLINE>
                                {
            <BLANKLINE>
                                    \scaleDurations #'(1 . 1) {
            <BLANKLINE>
                                        % [Violin_Music_Voice measure 2]                             %! baca.SegmentMaker._comment_measure_numbers()
                                        ef''!8
            <BLANKLINE>
                                    }
            <BLANKLINE>
                                }
            <BLANKLINE>
                                <<                                                                   %! PHANTOM:baca.SegmentMaker._make_multimeasure_rest_container()
            <BLANKLINE>
                                    \context Voice = "Violin_Music_Voice"                            %! PHANTOM:baca.SegmentMaker._make_multimeasure_rest_container()
                                    {                                                                %! PHANTOM:baca.SegmentMaker._make_multimeasure_rest_container()
            <BLANKLINE>
                                        % [Violin_Music_Voice measure 3]                             %! PHANTOM:baca.SegmentMaker._style_phantom_measures(5):baca.SegmentMaker._comment_measure_numbers()
                                        \baca-invisible-music                                        %! PHANTOM:baca.SegmentMaker._style_phantom_measures(5):baca.SegmentMaker._make_multimeasure_rest_container()
                                        c'1 * 1/4                                                    %! PHANTOM:baca.SegmentMaker._make_multimeasure_rest_container()
            <BLANKLINE>
                                    }                                                                %! PHANTOM:baca.SegmentMaker._make_multimeasure_rest_container()
            <BLANKLINE>
                                    \context Voice = "Violin_Rest_Voice"                             %! PHANTOM:baca.SegmentMaker._make_multimeasure_rest_container()
                                    {                                                                %! PHANTOM:baca.SegmentMaker._make_multimeasure_rest_container()
            <BLANKLINE>
                                        % [Violin_Rest_Voice measure 3]                              %! PHANTOM:baca.SegmentMaker._style_phantom_measures(5):baca.SegmentMaker._comment_measure_numbers()
                                        \once \override Score.TimeSignature.X-extent = ##f           %! PHANTOM:baca.SegmentMaker._style_phantom_measures(6)
                                        \once \override MultiMeasureRest.transparent = ##t           %! PHANTOM:baca.SegmentMaker._style_phantom_measures(7)
                                        \stopStaff                                                   %! PHANTOM:baca.SegmentMaker._style_phantom_measures(8)
                                        \once \override Staff.StaffSymbol.transparent = ##t          %! PHANTOM:baca.SegmentMaker._style_phantom_measures(8)
                                        \startStaff                                                  %! PHANTOM:baca.SegmentMaker._style_phantom_measures(8)
                                        R1 * 1/4                                                     %! PHANTOM:baca.SegmentMaker._make_multimeasure_rest_container()
            <BLANKLINE>
                                    }                                                                %! PHANTOM:baca.SegmentMaker._make_multimeasure_rest_container()
            <BLANKLINE>
                                >>                                                                   %! PHANTOM:baca.SegmentMaker._make_multimeasure_rest_container()
            <BLANKLINE>
                            }                                                                        %! baca.StringTrioScoreTemplate.__call__
            <BLANKLINE>
                        }                                                                            %! baca.StringTrioScoreTemplate.__call__
            <BLANKLINE>
                        \tag Viola                                                                   %! baca.ScoreTemplate._attach_liypond_tag
                        \context ViolaMusicStaff = "Viola_Music_Staff"                               %! baca.StringTrioScoreTemplate.__call__
                        {                                                                            %! baca.StringTrioScoreTemplate.__call__
            <BLANKLINE>
                            \context ViolaMusicVoice = "Viola_Music_Voice"                           %! baca.StringTrioScoreTemplate.__call__
                            {                                                                        %! baca.StringTrioScoreTemplate.__call__
            <BLANKLINE>
                                {
            <BLANKLINE>
                                    \scaleDurations #'(1 . 1) {
            <BLANKLINE>
                                        % [Viola_Music_Voice measure 1]                              %! baca.SegmentMaker._comment_measure_numbers()
                                        \override Stem.direction = #up                               %! baca.stem_up():OverrideCommand(1)
                                        \clef "alto"                                                 %! DEFAULT_CLEF:_set_status_tag:abjad.ScoreTemplate.attach_defaults
                                        \once \override ViolaMusicStaff.Clef.color = #(x11-color 'DarkViolet) %! DEFAULT_CLEF_COLOR:baca.SegmentMaker._attach_color_literal(2)
                                    %@% \override ViolaMusicStaff.Clef.color = ##f                   %! DEFAULT_CLEF_COLOR_CANCELLATION:baca.SegmentMaker._attach_color_literal(1)
                                        \set ViolaMusicStaff.forceClef = ##t                         %! DEFAULT_CLEF:_set_status_tag:baca.SegmentMaker._treat_persistent_wrapper(2):abjad.ScoreTemplate.attach_defaults
                                        c'8
                                        ^ \baca-default-indicator-markup "(Viola)"                   %! DEFAULT_INSTRUMENT_ALERT:baca.SegmentMaker._attach_latent_indicator_alert()
                                        \override ViolaMusicStaff.Clef.color = #(x11-color 'violet)  %! DEFAULT_CLEF_REDRAW_COLOR:baca.SegmentMaker._attach_color_literal(2)
            <BLANKLINE>
                                        d'8
            <BLANKLINE>
                                        e'8
            <BLANKLINE>
                                        \crossStaff                                                  %! baca.cross_staff:IndicatorCommand
                                        f'8
            <BLANKLINE>
                                        \crossStaff                                                  %! baca.cross_staff:IndicatorCommand
                                        g'8
                                        \revert Stem.direction                                       %! baca.stem_up():OverrideCommand(2)
            <BLANKLINE>
                                    }
            <BLANKLINE>
                                }
            <BLANKLINE>
                                <<                                                                   %! baca.SegmentMaker._make_multimeasure_rest_container()
            <BLANKLINE>
                                    \context Voice = "Viola_Music_Voice"                             %! baca.SegmentMaker._make_multimeasure_rest_container()
                                    {                                                                %! baca.SegmentMaker._make_multimeasure_rest_container()
            <BLANKLINE>
                                        % [Viola_Music_Voice measure 2]                              %! baca.SegmentMaker._comment_measure_numbers()
                                        \baca-invisible-music                                        %! baca.SegmentMaker._make_multimeasure_rest_container()
                                        c'1 * 1/8                                                    %! baca.SegmentMaker._make_multimeasure_rest_container()
            <BLANKLINE>
                                    }                                                                %! baca.SegmentMaker._make_multimeasure_rest_container()
            <BLANKLINE>
                                    \context Voice = "Viola_Rest_Voice"                              %! baca.SegmentMaker._make_multimeasure_rest_container()
                                    {                                                                %! baca.SegmentMaker._make_multimeasure_rest_container()
            <BLANKLINE>
                                        % [Viola_Rest_Voice measure 2]                               %! baca.SegmentMaker._comment_measure_numbers()
                                        R1 * 1/8                                                     %! baca.SegmentMaker._make_multimeasure_rest_container()
            <BLANKLINE>
                                    }                                                                %! baca.SegmentMaker._make_multimeasure_rest_container()
            <BLANKLINE>
                                >>                                                                   %! baca.SegmentMaker._make_multimeasure_rest_container()
            <BLANKLINE>
                                <<                                                                   %! PHANTOM:baca.SegmentMaker._make_multimeasure_rest_container()
            <BLANKLINE>
                                    \context Voice = "Viola_Music_Voice"                             %! PHANTOM:baca.SegmentMaker._make_multimeasure_rest_container()
                                    {                                                                %! PHANTOM:baca.SegmentMaker._make_multimeasure_rest_container()
            <BLANKLINE>
                                        % [Viola_Music_Voice measure 3]                              %! PHANTOM:baca.SegmentMaker._style_phantom_measures(5):baca.SegmentMaker._comment_measure_numbers()
                                        \baca-invisible-music                                        %! PHANTOM:baca.SegmentMaker._style_phantom_measures(5):baca.SegmentMaker._make_multimeasure_rest_container()
                                        R1 * 1/4                                                     %! PHANTOM:baca.SegmentMaker._make_multimeasure_rest_container()
            <BLANKLINE>
                                    }                                                                %! PHANTOM:baca.SegmentMaker._make_multimeasure_rest_container()
            <BLANKLINE>
                                    \context Voice = "Viola_Rest_Voice"                              %! PHANTOM:baca.SegmentMaker._make_multimeasure_rest_container()
                                    {                                                                %! PHANTOM:baca.SegmentMaker._make_multimeasure_rest_container()
            <BLANKLINE>
                                        % [Viola_Rest_Voice measure 3]                               %! PHANTOM:baca.SegmentMaker._style_phantom_measures(5):baca.SegmentMaker._comment_measure_numbers()
                                        \once \override Score.TimeSignature.X-extent = ##f           %! PHANTOM:baca.SegmentMaker._style_phantom_measures(6)
                                        \once \override MultiMeasureRest.transparent = ##t           %! PHANTOM:baca.SegmentMaker._style_phantom_measures(7)
                                        \stopStaff                                                   %! PHANTOM:baca.SegmentMaker._style_phantom_measures(8)
                                        \once \override Staff.StaffSymbol.transparent = ##t          %! PHANTOM:baca.SegmentMaker._style_phantom_measures(8)
                                        \startStaff                                                  %! PHANTOM:baca.SegmentMaker._style_phantom_measures(8)
                                        R1 * 1/4                                                     %! PHANTOM:baca.SegmentMaker._make_multimeasure_rest_container()
            <BLANKLINE>
                                    }                                                                %! PHANTOM:baca.SegmentMaker._make_multimeasure_rest_container()
            <BLANKLINE>
                                >>                                                                   %! PHANTOM:baca.SegmentMaker._make_multimeasure_rest_container()
            <BLANKLINE>
                            }                                                                        %! baca.StringTrioScoreTemplate.__call__
            <BLANKLINE>
                        }                                                                            %! baca.StringTrioScoreTemplate.__call__
            <BLANKLINE>
                        \tag Cello                                                                   %! baca.ScoreTemplate._attach_liypond_tag
                        \context CelloMusicStaff = "Cello_Music_Staff"                               %! baca.StringTrioScoreTemplate.__call__
                        {                                                                            %! baca.StringTrioScoreTemplate.__call__
            <BLANKLINE>
                            \context CelloMusicVoice = "Cello_Music_Voice"                           %! baca.StringTrioScoreTemplate.__call__
                            {                                                                        %! baca.StringTrioScoreTemplate.__call__
            <BLANKLINE>
                                % [Cello_Music_Voice measure 1]                                      %! baca.SegmentMaker._comment_measure_numbers()
                                \clef "bass"                                                         %! DEFAULT_CLEF:_set_status_tag:abjad.ScoreTemplate.attach_defaults
                                \once \override CelloMusicStaff.Clef.color = #(x11-color 'DarkViolet) %! DEFAULT_CLEF_COLOR:baca.SegmentMaker._attach_color_literal(2)
                            %@% \override CelloMusicStaff.Clef.color = ##f                           %! DEFAULT_CLEF_COLOR_CANCELLATION:baca.SegmentMaker._attach_color_literal(1)
                                \set CelloMusicStaff.forceClef = ##t                                 %! DEFAULT_CLEF:_set_status_tag:baca.SegmentMaker._treat_persistent_wrapper(2):abjad.ScoreTemplate.attach_defaults
                                R1 * 5/8                                                             %! _call_rhythm_commands
                                ^ \baca-default-indicator-markup "(Cello)"                           %! DEFAULT_INSTRUMENT_ALERT:baca.SegmentMaker._attach_latent_indicator_alert()
                                \override CelloMusicStaff.Clef.color = #(x11-color 'violet)          %! DEFAULT_CLEF_REDRAW_COLOR:baca.SegmentMaker._attach_color_literal(2)
            <BLANKLINE>
                                % [Cello_Music_Voice measure 2]                                      %! baca.SegmentMaker._comment_measure_numbers()
                                R1 * 1/8                                                             %! _call_rhythm_commands
            <BLANKLINE>
                                <<                                                                   %! PHANTOM:baca.SegmentMaker._make_multimeasure_rest_container()
            <BLANKLINE>
                                    \context Voice = "Cello_Music_Voice"                             %! PHANTOM:baca.SegmentMaker._make_multimeasure_rest_container()
                                    {                                                                %! PHANTOM:baca.SegmentMaker._make_multimeasure_rest_container()
            <BLANKLINE>
                                        % [Cello_Music_Voice measure 3]                              %! PHANTOM:baca.SegmentMaker._style_phantom_measures(5):baca.SegmentMaker._comment_measure_numbers()
                                        \baca-invisible-music                                        %! PHANTOM:baca.SegmentMaker._style_phantom_measures(5):baca.SegmentMaker._make_multimeasure_rest_container()
                                        R1 * 1/4                                                     %! PHANTOM:baca.SegmentMaker._make_multimeasure_rest_container()
            <BLANKLINE>
                                    }                                                                %! PHANTOM:baca.SegmentMaker._make_multimeasure_rest_container()
            <BLANKLINE>
                                    \context Voice = "Cello_Rest_Voice"                              %! PHANTOM:baca.SegmentMaker._make_multimeasure_rest_container()
                                    {                                                                %! PHANTOM:baca.SegmentMaker._make_multimeasure_rest_container()
            <BLANKLINE>
                                        % [Cello_Rest_Voice measure 3]                               %! PHANTOM:baca.SegmentMaker._style_phantom_measures(5):baca.SegmentMaker._comment_measure_numbers()
                                        \once \override Score.TimeSignature.X-extent = ##f           %! PHANTOM:baca.SegmentMaker._style_phantom_measures(6)
                                        \once \override MultiMeasureRest.transparent = ##t           %! PHANTOM:baca.SegmentMaker._style_phantom_measures(7)
                                        \stopStaff                                                   %! PHANTOM:baca.SegmentMaker._style_phantom_measures(8)
                                        \once \override Staff.StaffSymbol.transparent = ##t          %! PHANTOM:baca.SegmentMaker._style_phantom_measures(8)
                                        \startStaff                                                  %! PHANTOM:baca.SegmentMaker._style_phantom_measures(8)
                                        R1 * 1/4                                                     %! PHANTOM:baca.SegmentMaker._make_multimeasure_rest_container()
            <BLANKLINE>
                                    }                                                                %! PHANTOM:baca.SegmentMaker._make_multimeasure_rest_container()
            <BLANKLINE>
                                >>                                                                   %! PHANTOM:baca.SegmentMaker._make_multimeasure_rest_container()
            <BLANKLINE>
                            }                                                                        %! baca.StringTrioScoreTemplate.__call__
            <BLANKLINE>
                        }                                                                            %! baca.StringTrioScoreTemplate.__call__
            <BLANKLINE>
                    >>                                                                               %! baca.StringTrioScoreTemplate.__call__
            <BLANKLINE>
                >>                                                                                   %! baca.StringTrioScoreTemplate.__call__
            <BLANKLINE>
            >>                                                                                       %! baca.StringTrioScoreTemplate.__call__

    """
    return commandclasses.IndicatorCommand(
        indicators=[abjad.LilyPondLiteral(r"\crossStaff")],
        selector=selector,
        tags=[tag],
    )


def double_volta(
    selector: abjad.SelectorTyping = "baca.leaf(0)"
) -> scoping.Suite:
    """
    Attaches bar line and overrides bar line X-extent.
    """
    return scoping.suite(
        indicatorcommands.bar_line(":.|.:", selector, format_slot="before"),
        scoping.not_mol(overrides.bar_line_x_extent((0, 3), selector)),
        scoping.only_mol(overrides.bar_line_x_extent((0, 4), selector)),
    )


def dynamic_down(
    *,
    selector: abjad.SelectorTyping = "baca.leaf(0)",
    tag: typing.Optional[str] = "baca.dynamic_down",
) -> commandclasses.IndicatorCommand:
    r"""
    Attaches dynamic-down command.

    ..  container:: example

        Attaches dynamic-down command to leaf 0:

        >>> stack = baca.stack(
        ...     baca.figure(
        ...         [1, 1, 5, -1],
        ...         16,
        ...         affix=baca.rests_around([2], [4]),
        ...         restart_talea=True,
        ...         treatments=[-1],
        ...     ),
        ...     rmakers.beam(),
        ...     baca.dynamic('p'),
        ...     baca.dynamic('f', selector=baca.tuplets()[1:2].phead(0)),
        ...     baca.dynamic_down(),
        ...     baca.tuplet_bracket_staff_padding(2),
        ... )
        >>> selection = stack([[0, 2, 10], [18, 16, 15, 20, 19], [9]])
        >>> lilypond_file = abjad.LilyPondFile.rhythm(selection)
        >>> abjad.show(lilypond_file, strict=89) # doctest: +SKIP

        ..  docs::

            >>> abjad.f(lilypond_file[abjad.Score], strict=89)
            \new Score
            <<
                \new GlobalContext
                {
                    \time 11/8
                    s1 * 11/8
                }
                \new Staff
                {
                    \tweak text #tuplet-number::calc-fraction-text
                    \times 9/10 {
                        \override TupletBracket.staff-padding = #2                                   %! baca.tuplet_bracket_staff_padding():OverrideCommand(1)
                        \dynamicDown                                                                 %! baca.dynamic_down:IndicatorCommand
                        r8
                        c'16
                        \p                                                                           %! baca.dynamic:IndicatorCommand
                        [
                        d'16
                        ]
                        bf'4
                        ~
                        bf'16
                        r16
                    }
                    \tweak text #tuplet-number::calc-fraction-text
                    \times 9/10 {
                        fs''16
                        \f                                                                           %! baca.dynamic:IndicatorCommand
                        [
                        e''16
                        ]
                        ef''4
                        ~
                        ef''16
                        r16
                        af''16
                        [
                        g''16
                        ]
                    }
                    \times 4/5 {
                        a'16
                        r4
                        \revert TupletBracket.staff-padding                                          %! baca.tuplet_bracket_staff_padding():OverrideCommand(2)
                    }
                }
            >>

    """
    return commandclasses.IndicatorCommand(
        indicators=[abjad.LilyPondLiteral(r"\dynamicDown")],
        selector=selector,
        tags=[tag],
    )


def dynamic_up(
    *,
    selector: abjad.SelectorTyping = "baca.leaf(0)",
    tag: typing.Optional[str] = "baca.dynamic_down",
) -> commandclasses.IndicatorCommand:
    r"""
    Attaches dynamic-up command.

    ..  container:: example

        Attaches dynamic-up command to leaf 0:

        >>> stack = baca.stack(
        ...     baca.figure(
        ...         [1, 1, 5, -1],
        ...         16,
        ...         affix=baca.rests_around([2], [4]),
        ...         restart_talea=True,
        ...         treatments=[-1],
        ...     ),
        ...     rmakers.beam(),
        ...     baca.dynamic('p'),
        ...     baca.dynamic('f', selector=baca.tuplets()[1:2].phead(0)),
        ...     baca.dynamic_up(),
        ...     baca.tuplet_bracket_staff_padding(2),
        ... )
        >>> selection = stack([[0, 2, 10], [18, 16, 15, 20, 19], [9]])
        >>> lilypond_file = abjad.LilyPondFile.rhythm(selection)
        >>> abjad.show(lilypond_file, strict=89) # doctest: +SKIP

        ..  docs::

            >>> abjad.f(lilypond_file[abjad.Score], strict=89)
            \new Score
            <<
                \new GlobalContext
                {
                    \time 11/8
                    s1 * 11/8
                }
                \new Staff
                {
                    \tweak text #tuplet-number::calc-fraction-text
                    \times 9/10 {
                        \override TupletBracket.staff-padding = #2                                   %! baca.tuplet_bracket_staff_padding():OverrideCommand(1)
                        \dynamicUp                                                                   %! baca.dynamic_down:IndicatorCommand
                        r8
                        c'16
                        \p                                                                           %! baca.dynamic:IndicatorCommand
                        [
                        d'16
                        ]
                        bf'4
                        ~
                        bf'16
                        r16
                    }
                    \tweak text #tuplet-number::calc-fraction-text
                    \times 9/10 {
                        fs''16
                        \f                                                                           %! baca.dynamic:IndicatorCommand
                        [
                        e''16
                        ]
                        ef''4
                        ~
                        ef''16
                        r16
                        af''16
                        [
                        g''16
                        ]
                    }
                    \times 4/5 {
                        a'16
                        r4
                        \revert TupletBracket.staff-padding                                          %! baca.tuplet_bracket_staff_padding():OverrideCommand(2)
                    }
                }
            >>

    """
    return commandclasses.IndicatorCommand(
        indicators=[abjad.LilyPondLiteral(r"\dynamicUp")],
        selector=selector,
        tags=[tag],
    )


def edition(
    not_parts: typing.Union[
        str, abjad.Markup, commandclasses.IndicatorCommand
    ],
    only_parts: typing.Union[
        str, abjad.Markup, commandclasses.IndicatorCommand
    ],
) -> scoping.Suite:
    """
    Makes not-parts / only-parts markup suite.
    """
    if isinstance(not_parts, (str, abjad.Markup)):
        not_parts = markup(not_parts)
    assert isinstance(not_parts, commandclasses.IndicatorCommand)
    not_parts_ = scoping.not_parts(not_parts)
    if isinstance(only_parts, (str, abjad.Markup)):
        only_parts = markup(only_parts)
    assert isinstance(only_parts, commandclasses.IndicatorCommand)
    only_parts_ = scoping.only_parts(only_parts)
    return scoping.suite(not_parts_, only_parts_)


def finger_pressure_transition(
    *,
    selector: abjad.SelectorTyping = "baca.tleaves()",
    right_broken: bool = None,
    tag: typing.Optional[str] = "baca.finger_pressure_transition",
) -> commandclasses.GlissandoCommand:
    r"""
    Makes finger pressure transition glissando.

    ..  container:: example

        >>> maker = baca.SegmentMaker(
        ...     score_template=baca.SingleStaffScoreTemplate(),
        ...     spacing=baca.minimum_duration((1, 12)),
        ...     time_signatures=[(4, 8), (3, 8), (4, 8), (3, 8)],
        ...     )

        >>> maker(
        ...     'Music_Voice',
        ...     baca.finger_pressure_transition(selector=baca.notes()[:2]),
        ...     baca.finger_pressure_transition(selector=baca.notes()[2:]),
        ...     baca.make_notes(),
        ...     baca.note_head_style_harmonic(selector=baca.note(0)),
        ...     baca.note_head_style_harmonic(selector=baca.note(2)),
        ...     baca.pitch('C5'),
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
                        % [Global_Skips measure 1]                                                   %! baca.SegmentMaker._comment_measure_numbers()
                        \baca-new-spacing-section #1 #12                                             %! HorizontalSpacingSpecifier(1):SPACING_COMMAND
                        \time 4/8                                                                    %! EXPLICIT_TIME_SIGNATURE:_set_status_tag:baca.SegmentMaker._make_global_skips(2)
                        \baca-time-signature-color #'blue                                            %! EXPLICIT_TIME_SIGNATURE_COLOR:baca.SegmentMaker._attach_color_literal(2)
                        s1 * 1/2                                                                     %! baca.SegmentMaker._make_global_skips(1)
            <BLANKLINE>
                        % [Global_Skips measure 2]                                                   %! baca.SegmentMaker._comment_measure_numbers()
                        \baca-new-spacing-section #1 #12                                             %! HorizontalSpacingSpecifier(1):SPACING_COMMAND
                        \time 3/8                                                                    %! EXPLICIT_TIME_SIGNATURE:_set_status_tag:baca.SegmentMaker._make_global_skips(2)
                        \baca-time-signature-color #'blue                                            %! EXPLICIT_TIME_SIGNATURE_COLOR:baca.SegmentMaker._attach_color_literal(2)
                        s1 * 3/8                                                                     %! baca.SegmentMaker._make_global_skips(1)
            <BLANKLINE>
                        % [Global_Skips measure 3]                                                   %! baca.SegmentMaker._comment_measure_numbers()
                        \baca-new-spacing-section #1 #12                                             %! HorizontalSpacingSpecifier(1):SPACING_COMMAND
                        \time 4/8                                                                    %! EXPLICIT_TIME_SIGNATURE:_set_status_tag:baca.SegmentMaker._make_global_skips(2)
                        \baca-time-signature-color #'blue                                            %! EXPLICIT_TIME_SIGNATURE_COLOR:baca.SegmentMaker._attach_color_literal(2)
                        s1 * 1/2                                                                     %! baca.SegmentMaker._make_global_skips(1)
            <BLANKLINE>
                        % [Global_Skips measure 4]                                                   %! baca.SegmentMaker._comment_measure_numbers()
                        \baca-new-spacing-section #1 #12                                             %! HorizontalSpacingSpecifier(1):SPACING_COMMAND
                        \time 3/8                                                                    %! EXPLICIT_TIME_SIGNATURE:_set_status_tag:baca.SegmentMaker._make_global_skips(2)
                        \baca-time-signature-color #'blue                                            %! EXPLICIT_TIME_SIGNATURE_COLOR:baca.SegmentMaker._attach_color_literal(2)
                        s1 * 3/8                                                                     %! baca.SegmentMaker._make_global_skips(1)
                        \baca-bar-line-visible                                                       %! baca.SegmentMaker._attach_final_bar_line()
                        \bar "|"                                                                     %! baca.SegmentMaker._attach_final_bar_line()
            <BLANKLINE>
                        % [Global_Skips measure 5]                                                   %! PHANTOM:baca.SegmentMaker._style_phantom_measures(1):baca.SegmentMaker._comment_measure_numbers()
                        \baca-new-spacing-section #1 #4                                              %! PHANTOM:baca.SegmentMaker._style_phantom_measures(1):HorizontalSpacingSpecifier(1):SPACING_COMMAND
                        \time 1/4                                                                    %! PHANTOM:baca.SegmentMaker._style_phantom_measures(1):EXPLICIT_TIME_SIGNATURE:_set_status_tag:baca.SegmentMaker._make_global_skips(3)
                        \baca-time-signature-transparent                                             %! PHANTOM:baca.SegmentMaker._style_phantom_measures(2)
                        s1 * 1/4                                                                     %! PHANTOM:baca.SegmentMaker._make_global_skips(3)
                        \once \override Score.BarLine.transparent = ##t                              %! PHANTOM:baca.SegmentMaker._style_phantom_measures(3)
                        \once \override Score.SpanBar.transparent = ##t                              %! PHANTOM:baca.SegmentMaker._style_phantom_measures(3)
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
                            % [Music_Voice measure 1]                                                %! baca.SegmentMaker._comment_measure_numbers()
                            \once \override NoteHead.style = #'harmonic                              %! baca.note_head_style_harmonic():OverrideCommand(1)
                            c''2                                                                     %! baca.make_notes
                            - \tweak arrow-length #2                                                 %! baca.finger_pressure_transition
                            - \tweak arrow-width #0.5                                                %! baca.finger_pressure_transition
                            - \tweak bound-details.right.arrow ##t                                   %! baca.finger_pressure_transition
                            - \tweak thickness #3                                                    %! baca.finger_pressure_transition
                            \glissando                                                               %! baca.finger_pressure_transition
            <BLANKLINE>
                            % [Music_Voice measure 2]                                                %! baca.SegmentMaker._comment_measure_numbers()
                            c''4.                                                                    %! baca.make_notes
            <BLANKLINE>
                            % [Music_Voice measure 3]                                                %! baca.SegmentMaker._comment_measure_numbers()
                            \once \override NoteHead.style = #'harmonic                              %! baca.note_head_style_harmonic():OverrideCommand(1)
                            c''2                                                                     %! baca.make_notes
                            - \tweak arrow-length #2                                                 %! baca.finger_pressure_transition
                            - \tweak arrow-width #0.5                                                %! baca.finger_pressure_transition
                            - \tweak bound-details.right.arrow ##t                                   %! baca.finger_pressure_transition
                            - \tweak thickness #3                                                    %! baca.finger_pressure_transition
                            \glissando                                                               %! baca.finger_pressure_transition
            <BLANKLINE>
                            % [Music_Voice measure 4]                                                %! baca.SegmentMaker._comment_measure_numbers()
                            c''4.                                                                    %! baca.make_notes
            <BLANKLINE>
                            <<                                                                       %! PHANTOM:baca.SegmentMaker._make_multimeasure_rest_container()
            <BLANKLINE>
                                \context Voice = "Music_Voice"                                       %! PHANTOM:baca.SegmentMaker._make_multimeasure_rest_container()
                                {                                                                    %! PHANTOM:baca.SegmentMaker._make_multimeasure_rest_container()
            <BLANKLINE>
                                    % [Music_Voice measure 5]                                        %! PHANTOM:baca.SegmentMaker._style_phantom_measures(5):baca.SegmentMaker._comment_measure_numbers()
                                    \baca-invisible-music                                            %! PHANTOM:baca.SegmentMaker._style_phantom_measures(5):baca.SegmentMaker._make_multimeasure_rest_container()
                                    c'1 * 1/4                                                        %! PHANTOM:baca.SegmentMaker._make_multimeasure_rest_container()
            <BLANKLINE>
                                }                                                                    %! PHANTOM:baca.SegmentMaker._make_multimeasure_rest_container()
            <BLANKLINE>
                                \context Voice = "Rest_Voice"                                        %! PHANTOM:baca.SegmentMaker._make_multimeasure_rest_container()
                                {                                                                    %! PHANTOM:baca.SegmentMaker._make_multimeasure_rest_container()
            <BLANKLINE>
                                    % [Rest_Voice measure 5]                                         %! PHANTOM:baca.SegmentMaker._style_phantom_measures(5):baca.SegmentMaker._comment_measure_numbers()
                                    \once \override Score.TimeSignature.X-extent = ##f               %! PHANTOM:baca.SegmentMaker._style_phantom_measures(6)
                                    \once \override MultiMeasureRest.transparent = ##t               %! PHANTOM:baca.SegmentMaker._style_phantom_measures(7)
                                    \stopStaff                                                       %! PHANTOM:baca.SegmentMaker._style_phantom_measures(8)
                                    \once \override Staff.StaffSymbol.transparent = ##t              %! PHANTOM:baca.SegmentMaker._style_phantom_measures(8)
                                    \startStaff                                                      %! PHANTOM:baca.SegmentMaker._style_phantom_measures(8)
                                    R1 * 1/4                                                         %! PHANTOM:baca.SegmentMaker._make_multimeasure_rest_container()
            <BLANKLINE>
                                }                                                                    %! PHANTOM:baca.SegmentMaker._make_multimeasure_rest_container()
            <BLANKLINE>
                            >>                                                                       %! PHANTOM:baca.SegmentMaker._make_multimeasure_rest_container()
            <BLANKLINE>
                        }                                                                            %! baca.SingleStaffScoreTemplate.__call__
            <BLANKLINE>
                    }                                                                                %! baca.SingleStaffScoreTemplate.__call__
            <BLANKLINE>
                >>                                                                                   %! baca.SingleStaffScoreTemplate.__call__
            <BLANKLINE>
            >>                                                                                       %! baca.SingleStaffScoreTemplate.__call__

    """
    return commandclasses.GlissandoCommand(
        allow_repeats=True,
        right_broken=right_broken,
        selector=selector,
        tags=[tag],
        tweaks=(
            abjad.tweak(2).arrow_length,
            abjad.tweak(0.5).arrow_width,
            abjad.tweak(True).bound_details__right__arrow,
            abjad.tweak(3).thickness,
        ),
    )


def flat_glissando(
    # TODO: allow staff position entry in addition to pitch entry:
    pitch,
    *tweaks,
    hide_middle_stems=None,
    left_broken=None,
    right_broken=None,
    right_broken_show_next=None,
    rleak=None,
    selector="baca.pleaves()",
    stop_pitch=None,
):
    """
    Makes flat glissando.
    """
    # for selector evaluation
    import baca

    if isinstance(selector, str):
        selector = eval(selector)
    if stop_pitch is not None:
        assert pitch is not None
    if rleak:
        selector = selector.rleak()
    commands = []
    command = glissando(
        *tweaks,
        allow_repeats=True,
        allow_ties=True,
        hide_middle_note_heads=True,
        hide_middle_stems=hide_middle_stems,
        left_broken=left_broken,
        right_broken=right_broken,
        right_broken_show_next=right_broken_show_next,
        selector=selector,
    )
    commands.append(command)
    command = untie(selector.leaves())
    commands.append(command)
    if pitch is not None and stop_pitch is None:
        command = pitchcommands.pitch(pitch, selector=selector)
        commands.append(command)
    elif pitch is not None and stop_pitch is not None:
        command = pitchcommands.interpolate_staff_positions(
            pitch, stop_pitch, selector=selector
        )
        commands.append(command)
    return scoping.suite(*commands)


def fractions(items):
    """
    Makes fractions.
    """
    result = []
    for item in items:
        item_ = abjad.NonreducedFraction(item)
        result.append(item_)
    return result


def glissando(
    *tweaks: abjad.IndexedTweakManager,
    allow_repeats: bool = None,
    allow_ties: bool = None,
    hide_middle_note_heads: bool = None,
    hide_middle_stems: bool = None,
    left_broken: bool = None,
    map: abjad.SelectorTyping = None,
    right_broken: bool = None,
    right_broken_show_next: bool = None,
    selector: abjad.SelectorTyping = "baca.tleaves()",
    style: str = None,
    tag: typing.Optional[str] = "baca.glissando",
    zero_padding: bool = None,
) -> commandclasses.GlissandoCommand:
    r"""
    Attaches glissando.

    ..  container:: example

        With segment-maker:

        >>> maker = baca.SegmentMaker(
        ...     score_template=baca.SingleStaffScoreTemplate(),
        ...     time_signatures=[(4, 8), (3, 8), (4, 8), (3, 8)],
        ...     )

        >>> maker(
        ...     'Music_Voice',
        ...     baca.make_even_divisions(),
        ...     baca.pitches('E4 D5 F4 E5 G4 F5'),
        ...     baca.glissando()
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
                        % [Global_Skips measure 1]                                                   %! baca.SegmentMaker._comment_measure_numbers()
                        \time 4/8                                                                    %! EXPLICIT_TIME_SIGNATURE:_set_status_tag:baca.SegmentMaker._make_global_skips(2)
                        \baca-time-signature-color #'blue                                            %! EXPLICIT_TIME_SIGNATURE_COLOR:baca.SegmentMaker._attach_color_literal(2)
                        s1 * 1/2                                                                     %! baca.SegmentMaker._make_global_skips(1)
            <BLANKLINE>
                        % [Global_Skips measure 2]                                                   %! baca.SegmentMaker._comment_measure_numbers()
                        \time 3/8                                                                    %! EXPLICIT_TIME_SIGNATURE:_set_status_tag:baca.SegmentMaker._make_global_skips(2)
                        \baca-time-signature-color #'blue                                            %! EXPLICIT_TIME_SIGNATURE_COLOR:baca.SegmentMaker._attach_color_literal(2)
                        s1 * 3/8                                                                     %! baca.SegmentMaker._make_global_skips(1)
            <BLANKLINE>
                        % [Global_Skips measure 3]                                                   %! baca.SegmentMaker._comment_measure_numbers()
                        \time 4/8                                                                    %! EXPLICIT_TIME_SIGNATURE:_set_status_tag:baca.SegmentMaker._make_global_skips(2)
                        \baca-time-signature-color #'blue                                            %! EXPLICIT_TIME_SIGNATURE_COLOR:baca.SegmentMaker._attach_color_literal(2)
                        s1 * 1/2                                                                     %! baca.SegmentMaker._make_global_skips(1)
            <BLANKLINE>
                        % [Global_Skips measure 4]                                                   %! baca.SegmentMaker._comment_measure_numbers()
                        \time 3/8                                                                    %! EXPLICIT_TIME_SIGNATURE:_set_status_tag:baca.SegmentMaker._make_global_skips(2)
                        \baca-time-signature-color #'blue                                            %! EXPLICIT_TIME_SIGNATURE_COLOR:baca.SegmentMaker._attach_color_literal(2)
                        s1 * 3/8                                                                     %! baca.SegmentMaker._make_global_skips(1)
                        \baca-bar-line-visible                                                       %! baca.SegmentMaker._attach_final_bar_line()
                        \bar "|"                                                                     %! baca.SegmentMaker._attach_final_bar_line()
            <BLANKLINE>
                        % [Global_Skips measure 5]                                                   %! PHANTOM:baca.SegmentMaker._style_phantom_measures(1):baca.SegmentMaker._comment_measure_numbers()
                        \time 1/4                                                                    %! PHANTOM:baca.SegmentMaker._style_phantom_measures(1):EXPLICIT_TIME_SIGNATURE:_set_status_tag:baca.SegmentMaker._make_global_skips(3)
                        \baca-time-signature-transparent                                             %! PHANTOM:baca.SegmentMaker._style_phantom_measures(2)
                        s1 * 1/4                                                                     %! PHANTOM:baca.SegmentMaker._make_global_skips(3)
                        \once \override Score.BarLine.transparent = ##t                              %! PHANTOM:baca.SegmentMaker._style_phantom_measures(3)
                        \once \override Score.SpanBar.transparent = ##t                              %! PHANTOM:baca.SegmentMaker._style_phantom_measures(3)
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
                            % [Music_Voice measure 1]                                                %! baca.SegmentMaker._comment_measure_numbers()
                            e'8                                                                      %! baca.make_even_divisions
                            [                                                                        %! baca.make_even_divisions
                            \glissando                                                               %! baca.glissando
            <BLANKLINE>
                            d''8                                                                     %! baca.make_even_divisions
                            \glissando                                                               %! baca.glissando
            <BLANKLINE>
                            f'8                                                                      %! baca.make_even_divisions
                            \glissando                                                               %! baca.glissando
            <BLANKLINE>
                            e''8                                                                     %! baca.make_even_divisions
                            ]                                                                        %! baca.make_even_divisions
                            \glissando                                                               %! baca.glissando
            <BLANKLINE>
                            % [Music_Voice measure 2]                                                %! baca.SegmentMaker._comment_measure_numbers()
                            g'8                                                                      %! baca.make_even_divisions
                            [                                                                        %! baca.make_even_divisions
                            \glissando                                                               %! baca.glissando
            <BLANKLINE>
                            f''8                                                                     %! baca.make_even_divisions
                            \glissando                                                               %! baca.glissando
            <BLANKLINE>
                            e'8                                                                      %! baca.make_even_divisions
                            ]                                                                        %! baca.make_even_divisions
                            \glissando                                                               %! baca.glissando
            <BLANKLINE>
                            % [Music_Voice measure 3]                                                %! baca.SegmentMaker._comment_measure_numbers()
                            d''8                                                                     %! baca.make_even_divisions
                            [                                                                        %! baca.make_even_divisions
                            \glissando                                                               %! baca.glissando
            <BLANKLINE>
                            f'8                                                                      %! baca.make_even_divisions
                            \glissando                                                               %! baca.glissando
            <BLANKLINE>
                            e''8                                                                     %! baca.make_even_divisions
                            \glissando                                                               %! baca.glissando
            <BLANKLINE>
                            g'8                                                                      %! baca.make_even_divisions
                            ]                                                                        %! baca.make_even_divisions
                            \glissando                                                               %! baca.glissando
            <BLANKLINE>
                            % [Music_Voice measure 4]                                                %! baca.SegmentMaker._comment_measure_numbers()
                            f''8                                                                     %! baca.make_even_divisions
                            [                                                                        %! baca.make_even_divisions
                            \glissando                                                               %! baca.glissando
            <BLANKLINE>
                            e'8                                                                      %! baca.make_even_divisions
                            \glissando                                                               %! baca.glissando
            <BLANKLINE>
                            d''8                                                                     %! baca.make_even_divisions
                            ]                                                                        %! baca.make_even_divisions
            <BLANKLINE>
                            <<                                                                       %! PHANTOM:baca.SegmentMaker._make_multimeasure_rest_container()
            <BLANKLINE>
                                \context Voice = "Music_Voice"                                       %! PHANTOM:baca.SegmentMaker._make_multimeasure_rest_container()
                                {                                                                    %! PHANTOM:baca.SegmentMaker._make_multimeasure_rest_container()
            <BLANKLINE>
                                    % [Music_Voice measure 5]                                        %! PHANTOM:baca.SegmentMaker._style_phantom_measures(5):baca.SegmentMaker._comment_measure_numbers()
                                    \baca-invisible-music                                            %! PHANTOM:baca.SegmentMaker._style_phantom_measures(5):baca.SegmentMaker._make_multimeasure_rest_container()
                                    c'1 * 1/4                                                        %! PHANTOM:baca.SegmentMaker._make_multimeasure_rest_container()
            <BLANKLINE>
                                }                                                                    %! PHANTOM:baca.SegmentMaker._make_multimeasure_rest_container()
            <BLANKLINE>
                                \context Voice = "Rest_Voice"                                        %! PHANTOM:baca.SegmentMaker._make_multimeasure_rest_container()
                                {                                                                    %! PHANTOM:baca.SegmentMaker._make_multimeasure_rest_container()
            <BLANKLINE>
                                    % [Rest_Voice measure 5]                                         %! PHANTOM:baca.SegmentMaker._style_phantom_measures(5):baca.SegmentMaker._comment_measure_numbers()
                                    \once \override Score.TimeSignature.X-extent = ##f               %! PHANTOM:baca.SegmentMaker._style_phantom_measures(6)
                                    \once \override MultiMeasureRest.transparent = ##t               %! PHANTOM:baca.SegmentMaker._style_phantom_measures(7)
                                    \stopStaff                                                       %! PHANTOM:baca.SegmentMaker._style_phantom_measures(8)
                                    \once \override Staff.StaffSymbol.transparent = ##t              %! PHANTOM:baca.SegmentMaker._style_phantom_measures(8)
                                    \startStaff                                                      %! PHANTOM:baca.SegmentMaker._style_phantom_measures(8)
                                    R1 * 1/4                                                         %! PHANTOM:baca.SegmentMaker._make_multimeasure_rest_container()
            <BLANKLINE>
                                }                                                                    %! PHANTOM:baca.SegmentMaker._make_multimeasure_rest_container()
            <BLANKLINE>
                            >>                                                                       %! PHANTOM:baca.SegmentMaker._make_multimeasure_rest_container()
            <BLANKLINE>
                        }                                                                            %! baca.SingleStaffScoreTemplate.__call__
            <BLANKLINE>
                    }                                                                                %! baca.SingleStaffScoreTemplate.__call__
            <BLANKLINE>
                >>                                                                                   %! baca.SingleStaffScoreTemplate.__call__
            <BLANKLINE>
            >>                                                                                       %! baca.SingleStaffScoreTemplate.__call__

    ..  container:: example

        First and last PLTs:

        >>> maker = baca.SegmentMaker(
        ...     score_template=baca.SingleStaffScoreTemplate(),
        ...     time_signatures=[(4, 8), (3, 8), (4, 8), (3, 8)],
        ...     )

        >>> maker(
        ...     'Music_Voice',
        ...     baca.pitches('E4 D5 F4 E5 G4 F5'),
        ...     baca.make_even_divisions(),
        ...     baca.glissando(selector=baca.plts()[:2]),
        ...     baca.glissando(selector=baca.plts()[-2:]),
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
                        % [Global_Skips measure 1]                                                   %! baca.SegmentMaker._comment_measure_numbers()
                        \time 4/8                                                                    %! EXPLICIT_TIME_SIGNATURE:_set_status_tag:baca.SegmentMaker._make_global_skips(2)
                        \baca-time-signature-color #'blue                                            %! EXPLICIT_TIME_SIGNATURE_COLOR:baca.SegmentMaker._attach_color_literal(2)
                        s1 * 1/2                                                                     %! baca.SegmentMaker._make_global_skips(1)
            <BLANKLINE>
                        % [Global_Skips measure 2]                                                   %! baca.SegmentMaker._comment_measure_numbers()
                        \time 3/8                                                                    %! EXPLICIT_TIME_SIGNATURE:_set_status_tag:baca.SegmentMaker._make_global_skips(2)
                        \baca-time-signature-color #'blue                                            %! EXPLICIT_TIME_SIGNATURE_COLOR:baca.SegmentMaker._attach_color_literal(2)
                        s1 * 3/8                                                                     %! baca.SegmentMaker._make_global_skips(1)
            <BLANKLINE>
                        % [Global_Skips measure 3]                                                   %! baca.SegmentMaker._comment_measure_numbers()
                        \time 4/8                                                                    %! EXPLICIT_TIME_SIGNATURE:_set_status_tag:baca.SegmentMaker._make_global_skips(2)
                        \baca-time-signature-color #'blue                                            %! EXPLICIT_TIME_SIGNATURE_COLOR:baca.SegmentMaker._attach_color_literal(2)
                        s1 * 1/2                                                                     %! baca.SegmentMaker._make_global_skips(1)
            <BLANKLINE>
                        % [Global_Skips measure 4]                                                   %! baca.SegmentMaker._comment_measure_numbers()
                        \time 3/8                                                                    %! EXPLICIT_TIME_SIGNATURE:_set_status_tag:baca.SegmentMaker._make_global_skips(2)
                        \baca-time-signature-color #'blue                                            %! EXPLICIT_TIME_SIGNATURE_COLOR:baca.SegmentMaker._attach_color_literal(2)
                        s1 * 3/8                                                                     %! baca.SegmentMaker._make_global_skips(1)
                        \baca-bar-line-visible                                                       %! baca.SegmentMaker._attach_final_bar_line()
                        \bar "|"                                                                     %! baca.SegmentMaker._attach_final_bar_line()
            <BLANKLINE>
                        % [Global_Skips measure 5]                                                   %! PHANTOM:baca.SegmentMaker._style_phantom_measures(1):baca.SegmentMaker._comment_measure_numbers()
                        \time 1/4                                                                    %! PHANTOM:baca.SegmentMaker._style_phantom_measures(1):EXPLICIT_TIME_SIGNATURE:_set_status_tag:baca.SegmentMaker._make_global_skips(3)
                        \baca-time-signature-transparent                                             %! PHANTOM:baca.SegmentMaker._style_phantom_measures(2)
                        s1 * 1/4                                                                     %! PHANTOM:baca.SegmentMaker._make_global_skips(3)
                        \once \override Score.BarLine.transparent = ##t                              %! PHANTOM:baca.SegmentMaker._style_phantom_measures(3)
                        \once \override Score.SpanBar.transparent = ##t                              %! PHANTOM:baca.SegmentMaker._style_phantom_measures(3)
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
                            % [Music_Voice measure 1]                                                %! baca.SegmentMaker._comment_measure_numbers()
                            e'8                                                                      %! baca.make_even_divisions
                            [                                                                        %! baca.make_even_divisions
                            \glissando                                                               %! baca.glissando
            <BLANKLINE>
                            d''8                                                                     %! baca.make_even_divisions
            <BLANKLINE>
                            f'8                                                                      %! baca.make_even_divisions
            <BLANKLINE>
                            e''8                                                                     %! baca.make_even_divisions
                            ]                                                                        %! baca.make_even_divisions
            <BLANKLINE>
                            % [Music_Voice measure 2]                                                %! baca.SegmentMaker._comment_measure_numbers()
                            g'8                                                                      %! baca.make_even_divisions
                            [                                                                        %! baca.make_even_divisions
            <BLANKLINE>
                            f''8                                                                     %! baca.make_even_divisions
            <BLANKLINE>
                            e'8                                                                      %! baca.make_even_divisions
                            ]                                                                        %! baca.make_even_divisions
            <BLANKLINE>
                            % [Music_Voice measure 3]                                                %! baca.SegmentMaker._comment_measure_numbers()
                            d''8                                                                     %! baca.make_even_divisions
                            [                                                                        %! baca.make_even_divisions
            <BLANKLINE>
                            f'8                                                                      %! baca.make_even_divisions
            <BLANKLINE>
                            e''8                                                                     %! baca.make_even_divisions
            <BLANKLINE>
                            g'8                                                                      %! baca.make_even_divisions
                            ]                                                                        %! baca.make_even_divisions
            <BLANKLINE>
                            % [Music_Voice measure 4]                                                %! baca.SegmentMaker._comment_measure_numbers()
                            f''8                                                                     %! baca.make_even_divisions
                            [                                                                        %! baca.make_even_divisions
            <BLANKLINE>
                            e'8                                                                      %! baca.make_even_divisions
                            \glissando                                                               %! baca.glissando
            <BLANKLINE>
                            d''8                                                                     %! baca.make_even_divisions
                            ]                                                                        %! baca.make_even_divisions
            <BLANKLINE>
                            <<                                                                       %! PHANTOM:baca.SegmentMaker._make_multimeasure_rest_container()
            <BLANKLINE>
                                \context Voice = "Music_Voice"                                       %! PHANTOM:baca.SegmentMaker._make_multimeasure_rest_container()
                                {                                                                    %! PHANTOM:baca.SegmentMaker._make_multimeasure_rest_container()
            <BLANKLINE>
                                    % [Music_Voice measure 5]                                        %! PHANTOM:baca.SegmentMaker._style_phantom_measures(5):baca.SegmentMaker._comment_measure_numbers()
                                    \baca-invisible-music                                            %! PHANTOM:baca.SegmentMaker._style_phantom_measures(5):baca.SegmentMaker._make_multimeasure_rest_container()
                                    c'1 * 1/4                                                        %! PHANTOM:baca.SegmentMaker._make_multimeasure_rest_container()
            <BLANKLINE>
                                }                                                                    %! PHANTOM:baca.SegmentMaker._make_multimeasure_rest_container()
            <BLANKLINE>
                                \context Voice = "Rest_Voice"                                        %! PHANTOM:baca.SegmentMaker._make_multimeasure_rest_container()
                                {                                                                    %! PHANTOM:baca.SegmentMaker._make_multimeasure_rest_container()
            <BLANKLINE>
                                    % [Rest_Voice measure 5]                                         %! PHANTOM:baca.SegmentMaker._style_phantom_measures(5):baca.SegmentMaker._comment_measure_numbers()
                                    \once \override Score.TimeSignature.X-extent = ##f               %! PHANTOM:baca.SegmentMaker._style_phantom_measures(6)
                                    \once \override MultiMeasureRest.transparent = ##t               %! PHANTOM:baca.SegmentMaker._style_phantom_measures(7)
                                    \stopStaff                                                       %! PHANTOM:baca.SegmentMaker._style_phantom_measures(8)
                                    \once \override Staff.StaffSymbol.transparent = ##t              %! PHANTOM:baca.SegmentMaker._style_phantom_measures(8)
                                    \startStaff                                                      %! PHANTOM:baca.SegmentMaker._style_phantom_measures(8)
                                    R1 * 1/4                                                         %! PHANTOM:baca.SegmentMaker._make_multimeasure_rest_container()
            <BLANKLINE>
                                }                                                                    %! PHANTOM:baca.SegmentMaker._make_multimeasure_rest_container()
            <BLANKLINE>
                            >>                                                                       %! PHANTOM:baca.SegmentMaker._make_multimeasure_rest_container()
            <BLANKLINE>
                        }                                                                            %! baca.SingleStaffScoreTemplate.__call__
            <BLANKLINE>
                    }                                                                                %! baca.SingleStaffScoreTemplate.__call__
            <BLANKLINE>
                >>                                                                                   %! baca.SingleStaffScoreTemplate.__call__
            <BLANKLINE>
            >>                                                                                       %! baca.SingleStaffScoreTemplate.__call__

    ..  container:: example

        Works with tweaks:

        >>> maker = baca.SegmentMaker(
        ...     score_template=baca.SingleStaffScoreTemplate(),
        ...     time_signatures=[(4, 8), (3, 8), (4, 8), (3, 8)],
        ...     )

        >>> maker(
        ...     'Music_Voice',
        ...     baca.make_even_divisions(),
        ...     baca.pitches('E4 D5 F4 E5 G4 F5'),
        ...     baca.glissando(
        ...         abjad.tweak('red').color,
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
                        % [Global_Skips measure 1]                                                   %! baca.SegmentMaker._comment_measure_numbers()
                        \time 4/8                                                                    %! EXPLICIT_TIME_SIGNATURE:_set_status_tag:baca.SegmentMaker._make_global_skips(2)
                        \baca-time-signature-color #'blue                                            %! EXPLICIT_TIME_SIGNATURE_COLOR:baca.SegmentMaker._attach_color_literal(2)
                        s1 * 1/2                                                                     %! baca.SegmentMaker._make_global_skips(1)
            <BLANKLINE>
                        % [Global_Skips measure 2]                                                   %! baca.SegmentMaker._comment_measure_numbers()
                        \time 3/8                                                                    %! EXPLICIT_TIME_SIGNATURE:_set_status_tag:baca.SegmentMaker._make_global_skips(2)
                        \baca-time-signature-color #'blue                                            %! EXPLICIT_TIME_SIGNATURE_COLOR:baca.SegmentMaker._attach_color_literal(2)
                        s1 * 3/8                                                                     %! baca.SegmentMaker._make_global_skips(1)
            <BLANKLINE>
                        % [Global_Skips measure 3]                                                   %! baca.SegmentMaker._comment_measure_numbers()
                        \time 4/8                                                                    %! EXPLICIT_TIME_SIGNATURE:_set_status_tag:baca.SegmentMaker._make_global_skips(2)
                        \baca-time-signature-color #'blue                                            %! EXPLICIT_TIME_SIGNATURE_COLOR:baca.SegmentMaker._attach_color_literal(2)
                        s1 * 1/2                                                                     %! baca.SegmentMaker._make_global_skips(1)
            <BLANKLINE>
                        % [Global_Skips measure 4]                                                   %! baca.SegmentMaker._comment_measure_numbers()
                        \time 3/8                                                                    %! EXPLICIT_TIME_SIGNATURE:_set_status_tag:baca.SegmentMaker._make_global_skips(2)
                        \baca-time-signature-color #'blue                                            %! EXPLICIT_TIME_SIGNATURE_COLOR:baca.SegmentMaker._attach_color_literal(2)
                        s1 * 3/8                                                                     %! baca.SegmentMaker._make_global_skips(1)
                        \baca-bar-line-visible                                                       %! baca.SegmentMaker._attach_final_bar_line()
                        \bar "|"                                                                     %! baca.SegmentMaker._attach_final_bar_line()
            <BLANKLINE>
                        % [Global_Skips measure 5]                                                   %! PHANTOM:baca.SegmentMaker._style_phantom_measures(1):baca.SegmentMaker._comment_measure_numbers()
                        \time 1/4                                                                    %! PHANTOM:baca.SegmentMaker._style_phantom_measures(1):EXPLICIT_TIME_SIGNATURE:_set_status_tag:baca.SegmentMaker._make_global_skips(3)
                        \baca-time-signature-transparent                                             %! PHANTOM:baca.SegmentMaker._style_phantom_measures(2)
                        s1 * 1/4                                                                     %! PHANTOM:baca.SegmentMaker._make_global_skips(3)
                        \once \override Score.BarLine.transparent = ##t                              %! PHANTOM:baca.SegmentMaker._style_phantom_measures(3)
                        \once \override Score.SpanBar.transparent = ##t                              %! PHANTOM:baca.SegmentMaker._style_phantom_measures(3)
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
                            % [Music_Voice measure 1]                                                %! baca.SegmentMaker._comment_measure_numbers()
                            e'8                                                                      %! baca.make_even_divisions
                            [                                                                        %! baca.make_even_divisions
                            - \tweak color #red                                                      %! baca.glissando
                            \glissando                                                               %! baca.glissando
            <BLANKLINE>
                            d''8                                                                     %! baca.make_even_divisions
                            - \tweak color #red                                                      %! baca.glissando
                            \glissando                                                               %! baca.glissando
            <BLANKLINE>
                            f'8                                                                      %! baca.make_even_divisions
                            - \tweak color #red                                                      %! baca.glissando
                            \glissando                                                               %! baca.glissando
            <BLANKLINE>
                            e''8                                                                     %! baca.make_even_divisions
                            ]                                                                        %! baca.make_even_divisions
                            - \tweak color #red                                                      %! baca.glissando
                            \glissando                                                               %! baca.glissando
            <BLANKLINE>
                            % [Music_Voice measure 2]                                                %! baca.SegmentMaker._comment_measure_numbers()
                            g'8                                                                      %! baca.make_even_divisions
                            [                                                                        %! baca.make_even_divisions
                            - \tweak color #red                                                      %! baca.glissando
                            \glissando                                                               %! baca.glissando
            <BLANKLINE>
                            f''8                                                                     %! baca.make_even_divisions
                            - \tweak color #red                                                      %! baca.glissando
                            \glissando                                                               %! baca.glissando
            <BLANKLINE>
                            e'8                                                                      %! baca.make_even_divisions
                            ]                                                                        %! baca.make_even_divisions
                            - \tweak color #red                                                      %! baca.glissando
                            \glissando                                                               %! baca.glissando
            <BLANKLINE>
                            % [Music_Voice measure 3]                                                %! baca.SegmentMaker._comment_measure_numbers()
                            d''8                                                                     %! baca.make_even_divisions
                            [                                                                        %! baca.make_even_divisions
                            - \tweak color #red                                                      %! baca.glissando
                            \glissando                                                               %! baca.glissando
            <BLANKLINE>
                            f'8                                                                      %! baca.make_even_divisions
                            - \tweak color #red                                                      %! baca.glissando
                            \glissando                                                               %! baca.glissando
            <BLANKLINE>
                            e''8                                                                     %! baca.make_even_divisions
                            - \tweak color #red                                                      %! baca.glissando
                            \glissando                                                               %! baca.glissando
            <BLANKLINE>
                            g'8                                                                      %! baca.make_even_divisions
                            ]                                                                        %! baca.make_even_divisions
                            - \tweak color #red                                                      %! baca.glissando
                            \glissando                                                               %! baca.glissando
            <BLANKLINE>
                            % [Music_Voice measure 4]                                                %! baca.SegmentMaker._comment_measure_numbers()
                            f''8                                                                     %! baca.make_even_divisions
                            [                                                                        %! baca.make_even_divisions
                            - \tweak color #red                                                      %! baca.glissando
                            \glissando                                                               %! baca.glissando
            <BLANKLINE>
                            e'8                                                                      %! baca.make_even_divisions
                            - \tweak color #red                                                      %! baca.glissando
                            \glissando                                                               %! baca.glissando
            <BLANKLINE>
                            d''8                                                                     %! baca.make_even_divisions
                            ]                                                                        %! baca.make_even_divisions
            <BLANKLINE>
                            <<                                                                       %! PHANTOM:baca.SegmentMaker._make_multimeasure_rest_container()
            <BLANKLINE>
                                \context Voice = "Music_Voice"                                       %! PHANTOM:baca.SegmentMaker._make_multimeasure_rest_container()
                                {                                                                    %! PHANTOM:baca.SegmentMaker._make_multimeasure_rest_container()
            <BLANKLINE>
                                    % [Music_Voice measure 5]                                        %! PHANTOM:baca.SegmentMaker._style_phantom_measures(5):baca.SegmentMaker._comment_measure_numbers()
                                    \baca-invisible-music                                            %! PHANTOM:baca.SegmentMaker._style_phantom_measures(5):baca.SegmentMaker._make_multimeasure_rest_container()
                                    c'1 * 1/4                                                        %! PHANTOM:baca.SegmentMaker._make_multimeasure_rest_container()
            <BLANKLINE>
                                }                                                                    %! PHANTOM:baca.SegmentMaker._make_multimeasure_rest_container()
            <BLANKLINE>
                                \context Voice = "Rest_Voice"                                        %! PHANTOM:baca.SegmentMaker._make_multimeasure_rest_container()
                                {                                                                    %! PHANTOM:baca.SegmentMaker._make_multimeasure_rest_container()
            <BLANKLINE>
                                    % [Rest_Voice measure 5]                                         %! PHANTOM:baca.SegmentMaker._style_phantom_measures(5):baca.SegmentMaker._comment_measure_numbers()
                                    \once \override Score.TimeSignature.X-extent = ##f               %! PHANTOM:baca.SegmentMaker._style_phantom_measures(6)
                                    \once \override MultiMeasureRest.transparent = ##t               %! PHANTOM:baca.SegmentMaker._style_phantom_measures(7)
                                    \stopStaff                                                       %! PHANTOM:baca.SegmentMaker._style_phantom_measures(8)
                                    \once \override Staff.StaffSymbol.transparent = ##t              %! PHANTOM:baca.SegmentMaker._style_phantom_measures(8)
                                    \startStaff                                                      %! PHANTOM:baca.SegmentMaker._style_phantom_measures(8)
                                    R1 * 1/4                                                         %! PHANTOM:baca.SegmentMaker._make_multimeasure_rest_container()
            <BLANKLINE>
                                }                                                                    %! PHANTOM:baca.SegmentMaker._make_multimeasure_rest_container()
            <BLANKLINE>
                            >>                                                                       %! PHANTOM:baca.SegmentMaker._make_multimeasure_rest_container()
            <BLANKLINE>
                        }                                                                            %! baca.SingleStaffScoreTemplate.__call__
            <BLANKLINE>
                    }                                                                                %! baca.SingleStaffScoreTemplate.__call__
            <BLANKLINE>
                >>                                                                                   %! baca.SingleStaffScoreTemplate.__call__
            <BLANKLINE>
            >>                                                                                       %! baca.SingleStaffScoreTemplate.__call__

    ..  container:: example

        Works with indexed tweaks:

        >>> maker = baca.SegmentMaker(
        ...     score_template=baca.SingleStaffScoreTemplate(),
        ...     time_signatures=[(4, 8), (3, 8), (4, 8), (3, 8)],
        ...     )

        >>> maker(
        ...     'Music_Voice',
        ...     baca.make_even_divisions(),
        ...     baca.pitches('E4 D5 F4 E5 G4 F5'),
        ...     baca.glissando(
        ...         (abjad.tweak('red').color, 0),
        ...         (abjad.tweak('red').color, -1),
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
                        % [Global_Skips measure 1]                                                   %! baca.SegmentMaker._comment_measure_numbers()
                        \time 4/8                                                                    %! EXPLICIT_TIME_SIGNATURE:_set_status_tag:baca.SegmentMaker._make_global_skips(2)
                        \baca-time-signature-color #'blue                                            %! EXPLICIT_TIME_SIGNATURE_COLOR:baca.SegmentMaker._attach_color_literal(2)
                        s1 * 1/2                                                                     %! baca.SegmentMaker._make_global_skips(1)
            <BLANKLINE>
                        % [Global_Skips measure 2]                                                   %! baca.SegmentMaker._comment_measure_numbers()
                        \time 3/8                                                                    %! EXPLICIT_TIME_SIGNATURE:_set_status_tag:baca.SegmentMaker._make_global_skips(2)
                        \baca-time-signature-color #'blue                                            %! EXPLICIT_TIME_SIGNATURE_COLOR:baca.SegmentMaker._attach_color_literal(2)
                        s1 * 3/8                                                                     %! baca.SegmentMaker._make_global_skips(1)
            <BLANKLINE>
                        % [Global_Skips measure 3]                                                   %! baca.SegmentMaker._comment_measure_numbers()
                        \time 4/8                                                                    %! EXPLICIT_TIME_SIGNATURE:_set_status_tag:baca.SegmentMaker._make_global_skips(2)
                        \baca-time-signature-color #'blue                                            %! EXPLICIT_TIME_SIGNATURE_COLOR:baca.SegmentMaker._attach_color_literal(2)
                        s1 * 1/2                                                                     %! baca.SegmentMaker._make_global_skips(1)
            <BLANKLINE>
                        % [Global_Skips measure 4]                                                   %! baca.SegmentMaker._comment_measure_numbers()
                        \time 3/8                                                                    %! EXPLICIT_TIME_SIGNATURE:_set_status_tag:baca.SegmentMaker._make_global_skips(2)
                        \baca-time-signature-color #'blue                                            %! EXPLICIT_TIME_SIGNATURE_COLOR:baca.SegmentMaker._attach_color_literal(2)
                        s1 * 3/8                                                                     %! baca.SegmentMaker._make_global_skips(1)
                        \baca-bar-line-visible                                                       %! baca.SegmentMaker._attach_final_bar_line()
                        \bar "|"                                                                     %! baca.SegmentMaker._attach_final_bar_line()
            <BLANKLINE>
                        % [Global_Skips measure 5]                                                   %! PHANTOM:baca.SegmentMaker._style_phantom_measures(1):baca.SegmentMaker._comment_measure_numbers()
                        \time 1/4                                                                    %! PHANTOM:baca.SegmentMaker._style_phantom_measures(1):EXPLICIT_TIME_SIGNATURE:_set_status_tag:baca.SegmentMaker._make_global_skips(3)
                        \baca-time-signature-transparent                                             %! PHANTOM:baca.SegmentMaker._style_phantom_measures(2)
                        s1 * 1/4                                                                     %! PHANTOM:baca.SegmentMaker._make_global_skips(3)
                        \once \override Score.BarLine.transparent = ##t                              %! PHANTOM:baca.SegmentMaker._style_phantom_measures(3)
                        \once \override Score.SpanBar.transparent = ##t                              %! PHANTOM:baca.SegmentMaker._style_phantom_measures(3)
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
                            % [Music_Voice measure 1]                                                %! baca.SegmentMaker._comment_measure_numbers()
                            e'8                                                                      %! baca.make_even_divisions
                            [                                                                        %! baca.make_even_divisions
                            - \tweak color #red                                                      %! baca.glissando
                            \glissando                                                               %! baca.glissando
            <BLANKLINE>
                            d''8                                                                     %! baca.make_even_divisions
                            \glissando                                                               %! baca.glissando
            <BLANKLINE>
                            f'8                                                                      %! baca.make_even_divisions
                            \glissando                                                               %! baca.glissando
            <BLANKLINE>
                            e''8                                                                     %! baca.make_even_divisions
                            ]                                                                        %! baca.make_even_divisions
                            \glissando                                                               %! baca.glissando
            <BLANKLINE>
                            % [Music_Voice measure 2]                                                %! baca.SegmentMaker._comment_measure_numbers()
                            g'8                                                                      %! baca.make_even_divisions
                            [                                                                        %! baca.make_even_divisions
                            \glissando                                                               %! baca.glissando
            <BLANKLINE>
                            f''8                                                                     %! baca.make_even_divisions
                            \glissando                                                               %! baca.glissando
            <BLANKLINE>
                            e'8                                                                      %! baca.make_even_divisions
                            ]                                                                        %! baca.make_even_divisions
                            \glissando                                                               %! baca.glissando
            <BLANKLINE>
                            % [Music_Voice measure 3]                                                %! baca.SegmentMaker._comment_measure_numbers()
                            d''8                                                                     %! baca.make_even_divisions
                            [                                                                        %! baca.make_even_divisions
                            \glissando                                                               %! baca.glissando
            <BLANKLINE>
                            f'8                                                                      %! baca.make_even_divisions
                            \glissando                                                               %! baca.glissando
            <BLANKLINE>
                            e''8                                                                     %! baca.make_even_divisions
                            \glissando                                                               %! baca.glissando
            <BLANKLINE>
                            g'8                                                                      %! baca.make_even_divisions
                            ]                                                                        %! baca.make_even_divisions
                            \glissando                                                               %! baca.glissando
            <BLANKLINE>
                            % [Music_Voice measure 4]                                                %! baca.SegmentMaker._comment_measure_numbers()
                            f''8                                                                     %! baca.make_even_divisions
                            [                                                                        %! baca.make_even_divisions
                            \glissando                                                               %! baca.glissando
            <BLANKLINE>
                            e'8                                                                      %! baca.make_even_divisions
                            - \tweak color #red                                                      %! baca.glissando
                            \glissando                                                               %! baca.glissando
            <BLANKLINE>
                            d''8                                                                     %! baca.make_even_divisions
                            ]                                                                        %! baca.make_even_divisions
            <BLANKLINE>
                            <<                                                                       %! PHANTOM:baca.SegmentMaker._make_multimeasure_rest_container()
            <BLANKLINE>
                                \context Voice = "Music_Voice"                                       %! PHANTOM:baca.SegmentMaker._make_multimeasure_rest_container()
                                {                                                                    %! PHANTOM:baca.SegmentMaker._make_multimeasure_rest_container()
            <BLANKLINE>
                                    % [Music_Voice measure 5]                                        %! PHANTOM:baca.SegmentMaker._style_phantom_measures(5):baca.SegmentMaker._comment_measure_numbers()
                                    \baca-invisible-music                                            %! PHANTOM:baca.SegmentMaker._style_phantom_measures(5):baca.SegmentMaker._make_multimeasure_rest_container()
                                    c'1 * 1/4                                                        %! PHANTOM:baca.SegmentMaker._make_multimeasure_rest_container()
            <BLANKLINE>
                                }                                                                    %! PHANTOM:baca.SegmentMaker._make_multimeasure_rest_container()
            <BLANKLINE>
                                \context Voice = "Rest_Voice"                                        %! PHANTOM:baca.SegmentMaker._make_multimeasure_rest_container()
                                {                                                                    %! PHANTOM:baca.SegmentMaker._make_multimeasure_rest_container()
            <BLANKLINE>
                                    % [Rest_Voice measure 5]                                         %! PHANTOM:baca.SegmentMaker._style_phantom_measures(5):baca.SegmentMaker._comment_measure_numbers()
                                    \once \override Score.TimeSignature.X-extent = ##f               %! PHANTOM:baca.SegmentMaker._style_phantom_measures(6)
                                    \once \override MultiMeasureRest.transparent = ##t               %! PHANTOM:baca.SegmentMaker._style_phantom_measures(7)
                                    \stopStaff                                                       %! PHANTOM:baca.SegmentMaker._style_phantom_measures(8)
                                    \once \override Staff.StaffSymbol.transparent = ##t              %! PHANTOM:baca.SegmentMaker._style_phantom_measures(8)
                                    \startStaff                                                      %! PHANTOM:baca.SegmentMaker._style_phantom_measures(8)
                                    R1 * 1/4                                                         %! PHANTOM:baca.SegmentMaker._make_multimeasure_rest_container()
            <BLANKLINE>
                                }                                                                    %! PHANTOM:baca.SegmentMaker._make_multimeasure_rest_container()
            <BLANKLINE>
                            >>                                                                       %! PHANTOM:baca.SegmentMaker._make_multimeasure_rest_container()
            <BLANKLINE>
                        }                                                                            %! baca.SingleStaffScoreTemplate.__call__
            <BLANKLINE>
                    }                                                                                %! baca.SingleStaffScoreTemplate.__call__
            <BLANKLINE>
                >>                                                                                   %! baca.SingleStaffScoreTemplate.__call__
            <BLANKLINE>
            >>                                                                                       %! baca.SingleStaffScoreTemplate.__call__

    """
    return commandclasses.GlissandoCommand(
        allow_repeats=allow_repeats,
        allow_ties=allow_ties,
        hide_middle_note_heads=hide_middle_note_heads,
        hide_middle_stems=hide_middle_stems,
        left_broken=left_broken,
        map=map,
        right_broken=right_broken,
        right_broken_show_next=right_broken_show_next,
        selector=selector,
        tags=[tag],
        tweaks=tweaks,
        zero_padding=zero_padding,
    )


def global_fermata(
    description: str = "fermata",
    selector: abjad.SelectorTyping = "baca.leaf(0)",
    *,
    tag: typing.Optional[str] = "baca.global_fermata",
) -> commandclasses.GlobalFermataCommand:
    """
    Attaches global fermata.
    """
    fermatas = (
        commandclasses.GlobalFermataCommand.description_to_command.keys()
    )
    if description not in fermatas:
        message = f"must be in {repr(', '.join(fermatas))}:\n"
        message += f"   {repr(description)}"
        raise Exception(message)
    return commandclasses.GlobalFermataCommand(
        description=description, selector=selector, tags=[tag]
    )


def instrument(
    instrument: abjad.Instrument,
    *,
    selector: abjad.SelectorTyping = "baca.leaf(0)",
    tag: typing.Optional[str] = "baca.instrument",
) -> commandclasses.InstrumentChangeCommand:
    """
    Makes instrument change command.
    """
    if not isinstance(instrument, abjad.Instrument):
        message = f"instrument must be instrument (not {instrument!r})."
        raise Exception(message)
    return commandclasses.InstrumentChangeCommand(
        indicators=[instrument], selector=selector, tags=[tag]
    )


def invisible_music(
    selector: abjad.SelectorTyping = "baca.leaf(0)",
    *,
    map: abjad.SelectorTyping = None,
    tag: typing.Optional[str] = "baca.invisible_music",
) -> commandclasses.IndicatorCommand:
    r"""
    Attaches ``\baca-invisible-music`` literal.

    ..  container:: example

        Attaches ``\baca-invisible-music`` literal to middle leaves:

        >>> maker = baca.SegmentMaker(
        ...     score_template=baca.SingleStaffScoreTemplate(),
        ...     spacing=baca.minimum_duration((1, 12)),
        ...     time_signatures=[(4, 8), (3, 8), (4, 8), (3, 8)],
        ...     )

        >>> maker(
        ...     'Music_Voice',
        ...     baca.invisible_music(
        ...         selector=baca.leaves()[1:-1],
        ...         ),
        ...     baca.make_notes(),
        ...     baca.pitch('C5'),
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
                        % [Global_Skips measure 1]                                                   %! baca.SegmentMaker._comment_measure_numbers()
                        \baca-new-spacing-section #1 #12                                             %! HorizontalSpacingSpecifier(1):SPACING_COMMAND
                        \time 4/8                                                                    %! EXPLICIT_TIME_SIGNATURE:_set_status_tag:baca.SegmentMaker._make_global_skips(2)
                        \baca-time-signature-color #'blue                                            %! EXPLICIT_TIME_SIGNATURE_COLOR:baca.SegmentMaker._attach_color_literal(2)
                        s1 * 1/2                                                                     %! baca.SegmentMaker._make_global_skips(1)
            <BLANKLINE>
                        % [Global_Skips measure 2]                                                   %! baca.SegmentMaker._comment_measure_numbers()
                        \baca-new-spacing-section #1 #12                                             %! HorizontalSpacingSpecifier(1):SPACING_COMMAND
                        \time 3/8                                                                    %! EXPLICIT_TIME_SIGNATURE:_set_status_tag:baca.SegmentMaker._make_global_skips(2)
                        \baca-time-signature-color #'blue                                            %! EXPLICIT_TIME_SIGNATURE_COLOR:baca.SegmentMaker._attach_color_literal(2)
                        s1 * 3/8                                                                     %! baca.SegmentMaker._make_global_skips(1)
            <BLANKLINE>
                        % [Global_Skips measure 3]                                                   %! baca.SegmentMaker._comment_measure_numbers()
                        \baca-new-spacing-section #1 #12                                             %! HorizontalSpacingSpecifier(1):SPACING_COMMAND
                        \time 4/8                                                                    %! EXPLICIT_TIME_SIGNATURE:_set_status_tag:baca.SegmentMaker._make_global_skips(2)
                        \baca-time-signature-color #'blue                                            %! EXPLICIT_TIME_SIGNATURE_COLOR:baca.SegmentMaker._attach_color_literal(2)
                        s1 * 1/2                                                                     %! baca.SegmentMaker._make_global_skips(1)
            <BLANKLINE>
                        % [Global_Skips measure 4]                                                   %! baca.SegmentMaker._comment_measure_numbers()
                        \baca-new-spacing-section #1 #12                                             %! HorizontalSpacingSpecifier(1):SPACING_COMMAND
                        \time 3/8                                                                    %! EXPLICIT_TIME_SIGNATURE:_set_status_tag:baca.SegmentMaker._make_global_skips(2)
                        \baca-time-signature-color #'blue                                            %! EXPLICIT_TIME_SIGNATURE_COLOR:baca.SegmentMaker._attach_color_literal(2)
                        s1 * 3/8                                                                     %! baca.SegmentMaker._make_global_skips(1)
                        \baca-bar-line-visible                                                       %! baca.SegmentMaker._attach_final_bar_line()
                        \bar "|"                                                                     %! baca.SegmentMaker._attach_final_bar_line()
            <BLANKLINE>
                        % [Global_Skips measure 5]                                                   %! PHANTOM:baca.SegmentMaker._style_phantom_measures(1):baca.SegmentMaker._comment_measure_numbers()
                        \baca-new-spacing-section #1 #4                                              %! PHANTOM:baca.SegmentMaker._style_phantom_measures(1):HorizontalSpacingSpecifier(1):SPACING_COMMAND
                        \time 1/4                                                                    %! PHANTOM:baca.SegmentMaker._style_phantom_measures(1):EXPLICIT_TIME_SIGNATURE:_set_status_tag:baca.SegmentMaker._make_global_skips(3)
                        \baca-time-signature-transparent                                             %! PHANTOM:baca.SegmentMaker._style_phantom_measures(2)
                        s1 * 1/4                                                                     %! PHANTOM:baca.SegmentMaker._make_global_skips(3)
                        \once \override Score.BarLine.transparent = ##t                              %! PHANTOM:baca.SegmentMaker._style_phantom_measures(3)
                        \once \override Score.SpanBar.transparent = ##t                              %! PHANTOM:baca.SegmentMaker._style_phantom_measures(3)
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
                            % [Music_Voice measure 1]                                                %! baca.SegmentMaker._comment_measure_numbers()
                            c''2                                                                     %! baca.make_notes
            <BLANKLINE>
                            % [Music_Voice measure 2]                                                %! baca.SegmentMaker._comment_measure_numbers()
                            \baca-invisible-music                                                    %! baca.invisible_music:IndicatorCommand
                            c''4.                                                                    %! baca.make_notes
            <BLANKLINE>
                            % [Music_Voice measure 3]                                                %! baca.SegmentMaker._comment_measure_numbers()
                            \baca-invisible-music                                                    %! baca.invisible_music:IndicatorCommand
                            c''2                                                                     %! baca.make_notes
            <BLANKLINE>
                            % [Music_Voice measure 4]                                                %! baca.SegmentMaker._comment_measure_numbers()
                            c''4.                                                                    %! baca.make_notes
            <BLANKLINE>
                            <<                                                                       %! PHANTOM:baca.SegmentMaker._make_multimeasure_rest_container()
            <BLANKLINE>
                                \context Voice = "Music_Voice"                                       %! PHANTOM:baca.SegmentMaker._make_multimeasure_rest_container()
                                {                                                                    %! PHANTOM:baca.SegmentMaker._make_multimeasure_rest_container()
            <BLANKLINE>
                                    % [Music_Voice measure 5]                                        %! PHANTOM:baca.SegmentMaker._style_phantom_measures(5):baca.SegmentMaker._comment_measure_numbers()
                                    \baca-invisible-music                                            %! PHANTOM:baca.SegmentMaker._style_phantom_measures(5):baca.SegmentMaker._make_multimeasure_rest_container()
                                    c'1 * 1/4                                                        %! PHANTOM:baca.SegmentMaker._make_multimeasure_rest_container()
            <BLANKLINE>
                                }                                                                    %! PHANTOM:baca.SegmentMaker._make_multimeasure_rest_container()
            <BLANKLINE>
                                \context Voice = "Rest_Voice"                                        %! PHANTOM:baca.SegmentMaker._make_multimeasure_rest_container()
                                {                                                                    %! PHANTOM:baca.SegmentMaker._make_multimeasure_rest_container()
            <BLANKLINE>
                                    % [Rest_Voice measure 5]                                         %! PHANTOM:baca.SegmentMaker._style_phantom_measures(5):baca.SegmentMaker._comment_measure_numbers()
                                    \once \override Score.TimeSignature.X-extent = ##f               %! PHANTOM:baca.SegmentMaker._style_phantom_measures(6)
                                    \once \override MultiMeasureRest.transparent = ##t               %! PHANTOM:baca.SegmentMaker._style_phantom_measures(7)
                                    \stopStaff                                                       %! PHANTOM:baca.SegmentMaker._style_phantom_measures(8)
                                    \once \override Staff.StaffSymbol.transparent = ##t              %! PHANTOM:baca.SegmentMaker._style_phantom_measures(8)
                                    \startStaff                                                      %! PHANTOM:baca.SegmentMaker._style_phantom_measures(8)
                                    R1 * 1/4                                                         %! PHANTOM:baca.SegmentMaker._make_multimeasure_rest_container()
            <BLANKLINE>
                                }                                                                    %! PHANTOM:baca.SegmentMaker._make_multimeasure_rest_container()
            <BLANKLINE>
                            >>                                                                       %! PHANTOM:baca.SegmentMaker._make_multimeasure_rest_container()
            <BLANKLINE>
                        }                                                                            %! baca.SingleStaffScoreTemplate.__call__
            <BLANKLINE>
                    }                                                                                %! baca.SingleStaffScoreTemplate.__call__
            <BLANKLINE>
                >>                                                                                   %! baca.SingleStaffScoreTemplate.__call__
            <BLANKLINE>
            >>                                                                                       %! baca.SingleStaffScoreTemplate.__call__

    """
    return commandclasses.IndicatorCommand(
        indicators=[abjad.LilyPondLiteral(r"\baca-invisible-music")],
        map=map,
        selector=selector,
        tags=[tag],
    )


def label(
    expression: abjad.Expression,
    *,
    selector: abjad.SelectorTyping = "baca.leaves()",
) -> commandclasses.LabelCommand:
    r"""
    Labels ``selector`` output with label ``expression``.

    ..  container:: example

        Labels pitch names:

        >>> stack = baca.stack(
        ...     baca.figure(
        ...         [1, 1, 5, -1],
        ...         16,
        ...         affix=baca.rests_around([2], [4]),
        ...         restart_talea=True,
        ...         treatments=[-1],
        ...     ),
        ...     rmakers.beam(),
        ...     baca.label(abjad.label().with_pitches(locale='us')),
        ...     baca.tuplet_bracket_staff_padding(2),
        ... )
        >>> selection = stack([[0, 2, 10], [18, 16, 15, 20, 19], [9]])
        >>> lilypond_file = abjad.LilyPondFile.rhythm(selection)
        >>> abjad.show(lilypond_file, strict=89) # doctest: +SKIP

        ..  docs::

            >>> abjad.f(lilypond_file[abjad.Score], strict=89)
            \new Score
            <<
                \new GlobalContext
                {
                    \time 11/8
                    s1 * 11/8
                }
                \new Staff
                {
                    \tweak text #tuplet-number::calc-fraction-text
                    \times 9/10 {
                        \override TupletBracket.staff-padding = #2                                   %! baca.tuplet_bracket_staff_padding():OverrideCommand(1)
                        r8
                        c'16
                        ^ \markup { C4 }
                        [
                        d'16
                        ^ \markup { D4 }
                        ]
                        bf'4
                        ^ \markup { Bb4 }
                        ~
                        bf'16
                        r16
                    }
                    \tweak text #tuplet-number::calc-fraction-text
                    \times 9/10 {
                        fs''16
                        ^ \markup { "F#5" }
                        [
                        e''16
                        ^ \markup { E5 }
                        ]
                        ef''4
                        ^ \markup { Eb5 }
                        ~
                        ef''16
                        r16
                        af''16
                        ^ \markup { Ab5 }
                        [
                        g''16
                        ^ \markup { G5 }
                        ]
                    }
                    \times 4/5 {
                        a'16
                        ^ \markup { A4 }
                        r4
                        \revert TupletBracket.staff-padding                                          %! baca.tuplet_bracket_staff_padding():OverrideCommand(2)
                    }
                }
            >>

    """
    return commandclasses.LabelCommand(
        expression=expression, selector=selector
    )


def markup(
    argument: typing.Union[str, abjad.Markup],
    *tweaks: abjad.LilyPondTweakManager,
    boxed: bool = None,
    # typehinting is weird for some reason
    direction=abjad.Up,
    literal: bool = False,
    map: abjad.SelectorTyping = None,
    match: typings.Indices = None,
    measures: typings.SliceTyping = None,
    selector: abjad.SelectorTyping = "baca.pleaf(0)",
    tag: typing.Optional[str] = "baca.markup",
) -> commandclasses.IndicatorCommand:
    r"""
    Makes markup and inserts into indicator command.

    ..  container:: example

        Attaches markup to pitched head 0:

        >>> stack = baca.stack(
        ...     baca.figure(
        ...         [1, 1, 5, -1],
        ...         16,
        ...         affix=baca.rests_around([2], [4]),
        ...         restart_talea=True,
        ...         treatments=[-1],
        ...     ),
        ...     rmakers.beam(),
        ...     baca.markup('più mosso'),
        ...     baca.tuplet_bracket_outside_staff_priority(1000),
        ...     baca.tuplet_bracket_staff_padding(2),
        ... )
        >>> selection = stack([[0, 2, 10], [18, 16, 15, 20, 19], [9]])
        >>> lilypond_file = abjad.LilyPondFile.rhythm(selection)
        >>> abjad.show(lilypond_file, strict=89) # doctest: +SKIP

        ..  docs::

            >>> abjad.f(lilypond_file[abjad.Score], strict=89)
            \new Score
            <<
                \new GlobalContext
                {
                    \time 11/8
                    s1 * 11/8
                }
                \new Staff
                {
                    \tweak text #tuplet-number::calc-fraction-text
                    \times 9/10 {
                        \override TupletBracket.outside-staff-priority = #1000                       %! baca.tuplet_bracket_outside_staff_priority():OverrideCommand(1)
                        \override TupletBracket.staff-padding = #2                                   %! baca.tuplet_bracket_staff_padding():OverrideCommand(1)
                        r8
                        c'16
                        ^ \markup { "più mosso" }                                                    %! baca.markup:IndicatorCommand
                        [
                        d'16
                        ]
                        bf'4
                        ~
                        bf'16
                        r16
                    }
                    \tweak text #tuplet-number::calc-fraction-text
                    \times 9/10 {
                        fs''16
                        [
                        e''16
                        ]
                        ef''4
                        ~
                        ef''16
                        r16
                        af''16
                        [
                        g''16
                        ]
                    }
                    \times 4/5 {
                        a'16
                        r4
                        \revert TupletBracket.outside-staff-priority                                 %! baca.tuplet_bracket_outside_staff_priority():OverrideCommand(2)
                        \revert TupletBracket.staff-padding                                          %! baca.tuplet_bracket_staff_padding():OverrideCommand(2)
                    }
                }
            >>

    ..  container:: example

        Set ``literal=True`` to pass predefined markup commands:

        >>> stack = baca.stack(
        ...     baca.figure(
        ...         [1, 1, 5, -1],
        ...         16,
        ...         affix=baca.rests_around([2], [4]),
        ...         restart_talea=True,
        ...         treatments=[-1],
        ...     ),
        ...     rmakers.beam(),
        ...     baca.markup(
        ...         r'\markup { \baca-triple-diamond-markup }',
        ...         literal=True,
        ...         ),
        ...     baca.tuplet_bracket_outside_staff_priority(1000),
        ...     baca.tuplet_bracket_staff_padding(2),
        ... )
        >>> selection = stack([[0, 2, 10], [18, 16, 15, 20, 19], [9]])
        >>> lilypond_file = abjad.LilyPondFile.rhythm(selection)
        >>> abjad.show(lilypond_file, strict=89) # doctest: +SKIP

        ..  docs::

            >>> abjad.f(lilypond_file[abjad.Score], strict=89)
            \new Score
            <<
                \new GlobalContext
                {
                    \time 11/8
                    s1 * 11/8
                }
                \new Staff
                {
                    \tweak text #tuplet-number::calc-fraction-text
                    \times 9/10 {
                        \override TupletBracket.outside-staff-priority = #1000                       %! baca.tuplet_bracket_outside_staff_priority():OverrideCommand(1)
                        \override TupletBracket.staff-padding = #2                                   %! baca.tuplet_bracket_staff_padding():OverrideCommand(1)
                        r8
                        c'16
                        ^ \markup { \baca-triple-diamond-markup }                                    %! baca.markup:IndicatorCommand
                        [
                        d'16
                        ]
                        bf'4
                        ~
                        bf'16
                        r16
                    }
                    \tweak text #tuplet-number::calc-fraction-text
                    \times 9/10 {
                        fs''16
                        [
                        e''16
                        ]
                        ef''4
                        ~
                        ef''16
                        r16
                        af''16
                        [
                        g''16
                        ]
                    }
                    \times 4/5 {
                        a'16
                        r4
                        \revert TupletBracket.outside-staff-priority                                 %! baca.tuplet_bracket_outside_staff_priority():OverrideCommand(2)
                        \revert TupletBracket.staff-padding                                          %! baca.tuplet_bracket_staff_padding():OverrideCommand(2)
                    }
                }
            >>

    ..  container:: example exception

        Raises exception on nonstring, nonmarkup ``argument``:

        >>> baca.markup(['Allegro', 'ma non troppo'])
        Traceback (most recent call last):
            ...
        Exception: MarkupLibary.__call__():
            Value of 'argument' must be str or markup.
            Not ['Allegro', 'ma non troppo'].

    """
    if direction not in (abjad.Down, abjad.Up):
        message = f"direction must be up or down (not {direction!r})."
        raise Exception(message)
    if isinstance(argument, str):
        if literal:
            markup = abjad.Markup(argument, direction=direction, literal=True)
        else:
            markup = abjad.Markup(argument, direction=direction)
    elif isinstance(argument, abjad.Markup):
        markup = abjad.new(argument, direction=direction)
    else:
        message = "MarkupLibary.__call__():\n"
        message += "  Value of 'argument' must be str or markup.\n"
        message += f"  Not {argument!r}."
        raise Exception(message)
    if boxed:
        markup = markup.box().override(("box-padding", 0.5))
    prototype = (str, abjad.Expression)
    if selector is not None and not isinstance(selector, prototype):
        message = f"selector must be string or expression"
        message += f" (not {selector!r})."
        raise Exception(message)
    selector = selector or "baca.phead(0)"
    return commandclasses.IndicatorCommand(
        indicators=[markup],
        map=map,
        match=match,
        measures=measures,
        selector=selector,
        tags=[tag],
        tweaks=tweaks,
    )


def metronome_mark(
    key: typing.Union[str, indicators.Accelerando, indicators.Ritardando],
    selector: abjad.SelectorTyping = "baca.leaf(0)",
    *,
    redundant: bool = None,
) -> typing.Optional[commandclasses.MetronomeMarkCommand]:
    """
    Attaches metronome mark matching ``key`` metronome mark manifest.
    """
    if redundant is True:
        return None
    return commandclasses.MetronomeMarkCommand(
        key=key, redundant=redundant, selector=selector
    )


def parts(
    part_assignment: abjad.PartAssignment,
    *,
    selector: abjad.SelectorTyping = "baca.leaves()",
) -> commandclasses.PartAssignmentCommand:
    r"""
    Inserts ``selector`` output in container and sets part assignment.

    ..  container:: example

        >>> maker = baca.SegmentMaker(
        ...     score_template=baca.StringTrioScoreTemplate(),
        ...     time_signatures=[(4, 8), (3, 8), (4, 8), (3, 8)],
        ...     )

        >>> maker(
        ...     'Violin_Music_Voice',
        ...     baca.make_notes(),
        ...     baca.parts(abjad.PartAssignment('Violin')),
        ...     baca.pitch('E4'),
        ...     )

        >>> lilypond_file = maker.run(environment='docs')
        >>> abjad.show(lilypond_file, strict=89) # doctest: +SKIP

        >>> abjad.f(lilypond_file[abjad.Score], strict=89)
        <BLANKLINE>
        \context Score = "Score"                                                                 %! baca.StringTrioScoreTemplate.__call__
        <<                                                                                       %! baca.StringTrioScoreTemplate.__call__
        <BLANKLINE>
            \context GlobalContext = "Global_Context"                                            %! abjad.ScoreTemplate._make_global_context
            <<                                                                                   %! abjad.ScoreTemplate._make_global_context
        <BLANKLINE>
                \context GlobalSkips = "Global_Skips"                                            %! abjad.ScoreTemplate._make_global_context
                {                                                                                %! abjad.ScoreTemplate._make_global_context
        <BLANKLINE>
                    % [Global_Skips measure 1]                                                   %! baca.SegmentMaker._comment_measure_numbers()
                    \time 4/8                                                                    %! EXPLICIT_TIME_SIGNATURE:_set_status_tag:baca.SegmentMaker._make_global_skips(2)
                    \baca-time-signature-color #'blue                                            %! EXPLICIT_TIME_SIGNATURE_COLOR:baca.SegmentMaker._attach_color_literal(2)
                    s1 * 1/2                                                                     %! baca.SegmentMaker._make_global_skips(1)
        <BLANKLINE>
                    % [Global_Skips measure 2]                                                   %! baca.SegmentMaker._comment_measure_numbers()
                    \time 3/8                                                                    %! EXPLICIT_TIME_SIGNATURE:_set_status_tag:baca.SegmentMaker._make_global_skips(2)
                    \baca-time-signature-color #'blue                                            %! EXPLICIT_TIME_SIGNATURE_COLOR:baca.SegmentMaker._attach_color_literal(2)
                    s1 * 3/8                                                                     %! baca.SegmentMaker._make_global_skips(1)
        <BLANKLINE>
                    % [Global_Skips measure 3]                                                   %! baca.SegmentMaker._comment_measure_numbers()
                    \time 4/8                                                                    %! EXPLICIT_TIME_SIGNATURE:_set_status_tag:baca.SegmentMaker._make_global_skips(2)
                    \baca-time-signature-color #'blue                                            %! EXPLICIT_TIME_SIGNATURE_COLOR:baca.SegmentMaker._attach_color_literal(2)
                    s1 * 1/2                                                                     %! baca.SegmentMaker._make_global_skips(1)
        <BLANKLINE>
                    % [Global_Skips measure 4]                                                   %! baca.SegmentMaker._comment_measure_numbers()
                    \time 3/8                                                                    %! EXPLICIT_TIME_SIGNATURE:_set_status_tag:baca.SegmentMaker._make_global_skips(2)
                    \baca-time-signature-color #'blue                                            %! EXPLICIT_TIME_SIGNATURE_COLOR:baca.SegmentMaker._attach_color_literal(2)
                    s1 * 3/8                                                                     %! baca.SegmentMaker._make_global_skips(1)
                    \baca-bar-line-visible                                                       %! baca.SegmentMaker._attach_final_bar_line()
                    \bar "|"                                                                     %! baca.SegmentMaker._attach_final_bar_line()
        <BLANKLINE>
                    % [Global_Skips measure 5]                                                   %! PHANTOM:baca.SegmentMaker._style_phantom_measures(1):baca.SegmentMaker._comment_measure_numbers()
                    \time 1/4                                                                    %! PHANTOM:baca.SegmentMaker._style_phantom_measures(1):EXPLICIT_TIME_SIGNATURE:_set_status_tag:baca.SegmentMaker._make_global_skips(3)
                    \baca-time-signature-transparent                                             %! PHANTOM:baca.SegmentMaker._style_phantom_measures(2)
                    s1 * 1/4                                                                     %! PHANTOM:baca.SegmentMaker._make_global_skips(3)
                    \once \override Score.BarLine.transparent = ##t                              %! PHANTOM:baca.SegmentMaker._style_phantom_measures(3)
                    \once \override Score.SpanBar.transparent = ##t                              %! PHANTOM:baca.SegmentMaker._style_phantom_measures(3)
        <BLANKLINE>
                }                                                                                %! abjad.ScoreTemplate._make_global_context
        <BLANKLINE>
            >>                                                                                   %! abjad.ScoreTemplate._make_global_context
        <BLANKLINE>
            \context MusicContext = "Music_Context"                                              %! baca.StringTrioScoreTemplate.__call__
            <<                                                                                   %! baca.StringTrioScoreTemplate.__call__
        <BLANKLINE>
                \context StringSectionStaffGroup = "String_Section_Staff_Group"                  %! baca.StringTrioScoreTemplate.__call__
                <<                                                                               %! baca.StringTrioScoreTemplate.__call__
        <BLANKLINE>
                    \tag Violin                                                                  %! baca.ScoreTemplate._attach_liypond_tag
                    \context ViolinMusicStaff = "Violin_Music_Staff"                             %! baca.StringTrioScoreTemplate.__call__
                    {                                                                            %! baca.StringTrioScoreTemplate.__call__
        <BLANKLINE>
                        \context ViolinMusicVoice = "Violin_Music_Voice"                         %! baca.StringTrioScoreTemplate.__call__
                        {                                                                        %! baca.StringTrioScoreTemplate.__call__
        <BLANKLINE>
                            {   %*% PartAssignment('Violin')
        <BLANKLINE>
                                % [Violin_Music_Voice measure 1]                                 %! baca.SegmentMaker._comment_measure_numbers()
                                \clef "treble"                                                   %! DEFAULT_CLEF:_set_status_tag:abjad.ScoreTemplate.attach_defaults
                                \once \override ViolinMusicStaff.Clef.color = #(x11-color 'DarkViolet) %! DEFAULT_CLEF_COLOR:baca.SegmentMaker._attach_color_literal(2)
                            %@% \override ViolinMusicStaff.Clef.color = ##f                      %! DEFAULT_CLEF_COLOR_CANCELLATION:baca.SegmentMaker._attach_color_literal(1)
                                \set ViolinMusicStaff.forceClef = ##t                            %! DEFAULT_CLEF:_set_status_tag:baca.SegmentMaker._treat_persistent_wrapper(2):abjad.ScoreTemplate.attach_defaults
                                e'2                                                              %! baca.make_notes
                                ^ \baca-default-indicator-markup "(Violin)"                      %! DEFAULT_INSTRUMENT_ALERT:baca.SegmentMaker._attach_latent_indicator_alert()
                                \override ViolinMusicStaff.Clef.color = #(x11-color 'violet)     %! DEFAULT_CLEF_REDRAW_COLOR:baca.SegmentMaker._attach_color_literal(2)
        <BLANKLINE>
                                % [Violin_Music_Voice measure 2]                                 %! baca.SegmentMaker._comment_measure_numbers()
                                e'4.                                                             %! baca.make_notes
        <BLANKLINE>
                                % [Violin_Music_Voice measure 3]                                 %! baca.SegmentMaker._comment_measure_numbers()
                                e'2                                                              %! baca.make_notes
        <BLANKLINE>
                                % [Violin_Music_Voice measure 4]                                 %! baca.SegmentMaker._comment_measure_numbers()
                                e'4.                                                             %! baca.make_notes
        <BLANKLINE>
                            }   %*% PartAssignment('Violin')
        <BLANKLINE>
                            <<                                                                   %! PHANTOM:baca.SegmentMaker._make_multimeasure_rest_container()
        <BLANKLINE>
                                \context Voice = "Violin_Music_Voice"                            %! PHANTOM:baca.SegmentMaker._make_multimeasure_rest_container()
                                {                                                                %! PHANTOM:baca.SegmentMaker._make_multimeasure_rest_container()
        <BLANKLINE>
                                    % [Violin_Music_Voice measure 5]                             %! PHANTOM:baca.SegmentMaker._style_phantom_measures(5):baca.SegmentMaker._comment_measure_numbers()
                                    \baca-invisible-music                                        %! PHANTOM:baca.SegmentMaker._style_phantom_measures(5):baca.SegmentMaker._make_multimeasure_rest_container()
                                    c'1 * 1/4                                                    %! PHANTOM:baca.SegmentMaker._make_multimeasure_rest_container()
        <BLANKLINE>
                                }                                                                %! PHANTOM:baca.SegmentMaker._make_multimeasure_rest_container()
        <BLANKLINE>
                                \context Voice = "Violin_Rest_Voice"                             %! PHANTOM:baca.SegmentMaker._make_multimeasure_rest_container()
                                {                                                                %! PHANTOM:baca.SegmentMaker._make_multimeasure_rest_container()
        <BLANKLINE>
                                    % [Violin_Rest_Voice measure 5]                              %! PHANTOM:baca.SegmentMaker._style_phantom_measures(5):baca.SegmentMaker._comment_measure_numbers()
                                    \once \override Score.TimeSignature.X-extent = ##f           %! PHANTOM:baca.SegmentMaker._style_phantom_measures(6)
                                    \once \override MultiMeasureRest.transparent = ##t           %! PHANTOM:baca.SegmentMaker._style_phantom_measures(7)
                                    \stopStaff                                                   %! PHANTOM:baca.SegmentMaker._style_phantom_measures(8)
                                    \once \override Staff.StaffSymbol.transparent = ##t          %! PHANTOM:baca.SegmentMaker._style_phantom_measures(8)
                                    \startStaff                                                  %! PHANTOM:baca.SegmentMaker._style_phantom_measures(8)
                                    R1 * 1/4                                                     %! PHANTOM:baca.SegmentMaker._make_multimeasure_rest_container()
        <BLANKLINE>
                                }                                                                %! PHANTOM:baca.SegmentMaker._make_multimeasure_rest_container()
        <BLANKLINE>
                            >>                                                                   %! PHANTOM:baca.SegmentMaker._make_multimeasure_rest_container()
        <BLANKLINE>
                        }                                                                        %! baca.StringTrioScoreTemplate.__call__
        <BLANKLINE>
                    }                                                                            %! baca.StringTrioScoreTemplate.__call__
        <BLANKLINE>
                    \tag Viola                                                                   %! baca.ScoreTemplate._attach_liypond_tag
                    \context ViolaMusicStaff = "Viola_Music_Staff"                               %! baca.StringTrioScoreTemplate.__call__
                    {                                                                            %! baca.StringTrioScoreTemplate.__call__
        <BLANKLINE>
                        \context ViolaMusicVoice = "Viola_Music_Voice"                           %! baca.StringTrioScoreTemplate.__call__
                        {                                                                        %! baca.StringTrioScoreTemplate.__call__
        <BLANKLINE>
                            % [Viola_Music_Voice measure 1]                                      %! baca.SegmentMaker._comment_measure_numbers()
                            \clef "alto"                                                         %! DEFAULT_CLEF:_set_status_tag:abjad.ScoreTemplate.attach_defaults
                            \once \override ViolaMusicStaff.Clef.color = #(x11-color 'DarkViolet) %! DEFAULT_CLEF_COLOR:baca.SegmentMaker._attach_color_literal(2)
                        %@% \override ViolaMusicStaff.Clef.color = ##f                           %! DEFAULT_CLEF_COLOR_CANCELLATION:baca.SegmentMaker._attach_color_literal(1)
                            \set ViolaMusicStaff.forceClef = ##t                                 %! DEFAULT_CLEF:_set_status_tag:baca.SegmentMaker._treat_persistent_wrapper(2):abjad.ScoreTemplate.attach_defaults
                            R1 * 4/8                                                             %! _call_rhythm_commands
                            ^ \baca-default-indicator-markup "(Viola)"                           %! DEFAULT_INSTRUMENT_ALERT:baca.SegmentMaker._attach_latent_indicator_alert()
                            \override ViolaMusicStaff.Clef.color = #(x11-color 'violet)          %! DEFAULT_CLEF_REDRAW_COLOR:baca.SegmentMaker._attach_color_literal(2)
        <BLANKLINE>
                            % [Viola_Music_Voice measure 2]                                      %! baca.SegmentMaker._comment_measure_numbers()
                            R1 * 3/8                                                             %! _call_rhythm_commands
        <BLANKLINE>
                            % [Viola_Music_Voice measure 3]                                      %! baca.SegmentMaker._comment_measure_numbers()
                            R1 * 4/8                                                             %! _call_rhythm_commands
        <BLANKLINE>
                            % [Viola_Music_Voice measure 4]                                      %! baca.SegmentMaker._comment_measure_numbers()
                            R1 * 3/8                                                             %! _call_rhythm_commands
        <BLANKLINE>
                            <<                                                                   %! PHANTOM:baca.SegmentMaker._make_multimeasure_rest_container()
        <BLANKLINE>
                                \context Voice = "Viola_Music_Voice"                             %! PHANTOM:baca.SegmentMaker._make_multimeasure_rest_container()
                                {                                                                %! PHANTOM:baca.SegmentMaker._make_multimeasure_rest_container()
        <BLANKLINE>
                                    % [Viola_Music_Voice measure 5]                              %! PHANTOM:baca.SegmentMaker._style_phantom_measures(5):baca.SegmentMaker._comment_measure_numbers()
                                    \baca-invisible-music                                        %! PHANTOM:baca.SegmentMaker._style_phantom_measures(5):baca.SegmentMaker._make_multimeasure_rest_container()
                                    R1 * 1/4                                                     %! PHANTOM:baca.SegmentMaker._make_multimeasure_rest_container()
        <BLANKLINE>
                                }                                                                %! PHANTOM:baca.SegmentMaker._make_multimeasure_rest_container()
        <BLANKLINE>
                                \context Voice = "Viola_Rest_Voice"                              %! PHANTOM:baca.SegmentMaker._make_multimeasure_rest_container()
                                {                                                                %! PHANTOM:baca.SegmentMaker._make_multimeasure_rest_container()
        <BLANKLINE>
                                    % [Viola_Rest_Voice measure 5]                               %! PHANTOM:baca.SegmentMaker._style_phantom_measures(5):baca.SegmentMaker._comment_measure_numbers()
                                    \once \override Score.TimeSignature.X-extent = ##f           %! PHANTOM:baca.SegmentMaker._style_phantom_measures(6)
                                    \once \override MultiMeasureRest.transparent = ##t           %! PHANTOM:baca.SegmentMaker._style_phantom_measures(7)
                                    \stopStaff                                                   %! PHANTOM:baca.SegmentMaker._style_phantom_measures(8)
                                    \once \override Staff.StaffSymbol.transparent = ##t          %! PHANTOM:baca.SegmentMaker._style_phantom_measures(8)
                                    \startStaff                                                  %! PHANTOM:baca.SegmentMaker._style_phantom_measures(8)
                                    R1 * 1/4                                                     %! PHANTOM:baca.SegmentMaker._make_multimeasure_rest_container()
        <BLANKLINE>
                                }                                                                %! PHANTOM:baca.SegmentMaker._make_multimeasure_rest_container()
        <BLANKLINE>
                            >>                                                                   %! PHANTOM:baca.SegmentMaker._make_multimeasure_rest_container()
        <BLANKLINE>
                        }                                                                        %! baca.StringTrioScoreTemplate.__call__
        <BLANKLINE>
                    }                                                                            %! baca.StringTrioScoreTemplate.__call__
        <BLANKLINE>
                    \tag Cello                                                                   %! baca.ScoreTemplate._attach_liypond_tag
                    \context CelloMusicStaff = "Cello_Music_Staff"                               %! baca.StringTrioScoreTemplate.__call__
                    {                                                                            %! baca.StringTrioScoreTemplate.__call__
        <BLANKLINE>
                        \context CelloMusicVoice = "Cello_Music_Voice"                           %! baca.StringTrioScoreTemplate.__call__
                        {                                                                        %! baca.StringTrioScoreTemplate.__call__
        <BLANKLINE>
                            % [Cello_Music_Voice measure 1]                                      %! baca.SegmentMaker._comment_measure_numbers()
                            \clef "bass"                                                         %! DEFAULT_CLEF:_set_status_tag:abjad.ScoreTemplate.attach_defaults
                            \once \override CelloMusicStaff.Clef.color = #(x11-color 'DarkViolet) %! DEFAULT_CLEF_COLOR:baca.SegmentMaker._attach_color_literal(2)
                        %@% \override CelloMusicStaff.Clef.color = ##f                           %! DEFAULT_CLEF_COLOR_CANCELLATION:baca.SegmentMaker._attach_color_literal(1)
                            \set CelloMusicStaff.forceClef = ##t                                 %! DEFAULT_CLEF:_set_status_tag:baca.SegmentMaker._treat_persistent_wrapper(2):abjad.ScoreTemplate.attach_defaults
                            R1 * 4/8                                                             %! _call_rhythm_commands
                            ^ \baca-default-indicator-markup "(Cello)"                           %! DEFAULT_INSTRUMENT_ALERT:baca.SegmentMaker._attach_latent_indicator_alert()
                            \override CelloMusicStaff.Clef.color = #(x11-color 'violet)          %! DEFAULT_CLEF_REDRAW_COLOR:baca.SegmentMaker._attach_color_literal(2)
        <BLANKLINE>
                            % [Cello_Music_Voice measure 2]                                      %! baca.SegmentMaker._comment_measure_numbers()
                            R1 * 3/8                                                             %! _call_rhythm_commands
        <BLANKLINE>
                            % [Cello_Music_Voice measure 3]                                      %! baca.SegmentMaker._comment_measure_numbers()
                            R1 * 4/8                                                             %! _call_rhythm_commands
        <BLANKLINE>
                            % [Cello_Music_Voice measure 4]                                      %! baca.SegmentMaker._comment_measure_numbers()
                            R1 * 3/8                                                             %! _call_rhythm_commands
        <BLANKLINE>
                            <<                                                                   %! PHANTOM:baca.SegmentMaker._make_multimeasure_rest_container()
        <BLANKLINE>
                                \context Voice = "Cello_Music_Voice"                             %! PHANTOM:baca.SegmentMaker._make_multimeasure_rest_container()
                                {                                                                %! PHANTOM:baca.SegmentMaker._make_multimeasure_rest_container()
        <BLANKLINE>
                                    % [Cello_Music_Voice measure 5]                              %! PHANTOM:baca.SegmentMaker._style_phantom_measures(5):baca.SegmentMaker._comment_measure_numbers()
                                    \baca-invisible-music                                        %! PHANTOM:baca.SegmentMaker._style_phantom_measures(5):baca.SegmentMaker._make_multimeasure_rest_container()
                                    R1 * 1/4                                                     %! PHANTOM:baca.SegmentMaker._make_multimeasure_rest_container()
        <BLANKLINE>
                                }                                                                %! PHANTOM:baca.SegmentMaker._make_multimeasure_rest_container()
        <BLANKLINE>
                                \context Voice = "Cello_Rest_Voice"                              %! PHANTOM:baca.SegmentMaker._make_multimeasure_rest_container()
                                {                                                                %! PHANTOM:baca.SegmentMaker._make_multimeasure_rest_container()
        <BLANKLINE>
                                    % [Cello_Rest_Voice measure 5]                               %! PHANTOM:baca.SegmentMaker._style_phantom_measures(5):baca.SegmentMaker._comment_measure_numbers()
                                    \once \override Score.TimeSignature.X-extent = ##f           %! PHANTOM:baca.SegmentMaker._style_phantom_measures(6)
                                    \once \override MultiMeasureRest.transparent = ##t           %! PHANTOM:baca.SegmentMaker._style_phantom_measures(7)
                                    \stopStaff                                                   %! PHANTOM:baca.SegmentMaker._style_phantom_measures(8)
                                    \once \override Staff.StaffSymbol.transparent = ##t          %! PHANTOM:baca.SegmentMaker._style_phantom_measures(8)
                                    \startStaff                                                  %! PHANTOM:baca.SegmentMaker._style_phantom_measures(8)
                                    R1 * 1/4                                                     %! PHANTOM:baca.SegmentMaker._make_multimeasure_rest_container()
        <BLANKLINE>
                                }                                                                %! PHANTOM:baca.SegmentMaker._make_multimeasure_rest_container()
        <BLANKLINE>
                            >>                                                                   %! PHANTOM:baca.SegmentMaker._make_multimeasure_rest_container()
        <BLANKLINE>
                        }                                                                        %! baca.StringTrioScoreTemplate.__call__
        <BLANKLINE>
                    }                                                                            %! baca.StringTrioScoreTemplate.__call__
        <BLANKLINE>
                >>                                                                               %! baca.StringTrioScoreTemplate.__call__
        <BLANKLINE>
            >>                                                                                   %! baca.StringTrioScoreTemplate.__call__
        <BLANKLINE>
        >>                                                                                       %! baca.StringTrioScoreTemplate.__call__

    ..  container:: example exception

        Raises exception when voice does not allow part assignment:

        >>> maker = baca.SegmentMaker(
        ...     score_template=baca.StringTrioScoreTemplate(),
        ...     test_container_identifiers=True,
        ...     time_signatures=[(4, 8), (3, 8), (4, 8), (3, 8)],
        ...     )

        >>> part_assignment = abjad.PartAssignment('Flute')

        >>> maker(
        ...     'Violin_Music_Voice',
        ...     baca.make_notes(),
        ...     baca.parts(part_assignment),
        ...     baca.pitches('E4 F4'),
        ...     )

        >>> lilypond_file = maker.run(environment='docs')
        Traceback (most recent call last):
            ...
        Exception: Violin_Music_Voice does not allow Flute part assignment:
            abjad.PartAssignment('Flute')

    """
    if not isinstance(part_assignment, abjad.PartAssignment):
        message = "part_assignment must be part assignment"
        message += f" (not {part_assignment!r})."
        raise Exception(message)
    return commandclasses.PartAssignmentCommand(
        part_assignment=part_assignment, selector=selector
    )


def one_voice(
    *,
    selector: abjad.SelectorTyping = "baca.leaf(0)",
    tag: typing.Optional[str] = "baca.one_voice",
) -> commandclasses.IndicatorCommand:
    r"""
    Makes LilyPond ``\oneVoice`` command.
    """
    literal = abjad.LilyPondLiteral(r"\oneVoice")
    return commandclasses.IndicatorCommand(
        indicators=[literal], selector=selector, tags=[tag]
    )


def open_volta(
    selector: abjad.SelectorTyping = "baca.leaf(0)"
) -> scoping.Suite:
    """
    Attaches bar line and overrides bar line X-extent.
    """
    return scoping.suite(
        indicatorcommands.bar_line(".|:", selector, format_slot="before"),
        scoping.not_mol(overrides.bar_line_x_extent((0, 2), selector)),
        scoping.only_mol(overrides.bar_line_x_extent((0, 3), selector)),
    )


def previous_metadata(path: str) -> abjad.OrderedDict:
    """
    Gets previous segment metadata before ``path``.
    """
    # reproduces abjad.Path.get_previous_path()
    # because Travis isn't configured for scores-directory calculations
    definition_py = abjad.Path(path)
    segment = abjad.Path(definition_py).parent
    assert segment.is_segment(), repr(segment)
    segments = segment.parent
    assert segments.is_segments(), repr(segments)
    paths = segments.list_paths()
    paths = [_ for _ in paths if not _.name.startswith(".")]
    assert all(_.is_dir() for _ in paths), repr(paths)
    index = paths.index(segment)
    if index == 0:
        return abjad.OrderedDict()
    previous_index = index - 1
    previous_segment = paths[previous_index]
    previous_metadata = previous_segment.get_metadata()
    return previous_metadata


def select(items=None):
    if items is None:
        return classes.Expression().select()
    return classes.Selection(items=items)


def sequence(items=None, **keywords):
    if items is None:
        return classes.Expression.sequence(**keywords)
    return classes.Sequence(items=items, **keywords)


def untie(selector: abjad.SelectorTyping) -> commandclasses.DetachCommand:
    r"""
    Makes (repeat-)tie detach command.
    """
    return commandclasses.DetachCommand(
        [abjad.Tie, abjad.RepeatTie], selector=selector
    )


def voice_four(
    *,
    selector: abjad.SelectorTyping = "baca.leaf(0)",
    tag: typing.Optional[str] = "baca.voice_four",
) -> commandclasses.IndicatorCommand:
    r"""
    Makes LilyPond ``\voiceFour`` command.
    """
    literal = abjad.LilyPondLiteral(r"\voiceFour")
    return commandclasses.IndicatorCommand(
        indicators=[literal], selector=selector, tags=[tag]
    )


def voice_one(
    *,
    selector: abjad.SelectorTyping = "baca.leaf(0)",
    tag: typing.Optional[str] = "baca.voice_one",
) -> commandclasses.IndicatorCommand:
    r"""
    Makes LilyPond ``\voiceOne`` command.
    """
    literal = abjad.LilyPondLiteral(r"\voiceOne")
    return commandclasses.IndicatorCommand(
        indicators=[literal], selector=selector, tags=[tag]
    )


def voice_three(
    *,
    selector: abjad.SelectorTyping = "baca.leaf(0)",
    tag: typing.Optional[str] = "baca.voice_three",
) -> commandclasses.IndicatorCommand:
    r"""
    Makes LilyPond ``\voiceThree`` command.
    """
    literal = abjad.LilyPondLiteral(r"\voiceThree")
    return commandclasses.IndicatorCommand(
        indicators=[literal], selector=selector, tags=[tag]
    )


def voice_two(
    *,
    selector: abjad.SelectorTyping = "baca.leaf(0)",
    tag: typing.Optional[str] = "baca.voice_two",
) -> commandclasses.IndicatorCommand:
    r"""
    Makes LilyPond ``\voiceTwo`` command.
    """
    literal = abjad.LilyPondLiteral(r"\voiceTwo")
    return commandclasses.IndicatorCommand(
        indicators=[literal], selector=selector, tags=[tag]
    )
