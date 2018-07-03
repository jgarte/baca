import abjad
import baca
import collections
import typing
from abjadext import rmakers
from . import library
from . import typings
from .Command import Command
from .Command import Map
from .Command import Suite
from .Expression import Expression
from .IndicatorBundle import IndicatorBundle
from .IndicatorCommand import IndicatorCommand
from .Markup import Markup
from .OverrideCommand import OverrideCommand
from .PiecewiseIndicatorCommand import PiecewiseIndicatorCommand
from .Selection import Selection
from .SpannerCommand import SpannerCommand
from .TieCorrectionCommand import TieCorrectionCommand
from .VoltaCommand import VoltaCommand


class LibraryTZ(abjad.AbjadObject):
    """
    Library T - Z.

    >>> from abjadext import rmakers

    """

    ### CLASS VARIABLES ###

    __documentation_section__ = '(1) Library'

    __slots__ = (
        )

    ### PUBLIC METHODS ###

    @staticmethod
    def new_text_spanner(
        *items: typing.Iterable[typing.Union[str, abjad.Markup, None]],
        bookend: typing.Union[bool, int] = -1,
        leak: bool = None,
        #left_broken: bool = None,
        lilypond_id: int = None,
        no_upright: bool = None,
        piece_selector: typings.Selector = 'baca.group()',
        #right_broken: bool = None,
        selector: typings.Selector = 'baca.tleaves()',
        tweaks: typing.List[abjad.LilyPondTweakManager] = None,
        ) -> PiecewiseIndicatorCommand:
        r"""
        Attaches text span indicators.

        ..  container:: example

            Single-segment spanners.

            Dashed line with arrow:

            >>> maker = baca.SegmentMaker(
            ...     score_template=baca.SingleStaffScoreTemplate(),
            ...     spacing=baca.minimum_duration((1, 12)),
            ...     time_signatures=[(4, 8), (3, 8), (4, 8), (3, 8)],
            ...     )

            >>> maker(
            ...     'MusicVoice',
            ...     baca.new_text_spanner(
            ...         baca.markups.pont(),
            ...         '=>',
            ...         baca.markups.ord(),
            ...     ),
            ...     baca.make_even_divisions(),
            ...     baca.pitches('E4 D5 F4 E5 G4 F5'),
            ...     baca.text_spanner_staff_padding(4.5),
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
                            \baca_new_spacing_section #1 #12                                             %! HSS1:SPACING
                            \time 4/8                                                                    %! SM8:EXPLICIT_TIME_SIGNATURE:SM1
                            \once \override Score.TimeSignature.color = #(x11-color 'blue)               %! SM6:EXPLICIT_TIME_SIGNATURE_COLOR:SM1
                            s1 * 1/2
                <BLANKLINE>
                            % [GlobalSkips measure 2]                                                    %! SM4
                            \baca_new_spacing_section #1 #12                                             %! HSS1:SPACING
                            \time 3/8                                                                    %! SM8:EXPLICIT_TIME_SIGNATURE:SM1
                            \once \override Score.TimeSignature.color = #(x11-color 'blue)               %! SM6:EXPLICIT_TIME_SIGNATURE_COLOR:SM1
                            s1 * 3/8
                <BLANKLINE>
                            % [GlobalSkips measure 3]                                                    %! SM4
                            \baca_new_spacing_section #1 #12                                             %! HSS1:SPACING
                            \time 4/8                                                                    %! SM8:EXPLICIT_TIME_SIGNATURE:SM1
                            \once \override Score.TimeSignature.color = #(x11-color 'blue)               %! SM6:EXPLICIT_TIME_SIGNATURE_COLOR:SM1
                            s1 * 1/2
                <BLANKLINE>
                            % [GlobalSkips measure 4]                                                    %! SM4
                            \baca_new_spacing_section #1 #12                                             %! HSS1:SPACING
                            \time 3/8                                                                    %! SM8:EXPLICIT_TIME_SIGNATURE:SM1
                            \once \override Score.TimeSignature.color = #(x11-color 'blue)               %! SM6:EXPLICIT_TIME_SIGNATURE_COLOR:SM1
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
                <BLANKLINE>
                                % [MusicVoice measure 1]                                                 %! SM4
                                \override TextSpanner.staff-padding = #4.5                               %! OC1
                                e'8
                                - \abjad_dashed_line_with_arrow                                          %! PIC
                                - \tweak bound-details.left.text \markup {                               %! PIC
                                    \concat                                                              %! PIC
                                        {                                                                %! PIC
                                            \upright                                                     %! PIC
                                                pont.                                                    %! PIC
                                            \hspace                                                      %! PIC
                                                #0.5                                                     %! PIC
                                        }                                                                %! PIC
                                    }                                                                    %! PIC
                                - \tweak bound-details.right.text \markup {                              %! PIC
                                    \upright                                                             %! PIC
                                        ord.                                                             %! PIC
                                    }                                                                    %! PIC
                                - \tweak bound-details.right.padding #0.5                                %! PIC
                                - \tweak bound-details.right.stencil-align-dir-y #center                 %! PIC
                                \startTextSpan                                                           %! PIC
                                [
                <BLANKLINE>
                                d''8
                <BLANKLINE>
                                f'8
                <BLANKLINE>
                                e''8
                                ]
                <BLANKLINE>
                                % [MusicVoice measure 2]                                                 %! SM4
                                g'8
                                [
                <BLANKLINE>
                                f''8
                <BLANKLINE>
                                e'8
                                ]
                <BLANKLINE>
                                % [MusicVoice measure 3]                                                 %! SM4
                                d''8
                                [
                <BLANKLINE>
                                f'8
                <BLANKLINE>
                                e''8
                <BLANKLINE>
                                g'8
                                ]
                <BLANKLINE>
                                % [MusicVoice measure 4]                                                 %! SM4
                                f''8
                                [
                <BLANKLINE>
                                e'8
                <BLANKLINE>
                                d''8
                                \stopTextSpan                                                            %! PIC
                                ]
                                \revert TextSpanner.staff-padding                                        %! OC2
                <BLANKLINE>
                            }
                        }
                    >>
                >>

            Dashed line with hook:

            >>> maker = baca.SegmentMaker(
            ...     score_template=baca.SingleStaffScoreTemplate(),
            ...     spacing=baca.minimum_duration((1, 12)),
            ...     time_signatures=[(4, 8), (3, 8), (4, 8), (3, 8)],
            ...     )

            >>> maker(
            ...     'MusicVoice',
            ...     baca.new_text_spanner(
            ...         baca.markups.pont(),
            ...         '=|',
            ...         baca.markups.ord(),
            ...     ),
            ...     baca.make_even_divisions(),
            ...     baca.pitches('E4 D5 F4 E5 G4 F5'),
            ...     baca.text_spanner_staff_padding(4.5),
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
                            \baca_new_spacing_section #1 #12                                             %! HSS1:SPACING
                            \time 4/8                                                                    %! SM8:EXPLICIT_TIME_SIGNATURE:SM1
                            \once \override Score.TimeSignature.color = #(x11-color 'blue)               %! SM6:EXPLICIT_TIME_SIGNATURE_COLOR:SM1
                            s1 * 1/2
                <BLANKLINE>
                            % [GlobalSkips measure 2]                                                    %! SM4
                            \baca_new_spacing_section #1 #12                                             %! HSS1:SPACING
                            \time 3/8                                                                    %! SM8:EXPLICIT_TIME_SIGNATURE:SM1
                            \once \override Score.TimeSignature.color = #(x11-color 'blue)               %! SM6:EXPLICIT_TIME_SIGNATURE_COLOR:SM1
                            s1 * 3/8
                <BLANKLINE>
                            % [GlobalSkips measure 3]                                                    %! SM4
                            \baca_new_spacing_section #1 #12                                             %! HSS1:SPACING
                            \time 4/8                                                                    %! SM8:EXPLICIT_TIME_SIGNATURE:SM1
                            \once \override Score.TimeSignature.color = #(x11-color 'blue)               %! SM6:EXPLICIT_TIME_SIGNATURE_COLOR:SM1
                            s1 * 1/2
                <BLANKLINE>
                            % [GlobalSkips measure 4]                                                    %! SM4
                            \baca_new_spacing_section #1 #12                                             %! HSS1:SPACING
                            \time 3/8                                                                    %! SM8:EXPLICIT_TIME_SIGNATURE:SM1
                            \once \override Score.TimeSignature.color = #(x11-color 'blue)               %! SM6:EXPLICIT_TIME_SIGNATURE_COLOR:SM1
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
                <BLANKLINE>
                                % [MusicVoice measure 1]                                                 %! SM4
                                \override TextSpanner.staff-padding = #4.5                               %! OC1
                                e'8
                                - \abjad_dashed_line_with_hook                                           %! PIC
                                - \tweak bound-details.left.text \markup {                               %! PIC
                                    \concat                                                              %! PIC
                                        {                                                                %! PIC
                                            \upright                                                     %! PIC
                                                pont.                                                    %! PIC
                                            \hspace                                                      %! PIC
                                                #0.5                                                     %! PIC
                                        }                                                                %! PIC
                                    }                                                                    %! PIC
                                - \tweak bound-details.right.text \markup {                              %! PIC
                                    \concat                                                              %! PIC
                                        {                                                                %! PIC
                                            \raise                                                       %! PIC
                                                #-1                                                      %! PIC
                                                \draw-line                                               %! PIC
                                                    #'(0 . -1)                                           %! PIC
                                            \hspace                                                      %! PIC
                                                #0.75                                                    %! PIC
                                            \general-align                                               %! PIC
                                                #Y                                                       %! PIC
                                                #1                                                       %! PIC
                                                \upright                                                 %! PIC
                                                    ord.                                                 %! PIC
                                        }                                                                %! PIC
                                    }                                                                    %! PIC
                                - \tweak bound-details.right.padding #1.25                               %! PIC
                                - \tweak bound-details.right.stencil-align-dir-y #center                 %! PIC
                                \startTextSpan                                                           %! PIC
                                [
                <BLANKLINE>
                                d''8
                <BLANKLINE>
                                f'8
                <BLANKLINE>
                                e''8
                                ]
                <BLANKLINE>
                                % [MusicVoice measure 2]                                                 %! SM4
                                g'8
                                [
                <BLANKLINE>
                                f''8
                <BLANKLINE>
                                e'8
                                ]
                <BLANKLINE>
                                % [MusicVoice measure 3]                                                 %! SM4
                                d''8
                                [
                <BLANKLINE>
                                f'8
                <BLANKLINE>
                                e''8
                <BLANKLINE>
                                g'8
                                ]
                <BLANKLINE>
                                % [MusicVoice measure 4]                                                 %! SM4
                                f''8
                                [
                <BLANKLINE>
                                e'8
                <BLANKLINE>
                                d''8
                                \stopTextSpan                                                            %! PIC
                                ]
                                \revert TextSpanner.staff-padding                                        %! OC2
                <BLANKLINE>
                            }
                        }
                    >>
                >>

            Solid line with arrow:

            >>> maker = baca.SegmentMaker(
            ...     score_template=baca.SingleStaffScoreTemplate(),
            ...     spacing=baca.minimum_duration((1, 12)),
            ...     time_signatures=[(4, 8), (3, 8), (4, 8), (3, 8)],
            ...     )

            >>> maker(
            ...     'MusicVoice',
            ...     baca.new_text_spanner(
            ...         baca.markups.pont(),
            ...         '->',
            ...         baca.markups.ord(),
            ...     ),
            ...     baca.make_even_divisions(),
            ...     baca.pitches('E4 D5 F4 E5 G4 F5'),
            ...     baca.text_spanner_staff_padding(4.5),
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
                            \baca_new_spacing_section #1 #12                                             %! HSS1:SPACING
                            \time 4/8                                                                    %! SM8:EXPLICIT_TIME_SIGNATURE:SM1
                            \once \override Score.TimeSignature.color = #(x11-color 'blue)               %! SM6:EXPLICIT_TIME_SIGNATURE_COLOR:SM1
                            s1 * 1/2
                <BLANKLINE>
                            % [GlobalSkips measure 2]                                                    %! SM4
                            \baca_new_spacing_section #1 #12                                             %! HSS1:SPACING
                            \time 3/8                                                                    %! SM8:EXPLICIT_TIME_SIGNATURE:SM1
                            \once \override Score.TimeSignature.color = #(x11-color 'blue)               %! SM6:EXPLICIT_TIME_SIGNATURE_COLOR:SM1
                            s1 * 3/8
                <BLANKLINE>
                            % [GlobalSkips measure 3]                                                    %! SM4
                            \baca_new_spacing_section #1 #12                                             %! HSS1:SPACING
                            \time 4/8                                                                    %! SM8:EXPLICIT_TIME_SIGNATURE:SM1
                            \once \override Score.TimeSignature.color = #(x11-color 'blue)               %! SM6:EXPLICIT_TIME_SIGNATURE_COLOR:SM1
                            s1 * 1/2
                <BLANKLINE>
                            % [GlobalSkips measure 4]                                                    %! SM4
                            \baca_new_spacing_section #1 #12                                             %! HSS1:SPACING
                            \time 3/8                                                                    %! SM8:EXPLICIT_TIME_SIGNATURE:SM1
                            \once \override Score.TimeSignature.color = #(x11-color 'blue)               %! SM6:EXPLICIT_TIME_SIGNATURE_COLOR:SM1
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
                <BLANKLINE>
                                % [MusicVoice measure 1]                                                 %! SM4
                                \override TextSpanner.staff-padding = #4.5                               %! OC1
                                e'8
                                - \abjad_solid_line_with_arrow                                           %! PIC
                                - \tweak bound-details.left.text \markup {                               %! PIC
                                    \concat                                                              %! PIC
                                        {                                                                %! PIC
                                            \upright                                                     %! PIC
                                                pont.                                                    %! PIC
                                            \hspace                                                      %! PIC
                                                #0.5                                                     %! PIC
                                        }                                                                %! PIC
                                    }                                                                    %! PIC
                                - \tweak bound-details.right.text \markup {                              %! PIC
                                    \upright                                                             %! PIC
                                        ord.                                                             %! PIC
                                    }                                                                    %! PIC
                                - \tweak bound-details.right.padding #0.5                                %! PIC
                                - \tweak bound-details.right.stencil-align-dir-y #center                 %! PIC
                                \startTextSpan                                                           %! PIC
                                [
                <BLANKLINE>
                                d''8
                <BLANKLINE>
                                f'8
                <BLANKLINE>
                                e''8
                                ]
                <BLANKLINE>
                                % [MusicVoice measure 2]                                                 %! SM4
                                g'8
                                [
                <BLANKLINE>
                                f''8
                <BLANKLINE>
                                e'8
                                ]
                <BLANKLINE>
                                % [MusicVoice measure 3]                                                 %! SM4
                                d''8
                                [
                <BLANKLINE>
                                f'8
                <BLANKLINE>
                                e''8
                <BLANKLINE>
                                g'8
                                ]
                <BLANKLINE>
                                % [MusicVoice measure 4]                                                 %! SM4
                                f''8
                                [
                <BLANKLINE>
                                e'8
                <BLANKLINE>
                                d''8
                                \stopTextSpan                                                            %! PIC
                                ]
                                \revert TextSpanner.staff-padding                                        %! OC2
                <BLANKLINE>
                            }
                        }
                    >>
                >>

            Solid line with hook:

            >>> maker = baca.SegmentMaker(
            ...     score_template=baca.SingleStaffScoreTemplate(),
            ...     spacing=baca.minimum_duration((1, 12)),
            ...     time_signatures=[(4, 8), (3, 8), (4, 8), (3, 8)],
            ...     )

            >>> maker(
            ...     'MusicVoice',
            ...     baca.new_text_spanner(
            ...         baca.markups.pont(),
            ...         '-|',
            ...         baca.markups.ord(),
            ...     ),
            ...     baca.make_even_divisions(),
            ...     baca.pitches('E4 D5 F4 E5 G4 F5'),
            ...     baca.text_spanner_staff_padding(4.5),
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
                            \baca_new_spacing_section #1 #12                                             %! HSS1:SPACING
                            \time 4/8                                                                    %! SM8:EXPLICIT_TIME_SIGNATURE:SM1
                            \once \override Score.TimeSignature.color = #(x11-color 'blue)               %! SM6:EXPLICIT_TIME_SIGNATURE_COLOR:SM1
                            s1 * 1/2
                <BLANKLINE>
                            % [GlobalSkips measure 2]                                                    %! SM4
                            \baca_new_spacing_section #1 #12                                             %! HSS1:SPACING
                            \time 3/8                                                                    %! SM8:EXPLICIT_TIME_SIGNATURE:SM1
                            \once \override Score.TimeSignature.color = #(x11-color 'blue)               %! SM6:EXPLICIT_TIME_SIGNATURE_COLOR:SM1
                            s1 * 3/8
                <BLANKLINE>
                            % [GlobalSkips measure 3]                                                    %! SM4
                            \baca_new_spacing_section #1 #12                                             %! HSS1:SPACING
                            \time 4/8                                                                    %! SM8:EXPLICIT_TIME_SIGNATURE:SM1
                            \once \override Score.TimeSignature.color = #(x11-color 'blue)               %! SM6:EXPLICIT_TIME_SIGNATURE_COLOR:SM1
                            s1 * 1/2
                <BLANKLINE>
                            % [GlobalSkips measure 4]                                                    %! SM4
                            \baca_new_spacing_section #1 #12                                             %! HSS1:SPACING
                            \time 3/8                                                                    %! SM8:EXPLICIT_TIME_SIGNATURE:SM1
                            \once \override Score.TimeSignature.color = #(x11-color 'blue)               %! SM6:EXPLICIT_TIME_SIGNATURE_COLOR:SM1
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
                <BLANKLINE>
                                % [MusicVoice measure 1]                                                 %! SM4
                                \override TextSpanner.staff-padding = #4.5                               %! OC1
                                e'8
                                - \abjad_solid_line_with_hook                                            %! PIC
                                - \tweak bound-details.left.text \markup {                               %! PIC
                                    \concat                                                              %! PIC
                                        {                                                                %! PIC
                                            \upright                                                     %! PIC
                                                pont.                                                    %! PIC
                                            \hspace                                                      %! PIC
                                                #0.5                                                     %! PIC
                                        }                                                                %! PIC
                                    }                                                                    %! PIC
                                - \tweak bound-details.right.text \markup {                              %! PIC
                                    \concat                                                              %! PIC
                                        {                                                                %! PIC
                                            \raise                                                       %! PIC
                                                #-1                                                      %! PIC
                                                \draw-line                                               %! PIC
                                                    #'(0 . -1)                                           %! PIC
                                            \hspace                                                      %! PIC
                                                #0.75                                                    %! PIC
                                            \general-align                                               %! PIC
                                                #Y                                                       %! PIC
                                                #1                                                       %! PIC
                                                \upright                                                 %! PIC
                                                    ord.                                                 %! PIC
                                        }                                                                %! PIC
                                    }                                                                    %! PIC
                                - \tweak bound-details.right.padding #1.25                               %! PIC
                                - \tweak bound-details.right.stencil-align-dir-y #center                 %! PIC
                                \startTextSpan                                                           %! PIC
                                [
                <BLANKLINE>
                                d''8
                <BLANKLINE>
                                f'8
                <BLANKLINE>
                                e''8
                                ]
                <BLANKLINE>
                                % [MusicVoice measure 2]                                                 %! SM4
                                g'8
                                [
                <BLANKLINE>
                                f''8
                <BLANKLINE>
                                e'8
                                ]
                <BLANKLINE>
                                % [MusicVoice measure 3]                                                 %! SM4
                                d''8
                                [
                <BLANKLINE>
                                f'8
                <BLANKLINE>
                                e''8
                <BLANKLINE>
                                g'8
                                ]
                <BLANKLINE>
                                % [MusicVoice measure 4]                                                 %! SM4
                                f''8
                                [
                <BLANKLINE>
                                e'8
                <BLANKLINE>
                                d''8
                                \stopTextSpan                                                            %! PIC
                                ]
                                \revert TextSpanner.staff-padding                                        %! OC2
                <BLANKLINE>
                            }
                        }
                    >>
                >>

            Invisible lines:

            >>> maker = baca.SegmentMaker(
            ...     score_template=baca.SingleStaffScoreTemplate(),
            ...     spacing=baca.minimum_duration((1, 12)),
            ...     time_signatures=[(4, 8), (3, 8), (4, 8), (3, 8)],
            ...     )

            >>> maker(
            ...     'MusicVoice',
            ...     baca.new_text_spanner(
            ...         baca.markups.pont(),
            ...         baca.markups.ord(),
            ...     ),
            ...     baca.make_even_divisions(),
            ...     baca.pitches('E4 D5 F4 E5 G4 F5'),
            ...     baca.text_spanner_staff_padding(4.5),
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
                            \baca_new_spacing_section #1 #12                                             %! HSS1:SPACING
                            \time 4/8                                                                    %! SM8:EXPLICIT_TIME_SIGNATURE:SM1
                            \once \override Score.TimeSignature.color = #(x11-color 'blue)               %! SM6:EXPLICIT_TIME_SIGNATURE_COLOR:SM1
                            s1 * 1/2
                <BLANKLINE>
                            % [GlobalSkips measure 2]                                                    %! SM4
                            \baca_new_spacing_section #1 #12                                             %! HSS1:SPACING
                            \time 3/8                                                                    %! SM8:EXPLICIT_TIME_SIGNATURE:SM1
                            \once \override Score.TimeSignature.color = #(x11-color 'blue)               %! SM6:EXPLICIT_TIME_SIGNATURE_COLOR:SM1
                            s1 * 3/8
                <BLANKLINE>
                            % [GlobalSkips measure 3]                                                    %! SM4
                            \baca_new_spacing_section #1 #12                                             %! HSS1:SPACING
                            \time 4/8                                                                    %! SM8:EXPLICIT_TIME_SIGNATURE:SM1
                            \once \override Score.TimeSignature.color = #(x11-color 'blue)               %! SM6:EXPLICIT_TIME_SIGNATURE_COLOR:SM1
                            s1 * 1/2
                <BLANKLINE>
                            % [GlobalSkips measure 4]                                                    %! SM4
                            \baca_new_spacing_section #1 #12                                             %! HSS1:SPACING
                            \time 3/8                                                                    %! SM8:EXPLICIT_TIME_SIGNATURE:SM1
                            \once \override Score.TimeSignature.color = #(x11-color 'blue)               %! SM6:EXPLICIT_TIME_SIGNATURE_COLOR:SM1
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
                <BLANKLINE>
                                % [MusicVoice measure 1]                                                 %! SM4
                                \override TextSpanner.staff-padding = #4.5                               %! OC1
                                e'8
                                - \abjad_invisible_line                                                  %! PIC
                                - \tweak bound-details.left.text \markup {                               %! PIC
                                    \concat                                                              %! PIC
                                        {                                                                %! PIC
                                            \upright                                                     %! PIC
                                                pont.                                                    %! PIC
                                            \hspace                                                      %! PIC
                                                #0.5                                                     %! PIC
                                        }                                                                %! PIC
                                    }                                                                    %! PIC
                                - \tweak bound-details.right.text \markup {                              %! PIC
                                    \upright                                                             %! PIC
                                        ord.                                                             %! PIC
                                    }                                                                    %! PIC
                                - \tweak bound-details.right.padding #0.5                                %! PIC
                                - \tweak bound-details.right.stencil-align-dir-y #center                 %! PIC
                                \startTextSpan                                                           %! PIC
                                [
                <BLANKLINE>
                                d''8
                <BLANKLINE>
                                f'8
                <BLANKLINE>
                                e''8
                                ]
                <BLANKLINE>
                                % [MusicVoice measure 2]                                                 %! SM4
                                g'8
                                [
                <BLANKLINE>
                                f''8
                <BLANKLINE>
                                e'8
                                ]
                <BLANKLINE>
                                % [MusicVoice measure 3]                                                 %! SM4
                                d''8
                                [
                <BLANKLINE>
                                f'8
                <BLANKLINE>
                                e''8
                <BLANKLINE>
                                g'8
                                ]
                <BLANKLINE>
                                % [MusicVoice measure 4]                                                 %! SM4
                                f''8
                                [
                <BLANKLINE>
                                e'8
                <BLANKLINE>
                                d''8
                                \stopTextSpan                                                            %! PIC
                                ]
                                \revert TextSpanner.staff-padding                                        %! OC2
                <BLANKLINE>
                            }
                        }
                    >>
                >>

        ..  container:: example

            Piece selector groups leaves by measures:

            >>> maker = baca.SegmentMaker(
            ...     score_template=baca.SingleStaffScoreTemplate(),
            ...     spacing=baca.minimum_duration((1, 12)),
            ...     time_signatures=[(4, 8), (3, 8), (4, 8), (3, 8)],
            ...     )

            >>> maker(
            ...     'MusicVoice',
            ...     baca.dls_staff_padding(5),
            ...     baca.new_text_spanner(
            ...         'A',
            ...         'B',
            ...         piece_selector=baca.group_by_measures([1]),
            ...     ),
            ...     baca.make_even_divisions(),
            ...     baca.pitches('E4 D5 F4 E5 G4 F5'),
            ...     baca.text_spanner_staff_padding(4.5),
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
                            \baca_new_spacing_section #1 #12                                             %! HSS1:SPACING
                            \time 4/8                                                                    %! SM8:EXPLICIT_TIME_SIGNATURE:SM1
                            \once \override Score.TimeSignature.color = #(x11-color 'blue)               %! SM6:EXPLICIT_TIME_SIGNATURE_COLOR:SM1
                            s1 * 1/2
                <BLANKLINE>
                            % [GlobalSkips measure 2]                                                    %! SM4
                            \baca_new_spacing_section #1 #12                                             %! HSS1:SPACING
                            \time 3/8                                                                    %! SM8:EXPLICIT_TIME_SIGNATURE:SM1
                            \once \override Score.TimeSignature.color = #(x11-color 'blue)               %! SM6:EXPLICIT_TIME_SIGNATURE_COLOR:SM1
                            s1 * 3/8
                <BLANKLINE>
                            % [GlobalSkips measure 3]                                                    %! SM4
                            \baca_new_spacing_section #1 #12                                             %! HSS1:SPACING
                            \time 4/8                                                                    %! SM8:EXPLICIT_TIME_SIGNATURE:SM1
                            \once \override Score.TimeSignature.color = #(x11-color 'blue)               %! SM6:EXPLICIT_TIME_SIGNATURE_COLOR:SM1
                            s1 * 1/2
                <BLANKLINE>
                            % [GlobalSkips measure 4]                                                    %! SM4
                            \baca_new_spacing_section #1 #12                                             %! HSS1:SPACING
                            \time 3/8                                                                    %! SM8:EXPLICIT_TIME_SIGNATURE:SM1
                            \once \override Score.TimeSignature.color = #(x11-color 'blue)               %! SM6:EXPLICIT_TIME_SIGNATURE_COLOR:SM1
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
                <BLANKLINE>
                                % [MusicVoice measure 1]                                                 %! SM4
                                \override DynamicLineSpanner.staff-padding = #'5                         %! OC1
                                \override TextSpanner.staff-padding = #4.5                               %! OC1
                                e'8
                                - \abjad_invisible_line                                                  %! PIC
                                - \tweak bound-details.left.text \markup {                               %! PIC
                                    \concat                                                              %! PIC
                                        {                                                                %! PIC
                                            \upright                                                     %! PIC
                                                A                                                        %! PIC
                                            \hspace                                                      %! PIC
                                                #0.5                                                     %! PIC
                                        }                                                                %! PIC
                                    }                                                                    %! PIC
                                \startTextSpan                                                           %! PIC
                                [
                <BLANKLINE>
                                d''8
                <BLANKLINE>
                                f'8
                <BLANKLINE>
                                e''8
                                ]
                <BLANKLINE>
                                % [MusicVoice measure 2]                                                 %! SM4
                                g'8
                                \stopTextSpan                                                            %! PIC
                                - \abjad_invisible_line                                                  %! PIC
                                - \tweak bound-details.left.text \markup {                               %! PIC
                                    \concat                                                              %! PIC
                                        {                                                                %! PIC
                                            \upright                                                     %! PIC
                                                B                                                        %! PIC
                                            \hspace                                                      %! PIC
                                                #0.5                                                     %! PIC
                                        }                                                                %! PIC
                                    }                                                                    %! PIC
                                \startTextSpan                                                           %! PIC
                                [
                <BLANKLINE>
                                f''8
                <BLANKLINE>
                                e'8
                                ]
                <BLANKLINE>
                                % [MusicVoice measure 3]                                                 %! SM4
                                d''8
                                \stopTextSpan                                                            %! PIC
                                - \abjad_invisible_line                                                  %! PIC
                                - \tweak bound-details.left.text \markup {                               %! PIC
                                    \concat                                                              %! PIC
                                        {                                                                %! PIC
                                            \upright                                                     %! PIC
                                                A                                                        %! PIC
                                            \hspace                                                      %! PIC
                                                #0.5                                                     %! PIC
                                        }                                                                %! PIC
                                    }                                                                    %! PIC
                                \startTextSpan                                                           %! PIC
                                [
                <BLANKLINE>
                                f'8
                <BLANKLINE>
                                e''8
                <BLANKLINE>
                                g'8
                                ]
                <BLANKLINE>
                                % [MusicVoice measure 4]                                                 %! SM4
                                f''8
                                \stopTextSpan                                                            %! PIC
                                - \abjad_invisible_line                                                  %! PIC
                                - \tweak bound-details.left.text \markup {                               %! PIC
                                    \concat                                                              %! PIC
                                        {                                                                %! PIC
                                            \upright                                                     %! PIC
                                                B                                                        %! PIC
                                            \hspace                                                      %! PIC
                                                #0.5                                                     %! PIC
                                        }                                                                %! PIC
                                    }                                                                    %! PIC
                                - \tweak bound-details.right.text \markup {                              %! PIC
                                    \upright                                                             %! PIC
                                        A                                                                %! PIC
                                    }                                                                    %! PIC
                                - \tweak bound-details.right.padding #0.5                                %! PIC
                                - \tweak bound-details.right.stencil-align-dir-y #center                 %! PIC
                                \startTextSpan                                                           %! PIC
                                [
                <BLANKLINE>
                                e'8
                <BLANKLINE>
                                d''8
                                \stopTextSpan                                                            %! PIC
                                ]
                                \revert DynamicLineSpanner.staff-padding                                 %! OC2
                                \revert TextSpanner.staff-padding                                        %! OC2
                <BLANKLINE>
                            }
                        }
                    >>
                >>

            With spanners:

            >>> maker = baca.SegmentMaker(
            ...     score_template=baca.SingleStaffScoreTemplate(),
            ...     spacing=baca.minimum_duration((1, 12)),
            ...     time_signatures=[(4, 8), (3, 8), (4, 8), (3, 8)],
            ...     )

            >>> maker(
            ...     'MusicVoice',
            ...     baca.dls_staff_padding(5),
            ...     baca.new_text_spanner(
            ...         'A',
            ...         '->',
            ...         'B',
            ...         '->',
            ...         piece_selector=baca.group_by_measures([1]),
            ...     ),
            ...     baca.make_even_divisions(),
            ...     baca.pitches('E4 D5 F4 E5 G4 F5'),
            ...     baca.text_spanner_staff_padding(4.5),
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
                            \baca_new_spacing_section #1 #12                                             %! HSS1:SPACING
                            \time 4/8                                                                    %! SM8:EXPLICIT_TIME_SIGNATURE:SM1
                            \once \override Score.TimeSignature.color = #(x11-color 'blue)               %! SM6:EXPLICIT_TIME_SIGNATURE_COLOR:SM1
                            s1 * 1/2
                <BLANKLINE>
                            % [GlobalSkips measure 2]                                                    %! SM4
                            \baca_new_spacing_section #1 #12                                             %! HSS1:SPACING
                            \time 3/8                                                                    %! SM8:EXPLICIT_TIME_SIGNATURE:SM1
                            \once \override Score.TimeSignature.color = #(x11-color 'blue)               %! SM6:EXPLICIT_TIME_SIGNATURE_COLOR:SM1
                            s1 * 3/8
                <BLANKLINE>
                            % [GlobalSkips measure 3]                                                    %! SM4
                            \baca_new_spacing_section #1 #12                                             %! HSS1:SPACING
                            \time 4/8                                                                    %! SM8:EXPLICIT_TIME_SIGNATURE:SM1
                            \once \override Score.TimeSignature.color = #(x11-color 'blue)               %! SM6:EXPLICIT_TIME_SIGNATURE_COLOR:SM1
                            s1 * 1/2
                <BLANKLINE>
                            % [GlobalSkips measure 4]                                                    %! SM4
                            \baca_new_spacing_section #1 #12                                             %! HSS1:SPACING
                            \time 3/8                                                                    %! SM8:EXPLICIT_TIME_SIGNATURE:SM1
                            \once \override Score.TimeSignature.color = #(x11-color 'blue)               %! SM6:EXPLICIT_TIME_SIGNATURE_COLOR:SM1
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
                <BLANKLINE>
                                % [MusicVoice measure 1]                                                 %! SM4
                                \override DynamicLineSpanner.staff-padding = #'5                         %! OC1
                                \override TextSpanner.staff-padding = #4.5                               %! OC1
                                e'8
                                - \abjad_solid_line_with_arrow                                           %! PIC
                                - \tweak bound-details.left.text \markup {                               %! PIC
                                    \concat                                                              %! PIC
                                        {                                                                %! PIC
                                            \upright                                                     %! PIC
                                                A                                                        %! PIC
                                            \hspace                                                      %! PIC
                                                #0.5                                                     %! PIC
                                        }                                                                %! PIC
                                    }                                                                    %! PIC
                                \startTextSpan                                                           %! PIC
                                [
                <BLANKLINE>
                                d''8
                <BLANKLINE>
                                f'8
                <BLANKLINE>
                                e''8
                                ]
                <BLANKLINE>
                                % [MusicVoice measure 2]                                                 %! SM4
                                g'8
                                \stopTextSpan                                                            %! PIC
                                - \abjad_solid_line_with_arrow                                           %! PIC
                                - \tweak bound-details.left.text \markup {                               %! PIC
                                    \concat                                                              %! PIC
                                        {                                                                %! PIC
                                            \upright                                                     %! PIC
                                                B                                                        %! PIC
                                            \hspace                                                      %! PIC
                                                #0.5                                                     %! PIC
                                        }                                                                %! PIC
                                    }                                                                    %! PIC
                                \startTextSpan                                                           %! PIC
                                [
                <BLANKLINE>
                                f''8
                <BLANKLINE>
                                e'8
                                ]
                <BLANKLINE>
                                % [MusicVoice measure 3]                                                 %! SM4
                                d''8
                                \stopTextSpan                                                            %! PIC
                                - \abjad_solid_line_with_arrow                                           %! PIC
                                - \tweak bound-details.left.text \markup {                               %! PIC
                                    \concat                                                              %! PIC
                                        {                                                                %! PIC
                                            \upright                                                     %! PIC
                                                A                                                        %! PIC
                                            \hspace                                                      %! PIC
                                                #0.5                                                     %! PIC
                                        }                                                                %! PIC
                                    }                                                                    %! PIC
                                \startTextSpan                                                           %! PIC
                                [
                <BLANKLINE>
                                f'8
                <BLANKLINE>
                                e''8
                <BLANKLINE>
                                g'8
                                ]
                <BLANKLINE>
                                % [MusicVoice measure 4]                                                 %! SM4
                                f''8
                                \stopTextSpan                                                            %! PIC
                                - \abjad_solid_line_with_arrow                                           %! PIC
                                - \tweak bound-details.left.text \markup {                               %! PIC
                                    \concat                                                              %! PIC
                                        {                                                                %! PIC
                                            \upright                                                     %! PIC
                                                B                                                        %! PIC
                                            \hspace                                                      %! PIC
                                                #0.5                                                     %! PIC
                                        }                                                                %! PIC
                                    }                                                                    %! PIC
                                - \tweak bound-details.right.text \markup {                              %! PIC
                                    \upright                                                             %! PIC
                                        A                                                                %! PIC
                                    }                                                                    %! PIC
                                - \tweak bound-details.right.padding #0.5                                %! PIC
                                - \tweak bound-details.right.stencil-align-dir-y #center                 %! PIC
                                \startTextSpan                                                           %! PIC
                                [
                <BLANKLINE>
                                e'8
                <BLANKLINE>
                                d''8
                                \stopTextSpan                                                            %! PIC
                                ]
                                \revert DynamicLineSpanner.staff-padding                                 %! OC2
                                \revert TextSpanner.staff-padding                                        %! OC2
                <BLANKLINE>
                            }
                        }
                    >>
                >>

            Bookends each piece:

            >>> maker = baca.SegmentMaker(
            ...     score_template=baca.SingleStaffScoreTemplate(),
            ...     spacing=baca.minimum_duration((1, 12)),
            ...     time_signatures=[(4, 8), (3, 8), (4, 8), (3, 8)],
            ...     )

            >>> maker(
            ...     'MusicVoice',
            ...     baca.dls_staff_padding(5),
            ...     baca.new_text_spanner(
            ...         'A',
            ...         'B',
            ...         bookend=True,
            ...         piece_selector=baca.group_by_measures([1]),
            ...     ),
            ...     baca.make_even_divisions(),
            ...     baca.pitches('E4 D5 F4 E5 G4 F5'),
            ...     baca.text_spanner_staff_padding(4.5),
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
                            \baca_new_spacing_section #1 #12                                             %! HSS1:SPACING
                            \time 4/8                                                                    %! SM8:EXPLICIT_TIME_SIGNATURE:SM1
                            \once \override Score.TimeSignature.color = #(x11-color 'blue)               %! SM6:EXPLICIT_TIME_SIGNATURE_COLOR:SM1
                            s1 * 1/2
                <BLANKLINE>
                            % [GlobalSkips measure 2]                                                    %! SM4
                            \baca_new_spacing_section #1 #12                                             %! HSS1:SPACING
                            \time 3/8                                                                    %! SM8:EXPLICIT_TIME_SIGNATURE:SM1
                            \once \override Score.TimeSignature.color = #(x11-color 'blue)               %! SM6:EXPLICIT_TIME_SIGNATURE_COLOR:SM1
                            s1 * 3/8
                <BLANKLINE>
                            % [GlobalSkips measure 3]                                                    %! SM4
                            \baca_new_spacing_section #1 #12                                             %! HSS1:SPACING
                            \time 4/8                                                                    %! SM8:EXPLICIT_TIME_SIGNATURE:SM1
                            \once \override Score.TimeSignature.color = #(x11-color 'blue)               %! SM6:EXPLICIT_TIME_SIGNATURE_COLOR:SM1
                            s1 * 1/2
                <BLANKLINE>
                            % [GlobalSkips measure 4]                                                    %! SM4
                            \baca_new_spacing_section #1 #12                                             %! HSS1:SPACING
                            \time 3/8                                                                    %! SM8:EXPLICIT_TIME_SIGNATURE:SM1
                            \once \override Score.TimeSignature.color = #(x11-color 'blue)               %! SM6:EXPLICIT_TIME_SIGNATURE_COLOR:SM1
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
                <BLANKLINE>
                                % [MusicVoice measure 1]                                                 %! SM4
                                \override DynamicLineSpanner.staff-padding = #'5                         %! OC1
                                \override TextSpanner.staff-padding = #4.5                               %! OC1
                                e'8
                                - \abjad_invisible_line                                                  %! PIC
                                - \tweak bound-details.left.text \markup {                               %! PIC
                                    \concat                                                              %! PIC
                                        {                                                                %! PIC
                                            \upright                                                     %! PIC
                                                A                                                        %! PIC
                                            \hspace                                                      %! PIC
                                                #0.5                                                     %! PIC
                                        }                                                                %! PIC
                                    }                                                                    %! PIC
                                - \tweak bound-details.right.text \markup {                              %! PIC
                                    \upright                                                             %! PIC
                                        B                                                                %! PIC
                                    }                                                                    %! PIC
                                - \tweak bound-details.right.padding #0.5                                %! PIC
                                - \tweak bound-details.right.stencil-align-dir-y #center                 %! PIC
                                \startTextSpan                                                           %! PIC
                                [
                <BLANKLINE>
                                d''8
                <BLANKLINE>
                                f'8
                <BLANKLINE>
                                e''8
                                \stopTextSpan                                                            %! PIC
                                ]
                <BLANKLINE>
                                % [MusicVoice measure 2]                                                 %! SM4
                                g'8
                                \stopTextSpan                                                            %! PIC
                                - \abjad_invisible_line                                                  %! PIC
                                - \tweak bound-details.left.text \markup {                               %! PIC
                                    \concat                                                              %! PIC
                                        {                                                                %! PIC
                                            \upright                                                     %! PIC
                                                B                                                        %! PIC
                                            \hspace                                                      %! PIC
                                                #0.5                                                     %! PIC
                                        }                                                                %! PIC
                                    }                                                                    %! PIC
                                - \tweak bound-details.right.text \markup {                              %! PIC
                                    \upright                                                             %! PIC
                                        A                                                                %! PIC
                                    }                                                                    %! PIC
                                - \tweak bound-details.right.padding #0.5                                %! PIC
                                - \tweak bound-details.right.stencil-align-dir-y #center                 %! PIC
                                \startTextSpan                                                           %! PIC
                                [
                <BLANKLINE>
                                f''8
                <BLANKLINE>
                                e'8
                                \stopTextSpan                                                            %! PIC
                                ]
                <BLANKLINE>
                                % [MusicVoice measure 3]                                                 %! SM4
                                d''8
                                \stopTextSpan                                                            %! PIC
                                - \abjad_invisible_line                                                  %! PIC
                                - \tweak bound-details.left.text \markup {                               %! PIC
                                    \concat                                                              %! PIC
                                        {                                                                %! PIC
                                            \upright                                                     %! PIC
                                                A                                                        %! PIC
                                            \hspace                                                      %! PIC
                                                #0.5                                                     %! PIC
                                        }                                                                %! PIC
                                    }                                                                    %! PIC
                                - \tweak bound-details.right.text \markup {                              %! PIC
                                    \upright                                                             %! PIC
                                        B                                                                %! PIC
                                    }                                                                    %! PIC
                                - \tweak bound-details.right.padding #0.5                                %! PIC
                                - \tweak bound-details.right.stencil-align-dir-y #center                 %! PIC
                                \startTextSpan                                                           %! PIC
                                [
                <BLANKLINE>
                                f'8
                <BLANKLINE>
                                e''8
                <BLANKLINE>
                                g'8
                                \stopTextSpan                                                            %! PIC
                                ]
                <BLANKLINE>
                                % [MusicVoice measure 4]                                                 %! SM4
                                f''8
                                \stopTextSpan                                                            %! PIC
                                - \abjad_invisible_line                                                  %! PIC
                                - \tweak bound-details.left.text \markup {                               %! PIC
                                    \concat                                                              %! PIC
                                        {                                                                %! PIC
                                            \upright                                                     %! PIC
                                                B                                                        %! PIC
                                            \hspace                                                      %! PIC
                                                #0.5                                                     %! PIC
                                        }                                                                %! PIC
                                    }                                                                    %! PIC
                                - \tweak bound-details.right.text \markup {                              %! PIC
                                    \upright                                                             %! PIC
                                        A                                                                %! PIC
                                    }                                                                    %! PIC
                                - \tweak bound-details.right.padding #0.5                                %! PIC
                                - \tweak bound-details.right.stencil-align-dir-y #center                 %! PIC
                                \startTextSpan                                                           %! PIC
                                [
                <BLANKLINE>
                                e'8
                <BLANKLINE>
                                d''8
                                \stopTextSpan                                                            %! PIC
                                ]
                                \revert DynamicLineSpanner.staff-padding                                 %! OC2
                                \revert TextSpanner.staff-padding                                        %! OC2
                <BLANKLINE>
                            }
                        }
                    >>
                >>

            With spanners:

            >>> maker = baca.SegmentMaker(
            ...     score_template=baca.SingleStaffScoreTemplate(),
            ...     spacing=baca.minimum_duration((1, 12)),
            ...     time_signatures=[(4, 8), (3, 8), (4, 8), (3, 8)],
            ...     )

            >>> maker(
            ...     'MusicVoice',
            ...     baca.dls_staff_padding(5),
            ...     baca.new_text_spanner(
            ...         'A',
            ...         '->',
            ...         'B',
            ...         '->',
            ...         bookend=True,
            ...         piece_selector=baca.group_by_measures([1]),
            ...     ),
            ...     baca.make_even_divisions(),
            ...     baca.pitches('E4 D5 F4 E5 G4 F5'),
            ...     baca.text_spanner_staff_padding(4.5),
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
                            \baca_new_spacing_section #1 #12                                             %! HSS1:SPACING
                            \time 4/8                                                                    %! SM8:EXPLICIT_TIME_SIGNATURE:SM1
                            \once \override Score.TimeSignature.color = #(x11-color 'blue)               %! SM6:EXPLICIT_TIME_SIGNATURE_COLOR:SM1
                            s1 * 1/2
                <BLANKLINE>
                            % [GlobalSkips measure 2]                                                    %! SM4
                            \baca_new_spacing_section #1 #12                                             %! HSS1:SPACING
                            \time 3/8                                                                    %! SM8:EXPLICIT_TIME_SIGNATURE:SM1
                            \once \override Score.TimeSignature.color = #(x11-color 'blue)               %! SM6:EXPLICIT_TIME_SIGNATURE_COLOR:SM1
                            s1 * 3/8
                <BLANKLINE>
                            % [GlobalSkips measure 3]                                                    %! SM4
                            \baca_new_spacing_section #1 #12                                             %! HSS1:SPACING
                            \time 4/8                                                                    %! SM8:EXPLICIT_TIME_SIGNATURE:SM1
                            \once \override Score.TimeSignature.color = #(x11-color 'blue)               %! SM6:EXPLICIT_TIME_SIGNATURE_COLOR:SM1
                            s1 * 1/2
                <BLANKLINE>
                            % [GlobalSkips measure 4]                                                    %! SM4
                            \baca_new_spacing_section #1 #12                                             %! HSS1:SPACING
                            \time 3/8                                                                    %! SM8:EXPLICIT_TIME_SIGNATURE:SM1
                            \once \override Score.TimeSignature.color = #(x11-color 'blue)               %! SM6:EXPLICIT_TIME_SIGNATURE_COLOR:SM1
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
                <BLANKLINE>
                                % [MusicVoice measure 1]                                                 %! SM4
                                \override DynamicLineSpanner.staff-padding = #'5                         %! OC1
                                \override TextSpanner.staff-padding = #4.5                               %! OC1
                                e'8
                                - \abjad_solid_line_with_arrow                                           %! PIC
                                - \tweak bound-details.left.text \markup {                               %! PIC
                                    \concat                                                              %! PIC
                                        {                                                                %! PIC
                                            \upright                                                     %! PIC
                                                A                                                        %! PIC
                                            \hspace                                                      %! PIC
                                                #0.5                                                     %! PIC
                                        }                                                                %! PIC
                                    }                                                                    %! PIC
                                - \tweak bound-details.right.text \markup {                              %! PIC
                                    \upright                                                             %! PIC
                                        B                                                                %! PIC
                                    }                                                                    %! PIC
                                - \tweak bound-details.right.padding #0.5                                %! PIC
                                - \tweak bound-details.right.stencil-align-dir-y #center                 %! PIC
                                \startTextSpan                                                           %! PIC
                                [
                <BLANKLINE>
                                d''8
                <BLANKLINE>
                                f'8
                <BLANKLINE>
                                e''8
                                \stopTextSpan                                                            %! PIC
                                ]
                <BLANKLINE>
                                % [MusicVoice measure 2]                                                 %! SM4
                                g'8
                                \stopTextSpan                                                            %! PIC
                                - \abjad_solid_line_with_arrow                                           %! PIC
                                - \tweak bound-details.left.text \markup {                               %! PIC
                                    \concat                                                              %! PIC
                                        {                                                                %! PIC
                                            \upright                                                     %! PIC
                                                B                                                        %! PIC
                                            \hspace                                                      %! PIC
                                                #0.5                                                     %! PIC
                                        }                                                                %! PIC
                                    }                                                                    %! PIC
                                - \tweak bound-details.right.text \markup {                              %! PIC
                                    \upright                                                             %! PIC
                                        A                                                                %! PIC
                                    }                                                                    %! PIC
                                - \tweak bound-details.right.padding #0.5                                %! PIC
                                - \tweak bound-details.right.stencil-align-dir-y #center                 %! PIC
                                \startTextSpan                                                           %! PIC
                                [
                <BLANKLINE>
                                f''8
                <BLANKLINE>
                                e'8
                                \stopTextSpan                                                            %! PIC
                                ]
                <BLANKLINE>
                                % [MusicVoice measure 3]                                                 %! SM4
                                d''8
                                \stopTextSpan                                                            %! PIC
                                - \abjad_solid_line_with_arrow                                           %! PIC
                                - \tweak bound-details.left.text \markup {                               %! PIC
                                    \concat                                                              %! PIC
                                        {                                                                %! PIC
                                            \upright                                                     %! PIC
                                                A                                                        %! PIC
                                            \hspace                                                      %! PIC
                                                #0.5                                                     %! PIC
                                        }                                                                %! PIC
                                    }                                                                    %! PIC
                                - \tweak bound-details.right.text \markup {                              %! PIC
                                    \upright                                                             %! PIC
                                        B                                                                %! PIC
                                    }                                                                    %! PIC
                                - \tweak bound-details.right.padding #0.5                                %! PIC
                                - \tweak bound-details.right.stencil-align-dir-y #center                 %! PIC
                                \startTextSpan                                                           %! PIC
                                [
                <BLANKLINE>
                                f'8
                <BLANKLINE>
                                e''8
                <BLANKLINE>
                                g'8
                                \stopTextSpan                                                            %! PIC
                                ]
                <BLANKLINE>
                                % [MusicVoice measure 4]                                                 %! SM4
                                f''8
                                \stopTextSpan                                                            %! PIC
                                - \abjad_solid_line_with_arrow                                           %! PIC
                                - \tweak bound-details.left.text \markup {                               %! PIC
                                    \concat                                                              %! PIC
                                        {                                                                %! PIC
                                            \upright                                                     %! PIC
                                                B                                                        %! PIC
                                            \hspace                                                      %! PIC
                                                #0.5                                                     %! PIC
                                        }                                                                %! PIC
                                    }                                                                    %! PIC
                                - \tweak bound-details.right.text \markup {                              %! PIC
                                    \upright                                                             %! PIC
                                        A                                                                %! PIC
                                    }                                                                    %! PIC
                                - \tweak bound-details.right.padding #0.5                                %! PIC
                                - \tweak bound-details.right.stencil-align-dir-y #center                 %! PIC
                                \startTextSpan                                                           %! PIC
                                [
                <BLANKLINE>
                                e'8
                <BLANKLINE>
                                d''8
                                \stopTextSpan                                                            %! PIC
                                ]
                                \revert DynamicLineSpanner.staff-padding                                 %! OC2
                                \revert TextSpanner.staff-padding                                        %! OC2
                <BLANKLINE>
                            }
                        }
                    >>
                >>

        ..  container:: example

            REGRESSION. Bookended hooks are kerned:

            >>> maker = baca.SegmentMaker(
            ...     score_template=baca.SingleStaffScoreTemplate(),
            ...     spacing=baca.minimum_duration((1, 12)),
            ...     time_signatures=[(4, 8), (3, 8), (4, 8), (3, 8)],
            ...     )

            >>> maker(
            ...     'MusicVoice',
            ...     baca.dls_staff_padding(5),
            ...     baca.new_text_spanner(
            ...         'A',
            ...         '-|',
            ...         'B',
            ...         '-|',
            ...         piece_selector=baca.group_by_measures([1]),
            ...     ),
            ...     baca.make_even_divisions(),
            ...     baca.pitches('E4 D5 F4 E5 G4 F5'),
            ...     baca.text_spanner_staff_padding(4.5),
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
                            \baca_new_spacing_section #1 #12                                             %! HSS1:SPACING
                            \time 4/8                                                                    %! SM8:EXPLICIT_TIME_SIGNATURE:SM1
                            \once \override Score.TimeSignature.color = #(x11-color 'blue)               %! SM6:EXPLICIT_TIME_SIGNATURE_COLOR:SM1
                            s1 * 1/2
                <BLANKLINE>
                            % [GlobalSkips measure 2]                                                    %! SM4
                            \baca_new_spacing_section #1 #12                                             %! HSS1:SPACING
                            \time 3/8                                                                    %! SM8:EXPLICIT_TIME_SIGNATURE:SM1
                            \once \override Score.TimeSignature.color = #(x11-color 'blue)               %! SM6:EXPLICIT_TIME_SIGNATURE_COLOR:SM1
                            s1 * 3/8
                <BLANKLINE>
                            % [GlobalSkips measure 3]                                                    %! SM4
                            \baca_new_spacing_section #1 #12                                             %! HSS1:SPACING
                            \time 4/8                                                                    %! SM8:EXPLICIT_TIME_SIGNATURE:SM1
                            \once \override Score.TimeSignature.color = #(x11-color 'blue)               %! SM6:EXPLICIT_TIME_SIGNATURE_COLOR:SM1
                            s1 * 1/2
                <BLANKLINE>
                            % [GlobalSkips measure 4]                                                    %! SM4
                            \baca_new_spacing_section #1 #12                                             %! HSS1:SPACING
                            \time 3/8                                                                    %! SM8:EXPLICIT_TIME_SIGNATURE:SM1
                            \once \override Score.TimeSignature.color = #(x11-color 'blue)               %! SM6:EXPLICIT_TIME_SIGNATURE_COLOR:SM1
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
                <BLANKLINE>
                                % [MusicVoice measure 1]                                                 %! SM4
                                \override DynamicLineSpanner.staff-padding = #'5                         %! OC1
                                \override TextSpanner.staff-padding = #4.5                               %! OC1
                                e'8
                                - \abjad_solid_line_with_hook                                            %! PIC
                                - \tweak bound-details.left.text \markup {                               %! PIC
                                    \concat                                                              %! PIC
                                        {                                                                %! PIC
                                            \upright                                                     %! PIC
                                                A                                                        %! PIC
                                            \hspace                                                      %! PIC
                                                #0.5                                                     %! PIC
                                        }                                                                %! PIC
                                    }                                                                    %! PIC
                                \startTextSpan                                                           %! PIC
                                [
                <BLANKLINE>
                                d''8
                <BLANKLINE>
                                f'8
                <BLANKLINE>
                                e''8
                                ]
                <BLANKLINE>
                                % [MusicVoice measure 2]                                                 %! SM4
                                g'8
                                \stopTextSpan                                                            %! PIC
                                - \abjad_solid_line_with_hook                                            %! PIC
                                - \tweak bound-details.left.text \markup {                               %! PIC
                                    \concat                                                              %! PIC
                                        {                                                                %! PIC
                                            \upright                                                     %! PIC
                                                B                                                        %! PIC
                                            \hspace                                                      %! PIC
                                                #0.5                                                     %! PIC
                                        }                                                                %! PIC
                                    }                                                                    %! PIC
                                \startTextSpan                                                           %! PIC
                                [
                <BLANKLINE>
                                f''8
                <BLANKLINE>
                                e'8
                                ]
                <BLANKLINE>
                                % [MusicVoice measure 3]                                                 %! SM4
                                d''8
                                \stopTextSpan                                                            %! PIC
                                - \abjad_solid_line_with_hook                                            %! PIC
                                - \tweak bound-details.left.text \markup {                               %! PIC
                                    \concat                                                              %! PIC
                                        {                                                                %! PIC
                                            \upright                                                     %! PIC
                                                A                                                        %! PIC
                                            \hspace                                                      %! PIC
                                                #0.5                                                     %! PIC
                                        }                                                                %! PIC
                                    }                                                                    %! PIC
                                \startTextSpan                                                           %! PIC
                                [
                <BLANKLINE>
                                f'8
                <BLANKLINE>
                                e''8
                <BLANKLINE>
                                g'8
                                ]
                <BLANKLINE>
                                % [MusicVoice measure 4]                                                 %! SM4
                                f''8
                                \stopTextSpan                                                            %! PIC
                                - \abjad_solid_line_with_hook                                            %! PIC
                                - \tweak bound-details.left.text \markup {                               %! PIC
                                    \concat                                                              %! PIC
                                        {                                                                %! PIC
                                            \upright                                                     %! PIC
                                                B                                                        %! PIC
                                            \hspace                                                      %! PIC
                                                #0.5                                                     %! PIC
                                        }                                                                %! PIC
                                    }                                                                    %! PIC
                                - \tweak bound-details.right.text \markup {                              %! PIC
                                    \concat                                                              %! PIC
                                        {                                                                %! PIC
                                            \raise                                                       %! PIC
                                                #-1                                                      %! PIC
                                                \draw-line                                               %! PIC
                                                    #'(0 . -1)                                           %! PIC
                                            \hspace                                                      %! PIC
                                                #0.75                                                    %! PIC
                                            \general-align                                               %! PIC
                                                #Y                                                       %! PIC
                                                #1                                                       %! PIC
                                                \upright                                                 %! PIC
                                                    A                                                    %! PIC
                                        }                                                                %! PIC
                                    }                                                                    %! PIC
                                - \tweak bound-details.right.padding #1.25                               %! PIC
                                - \tweak bound-details.right.stencil-align-dir-y #center                 %! PIC
                                \startTextSpan                                                           %! PIC
                                [
                <BLANKLINE>
                                e'8
                <BLANKLINE>
                                d''8
                                \stopTextSpan                                                            %! PIC
                                ]
                                \revert DynamicLineSpanner.staff-padding                                 %! OC2
                                \revert TextSpanner.staff-padding                                        %! OC2
                <BLANKLINE>
                            }
                        }
                    >>
                >>

        """
        bundles = []
        if len(items) == 1:
            raise NotImplementedError('implement lone item')
        shape_to_style = abjad.StartTextSpan._shape_to_style
        if lilypond_id is None:
            command = r'\stopTextSpan'
        elif lilypond_id == 1:
            command = r'\stopTextSpanOne'
        elif lilypond_id == 2:
            command = r'\stopTextSpanTwo'
        elif lilypond_id == 3:
            command = r'\stopTextSpanThree'
        else:
            raise ValueError(lilypond_id)
        stop_text_span = abjad.StopTextSpan(command=command)
        items_ = abjad.CyclicTuple(items)
        for i, item in enumerate(items_):
            if item in shape_to_style:
                continue
            if isinstance(item, str):
                item_markup = abjad.Markup(item)
            else:
                item_markup = item
            assert isinstance(item_markup, abjad.Markup)
            if not no_upright:
                item_markup = item_markup.upright()
            style = 'invisible_line'
            if items_[i + 1] in shape_to_style:
                style = shape_to_style[items_[i + 1]]
                right_text = items_[i + 2]
            else:
                right_text = items_[i + 1]
            if isinstance(right_text, str):
                right_markup = abjad.Markup(right_text)
            else:
                assert isinstance(right_text, abjad.Markup)
                right_markup = right_text
            if not no_upright:
                right_markup = right_markup.upright()
            if lilypond_id is None:
                command = r'\startTextSpan'
            elif lilypond_id == 1:
                command = r'\startTextSpanOne'
            elif lilypond_id == 2:
                command = r'\startTextSpanTwo'
            elif lilypond_id == 3:
                command = r'\startTextSpanThree'
            else:
                raise ValueError(lilypond_id)
            start_text_span = abjad.StartTextSpan(
                command=command,
                left_text=item_markup,
                style=style,
                )
            if tweaks:
                library.apply_tweaks(start_text_span, tweaks)
            # kerns bookended hook
            if 'hook' in style:
                line = abjad.Markup.draw_line(0, -1)
                line = line.raise_(-1)
                hspace = abjad.Markup.hspace(0.75)
                right_markup = right_markup.general_align('Y', 1)
                right_markup = abjad.Markup.concat([line, hspace, right_markup])
            bookended_spanner_start = abjad.new(
                start_text_span,
                right_text=right_markup,
                )
            manager = abjad.tweak(bookended_spanner_start)
            manager.bound_details__right__stencil_align_dir_y = abjad.Center
            if 'hook' in style:
                manager.bound_details__right__padding = 1.25
            else:
                manager.bound_details__right__padding = 0.5
            bundle = IndicatorBundle(
                stop_text_span,
                start_text_span,
                bookended_spanner_start=bookended_spanner_start,
                enchained=True,
                )
            bundles.append(bundle)
        return PiecewiseIndicatorCommand(
            bookend=bookend,
            bundles=bundles,
            leak=leak,
            piece_selector=piece_selector,
            selector=selector,
            )
    
    @staticmethod
    def new_transition(
        *items: typing.Iterable[typing.Union[str, abjad.Markup, None]],
        selector: typings.Selector = 'baca.tleaves()',
        tweaks: typing.List[abjad.LilyPondTweakManager] = None,
        ):
        """
        Attaches text span indicators.
        """
        items_ = []
        for item in items:
            items_.append(item)
            items_.append('=>')
        return LibraryTZ.new_text_spanner(
            *items_,
            selector=selector,
            tweaks=tweaks,
            )

    @staticmethod
    def tenuto(
        *,
        selector: typings.Selector = 'baca.phead(0)',
        ) -> IndicatorCommand:
        r"""
        Attaches tenuto.

        ..  container:: example

            Attaches tenuto to pitched head 0:

            >>> music_maker = baca.MusicMaker()
            >>> contribution = music_maker(
            ...     'Voice 1',
            ...     [[0, 2, 10], [18, 16, 15, 20, 19], [9]],
            ...     baca.rests_around([2], [4]),
            ...     baca.tenuto(),
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
                    \context Voice = "Voice 1"
                    {
                        \voiceOne
                        {
                            \tweak text #tuplet-number::calc-fraction-text
                            \times 9/10 {
                                \override TupletBracket.staff-padding = #5                               %! OC1
                                r8
                                c'16
                                -\tenuto                                                                 %! IC
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
                                \revert TupletBracket.staff-padding                                      %! OC2
                            }
                        }
                    }
                >>

        ..  container:: example

            Attaches tenuto to pitched heads in tuplet 1:

            >>> music_maker = baca.MusicMaker()
            >>> contribution = music_maker(
            ...     'Voice 1',
            ...     [[0, 2, 10], [18, 16, 15, 20, 19], [9]],
            ...     baca.map(
            ...         baca.tuplet(1),
            ...         baca.tenuto(selector=baca.pheads()),
            ...         ),
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
                    \context Voice = "Voice 1"
                    {
                        \voiceOne
                        {
                            \tweak text #tuplet-number::calc-fraction-text
                            \times 9/10 {
                                \override TupletBracket.staff-padding = #5                               %! OC1
                                r8
                                c'16
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
                                -\tenuto                                                                 %! IC
                                [
                                e''16
                                -\tenuto                                                                 %! IC
                                ]
                                ef''4
                                -\tenuto                                                                 %! IC
                                ~
                                ef''16
                                r16
                                af''16
                                -\tenuto                                                                 %! IC
                                [
                                g''16
                                -\tenuto                                                                 %! IC
                                ]
                            }
                            \times 4/5 {
                                a'16
                                r4
                                \revert TupletBracket.staff-padding                                      %! OC2
                            }
                        }
                    }
                >>

        """
        return IndicatorCommand(
            indicators=[abjad.Articulation('tenuto')],
            selector=selector,
            )

    @staticmethod
    def text_script_color(
        color: str = 'red',
        *,
        selector: typings.Selector = 'baca.leaves()',
        allow_mmrests: bool = False,
        ) -> OverrideCommand:
        r"""
        Overrides text script color.

        ..  container:: example

            Overrides text script color on all leaves:

            >>> music_maker = baca.MusicMaker()
            >>> contribution = music_maker(
            ...     'Voice 1',
            ...     [[0, 2, 10], [18, 16, 15, 20, 19], [9]],
            ...     baca.markup('più mosso'),
            ...     baca.markup(
            ...         'lo stesso tempo',
            ...         selector=baca.tuplets()[1:2].phead(0),
            ...         ),
            ...     baca.rests_around([2], [4]),
            ...     baca.text_script_color('red'),
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
                    \context Voice = "Voice 1"
                    {
                        \voiceOne
                        {
                            \tweak text #tuplet-number::calc-fraction-text
                            \times 9/10 {
                                \override TextScript.color = #red                                        %! OC1
                                \override TupletBracket.staff-padding = #5                               %! OC1
                                r8
                                c'16
                                ^ \markup { "più mosso" }                                                %! IC
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
                                ^ \markup { "lo stesso tempo" }                                          %! IC
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
                                \revert TextScript.color                                                 %! OC2
                                \revert TupletBracket.staff-padding                                      %! OC2
                            }
                        }
                    }
                >>

        ..  container:: example

            Overrides text script color on leaves in tuplet 1:

            >>> music_maker = baca.MusicMaker()
            >>> contribution = music_maker(
            ...     'Voice 1',
            ...     [[0, 2, 10], [18, 16, 15, 20, 19], [9]],
            ...     baca.markup('più mosso'),
            ...     baca.markup(
            ...         'lo stesso tempo',
            ...         selector=baca.tuplets()[1:2].phead(0),
            ...         ),
            ...     baca.rests_around([2], [4]),
            ...     baca.map(
            ...         baca.tuplet(1),
            ...         baca.text_script_color('red'),
            ...         ),
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
                    \context Voice = "Voice 1"
                    {
                        \voiceOne
                        {
                            \tweak text #tuplet-number::calc-fraction-text
                            \times 9/10 {
                                \override TupletBracket.staff-padding = #5                               %! OC1
                                r8
                                c'16
                                ^ \markup { "più mosso" }                                                %! IC
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
                                \override TextScript.color = #red                                        %! OC1
                                fs''16
                                ^ \markup { "lo stesso tempo" }                                          %! IC
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
                                \revert TextScript.color                                                 %! OC2
                            }
                            \times 4/5 {
                                a'16
                                r4
                                \revert TupletBracket.staff-padding                                      %! OC2
                            }
                        }
                    }
                >>

        ..  container:: example

            Raises exception when called on multimeasure rests:

            >>> maker = baca.SegmentMaker(
            ...     score_template=baca.SingleStaffScoreTemplate(),
            ...     time_signatures=[(4, 8), (3, 8), (4, 8), (3, 8)],
            ...     )

            >>> maker(
            ...     'MusicVoice',
            ...     baca.markup(
            ...         baca.markups.still().boxed(),
            ...         selector=baca.leaf(1),
            ...         ),
            ...     baca.text_script_color('red'),
            ...     )

            >>> lilypond_file = maker.run(environment='docs')
            Traceback (most recent call last):
                ...
            Exception: MultimeasureRest is forbidden.

        """
        if allow_mmrests is True:
            blacklist = None
        else:
            blacklist = (abjad.MultimeasureRest,)
        return OverrideCommand(
            attribute='color',
            blacklist=blacklist,
            value=color,
            grob='text_script',
            selector=selector,
            )

    @staticmethod
    def text_script_down(
        selector: typings.Selector = 'baca.leaves()',
        *,
        allow_mmrests: bool = False,
        ) -> OverrideCommand:
        r"""
        Overrides text script direction.

        ..  container:: example

            Down-overrides text script direction on leaves:

            >>> music_maker = baca.MusicMaker()
            >>> contribution = music_maker(
            ...     'Voice 1',
            ...     [[0, 2, 10], [18, 16, 15, 20, 19], [9]],
            ...     baca.markup('più mosso'),
            ...     baca.markup(
            ...         'lo stesso tempo',
            ...         selector=baca.tuplets()[1:2].phead(0),
            ...         ),
            ...     baca.rests_around([2], [4]),
            ...     baca.text_script_down(),
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
                    \context Voice = "Voice 1"
                    {
                        \voiceOne
                        {
                            \tweak text #tuplet-number::calc-fraction-text
                            \times 9/10 {
                                \override TextScript.direction = #down                                   %! OC1
                                \override TupletBracket.staff-padding = #5                               %! OC1
                                r8
                                c'16
                                ^ \markup { "più mosso" }                                                %! IC
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
                                ^ \markup { "lo stesso tempo" }                                          %! IC
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
                                \revert TextScript.direction                                             %! OC2
                                \revert TupletBracket.staff-padding                                      %! OC2
                            }
                        }
                    }
                >>

        ..  container:: example

            Down-overrides text script direction on leaves in tuplet 1:

            >>> music_maker = baca.MusicMaker()
            >>> contribution = music_maker(
            ...     'Voice 1',
            ...     [[0, 2, 10], [18, 16, 15, 20, 19], [9]],
            ...     baca.markup('più mosso'),
            ...     baca.markup(
            ...         'lo stesso tempo',
            ...         selector=baca.tuplets()[1:2].phead(0),
            ...         ),
            ...     baca.rests_around([2], [4]),
            ...     baca.map(
            ...         baca.tuplet(1),
            ...         baca.text_script_down(),
            ...         ),
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
                    \context Voice = "Voice 1"
                    {
                        \voiceOne
                        {
                            \tweak text #tuplet-number::calc-fraction-text
                            \times 9/10 {
                                \override TupletBracket.staff-padding = #5                               %! OC1
                                r8
                                c'16
                                ^ \markup { "più mosso" }                                                %! IC
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
                                \override TextScript.direction = #down                                   %! OC1
                                fs''16
                                ^ \markup { "lo stesso tempo" }                                          %! IC
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
                                \revert TextScript.direction                                             %! OC2
                            }
                            \times 4/5 {
                                a'16
                                r4
                                \revert TupletBracket.staff-padding                                      %! OC2
                            }
                        }
                    }
                >>

        ..  container:: example

            Raises exception when called on multimeasure rests:

            >>> maker = baca.SegmentMaker(
            ...     score_template=baca.SingleStaffScoreTemplate(),
            ...     time_signatures=[(4, 8), (3, 8), (4, 8), (3, 8)],
            ...     )

            >>> maker(
            ...     'MusicVoice',
            ...     baca.markup(
            ...         baca.markups.still().boxed(),
            ...         selector=baca.leaf(1),
            ...         ),
            ...     baca.text_script_down()
            ...     )

            >>> lilypond_file = maker.run(environment='docs')
            Traceback (most recent call last):
                ...
            Exception: MultimeasureRest is forbidden.

        """
        if allow_mmrests is True:
            blacklist = None
        else:
            blacklist = (abjad.MultimeasureRest,)
        return OverrideCommand(
            attribute='direction',
            blacklist=blacklist,
            value=abjad.Down,
            grob='text_script',
            selector=selector,
            )

    @staticmethod
    def text_script_extra_offset(
        pair: typings.NumberPair,
        *,
        selector: typings.Selector = 'baca.leaves()',
        allow_mmrests: bool = False,
        ) -> OverrideCommand:
        r"""
        Overrides text script extra offset.

        ..  container:: example

            Raises exception when called on multimeasure rests:

            >>> maker = baca.SegmentMaker(
            ...     score_template=baca.SingleStaffScoreTemplate(),
            ...     time_signatures=[(4, 8), (3, 8), (4, 8), (3, 8)],
            ...     )

            >>> maker(
            ...     'MusicVoice',
            ...     baca.markup(
            ...         baca.markups.still().boxed(),
            ...         selector=baca.leaf(1),
            ...         ),
            ...     baca.text_script_extra_offset((0, 2)),
            ...     )

            >>> lilypond_file = maker.run(environment='docs')
            Traceback (most recent call last):
                ...
            Exception: MultimeasureRest is forbidden.

        """
        if allow_mmrests is True:
            blacklist = None
        else:
            blacklist = (abjad.MultimeasureRest,)
        return OverrideCommand(
            attribute='extra_offset',
            blacklist=blacklist,
            value=pair,
            grob='text_script',
            selector=selector,
            )

    @staticmethod
    def text_script_font_size(
        n: typings.Number,
        *,
        selector: typings.Selector = 'baca.leaves()',
        allow_mmrests: bool = False,
        ) -> OverrideCommand:
        """
        Overrides text script font size.
        """
        if allow_mmrests is True:
            blacklist = None
        else:
            blacklist = (abjad.MultimeasureRest,)
        return OverrideCommand(
            attribute='font_size',
            blacklist=blacklist,
            value=n,
            grob='text_script',
            selector=selector,
            )

    @staticmethod
    def text_script_padding(
        n: typings.Number,
        *,
        selector: typings.Selector = 'baca.leaves()',
        allow_mmrests: bool = False,
        ) -> OverrideCommand:
        r"""
        Overrides text script padding.

        ..  container:: example

            Overrides text script padding on leaves:

                >>> music_maker = baca.MusicMaker()
                >>> contribution = music_maker(
                ...     'Voice 1',
                ...     [[0, 2, 10], [18, 16, 15, 20, 19], [9]],
                ...     baca.markup('più mosso'),
                ...     baca.markup(
                ...         'lo stesso tempo',
                ...         selector=baca.tuplets()[1:2].phead(0),
                ...         ),
                ...     baca.rests_around([2], [4]),
                ...     baca.text_script_padding(4),
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
                    \context Voice = "Voice 1"
                    {
                        \voiceOne
                        {
                            \tweak text #tuplet-number::calc-fraction-text
                            \times 9/10 {
                                \override TextScript.padding = #4                                        %! OC1
                                \override TupletBracket.staff-padding = #5                               %! OC1
                                r8
                                c'16
                                ^ \markup { "più mosso" }                                                %! IC
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
                                ^ \markup { "lo stesso tempo" }                                          %! IC
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
                                \revert TextScript.padding                                               %! OC2
                                \revert TupletBracket.staff-padding                                      %! OC2
                            }
                        }
                    }
                >>

        ..  container:: example

            Overrides text script padding on leaves in tuplet 1:

            >>> music_maker = baca.MusicMaker()
            >>> contribution = music_maker(
            ...     'Voice 1',
            ...     [[0, 2, 10], [18, 16, 15, 20, 19], [9]],
            ...     baca.markup('più mosso'),
            ...     baca.markup(
            ...         'lo stesso tempo',
            ...         selector=baca.tuplets()[1:2].phead(0),
            ...         ),
            ...     baca.rests_around([2], [4]),
            ...     baca.map(
            ...         baca.tuplet(1),
            ...         baca.text_script_padding(4),
            ...         ),
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
                    \context Voice = "Voice 1"
                    {
                        \voiceOne
                        {
                            \tweak text #tuplet-number::calc-fraction-text
                            \times 9/10 {
                                \override TupletBracket.staff-padding = #5                               %! OC1
                                r8
                                c'16
                                ^ \markup { "più mosso" }                                                %! IC
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
                                \override TextScript.padding = #4                                        %! OC1
                                fs''16
                                ^ \markup { "lo stesso tempo" }                                          %! IC
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
                                \revert TextScript.padding                                               %! OC2
                            }
                            \times 4/5 {
                                a'16
                                r4
                                \revert TupletBracket.staff-padding                                      %! OC2
                            }
                        }
                    }
                >>

        ..  container:: example

            Raises exception when called on multimeasure rests:

            >>> maker = baca.SegmentMaker(
            ...     score_template=baca.SingleStaffScoreTemplate(),
            ...     time_signatures=[(4, 8), (3, 8), (4, 8), (3, 8)],
            ...     )

            >>> maker(
            ...     'MusicVoice',
            ...     baca.markup(
            ...         baca.markups.still().boxed(),
            ...         selector=baca.leaf(1),
            ...         ),
            ...     baca.text_script_padding(2),
            ...     )

            >>> lilypond_file = maker.run(environment='docs')
            Traceback (most recent call last):
                ...
            Exception: MultimeasureRest is forbidden.

        """
        if allow_mmrests is True:
            blacklist = None
        else:
            blacklist = (abjad.MultimeasureRest,)
        return OverrideCommand(
            attribute='padding',
            blacklist=blacklist,
            value=n,
            grob='text_script',
            selector=selector,
            )

    @staticmethod
    def text_script_parent_center(
        selector: typings.Selector = 'baca.leaves()',
        *,
        allow_mmrests: bool = False,
        ) -> OverrideCommand:
        r"""
        Overrides text script parent alignment X to center.

        ..  container:: example

            Raises exception when called on multimeasure rests:

            >>> maker = baca.SegmentMaker(
            ...     score_template=baca.SingleStaffScoreTemplate(),
            ...     time_signatures=[(4, 8), (3, 8), (4, 8), (3, 8)],
            ...     )

            >>> maker(
            ...     'MusicVoice',
            ...     baca.markup(
            ...         baca.markups.still().boxed(),
            ...         selector=baca.leaf(1),
            ...         ),
            ...     baca.text_script_parent_center()
            ...     )

            >>> lilypond_file = maker.run(environment='docs')
            Traceback (most recent call last):
                ...
            Exception: MultimeasureRest is forbidden.

        """
        if allow_mmrests is True:
            blacklist = None
        else:
            blacklist = (abjad.MultimeasureRest,)
        return OverrideCommand(
            attribute='parent_alignment_X',
            blacklist=blacklist,
            value=0,
            grob='text_script',
            selector=selector,
            )

    @staticmethod
    def text_script_staff_padding(
        n: typings.Number,
        *,
        selector: typings.Selector = 'baca.leaves()',
        allow_mmrests: bool = False,
        ) -> OverrideCommand:
        r"""
        Overrides text script staff padding.

        ..  container:: example

            Overrides text script staff padding on leaves:

            >>> music_maker = baca.MusicMaker()
            >>> contribution = music_maker(
            ...     'Voice 1',
            ...     [[0, 2, 10], [18, 16, 15, 20, 19], [9]],
            ...     baca.markup('più mosso'),
            ...     baca.markup(
            ...         'lo stesso tempo',
            ...         selector=baca.tuplets()[1:2].phead(0),
            ...         ),
            ...     baca.rests_around([2], [4]),
            ...     baca.text_script_staff_padding(n=4),
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
                    \context Voice = "Voice 1"
                    {
                        \voiceOne
                        {
                            \tweak text #tuplet-number::calc-fraction-text
                            \times 9/10 {
                                \override TextScript.staff-padding = #4                                  %! OC1
                                \override TupletBracket.staff-padding = #5                               %! OC1
                                r8
                                c'16
                                ^ \markup { "più mosso" }                                                %! IC
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
                                ^ \markup { "lo stesso tempo" }                                          %! IC
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
                                \revert TextScript.staff-padding                                         %! OC2
                                \revert TupletBracket.staff-padding                                      %! OC2
                            }
                        }
                    }
                >>

        ..  container:: example

            Overrides text script staff padding on leaves in tuplet 1:

            >>> music_maker = baca.MusicMaker()
            >>> contribution = music_maker(
            ...     'Voice 1',
            ...     [[0, 2, 10], [18, 16, 15, 20, 19], [9]],
            ...     baca.markup('più mosso'),
            ...     baca.markup(
            ...         'lo stesso tempo',
            ...         selector=baca.tuplets()[1:2].phead(0),
            ...         ),
            ...     baca.rests_around([2], [4]),
            ...     baca.map(
            ...         baca.tuplet(1),
            ...         baca.text_script_staff_padding(4),
            ...         ),
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
                    \context Voice = "Voice 1"
                    {
                        \voiceOne
                        {
                            \tweak text #tuplet-number::calc-fraction-text
                            \times 9/10 {
                                \override TupletBracket.staff-padding = #5                               %! OC1
                                r8
                                c'16
                                ^ \markup { "più mosso" }                                                %! IC
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
                                \override TextScript.staff-padding = #4                                  %! OC1
                                fs''16
                                ^ \markup { "lo stesso tempo" }                                          %! IC
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
                                \revert TextScript.staff-padding                                         %! OC2
                            }
                            \times 4/5 {
                                a'16
                                r4
                                \revert TupletBracket.staff-padding                                      %! OC2
                            }
                        }
                    }
                >>

        ..  container:: example

            Raises exception when called on multimeasure rests:

            >>> maker = baca.SegmentMaker(
            ...     score_template=baca.SingleStaffScoreTemplate(),
            ...     time_signatures=[(4, 8), (3, 8), (4, 8), (3, 8)],
            ...     )

            >>> maker(
            ...     'MusicVoice',
            ...     baca.markup(
            ...         baca.markups.still().boxed(),
            ...         selector=baca.leaf(1),
            ...         ),
            ...     baca.text_script_staff_padding(2)
            ...     )

            >>> lilypond_file = maker.run(environment='docs')
            Traceback (most recent call last):
                ...
            Exception: MultimeasureRest is forbidden.

        """
        if allow_mmrests is True:
            blacklist = None
        else:
            blacklist = (abjad.MultimeasureRest,)
        return OverrideCommand(
            attribute='staff_padding',
            blacklist=blacklist,
            value=n,
            grob='text_script',
            selector=selector,
            )

    @staticmethod
    def text_script_up(
        selector: typings.Selector = 'baca.leaves()',
        *,
        allow_mmrests: bool = False,
        ) -> OverrideCommand:
        r"""
        Overrides text script direction.

        ..  container:: example

            Up-overrides text script direction on leaves:

            >>> music_maker = baca.MusicMaker()
            >>> contribution = music_maker(
            ...     'Voice 1',
            ...     [[0, 2, 10], [18, 16, 15, 20, 19], [9]],
            ...     baca.markup('più mosso'),
            ...     baca.markup(
            ...         'lo stesso tempo',
            ...         selector=baca.tuplets()[1:2].phead(0),
            ...         ),
            ...     baca.rests_around([2], [4]),
            ...     baca.text_script_up(),
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
                    \context Voice = "Voice 1"
                    {
                        \voiceOne
                        {
                            \tweak text #tuplet-number::calc-fraction-text
                            \times 9/10 {
                                \override TextScript.direction = #up                                     %! OC1
                                \override TupletBracket.staff-padding = #5                               %! OC1
                                r8
                                c'16
                                ^ \markup { "più mosso" }                                                %! IC
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
                                ^ \markup { "lo stesso tempo" }                                          %! IC
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
                                \revert TextScript.direction                                             %! OC2
                                \revert TupletBracket.staff-padding                                      %! OC2
                            }
                        }
                    }
                >>

        ..  container:: example

            Up-overrides text script direction on leaves in tuplet 1:

            >>> music_maker = baca.MusicMaker()
            >>> contribution = music_maker(
            ...     'Voice 1',
            ...     [[0, 2, 10], [18, 16, 15, 20, 19], [9]],
            ...     baca.markup('più mosso'),
            ...     baca.markup(
            ...         'lo stesso tempo',
            ...         selector=baca.tuplets()[1:2].phead(0),
            ...         ),
            ...     baca.rests_around([2], [4]),
            ...     baca.map(
            ...         baca.tuplet(1),
            ...         baca.text_script_up(),
            ...         ),
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
                    \context Voice = "Voice 1"
                    {
                        \voiceOne
                        {
                            \tweak text #tuplet-number::calc-fraction-text
                            \times 9/10 {
                                \override TupletBracket.staff-padding = #5                               %! OC1
                                r8
                                c'16
                                ^ \markup { "più mosso" }                                                %! IC
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
                                \override TextScript.direction = #up                                     %! OC1
                                fs''16
                                ^ \markup { "lo stesso tempo" }                                          %! IC
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
                                \revert TextScript.direction                                             %! OC2
                            }
                            \times 4/5 {
                                a'16
                                r4
                                \revert TupletBracket.staff-padding                                      %! OC2
                            }
                        }
                    }
                >>

        ..  container:: example

            Raises exception when called on multimeasure rests:

            >>> maker = baca.SegmentMaker(
            ...     score_template=baca.SingleStaffScoreTemplate(),
            ...     time_signatures=[(4, 8), (3, 8), (4, 8), (3, 8)],
            ...     )

            >>> maker(
            ...     'MusicVoice',
            ...     baca.markup(
            ...         baca.markups.still().boxed(),
            ...         selector=baca.leaf(1),
            ...         ),
            ...     baca.text_script_up()
            ...     )

            >>> lilypond_file = maker.run(environment='docs')
            Traceback (most recent call last):
                ...
            Exception: MultimeasureRest is forbidden.

        """
        if allow_mmrests is True:
            blacklist = None
        else:
            blacklist = (abjad.MultimeasureRest,)
        return OverrideCommand(
            attribute='direction',
            blacklist=blacklist,
            value=abjad.Up,
            grob='text_script',
            selector=selector,
            )

    @staticmethod
    def text_script_x_offset(
        n: typings.Number,
        *,
        selector: typings.Selector = 'baca.leaves()',
        allow_mmrests: bool = False,
        ) -> OverrideCommand:
        """
        Overrides text script X-offset.
        """
        if allow_mmrests is True:
            blacklist = None
        else:
            blacklist = (abjad.MultimeasureRest,)
        return OverrideCommand(
            attribute='X_offset',
            blacklist=blacklist,
            value=n,
            grob='text_script',
            selector=selector,
            )

    @staticmethod
    def text_script_y_offset(
        n: typings.Number,
        *,
        selector: typings.Selector = 'baca.leaves()',
        allow_mmrests: bool = False,
        ) -> OverrideCommand:
        """
        Overrides text script Y-offset.
        """
        if allow_mmrests is True:
            blacklist = None
        else:
            blacklist = (abjad.MultimeasureRest,)
        return OverrideCommand(
            attribute='Y_offset',
            blacklist=blacklist,
            value=n,
            grob='text_script',
            selector=selector,
            )

    @staticmethod
    def text_spanner(
        text: typing.Union[str, abjad.Markup],
        *tweaks: abjad.LilyPondTweakManager,
        leak: bool = None,
        lilypond_id: int = None,
        no_upright: bool = None,
        right_padding: typing.Optional[typings.Number] = 1.25,
        selector: typings.Selector = 'baca.tleaves()',
        ) -> Suite:
        r"""
        Makes text spanner command.

        ..  container:: example

            >>> maker = baca.SegmentMaker(
            ...     score_template=baca.SingleStaffScoreTemplate(),
            ...     spacing=baca.minimum_duration((1, 12)),
            ...     time_signatures=[(4, 8), (3, 8), (4, 8), (3, 8)],
            ...     )

            >>> maker(
            ...     'MusicVoice',
            ...     baca.text_spanner(
            ...         '1/2 clt',
            ...         abjad.tweak(4).staff_padding,
            ...         selector=baca.leaves()[:7 + 1],
            ...         ),
            ...     baca.text_spanner(
            ...         'damp',
            ...         abjad.tweak(6.5).staff_padding,
            ...         lilypond_id=1,
            ...         selector=baca.leaves()[:11 + 1],
            ...         ),
            ...     baca.make_even_divisions(),
            ...     baca.pitches('E4 D5 F4 E5 G4 F5'),
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
                            \baca_new_spacing_section #1 #12                                             %! HSS1:SPACING
                            \time 4/8                                                                    %! SM8:EXPLICIT_TIME_SIGNATURE:SM1
                            \once \override Score.TimeSignature.color = #(x11-color 'blue)               %! SM6:EXPLICIT_TIME_SIGNATURE_COLOR:SM1
                            s1 * 1/2
                <BLANKLINE>
                            % [GlobalSkips measure 2]                                                    %! SM4
                            \baca_new_spacing_section #1 #12                                             %! HSS1:SPACING
                            \time 3/8                                                                    %! SM8:EXPLICIT_TIME_SIGNATURE:SM1
                            \once \override Score.TimeSignature.color = #(x11-color 'blue)               %! SM6:EXPLICIT_TIME_SIGNATURE_COLOR:SM1
                            s1 * 3/8
                <BLANKLINE>
                            % [GlobalSkips measure 3]                                                    %! SM4
                            \baca_new_spacing_section #1 #12                                             %! HSS1:SPACING
                            \time 4/8                                                                    %! SM8:EXPLICIT_TIME_SIGNATURE:SM1
                            \once \override Score.TimeSignature.color = #(x11-color 'blue)               %! SM6:EXPLICIT_TIME_SIGNATURE_COLOR:SM1
                            s1 * 1/2
                <BLANKLINE>
                            % [GlobalSkips measure 4]                                                    %! SM4
                            \baca_new_spacing_section #1 #12                                             %! HSS1:SPACING
                            \time 3/8                                                                    %! SM8:EXPLICIT_TIME_SIGNATURE:SM1
                            \once \override Score.TimeSignature.color = #(x11-color 'blue)               %! SM6:EXPLICIT_TIME_SIGNATURE_COLOR:SM1
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
                <BLANKLINE>
                                % [MusicVoice measure 1]                                                 %! SM4
                                e'8
                                - \abjad_dashed_line_with_hook                                           %! IC
                                - \tweak bound-details.left.text \markup {                               %! IC
                                    \concat                                                              %! IC
                                        {                                                                %! IC
                                            \upright                                                     %! IC
                                                "1/2 clt"                                                %! IC
                                            \hspace                                                      %! IC
                                                #0.5                                                     %! IC
                                        }                                                                %! IC
                                    }                                                                    %! IC
                                - \tweak bound-details.right.padding 1.25                                %! IC
                                - \tweak staff-padding #4                                                %! IC
                                \startTextSpan                                                           %! IC
                                - \abjad_dashed_line_with_hook                                           %! IC
                                - \tweak bound-details.left.text \markup {                               %! IC
                                    \concat                                                              %! IC
                                        {                                                                %! IC
                                            \upright                                                     %! IC
                                                damp                                                     %! IC
                                            \hspace                                                      %! IC
                                                #0.5                                                     %! IC
                                        }                                                                %! IC
                                    }                                                                    %! IC
                                - \tweak bound-details.right.padding 1.25                                %! IC
                                - \tweak staff-padding #6.5                                              %! IC
                                \startTextSpanOne                                                        %! IC
                                [
                <BLANKLINE>
                                d''8
                <BLANKLINE>
                                f'8
                <BLANKLINE>
                                e''8
                                ]
                <BLANKLINE>
                                % [MusicVoice measure 2]                                                 %! SM4
                                g'8
                                [
                <BLANKLINE>
                                f''8
                <BLANKLINE>
                                e'8
                                ]
                <BLANKLINE>
                                % [MusicVoice measure 3]                                                 %! SM4
                                d''8
                                \stopTextSpan                                                            %! IC
                                [
                <BLANKLINE>
                                f'8
                <BLANKLINE>
                                e''8
                <BLANKLINE>
                                g'8
                                ]
                <BLANKLINE>
                                % [MusicVoice measure 4]                                                 %! SM4
                                f''8
                                \stopTextSpanOne                                                         %! IC
                                [
                <BLANKLINE>
                                e'8
                <BLANKLINE>
                                d''8
                                ]
                <BLANKLINE>
                            }
                        }
                    >>
                >>

        """
        if isinstance(text, abjad.Markup):
            markup = text
        else:
            assert isinstance(text, str), repr(text)
            markup = Markup(text)
        if no_upright is not True:
            string = format(markup)
            if 'upright' in string:
                raise Exception(f'markup already upright:\n  {markup}')
            markup = markup.upright()
        if isinstance(selector, str):
            selector = eval(selector)
        assert isinstance(selector, abjad.Expression)
        if lilypond_id is None:
            command = r'\startTextSpan'
        elif lilypond_id == 1:
            command = r'\startTextSpanOne'
        elif lilypond_id == 2:
            command = r'\startTextSpanTwo'
        elif lilypond_id == 3:
            command = r'\startTextSpanThree'
        else:
            raise ValueError(lilypond_id)
        start_text_span = abjad.StartTextSpan(
            command=command,
            left_text=markup,
            right_padding=right_padding,
            style='dashed_line_with_hook',
            )
        library.apply_tweaks(start_text_span, tweaks)
        selector_ = selector.leaf(0)
        start_command = IndicatorCommand(
            indicators=[start_text_span],
            selector=selector_,
            )
        if lilypond_id is None:
            command = r'\stopTextSpan'
        elif lilypond_id == 1:
            command = r'\stopTextSpanOne'
        elif lilypond_id == 2:
            command = r'\stopTextSpanTwo'
        elif lilypond_id == 3:
            command = r'\stopTextSpanThree'
        else:
            raise ValueError(lilypond_id)
        stop_text_span = abjad.StopTextSpan(
            command=command,
            leak=leak,
            )
        selector = selector.leaf(-1)
        stop_command = IndicatorCommand(
            indicators=[stop_text_span],
            selector=selector,
            )
        return library.suite(
            start_command,
            stop_command,
            )

    @staticmethod
    def text_spanner_left_padding(
        n: typings.Number,
        *,
        selector: typings.Selector = 'baca.leaves()',
        ) -> OverrideCommand:
        """
        Overrides text spanner left padding.
        """
        return OverrideCommand(
            attribute='bound_details__left__padding',
            value=n,
            grob='text_spanner',
            selector=selector,
            )

    @staticmethod
    def text_spanner_right_padding(
        n: typings.Number,
        *,
        selector: typings.Selector = 'baca.leaves()',
        ) -> OverrideCommand:
        """
        Overrides text spanner right padding.
        """
        return OverrideCommand(
            attribute='bound_details__right__padding',
            value=n,
            grob='text_spanner',
            selector=selector,
            )

    @staticmethod
    def text_spanner_staff_padding(
        n: typings.Number,
        *,
        selector: typings.Selector = 'baca.leaves()',
        ) -> OverrideCommand:
        r"""
        Overrides text spanner staff padding.

        ..  container:: example

            Overrides text spanner staff padding on all trimmed leaves:

            >>> music_maker = baca.MusicMaker()
            >>> contribution = music_maker(
            ...     'Voice 1',
            ...     [[0, 2, 10], [18, 16, 15, 20, 19], [9]],
            ...     baca.rests_around([2], [4]),
            ...     baca.text_spanner_staff_padding(6),
            ...     baca.text_script_staff_padding(6),
            ...     baca.new_transition(
            ...         baca.markups.pont(),
            ...         baca.markups.ord(),
            ...         ),
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
                    \context Voice = "Voice 1"
                    {
                        \voiceOne
                        {
                            \tweak text #tuplet-number::calc-fraction-text
                            \times 9/10 {
                                \override TextSpanner.staff-padding = #6                                 %! OC1
                                \override TextScript.staff-padding = #6                                  %! OC1
                                \override TupletBracket.staff-padding = #5                               %! OC1
                                r8
                                c'16
                                - \abjad_dashed_line_with_arrow                                          %! PIC
                                - \tweak bound-details.left.text \markup {                               %! PIC
                                    \concat                                                              %! PIC
                                        {                                                                %! PIC
                                            \upright                                                     %! PIC
                                                pont.                                                    %! PIC
                                            \hspace                                                      %! PIC
                                                #0.5                                                     %! PIC
                                        }                                                                %! PIC
                                    }                                                                    %! PIC
                                - \tweak bound-details.right.text \markup {                              %! PIC
                                    \upright                                                             %! PIC
                                        ord.                                                             %! PIC
                                    }                                                                    %! PIC
                                - \tweak bound-details.right.padding #0.5                                %! PIC
                                - \tweak bound-details.right.stencil-align-dir-y #center                 %! PIC
                                \startTextSpan                                                           %! PIC
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
                                \stopTextSpan                                                            %! PIC
                                r4
                                \revert TextSpanner.staff-padding                                        %! OC2
                                \revert TextScript.staff-padding                                         %! OC2
                                \revert TupletBracket.staff-padding                                      %! OC2
                            }
                        }
                    }
                >>

        ..  container:: example

            Overrides text spanner staff padding on trimmed leaves in tuplet 1:

            >>> music_maker = baca.MusicMaker()
            >>> contribution = music_maker(
            ...     'Voice 1',
            ...     [[0, 2, 10], [18, 16, 15, 20, 19], [9]],
            ...     baca.rests_around([2], [4]),
            ...     baca.map(
            ...         baca.tuplet(1),
            ...         baca.text_spanner_staff_padding(6),
            ...         ),
            ...     baca.text_script_staff_padding(6),
            ...     baca.new_transition(
            ...         baca.markups.pont(),
            ...         baca.markups.ord(),
            ...         selector=baca.tuplets()[1:2].tleaves(),
            ...         ),
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
                    \context Voice = "Voice 1"
                    {
                        \voiceOne
                        {
                            \tweak text #tuplet-number::calc-fraction-text
                            \times 9/10 {
                                \override TextScript.staff-padding = #6                                  %! OC1
                                \override TupletBracket.staff-padding = #5                               %! OC1
                                r8
                                c'16
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
                                \override TextSpanner.staff-padding = #6                                 %! OC1
                                fs''16
                                - \abjad_dashed_line_with_arrow                                          %! PIC
                                - \tweak bound-details.left.text \markup {                               %! PIC
                                    \concat                                                              %! PIC
                                        {                                                                %! PIC
                                            \upright                                                     %! PIC
                                                pont.                                                    %! PIC
                                            \hspace                                                      %! PIC
                                                #0.5                                                     %! PIC
                                        }                                                                %! PIC
                                    }                                                                    %! PIC
                                - \tweak bound-details.right.text \markup {                              %! PIC
                                    \upright                                                             %! PIC
                                        ord.                                                             %! PIC
                                    }                                                                    %! PIC
                                - \tweak bound-details.right.padding #0.5                                %! PIC
                                - \tweak bound-details.right.stencil-align-dir-y #center                 %! PIC
                                \startTextSpan                                                           %! PIC
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
                                \stopTextSpan                                                            %! PIC
                                ]
                                \revert TextSpanner.staff-padding                                        %! OC2
                            }
                            \times 4/5 {
                                a'16
                                r4
                                \revert TextScript.staff-padding                                         %! OC2
                                \revert TupletBracket.staff-padding                                      %! OC2
                            }
                        }
                    }
                >>

        """
        return OverrideCommand(
            attribute='staff_padding',
            value=n,
            grob='text_spanner',
            selector=selector,
            )

    @staticmethod
    def text_spanner_stencil_false(
        *,
        selector: typings.Selector = 'baca.leaves()',
        ) -> OverrideCommand:
        """
        Overrides text spanner stencil.
        """
        return OverrideCommand(
            attribute='stencil',
            value=False,
            grob='text_spanner',
            selector=selector,
            )

    @staticmethod
    def text_spanner_transparent(
        *,
        selector: typings.Selector = 'baca.leaves()',
        ) -> OverrideCommand:
        """
        Overrides text spanner transparent.
        """
        return OverrideCommand(
            attribute='transparent',
            value=True,
            grob='text_spanner',
            selector=selector,
            )

    @staticmethod
    def text_spanner_y_offset(
        n: typings.Number,
        *,
        selector: typings.Selector = 'baca.leaves()',
        ) -> OverrideCommand:
        """
        Overrides text spanner Y-offset.
        """
        return OverrideCommand(
            attribute='Y_offset',
            value=n,
            grob='text_spanner',
            selector=selector,
            )

    @staticmethod
    def tie(
        *,
        repeat: typing.Union[
            bool,
            typings.IntegerPair,
            abjad.DurationInequality,
            ] = None,
        selector: typings.Selector = 'baca.qrun(0)',
        ) -> SpannerCommand:
        r"""
        Attaches tie.

        ..  container:: example

            Attaches ties to equipitch runs:

            >>> music_maker = baca.MusicMaker()
            >>> contribution = music_maker(
            ...     'Voice 1',
            ...     [[0, 0, 10], [10, 16, 16, 18, 20], [9]],
            ...     baca.map(
            ...         baca.qruns(),
            ...         baca.tie(),
            ...         ),
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
                    \context Voice = "Voice 1"
                    {
                        \voiceOne
                        {
                            \tweak text #tuplet-number::calc-fraction-text
                            \times 9/10 {
                                \override TupletBracket.staff-padding = #5                               %! OC1
                                r8
                                c'16
                                ~                                                                        %! SC
                                [
                                c'16
                                ]
                                bf'4
                                ~                                                                        %! SC
                                bf'16
                                r16
                            }
                            \tweak text #tuplet-number::calc-fraction-text
                            \times 9/10 {
                                bf'16
                                [
                                e''16
                                ~                                                                        %! SC
                                ]
                                e''4
                                ~                                                                        %! SC
                                e''16
                                r16
                                fs''16
                                [
                                af''16
                                ]
                            }
                            \times 4/5 {
                                a'16
                                r4
                                \revert TupletBracket.staff-padding                                      %! OC2
                            }
                        }
                    }
                >>

        ..  container:: example

            Attaches repeat-threshold ties to equipitch runs:

            >>> music_maker = baca.MusicMaker()
            >>> contribution = music_maker(
            ...     'Voice 1',
            ...     [[0, 0, 10], [10, 16, 16, 18, 20], [9]],
            ...     baca.map(
            ...         baca.qruns(),
            ...         baca.tie(repeat=(1, 8)),
            ...         ),
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
                    \context Voice = "Voice 1"
                    {
                        \voiceOne
                        {
                            \tweak text #tuplet-number::calc-fraction-text
                            \times 9/10 {
                                \override TupletBracket.staff-padding = #5                               %! OC1
                                r8
                                c'16
                                [
                                c'16
                                \repeatTie                                                               %! SC
                                ]
                                bf'4
                                bf'16
                                \repeatTie                                                               %! SC
                                r16
                            }
                            \tweak text #tuplet-number::calc-fraction-text
                            \times 9/10 {
                                bf'16
                                [
                                e''16
                                ]
                                e''4
                                \repeatTie                                                               %! SC
                                e''16
                                \repeatTie                                                               %! SC
                                r16
                                fs''16
                                [
                                af''16
                                ]
                            }
                            \times 4/5 {
                                a'16
                                r4
                                \revert TupletBracket.staff-padding                                      %! OC2
                            }
                        }
                    }
                >>

        """
        tie = abjad.Tie(
            repeat=repeat,
            )
        return SpannerCommand(
            selector=selector,
            spanner=tie,
            )

    @staticmethod
    def tie_down(
        *,
        selector: typings.Selector = 'baca.tleaves()',
        ) -> OverrideCommand:
        r"""
        Overrides tie direction.

        ..  container:: example

            Overrides tie direction on pitched leaves:

            >>> music_maker = baca.MusicMaker()
            >>> contribution = music_maker(
            ...     'Voice 1',
            ...     [[11, 11, 12], [11, 11, 11], [11]],
            ...     baca.rests_around([2], [4]),
            ...     baca.stem_up(),
            ...     baca.map(
            ...         baca.qruns(),
            ...         baca.tie(),
            ...         ),
            ...     baca.tie_down(),
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
                    \context Voice = "Voice 1"
                    {
                        \voiceOne
                        {
                            \tweak text #tuplet-number::calc-fraction-text
                            \times 9/10 {
                                \override TupletBracket.staff-padding = #5                               %! OC1
                                r8
                                \override Stem.direction = #up                                           %! OC1
                                \override Tie.direction = #down                                          %! OC1
                                b'16
                                ~                                                                        %! SC
                                [
                                b'16
                                ]
                                c''4
                                ~                                                                        %! SC
                                c''16
                                r16
                            }
                            \tweak text #tuplet-number::calc-fraction-text
                            \times 7/8 {
                                b'16
                                ~                                                                        %! SC
                                [
                                b'16
                                ~                                                                        %! SC
                                ]
                                b'4
                                ~                                                                        %! SC
                                b'16
                                r16
                            }
                            \times 4/5 {
                                b'16
                                \revert Stem.direction                                                   %! OC2
                                \revert Tie.direction                                                    %! OC2
                                r4
                                \revert TupletBracket.staff-padding                                      %! OC2
                            }
                        }
                    }
                >>

        ..  container:: example

            Overrides tie direction on pitched leaves in tuplet 1:

            >>> music_maker = baca.MusicMaker()
            >>> contribution = music_maker(
            ...     'Voice 1',
            ...     [[11, 11, 12], [11, 11, 11], [11]],
            ...     baca.rests_around([2], [4]),
            ...     baca.stem_up(),
            ...     baca.map(
            ...         baca.qruns(),
            ...         baca.tie(),
            ...         ),
            ...     baca.map(
            ...         baca.tuplet(1),
            ...         baca.tie_down(),
            ...         ),
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
                    \context Voice = "Voice 1"
                    {
                        \voiceOne
                        {
                            \tweak text #tuplet-number::calc-fraction-text
                            \times 9/10 {
                                \override TupletBracket.staff-padding = #5                               %! OC1
                                r8
                                \override Stem.direction = #up                                           %! OC1
                                b'16
                                ~                                                                        %! SC
                                [
                                b'16
                                ]
                                c''4
                                ~                                                                        %! SC
                                c''16
                                r16
                            }
                            \tweak text #tuplet-number::calc-fraction-text
                            \times 7/8 {
                                \override Tie.direction = #down                                          %! OC1
                                b'16
                                ~                                                                        %! SC
                                [
                                b'16
                                ~                                                                        %! SC
                                ]
                                b'4
                                ~                                                                        %! SC
                                b'16
                                \revert Tie.direction                                                    %! OC2
                                r16
                            }
                            \times 4/5 {
                                b'16
                                \revert Stem.direction                                                   %! OC2
                                r4
                                \revert TupletBracket.staff-padding                                      %! OC2
                            }
                        }
                    }
                >>

        """
        return OverrideCommand(
            attribute='direction',
            value=abjad.Down,
            grob='tie',
            selector=selector,
            )

    @staticmethod
    def tie_from(
        *,
        selector: typings.Selector = 'baca.pleaf(-1)',
        ) -> TieCorrectionCommand:
        r"""
        Ties from leaf.

        ..  container:: example

            >>> maker = baca.SegmentMaker(
            ...     ignore_unpitched_notes=True,
            ...     score_template=baca.SingleStaffScoreTemplate(),
            ...     time_signatures=[(4, 8), (3, 8), (4, 8), (3, 8)],
            ...     )

            >>> maker(
            ...     'MusicVoice',
            ...     baca.make_notes(),
            ...     baca.tie_from(selector=baca.leaf(1)),
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
                            \time 4/8                                                                    %! SM8:EXPLICIT_TIME_SIGNATURE:SM1
                            \once \override Score.TimeSignature.color = #(x11-color 'blue)               %! SM6:EXPLICIT_TIME_SIGNATURE_COLOR:SM1
                            s1 * 1/2
                <BLANKLINE>
                            % [GlobalSkips measure 2]                                                    %! SM4
                            \time 3/8                                                                    %! SM8:EXPLICIT_TIME_SIGNATURE:SM1
                            \once \override Score.TimeSignature.color = #(x11-color 'blue)               %! SM6:EXPLICIT_TIME_SIGNATURE_COLOR:SM1
                            s1 * 3/8
                <BLANKLINE>
                            % [GlobalSkips measure 3]                                                    %! SM4
                            \time 4/8                                                                    %! SM8:EXPLICIT_TIME_SIGNATURE:SM1
                            \once \override Score.TimeSignature.color = #(x11-color 'blue)               %! SM6:EXPLICIT_TIME_SIGNATURE_COLOR:SM1
                            s1 * 1/2
                <BLANKLINE>
                            % [GlobalSkips measure 4]                                                    %! SM4
                            \time 3/8                                                                    %! SM8:EXPLICIT_TIME_SIGNATURE:SM1
                            \once \override Score.TimeSignature.color = #(x11-color 'blue)               %! SM6:EXPLICIT_TIME_SIGNATURE_COLOR:SM1
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
                <BLANKLINE>
                                % [MusicVoice measure 1]                                                 %! SM4
                                c'2
                <BLANKLINE>
                                % [MusicVoice measure 2]                                                 %! SM4
                                c'4.
                                ~                                                                        %! TCC
                <BLANKLINE>
                                % [MusicVoice measure 3]                                                 %! SM4
                                c'2
                <BLANKLINE>
                                % [MusicVoice measure 4]                                                 %! SM4
                                c'4.
                <BLANKLINE>
                            }
                        }
                    >>
                >>

        """
        return TieCorrectionCommand(
            repeat=False,
            selector=selector,
            )

    @staticmethod
    def tie_repeat_pitches() -> Map:
        """
        Ties repeat pitches.
        """
        return library.map(
            baca.select().ltqruns().nontrivial(),
            LibraryTZ.tie(),
            )

    @staticmethod
    def tie_to(
        *,
        selector: typings.Selector = 'baca.pleaf(0)',
        ) -> TieCorrectionCommand:
        r"""
        Ties to leaf.

        ..  container:: example

            >>> maker = baca.SegmentMaker(
            ...     ignore_unpitched_notes=True,
            ...     score_template=baca.SingleStaffScoreTemplate(),
            ...     time_signatures=[(4, 8), (3, 8), (4, 8), (3, 8)],
            ...     )

            >>> maker(
            ...     'MusicVoice',
            ...     baca.make_notes(),
            ...     baca.tie_to(selector=baca.leaf(1)),
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
                            \time 4/8                                                                    %! SM8:EXPLICIT_TIME_SIGNATURE:SM1
                            \once \override Score.TimeSignature.color = #(x11-color 'blue)               %! SM6:EXPLICIT_TIME_SIGNATURE_COLOR:SM1
                            s1 * 1/2
                <BLANKLINE>
                            % [GlobalSkips measure 2]                                                    %! SM4
                            \time 3/8                                                                    %! SM8:EXPLICIT_TIME_SIGNATURE:SM1
                            \once \override Score.TimeSignature.color = #(x11-color 'blue)               %! SM6:EXPLICIT_TIME_SIGNATURE_COLOR:SM1
                            s1 * 3/8
                <BLANKLINE>
                            % [GlobalSkips measure 3]                                                    %! SM4
                            \time 4/8                                                                    %! SM8:EXPLICIT_TIME_SIGNATURE:SM1
                            \once \override Score.TimeSignature.color = #(x11-color 'blue)               %! SM6:EXPLICIT_TIME_SIGNATURE_COLOR:SM1
                            s1 * 1/2
                <BLANKLINE>
                            % [GlobalSkips measure 4]                                                    %! SM4
                            \time 3/8                                                                    %! SM8:EXPLICIT_TIME_SIGNATURE:SM1
                            \once \override Score.TimeSignature.color = #(x11-color 'blue)               %! SM6:EXPLICIT_TIME_SIGNATURE_COLOR:SM1
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
                <BLANKLINE>
                                % [MusicVoice measure 1]                                                 %! SM4
                                c'2
                                ~                                                                        %! TCC
                <BLANKLINE>
                                % [MusicVoice measure 2]                                                 %! SM4
                                c'4.
                <BLANKLINE>
                                % [MusicVoice measure 3]                                                 %! SM4
                                c'2
                <BLANKLINE>
                                % [MusicVoice measure 4]                                                 %! SM4
                                c'4.
                <BLANKLINE>
                            }
                        }
                    >>
                >>

        """
        return TieCorrectionCommand(
            direction=abjad.Left,
            repeat=False,
            selector=selector,
            )

    @staticmethod
    def tie_up(
        *,
        selector: typings.Selector = 'baca.tleaves()',
        ) -> OverrideCommand:
        r"""
        Overrides tie direction.

        ..  container:: example

            Overrides tie direction on pitched leaves:

            >>> music_maker = baca.MusicMaker()
            >>> contribution = music_maker(
            ...     'Voice 1',
            ...     [[11, 11, 12], [11, 11, 11], [11]],
            ...     baca.rests_around([2], [4]),
            ...     baca.stem_down(),
            ...     baca.map(
            ...         baca.qruns(),
            ...         baca.tie(),
            ...         ),
            ...     baca.tie_up(),
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
                    \context Voice = "Voice 1"
                    {
                        \voiceOne
                        {
                            \tweak text #tuplet-number::calc-fraction-text
                            \times 9/10 {
                                \override TupletBracket.staff-padding = #5                               %! OC1
                                r8
                                \override Stem.direction = #down                                         %! OC1
                                \override Tie.direction = #up                                            %! OC1
                                b'16
                                ~                                                                        %! SC
                                [
                                b'16
                                ]
                                c''4
                                ~                                                                        %! SC
                                c''16
                                r16
                            }
                            \tweak text #tuplet-number::calc-fraction-text
                            \times 7/8 {
                                b'16
                                ~                                                                        %! SC
                                [
                                b'16
                                ~                                                                        %! SC
                                ]
                                b'4
                                ~                                                                        %! SC
                                b'16
                                r16
                            }
                            \times 4/5 {
                                b'16
                                \revert Stem.direction                                                   %! OC2
                                \revert Tie.direction                                                    %! OC2
                                r4
                                \revert TupletBracket.staff-padding                                      %! OC2
                            }
                        }
                    }
                >>

        ..  container:: example

            Overrides tie direction on pitched leaves in tuplet 1:

            >>> music_maker = baca.MusicMaker()
            >>> contribution = music_maker(
            ...     'Voice 1',
            ...     [[11, 11, 12], [11, 11, 11], [11]],
            ...     baca.rests_around([2], [4]),
            ...     baca.stem_down(),
            ...     baca.map(
            ...         baca.qruns(),
            ...         baca.tie(),
            ...         ),
            ...     baca.map(
            ...         baca.tuplet(1),
            ...         baca.tie_up(),
            ...         ),
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
                    \context Voice = "Voice 1"
                    {
                        \voiceOne
                        {
                            \tweak text #tuplet-number::calc-fraction-text
                            \times 9/10 {
                                \override TupletBracket.staff-padding = #5                               %! OC1
                                r8
                                \override Stem.direction = #down                                         %! OC1
                                b'16
                                ~                                                                        %! SC
                                [
                                b'16
                                ]
                                c''4
                                ~                                                                        %! SC
                                c''16
                                r16
                            }
                            \tweak text #tuplet-number::calc-fraction-text
                            \times 7/8 {
                                \override Tie.direction = #up                                            %! OC1
                                b'16
                                ~                                                                        %! SC
                                [
                                b'16
                                ~                                                                        %! SC
                                ]
                                b'4
                                ~                                                                        %! SC
                                b'16
                                \revert Tie.direction                                                    %! OC2
                                r16
                            }
                            \times 4/5 {
                                b'16
                                \revert Stem.direction                                                   %! OC2
                                r4
                                \revert TupletBracket.staff-padding                                      %! OC2
                            }
                        }
                    }
                >>

        """
        return OverrideCommand(
            attribute='direction',
            value=abjad.Up,
            grob='tie',
            selector=selector,
            )

    @staticmethod
    def time_signature_extra_offset(
        pair: typings.NumberPair,
        *,
        selector: typings.Selector = 'baca.leaf(0)',
        ) -> OverrideCommand:
        r"""
        Overrides time signature extra offset.

        ..  container:: example

            Overrides time signature extra offset on leaf 0:

            >>> music_maker = baca.MusicMaker()
            >>> contribution = music_maker(
            ...     'Voice 1',
            ...     [[0, 2, 10], [18, 16, 15, 20, 19], [9]],
            ...     baca.rests_around([2], [4]),
            ...     baca.time_signature_extra_offset((-6, 0)),
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
                    \context Voice = "Voice 1"
                    {
                        \voiceOne
                        {
                            \tweak text #tuplet-number::calc-fraction-text
                            \times 9/10 {
                                \once \override Score.TimeSignature.extra-offset = #'(-6 . 0)            %! OC1
                                \override TupletBracket.staff-padding = #5                               %! OC1
                                r8
                                c'16
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
                                \revert TupletBracket.staff-padding                                      %! OC2
                            }
                        }
                    }
                >>

        """
        assert isinstance(pair, tuple), repr(pair)
        return OverrideCommand(
            attribute='extra_offset',
            value=pair,
            context='Score',
            grob='time_signature',
            selector=selector,
            )

    @staticmethod
    def time_signature_transparent(
        *,
        selector: typings.Selector = 'baca.leaves()',
        ) -> OverrideCommand:
        r"""
        Overrides time signature transparency.

        ..  container:: example

            Makes all time signatures transparent:

            >>> music_maker = baca.MusicMaker()
            >>> contribution = music_maker(
            ...     'Voice 1',
            ...     [[0, 2, 10], [18, 16, 15, 20, 19], [9]],
            ...     baca.rests_around([2], [4]),
            ...     baca.time_signature_transparent(),
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
                    \context Voice = "Voice 1"
                    {
                        \voiceOne
                        {
                            \tweak text #tuplet-number::calc-fraction-text
                            \times 9/10 {
                                \override Score.TimeSignature.transparent = ##t                          %! OC1
                                \override TupletBracket.staff-padding = #5                               %! OC1
                                r8
                                c'16
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
                                \revert Score.TimeSignature.transparent                                  %! OC2
                                \revert TupletBracket.staff-padding                                      %! OC2
                            }
                        }
                    }
                >>

        """
        return OverrideCommand(
            attribute='transparent',
            value=True,
            context='Score',
            grob='time_signature',
            selector=selector,
            )

    @staticmethod
    def tremolo_down(
        n: typings.Number,
        *,
        selector: typings.Selector = 'baca.tleaves()',
        ) -> OverrideCommand:
        """
        Overrides stem tremolo extra offset.
        """
        pair = (0, -n)
        return OverrideCommand(
            attribute='extra_offset',
            value=str(pair),
            grob='stem_tremolo',
            selector=selector,
            )

    @staticmethod
    def trill_spanner(
        string: str = None,
        *,
        harmonic: bool = None,
        left_broken: bool = None,
        right_broken: bool = None,
        selector: typings.Selector = 'baca.tleaves().with_next_leaf()',
        ) -> SpannerCommand:
        r"""
        Attaches trill spanner.

        ..  container:: example

            Attaches trill spanner to trimmed leaves (leaked to the right):

            >>> music_maker = baca.MusicMaker()
            >>> contribution = music_maker(
            ...     'Voice 1',
            ...     [[0, 2, 10], [18, 16, 15, 20, 19], [9]],
            ...     baca.rests_around([2], [4]),
            ...     baca.trill_spanner(),
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
                    \context Voice = "Voice 1"
                    {
                        \voiceOne
                        {
                            \tweak text #tuplet-number::calc-fraction-text
                            \times 9/10 {
                                \override TupletBracket.staff-padding = #5                               %! OC1
                                r8
                                c'16
                                [
                                \startTrillSpan
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
                                \stopTrillSpan                                                           %! SC
                                \revert TupletBracket.staff-padding                                      %! OC2
                            }
                        }
                    }
                >>

        ..  container:: example

            Attaches trill spanner to trimmed leaves (leaked to the right) in
            every equipitch run:

            >>> music_maker = baca.MusicMaker()
            >>> contribution = music_maker(
            ...     'Voice 1',
            ...     [[0, 2, 10], [18, 16, 15, 20, 19], [9]],
            ...     baca.map(
            ...         baca.qruns(),
            ...         baca.trill_spanner(),
            ...         ),
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
                    \context Voice = "Voice 1"
                    {
                        \voiceOne
                        {
                            \tweak text #tuplet-number::calc-fraction-text
                            \times 9/10 {
                                \override TupletBracket.staff-padding = #5                               %! OC1
                                r8
                                c'16
                                [
                                \startTrillSpan
                                d'16
                                ]
                                \stopTrillSpan                                                           %! SC
                                \startTrillSpan
                                bf'4
                                ~
                                \stopTrillSpan                                                           %! SC
                                \startTrillSpan
                                bf'16
                                r16
                                \stopTrillSpan                                                           %! SC
                            }
                            \tweak text #tuplet-number::calc-fraction-text
                            \times 9/10 {
                                fs''16
                                [
                                \startTrillSpan
                                e''16
                                ]
                                \stopTrillSpan                                                           %! SC
                                \startTrillSpan
                                ef''4
                                ~
                                \stopTrillSpan                                                           %! SC
                                \startTrillSpan
                                ef''16
                                r16
                                \stopTrillSpan                                                           %! SC
                                af''16
                                [
                                \startTrillSpan
                                g''16
                                ]
                                \stopTrillSpan                                                           %! SC
                                \startTrillSpan
                            }
                            \times 4/5 {
                                a'16
                                \stopTrillSpan                                                           %! SC
                                \startTrillSpan
                                r4
                                \stopTrillSpan                                                           %! SC
                                \revert TupletBracket.staff-padding                                      %! OC2
                            }
                        }
                    }
                >>

        ..  container:: example

            Attaches trill to trimmed leaves (leaked to the right) in every
            run:

            >>> music_maker = baca.MusicMaker()
            >>> contribution = music_maker(
            ...     'Voice 1',
            ...     [[0, 2, 10], [18, 16, 15, 20, 19], [9]],
            ...     baca.map(
            ...         baca.runs(),
            ...         baca.trill_spanner(),
            ...         ),
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
                    \context Voice = "Voice 1"
                    {
                        \voiceOne
                        {
                            \tweak text #tuplet-number::calc-fraction-text
                            \times 9/10 {
                                \override TupletBracket.staff-padding = #5                               %! OC1
                                r8
                                c'16
                                [
                                \startTrillSpan
                                d'16
                                ]
                                bf'4
                                ~
                                bf'16
                                r16
                                \stopTrillSpan                                                           %! SC
                            }
                            \tweak text #tuplet-number::calc-fraction-text
                            \times 9/10 {
                                fs''16
                                [
                                \startTrillSpan
                                e''16
                                ]
                                ef''4
                                ~
                                ef''16
                                r16
                                \stopTrillSpan                                                           %! SC
                                af''16
                                [
                                \startTrillSpan
                                g''16
                                ]
                            }
                            \times 4/5 {
                                a'16
                                r4
                                \stopTrillSpan                                                           %! SC
                                \revert TupletBracket.staff-padding                                      %! OC2
                            }
                        }
                    }
                >>

        ..  container:: example

            Attaches pitched trill to trimmed leaves (leaked to the right) in
            equipitch run 0:

            >>> music_maker = baca.MusicMaker()
            >>> contribution = music_maker(
            ...     'Voice 1',
            ...     [[0, 2, 10], [18, 16, 15, 20, 19], [9]],
            ...     baca.rests_around([2], [4]),
            ...     baca.map(
            ...         baca.qrun(0),
            ...         baca.trill_spanner(string='Eb4'),
            ...         ),
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
                    \context Voice = "Voice 1"
                    {
                        \voiceOne
                        {
                            \tweak text #tuplet-number::calc-fraction-text
                            \times 9/10 {
                                \override TupletBracket.staff-padding = #5                               %! OC1
                                r8
                                \pitchedTrill                                                            %! SC
                                c'16
                                [
                                \startTrillSpan ef'
                                d'16
                                ]
                                \stopTrillSpan                                                           %! SC
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
                                \revert TupletBracket.staff-padding                                      %! OC2
                            }
                        }
                    }
                >>

        ..  container:: example

            Attaches pitched trill to trimmed leaves (leaked to the right) in
            every equipitch run:

            >>> music_maker = baca.MusicMaker()
            >>> contribution = music_maker(
            ...     'Voice 1',
            ...     [[0, 2, 10], [18, 16, 15, 20, 19], [9]],
            ...     baca.map(
            ...         baca.qruns(),
            ...         baca.trill_spanner(string='Eb4'),
            ...         ),
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
                    \context Voice = "Voice 1"
                    {
                        \voiceOne
                        {
                            \tweak text #tuplet-number::calc-fraction-text
                            \times 9/10 {
                                \override TupletBracket.staff-padding = #5                               %! OC1
                                r8
                                \pitchedTrill                                                            %! SC
                                c'16
                                [
                                \startTrillSpan ef'
                                \pitchedTrill                                                            %! SC
                                d'16
                                ]
                                \stopTrillSpan                                                           %! SC
                                \startTrillSpan ef'
                                \pitchedTrill                                                            %! SC
                                bf'4
                                ~
                                \stopTrillSpan                                                           %! SC
                                \startTrillSpan ef'
                                bf'16
                                r16
                                \stopTrillSpan                                                           %! SC
                            }
                            \tweak text #tuplet-number::calc-fraction-text
                            \times 9/10 {
                                \pitchedTrill                                                            %! SC
                                fs''16
                                [
                                \startTrillSpan ef'
                                \pitchedTrill                                                            %! SC
                                e''16
                                ]
                                \stopTrillSpan                                                           %! SC
                                \startTrillSpan ef'
                                \pitchedTrill                                                            %! SC
                                ef''4
                                ~
                                \stopTrillSpan                                                           %! SC
                                \startTrillSpan ef'
                                ef''16
                                r16
                                \stopTrillSpan                                                           %! SC
                                \pitchedTrill                                                            %! SC
                                af''16
                                [
                                \startTrillSpan ef'
                                \pitchedTrill                                                            %! SC
                                g''16
                                ]
                                \stopTrillSpan                                                           %! SC
                                \startTrillSpan ef'
                            }
                            \times 4/5 {
                                \pitchedTrill                                                            %! SC
                                a'16
                                \stopTrillSpan                                                           %! SC
                                \startTrillSpan ef'
                                r4
                                \stopTrillSpan                                                           %! SC
                                \revert TupletBracket.staff-padding                                      %! OC2
                            }
                        }
                    }
                >>

        ..  container:: example

            Attaches pitched trill (specified by interval) to trimmed leaves
            (leaked to the right) in every equipitch run:

            >>> music_maker = baca.MusicMaker()
            >>> contribution = music_maker(
            ...     'Voice 1',
            ...     [[0, 2, 10], [18, 16, 15, 20, 19], [9]],
            ...     baca.map(
            ...         baca.qruns(),
            ...         baca.trill_spanner(string='M2'),
            ...         ),
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
                    \context Voice = "Voice 1"
                    {
                        \voiceOne
                        {
                            \tweak text #tuplet-number::calc-fraction-text
                            \times 9/10 {
                                \override TupletBracket.staff-padding = #5                               %! OC1
                                r8
                                \pitchedTrill                                                            %! SC
                                c'16
                                [
                                \startTrillSpan d'
                                \pitchedTrill                                                            %! SC
                                d'16
                                ]
                                \stopTrillSpan                                                           %! SC
                                \startTrillSpan e'
                                \pitchedTrill                                                            %! SC
                                bf'4
                                ~
                                \stopTrillSpan                                                           %! SC
                                \startTrillSpan c''
                                bf'16
                                r16
                                \stopTrillSpan                                                           %! SC
                            }
                            \tweak text #tuplet-number::calc-fraction-text
                            \times 9/10 {
                                \pitchedTrill                                                            %! SC
                                fs''16
                                [
                                \startTrillSpan gs''
                                \pitchedTrill                                                            %! SC
                                e''16
                                ]
                                \stopTrillSpan                                                           %! SC
                                \startTrillSpan fs''
                                \pitchedTrill                                                            %! SC
                                ef''4
                                ~
                                \stopTrillSpan                                                           %! SC
                                \startTrillSpan f''
                                ef''16
                                r16
                                \stopTrillSpan                                                           %! SC
                                \pitchedTrill                                                            %! SC
                                af''16
                                [
                                \startTrillSpan bf''
                                \pitchedTrill                                                            %! SC
                                g''16
                                ]
                                \stopTrillSpan                                                           %! SC
                                \startTrillSpan a''
                            }
                            \times 4/5 {
                                \pitchedTrill                                                            %! SC
                                a'16
                                \stopTrillSpan                                                           %! SC
                                \startTrillSpan b'
                                r4
                                \stopTrillSpan                                                           %! SC
                                \revert TupletBracket.staff-padding                                      %! OC2
                            }
                        }
                    }
                >>

        """
        if string is None:
            interval = None
            pitch = None
        else:
            try:
                interval = None
                pitch = abjad.NamedPitch(string)
            except ValueError:
                interval = abjad.NamedInterval(string)
                pitch = None
        return SpannerCommand(
            left_broken=left_broken,
            right_broken=right_broken,
            spanner=abjad.TrillSpanner(
                interval=interval,
                is_harmonic=harmonic,
                pitch=pitch,
                ),
            selector=selector,
            )

    @staticmethod
    def trill_spanner_staff_padding(
        n: typings.Number,
        *,
        selector: typings.Selector = 'baca.tleaves().with_next_leaf()',
        ) -> OverrideCommand:
        """
        Overrides trill spanner staff padding.
        """
        return OverrideCommand(
            attribute='staff_padding',
            value=n,
            grob='trill_spanner',
            selector=selector,
            )

    @staticmethod
    def tuplet_bracket_down(
        *,
        selector: typings.Selector = 'baca.leaves()',
        ) -> OverrideCommand:
        r"""
        Overrides tuplet bracket direction.

        ..  container:: example

            Overrides tuplet bracket direction on leaves:

            >>> music_maker = baca.MusicMaker()
            >>> contribution = music_maker(
            ...     'Voice 1',
            ...     [[0, 2, 10], [18, 16, 15, 20, 19], [9]],
            ...     baca.rests_around([2], [4]),
            ...     baca.tuplet_bracket_staff_padding(5),
            ...     baca.tuplet_bracket_down(),
            ...     counts=[1, 1, 5, -1],
            ...     time_treatments=[-1],
            ...     )
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
                            \tweak text #tuplet-number::calc-fraction-text
                            \times 9/10 {
                                \override TupletBracket.staff-padding = #5                               %! OC1
                                \override TupletBracket.direction = #down                                %! OC1
                                r8
                                c'16
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
                                \revert TupletBracket.staff-padding                                      %! OC2
                                \revert TupletBracket.direction                                          %! OC2
                            }
                        }
                    }
                >>

        ..  container:: example

            Overrides tuplet bracket direction on leaves in tuplet 1:

            >>> music_maker = baca.MusicMaker()
            >>> contribution = music_maker(
            ...     'Voice 1',
            ...     [[0, 2, 10], [18, 16, 15, 20, 19], [9]],
            ...     baca.rests_around([2], [4]),
            ...     baca.tuplet_bracket_staff_padding(5),
            ...     baca.map(
            ...         baca.tuplet(1),
            ...         baca.tuplet_bracket_down(),
            ...         ),
            ...     counts=[1, 1, 5, -1],
            ...     time_treatments=[-1],
            ...     )
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
                            \tweak text #tuplet-number::calc-fraction-text
                            \times 9/10 {
                                \override TupletBracket.staff-padding = #5                               %! OC1
                                r8
                                c'16
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
                                \override TupletBracket.direction = #down                                %! OC1
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
                                \revert TupletBracket.direction                                          %! OC2
                            }
                            \times 4/5 {
                                a'16
                                r4
                                \revert TupletBracket.staff-padding                                      %! OC2
                            }
                        }
                    }
                >>

        """
        return OverrideCommand(
            attribute='direction',
            value=abjad.Down,
            grob='tuplet_bracket',
            selector=selector,
            )

    @staticmethod
    def tuplet_bracket_extra_offset(
        pair: typings.NumberPair,
        *,
        selector: typings.Selector = 'baca.leaf(0)',
        ) -> OverrideCommand:
        r"""
        Overrides tuplet bracket extra offset.

        ..  container:: example

            Overrides tuplet bracket extra offset on leaf 0:

            >>> music_maker = baca.MusicMaker()
            >>> contribution = music_maker(
            ...     'Voice 1',
            ...     [[0, 2, 10], [18, 16, 15, 20, 19], [9]],
            ...     baca.rests_around([2], [4]),
            ...     baca.tuplet_bracket_extra_offset((-1, 0)),
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
                    \context Voice = "Voice 1"
                    {
                        \voiceOne
                        {
                            \tweak text #tuplet-number::calc-fraction-text
                            \times 9/10 {
                                \once \override TupletBracket.extra-offset = #'(-1 . 0)                  %! OC1
                                \override TupletBracket.staff-padding = #5                               %! OC1
                                r8
                                c'16
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
                                \revert TupletBracket.staff-padding                                      %! OC2
                            }
                        }
                    }
                >>

        ..  container:: example

            Overrides tuplet bracket extra offset on leaves in tuplet 1:

            >>> music_maker = baca.MusicMaker()
            >>> contribution = music_maker(
            ...     'Voice 1',
            ...     [[0, 2, 10], [18, 16, 15, 20, 19], [9]],
            ...     baca.rests_around([2], [4]),
            ...     baca.map(
            ...         baca.tuplet(1),
            ...         baca.tuplet_bracket_extra_offset((-1, 0)),
            ...         ),
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
                    \context Voice = "Voice 1"
                    {
                        \voiceOne
                        {
                            \tweak text #tuplet-number::calc-fraction-text
                            \times 9/10 {
                                \override TupletBracket.staff-padding = #5                               %! OC1
                                r8
                                c'16
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
                                \once \override TupletBracket.extra-offset = #'(-1 . 0)                  %! OC1
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
                                \revert TupletBracket.staff-padding                                      %! OC2
                            }
                        }
                    }
                >>

        """
        return OverrideCommand(
            attribute='extra_offset',
            value=pair,
            grob='tuplet_bracket',
            selector=selector,
            )

    @staticmethod
    def tuplet_bracket_outside_staff_priority(
        n: typings.Number,
        *,
        selector: typings.Selector = 'baca.leaves()',
        ) -> OverrideCommand:
        """
        Overrides tuplet bracket outside-staff-priority.
        """
        return OverrideCommand(
            attribute='outside_staff_priority',
            value=n,
            grob='tuplet_bracket',
            selector=selector,
            )

    @staticmethod
    def tuplet_bracket_padding(
        n: typings.Number,
        *,
        selector: typings.Selector = 'baca.leaves()',
        ) -> OverrideCommand:
        """
        Overrides tuplet bracket padding.
        """
        return OverrideCommand(
            attribute='padding',
            value=n,
            grob='tuplet_bracket',
            selector=selector,
            )

    @staticmethod
    def tuplet_bracket_shorten_pair(
        pair: typings.NumberPair,
        *,
        selector: typings.Selector = 'baca.leaf(0)',
        ) -> OverrideCommand:
        """
        Overrides tuplet bracket shorten pair.
        """
        return OverrideCommand(
            attribute='shorten_pair',
            value=pair,
            grob='tuplet_bracket',
            selector=selector,
            )

    @staticmethod
    def tuplet_bracket_staff_padding(
        n: typings.Number,
        *,
        selector: typings.Selector = 'baca.leaves()',
        ) -> OverrideCommand:
        r"""
        Overrides tuplet bracket staff padding.

        ..  container:: example

            Overrides tuplet bracket staff padding on leaves:

            >>> music_maker = baca.MusicMaker()
            >>> contribution = music_maker(
            ...     'Voice 1',
            ...     [[0, 2, 10], [18, 16, 15, 20, 19], [9]],
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
                    \context Voice = "Voice 1"
                    {
                        \voiceOne
                        {
                            \tweak text #tuplet-number::calc-fraction-text
                            \times 9/10 {
                                \override TupletBracket.staff-padding = #5                               %! OC1
                                r8
                                c'16
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
                                \revert TupletBracket.staff-padding                                      %! OC2
                            }
                        }
                    }
                >>

        ..  container:: example

            Overrides tuplet bracket staff padding on leaves in tuplet 1:

            >>> music_maker = baca.MusicMaker()
            >>> contribution = music_maker(
            ...     'Voice 1',
            ...     [[0, 2, 10], [18, 16, 15, 20, 19], [9]],
            ...     baca.rests_around([2], [4]),
            ...     baca.map(
            ...         baca.tuplet(1),
            ...         baca.tuplet_bracket_staff_padding(5),
            ...         ),
            ...     counts=[1, 1, 5, -1],
            ...     time_treatments=[-1],
            ...     )
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
                            \tweak text #tuplet-number::calc-fraction-text
                            \times 9/10 {
                                r8
                                c'16
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
                                \override TupletBracket.staff-padding = #5                               %! OC1
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
                                \revert TupletBracket.staff-padding                                      %! OC2
                            }
                            \times 4/5 {
                                a'16
                                r4
                            }
                        }
                    }
                >>

        """
        return OverrideCommand(
            attribute='staff_padding',
            value=n,
            grob='tuplet_bracket',
            selector=selector,
            )

    @staticmethod
    def tuplet_bracket_up(
        *,
        selector: typings.Selector = 'baca.leaves()',
        ) -> OverrideCommand:
        r"""
        Overrides tuplet bracket direction.

        ..  container:: example

            Override tuplet bracket direction on leaves:

            >>> music_maker = baca.MusicMaker()
            >>> contribution = music_maker(
            ...     'Voice 1',
            ...     [[0, 2, 10], [18, 16, 15, 20, 19], [9]],
            ...     baca.rests_around([2], [4]),
            ...     baca.tuplet_bracket_staff_padding(5),
            ...     baca.tuplet_bracket_up(),
            ...     counts=[1, 1, 5, -1],
            ...     time_treatments=[-1],
            ...     )
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
                            \tweak text #tuplet-number::calc-fraction-text
                            \times 9/10 {
                                \override TupletBracket.staff-padding = #5                               %! OC1
                                \override TupletBracket.direction = #up                                  %! OC1
                                r8
                                c'16
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
                                \revert TupletBracket.staff-padding                                      %! OC2
                                \revert TupletBracket.direction                                          %! OC2
                            }
                        }
                    }
                >>

        ..  container:: example

            Override tuplet bracket direction on leaves in tuplet 1:

            >>> music_maker = baca.MusicMaker()
            >>> contribution = music_maker(
            ...     'Voice 1',
            ...     [[0, 2, 10], [18, 16, 15, 20, 19], [9]],
            ...     baca.rests_around([2], [4]),
            ...     baca.tuplet_bracket_staff_padding(5),
            ...     baca.map(
            ...         baca.tuplet(1),
            ...         baca.tuplet_bracket_up(),
            ...         ),
            ...     counts=[1, 1, 5, -1],
            ...     time_treatments=[-1],
            ...     )
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
                            \tweak text #tuplet-number::calc-fraction-text
                            \times 9/10 {
                                \override TupletBracket.staff-padding = #5                               %! OC1
                                r8
                                c'16
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
                                \override TupletBracket.direction = #up                                  %! OC1
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
                                \revert TupletBracket.direction                                          %! OC2
                            }
                            \times 4/5 {
                                a'16
                                r4
                                \revert TupletBracket.staff-padding                                      %! OC2
                            }
                        }
                    }
                >>

        """
        return OverrideCommand(
            attribute='direction',
            value=abjad.Up,
            grob='tuplet_bracket',
            selector=selector,
            )

    @staticmethod
    def tuplet_number_denominator(
        *,
        selector: typings.Selector = 'baca.leaves()',
        ) -> OverrideCommand:
        """
        Overrides tuplet number text.
        """
        return OverrideCommand(
            attribute='text',
            value='tuplet-number::calc-denominator-text',
            grob='tuplet_number',
            selector=selector,
            )

    @staticmethod
    def tuplet_number_extra_offset(
        pair: typings.NumberPair,
        *,
        selector: typings.Selector = 'baca.leaf(0)',
        ) -> OverrideCommand:
        r"""
        Overrides tuplet number extra offset.

        ..  container:: example

            Overrides tuplet number extra offset on leaf 0:

            >>> music_maker = baca.MusicMaker()
            >>> contribution = music_maker(
            ...     'Voice 1',
            ...     [[0, 2, 10], [18, 16, 15, 20, 19], [9]],
            ...     baca.rests_around([2], [4]),
            ...     baca.tuplet_bracket_staff_padding(5),
            ...     baca.tuplet_number_extra_offset((-1, 0)),
            ...     counts=[1, 1, 5, -1],
            ...     time_treatments=[-1],
            ...     )
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
                            \tweak text #tuplet-number::calc-fraction-text
                            \times 9/10 {
                                \override TupletBracket.staff-padding = #5                               %! OC1
                                \once \override TupletNumber.extra-offset = #'(-1 . 0)                   %! OC1
                                r8
                                c'16
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
                                \revert TupletBracket.staff-padding                                      %! OC2
                            }
                        }
                    }
                >>

        ..  container:: example

            Overrides tuplet number extra offset on leaves in tuplet 1:

            >>> music_maker = baca.MusicMaker()
            >>> contribution = music_maker(
            ...     'Voice 1',
            ...     [[0, 2, 10], [18, 16, 15, 20, 19], [9]],
            ...     baca.rests_around([2], [4]),
            ...     baca.tuplet_bracket_staff_padding(5),
            ...     baca.map(
            ...         baca.tuplet(1),
            ...         baca.tuplet_number_extra_offset((-1, 0)),
            ...         ),
            ...     counts=[1, 1, 5, -1],
            ...     time_treatments=[-1],
            ...     )
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
                            \tweak text #tuplet-number::calc-fraction-text
                            \times 9/10 {
                                \override TupletBracket.staff-padding = #5                               %! OC1
                                r8
                                c'16
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
                                \once \override TupletNumber.extra-offset = #'(-1 . 0)                   %! OC1
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
                                \revert TupletBracket.staff-padding                                      %! OC2
                            }
                        }
                    }
                >>

        """
        return OverrideCommand(
            attribute='extra_offset',
            value=pair,
            grob='tuplet_number',
            selector=selector,
            )

    @staticmethod
    def untie_to(
        *,
        selector: typings.Selector = 'baca.pleaf(0)',
        ) -> TieCorrectionCommand:
        r"""
        Unties to leaf.

        ..  container:: example

            >>> maker = baca.SegmentMaker(
            ...     ignore_unpitched_notes=True,
            ...     score_template=baca.SingleStaffScoreTemplate(),
            ...     time_signatures=[(4, 8), (3, 8), (4, 8), (3, 8)],
            ...     )

            >>> maker(
            ...     'MusicVoice',
            ...     baca.make_tied_notes(),
            ...     baca.untie_to(selector=baca.leaf(2)),
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
                            \time 4/8                                                                    %! SM8:EXPLICIT_TIME_SIGNATURE:SM1
                            \once \override Score.TimeSignature.color = #(x11-color 'blue)               %! SM6:EXPLICIT_TIME_SIGNATURE_COLOR:SM1
                            s1 * 1/2
                <BLANKLINE>
                            % [GlobalSkips measure 2]                                                    %! SM4
                            \time 3/8                                                                    %! SM8:EXPLICIT_TIME_SIGNATURE:SM1
                            \once \override Score.TimeSignature.color = #(x11-color 'blue)               %! SM6:EXPLICIT_TIME_SIGNATURE_COLOR:SM1
                            s1 * 3/8
                <BLANKLINE>
                            % [GlobalSkips measure 3]                                                    %! SM4
                            \time 4/8                                                                    %! SM8:EXPLICIT_TIME_SIGNATURE:SM1
                            \once \override Score.TimeSignature.color = #(x11-color 'blue)               %! SM6:EXPLICIT_TIME_SIGNATURE_COLOR:SM1
                            s1 * 1/2
                <BLANKLINE>
                            % [GlobalSkips measure 4]                                                    %! SM4
                            \time 3/8                                                                    %! SM8:EXPLICIT_TIME_SIGNATURE:SM1
                            \once \override Score.TimeSignature.color = #(x11-color 'blue)               %! SM6:EXPLICIT_TIME_SIGNATURE_COLOR:SM1
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
                <BLANKLINE>
                                % [MusicVoice measure 1]                                                 %! SM4
                                c'2
                                ~
                <BLANKLINE>
                                % [MusicVoice measure 2]                                                 %! SM4
                                c'4.
                <BLANKLINE>
                                % [MusicVoice measure 3]                                                 %! SM4
                                c'2
                                ~
                <BLANKLINE>
                                % [MusicVoice measure 4]                                                 %! SM4
                                c'4.
                <BLANKLINE>
                            }
                        }
                    >>
                >>

        """
        return TieCorrectionCommand(
            direction=abjad.Left,
            selector=selector,
            untie=True,
            )

    @staticmethod
    def up_arpeggio(
        *,
        selector: typings.Selector = 'baca.chead(0)',
        ) -> IndicatorCommand:
        r"""
        Attaches up-arpeggio.

        ..  container:: example

            Attaches up-arpeggios to chord head 0:

            >>> music_maker = baca.MusicMaker()
            >>> contribution = music_maker(
            ...     'Voice 1',
            ...     [{0, 2, 10}, [17], {15, 16, 30}, {7, 20}, [9]],
            ...     baca.up_arpeggio(),
            ...     counts=[5, -3],
            ...     talea_denominator=32,
            ...     )
            >>> lilypond_file = music_maker.show(contribution)
            >>> abjad.show(lilypond_file, strict=89) # doctest: +SKIP
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
                                \arpeggioArrowUp                                                         %! IC
                                <c' d' bf'>8
                                \arpeggio                                                                %! IC
                                ~
                                [
                                <c' d' bf'>32
                                ]
                                r16.
                            }
                            \scaleDurations #'(1 . 1) {
                                f''8
                                ~
                                [
                                f''32
                                ]
                                r16.
                            }
                            \scaleDurations #'(1 . 1) {
                                <ef'' e'' fs'''>8
                                ~
                                [
                                <ef'' e'' fs'''>32
                                ]
                                r16.
                            }
                            \scaleDurations #'(1 . 1) {
                                <g' af''>8
                                ~
                                [
                                <g' af''>32
                                ]
                                r16.
                            }
                            \scaleDurations #'(1 . 1) {
                                a'8
                                ~
                                [
                                a'32
                                ]
                                r16.
                            }
                        }
                    }
                >>

        ..  container:: example

            Attaches up-arpeggios to last two chord heads:

            >>> music_maker = baca.MusicMaker()
            >>> contribution = music_maker(
            ...     'Voice 1',
            ...     [{0, 2, 10}, [17], {15, 16, 30}, {7, 20}, [9]],
            ...     baca.up_arpeggio(selector=baca.cheads()[-2:]),
            ...     counts=[5, -3],
            ...     talea_denominator=32,
            ...     )
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
                                <c' d' bf'>8
                                ~
                                [
                                <c' d' bf'>32
                                ]
                                r16.
                            }
                            \scaleDurations #'(1 . 1) {
                                f''8
                                ~
                                [
                                f''32
                                ]
                                r16.
                            }
                            \scaleDurations #'(1 . 1) {
                                \arpeggioArrowUp                                                         %! IC
                                <ef'' e'' fs'''>8
                                \arpeggio                                                                %! IC
                                ~
                                [
                                <ef'' e'' fs'''>32
                                ]
                                r16.
                            }
                            \scaleDurations #'(1 . 1) {
                                \arpeggioArrowUp                                                         %! IC
                                <g' af''>8
                                \arpeggio                                                                %! IC
                                ~
                                [
                                <g' af''>32
                                ]
                                r16.
                            }
                            \scaleDurations #'(1 . 1) {
                                a'8
                                ~
                                [
                                a'32
                                ]
                                r16.
                            }
                        }
                    }
                >>

        """
        return IndicatorCommand(
            indicators=[abjad.Arpeggio(direction=abjad.Up)],
            selector=selector,
            )

    @staticmethod
    def up_bow(
        *,
        selector: typings.Selector = 'baca.phead(0)',
        ) -> IndicatorCommand:
        r"""
        Attaches up-bow.

        ..  container:: example

            Attaches up-bow to pitched head 0:

            >>> music_maker = baca.MusicMaker()
            >>> contribution = music_maker(
            ...     'Voice 1',
            ...     [[0, 2, 10], [18, 16, 15, 20, 19], [9]],
            ...     baca.rests_around([2], [4]),
            ...     baca.tuplet_bracket_staff_padding(5),
            ...     baca.up_bow(),
            ...     counts=[1, 1, 5, -1],
            ...     time_treatments=[-1],
            ...     )
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
                            \tweak text #tuplet-number::calc-fraction-text
                            \times 9/10 {
                                \override TupletBracket.staff-padding = #5                               %! OC1
                                r8
                                c'16
                                -\upbow                                                                  %! IC
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
                                \revert TupletBracket.staff-padding                                      %! OC2
                            }
                        }
                    }
                >>

        ..  container:: example

            Attaches up-bow to pitched heads in tuplet 1:

            >>> music_maker = baca.MusicMaker()
            >>> contribution = music_maker(
            ...     'Voice 1',
            ...     [[0, 2, 10], [18, 16, 15, 20, 19], [9]],
            ...     baca.map(
            ...         baca.tuplet(1),
            ...         baca.up_bow(selector=baca.pheads()),
            ...         ),
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
                    \context Voice = "Voice 1"
                    {
                        \voiceOne
                        {
                            \tweak text #tuplet-number::calc-fraction-text
                            \times 9/10 {
                                \override TupletBracket.staff-padding = #5                               %! OC1
                                r8
                                c'16
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
                                -\upbow                                                                  %! IC
                                [
                                e''16
                                -\upbow                                                                  %! IC
                                ]
                                ef''4
                                -\upbow                                                                  %! IC
                                ~
                                ef''16
                                r16
                                af''16
                                -\upbow                                                                  %! IC
                                [
                                g''16
                                -\upbow                                                                  %! IC
                                ]
                            }
                            \times 4/5 {
                                a'16
                                r4
                                \revert TupletBracket.staff-padding                                      %! OC2
                            }
                        }
                    }
                >>

        """
        return IndicatorCommand(
            indicators=[abjad.Articulation('upbow')],
            selector=selector,
            )

    @staticmethod
    def very_long_fermata(
        *,
        selector: typings.Selector = 'baca.leaf(0)',
        ) -> IndicatorCommand:
        r"""
        Attaches very long fermata.

        ..  container:: example

            Attaches very long fermata to first leaf:

            >>> music_maker = baca.MusicMaker()
            >>> contribution = music_maker(
            ...     'Voice 1',
            ...     [[0, 2, 10], [18, 16, 15, 20, 19], [9]],
            ...     baca.very_long_fermata(),
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
                    \context Voice = "Voice 1"
                    {
                        \voiceOne
                        {
                            \tweak text #tuplet-number::calc-fraction-text
                            \times 9/10 {
                                \override TupletBracket.staff-padding = #5                               %! OC1
                                r8
                                -\verylongfermata                                                        %! IC
                                c'16
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
                                \revert TupletBracket.staff-padding                                      %! OC2
                            }
                        }
                    }
                >>

        ..  container:: example

            Attaches very long fermata to first leaf in tuplet 1:

            >>> music_maker = baca.MusicMaker()
            >>> contribution = music_maker(
            ...     'Voice 1',
            ...     [[0, 2, 10], [18, 16, 15, 20, 19], [9]],
            ...     baca.very_long_fermata(
            ...         selector=baca.tuplets()[1:2].phead(0),
            ...         ),
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
                    \context Voice = "Voice 1"
                    {
                        \voiceOne
                        {
                            \tweak text #tuplet-number::calc-fraction-text
                            \times 9/10 {
                                \override TupletBracket.staff-padding = #5                               %! OC1
                                r8
                                c'16
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
                                -\verylongfermata                                                        %! IC
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
                                \revert TupletBracket.staff-padding                                      %! OC2
                            }
                        }
                    }
                >>

        """
        return IndicatorCommand(
            indicators=[abjad.Articulation('verylongfermata')],
            selector=selector,
            )

    @staticmethod
    def voice_four(
        *,
        selector: typings.Selector = 'baca.leaf(0)',
        ) -> IndicatorCommand:
        r"""
        Makes LilyPond ``\voiceFour`` command.
        """
        literal = abjad.LilyPondLiteral(r'\voiceFour')
        return IndicatorCommand(
            indicators=[literal],
            selector=selector,
            )

    @staticmethod
    def voice_one(
        *,
        selector: typings.Selector = 'baca.leaf(0)',
        ) -> IndicatorCommand:
        r"""
        Makes LilyPond ``\voiceOne`` command.
        """
        literal = abjad.LilyPondLiteral(r'\voiceOne')
        return IndicatorCommand(
            indicators=[literal],
            selector=selector,
            )

    @staticmethod
    def voice_three(
        *,
        selector: typings.Selector = 'baca.leaf(0)',
        ) -> IndicatorCommand:
        r"""
        Makes LilyPond ``\voiceThree`` command.
        """
        literal = abjad.LilyPondLiteral(r'\voiceThree')
        return IndicatorCommand(
            indicators=[literal],
            selector=selector,
            )

    @staticmethod
    def voice_two(
        *,
        selector: typings.Selector = 'baca.leaf(0)',
        ) -> IndicatorCommand:
        r"""
        Makes LilyPond ``\voiceTwo`` command.
        """
        literal = abjad.LilyPondLiteral(r'\voiceTwo')
        return IndicatorCommand(
            indicators=[literal],
            selector=selector,
            )

    @staticmethod
    def volta(
        *,
        selector: typings.Selector = 'baca.leaves()',
        ) -> VoltaCommand:
        r"""
        Makes volta container and extends container with ``selector`` output.

        ..  container:: example

            Wraps stage 1 (global skips 1 and 2) in volta container:

            >>> maker = baca.SegmentMaker(
            ...     score_template=baca.SingleStaffScoreTemplate(),
            ...     time_signatures=[(4, 8), (3, 8), (4, 8), (3, 8)],
            ...     )

            >>> maker(
            ...     'MusicVoice',
            ...     baca.pitches('E4 D5 F4 E5 G4 F5'),
            ...     baca.RhythmCommand(
            ...         rhythm_maker=rmakers.TaleaRhythmMaker(
            ...             talea=rmakers.Talea(
            ...                 counts=[1, 1, 1, -1],
            ...                 denominator=8,
            ...                 ),
            ...             ),
            ...         ),
            ...     )

            >>> maker(
            ...     'GlobalSkips',
            ...     baca.volta(selector=baca.skips()[1:3]),
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
                            \time 4/8                                                                    %! SM8:EXPLICIT_TIME_SIGNATURE:SM1
                            \once \override Score.TimeSignature.color = #(x11-color 'blue)               %! SM6:EXPLICIT_TIME_SIGNATURE_COLOR:SM1
                            s1 * 1/2
                            \repeat volta 2
                            {
                <BLANKLINE>
                                % [GlobalSkips measure 2]                                                %! SM4
                                \time 3/8                                                                %! SM8:EXPLICIT_TIME_SIGNATURE:SM1
                                \once \override Score.TimeSignature.color = #(x11-color 'blue)           %! SM6:EXPLICIT_TIME_SIGNATURE_COLOR:SM1
                                s1 * 3/8
                <BLANKLINE>
                                % [GlobalSkips measure 3]                                                %! SM4
                                \time 4/8                                                                %! SM8:EXPLICIT_TIME_SIGNATURE:SM1
                                \once \override Score.TimeSignature.color = #(x11-color 'blue)           %! SM6:EXPLICIT_TIME_SIGNATURE_COLOR:SM1
                                s1 * 1/2
                            }
                <BLANKLINE>
                            % [GlobalSkips measure 4]                                                    %! SM4
                            \time 3/8                                                                    %! SM8:EXPLICIT_TIME_SIGNATURE:SM1
                            \once \override Score.TimeSignature.color = #(x11-color 'blue)               %! SM6:EXPLICIT_TIME_SIGNATURE_COLOR:SM1
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
                <BLANKLINE>
                                % [MusicVoice measure 1]                                                 %! SM4
                                e'8
                                [
                <BLANKLINE>
                                d''8
                <BLANKLINE>
                                f'8
                                ]
                <BLANKLINE>
                                r8
                <BLANKLINE>
                                % [MusicVoice measure 2]                                                 %! SM4
                                e''8
                                [
                <BLANKLINE>
                                g'8
                <BLANKLINE>
                                f''8
                                ]
                <BLANKLINE>
                                % [MusicVoice measure 3]                                                 %! SM4
                                r8
                <BLANKLINE>
                                e'8
                                [
                <BLANKLINE>
                                d''8
                <BLANKLINE>
                                f'8
                                ]
                <BLANKLINE>
                                % [MusicVoice measure 4]                                                 %! SM4
                                r8
                <BLANKLINE>
                                e''8
                                [
                <BLANKLINE>
                                g'8
                                ]
                <BLANKLINE>
                            }
                        }
                    >>
                >>

        ..  container:: example

            Wraps stage 2 global skips in volta container:

            >>> maker = baca.SegmentMaker(
            ...     measures_per_stage=[1, 2, 1],
            ...     score_template=baca.SingleStaffScoreTemplate(),
            ...     time_signatures=[(4, 8), (3, 8), (4, 8), (3, 8)],
            ...     )

            >>> maker(
            ...     ('MusicVoice', (1, 3)),
            ...     baca.pitches('E4 D5 F4 E5 G4 F5'),
            ...     baca.RhythmCommand(
            ...         rhythm_maker=rmakers.TaleaRhythmMaker(
            ...             talea=rmakers.Talea(
            ...                 counts=[1, 1, 1, -1],
            ...                 denominator=8,
            ...                 ),
            ...             ),
            ...         ),
            ...     )

            >>> maker(
            ...     ('GlobalSkips', 2),
            ...     baca.volta(),
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
                            \time 4/8                                                                    %! SM8:EXPLICIT_TIME_SIGNATURE:SM1
                            \once \override Score.TimeSignature.color = #(x11-color 'blue)               %! SM6:EXPLICIT_TIME_SIGNATURE_COLOR:SM1
                            s1 * 1/2
                            \repeat volta 2
                            {
                <BLANKLINE>
                                % [GlobalSkips measure 2]                                                %! SM4
                                \time 3/8                                                                %! SM8:EXPLICIT_TIME_SIGNATURE:SM1
                                \once \override Score.TimeSignature.color = #(x11-color 'blue)           %! SM6:EXPLICIT_TIME_SIGNATURE_COLOR:SM1
                                s1 * 3/8
                <BLANKLINE>
                                % [GlobalSkips measure 3]                                                %! SM4
                                \time 4/8                                                                %! SM8:EXPLICIT_TIME_SIGNATURE:SM1
                                \once \override Score.TimeSignature.color = #(x11-color 'blue)           %! SM6:EXPLICIT_TIME_SIGNATURE_COLOR:SM1
                                s1 * 1/2
                            }
                <BLANKLINE>
                            % [GlobalSkips measure 4]                                                    %! SM4
                            \time 3/8                                                                    %! SM8:EXPLICIT_TIME_SIGNATURE:SM1
                            \once \override Score.TimeSignature.color = #(x11-color 'blue)               %! SM6:EXPLICIT_TIME_SIGNATURE_COLOR:SM1
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
                <BLANKLINE>
                                % [MusicVoice measure 1]                                                 %! SM4
                                e'8
                                [
                <BLANKLINE>
                                d''8
                <BLANKLINE>
                                f'8
                                ]
                <BLANKLINE>
                                r8
                <BLANKLINE>
                                % [MusicVoice measure 2]                                                 %! SM4
                                e''8
                                [
                <BLANKLINE>
                                g'8
                <BLANKLINE>
                                f''8
                                ]
                <BLANKLINE>
                                % [MusicVoice measure 3]                                                 %! SM4
                                r8
                <BLANKLINE>
                                e'8
                                [
                <BLANKLINE>
                                d''8
                <BLANKLINE>
                                f'8
                                ]
                <BLANKLINE>
                                % [MusicVoice measure 4]                                                 %! SM4
                                r8
                <BLANKLINE>
                                e''8
                                [
                <BLANKLINE>
                                g'8
                                ]
                <BLANKLINE>
                            }
                        }
                    >>
                >>

        """
        return VoltaCommand(selector=selector)
