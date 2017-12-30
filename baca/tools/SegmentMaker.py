import abjad
import baca
import os
import pathlib
import time
import traceback
from abjad import rhythmmakertools as rhythmos


class SegmentMaker(abjad.SegmentMaker):
    r'''Segment-maker.

    >>> from abjad import rhythmmakertools as rhythmos

    ..  container:: example

        >>> maker = baca.SegmentMaker(
        ...     ignore_unpitched_notes=True,
        ...     score_template=baca.SingleStaffScoreTemplate(),
        ...     time_signatures=[(4, 8), (3, 8), (4, 8), (3, 8)],
        ...     )

        >>> maker(
        ...     baca.scope('MusicVoice', 1),
        ...     baca.make_even_runs(),
        ...     )

        >>> lilypond_file = maker.run(
        ...     environment='docs',
        ...     remove=[baca.Tags.STAGE_NUMBER_MARKUP],
        ...     )
        >>> abjad.show(lilypond_file, strict=89) # doctest: +SKIP

        ..  docs::

            >>> abjad.f(lilypond_file[abjad.Score], strict=89)
            \context Score = "Score" <<
                \context GlobalContext = "GlobalContext" <<
                    \context GlobalSkips = "GlobalSkips" {
            <BLANKLINE>
                        % GlobalSkips [measure 1]                                                    %! SM4
                        \time 4/8                                                                    %! EXPLICIT_TIME_SIGNATURE:SM8
                        \bar ""                                                                      %! EMPTY_START_BAR:SM2
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
                                c'8
                                [
            <BLANKLINE>
                                c'8
            <BLANKLINE>
                                c'8
            <BLANKLINE>
                                c'8
                                ]
                            }
                            {
            <BLANKLINE>
                                % MusicVoice [measure 2]                                             %! SM4
                                c'8
                                [
            <BLANKLINE>
                                c'8
            <BLANKLINE>
                                c'8
                                ]
                            }
                            {
            <BLANKLINE>
                                % MusicVoice [measure 3]                                             %! SM4
                                c'8
                                [
            <BLANKLINE>
                                c'8
            <BLANKLINE>
                                c'8
            <BLANKLINE>
                                c'8
                                ]
                            }
                            {
            <BLANKLINE>
                                % MusicVoice [measure 4]                                             %! SM4
                                c'8
                                [
            <BLANKLINE>
                                c'8
            <BLANKLINE>
                                c'8
                                ]
            <BLANKLINE>
                            }
                        }
                    }
                >>
            >>

    '''

    ### CLASS ATTRIBUTES ###

    __documentation_section__ = '(2) Makers'

    __slots__ = (
        '_allow_empty_selections',
        '_break_offsets',
        '_builds_metadata',
        '_cache',
        '_cached_time_signatures',
        '_color_octaves',
        '_color_out_of_range_pitches',
        '_color_repeat_pitch_classes',
        '_design_checker',
        '_duration',
        '_environment',
        '_fermata_measure_staff_line_count',
        '_fermata_start_offsets',
        '_final_bar_line',
        '_final_markup',
        '_final_markup_extra_offset',
        '_ignore_repeat_pitch_classes',
        '_ignore_unpitched_notes',
        '_ignore_unregistered_pitches',
        '_instruments',
        '_last_segment',
        '_layout_measure_map',
        '_margin_markup',
        '_measures_per_stage',
        '_metronome_mark_measure_map',
        '_metronome_marks',
        '_midi',
        '_omit_empty_start_bar',
        '_omit_stage_number_markup',
        '_print_segment_duration',
        '_print_timings',
        '_range_checker',
        '_rehearsal_letter',
        '_score',
        '_score_template',
        '_segment_duration',
        '_skip_wellformedness_checks',
        '_skips_instead_of_rests',
        '_spacing_specifier',
        '_stage_label_base_string',
        '_start_clock_time',
        '_stop_clock_time',
        '_time_signatures',
        '_transpose_score',
        '_wrappers',
        )

    _absolute_string_trio_stylesheet_path = pathlib.Path(
        '/',
        'Users',
        'trevorbaca',
        'Scores',
        '_docs',
        'source',
        '_stylesheets',
        'string-trio-stylesheet.ily',
        )

    _absolute_two_voice_staff_stylesheet_path = pathlib.Path(
        '/',
        'Users',
        'trevorbaca',
        'Scores',
        '_docs',
        'source',
        '_stylesheets',
        'two-voice-staff-stylesheet.ily',
        )

    _prototype_to_manifest_name = {
        'abjad.Instrument': 'instruments',
        'abjad.MetronomeMark': 'metronome_marks',
        'baca.MarginMarkup': 'margin_markup',
        }

    _extend_beam_tag = 'extend beam'

    _publish_storage_format = True

    _status_to_color = {
        'default': 'DarkViolet',
        'explicit': 'blue',
        'reapplied': 'green4',
        'redundant': 'DeepPink1',
        }

    _status_to_redraw_color = {
        'default': 'violet',
        'explicit': 'DeepSkyBlue2',
        'reapplied': 'OliveDrab',
        'redundant': 'DeepPink4',
        }

    _relative_string_trio_stylesheet_path = pathlib.Path(
        '..',
        '..',
        '..',
        '..',
        'source',
        '_stylesheets',
        'string-trio-stylesheet.ily',
        )

    _relative_two_voice_staff_stylesheet_path = pathlib.Path(
        '..',
        '..',
        '..',
        '..',
        'source',
        '_stylesheets',
        'two-voice-staff-stylesheet.ily',
        )

    _score_package_stylesheet_path = pathlib.Path(
        '..', '..', 'stylesheets', 'stylesheet.ily',
        )

    _score_package_nonfirst_stylesheet_path = pathlib.Path(
        '..', '..', 'stylesheets', 'nonfirst-segment.ily',
        )

    ### INITIALIZER ###

    def __init__(
        self,
        allow_empty_selections=None,
        color_octaves=None,
        color_out_of_range_pitches=None,
        color_repeat_pitch_classes=None,
        design_checker=None,
        fermata_measure_staff_line_count=None,
        final_bar_line=None,
        final_markup=None,
        final_markup_extra_offset=None,
        ignore_repeat_pitch_classes=None,
        ignore_unpitched_notes=None,
        ignore_unregistered_pitches=None,
        instruments=None,
        last_segment=None,
        layout_measure_map=None,
        margin_markup=None,
        measures_per_stage=None,
        metronome_mark_measure_map=None,
        metronome_marks=None,
        omit_empty_start_bar=None,
        omit_stage_number_markup=None,
        print_segment_duration=None,
        print_timings=None,
        range_checker=None,
        rehearsal_letter=None,
        score_template=None,
        skip_wellformedness_checks=None,
        skips_instead_of_rests=None,
        spacing_specifier=None,
        stage_label_base_string=None,
        time_signatures=None,
        transpose_score=None,
        ):
        super(SegmentMaker, self).__init__()
        if allow_empty_selections is not None:
            allow_empty_selections = bool(allow_empty_selections)
        self._allow_empty_selections = allow_empty_selections
        self._break_offsets = []
        if color_octaves is not None:
            color_octaves = bool(color_octaves)
        self._color_octaves = color_octaves
        if color_out_of_range_pitches is not None:
            color_out_of_range_pitches = bool(color_out_of_range_pitches)
        self._color_out_of_range_pitches = color_out_of_range_pitches
        if color_repeat_pitch_classes is not None:
            color_repeat_pitch_classes = bool(color_repeat_pitch_classes)
        self._color_repeat_pitch_classes = color_repeat_pitch_classes
        self._cache = None
        self._cached_time_signatures = []
        self._design_checker = design_checker
        self._duration = None
        if fermata_measure_staff_line_count is not None:
            assert isinstance(fermata_measure_staff_line_count, int)
            assert 0 <= fermata_measure_staff_line_count
        self._fermata_measure_staff_line_count = \
            fermata_measure_staff_line_count
        self._fermata_start_offsets = []
        if final_bar_line not in (None, False, abjad.Exact):
            assert isinstance(final_bar_line, str), repr(final_bar_line)
        self._final_bar_line = final_bar_line
        if final_markup is not None:
            assert isinstance(final_markup, (tuple, list))
        self._final_markup = final_markup
        if final_markup_extra_offset is not None:
            assert isinstance(final_markup_extra_offset, tuple)
        self._final_markup_extra_offset = final_markup_extra_offset
        if ignore_repeat_pitch_classes is not None:
            ignore_repeat_pitch_classes = bool(
                ignore_repeat_pitch_classes)
        self._ignore_repeat_pitch_classes = ignore_repeat_pitch_classes
        if ignore_unpitched_notes is not None:
            ignore_unpitched_notes = bool(ignore_unpitched_notes)
        self._ignore_unpitched_notes = ignore_unpitched_notes
        if ignore_unregistered_pitches is not None:
            ignore_unregistered_pitches = bool(ignore_unregistered_pitches)
        self._ignore_unregistered_pitches = ignore_unregistered_pitches
        if instruments is not None:
            assert isinstance(instruments, abjad.TypedOrderedDict)
        self._instruments = instruments
        if last_segment is not None:
            last_segment = bool(last_segment)
        self._last_segment = last_segment
        if layout_measure_map is not None:
            assert isinstance(layout_measure_map, baca.LayoutMeasureMap)
        self._layout_measure_map = layout_measure_map
        if margin_markup is not None:
            assert isinstance(margin_markup, abjad.TypedOrderedDict)
        self._margin_markup = margin_markup
        self._measures_per_stage = measures_per_stage
        self._metronome_mark_measure_map = metronome_mark_measure_map
        if metronome_marks is not None:
            assert isinstance(metronome_marks, abjad.TypedOrderedDict)
        self._metronome_marks = metronome_marks
        self._midi = None
        if omit_empty_start_bar is not None:
            omit_empty_start_bar = bool(omit_empty_start_bar)
        self._omit_empty_start_bar = omit_empty_start_bar
        if omit_stage_number_markup is not None:
            omit_stage_number_markup = bool(omit_stage_number_markup)
        self._omit_stage_number_markup = omit_stage_number_markup
        self._print_segment_duration = print_segment_duration
        self._print_timings = print_timings
        self._range_checker = range_checker
        self._rehearsal_letter = rehearsal_letter
        self._initialize_time_signatures(time_signatures)
        if score_template is not None:
            assert isinstance(score_template, baca.ScoreTemplate)
        self._score_template = score_template
        self._segment_duration = None
        if skip_wellformedness_checks is not None:
            skip_wellformedness_checks = bool(skip_wellformedness_checks)
        self._skip_wellformedness_checks = skip_wellformedness_checks
        if skips_instead_of_rests is not None:
            skips_instead_of_rests = bool(skips_instead_of_rests)
        self._skips_instead_of_rests = skips_instead_of_rests
        if spacing_specifier is not None:
            assert isinstance(spacing_specifier, baca.HorizontalSpacingSpecifier)
        self._spacing_specifier = spacing_specifier
        if stage_label_base_string is not None:
            assert isinstance(stage_label_base_string, str)
        self._stage_label_base_string = stage_label_base_string
        self._start_clock_time = None
        self._stop_clock_time = None
        if transpose_score is not None:
            transpose_score = bool(transpose_score)
        self._transpose_score = transpose_score
        self._wrappers = []

    ### SPECIAL METHODS ###

    def __call__(self, scopes, *commands):
        r'''Wraps each command in `commands` with each scope in `scopes`.

        ..  container:: example

            >>> maker = baca.SegmentMaker(
            ...     score_template=baca.SingleStaffScoreTemplate(),
            ...     time_signatures=[(4, 8), (3, 8), (4, 8), (3, 8)],
            ...     )

            >>> maker(
            ...     baca.scope('MusicVoice', 1),
            ...     baca.make_even_runs(),
            ...     baca.label(abjad.label().with_indices()),
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
                            \bar ""                                                                      %! EMPTY_START_BAR:SM2
                            \once \override Score.TimeSignature.color = #(x11-color 'blue)               %! EXPLICIT_TIME_SIGNATURE_COLOR:SM6
                            s1 * 1/2
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
                                    \once \override Accidental.color = #blue                             %! SM24
                                    \once \override Beam.color = #blue                                   %! SM24
                                    \once \override Dots.color = #blue                                   %! SM24
                                    \once \override Flag.color = #blue                                   %! SM24
                                    \once \override NoteHead.color = #blue                               %! SM24
                                    \once \override Stem.color = #blue                                   %! SM24
                                    c'8
                                    [
                                    ^ \markup {
                                        \small
                                            0
                                        }
                <BLANKLINE>
                                    \once \override Accidental.color = #blue                             %! SM24
                                    \once \override Beam.color = #blue                                   %! SM24
                                    \once \override Dots.color = #blue                                   %! SM24
                                    \once \override Flag.color = #blue                                   %! SM24
                                    \once \override NoteHead.color = #blue                               %! SM24
                                    \once \override Stem.color = #blue                                   %! SM24
                                    c'8
                                    ^ \markup {
                                        \small
                                            1
                                        }
                <BLANKLINE>
                                    \once \override Accidental.color = #blue                             %! SM24
                                    \once \override Beam.color = #blue                                   %! SM24
                                    \once \override Dots.color = #blue                                   %! SM24
                                    \once \override Flag.color = #blue                                   %! SM24
                                    \once \override NoteHead.color = #blue                               %! SM24
                                    \once \override Stem.color = #blue                                   %! SM24
                                    c'8
                                    ^ \markup {
                                        \small
                                            2
                                        }
                <BLANKLINE>
                                    \once \override Accidental.color = #blue                             %! SM24
                                    \once \override Beam.color = #blue                                   %! SM24
                                    \once \override Dots.color = #blue                                   %! SM24
                                    \once \override Flag.color = #blue                                   %! SM24
                                    \once \override NoteHead.color = #blue                               %! SM24
                                    \once \override Stem.color = #blue                                   %! SM24
                                    c'8
                                    ]
                                    ^ \markup {
                                        \small
                                            3
                                        }
                                }
                                {
                <BLANKLINE>
                                    % MusicVoice [measure 2]                                             %! SM4
                                    \once \override Accidental.color = #blue                             %! SM24
                                    \once \override Beam.color = #blue                                   %! SM24
                                    \once \override Dots.color = #blue                                   %! SM24
                                    \once \override Flag.color = #blue                                   %! SM24
                                    \once \override NoteHead.color = #blue                               %! SM24
                                    \once \override Stem.color = #blue                                   %! SM24
                                    c'8
                                    [
                                    ^ \markup {
                                        \small
                                            4
                                        }
                <BLANKLINE>
                                    \once \override Accidental.color = #blue                             %! SM24
                                    \once \override Beam.color = #blue                                   %! SM24
                                    \once \override Dots.color = #blue                                   %! SM24
                                    \once \override Flag.color = #blue                                   %! SM24
                                    \once \override NoteHead.color = #blue                               %! SM24
                                    \once \override Stem.color = #blue                                   %! SM24
                                    c'8
                                    ^ \markup {
                                        \small
                                            5
                                        }
                <BLANKLINE>
                                    \once \override Accidental.color = #blue                             %! SM24
                                    \once \override Beam.color = #blue                                   %! SM24
                                    \once \override Dots.color = #blue                                   %! SM24
                                    \once \override Flag.color = #blue                                   %! SM24
                                    \once \override NoteHead.color = #blue                               %! SM24
                                    \once \override Stem.color = #blue                                   %! SM24
                                    c'8
                                    ]
                                    ^ \markup {
                                        \small
                                            6
                                        }
                                }
                                {
                <BLANKLINE>
                                    % MusicVoice [measure 3]                                             %! SM4
                                    \once \override Accidental.color = #blue                             %! SM24
                                    \once \override Beam.color = #blue                                   %! SM24
                                    \once \override Dots.color = #blue                                   %! SM24
                                    \once \override Flag.color = #blue                                   %! SM24
                                    \once \override NoteHead.color = #blue                               %! SM24
                                    \once \override Stem.color = #blue                                   %! SM24
                                    c'8
                                    [
                                    ^ \markup {
                                        \small
                                            7
                                        }
                <BLANKLINE>
                                    \once \override Accidental.color = #blue                             %! SM24
                                    \once \override Beam.color = #blue                                   %! SM24
                                    \once \override Dots.color = #blue                                   %! SM24
                                    \once \override Flag.color = #blue                                   %! SM24
                                    \once \override NoteHead.color = #blue                               %! SM24
                                    \once \override Stem.color = #blue                                   %! SM24
                                    c'8
                                    ^ \markup {
                                        \small
                                            8
                                        }
                <BLANKLINE>
                                    \once \override Accidental.color = #blue                             %! SM24
                                    \once \override Beam.color = #blue                                   %! SM24
                                    \once \override Dots.color = #blue                                   %! SM24
                                    \once \override Flag.color = #blue                                   %! SM24
                                    \once \override NoteHead.color = #blue                               %! SM24
                                    \once \override Stem.color = #blue                                   %! SM24
                                    c'8
                                    ^ \markup {
                                        \small
                                            9
                                        }
                <BLANKLINE>
                                    \once \override Accidental.color = #blue                             %! SM24
                                    \once \override Beam.color = #blue                                   %! SM24
                                    \once \override Dots.color = #blue                                   %! SM24
                                    \once \override Flag.color = #blue                                   %! SM24
                                    \once \override NoteHead.color = #blue                               %! SM24
                                    \once \override Stem.color = #blue                                   %! SM24
                                    c'8
                                    ]
                                    ^ \markup {
                                        \small
                                            10
                                        }
                                }
                                {
                <BLANKLINE>
                                    % MusicVoice [measure 4]                                             %! SM4
                                    \once \override Accidental.color = #blue                             %! SM24
                                    \once \override Beam.color = #blue                                   %! SM24
                                    \once \override Dots.color = #blue                                   %! SM24
                                    \once \override Flag.color = #blue                                   %! SM24
                                    \once \override NoteHead.color = #blue                               %! SM24
                                    \once \override Stem.color = #blue                                   %! SM24
                                    c'8
                                    [
                                    ^ \markup {
                                        \small
                                            11
                                        }
                <BLANKLINE>
                                    \once \override Accidental.color = #blue                             %! SM24
                                    \once \override Beam.color = #blue                                   %! SM24
                                    \once \override Dots.color = #blue                                   %! SM24
                                    \once \override Flag.color = #blue                                   %! SM24
                                    \once \override NoteHead.color = #blue                               %! SM24
                                    \once \override Stem.color = #blue                                   %! SM24
                                    c'8
                                    ^ \markup {
                                        \small
                                            12
                                        }
                <BLANKLINE>
                                    \once \override Accidental.color = #blue                             %! SM24
                                    \once \override Beam.color = #blue                                   %! SM24
                                    \once \override Dots.color = #blue                                   %! SM24
                                    \once \override Flag.color = #blue                                   %! SM24
                                    \once \override NoteHead.color = #blue                               %! SM24
                                    \once \override Stem.color = #blue                                   %! SM24
                                    c'8
                                    ]
                                    ^ \markup {
                                        \small
                                            13
                                        }
                <BLANKLINE>
                                }
                            }
                        }
                    >>
                >>

        Returns none.
        '''
        prototype = (baca.Scope, baca.TimelineScope)
        if isinstance(scopes, prototype):
            scopes = [scopes]
        else:
            assert all(isinstance(_, prototype) for _ in scopes), repr(scopes)
        for command in commands:
            if not isinstance(command, baca.Command):
                raise Exception(f'commands only:\n\n{format(command)}')
        for scope in scopes:
            for command in commands:
                manifest = getattr(command, '_manifest', None)
                if manifest is not None:
                    manifest = getattr(self, manifest)
                    command._manifest = manifest
                wrapper = baca.CommandWrapper(command=command, scope=scope)
                self.wrappers.append(wrapper)

    ### PRIVATE METHODS ###

    def _add_final_bar_line(self):
        if self.final_bar_line is False:
            return
        strings = []
        abbreviation = '|'
        if self.last_segment:
            abbreviation = '|.'
        if isinstance(self.final_bar_line, str):
            abbreviation = self.final_bar_line
        strings.append(r'\override Score.BarLine.transparent = ##f')
        strings.append(rf'\bar "{abbreviation}"')
        literal = abjad.LilyPondLiteral(strings, 'after')
        last_skip = baca.select(self.score['GlobalSkips']).skip(-1)
        abjad.attach(literal, last_skip, site='SM5')

    def _add_final_markup(self):
        if self.final_markup is None:
            return
        command = baca.markup.final_markup(*self.final_markup)
        self.score.add_final_markup(
            command.indicators[0],
            extra_offset=self.final_markup_extra_offset,
            )

    def _analyze_momento(self, context, momento):
        previous_indicator = self._momento_to_indicator(momento)
        if previous_indicator is None:
            return
        momento_context = self.score[momento.context]
        leaf = abjad.inspect(momento_context).get_leaf(0)
        if isinstance(previous_indicator, abjad.Instrument):
            prototype = abjad.Instrument
        else:
            prototype = type(previous_indicator)
        indicator = abjad.inspect(leaf).get_indicator(prototype)
        status = None
        if indicator is None:
            status = 'reapplied'
        elif previous_indicator == indicator:
            if isinstance(previous_indicator, abjad.TimeSignature):
                status = 'reapplied'
            elif isinstance(previous_indicator, abjad.Dynamic):
                pass
            else:
                status = 'redundant'
        return leaf, previous_indicator, status

    def _apply_fermata_measure_staff_line_count(self):
        if self.fermata_measure_staff_line_count is None:
            return
        if not self._fermata_start_offsets:
            return
        self._attach_fermata_measure_adjustments(self._break_offsets)
        for build_name, build_metadata in self._builds_metadata.items():
            break_measure_numbers = build_metadata.get('break_measures')
            break_measure_timespans = self._get_measure_timespans(
                break_measure_numbers)
            break_measure_stop_offsets = [
                _.stop_offset for _ in break_measure_timespans
                ]
            if break_measure_stop_offsets:
                self._attach_fermata_measure_adjustments(
                    break_measure_stop_offsets,
                    build_name,
                    )

    def _apply_first_and_last_ties(self, voice):
        dummy_tie = abjad.Tie()
        for current_leaf in abjad.iterate(voice).leaves():
            if not dummy_tie._attachment_test(current_leaf):
                continue
            if abjad.inspect(current_leaf).has_indicator('tie to me'):
                previous_leaf = abjad.inspect(current_leaf).get_leaf(-1)
                if dummy_tie._attachment_test(previous_leaf):
                    previous_logical_tie = abjad.inspect(
                        previous_leaf).get_logical_tie()
                    if current_leaf not in previous_logical_tie:
                        current_logical_tie = abjad.inspect(
                            current_leaf).get_logical_tie()
                        leaves = previous_logical_tie + current_logical_tie
                        abjad.detach(abjad.Tie, previous_leaf)
                        abjad.detach(abjad.Tie, current_leaf)
                        inspector = abjad.inspect(current_leaf)
                        string = 'use messiaen style ties'
                        repeat_ties = inspector.has_indicator(string)
                        tie = abjad.Tie(repeat_ties=repeat_ties)
                        abjad.attach(tie, leaves, site='SM16')
                abjad.detach('tie to me', current_leaf)
            if abjad.inspect(current_leaf).has_indicator('tie from me'):
                next_leaf = abjad.inspect(current_leaf).get_leaf(1)
                if dummy_tie._attachment_test(next_leaf):
                    current_logical_tie = abjad.inspect(
                        current_leaf).get_logical_tie()
                    if next_leaf not in current_logical_tie:
                        next_logical_tie = abjad.inspect(
                            next_leaf).get_logical_tie()
                        leaves = current_logical_tie + next_logical_tie
                        abjad.detach(abjad.Tie, current_leaf)
                        abjad.detach(abjad.Tie, next_leaf)
                        inspector = abjad.inspect(current_leaf)
                        string = 'use messiaen style ties'
                        repeat_ties = inspector.has_indicator(string)
                        tie = abjad.Tie(repeat_ties=repeat_ties)
                        abjad.attach(tie, leaves, site='SM17')
                abjad.detach('tie from me', current_leaf)

    def _apply_layout_measure_map(self):
        if self.layout_measure_map is None:
            return
        self.layout_measure_map(self.score['GlobalSkips'])

    def _apply_spacing_specifier(self):
        start_time = time.time()
        if self.spacing_specifier is None:
            return
        self.spacing_specifier(self)
        stop_time = time.time()
        total_time = int(stop_time - start_time)
        if self.print_timings:
            print(f'spacing specifier time {total_time} seconds ...')
        if os.getenv('TRAVIS'):
            return
        if 3 < total_time:
            raise Exception(f'spacing specifier time {total_time} seconds!')

    def _assert_nonoverlapping_rhythms(self, rhythms, voice):
        previous_stop_offset = 0
        for rhythm in rhythms:
            start_offset = rhythm.start_offset
            if start_offset < previous_stop_offset:
                raise Exception(f'{voice!r} has overlapping rhythms.')
            duration = abjad.inspect(rhythm.annotation).get_duration()
            stop_offset = start_offset + duration
            previous_stop_offset = stop_offset

    def _assert_valid_stage_number(self, stage_number):
        if not 1 <= stage_number <= self.stage_count:
            message = f'must be 1 <= x <= {self.stage_count}: {stage_number}.'
            raise Exception(message)

    def _attach_fermata_measure_adjustments(self, break_offsets, build=None):
        prototype = baca.StaffLines
        staff_lines = baca.StaffLines(self.fermata_measure_staff_line_count)
        breaks_already_treated = []
        for staff in abjad.iterate(self.score).components(abjad.Staff):
            for leaf in abjad.iterate(staff).leaves():
                start_offset = abjad.inspect(leaf).get_timespan().start_offset
                if start_offset not in self._fermata_start_offsets:
                    continue
                leaf_stop = abjad.inspect(leaf).get_timespan().stop_offset
                ends_at_break = leaf_stop in break_offsets
                before = abjad.inspect(leaf).get_effective(prototype)
                next_leaf = abjad.inspect(leaf).get_leaf(1)
                if next_leaf is not None:
                    after = abjad.inspect(next_leaf).get_effective(prototype)
                if before != staff_lines:
                    strings = []
                    if build is None:
                        strings_ = staff_lines._get_lilypond_format(
                            context=staff,
                            )
                        strings.extend(strings_)
                    if getattr(before, 'line_count', 5) == 5:
                        string = rf'\once \override {staff.name}.BarLine'
                        string += f".bar-extent = #'(-2 . 2)"
                        strings.append(string)
                    if strings:
                        literal = abjad.LilyPondLiteral(strings)
                        abjad.attach(literal, leaf, site='SM20')
                if next_leaf is not None and staff_lines != after:
                    strings = after._get_lilypond_format(context=staff)
                    literal = abjad.LilyPondLiteral(strings)
                    abjad.attach(literal, next_leaf, site='SM21')
                if ends_at_break and leaf_stop not in breaks_already_treated:
                    strings = []
                    if staff_lines.line_count == 0:
                        string = r'\override Score.BarLine.transparent = ##t'
                        string = r'\once ' + string
                        strings.append(string)
                        string = r'\override Score.SpanBar.transparent = ##t'
                        string = r'\once ' + string
                        strings.append(string)
                    elif staff_lines.line_count == 1:
                        string = "Score.BarLine.bar-extent = #'(-2 . 2)"
                        string = r'\once \override ' + string
                        strings.append(string)
                    if strings:
                        literal = abjad.LilyPondLiteral(strings, 'after')
                        tag = baca.Tags.FERMATA_BAR_LINE
                        tag = baca.Tags.build(tag, build)
                        abjad.attach(literal, leaf, site='SM22', tag=tag)
                    breaks_already_treated.append(leaf_stop)
                if (build is None and
                    next_leaf is None and
                    before != staff_lines):
                    before_line_count = getattr(before, 'line_count', 5)
                    before_staff_lines = baca.StaffLines(
                        line_count=before_line_count,
                        hide=True,
                        )
                    abjad.attach(
                        before_staff_lines,
                        leaf,
                        site='SM23',
                        synthetic_offset=1_000_000,
                        )

    def _attach_fermatas(self):
        if not self.metronome_mark_measure_map:
            del(self.score['GlobalRests'])
            return
        has_fermata = False
        for entry in self.metronome_mark_measure_map:
            if isinstance(entry[1], abjad.Fermata):
                has_fermata = True
        if not has_fermata:
            del(self.score['GlobalRests'])
            return
        context = self.score['GlobalRests']
        rests = self._make_multimeasure_rests()
        context.extend(rests)
        directive_prototype = (
            abjad.BreathMark,
            abjad.Fermata,
            )
        for stage_number, directive in self.metronome_mark_measure_map:
            if not isinstance(directive, directive_prototype):
                continue
            assert 0 < stage_number <= self.stage_count
            result = self._stage_number_to_measure_indices(stage_number)
            start_measure_index, stop_measure_index = result
            rest = context[start_measure_index]
            assert isinstance(rest, abjad.MultimeasureRest)
            fermata_y_offset = None
            if isinstance(directive, abjad.Fermata):
                if directive.command == 'shortfermata':
                    string = 'scripts.ushortfermata'
                    fermata_y_offset = -7
                elif directive.command == 'fermata':
                    string = 'scripts.ufermata'
                    fermata_y_offset = -7
                elif directive.command == 'longfermata':
                    string = 'scripts.ulongfermata'
                    fermata_y_offset = -7
                elif directive.command == 'verylongfermata':
                    string = 'scripts.uverylongfermata'
                    fermata_y_offset = -7
                else:
                    raise Exception(f'unknown fermata: {directive.command!r}.')
                directive = abjad.Markup.musicglyph(string)
                directive = abjad.new(directive, direction=abjad.Up)
            else:
                directive = abjad.new(directive)
            abjad.attach(directive, rest, site='SM18')
            strings = []
            if fermata_y_offset is not None:
                string = r'\once \override MultiMeasureRestText.extra-offset'
                string += f" = #'(0 . {fermata_y_offset})"
                strings.append(string)
            string = r'\once \override'
            string += ' Score.MultiMeasureRest.transparent = ##t'
            strings.append(string)
            string = r'\once \override Score.TimeSignature.stencil = ##f'
            strings.append(string)
            literal = abjad.LilyPondLiteral(strings)
            abjad.attach(literal, rest, site='SM19')
            abjad.attach('fermata measure', rest, site='')
            start_offset = abjad.inspect(rest).get_timespan().start_offset
            self._fermata_start_offsets.append(start_offset)

    def _attach_score_template_defaults(self):
        if not self.first_segment:
            return
        pairs = self.score_template.attach_defaults(self.score)
        for leaf, indicator in pairs:
            wrapper = abjad.inspect(leaf).wrapper(indicator)
            assert wrapper is not None
            assert getattr(wrapper.indicator, 'persistent', False)
            context = wrapper._find_correct_effective_context()
            self._categorize_persistent_indicator(
                self.manifests,
                context,
                leaf, 
                wrapper.indicator,
                'default',
                )

    @staticmethod
    def _attach_latent_indicator_alert(leaf, indicator, status, manifests):
        assert indicator.latent, repr(indicator)
        if isinstance(indicator, abjad.Clef):
            return
        key = SegmentMaker._indicator_to_key(indicator, manifests)
        if key is not None:
            key = f'“{key}”'
        else:
            key = type(indicator).__name__
        if isinstance(indicator, abjad.Instrument):
            left, right = '(', ')'
        elif isinstance(indicator, baca.MarginMarkup):
            left, right = '[', ']'
        else:
            raise TypeError(indicator)
        if getattr(indicator, 'hide', False):
            markup = abjad.Markup.from_literal(f'{left}{key}{right}')
        else:
            items = [abjad.Markup.from_literal(f'{left}{key}').vcenter()]
            items.append(indicator.markup.vcenter())
            item = indicator.short_markup.vcenter()
            item = abjad.Markup.concat([item, abjad.Markup(right).vcenter()])
            items.append(item)
            markup = abjad.Markup(items)
        markup = abjad.new(markup, direction=abjad.Up)
        stem = SegmentMaker._indicator_to_stem(indicator)
        tag = f'{status.upper()}_{stem}_ALERT'
        tag = getattr(baca.Tags, tag)
        abjad.attach(markup, leaf, deactivate=True, site='SM10', tag=tag)
        color = SegmentMaker._status_to_color[status]
        color = abjad.SchemeColor(color)
        markup = markup.with_color(color)
        tag = f'{status.upper()}_{stem}_ALERT_WITH_COLOR'
        tag = getattr(baca.Tags, tag)
        abjad.attach(markup, leaf, site='SM11', tag=tag)

    def _attach_metronome_marks(self):
        skips = baca.select(self.score['GlobalSkips']).skips()
        left_broken_text = abjad.Markup().null()
        left_broken_text = abjad.new(left_broken_text, direction=None)
        spanner = abjad.MetronomeMarkSpanner(
            left_broken_padding=0,
            left_broken_text=left_broken_text,
            start_with_parenthesized_metronome_mark=False,
            )
        abjad.attach(spanner, skips, site='')
        if not self.metronome_mark_measure_map:
            return
        for stage_number, directive in self.metronome_mark_measure_map:
            self._assert_valid_stage_number(stage_number)
            start, _ = self._stage_number_to_measure_indices(stage_number)
            skip = skips[start]
            spanner.attach(directive, skip)

    @staticmethod
    def _categorize_persistent_indicator(
        manifests,
        context,
        leaf,
        indicator,
        status,
        spanner=None,
        ):
        assert isinstance(context, abjad.Context), repr(context)
        if status is None:
            return
        SegmentMaker._color_persistent_indicator(
            context,
            leaf,
            indicator,
            status,
            )
        if getattr(indicator, 'latent', False):
            SegmentMaker._attach_latent_indicator_alert(
                leaf,
                indicator,
                status,
                manifests,
                )
        elif (getattr(indicator, 'redraw', False)
            and not getattr(indicator, 'hide', False)):
            SegmentMaker._color_persistent_indicator(
                context,
                leaf,
                indicator,
                status,
                uncolor=True,
                )
        if isinstance(indicator, abjad.Clef):
            string = rf'\set {context.headword}.forceClef = ##t'
            literal = abjad.LilyPondLiteral(string)
            SegmentMaker._tag_persistent_indicator(
                context,
                leaf,
                literal,
                status,
                stem='CLEF',
                )
        abjad.detach(indicator, leaf)
        SegmentMaker._tag_persistent_indicator(
            context,
            leaf,
            indicator,
            status,
            spanner=spanner,
            )
        if (getattr(indicator, 'redraw', False)
            and not getattr(indicator, 'hide', False)):
            SegmentMaker._color_persistent_indicator(
                context,
                leaf,
                indicator,
                status,
                redraw=True,
                )
            if isinstance(indicator, (abjad.Instrument, baca.MarginMarkup)):
                strings = indicator._get_lilypond_format(context=context)
                literal = abjad.LilyPondLiteral(strings, 'after')
                stem = SegmentMaker._indicator_to_stem(indicator)
                SegmentMaker._tag_persistent_indicator(
                    context,
                    leaf,
                    literal,
                    status,
                    redraw=True,
                    stem=stem,
                    )

    def _attach_rehearsal_mark(self):
        if self.rehearsal_letter == '':
            return
        letter_number = None
        if self.rehearsal_letter is None:
            segment_number = self._get_segment_number()
            letter_number = segment_number - 1
        elif isinstance(self.rehearsal_letter, str):
            assert len(self.rehearsal_letter) == 1
            rehearsal_letter = self.rehearsal_letter.upper()
            letter_number = ord(rehearsal_letter) - ord('A') + 1
        if letter_number == 0:
            return
        rehearsal_mark = abjad.RehearsalMark(
            number=letter_number
            )
        skip = baca.select(self.score['GlobalSkips']).skip(0)
        abjad.attach(rehearsal_mark, skip, site='SM9')

    def _cache_break_offsets(self):
        prototype = abjad.LilyPondLiteral
        for skip in baca.select(self.score['GlobalSkips']).skips():
            literals = abjad.inspect(skip).get_indicators(prototype)
            if not literals:
                continue
            if not any(
                _.argument in (r'\break', r'\pageBreak') for _ in literals
                ):
                continue
            offset = abjad.inspect(skip).get_timespan().start_offset
            self._break_offsets.append(offset)
        segment_stop_offset = abjad.inspect(skip).get_timespan().stop_offset
        self._break_offsets.append(segment_stop_offset)

    def _cache_leaves(self):
        stage_timespans = []
        for stage_index in range(self.stage_count):
            stage_number = stage_index + 1
            stage_offsets = self._get_stage_offsets(stage_number, stage_number)
            stage_timespan = abjad.Timespan(*stage_offsets)
            stage_timespans.append(stage_timespan)
        self._cache = abjad.TypedOrderedDict()
        contexts = [self.score['GlobalSkips']]
        contexts.extend(abjad.select(self.score).components(abjad.Voice))
        for context in contexts:
            leaves_by_stage_number = abjad.TypedOrderedDict()
            self._cache[context.name] = leaves_by_stage_number
            for stage_index in range(self.stage_count):
                stage_number = stage_index + 1
                leaves_by_stage_number[stage_number] = []
            for leaf in abjad.iterate(context).leaves():
                leaf_timespan = abjad.inspect(leaf).get_timespan()
                for stage_index, stage_timespan in enumerate(stage_timespans):
                    stage_number = stage_index + 1
                    if leaf_timespan.starts_during_timespan(stage_timespan):
                        leaves_by_stage_number[stage_number].append(leaf)

    def _call_commands(self):
        start_time = time.time()
        for wrapper in self.wrappers:
            assert isinstance(wrapper, baca.CommandWrapper)
            assert isinstance(wrapper.command, baca.Command)
            if isinstance(wrapper.command, baca.RhythmCommand):
                continue
            selection = self._scope_to_leaf_selection(wrapper)
            wrapper.command._manifests = self.manifests
            try:
                wrapper.command(selection)
            except:
                traceback.print_exc()
                raise Exception(f'can not interpret ...\n\n{format(wrapper)}')
            self._handle_mutator(wrapper)
        stop_time = time.time()
        count = int(stop_time - start_time)
        counter = abjad.String('second').pluralize(count)
        if self.print_timings:
            print(f'command interpretation {count} {counter} ...')

    def _call_rhythm_commands(self):
        self._attach_metronome_marks()
        self._attach_fermatas()
        for voice in abjad.iterate(self.score).components(abjad.Voice):
            assert not len(voice), repr(voice)
            wrappers = self._voice_to_rhythm_wrappers(voice)
            if not wrappers:
                if self.skips_instead_of_rests:
                    maker = rhythmos.SkipRhythmMaker()
                else:
                    mask = abjad.silence([0], 1, use_multimeasure_rests=True)
                    maker = rhythmos.NoteRhythmMaker(division_masks=[mask])
                selections = maker(self.time_signatures)
                voice.extend(selections)
                continue
            rhythms = []
            for wrapper in wrappers:
                assert isinstance(wrapper, baca.CommandWrapper)
                if wrapper.scope.stages is None:
                    raise Exception(format(wrapper))
                result = self._get_stage_time_signatures(*wrapper.scope.stages)
                start_offset, time_signatures = result
                try:
                    rhythm = wrapper.command(start_offset, time_signatures)
                except:
                    raise Exception(format(wrapper))
                rhythms.append(rhythm)
            rhythms.sort()
            self._assert_nonoverlapping_rhythms(rhythms, voice.name)
            rhythms = self._intercalate_silences(rhythms)
            voice.extend(rhythms)
            self._apply_first_and_last_ties(voice)

    def _check_design(self):
        if self.design_checker is None:
            return
        return self.design_checker(self.score)

    def _check_range(self):
        if not self.range_checker:
            return
        if isinstance(self.range_checker, abjad.PitchRange):
            markup = abjad.Markup('*', direction=abjad.Up)
            abjad.tweak(markup).color = 'red'
            for voice in abjad.iterate(self.score).components(abjad.Voice):
                for leaf in abjad.iterate(voice).leaves(pitched=True):
                    if leaf not in self.range_checker:
                        if self.color_out_of_range_pitches:
                            abjad.label(leaf).color_leaves('red')
                            abjad.attach(markup, leaf, site='SM13')
                        else:
                            raise Exception(f'out of range: {leaf!r}.')
        else:
            raise NotImplementedError(self.range_checker)

    def _check_wellformedness(self):
        if self.skip_wellformedness_checks:
            return
        score = self._lilypond_file['Score']
        if (self.color_octaves or
            self.color_repeat_pitch_classes or
            self.ignore_repeat_pitch_classes):
            return
        manager = baca.WellformednessManager()
        if not manager.is_well_formed(score):
            message = manager.tabulate_wellformedness(score)
            raise Exception(message)

    def _collect_metadata(self):
        result = {}
        result['duration'] = self._duration
        result['first_measure_number'] = self._get_first_measure_number()
        result['persistent_indicators'] = self._collect_persistent_indicators()
        result['segment_number'] = self._get_segment_number()
        result['start_clock_time'] = self._start_clock_time
        result['stop_clock_time'] = self._stop_clock_time
        result['time_signatures'] = self._cached_time_signatures
        items = sorted(result.items())
        self._metadata = abjad.TypedOrderedDict(items)

    def _collect_persistent_indicators(self):
        result = abjad.TypedOrderedDict()
        contexts = abjad.iterate(self.score).components(abjad.Context)
        contexts = list(contexts)
        contexts.sort(key=lambda _: _.name)
        for context in contexts:
            momentos = []
            dictionary = context._get_persistent_wrappers()
            for wrapper in dictionary.values():
                leaf = wrapper.component
                parentage = abjad.inspect(leaf).get_parentage()
                first_context = parentage.get_first(abjad.Context)
                indicator = wrapper.indicator
                value = self._indicator_to_key(indicator, self.manifests)
                if isinstance(indicator.persistent, str):
                    prototype = indicator.persistent
                else:
                    prototype = type(indicator)
                    prototype = self._prototype_string(prototype)
                momento = abjad.Momento(
                    context=first_context.name,
                    prototype=prototype,
                    value=value,
                    )
                momentos.append(momento)
            if momentos:
                momentos.sort(key=lambda _: _.prototype)
                result[context.name] = momentos
        return result

    def _color_octaves_(self):
        if not self.color_octaves:
            return
        score = self.score
        vertical_moments = abjad.iterate(score).vertical_moments()
        markup = abjad.Markup('OCTAVE', direction=abjad.Up)
        abjad.tweak(markup).color = 'red'
        for vertical_moment in vertical_moments:
            pitches = []
            for leaf in vertical_moment.leaves:
                if isinstance(leaf, abjad.Note):
                    pitches.append(leaf.written_pitch)
                elif isinstance(leaf, abjad.Chord):
                    pitches.extend(leaf.written_pitches)
            if not pitches:
                continue
            pitch_classes = [_.pitch_class for _ in pitches]
            if baca.PitchClassSegment(pitch_classes).has_duplicates():
                notes_and_chords = vertical_moment.notes_and_chords
                notes_and_chords = abjad.select(notes_and_chords)
                abjad.label(notes_and_chords).color_leaves('red')
                for leaf in notes_and_chords:
                    abjad.attach(markup, leaf, site='SM12')

    @staticmethod
    def _color_persistent_indicator(
        #self,
        context,
        leaf,
        indicator,
        status,
        redraw=False,
        uncolor=False,
        ):
        if context is not None:
            assert isinstance(context, abjad.Context), repr(context)
        stem = SegmentMaker._indicator_to_stem(indicator)
        if stem == 'METRONOME_MARK':
            context = None
            markup = indicator._get_markup()
            color = SegmentMaker._status_to_color[status]
            color = abjad.SchemeColor(color)
            markup = markup.with_color(color)
            markup = abjad.new(markup, direction=abjad.Up)
            tag = f'{status.upper()}_{stem}_WITH_COLOR'
            tag = getattr(baca.Tags, tag)
            abjad.attach(markup, leaf, site='SM15', tag=tag)
            return
        grob = SegmentMaker._indicator_to_grob(indicator)
        if context is not None:
            string = rf'\override {context.headword}.{grob}.color ='
        else:
            string = rf'\override {grob}.color ='
        if uncolor is True:
            string += ' ##f'
        elif redraw is True:
            color = SegmentMaker._status_to_redraw_color[status]
            string += f" #(x11-color '{color})"
        else:
            string = rf'\once {string}'
            color = SegmentMaker._status_to_color[status]
            string += f" #(x11-color '{color})"
        if redraw:
            literal = abjad.LilyPondLiteral(string, 'after')
        else:
            literal = abjad.LilyPondLiteral(string)
        if getattr(indicator, 'latent', False):
            if redraw:
                prefix = 'redrawn'
            else:
                prefix = None
            if uncolor:
                suffix = 'color_cancellation'
            else:
                suffix = 'color'
        else:
            prefix = None
            if redraw:
                suffix = 'redraw_color'
            elif uncolor:
                suffix = 'color_cancellation'
            else:
                suffix = 'color'
        tag = SegmentMaker._get_tag(status, stem, prefix=prefix, suffix=suffix)
        if uncolor is True:
            abjad.attach(literal, leaf, deactivate=True, site='SM7', tag=tag)
        else:
            abjad.attach(literal, leaf, site='SM6', tag=tag)

    def _color_repeat_pitch_classes_(self):
        manager = baca.WellformednessManager
        lts = manager._find_repeat_pitch_classes(self.score)
        markup = abjad.Markup('@', direction=abjad.Up)
        abjad.tweak(markup).color = 'red'
        for lt in lts:
            abjad.label(lt).color_leaves('red')
            for leaf in lt:
                abjad.attach(markup, leaf, site='SM14')

    def _color_unpitched_notes(self):
        if self.ignore_unpitched_notes:
            return
        color = 'blue'
        for pleaf in abjad.iterate(self.score).leaves(pitched=True):
            if not abjad.inspect(pleaf).has_indicator('not yet pitched'):
                continue
            strings = [
                rf'\once \override Accidental.color = #{color}',
                rf'\once \override Beam.color = #{color}',
                rf'\once \override Dots.color = #{color}',
                rf'\once \override Flag.color = #{color}',
                rf'\once \override NoteHead.color = #{color}',
                rf'\once \override Stem.color = #{color}',
                ]
            literal = abjad.LilyPondLiteral(strings)
            abjad.attach(literal, pleaf, site='SM24')

    def _color_unregistered_pitches(self):
        if self.ignore_unregistered_pitches:
            return
        color = 'magenta'
        for pleaf in abjad.iterate(self.score).leaves(pitched=True):
            if not abjad.inspect(pleaf).has_indicator('not yet registered'):
                continue
            strings = [
                rf'\once \override Accidental.color = #{color}',
                rf'\once \override Beam.color = #{color}',
                rf'\once \override Dots.color = #{color}',
                rf'\once \override Flag.color = #{color}',
                rf'\once \override NoteHead.color = #{color}',
                rf'\once \override Stem.color = #{color}',
                ]
            literal = abjad.LilyPondLiteral(strings)
            abjad.attach(literal, pleaf, site='SM25')

    def _comment_measure_numbers(self):
        offset_to_measure_number = {}
        measure_number = self._get_first_measure_number()
        for skip in baca.select(self.score['GlobalSkips']).skips():
            offset = abjad.inspect(skip).get_timespan().start_offset
            offset_to_measure_number[offset] = measure_number
            measure_number += 1
        contexts = []
        contexts.extend(self.score['GlobalContext'])
        contexts.extend(abjad.iterate(self.score).components(abjad.Voice))
        for context in contexts:
            for leaf in abjad.iterate(context).leaves():
                offset = abjad.inspect(leaf).get_timespan().start_offset
                measure_number = offset_to_measure_number.get(offset, None)
                if measure_number is None:
                    continue
                string = f'% {context.name} [measure {measure_number}]'
                literal = abjad.LilyPondLiteral(string, 'absolute_before')
                abjad.attach(literal, leaf, site='SM4')

    def _deactivate_tags(self, tags):
        if not tags:
            return
        for leaf in abjad.iterate(self.score).leaves():
            for wrapper in abjad.inspect(leaf).wrappers():
                if wrapper.tag is None:
                    continue
                index = wrapper.tag.rfind(':')
                tag = wrapper.tag[:index]
                if tag in tags:
                    wrapper._deactivate = True

    @staticmethod
    def _extend_beam(leaf):
        beam = abjad.inspect(leaf).get_spanner(abjad.Beam)
        if beam is None:
            return
        all_leaves = []
        all_leaves.extend(beam.leaves)
        durations = []
        if hasattr(beam, 'durations'):
            durations.extend(beam.durations)
        else:
            duration = abjad.inspect(beam.leaves).get_duration()
            durations.append(duration)
        intervening_skips = []
        index = 1
        while True:
            next_leaf = abjad.inspect(leaf).get_leaf(index)
            if next_leaf is None:
                return
            index += 1
            if isinstance(next_leaf, abjad.Skip):
                beam = abjad.inspect(next_leaf).get_spanner(abjad.Beam)
                if beam is None:
                    intervening_skips.append(next_leaf)
                    continue
            break
        abjad.detach(abjad.Beam, leaf)
        all_leaves.extend(intervening_skips)
        if intervening_skips:
            intervening_skips = abjad.select(intervening_skips)
            duration = abjad.inspect(intervening_skips).get_duration()
            durations.append(duration)
        beam = abjad.inspect(next_leaf).get_spanner(abjad.Beam)
        if beam is None:
            all_leaves.append(next_leaf)
            duration = abjad.inspect(next_leaf).get_duration()
            durations.append(duration)
        else:
            all_leaves.extend(beam.leaves)
            if hasattr(beam, 'durations'):
                durations.extend(beam.durations)
            else:
                duration = abjad.inspect(beam.leaves).get_duration()
                durations.append(duration)
        abjad.detach(abjad.Beam, next_leaf)
        all_leaves = abjad.select(all_leaves)
        assert abjad.inspect(all_leaves).get_duration() == sum(durations)
        beam = abjad.DuratedComplexBeam(beam_rests=True, durations=durations)
        abjad.attach(beam, all_leaves, site='')

    def _extend_beams(self):
        for leaf in abjad.iterate(self.score).leaves():
            if abjad.inspect(leaf).get_indicator(self._extend_beam_tag):
                self._extend_beam(leaf)

    def _get_first_measure_number(self):
        if not self._previous_metadata:
            return 1
        string = 'first_measure_number'
        first_measure_number = self._previous_metadata.get(string)
        time_signatures = self._previous_metadata.get('time_signatures')
        if first_measure_number is None or time_signatures is None:
            return 1
        first_measure_number += len(time_signatures)
        return first_measure_number

    @staticmethod
    def _get_key(dictionary, value):
        if dictionary is not None:
            for key, value_ in dictionary.items():
                if value_ == value:
                    return key

    def _get_measure_timespans(self, measure_numbers):
        timespans = []
        first_measure_number = self._get_first_measure_number()
        measure_indices = [
            _ - first_measure_number - 1 for _ in measure_numbers
            ]
        skips = baca.select(self.score['GlobalSkips']).skips()
        for i, skip in enumerate(skips):
            if i in measure_indices:
                timespan = abjad.inspect(skip).get_timespan()
                timespans.append(timespan)
        return timespans

    def _get_persistent_indicator(self, context, prototype):
        assert isinstance(context, abjad.Context), repr(context)
        if not self._previous_metadata:
            return
        dictionary = self._previous_metadata.get('persistent_indicators')
        if not dictionary:
            return
        momentos = dictionary.get(context.name)
        if not momentos:
            return
        prototype_string = self._prototype_string(prototype)
        for momento in momentos:
            if momento.prototype == prototype_string:
                indicator = self._key_to_indicator(momento.value, prototype)
                return (indicator, momento.context)

    def _get_previous_stop_clock_time(self):
        if self._previous_metadata:
            return self._previous_metadata.get('stop_clock_time')

    def _get_rehearsal_letter(self):
        if self.rehearsal_letter:
            return self.rehearsal_letter
        segment_number = self._get_segment_number()
        if segment_number == 1:
            return ''
        segment_index = segment_number - 1
        rehearsal_ordinal = ord('A') - 1 + segment_index
        rehearsal_letter = chr(rehearsal_ordinal)
        return rehearsal_letter

    def _get_segment_identifier(self):
        segment_name = self._metadata.get('segment_name')
        if segment_name is not None:
            return segment_name
        segment_number = self._get_segment_number()
        return segment_number

    def _get_segment_number(self):
        if not self._previous_metadata:
            segment_number = 0
        else:
            segment_number = self._previous_metadata.get('segment_number')
            if segment_number is None:
                message = 'previous metadata missing segment number.'
                raise Exception(message)
        return segment_number + 1

    def _get_stage_offsets(self, start_stage, stop_stage):
        skips = baca.select(self.score['GlobalSkips']).skips()
        result = self._stage_number_to_measure_indices(start_stage)
        start_measure_index, stop_measure_index = result
        start_skip = skips[start_measure_index]
        assert isinstance(start_skip, abjad.Skip), start_skip
        start_offset = abjad.inspect(start_skip).get_timespan().start_offset
        result = self._stage_number_to_measure_indices(stop_stage)
        start_measure_index, stop_measure_index = result
        stop_skip = skips[stop_measure_index]
        assert isinstance(stop_skip, abjad.Skip), stop_skip
        stop_offset = abjad.inspect(stop_skip).get_timespan().stop_offset
        return start_offset, stop_offset

    def _get_stage_time_signatures(self, start_stage=None, stop_stage=None):
        assert len(self.time_signatures) == sum(self.measures_per_stage)
        stages = baca.Sequence(self.time_signatures).partition_by_counts(
            self.measures_per_stage,
            )
        start_index = start_stage - 1
        if stop_stage is None:
            time_signatures = stages[start_index]
        else:
            stop_index = stop_stage
            stages = stages[start_index:stop_index]
            time_signatures = baca.sequence(stages).flatten(depth=-1)
        pair = (start_stage, stop_stage)
        start_offset, stop_offset = self._get_stage_offsets(*pair)
        return start_offset, time_signatures

    def _get_stylesheets(self):
        if self._environment == 'docs':
            if abjad.inspect(self.score).get_indicator('two-voice'):
                return [self._relative_two_voice_staff_stylesheet_path]
            else:
                return [self._relative_string_trio_stylesheet_path]
        elif self._environment == 'external':
            if abjad.inspect(self.score).get_indicator('two-voice'):
                return [self._absolute_two_voice_staff_stylesheet_path]
            else:
                return [self._absolute_string_trio_stylesheet_path]
        includes = []
        includes.append(self._score_package_stylesheet_path)
        if 1 < self._get_segment_number():
            includes.append(self._score_package_nonfirst_stylesheet_path)
        return includes

    @staticmethod
    def _get_tag(status, stem, prefix=None, suffix=None):
        stem = abjad.String(stem).delimit_words()
        stem = '_'.join([_.upper() for _ in stem])
        if suffix is not None:
            name = f'{status.upper()}_{stem}_{suffix.upper()}'
        else:
            name = f'{status.upper()}_{stem}'
        if prefix is not None:
            name = f'{prefix.upper()}_{name}'
        tag = getattr(baca.Tags, name)
        return tag

    def _handle_mutator(self, command):
        if (hasattr(command.command, '_mutates_score') and
            command.command._mutates_score()):
            self._cache = None

    @staticmethod
    def _indicator_to_grob(indicator):
        if isinstance(indicator, abjad.Dynamic):
            return 'DynamicText'
        elif isinstance(indicator, abjad.Instrument):
            return 'InstrumentName'
        elif isinstance(indicator, abjad.MetronomeMark):
            return 'TextScript'
        elif isinstance(indicator, baca.MarginMarkup):
            return 'InstrumentName'
        elif isinstance(indicator, baca.StaffLines):
            return 'StaffSymbol'
        return type(indicator).__name__

    @staticmethod
    def _indicator_to_key(indicator, manifests):
        if isinstance(indicator, (abjad.Clef, abjad.Dynamic)):
            return indicator.name
        if isinstance(indicator, abjad.Instrument):
            return SegmentMaker._get_key(
                manifests['abjad.Instrument'],
                indicator,
                )
        elif isinstance(indicator, abjad.MetronomeMark):
            return SegmentMaker._get_key(
                manifests['abjad.MetronomeMark'],
                indicator,
                )
        elif isinstance(indicator, baca.MarginMarkup):
            return SegmentMaker._get_key(
                manifests['baca.MarginMarkup'],
                indicator,
                )
        elif isinstance(indicator, baca.StaffLines):
            return indicator.line_count
        return str(indicator)

    @staticmethod
    def _indicator_to_stem(indicator):
        if isinstance(indicator.persistent, str):
            stem = indicator.persistent
            stem = stem.lstrip('abjad.')
        else:
            stem = type(indicator).__name__
        stem = abjad.String(stem).delimit_words()
        stem = '_'.join([_.upper() for _ in stem])
        return stem

    def _initialize_time_signatures(self, time_signatures):
        time_signatures = time_signatures or ()
        time_signatures_ = list(time_signatures)
        time_signatures_ = []
        for time_signature in time_signatures:
            time_signature = abjad.TimeSignature(time_signature)
            time_signatures_.append(time_signature)
        time_signatures_ = tuple(time_signatures_)
        if not time_signatures_:
            time_signatures_ = None
        self._time_signatures = time_signatures_

    def _intercalate_silences(self, rhythms):
        result = []
        durations = [_.duration for _ in self.time_signatures]
        measure_start_offsets = abjad.mathtools.cumulative_sums(durations)
        segment_duration = measure_start_offsets[-1]
        self._segment_duration = segment_duration
        previous_stop_offset = abjad.Offset(0)
        for rhythm in rhythms:
            start_offset = rhythm.start_offset
            if start_offset < previous_stop_offset:
                raise Exception('overlapping offsets: {rhythm!r}.')
            if previous_stop_offset < start_offset:
                silences = self._make_measure_silences(
                    previous_stop_offset,
                    start_offset,
                    measure_start_offsets,
                    )
                result.extend(silences)
            result.extend(rhythm.annotation)
            duration = abjad.inspect(rhythm.annotation).get_duration()
            previous_stop_offset = start_offset + duration
        if previous_stop_offset < segment_duration:
            silences = self._make_measure_silences(
                previous_stop_offset,
                segment_duration,
                measure_start_offsets,
                )
            result.extend(silences)
        return result

    def _key_to_indicator(self, key, prototype):
        assert isinstance(key, (int, str)), repr(key)
        if key is None:
            return 
        if prototype in (abjad.Clef, abjad.Dynamic):
            indicator = prototype(key)
        elif prototype is abjad.Instrument:
            indicator = self.instruments.get(key)
        elif prototype is abjad.MetronomeMark:
            indicator = self.metronome_marks.get(key)
        elif prototype is abjad.TimeSignature:
            indicator = abjad.TimeSignature.from_string(key)
        elif prototype is baca.MarginMarkup:
            indicator = self.margin_markup.get(key)
        elif prototype is baca.StaffLines:
            indicator = baca.StaffLines(line_count=key)
        else:
            raise Exception(prototype)
        return indicator

    def _label_stage_numbers(self):
        if self.omit_stage_number_markup:
            return
        skips = baca.select(self.score['GlobalSkips']).skips()
        for stage_index in range(self.stage_count):
            stage_number = stage_index + 1
            result = self._stage_number_to_measure_indices(stage_number)
            start_measure_index, stop_measure_index = result
            base = self.stage_label_base_string
            base = base or self._get_rehearsal_letter()
            if base not in ('', None):
                string = f'[{base}.{stage_number}]'
            else:
                string = f'[{stage_number}]'
            markup = abjad.Markup(string)
            markup = markup.with_color(abjad.SchemeColor('DarkCyan'))
            markup = markup.fontsize(-3)
            markup = abjad.new(markup, direction=abjad.Up)
            skip = skips[start_measure_index]
            abjad.attach(
                markup,
                skip,
                site='SM3',
                tag=baca.Tags.STAGE_NUMBER_MARKUP,
                )

    def _make_global_skips(self):
        context = self.score['GlobalSkips']
        for time_signature in self.time_signatures:
            skip = abjad.Skip(1)
            multiplier = abjad.Multiplier(time_signature.duration)
            abjad.attach(multiplier, skip, site='')
            abjad.attach(time_signature, skip, context='Score', site='SM1')
            context.append(skip)
        # empty start bar allows LilyPond to print first bar number
        if self.omit_empty_start_bar:
            return
        first_skip = baca.select(context).skip(0)
        literal = abjad.LilyPondLiteral(r'\bar ""')
        abjad.attach(
            literal,
            first_skip,
            site='SM2',
            tag=baca.Tags.EMPTY_START_BAR,
            )

    def _make_lilypond_file(self):
        includes = self._get_stylesheets()
        if self._environment == 'external':
            use_relative_includes = False
        else:
            use_relative_includes = True
        lilypond_file = abjad.LilyPondFile.new(
            music=self.score,
            date_time_token=False,
            includes=includes,
            use_relative_includes=use_relative_includes,
            )
        block_names = ('layout', 'paper')
        for item in lilypond_file.items[:]:
            if getattr(item, 'name', None) in block_names:
                lilypond_file.items.remove(item)
        if self._midi:
            block = abjad.Block(name='midi')
            lilypond_file.items.append(block)
        for item in lilypond_file.items[:]:
            if getattr(item, 'name', None) == 'header':
                lilypond_file.items.remove(item)
        self._lilypond_file = lilypond_file

    def _make_measure_silences(self, start, stop, measure_start_offsets):
        offsets = [start]
        for measure_start_offset in measure_start_offsets:
            if start < measure_start_offset < stop:
                offsets.append(measure_start_offset)
        offsets.append(stop)
        silences = []
        durations = abjad.mathtools.difference_series(offsets)
        for duration in durations:
            multiplier = abjad.Multiplier(duration)
            if self.skips_instead_of_rests:
                silence = abjad.Skip(1)
            else:
                silence = abjad.MultimeasureRest(1)
            abjad.attach(multiplier, silence, site='')
            silences.append(silence)
        return silences

    def _make_multimeasure_rests(self):
        rests = []
        for time_signature in self.time_signatures:
            rest = abjad.MultimeasureRest(abjad.Duration(1))
            multiplier = abjad.Multiplier(time_signature.duration)
            abjad.attach(multiplier, rest, site='')
            rests.append(rest)
        return rests

    def _make_score(self):
        score = self.score_template()
        first_measure_number = self._get_first_measure_number()
        if first_measure_number != 1:
            abjad.setting(score).current_bar_number = first_measure_number
        self._score = score

    def _momento_to_indicator(self, momento):
        if momento.value is None:
            return
        if momento.prototype in self._prototype_to_manifest_name:
            name = self._prototype_to_manifest_name.get(momento.prototype)
            dictionary = getattr(self, name)
            return dictionary.get(momento.value)
        class_ = eval(momento.prototype)
        if hasattr(class_, 'from_string'):
            return class_.from_string(momento.value)
        return class_(momento.value)

    def _print_cache(self):
        for context in self._cache:
            print(f'CONTEXT {context} ...')
            leaves_by_stage_number = self._cache[context]
            for stage_number in leaves_by_stage_number:
                print(f'STAGE {stage_number} ...')
                for leaf in leaves_by_stage_number[stage_number]:
                    print(leaf)

    def _print_segment_duration_(self):
        if not self.print_segment_duration:
            return
        current_tempo = None
        skips = baca.select(self.score['GlobalSkips']).skips()
        measure_summaries = []
        tempo_index = 0
        is_trending = False
        for i, skip in enumerate(skips):
            duration = abjad.inspect(skip).get_duration()
            tempi = abjad.inspect(skip).get_indicators(abjad.MetronomeMark)
            if tempi:
                current_tempo = tempi[0]
                for measure_summary in measure_summaries[tempo_index:]:
                    assert measure_summary[-1] is None
                    measure_summary[-1] = current_tempo
                tempo_index = i
                is_trending = False
            if abjad.inspect(skip).has_indicator(abjad.Accelerando):
                is_trending = True
            if abjad.inspect(skip).has_indicator(abjad.Ritardando):
                is_trending = True
            next_tempo = None
            measure_summary = [
                duration,
                current_tempo,
                is_trending,
                next_tempo,
                ]
            measure_summaries.append(measure_summary)
        total_duration = abjad.Duration(0)
        for measure_summary in measure_summaries:
            duration, current_tempo, is_trending, next_tempo = measure_summary
            if is_trending and current_tempo is not None:
                effective_tempo = current_tempo + next_tempo
                effective_tempo /= 2
            else:
                effective_tempo = current_tempo
            if effective_tempo is None:
                message = 'no effective tempo found ...'
                print(message)
                return
            duration_ = effective_tempo.duration_to_milliseconds(duration)
            duration_ /= 1000
            total_duration += duration_
        total_duration = int(round(total_duration))
        counter = abjad.String('second').pluralize(total_duration)
        print(f'segment duration {total_duration} {counter} ...')

    @staticmethod
    def _prototype_string(class_):
        parts = class_.__module__.split('.')
        return f'{parts[0]}.{parts[-1]}'

    def _reapply_persistent_indicators(self):
        if self.first_segment:
            return
        string = 'persistent_indicators'
        dictionary = self._previous_metadata.get('persistent_indicators')
        if not dictionary:
            return
        for context in abjad.iterate(self.score).components(abjad.Context):
            momentos = dictionary.get(context.name)
            if not momentos:
                continue
            for momento in momentos:
                result = self._analyze_momento(context, momento)
                if result is None:
                    continue
                leaf, previous_indicator, status = result
                if isinstance(previous_indicator, abjad.MetronomeMark):
                    spanner = abjad.inspect(leaf).get_spanner(
                        abjad.MetronomeMarkSpanner
                        )
                    assert spanner is not None, repr(spanner)
                else:
                    spanner = None
                self._categorize_persistent_indicator(
                    self.manifests,
                    context,
                    leaf,
                    previous_indicator,
                    status,
                    spanner=spanner,
                    )

    def _remove_redundant_time_signatures(self):
        previous_time_signature = None
        self._cached_time_signatures = []
        for skip in baca.select(self.score['GlobalSkips']).skips():
            time_signature = abjad.inspect(skip).get_indicator(
                abjad.TimeSignature
                )
            self._cached_time_signatures.append(str(time_signature))
            if time_signature == previous_time_signature:
                abjad.detach(time_signature, skip)
            else:
                previous_time_signature = time_signature

    def _remove_tags(self, tags):
        if not tags:
            return
        assert isinstance(tags, (tuple, list)), repr(tags)
        tags_ = []
        for tag in tags:
            if isinstance(tag, str):
                tags_.append(tag)
            else:
                tags_.append(tag.name)
        tags = tags_
        for leaf in abjad.iterate(self.score).leaves():
            for wrapper in abjad.inspect(leaf).wrappers():
                if wrapper.tag is None:
                    continue
                if wrapper.tag in tags:
                    abjad.detach(wrapper, leaf)

    def _scope_to_leaf_selection(self, wrapper):
        leaves = []
        selections = self._scope_to_leaf_selections(wrapper.scope)
        for selection in selections:
            leaves.extend(selection)
        selection = abjad.select(leaves)
        if not selection:
            message = f'EMPTY SELECTION:\n\n{format(wrapper)}'
            if self.allow_empty_selections:
                print(message)
            else:
                raise Exception(message)
        assert selection.are_leaves(), repr(selection)
        if isinstance(wrapper.scope, baca.TimelineScope):
            selection = wrapper.scope._sort_by_timeline(selection)
        return selection

    def _scope_to_leaf_selections(self, scope):
        if self._cache is None:
            self._cache_leaves()
        if isinstance(scope, baca.Scope):
            scopes = [scope]
        else:
            assert isinstance(scope, baca.TimelineScope)
            scopes = list(scope.scopes)
        leaf_selections = []
        for scope in scopes:
            leaves = []
            try:
                leaves_by_stage_number = self._cache[scope.voice_name]
            except KeyError:
                message = f'unknown voice {scope.voice_name!r}.'
                raise Exception(message)
            start = scope.stages[0]
            if (scope.stages[1] == abjad.Infinity or
                scope.stages[1] is abjad.Infinity):
                stop = self.stage_count + 1
            else:
                stop = scope.stages[1] + 1
            for stage_number in range(start, stop):
                leaves.extend(leaves_by_stage_number[stage_number])
            leaf_selections.append(abjad.select(leaves))
        return leaf_selections

    def _shorten_long_repeat_ties(self):
        leaves = abjad.iterate(self.score).leaves()
        for leaf in leaves:
            ties = abjad.inspect(leaf).get_spanners(abjad.Tie)
            if not ties:
                continue
            tie = ties.pop()
            if not tie.repeat_ties:
                continue
            previous_leaf = abjad.inspect(leaf).get_leaf(-1)
            if previous_leaf is None:
                continue
            minimum_duration = abjad.Duration(1, 8)
            if abjad.inspect(previous_leaf).get_duration() < minimum_duration:
                string = r"\shape #'((2 . 0) (1 . 0) (0.5 . 0) (0 . 0))"
                string += " RepeatTie"
                literal = abjad.LilyPondLiteral(string)
                abjad.attach(literal, leaf, site='SM26')

    def _stage_number_to_measure_indices(self, stage_number):
        if stage_number is abjad.Infinity or stage_number == abjad.Infinity:
            stage_number = self.stage_count
        if self.stage_count < stage_number:
            count = self.stage_count
            counter = abjad.String('stage').pluralize(count)
            message = f'segment has only {count} {counter}'
            message += f' (not {stage_number}).'
            raise Exception(message)
        measure_indices = abjad.mathtools.cumulative_sums(
            self.measures_per_stage)
        stop = stage_number - 1
        start_measure_index = measure_indices[stop]
        stop_measure_index = measure_indices[stage_number] - 1
        return start_measure_index, stop_measure_index

    def _tag_clock_time(self):
        skips = baca.select(self.score['GlobalSkips']).skips()
        if abjad.inspect(skips[0]).get_effective(abjad.MetronomeMark) is None:
            return
        skips_ = []
        for skip in skips:
            start_offset = abjad.inspect(skip).get_timespan().start_offset
            if start_offset in self._fermata_start_offsets:
                continue
            skips_.append(skip)
        start_clock_time = self._get_previous_stop_clock_time()
        start_clock_time = start_clock_time or "0'00''"
        self._start_clock_time = start_clock_time 
        minutes = 0
        if "'" in self._start_clock_time:
            tick_index = self._start_clock_time.find("'")
            minutes = self._start_clock_time[:tick_index]
            minutes = int(minutes)
        seconds = self._start_clock_time[-4:-2]
        seconds = int(seconds)
        seconds = 60 * minutes + seconds
        segment_start_offset = abjad.Duration(seconds)
        tag = baca.Tags.CLOCK_TIME_MARKUP
        label = abjad.label(skips_, site='SM28', tag=tag)
        segment_stop_duration = label.with_start_offsets(
            clock_time=True,
            font_size=-2,
            global_offset=segment_start_offset,
            )
        segment_stop_offset = abjad.Offset(segment_stop_duration)
        self._stop_clock_time = segment_stop_offset.to_clock_string()
        segment_duration = segment_stop_offset - segment_start_offset
        segment_duration = segment_duration.to_clock_string()
        self._duration = segment_duration

    @staticmethod
    def _tag_persistent_indicator(
        #self,
        context,
        leaf,
        indicator,
        status,
        redraw=None,
        spanner=None,
        stem=None,
        ):
        if context is not None:
            assert isinstance(context, abjad.Context), repr(context)
        stem = stem or SegmentMaker._indicator_to_stem(indicator)
        if redraw is True:
            if (getattr(indicator, 'latent', False) or
                stem in ('INSTRUMENT', 'MARGIN_MARKUP')):
                tag = SegmentMaker._get_tag(status, stem, prefix='redrawn')
            else:
                #raise Exception('FOO?')
                tag = SegmentMaker._get_tag(status, stem, prefix='redrawn')
        else:
            tag = SegmentMaker._get_tag(status, stem)
        if spanner is not None:
            spanner.attach(
                indicator,
                leaf,
                deactivate=True,
                site='SM27',
                tag=tag,
                )
        else:
            headword = getattr(context, 'headword', None)
            abjad.attach(
                indicator,
                leaf,
                context=headword,
                site='SM8',
                tag=tag,
                )

    def _categorize_uncategorized_persistent_indicators(self):
        for leaf in abjad.iterate(self.score).leaves():
            for wrapper in  abjad.inspect(leaf).wrappers():
                if not getattr(wrapper.indicator, 'persistent', False):
                    continue
                if wrapper.tag is not None:
                    continue
                previous_indicator = abjad.inspect(leaf).get_effective(
                    type(wrapper.indicator),
                    n=-1,
                    )
                if previous_indicator == wrapper.indicator:
                    status = 'redundant'
                else:
                    status = 'explicit'
                context = wrapper._find_correct_effective_context()
                self._categorize_persistent_indicator(
                    self.manifests,
                    context,
                    leaf,
                    wrapper.indicator,
                    status,
                    spanner=wrapper.piecewise_spanner,
                    )

    def _transpose_score_(self):
        if not self.transpose_score:
            return
        for pleaf in baca.select(self.score).pleaves():
            if abjad.inspect(pleaf).has_indicator(baca.Tags.DO_NOT_TRANSPOSE):
                continue
            abjad.Instrument.transpose_from_sounding_pitch(pleaf)

    def _voice_to_rhythm_wrappers(self, voice):
        wrappers = []
        for wrapper in self.wrappers:
            if not isinstance(wrapper.command, baca.RhythmCommand):
                continue
            if wrapper.scope.voice_name == voice.name:
                wrappers.append(wrapper)
        return wrappers

    def _whitespace_leaves(self):
        for leaf in abjad.iterate(self.score).leaves():
            literal = abjad.LilyPondLiteral('', 'absolute_before')
            abjad.attach(literal, leaf, site='')
            if abjad.inspect(leaf).get_leaf(1) is None:
                literal = abjad.LilyPondLiteral('', 'absolute_after')
                abjad.attach(literal, leaf, site='')

    ### PUBLIC PROPERTIES ###

    @property
    def allow_empty_selections(self):
        r'''Is true when segment allows empty selectors.

        Otherwise segment raises exception on empty selectors.

        Defaults to none.

        Set to true, false or none.

        Returns true, false or none.
        '''
        return self._allow_empty_selections

    @property
    def clefs(self):
        r'''Gets clefs.

        ..  container:: example

            Default clefs color purple and redraw dull purple:

            >>> layout_measure_map = baca.layout(
            ...     baca.page(
            ...         [1, 0, (7,)],
            ...         [2, 20, (7,)],
            ...         ),
            ...     )
            >>> score_template = baca.SingleStaffScoreTemplate()
            >>> triple = ('MusicStaff', 'default_clef', abjad.Clef('treble'))
            >>> score_template.defaults.append(triple)
            >>> maker = baca.SegmentMaker(
            ...     ignore_unpitched_notes=True,
            ...     layout_measure_map=layout_measure_map,
            ...     score_template=score_template,
            ...     spacing_specifier=baca.minimum_width((1, 24)),
            ...     time_signatures=[(3, 8), (3, 8)],
            ...     )

            >>> lilypond_file = maker.run(
            ...     environment='docs',
            ...     remove=[
            ...         baca.Tags.build(baca.Tags.SPACING_MARKUP),
            ...         baca.Tags.STAGE_NUMBER_MARKUP,
            ...         ],
            ...     )
            >>> block = abjad.Block(name='layout')
            >>> block.indent = 0
            >>> lilypond_file.items.insert(0, block)
            >>> abjad.show(lilypond_file, strict=89) # doctest: +SKIP

            ..  docs::

                >>> abjad.f(lilypond_file[abjad.Score], strict=89)
                \context Score = "Score" <<
                    \context GlobalContext = "GlobalContext" <<
                        \context GlobalSkips = "GlobalSkips" {
                <BLANKLINE>
                            % GlobalSkips [measure 1]                                                    %! SM4
                            \autoPageBreaksOff                                                           %! SEGMENT:LAYOUT:LMM1
                            \noBreak                                                                     %! SEGMENT:LAYOUT:LMM2
                            \overrideProperty Score.NonMusicalPaperColumn.line-break-system-details      %! SEGMENT:LAYOUT:LMM3
                            #'((Y-offset . 0) (alignment-distances . (7)))                               %! SEGMENT:LAYOUT:LMM3
                            \time 3/8                                                                    %! EXPLICIT_TIME_SIGNATURE:SM8
                            \bar ""                                                                      %! EMPTY_START_BAR:SM2
                            \once \override Score.TimeSignature.color = #(x11-color 'blue)               %! EXPLICIT_TIME_SIGNATURE_COLOR:SM6
                            \newSpacingSection                                                           %! SEGMENT:SPACING:HSS1
                            \set Score.proportionalNotationDuration = #(ly:make-moment 1 24)             %! SEGMENT:SPACING:HSS1
                            \pageBreak                                                                   %! SEGMENT:LAYOUT:LMM3
                            s1 * 3/8
                <BLANKLINE>
                            % GlobalSkips [measure 2]                                                    %! SM4
                            \noBreak                                                                     %! SEGMENT:LAYOUT:LMM2
                            \overrideProperty Score.NonMusicalPaperColumn.line-break-system-details      %! SEGMENT:LAYOUT:LMM3
                            #'((Y-offset . 20) (alignment-distances . (7)))                              %! SEGMENT:LAYOUT:LMM3
                            \once \override Score.TimeSignature.color = #(x11-color 'DeepPink1)          %! REDUNDANT_TIME_SIGNATURE_COLOR:SM6
                            \newSpacingSection                                                           %! SEGMENT:SPACING:HSS1
                            \set Score.proportionalNotationDuration = #(ly:make-moment 1 24)             %! SEGMENT:SPACING:HSS1
                            \break                                                                       %! SEGMENT:LAYOUT:LMM3
                            s1 * 3/8
                            \override Score.BarLine.transparent = ##f                                    %! SM5
                            \bar "|"                                                                     %! SM5
                <BLANKLINE>
                        }
                    >>
                    \context MusicContext = "MusicContext" <<
                        \context Staff = "MusicStaff" {
                            \context Voice = "MusicVoice" {
                <BLANKLINE>
                                % MusicVoice [measure 1]                                                 %! SM4
                                \set Staff.forceClef = ##t                                               %! DEFAULT_CLEF:SM8
                                \clef "treble"                                                           %! DEFAULT_CLEF:SM8
                                \once \override Staff.Clef.color = #(x11-color 'DarkViolet)              %! DEFAULT_CLEF_COLOR:SM6
                                %%% \override Staff.Clef.color = ##f                                     %! DEFAULT_CLEF_COLOR_CANCELLATION:SM7
                                R1 * 3/8
                                \override Staff.Clef.color = #(x11-color 'violet)                        %! DEFAULT_CLEF_REDRAW_COLOR:SM6
                <BLANKLINE>
                                % MusicVoice [measure 2]                                                 %! SM4
                                R1 * 3/8
                <BLANKLINE>
                            }
                        }
                    >>
                >>

        ..  container:: example

            Explicit clefs color blue and redraw dull blue:

            >>> layout_measure_map = baca.layout(
            ...     baca.page(
            ...         [1, 0, (7,)],
            ...         [2, 20, (7,)],
            ...         ),
            ...     )
            >>> maker = baca.SegmentMaker(
            ...     ignore_unpitched_notes=True,
            ...     layout_measure_map=layout_measure_map,
            ...     score_template=baca.SingleStaffScoreTemplate(),
            ...     spacing_specifier=baca.minimum_width((1, 24)),
            ...     time_signatures=[(3, 8), (3, 8)],
            ...     )
            >>> maker(
            ...     baca.scope('MusicVoice', 1),
            ...     baca.clef('treble'),
            ...     )

            >>> lilypond_file = maker.run(
            ...     environment='docs',
            ...     remove=[
            ...         baca.Tags.build(baca.Tags.SPACING_MARKUP),
            ...         baca.Tags.STAGE_NUMBER_MARKUP,
            ...         ],
            ...     )
            >>> block = abjad.Block(name='layout')
            >>> block.indent = 0
            >>> lilypond_file.items.insert(0, block)
            >>> abjad.show(lilypond_file, strict=89) # doctest: +SKIP

            ..  docs::

                >>> abjad.f(lilypond_file[abjad.Score], strict=89)
                \context Score = "Score" <<
                    \context GlobalContext = "GlobalContext" <<
                        \context GlobalSkips = "GlobalSkips" {
                <BLANKLINE>
                            % GlobalSkips [measure 1]                                                    %! SM4
                            \autoPageBreaksOff                                                           %! SEGMENT:LAYOUT:LMM1
                            \noBreak                                                                     %! SEGMENT:LAYOUT:LMM2
                            \overrideProperty Score.NonMusicalPaperColumn.line-break-system-details      %! SEGMENT:LAYOUT:LMM3
                            #'((Y-offset . 0) (alignment-distances . (7)))                               %! SEGMENT:LAYOUT:LMM3
                            \time 3/8                                                                    %! EXPLICIT_TIME_SIGNATURE:SM8
                            \bar ""                                                                      %! EMPTY_START_BAR:SM2
                            \once \override Score.TimeSignature.color = #(x11-color 'blue)               %! EXPLICIT_TIME_SIGNATURE_COLOR:SM6
                            \newSpacingSection                                                           %! SEGMENT:SPACING:HSS1
                            \set Score.proportionalNotationDuration = #(ly:make-moment 1 24)             %! SEGMENT:SPACING:HSS1
                            \pageBreak                                                                   %! SEGMENT:LAYOUT:LMM3
                            s1 * 3/8
                <BLANKLINE>
                            % GlobalSkips [measure 2]                                                    %! SM4
                            \noBreak                                                                     %! SEGMENT:LAYOUT:LMM2
                            \overrideProperty Score.NonMusicalPaperColumn.line-break-system-details      %! SEGMENT:LAYOUT:LMM3
                            #'((Y-offset . 20) (alignment-distances . (7)))                              %! SEGMENT:LAYOUT:LMM3
                            \once \override Score.TimeSignature.color = #(x11-color 'DeepPink1)          %! REDUNDANT_TIME_SIGNATURE_COLOR:SM6
                            \newSpacingSection                                                           %! SEGMENT:SPACING:HSS1
                            \set Score.proportionalNotationDuration = #(ly:make-moment 1 24)             %! SEGMENT:SPACING:HSS1
                            \break                                                                       %! SEGMENT:LAYOUT:LMM3
                            s1 * 3/8
                            \override Score.BarLine.transparent = ##f                                    %! SM5
                            \bar "|"                                                                     %! SM5
                <BLANKLINE>
                        }
                    >>
                    \context MusicContext = "MusicContext" <<
                        \context Staff = "MusicStaff" {
                            \context Voice = "MusicVoice" {
                <BLANKLINE>
                                % MusicVoice [measure 1]                                                 %! SM4
                                \set Staff.forceClef = ##t                                               %! EXPLICIT_CLEF:SM8
                                \clef "treble"                                                           %! EXPLICIT_CLEF:SM8
                                \once \override Staff.Clef.color = #(x11-color 'blue)                    %! EXPLICIT_CLEF_COLOR:SM6
                                %%% \override Staff.Clef.color = ##f                                     %! EXPLICIT_CLEF_COLOR_CANCELLATION:SM7
                                R1 * 3/8
                                \override Staff.Clef.color = #(x11-color 'DeepSkyBlue2)                  %! EXPLICIT_CLEF_REDRAW_COLOR:SM6
                <BLANKLINE>
                                % MusicVoice [measure 2]                                                 %! SM4
                                R1 * 3/8
                <BLANKLINE>
                            }
                        }
                    >>
                >>

            Even after a previous clef:

            >>> layout_measure_map = baca.layout(
            ...     baca.page(
            ...         [1, 0, (7,)],
            ...         [2, 20, (7,)],
            ...         ),
            ...     )
            >>> maker = baca.SegmentMaker(
            ...     ignore_unpitched_notes=True,
            ...     layout_measure_map=layout_measure_map,
            ...     score_template=baca.SingleStaffScoreTemplate(),
            ...     spacing_specifier=baca.minimum_width((1, 24)),
            ...     time_signatures=[(3, 8), (3, 8)],
            ...     )
            >>> maker(
            ...     baca.scope('MusicVoice', 1),
            ...     baca.clef('alto'),
            ...     )

            >>> metadata = {}
            >>> metadata['persistent_indicators'] = {}
            >>> metadata['persistent_indicators']['MusicStaff'] = [
            ...     abjad.Momento(
            ...         context='MusicVoice',
            ...         prototype='abjad.Clef',
            ...         value='treble',
            ...         )
            ...     ]
            >>> metadata['segment_number'] = 1
            >>> lilypond_file = maker.run(
            ...     environment='docs',
            ...     previous_metadata=metadata,
            ...     remove=[
            ...         baca.Tags.build(baca.Tags.SPACING_MARKUP),
            ...         baca.Tags.STAGE_NUMBER_MARKUP,
            ...         ],
            ...     )
            >>> block = abjad.Block(name='layout')
            >>> block.indent = 0
            >>> lilypond_file.items.insert(0, block)
            >>> abjad.show(lilypond_file, strict=89) # doctest: +SKIP

            ..  docs::

                >>> abjad.f(lilypond_file[abjad.Score], strict=89)
                \context Score = "Score" <<
                    \context GlobalContext = "GlobalContext" <<
                        \context GlobalSkips = "GlobalSkips" {
                <BLANKLINE>
                            % GlobalSkips [measure 1]                                                    %! SM4
                            \autoPageBreaksOff                                                           %! SEGMENT:LAYOUT:LMM1
                            \noBreak                                                                     %! SEGMENT:LAYOUT:LMM2
                            \overrideProperty Score.NonMusicalPaperColumn.line-break-system-details      %! SEGMENT:LAYOUT:LMM3
                            #'((Y-offset . 0) (alignment-distances . (7)))                               %! SEGMENT:LAYOUT:LMM3
                            \time 3/8                                                                    %! EXPLICIT_TIME_SIGNATURE:SM8
                            \mark #1                                                                     %! SM9
                            \bar ""                                                                      %! EMPTY_START_BAR:SM2
                            \once \override Score.TimeSignature.color = #(x11-color 'blue)               %! EXPLICIT_TIME_SIGNATURE_COLOR:SM6
                            \newSpacingSection                                                           %! SEGMENT:SPACING:HSS1
                            \set Score.proportionalNotationDuration = #(ly:make-moment 1 24)             %! SEGMENT:SPACING:HSS1
                            \pageBreak                                                                   %! SEGMENT:LAYOUT:LMM3
                            s1 * 3/8
                <BLANKLINE>
                            % GlobalSkips [measure 2]                                                    %! SM4
                            \noBreak                                                                     %! SEGMENT:LAYOUT:LMM2
                            \overrideProperty Score.NonMusicalPaperColumn.line-break-system-details      %! SEGMENT:LAYOUT:LMM3
                            #'((Y-offset . 20) (alignment-distances . (7)))                              %! SEGMENT:LAYOUT:LMM3
                            \once \override Score.TimeSignature.color = #(x11-color 'DeepPink1)          %! REDUNDANT_TIME_SIGNATURE_COLOR:SM6
                            \newSpacingSection                                                           %! SEGMENT:SPACING:HSS1
                            \set Score.proportionalNotationDuration = #(ly:make-moment 1 24)             %! SEGMENT:SPACING:HSS1
                            \break                                                                       %! SEGMENT:LAYOUT:LMM3
                            s1 * 3/8
                            \override Score.BarLine.transparent = ##f                                    %! SM5
                            \bar "|"                                                                     %! SM5
                <BLANKLINE>
                        }
                    >>
                    \context MusicContext = "MusicContext" <<
                        \context Staff = "MusicStaff" {
                            \context Voice = "MusicVoice" {
                <BLANKLINE>
                                % MusicVoice [measure 1]                                                 %! SM4
                                \set Staff.forceClef = ##t                                               %! EXPLICIT_CLEF:SM8
                                \clef "alto"                                                             %! EXPLICIT_CLEF:SM8
                                \once \override Staff.Clef.color = #(x11-color 'blue)                    %! EXPLICIT_CLEF_COLOR:SM6
                                %%% \override Staff.Clef.color = ##f                                     %! EXPLICIT_CLEF_COLOR_CANCELLATION:SM7
                                R1 * 3/8
                                \override Staff.Clef.color = #(x11-color 'DeepSkyBlue2)                  %! EXPLICIT_CLEF_REDRAW_COLOR:SM6
                <BLANKLINE>
                                % MusicVoice [measure 2]                                                 %! SM4
                                R1 * 3/8
                <BLANKLINE>
                            }
                        }
                    >>
                >>

        ..  container:: example

            Reapplied clefs color green and redraw dull green:

            >>> layout_measure_map = baca.layout(
            ...     baca.page(
            ...         [1, 0, (7,)],
            ...         [2, 20, (7,)],
            ...         ),
            ...     )
            >>> maker = baca.SegmentMaker(
            ...     ignore_unpitched_notes=True,
            ...     layout_measure_map=layout_measure_map,
            ...     score_template=baca.SingleStaffScoreTemplate(),
            ...     spacing_specifier=baca.minimum_width((1, 24)),
            ...     time_signatures=[(3, 8), (3, 8)],
            ...     )

            >>> metadata = {}
            >>> metadata['persistent_indicators'] = {}
            >>> metadata['persistent_indicators']['MusicStaff'] = [
            ...     abjad.Momento(
            ...         context='MusicVoice',
            ...         prototype='abjad.Clef',
            ...         value='treble',
            ...         )
            ...     ]
            >>> metadata['segment_number'] = 1
            >>> lilypond_file = maker.run(
            ...     environment='docs',
            ...     previous_metadata=metadata,
            ...     remove=[
            ...         baca.Tags.build(baca.Tags.SPACING_MARKUP),
            ...         baca.Tags.STAGE_NUMBER_MARKUP,
            ...         ],
            ...     )
            >>> block = abjad.Block(name='layout')
            >>> block.indent = 0
            >>> lilypond_file.items.insert(0, block)

            >>> abjad.show(lilypond_file, strict=89) # doctest: +SKIP

            ..  docs::

                >>> abjad.f(lilypond_file[abjad.Score], strict=89)
                \context Score = "Score" <<
                    \context GlobalContext = "GlobalContext" <<
                        \context GlobalSkips = "GlobalSkips" {
                <BLANKLINE>
                            % GlobalSkips [measure 1]                                                    %! SM4
                            \autoPageBreaksOff                                                           %! SEGMENT:LAYOUT:LMM1
                            \noBreak                                                                     %! SEGMENT:LAYOUT:LMM2
                            \overrideProperty Score.NonMusicalPaperColumn.line-break-system-details      %! SEGMENT:LAYOUT:LMM3
                            #'((Y-offset . 0) (alignment-distances . (7)))                               %! SEGMENT:LAYOUT:LMM3
                            \time 3/8                                                                    %! EXPLICIT_TIME_SIGNATURE:SM8
                            \mark #1                                                                     %! SM9
                            \bar ""                                                                      %! EMPTY_START_BAR:SM2
                            \once \override Score.TimeSignature.color = #(x11-color 'blue)               %! EXPLICIT_TIME_SIGNATURE_COLOR:SM6
                            \newSpacingSection                                                           %! SEGMENT:SPACING:HSS1
                            \set Score.proportionalNotationDuration = #(ly:make-moment 1 24)             %! SEGMENT:SPACING:HSS1
                            \pageBreak                                                                   %! SEGMENT:LAYOUT:LMM3
                            s1 * 3/8
                <BLANKLINE>
                            % GlobalSkips [measure 2]                                                    %! SM4
                            \noBreak                                                                     %! SEGMENT:LAYOUT:LMM2
                            \overrideProperty Score.NonMusicalPaperColumn.line-break-system-details      %! SEGMENT:LAYOUT:LMM3
                            #'((Y-offset . 20) (alignment-distances . (7)))                              %! SEGMENT:LAYOUT:LMM3
                            \once \override Score.TimeSignature.color = #(x11-color 'DeepPink1)          %! REDUNDANT_TIME_SIGNATURE_COLOR:SM6
                            \newSpacingSection                                                           %! SEGMENT:SPACING:HSS1
                            \set Score.proportionalNotationDuration = #(ly:make-moment 1 24)             %! SEGMENT:SPACING:HSS1
                            \break                                                                       %! SEGMENT:LAYOUT:LMM3
                            s1 * 3/8
                            \override Score.BarLine.transparent = ##f                                    %! SM5
                            \bar "|"                                                                     %! SM5
                <BLANKLINE>
                        }
                    >>
                    \context MusicContext = "MusicContext" <<
                        \context Staff = "MusicStaff" {
                            \context Voice = "MusicVoice" {
                <BLANKLINE>
                                % MusicVoice [measure 1]                                                 %! SM4
                                \set Staff.forceClef = ##t                                               %! REAPPLIED_CLEF:SM8
                                \clef "treble"                                                           %! REAPPLIED_CLEF:SM8
                                \once \override Staff.Clef.color = #(x11-color 'green4)                  %! REAPPLIED_CLEF_COLOR:SM6
                                %%% \override Staff.Clef.color = ##f                                     %! REAPPLIED_CLEF_COLOR_CANCELLATION:SM7
                                R1 * 3/8
                                \override Staff.Clef.color = #(x11-color 'OliveDrab)                     %! REAPPLIED_CLEF_REDRAW_COLOR:SM6
                <BLANKLINE>
                                % MusicVoice [measure 2]                                                 %! SM4
                                R1 * 3/8
                <BLANKLINE>
                            }
                        }
                    >>
                >>

        ..  container:: example

            Redundant clefs color pink and redraw dull pink:

            >>> layout_measure_map = baca.layout(
            ...     baca.page(
            ...         [1, 0, (7,)],
            ...         [3, 20, (7,)],
            ...         ),
            ...     )
            >>> maker = baca.SegmentMaker(
            ...     ignore_unpitched_notes=True,
            ...     layout_measure_map=layout_measure_map,
            ...     score_template=baca.SingleStaffScoreTemplate(),
            ...     spacing_specifier=baca.minimum_width((1, 24)),
            ...     time_signatures=[(3, 8), (3, 8), (3, 8)],
            ...     )
            >>> maker(
            ...     baca.scope('MusicVoice', 1),
            ...     baca.clef('treble', baca.leaf(0)),
            ...     baca.clef('treble', baca.leaf(1)),
            ...     )
            >>> lilypond_file = maker.run(
            ...     environment='docs',
            ...     remove=(
            ...         baca.Tags.build(baca.Tags.SPACING_MARKUP),
            ...         baca.Tags.STAGE_NUMBER_MARKUP,
            ...         ),
            ...     )
            >>> block = abjad.Block(name='layout')
            >>> block.indent = 0
            >>> lilypond_file.items.insert(0, block)

            >>> abjad.show(lilypond_file, strict=89) # doctest: +SKIP

            ..  docs::

                >>> abjad.f(lilypond_file[abjad.Score], strict=89)
                \context Score = "Score" <<
                    \context GlobalContext = "GlobalContext" <<
                        \context GlobalSkips = "GlobalSkips" {
                <BLANKLINE>
                            % GlobalSkips [measure 1]                                                    %! SM4
                            \autoPageBreaksOff                                                           %! SEGMENT:LAYOUT:LMM1
                            \noBreak                                                                     %! SEGMENT:LAYOUT:LMM2
                            \overrideProperty Score.NonMusicalPaperColumn.line-break-system-details      %! SEGMENT:LAYOUT:LMM3
                            #'((Y-offset . 0) (alignment-distances . (7)))                               %! SEGMENT:LAYOUT:LMM3
                            \time 3/8                                                                    %! EXPLICIT_TIME_SIGNATURE:SM8
                            \bar ""                                                                      %! EMPTY_START_BAR:SM2
                            \once \override Score.TimeSignature.color = #(x11-color 'blue)               %! EXPLICIT_TIME_SIGNATURE_COLOR:SM6
                            \newSpacingSection                                                           %! SEGMENT:SPACING:HSS1
                            \set Score.proportionalNotationDuration = #(ly:make-moment 1 24)             %! SEGMENT:SPACING:HSS1
                            \pageBreak                                                                   %! SEGMENT:LAYOUT:LMM3
                            s1 * 3/8
                <BLANKLINE>
                            % GlobalSkips [measure 2]                                                    %! SM4
                            \noBreak                                                                     %! SEGMENT:LAYOUT:LMM2
                            \once \override Score.TimeSignature.color = #(x11-color 'DeepPink1)          %! REDUNDANT_TIME_SIGNATURE_COLOR:SM6
                            \newSpacingSection                                                           %! SEGMENT:SPACING:HSS1
                            \set Score.proportionalNotationDuration = #(ly:make-moment 1 24)             %! SEGMENT:SPACING:HSS1
                            s1 * 3/8
                <BLANKLINE>
                            % GlobalSkips [measure 3]                                                    %! SM4
                            \noBreak                                                                     %! SEGMENT:LAYOUT:LMM2
                            \overrideProperty Score.NonMusicalPaperColumn.line-break-system-details      %! SEGMENT:LAYOUT:LMM3
                            #'((Y-offset . 20) (alignment-distances . (7)))                              %! SEGMENT:LAYOUT:LMM3
                            \once \override Score.TimeSignature.color = #(x11-color 'DeepPink1)          %! REDUNDANT_TIME_SIGNATURE_COLOR:SM6
                            \newSpacingSection                                                           %! SEGMENT:SPACING:HSS1
                            \set Score.proportionalNotationDuration = #(ly:make-moment 1 24)             %! SEGMENT:SPACING:HSS1
                            \break                                                                       %! SEGMENT:LAYOUT:LMM3
                            s1 * 3/8
                            \override Score.BarLine.transparent = ##f                                    %! SM5
                            \bar "|"                                                                     %! SM5
                <BLANKLINE>
                        }
                    >>
                    \context MusicContext = "MusicContext" <<
                        \context Staff = "MusicStaff" {
                            \context Voice = "MusicVoice" {
                <BLANKLINE>
                                % MusicVoice [measure 1]                                                 %! SM4
                                \set Staff.forceClef = ##t                                               %! EXPLICIT_CLEF:SM8
                                \clef "treble"                                                           %! EXPLICIT_CLEF:SM8
                                \once \override Staff.Clef.color = #(x11-color 'blue)                    %! EXPLICIT_CLEF_COLOR:SM6
                                %%% \override Staff.Clef.color = ##f                                     %! EXPLICIT_CLEF_COLOR_CANCELLATION:SM7
                                R1 * 3/8
                                \override Staff.Clef.color = #(x11-color 'DeepSkyBlue2)                  %! EXPLICIT_CLEF_REDRAW_COLOR:SM6
                <BLANKLINE>
                                % MusicVoice [measure 2]                                                 %! SM4
                                \set Staff.forceClef = ##t                                               %! REDUNDANT_CLEF:SM8
                                \clef "treble"                                                           %! REDUNDANT_CLEF:SM8
                                \once \override Staff.Clef.color = #(x11-color 'DeepPink1)               %! REDUNDANT_CLEF_COLOR:SM6
                                %%% \override Staff.Clef.color = ##f                                     %! REDUNDANT_CLEF_COLOR_CANCELLATION:SM7
                                R1 * 3/8
                                \override Staff.Clef.color = #(x11-color 'DeepPink4)                     %! REDUNDANT_CLEF_REDRAW_COLOR:SM6
                <BLANKLINE>
                                % MusicVoice [measure 3]                                                 %! SM4
                                R1 * 3/8
                <BLANKLINE>
                            }
                        }
                    >>
                >>

            Even at the beginning of a segment:

            >>> layout_measure_map = baca.layout(
            ...     baca.page(
            ...         [1, 0, (7,)],
            ...         [2, 20, (7,)],
            ...         ),
            ...     )
            >>> maker = baca.SegmentMaker(
            ...     ignore_unpitched_notes=True,
            ...     layout_measure_map=layout_measure_map,
            ...     score_template=baca.SingleStaffScoreTemplate(),
            ...     spacing_specifier=baca.minimum_width((1, 24)),
            ...     time_signatures=[(3, 8), (3, 8)],
            ...     )
            >>> maker(
            ...     baca.scope('MusicVoice', 1),
            ...     baca.clef('treble'),
            ...     )

            >>> metadata = {}
            >>> metadata['persistent_indicators'] = {}
            >>> metadata['persistent_indicators']['MusicStaff'] = [
            ...     abjad.Momento(
            ...         context='MusicVoice',
            ...         prototype='abjad.Clef',
            ...         value='treble',
            ...         )
            ...     ]
            >>> metadata['segment_number'] = 1
            >>> lilypond_file = maker.run(
            ...     environment='docs',
            ...     previous_metadata=metadata,
            ...     remove=(
            ...         baca.Tags.build(baca.Tags.SPACING_MARKUP),
            ...         baca.Tags.STAGE_NUMBER_MARKUP,
            ...         ),
            ...     )
            >>> block = abjad.Block(name='layout')
            >>> block.indent = 0
            >>> lilypond_file.items.insert(0, block)

            >>> abjad.show(lilypond_file, strict=89) # doctest: +SKIP

            ..  docs::

                >>> abjad.f(lilypond_file[abjad.Score], strict=89)
                \context Score = "Score" <<
                    \context GlobalContext = "GlobalContext" <<
                        \context GlobalSkips = "GlobalSkips" {
                <BLANKLINE>
                            % GlobalSkips [measure 1]                                                    %! SM4
                            \autoPageBreaksOff                                                           %! SEGMENT:LAYOUT:LMM1
                            \noBreak                                                                     %! SEGMENT:LAYOUT:LMM2
                            \overrideProperty Score.NonMusicalPaperColumn.line-break-system-details      %! SEGMENT:LAYOUT:LMM3
                            #'((Y-offset . 0) (alignment-distances . (7)))                               %! SEGMENT:LAYOUT:LMM3
                            \time 3/8                                                                    %! EXPLICIT_TIME_SIGNATURE:SM8
                            \mark #1                                                                     %! SM9
                            \bar ""                                                                      %! EMPTY_START_BAR:SM2
                            \once \override Score.TimeSignature.color = #(x11-color 'blue)               %! EXPLICIT_TIME_SIGNATURE_COLOR:SM6
                            \newSpacingSection                                                           %! SEGMENT:SPACING:HSS1
                            \set Score.proportionalNotationDuration = #(ly:make-moment 1 24)             %! SEGMENT:SPACING:HSS1
                            \pageBreak                                                                   %! SEGMENT:LAYOUT:LMM3
                            s1 * 3/8
                <BLANKLINE>
                            % GlobalSkips [measure 2]                                                    %! SM4
                            \noBreak                                                                     %! SEGMENT:LAYOUT:LMM2
                            \overrideProperty Score.NonMusicalPaperColumn.line-break-system-details      %! SEGMENT:LAYOUT:LMM3
                            #'((Y-offset . 20) (alignment-distances . (7)))                              %! SEGMENT:LAYOUT:LMM3
                            \once \override Score.TimeSignature.color = #(x11-color 'DeepPink1)          %! REDUNDANT_TIME_SIGNATURE_COLOR:SM6
                            \newSpacingSection                                                           %! SEGMENT:SPACING:HSS1
                            \set Score.proportionalNotationDuration = #(ly:make-moment 1 24)             %! SEGMENT:SPACING:HSS1
                            \break                                                                       %! SEGMENT:LAYOUT:LMM3
                            s1 * 3/8
                            \override Score.BarLine.transparent = ##f                                    %! SM5
                            \bar "|"                                                                     %! SM5
                <BLANKLINE>
                        }
                    >>
                    \context MusicContext = "MusicContext" <<
                        \context Staff = "MusicStaff" {
                            \context Voice = "MusicVoice" {
                <BLANKLINE>
                                % MusicVoice [measure 1]                                                 %! SM4
                                \set Staff.forceClef = ##t                                               %! REDUNDANT_CLEF:SM8
                                \clef "treble"                                                           %! REDUNDANT_CLEF:SM8
                                \once \override Staff.Clef.color = #(x11-color 'DeepPink1)               %! REDUNDANT_CLEF_COLOR:SM6
                                %%% \override Staff.Clef.color = ##f                                     %! REDUNDANT_CLEF_COLOR_CANCELLATION:SM7
                                R1 * 3/8
                                \override Staff.Clef.color = #(x11-color 'DeepPink4)                     %! REDUNDANT_CLEF_REDRAW_COLOR:SM6
                <BLANKLINE>
                                % MusicVoice [measure 2]                                                 %! SM4
                                R1 * 3/8
                <BLANKLINE>
                            }
                        }
                    >>
                >>

        Returns none.
        '''
        pass

    @property
    def color_octaves(self):
        r'''Is true when segment-maker colors octaves.

        ..  container:: example

            Colors octaves:

            >>> maker = baca.SegmentMaker(
            ...     color_octaves=True,
            ...     score_template=baca.StringTrioScoreTemplate(),
            ...     spacing_specifier=baca.minimum_width((1, 31)),
            ...     time_signatures=[(6, 16)],
            ...     )

            >>> music_maker = baca.MusicMaker()
            >>> contribution = music_maker(
            ...     'ViolinMusicVoice',
            ...     [[2, 4, 5, 7, 9, 11]],
            ...     baca.flags(),
            ...     )
            >>> maker(
            ...     baca.scope('ViolinMusicVoice', 1),
            ...     baca.rhythm(contribution['ViolinMusicVoice']),
            ...     )

            >>> contribution = music_maker(
            ...     'CelloMusicVoice',
            ...     [[-3, -5, -7, -8, -10, -12]],
            ...     baca.flags(),
            ...     )
            >>> maker(
            ...     baca.scope('CelloMusicVoice', 1),
            ...     baca.rhythm(contribution['CelloMusicVoice']),
            ...     )

            >>> lilypond_file = maker.run(environment='docs')
            >>> abjad.setting(lilypond_file['Score']).auto_beaming = False
            >>> abjad.show(lilypond_file, strict=89) # doctest: +SKIP

            ..  docs::

                >>> abjad.f(lilypond_file[abjad.Score], strict=89)
                \context Score = "Score" \with {
                    autoBeaming = ##f
                } <<
                    \tag violin.viola.cello                                                              %! ST4
                    \context GlobalContext = "GlobalContext" <<
                        \context GlobalSkips = "GlobalSkips" {
                <BLANKLINE>
                            % GlobalSkips [measure 1]                                                    %! SM4
                            \time 6/16                                                                   %! EXPLICIT_TIME_SIGNATURE:SM8
                            \bar ""                                                                      %! EMPTY_START_BAR:SM2
                            \once \override Score.TimeSignature.color = #(x11-color 'blue)               %! EXPLICIT_TIME_SIGNATURE_COLOR:SM6
                            \newSpacingSection                                                           %! SEGMENT:SPACING:HSS1
                            \set Score.proportionalNotationDuration = #(ly:make-moment 1 31)             %! SEGMENT:SPACING:HSS1
                            s1 * 3/8
                            ^ \markup {
                                \column
                                    {
                                        \line                                                            %! STAGE_NUMBER_MARKUP:SM3
                                            {                                                            %! STAGE_NUMBER_MARKUP:SM3
                                                \fontsize                                                %! STAGE_NUMBER_MARKUP:SM3
                                                    #-3                                                  %! STAGE_NUMBER_MARKUP:SM3
                                                    \with-color                                          %! STAGE_NUMBER_MARKUP:SM3
                                                        #(x11-color 'DarkCyan)                           %! STAGE_NUMBER_MARKUP:SM3
                                                        [1]                                              %! STAGE_NUMBER_MARKUP:SM3
                                            }                                                            %! STAGE_NUMBER_MARKUP:SM3
                                        \line                                                            %! SEGMENT:SPACING_MARKUP:HSS2
                                            {                                                            %! SEGMENT:SPACING_MARKUP:HSS2
                                                \with-color                                              %! SEGMENT:SPACING_MARKUP:HSS2
                                                    #(x11-color 'DarkCyan)                               %! SEGMENT:SPACING_MARKUP:HSS2
                                                    \fontsize                                            %! SEGMENT:SPACING_MARKUP:HSS2
                                                        #-3                                              %! SEGMENT:SPACING_MARKUP:HSS2
                                                        (1/31)                                           %! SEGMENT:SPACING_MARKUP:HSS2
                                            }                                                            %! SEGMENT:SPACING_MARKUP:HSS2
                                    }
                                }
                            \override Score.BarLine.transparent = ##f                                    %! SM5
                            \bar "|"                                                                     %! SM5
                <BLANKLINE>
                        }
                    >>
                    \context MusicContext = "MusicContext" <<
                        \context StringSectionStaffGroup = "String Section Staff Group" <<
                            \tag violin                                                                  %! ST4
                            \context ViolinMusicStaff = "ViolinMusicStaff" {
                                \context ViolinMusicVoice = "ViolinMusicVoice" {
                                    {
                                        {
                <BLANKLINE>
                                            % ViolinMusicVoice [measure 1]                               %! SM4
                                            \set ViolinMusicStaff.instrumentName = \markup {             %! DEFAULT_INSTRUMENT:SM8
                                                \hcenter-in                                              %! DEFAULT_INSTRUMENT:SM8
                                                    #10                                                  %! DEFAULT_INSTRUMENT:SM8
                                                    Violin                                               %! DEFAULT_INSTRUMENT:SM8
                                                }                                                        %! DEFAULT_INSTRUMENT:SM8
                                            \set ViolinMusicStaff.shortInstrumentName = \markup {        %! DEFAULT_INSTRUMENT:SM8
                                                \hcenter-in                                              %! DEFAULT_INSTRUMENT:SM8
                                                    #10                                                  %! DEFAULT_INSTRUMENT:SM8
                                                    Vn.                                                  %! DEFAULT_INSTRUMENT:SM8
                                                }                                                        %! DEFAULT_INSTRUMENT:SM8
                                            \set ViolinMusicStaff.forceClef = ##t                        %! DEFAULT_CLEF:SM8
                                            \clef "treble"                                               %! DEFAULT_CLEF:SM8
                                            \once \override ViolinMusicStaff.InstrumentName.color = #(x11-color 'DarkViolet) %! DEFAULT_INSTRUMENT_COLOR:SM6
                                            \once \override ViolinMusicStaff.Clef.color = #(x11-color 'DarkViolet) %! DEFAULT_CLEF_COLOR:SM6
                                            %%% \override ViolinMusicStaff.Clef.color = ##f              %! DEFAULT_CLEF_COLOR_CANCELLATION:SM7
                                            d'16
                                            ^ \markup {
                                                \column
                                                    {
                                                        %%% \line                                        %! DEFAULT_INSTRUMENT_ALERT:SM10
                                                        %%%     {                                        %! DEFAULT_INSTRUMENT_ALERT:SM10
                                                        %%%         \vcenter                             %! DEFAULT_INSTRUMENT_ALERT:SM10
                                                        %%%             (Violin                          %! DEFAULT_INSTRUMENT_ALERT:SM10
                                                        %%%         \vcenter                             %! DEFAULT_INSTRUMENT_ALERT:SM10
                                                        %%%             \hcenter-in                      %! DEFAULT_INSTRUMENT_ALERT:SM10
                                                        %%%                 #10                          %! DEFAULT_INSTRUMENT_ALERT:SM10
                                                        %%%                 Violin                       %! DEFAULT_INSTRUMENT_ALERT:SM10
                                                        %%%         \concat                              %! DEFAULT_INSTRUMENT_ALERT:SM10
                                                        %%%             {                                %! DEFAULT_INSTRUMENT_ALERT:SM10
                                                        %%%                 \vcenter                     %! DEFAULT_INSTRUMENT_ALERT:SM10
                                                        %%%                     \hcenter-in              %! DEFAULT_INSTRUMENT_ALERT:SM10
                                                        %%%                         #10                  %! DEFAULT_INSTRUMENT_ALERT:SM10
                                                        %%%                         Vn.                  %! DEFAULT_INSTRUMENT_ALERT:SM10
                                                        %%%                 \vcenter                     %! DEFAULT_INSTRUMENT_ALERT:SM10
                                                        %%%                     )                        %! DEFAULT_INSTRUMENT_ALERT:SM10
                                                        %%%             }                                %! DEFAULT_INSTRUMENT_ALERT:SM10
                                                        %%%     }                                        %! DEFAULT_INSTRUMENT_ALERT:SM10
                                                        \line                                            %! DEFAULT_INSTRUMENT_ALERT_WITH_COLOR:SM11
                                                            {                                            %! DEFAULT_INSTRUMENT_ALERT_WITH_COLOR:SM11
                                                                \with-color                              %! DEFAULT_INSTRUMENT_ALERT_WITH_COLOR:SM11
                                                                    #(x11-color 'DarkViolet)             %! DEFAULT_INSTRUMENT_ALERT_WITH_COLOR:SM11
                                                                    {                                    %! DEFAULT_INSTRUMENT_ALERT_WITH_COLOR:SM11
                                                                        \vcenter                         %! DEFAULT_INSTRUMENT_ALERT_WITH_COLOR:SM11
                                                                            (Violin                      %! DEFAULT_INSTRUMENT_ALERT_WITH_COLOR:SM11
                                                                        \vcenter                         %! DEFAULT_INSTRUMENT_ALERT_WITH_COLOR:SM11
                                                                            \hcenter-in                  %! DEFAULT_INSTRUMENT_ALERT_WITH_COLOR:SM11
                                                                                #10                      %! DEFAULT_INSTRUMENT_ALERT_WITH_COLOR:SM11
                                                                                Violin                   %! DEFAULT_INSTRUMENT_ALERT_WITH_COLOR:SM11
                                                                        \concat                          %! DEFAULT_INSTRUMENT_ALERT_WITH_COLOR:SM11
                                                                            {                            %! DEFAULT_INSTRUMENT_ALERT_WITH_COLOR:SM11
                                                                                \vcenter                 %! DEFAULT_INSTRUMENT_ALERT_WITH_COLOR:SM11
                                                                                    \hcenter-in          %! DEFAULT_INSTRUMENT_ALERT_WITH_COLOR:SM11
                                                                                        #10              %! DEFAULT_INSTRUMENT_ALERT_WITH_COLOR:SM11
                                                                                        Vn.              %! DEFAULT_INSTRUMENT_ALERT_WITH_COLOR:SM11
                                                                                \vcenter                 %! DEFAULT_INSTRUMENT_ALERT_WITH_COLOR:SM11
                                                                                    )                    %! DEFAULT_INSTRUMENT_ALERT_WITH_COLOR:SM11
                                                                            }                            %! DEFAULT_INSTRUMENT_ALERT_WITH_COLOR:SM11
                                                                    }                                    %! DEFAULT_INSTRUMENT_ALERT_WITH_COLOR:SM11
                                                            }                                            %! DEFAULT_INSTRUMENT_ALERT_WITH_COLOR:SM11
                                                    }
                                                }
                                            \set ViolinMusicStaff.instrumentName = \markup {             %! REDRAWN_DEFAULT_INSTRUMENT:SM8
                                                \hcenter-in                                              %! REDRAWN_DEFAULT_INSTRUMENT:SM8
                                                    #10                                                  %! REDRAWN_DEFAULT_INSTRUMENT:SM8
                                                    Violin                                               %! REDRAWN_DEFAULT_INSTRUMENT:SM8
                                                }                                                        %! REDRAWN_DEFAULT_INSTRUMENT:SM8
                                            \set ViolinMusicStaff.shortInstrumentName = \markup {        %! REDRAWN_DEFAULT_INSTRUMENT:SM8
                                                \hcenter-in                                              %! REDRAWN_DEFAULT_INSTRUMENT:SM8
                                                    #10                                                  %! REDRAWN_DEFAULT_INSTRUMENT:SM8
                                                    Vn.                                                  %! REDRAWN_DEFAULT_INSTRUMENT:SM8
                                                }                                                        %! REDRAWN_DEFAULT_INSTRUMENT:SM8
                                            \override ViolinMusicStaff.InstrumentName.color = #(x11-color 'violet) %! REDRAWN_DEFAULT_INSTRUMENT_COLOR:SM6
                                            \override ViolinMusicStaff.Clef.color = #(x11-color 'violet) %! DEFAULT_CLEF_REDRAW_COLOR:SM6
                <BLANKLINE>
                                            e'16
                <BLANKLINE>
                                            \once \override Accidental.color = #red
                                            \once \override Beam.color = #red
                                            \once \override Dots.color = #red
                                            \once \override NoteHead.color = #red
                                            \once \override Stem.color = #red
                                            f'16
                                            - \tweak color #red                                          %! SM12
                                            ^ \markup { OCTAVE }                                         %! SM12
                <BLANKLINE>
                                            g'16
                <BLANKLINE>
                                            a'16
                <BLANKLINE>
                                            b'16
                <BLANKLINE>
                                        }
                                    }
                                }
                            }
                            \tag viola                                                                   %! ST4
                            \context ViolaMusicStaff = "ViolaMusicStaff" {
                                \context ViolaMusicVoice = "ViolaMusicVoice" {
                <BLANKLINE>
                                    % ViolaMusicVoice [measure 1]                                        %! SM4
                                    \set ViolaMusicStaff.instrumentName = \markup {                      %! DEFAULT_INSTRUMENT:SM8
                                        \hcenter-in                                                      %! DEFAULT_INSTRUMENT:SM8
                                            #10                                                          %! DEFAULT_INSTRUMENT:SM8
                                            Viola                                                        %! DEFAULT_INSTRUMENT:SM8
                                        }                                                                %! DEFAULT_INSTRUMENT:SM8
                                    \set ViolaMusicStaff.shortInstrumentName = \markup {                 %! DEFAULT_INSTRUMENT:SM8
                                        \hcenter-in                                                      %! DEFAULT_INSTRUMENT:SM8
                                            #10                                                          %! DEFAULT_INSTRUMENT:SM8
                                            Va.                                                          %! DEFAULT_INSTRUMENT:SM8
                                        }                                                                %! DEFAULT_INSTRUMENT:SM8
                                    \set ViolaMusicStaff.forceClef = ##t                                 %! DEFAULT_CLEF:SM8
                                    \clef "alto"                                                         %! DEFAULT_CLEF:SM8
                                    \once \override ViolaMusicStaff.InstrumentName.color = #(x11-color 'DarkViolet) %! DEFAULT_INSTRUMENT_COLOR:SM6
                                    \once \override ViolaMusicStaff.Clef.color = #(x11-color 'DarkViolet) %! DEFAULT_CLEF_COLOR:SM6
                                    %%% \override ViolaMusicStaff.Clef.color = ##f                       %! DEFAULT_CLEF_COLOR_CANCELLATION:SM7
                                    R1 * 3/8
                                    ^ \markup {
                                        \column
                                            {
                                                %%% \line                                                %! DEFAULT_INSTRUMENT_ALERT:SM10
                                                %%%     {                                                %! DEFAULT_INSTRUMENT_ALERT:SM10
                                                %%%         \vcenter                                     %! DEFAULT_INSTRUMENT_ALERT:SM10
                                                %%%             (Viola                                   %! DEFAULT_INSTRUMENT_ALERT:SM10
                                                %%%         \vcenter                                     %! DEFAULT_INSTRUMENT_ALERT:SM10
                                                %%%             \hcenter-in                              %! DEFAULT_INSTRUMENT_ALERT:SM10
                                                %%%                 #10                                  %! DEFAULT_INSTRUMENT_ALERT:SM10
                                                %%%                 Viola                                %! DEFAULT_INSTRUMENT_ALERT:SM10
                                                %%%         \concat                                      %! DEFAULT_INSTRUMENT_ALERT:SM10
                                                %%%             {                                        %! DEFAULT_INSTRUMENT_ALERT:SM10
                                                %%%                 \vcenter                             %! DEFAULT_INSTRUMENT_ALERT:SM10
                                                %%%                     \hcenter-in                      %! DEFAULT_INSTRUMENT_ALERT:SM10
                                                %%%                         #10                          %! DEFAULT_INSTRUMENT_ALERT:SM10
                                                %%%                         Va.                          %! DEFAULT_INSTRUMENT_ALERT:SM10
                                                %%%                 \vcenter                             %! DEFAULT_INSTRUMENT_ALERT:SM10
                                                %%%                     )                                %! DEFAULT_INSTRUMENT_ALERT:SM10
                                                %%%             }                                        %! DEFAULT_INSTRUMENT_ALERT:SM10
                                                %%%     }                                                %! DEFAULT_INSTRUMENT_ALERT:SM10
                                                \line                                                    %! DEFAULT_INSTRUMENT_ALERT_WITH_COLOR:SM11
                                                    {                                                    %! DEFAULT_INSTRUMENT_ALERT_WITH_COLOR:SM11
                                                        \with-color                                      %! DEFAULT_INSTRUMENT_ALERT_WITH_COLOR:SM11
                                                            #(x11-color 'DarkViolet)                     %! DEFAULT_INSTRUMENT_ALERT_WITH_COLOR:SM11
                                                            {                                            %! DEFAULT_INSTRUMENT_ALERT_WITH_COLOR:SM11
                                                                \vcenter                                 %! DEFAULT_INSTRUMENT_ALERT_WITH_COLOR:SM11
                                                                    (Viola                               %! DEFAULT_INSTRUMENT_ALERT_WITH_COLOR:SM11
                                                                \vcenter                                 %! DEFAULT_INSTRUMENT_ALERT_WITH_COLOR:SM11
                                                                    \hcenter-in                          %! DEFAULT_INSTRUMENT_ALERT_WITH_COLOR:SM11
                                                                        #10                              %! DEFAULT_INSTRUMENT_ALERT_WITH_COLOR:SM11
                                                                        Viola                            %! DEFAULT_INSTRUMENT_ALERT_WITH_COLOR:SM11
                                                                \concat                                  %! DEFAULT_INSTRUMENT_ALERT_WITH_COLOR:SM11
                                                                    {                                    %! DEFAULT_INSTRUMENT_ALERT_WITH_COLOR:SM11
                                                                        \vcenter                         %! DEFAULT_INSTRUMENT_ALERT_WITH_COLOR:SM11
                                                                            \hcenter-in                  %! DEFAULT_INSTRUMENT_ALERT_WITH_COLOR:SM11
                                                                                #10                      %! DEFAULT_INSTRUMENT_ALERT_WITH_COLOR:SM11
                                                                                Va.                      %! DEFAULT_INSTRUMENT_ALERT_WITH_COLOR:SM11
                                                                        \vcenter                         %! DEFAULT_INSTRUMENT_ALERT_WITH_COLOR:SM11
                                                                            )                            %! DEFAULT_INSTRUMENT_ALERT_WITH_COLOR:SM11
                                                                    }                                    %! DEFAULT_INSTRUMENT_ALERT_WITH_COLOR:SM11
                                                            }                                            %! DEFAULT_INSTRUMENT_ALERT_WITH_COLOR:SM11
                                                    }                                                    %! DEFAULT_INSTRUMENT_ALERT_WITH_COLOR:SM11
                                            }
                                        }
                                    \set ViolaMusicStaff.instrumentName = \markup {                      %! REDRAWN_DEFAULT_INSTRUMENT:SM8
                                        \hcenter-in                                                      %! REDRAWN_DEFAULT_INSTRUMENT:SM8
                                            #10                                                          %! REDRAWN_DEFAULT_INSTRUMENT:SM8
                                            Viola                                                        %! REDRAWN_DEFAULT_INSTRUMENT:SM8
                                        }                                                                %! REDRAWN_DEFAULT_INSTRUMENT:SM8
                                    \set ViolaMusicStaff.shortInstrumentName = \markup {                 %! REDRAWN_DEFAULT_INSTRUMENT:SM8
                                        \hcenter-in                                                      %! REDRAWN_DEFAULT_INSTRUMENT:SM8
                                            #10                                                          %! REDRAWN_DEFAULT_INSTRUMENT:SM8
                                            Va.                                                          %! REDRAWN_DEFAULT_INSTRUMENT:SM8
                                        }                                                                %! REDRAWN_DEFAULT_INSTRUMENT:SM8
                                    \override ViolaMusicStaff.InstrumentName.color = #(x11-color 'violet) %! REDRAWN_DEFAULT_INSTRUMENT_COLOR:SM6
                                    \override ViolaMusicStaff.Clef.color = #(x11-color 'violet)          %! DEFAULT_CLEF_REDRAW_COLOR:SM6
                <BLANKLINE>
                                }
                            }
                            \tag cello                                                                   %! ST4
                            \context CelloMusicStaff = "CelloMusicStaff" {
                                \context CelloMusicVoice = "CelloMusicVoice" {
                                    {
                                        {
                <BLANKLINE>
                                            % CelloMusicVoice [measure 1]                                %! SM4
                                            \set CelloMusicStaff.instrumentName = \markup {              %! DEFAULT_INSTRUMENT:SM8
                                                \hcenter-in                                              %! DEFAULT_INSTRUMENT:SM8
                                                    #10                                                  %! DEFAULT_INSTRUMENT:SM8
                                                    Cello                                                %! DEFAULT_INSTRUMENT:SM8
                                                }                                                        %! DEFAULT_INSTRUMENT:SM8
                                            \set CelloMusicStaff.shortInstrumentName = \markup {         %! DEFAULT_INSTRUMENT:SM8
                                                \hcenter-in                                              %! DEFAULT_INSTRUMENT:SM8
                                                    #10                                                  %! DEFAULT_INSTRUMENT:SM8
                                                    Vc.                                                  %! DEFAULT_INSTRUMENT:SM8
                                                }                                                        %! DEFAULT_INSTRUMENT:SM8
                                            \set CelloMusicStaff.forceClef = ##t                         %! DEFAULT_CLEF:SM8
                                            \clef "bass"                                                 %! DEFAULT_CLEF:SM8
                                            \once \override CelloMusicStaff.InstrumentName.color = #(x11-color 'DarkViolet) %! DEFAULT_INSTRUMENT_COLOR:SM6
                                            \once \override CelloMusicStaff.Clef.color = #(x11-color 'DarkViolet) %! DEFAULT_CLEF_COLOR:SM6
                                            %%% \override CelloMusicStaff.Clef.color = ##f               %! DEFAULT_CLEF_COLOR_CANCELLATION:SM7
                                            a16
                                            ^ \markup {
                                                \column
                                                    {
                                                        %%% \line                                        %! DEFAULT_INSTRUMENT_ALERT:SM10
                                                        %%%     {                                        %! DEFAULT_INSTRUMENT_ALERT:SM10
                                                        %%%         \vcenter                             %! DEFAULT_INSTRUMENT_ALERT:SM10
                                                        %%%             (Cello                           %! DEFAULT_INSTRUMENT_ALERT:SM10
                                                        %%%         \vcenter                             %! DEFAULT_INSTRUMENT_ALERT:SM10
                                                        %%%             \hcenter-in                      %! DEFAULT_INSTRUMENT_ALERT:SM10
                                                        %%%                 #10                          %! DEFAULT_INSTRUMENT_ALERT:SM10
                                                        %%%                 Cello                        %! DEFAULT_INSTRUMENT_ALERT:SM10
                                                        %%%         \concat                              %! DEFAULT_INSTRUMENT_ALERT:SM10
                                                        %%%             {                                %! DEFAULT_INSTRUMENT_ALERT:SM10
                                                        %%%                 \vcenter                     %! DEFAULT_INSTRUMENT_ALERT:SM10
                                                        %%%                     \hcenter-in              %! DEFAULT_INSTRUMENT_ALERT:SM10
                                                        %%%                         #10                  %! DEFAULT_INSTRUMENT_ALERT:SM10
                                                        %%%                         Vc.                  %! DEFAULT_INSTRUMENT_ALERT:SM10
                                                        %%%                 \vcenter                     %! DEFAULT_INSTRUMENT_ALERT:SM10
                                                        %%%                     )                        %! DEFAULT_INSTRUMENT_ALERT:SM10
                                                        %%%             }                                %! DEFAULT_INSTRUMENT_ALERT:SM10
                                                        %%%     }                                        %! DEFAULT_INSTRUMENT_ALERT:SM10
                                                        \line                                            %! DEFAULT_INSTRUMENT_ALERT_WITH_COLOR:SM11
                                                            {                                            %! DEFAULT_INSTRUMENT_ALERT_WITH_COLOR:SM11
                                                                \with-color                              %! DEFAULT_INSTRUMENT_ALERT_WITH_COLOR:SM11
                                                                    #(x11-color 'DarkViolet)             %! DEFAULT_INSTRUMENT_ALERT_WITH_COLOR:SM11
                                                                    {                                    %! DEFAULT_INSTRUMENT_ALERT_WITH_COLOR:SM11
                                                                        \vcenter                         %! DEFAULT_INSTRUMENT_ALERT_WITH_COLOR:SM11
                                                                            (Cello                       %! DEFAULT_INSTRUMENT_ALERT_WITH_COLOR:SM11
                                                                        \vcenter                         %! DEFAULT_INSTRUMENT_ALERT_WITH_COLOR:SM11
                                                                            \hcenter-in                  %! DEFAULT_INSTRUMENT_ALERT_WITH_COLOR:SM11
                                                                                #10                      %! DEFAULT_INSTRUMENT_ALERT_WITH_COLOR:SM11
                                                                                Cello                    %! DEFAULT_INSTRUMENT_ALERT_WITH_COLOR:SM11
                                                                        \concat                          %! DEFAULT_INSTRUMENT_ALERT_WITH_COLOR:SM11
                                                                            {                            %! DEFAULT_INSTRUMENT_ALERT_WITH_COLOR:SM11
                                                                                \vcenter                 %! DEFAULT_INSTRUMENT_ALERT_WITH_COLOR:SM11
                                                                                    \hcenter-in          %! DEFAULT_INSTRUMENT_ALERT_WITH_COLOR:SM11
                                                                                        #10              %! DEFAULT_INSTRUMENT_ALERT_WITH_COLOR:SM11
                                                                                        Vc.              %! DEFAULT_INSTRUMENT_ALERT_WITH_COLOR:SM11
                                                                                \vcenter                 %! DEFAULT_INSTRUMENT_ALERT_WITH_COLOR:SM11
                                                                                    )                    %! DEFAULT_INSTRUMENT_ALERT_WITH_COLOR:SM11
                                                                            }                            %! DEFAULT_INSTRUMENT_ALERT_WITH_COLOR:SM11
                                                                    }                                    %! DEFAULT_INSTRUMENT_ALERT_WITH_COLOR:SM11
                                                            }                                            %! DEFAULT_INSTRUMENT_ALERT_WITH_COLOR:SM11
                                                    }
                                                }
                                            \set CelloMusicStaff.instrumentName = \markup {              %! REDRAWN_DEFAULT_INSTRUMENT:SM8
                                                \hcenter-in                                              %! REDRAWN_DEFAULT_INSTRUMENT:SM8
                                                    #10                                                  %! REDRAWN_DEFAULT_INSTRUMENT:SM8
                                                    Cello                                                %! REDRAWN_DEFAULT_INSTRUMENT:SM8
                                                }                                                        %! REDRAWN_DEFAULT_INSTRUMENT:SM8
                                            \set CelloMusicStaff.shortInstrumentName = \markup {         %! REDRAWN_DEFAULT_INSTRUMENT:SM8
                                                \hcenter-in                                              %! REDRAWN_DEFAULT_INSTRUMENT:SM8
                                                    #10                                                  %! REDRAWN_DEFAULT_INSTRUMENT:SM8
                                                    Vc.                                                  %! REDRAWN_DEFAULT_INSTRUMENT:SM8
                                                }                                                        %! REDRAWN_DEFAULT_INSTRUMENT:SM8
                                            \override CelloMusicStaff.InstrumentName.color = #(x11-color 'violet) %! REDRAWN_DEFAULT_INSTRUMENT_COLOR:SM6
                                            \override CelloMusicStaff.Clef.color = #(x11-color 'violet)  %! DEFAULT_CLEF_REDRAW_COLOR:SM6
                <BLANKLINE>
                                            g16
                <BLANKLINE>
                                            \once \override Accidental.color = #red
                                            \once \override Beam.color = #red
                                            \once \override Dots.color = #red
                                            \once \override NoteHead.color = #red
                                            \once \override Stem.color = #red
                                            f16
                                            - \tweak color #red                                          %! SM12
                                            ^ \markup { OCTAVE }                                         %! SM12
                <BLANKLINE>
                                            e16
                <BLANKLINE>
                                            d16
                <BLANKLINE>
                                            c16
                <BLANKLINE>
                                        }
                                    }
                                }
                            }
                        >>
                    >>
                >>

        Defaults to none.

        Set to true, false or none.

        Returns true, false or none.
        '''
        return self._color_octaves

    @property
    def color_out_of_range_pitches(self):
        r'''Is true when segment-maker colors out-of-range pitches.

        ..  container:: example

            Colors out-of-range pitches:

            >>> music_maker = baca.MusicMaker()

            >>> collection_lists = [
            ...     [[4]],
            ...     [[-12, 2, 3, 5, 8, 9, 0]],
            ...     [[11]],
            ...     [[10, 7, 9, 10, 0, 5]],
            ...     ]
            >>> figures, time_signatures = [], []
            >>> for i, collections in enumerate(collection_lists):
            ...     contribution = music_maker(
            ...         'Voice 1',
            ...         collections,
            ...         baca.flags(),
            ...         )
            ...     figures.append(contribution['Voice 1'])
            ...     time_signatures.append(contribution.time_signature)
            ...
            >>> figures_ = []
            >>> for figure in figures:
            ...     figures_.extend(figure)
            ...
            >>> figures = abjad.select(figures_)

            >>> pitch_range = abjad.Violin().pitch_range
            >>> maker = baca.SegmentMaker(
            ...     color_out_of_range_pitches=True,
            ...     range_checker=pitch_range,
            ...     score_template=baca.SingleStaffScoreTemplate(),
            ...     spacing_specifier=baca.minimum_width((1, 24)),
            ...     time_signatures=time_signatures,
            ...     )
            >>> maker(
            ...     baca.scope('MusicVoice', 1),
            ...     baca.rhythm(figures),
            ...     )

            >>> lilypond_file = maker.run(environment='docs')
            >>> abjad.setting(lilypond_file['Score']).auto_beaming = False
            >>> abjad.show(lilypond_file, strict=89) # doctest: +SKIP

            ..  docs::

                >>> abjad.f(lilypond_file[abjad.Score], strict=89)
                \context Score = "Score" \with {
                    autoBeaming = ##f
                } <<
                    \context GlobalContext = "GlobalContext" <<
                        \context GlobalSkips = "GlobalSkips" {
                <BLANKLINE>
                            % GlobalSkips [measure 1]                                                    %! SM4
                            \time 1/16                                                                   %! EXPLICIT_TIME_SIGNATURE:SM8
                            \bar ""                                                                      %! EMPTY_START_BAR:SM2
                            \once \override Score.TimeSignature.color = #(x11-color 'blue)               %! EXPLICIT_TIME_SIGNATURE_COLOR:SM6
                            \newSpacingSection                                                           %! SEGMENT:SPACING:HSS1
                            \set Score.proportionalNotationDuration = #(ly:make-moment 1 24)             %! SEGMENT:SPACING:HSS1
                            s1 * 1/16
                            ^ \markup {
                                \column
                                    {
                                        \line                                                            %! STAGE_NUMBER_MARKUP:SM3
                                            {                                                            %! STAGE_NUMBER_MARKUP:SM3
                                                \fontsize                                                %! STAGE_NUMBER_MARKUP:SM3
                                                    #-3                                                  %! STAGE_NUMBER_MARKUP:SM3
                                                    \with-color                                          %! STAGE_NUMBER_MARKUP:SM3
                                                        #(x11-color 'DarkCyan)                           %! STAGE_NUMBER_MARKUP:SM3
                                                        [1]                                              %! STAGE_NUMBER_MARKUP:SM3
                                            }                                                            %! STAGE_NUMBER_MARKUP:SM3
                                        \line                                                            %! SEGMENT:SPACING_MARKUP:HSS2
                                            {                                                            %! SEGMENT:SPACING_MARKUP:HSS2
                                                \with-color                                              %! SEGMENT:SPACING_MARKUP:HSS2
                                                    #(x11-color 'DarkCyan)                               %! SEGMENT:SPACING_MARKUP:HSS2
                                                    \fontsize                                            %! SEGMENT:SPACING_MARKUP:HSS2
                                                        #-3                                              %! SEGMENT:SPACING_MARKUP:HSS2
                                                        (1/24)                                           %! SEGMENT:SPACING_MARKUP:HSS2
                                            }                                                            %! SEGMENT:SPACING_MARKUP:HSS2
                                    }
                                }
                <BLANKLINE>
                            % GlobalSkips [measure 2]                                                    %! SM4
                            \time 7/16                                                                   %! EXPLICIT_TIME_SIGNATURE:SM8
                            \once \override Score.TimeSignature.color = #(x11-color 'blue)               %! EXPLICIT_TIME_SIGNATURE_COLOR:SM6
                            \newSpacingSection                                                           %! SEGMENT:SPACING:HSS1
                            \set Score.proportionalNotationDuration = #(ly:make-moment 1 24)             %! SEGMENT:SPACING:HSS1
                            s1 * 7/16
                            ^ \markup {                                                                  %! SEGMENT:SPACING_MARKUP:HSS2
                                \with-color                                                              %! SEGMENT:SPACING_MARKUP:HSS2
                                    #(x11-color 'DarkCyan)                                               %! SEGMENT:SPACING_MARKUP:HSS2
                                    \fontsize                                                            %! SEGMENT:SPACING_MARKUP:HSS2
                                        #-3                                                              %! SEGMENT:SPACING_MARKUP:HSS2
                                        (1/24)                                                           %! SEGMENT:SPACING_MARKUP:HSS2
                                }                                                                        %! SEGMENT:SPACING_MARKUP:HSS2
                <BLANKLINE>
                            % GlobalSkips [measure 3]                                                    %! SM4
                            \time 1/16                                                                   %! EXPLICIT_TIME_SIGNATURE:SM8
                            \once \override Score.TimeSignature.color = #(x11-color 'blue)               %! EXPLICIT_TIME_SIGNATURE_COLOR:SM6
                            \newSpacingSection                                                           %! SEGMENT:SPACING:HSS1
                            \set Score.proportionalNotationDuration = #(ly:make-moment 1 24)             %! SEGMENT:SPACING:HSS1
                            s1 * 1/16
                            ^ \markup {                                                                  %! SEGMENT:SPACING_MARKUP:HSS2
                                \with-color                                                              %! SEGMENT:SPACING_MARKUP:HSS2
                                    #(x11-color 'DarkCyan)                                               %! SEGMENT:SPACING_MARKUP:HSS2
                                    \fontsize                                                            %! SEGMENT:SPACING_MARKUP:HSS2
                                        #-3                                                              %! SEGMENT:SPACING_MARKUP:HSS2
                                        (1/24)                                                           %! SEGMENT:SPACING_MARKUP:HSS2
                                }                                                                        %! SEGMENT:SPACING_MARKUP:HSS2
                <BLANKLINE>
                            % GlobalSkips [measure 4]                                                    %! SM4
                            \time 3/8                                                                    %! EXPLICIT_TIME_SIGNATURE:SM8
                            \once \override Score.TimeSignature.color = #(x11-color 'blue)               %! EXPLICIT_TIME_SIGNATURE_COLOR:SM6
                            \newSpacingSection                                                           %! SEGMENT:SPACING:HSS1
                            \set Score.proportionalNotationDuration = #(ly:make-moment 1 24)             %! SEGMENT:SPACING:HSS1
                            s1 * 3/8
                            ^ \markup {                                                                  %! SEGMENT:SPACING_MARKUP:HSS2
                                \with-color                                                              %! SEGMENT:SPACING_MARKUP:HSS2
                                    #(x11-color 'DarkCyan)                                               %! SEGMENT:SPACING_MARKUP:HSS2
                                    \fontsize                                                            %! SEGMENT:SPACING_MARKUP:HSS2
                                        #-3                                                              %! SEGMENT:SPACING_MARKUP:HSS2
                                        (1/24)                                                           %! SEGMENT:SPACING_MARKUP:HSS2
                                }                                                                        %! SEGMENT:SPACING_MARKUP:HSS2
                            \override Score.BarLine.transparent = ##f                                    %! SM5
                            \bar "|"                                                                     %! SM5
                <BLANKLINE>
                        }
                    >>
                    \context MusicContext = "MusicContext" <<
                        \context Staff = "MusicStaff" {
                            \context Voice = "MusicVoice" {
                                {
                                    {
                <BLANKLINE>
                                        % MusicVoice [measure 1]                                         %! SM4
                                        e'16
                                    }
                                }
                                {
                                    {
                <BLANKLINE>
                                        % MusicVoice [measure 2]                                         %! SM4
                                        \once \override Accidental.color = #red
                                        \once \override Beam.color = #red
                                        \once \override Dots.color = #red
                                        \once \override NoteHead.color = #red
                                        \once \override Stem.color = #red
                                        c16
                                        - \tweak color #red                                              %! SM13
                                        ^ \markup { * }                                                  %! SM13
                <BLANKLINE>
                                        d'16
                <BLANKLINE>
                                        ef'16
                <BLANKLINE>
                                        f'16
                <BLANKLINE>
                                        af'16
                <BLANKLINE>
                                        a'16
                <BLANKLINE>
                                        c'16
                                    }
                                }
                                {
                                    {
                <BLANKLINE>
                                        % MusicVoice [measure 3]                                         %! SM4
                                        b'16
                                    }
                                }
                                {
                                    {
                <BLANKLINE>
                                        % MusicVoice [measure 4]                                         %! SM4
                                        bf'16
                <BLANKLINE>
                                        g'16
                <BLANKLINE>
                                        a'16
                <BLANKLINE>
                                        bf'16
                <BLANKLINE>
                                        c'16
                <BLANKLINE>
                                        f'16
                <BLANKLINE>
                                    }
                                }
                            }
                        }
                    >>
                >>

        Defaults to none.

        Set to true, false or none.

        Returns true, false or none.
        '''
        return self._color_out_of_range_pitches

    @property
    def color_repeat_pitch_classes(self):
        r'''Is true when segment-maker colors repeat pitch-classes.

        ..  container:: example

            Colors repeat pitch-classes:

            >>> music_maker = baca.MusicMaker()

            >>> collection_lists = [
            ...     [[4]],
            ...     [[6, 2, 3, 5, 9, 9, 0]],
            ...     [[11]],
            ...     [[10, 7, 9, 12, 0, 5]],
            ...     ]
            >>> figures, time_signatures = [], []
            >>> for i, collections in enumerate(collection_lists):
            ...     contribution = music_maker(
            ...         'Voice 1',
            ...         collections,
            ...         baca.flags(),
            ...         )
            ...     figures.append(contribution['Voice 1'])
            ...     time_signatures.append(contribution.time_signature)
            ...
            >>> figures_ = []
            >>> for figure in figures:
            ...     figures_.extend(figure)
            ...
            >>> figures = abjad.select(figures_)

            >>> maker = baca.SegmentMaker(
            ...     color_repeat_pitch_classes=True,
            ...     score_template=baca.SingleStaffScoreTemplate(),
            ...     spacing_specifier=baca.HorizontalSpacingSpecifier(
            ...         minimum_width=abjad.Duration(1, 24),
            ...         ),
            ...     time_signatures=time_signatures,
            ...     )
            >>> maker(
            ...     baca.scope('MusicVoice', 1),
            ...     baca.rhythm(figures),
            ...     )

            >>> lilypond_file = maker.run(environment='docs')
            >>> abjad.setting(lilypond_file['Score']).auto_beaming = False
            >>> abjad.show(lilypond_file, strict=89) # doctest: +SKIP

            ..  docs::

                >>> abjad.f(lilypond_file[abjad.Score], strict=89)
                \context Score = "Score" \with {
                    autoBeaming = ##f
                } <<
                    \context GlobalContext = "GlobalContext" <<
                        \context GlobalSkips = "GlobalSkips" {
                <BLANKLINE>
                            % GlobalSkips [measure 1]                                                    %! SM4
                            \time 1/16                                                                   %! EXPLICIT_TIME_SIGNATURE:SM8
                            \bar ""                                                                      %! EMPTY_START_BAR:SM2
                            \once \override Score.TimeSignature.color = #(x11-color 'blue)               %! EXPLICIT_TIME_SIGNATURE_COLOR:SM6
                            \newSpacingSection                                                           %! SEGMENT:SPACING:HSS1
                            \set Score.proportionalNotationDuration = #(ly:make-moment 1 24)             %! SEGMENT:SPACING:HSS1
                            s1 * 1/16
                            ^ \markup {
                                \column
                                    {
                                        \line                                                            %! STAGE_NUMBER_MARKUP:SM3
                                            {                                                            %! STAGE_NUMBER_MARKUP:SM3
                                                \fontsize                                                %! STAGE_NUMBER_MARKUP:SM3
                                                    #-3                                                  %! STAGE_NUMBER_MARKUP:SM3
                                                    \with-color                                          %! STAGE_NUMBER_MARKUP:SM3
                                                        #(x11-color 'DarkCyan)                           %! STAGE_NUMBER_MARKUP:SM3
                                                        [1]                                              %! STAGE_NUMBER_MARKUP:SM3
                                            }                                                            %! STAGE_NUMBER_MARKUP:SM3
                                        \line                                                            %! SEGMENT:SPACING_MARKUP:HSS2
                                            {                                                            %! SEGMENT:SPACING_MARKUP:HSS2
                                                \with-color                                              %! SEGMENT:SPACING_MARKUP:HSS2
                                                    #(x11-color 'DarkCyan)                               %! SEGMENT:SPACING_MARKUP:HSS2
                                                    \fontsize                                            %! SEGMENT:SPACING_MARKUP:HSS2
                                                        #-3                                              %! SEGMENT:SPACING_MARKUP:HSS2
                                                        (1/24)                                           %! SEGMENT:SPACING_MARKUP:HSS2
                                            }                                                            %! SEGMENT:SPACING_MARKUP:HSS2
                                    }
                                }
                <BLANKLINE>
                            % GlobalSkips [measure 2]                                                    %! SM4
                            \time 7/16                                                                   %! EXPLICIT_TIME_SIGNATURE:SM8
                            \once \override Score.TimeSignature.color = #(x11-color 'blue)               %! EXPLICIT_TIME_SIGNATURE_COLOR:SM6
                            \newSpacingSection                                                           %! SEGMENT:SPACING:HSS1
                            \set Score.proportionalNotationDuration = #(ly:make-moment 1 24)             %! SEGMENT:SPACING:HSS1
                            s1 * 7/16
                            ^ \markup {                                                                  %! SEGMENT:SPACING_MARKUP:HSS2
                                \with-color                                                              %! SEGMENT:SPACING_MARKUP:HSS2
                                    #(x11-color 'DarkCyan)                                               %! SEGMENT:SPACING_MARKUP:HSS2
                                    \fontsize                                                            %! SEGMENT:SPACING_MARKUP:HSS2
                                        #-3                                                              %! SEGMENT:SPACING_MARKUP:HSS2
                                        (1/24)                                                           %! SEGMENT:SPACING_MARKUP:HSS2
                                }                                                                        %! SEGMENT:SPACING_MARKUP:HSS2
                <BLANKLINE>
                            % GlobalSkips [measure 3]                                                    %! SM4
                            \time 1/16                                                                   %! EXPLICIT_TIME_SIGNATURE:SM8
                            \once \override Score.TimeSignature.color = #(x11-color 'blue)               %! EXPLICIT_TIME_SIGNATURE_COLOR:SM6
                            \newSpacingSection                                                           %! SEGMENT:SPACING:HSS1
                            \set Score.proportionalNotationDuration = #(ly:make-moment 1 24)             %! SEGMENT:SPACING:HSS1
                            s1 * 1/16
                            ^ \markup {                                                                  %! SEGMENT:SPACING_MARKUP:HSS2
                                \with-color                                                              %! SEGMENT:SPACING_MARKUP:HSS2
                                    #(x11-color 'DarkCyan)                                               %! SEGMENT:SPACING_MARKUP:HSS2
                                    \fontsize                                                            %! SEGMENT:SPACING_MARKUP:HSS2
                                        #-3                                                              %! SEGMENT:SPACING_MARKUP:HSS2
                                        (1/24)                                                           %! SEGMENT:SPACING_MARKUP:HSS2
                                }                                                                        %! SEGMENT:SPACING_MARKUP:HSS2
                <BLANKLINE>
                            % GlobalSkips [measure 4]                                                    %! SM4
                            \time 3/8                                                                    %! EXPLICIT_TIME_SIGNATURE:SM8
                            \once \override Score.TimeSignature.color = #(x11-color 'blue)               %! EXPLICIT_TIME_SIGNATURE_COLOR:SM6
                            \newSpacingSection                                                           %! SEGMENT:SPACING:HSS1
                            \set Score.proportionalNotationDuration = #(ly:make-moment 1 24)             %! SEGMENT:SPACING:HSS1
                            s1 * 3/8
                            ^ \markup {                                                                  %! SEGMENT:SPACING_MARKUP:HSS2
                                \with-color                                                              %! SEGMENT:SPACING_MARKUP:HSS2
                                    #(x11-color 'DarkCyan)                                               %! SEGMENT:SPACING_MARKUP:HSS2
                                    \fontsize                                                            %! SEGMENT:SPACING_MARKUP:HSS2
                                        #-3                                                              %! SEGMENT:SPACING_MARKUP:HSS2
                                        (1/24)                                                           %! SEGMENT:SPACING_MARKUP:HSS2
                                }                                                                        %! SEGMENT:SPACING_MARKUP:HSS2
                            \override Score.BarLine.transparent = ##f                                    %! SM5
                            \bar "|"                                                                     %! SM5
                <BLANKLINE>
                        }
                    >>
                    \context MusicContext = "MusicContext" <<
                        \context Staff = "MusicStaff" {
                            \context Voice = "MusicVoice" {
                                {
                                    {
                <BLANKLINE>
                                        % MusicVoice [measure 1]                                         %! SM4
                                        e'16
                                    }
                                }
                                {
                                    {
                <BLANKLINE>
                                        % MusicVoice [measure 2]                                         %! SM4
                                        fs'16
                <BLANKLINE>
                                        d'16
                <BLANKLINE>
                                        ef'16
                <BLANKLINE>
                                        f'16
                <BLANKLINE>
                                        \once \override Accidental.color = #red
                                        \once \override Beam.color = #red
                                        \once \override Dots.color = #red
                                        \once \override NoteHead.color = #red
                                        \once \override Stem.color = #red
                                        a'16
                                        - \tweak color #red                                              %! SM14
                                        ^ \markup { @ }                                                  %! SM14
                <BLANKLINE>
                                        \once \override Accidental.color = #red
                                        \once \override Beam.color = #red
                                        \once \override Dots.color = #red
                                        \once \override NoteHead.color = #red
                                        \once \override Stem.color = #red
                                        a'16
                                        - \tweak color #red                                              %! SM14
                                        ^ \markup { @ }                                                  %! SM14
                <BLANKLINE>
                                        c'16
                                    }
                                }
                                {
                                    {
                <BLANKLINE>
                                        % MusicVoice [measure 3]                                         %! SM4
                                        b'16
                                    }
                                }
                                {
                                    {
                <BLANKLINE>
                                        % MusicVoice [measure 4]                                         %! SM4
                                        bf'16
                <BLANKLINE>
                                        g'16
                <BLANKLINE>
                                        a'16
                <BLANKLINE>
                                        \once \override Accidental.color = #red
                                        \once \override Beam.color = #red
                                        \once \override Dots.color = #red
                                        \once \override NoteHead.color = #red
                                        \once \override Stem.color = #red
                                        c''16
                                        - \tweak color #red                                              %! SM14
                                        ^ \markup { @ }                                                  %! SM14
                <BLANKLINE>
                                        \once \override Accidental.color = #red
                                        \once \override Beam.color = #red
                                        \once \override Dots.color = #red
                                        \once \override NoteHead.color = #red
                                        \once \override Stem.color = #red
                                        c'16
                                        - \tweak color #red                                              %! SM14
                                        ^ \markup { @ }                                                  %! SM14
                <BLANKLINE>
                                        f'16
                <BLANKLINE>
                                    }
                                }
                            }
                        }
                    >>
                >>

        Defaults to none.

        Set to true, false or none.

        Returns true, false or none.
        '''
        return self._color_repeat_pitch_classes

    @property
    def design_checker(self):
        r'''Gets design-checker.

        Defaults to none.

        Set to design-checker or none.

        Returns design-checker or none.
        '''
        return self._design_checker

    @property
    def dynamics(self):
        r'''Gets dynamics.

        ..  container:: example

            Reapplied dynamics color green:

            >>> maker = baca.SegmentMaker(
            ...     ignore_unpitched_notes=True,
            ...     score_template=baca.SingleStaffScoreTemplate(),
            ...     spacing_specifier=baca.minimum_width((1, 24)),
            ...     time_signatures=[(3, 8)],
            ...     )
            >>> maker(
            ...     baca.scope('MusicVoice', 1),
            ...     baca.make_notes(),
            ...     )

            >>> metadata = {}
            >>> metadata['persistent_indicators'] = {}
            >>> metadata['persistent_indicators']['MusicStaff'] = [
            ...     abjad.Momento(
            ...         context='MusicVoice',
            ...         prototype='abjad.Dynamic',
            ...         value='f',
            ...         )
            ...     ]
            >>> metadata['segment_number'] = 1
            >>> lilypond_file = maker.run(
            ...     environment='docs',
            ...     previous_metadata=metadata,
            ...     remove=[
            ...         baca.Tags.build(baca.Tags.SPACING_MARKUP),
            ...         baca.Tags.STAGE_NUMBER_MARKUP,
            ...         ],
            ...     )
            >>> block = abjad.Block(name='layout')
            >>> block.indent = 0
            >>> lilypond_file.items.insert(0, block)
            >>> abjad.show(lilypond_file, strict=89) # doctest: +SKIP

            ..  docs::

                >>> abjad.f(lilypond_file[abjad.Score], strict=89)
                \context Score = "Score" <<
                    \context GlobalContext = "GlobalContext" <<
                        \context GlobalSkips = "GlobalSkips" {
                <BLANKLINE>
                            % GlobalSkips [measure 1]                                                    %! SM4
                            \time 3/8                                                                    %! EXPLICIT_TIME_SIGNATURE:SM8
                            \mark #1                                                                     %! SM9
                            \bar ""                                                                      %! EMPTY_START_BAR:SM2
                            \once \override Score.TimeSignature.color = #(x11-color 'blue)               %! EXPLICIT_TIME_SIGNATURE_COLOR:SM6
                            \newSpacingSection                                                           %! SEGMENT:SPACING:HSS1
                            \set Score.proportionalNotationDuration = #(ly:make-moment 1 24)             %! SEGMENT:SPACING:HSS1
                            s1 * 3/8
                            \override Score.BarLine.transparent = ##f                                    %! SM5
                            \bar "|"                                                                     %! SM5
                <BLANKLINE>
                        }
                    >>
                    \context MusicContext = "MusicContext" <<
                        \context Staff = "MusicStaff" {
                            \context Voice = "MusicVoice" {
                <BLANKLINE>
                                % MusicVoice [measure 1]                                                 %! SM4
                                \once \override Staff.DynamicText.color = #(x11-color 'green4)           %! REAPPLIED_DYNAMIC_COLOR:SM6
                                c'4.
                                \f                                                                       %! REAPPLIED_DYNAMIC:SM8
                <BLANKLINE>
                            }
                        }
                    >>
                >>

        '''
        pass

    @property
    def fermata_measure_staff_line_count(self):
        r'''Gets fermata measure staff lines.

        Defaults to none.

        Set to nonnegative integer or none.

        Returns nonnegative integer or none.
        '''
        return self._fermata_measure_staff_line_count

    @property
    def final_bar_line(self):
        r'''Gets final bar line.

        ..  container:: example

            Nonlast segment sets final bar line to ``'|'`` by default:

            >>> maker = baca.SegmentMaker(
            ...     ignore_unpitched_notes=True,
            ...     score_template=baca.SingleStaffScoreTemplate(),
            ...     time_signatures=[(4, 8), (3, 8), (4, 8), (3, 8)],
            ...     )

            >>> maker(
            ...     baca.scope('MusicVoice', 1),
            ...     baca.make_even_runs(),
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
                            \bar ""                                                                      %! EMPTY_START_BAR:SM2
                            \once \override Score.TimeSignature.color = #(x11-color 'blue)               %! EXPLICIT_TIME_SIGNATURE_COLOR:SM6
                            s1 * 1/2
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
                                    c'8
                                    [
                <BLANKLINE>
                                    c'8
                <BLANKLINE>
                                    c'8
                <BLANKLINE>
                                    c'8
                                    ]
                                }
                                {
                <BLANKLINE>
                                    % MusicVoice [measure 2]                                             %! SM4
                                    c'8
                                    [
                <BLANKLINE>
                                    c'8
                <BLANKLINE>
                                    c'8
                                    ]
                                }
                                {
                <BLANKLINE>
                                    % MusicVoice [measure 3]                                             %! SM4
                                    c'8
                                    [
                <BLANKLINE>
                                    c'8
                <BLANKLINE>
                                    c'8
                <BLANKLINE>
                                    c'8
                                    ]
                                }
                                {
                <BLANKLINE>
                                    % MusicVoice [measure 4]                                             %! SM4
                                    c'8
                                    [
                <BLANKLINE>
                                    c'8
                <BLANKLINE>
                                    c'8
                                    ]
                <BLANKLINE>
                                }
                            }
                        }
                    >>
                >>

            Override nonlast segment final bar line like this:

            >>> maker = baca.SegmentMaker(
            ...     final_bar_line='||',
            ...     ignore_unpitched_notes=True,
            ...     score_template=baca.SingleStaffScoreTemplate(),
            ...     time_signatures=[(4, 8), (3, 8), (4, 8), (3, 8)],
            ...     )

            >>> maker(
            ...     baca.scope('MusicVoice', 1),
            ...     baca.make_even_runs(),
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
                            \bar ""                                                                      %! EMPTY_START_BAR:SM2
                            \once \override Score.TimeSignature.color = #(x11-color 'blue)               %! EXPLICIT_TIME_SIGNATURE_COLOR:SM6
                            s1 * 1/2
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
                            \override Score.BarLine.transparent = ##f                                    %! SM5
                            \bar "||"                                                                    %! SM5
                <BLANKLINE>
                        }
                    >>
                    \context MusicContext = "MusicContext" <<
                        \context Staff = "MusicStaff" {
                            \context Voice = "MusicVoice" {
                                {
                <BLANKLINE>
                                    % MusicVoice [measure 1]                                             %! SM4
                                    c'8
                                    [
                <BLANKLINE>
                                    c'8
                <BLANKLINE>
                                    c'8
                <BLANKLINE>
                                    c'8
                                    ]
                                }
                                {
                <BLANKLINE>
                                    % MusicVoice [measure 2]                                             %! SM4
                                    c'8
                                    [
                <BLANKLINE>
                                    c'8
                <BLANKLINE>
                                    c'8
                                    ]
                                }
                                {
                <BLANKLINE>
                                    % MusicVoice [measure 3]                                             %! SM4
                                    c'8
                                    [
                <BLANKLINE>
                                    c'8
                <BLANKLINE>
                                    c'8
                <BLANKLINE>
                                    c'8
                                    ]
                                }
                                {
                <BLANKLINE>
                                    % MusicVoice [measure 4]                                             %! SM4
                                    c'8
                                    [
                <BLANKLINE>
                                    c'8
                <BLANKLINE>
                                    c'8
                                    ]
                <BLANKLINE>
                                }
                            }
                        }
                    >>
                >>

        ..  container:: example

            Last segment in score sets final bar line to ``'|.'`` by default:

            >>> maker = baca.SegmentMaker(
            ...     ignore_unpitched_notes=True,
            ...     last_segment=True,
            ...     score_template=baca.SingleStaffScoreTemplate(),
            ...     time_signatures=[(4, 8), (3, 8), (4, 8), (3, 8)],
            ...     )

            >>> maker(
            ...     baca.scope('MusicVoice', 1),
            ...     baca.make_even_runs(),
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
                            \bar ""                                                                      %! EMPTY_START_BAR:SM2
                            \once \override Score.TimeSignature.color = #(x11-color 'blue)               %! EXPLICIT_TIME_SIGNATURE_COLOR:SM6
                            s1 * 1/2
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
                            \override Score.BarLine.transparent = ##f                                    %! SM5
                            \bar "|."                                                                    %! SM5
                <BLANKLINE>
                        }
                    >>
                    \context MusicContext = "MusicContext" <<
                        \context Staff = "MusicStaff" {
                            \context Voice = "MusicVoice" {
                                {
                <BLANKLINE>
                                    % MusicVoice [measure 1]                                             %! SM4
                                    c'8
                                    [
                <BLANKLINE>
                                    c'8
                <BLANKLINE>
                                    c'8
                <BLANKLINE>
                                    c'8
                                    ]
                                }
                                {
                <BLANKLINE>
                                    % MusicVoice [measure 2]                                             %! SM4
                                    c'8
                                    [
                <BLANKLINE>
                                    c'8
                <BLANKLINE>
                                    c'8
                                    ]
                                }
                                {
                <BLANKLINE>
                                    % MusicVoice [measure 3]                                             %! SM4
                                    c'8
                                    [
                <BLANKLINE>
                                    c'8
                <BLANKLINE>
                                    c'8
                <BLANKLINE>
                                    c'8
                                    ]
                                }
                                {
                <BLANKLINE>
                                    % MusicVoice [measure 4]                                             %! SM4
                                    c'8
                                    [
                <BLANKLINE>
                                    c'8
                <BLANKLINE>
                                    c'8
                                    ]
                <BLANKLINE>
                                }
                            }
                        }
                    >>
                >>

            Override last segment final bar line like this:

            >>> maker = baca.SegmentMaker(
            ...     final_bar_line='||',
            ...     ignore_unpitched_notes=True,
            ...     score_template=baca.SingleStaffScoreTemplate(),
            ...     time_signatures=[(4, 8), (3, 8), (4, 8), (3, 8)],
            ...     )

            >>> maker(
            ...     baca.scope('MusicVoice', 1),
            ...     baca.make_even_runs(),
            ...     )

            >>> metadata = {'segment_count': 1}
            >>> lilypond_file = maker.run(
            ...     environment='docs',
            ...     metadata=metadata,
            ...     )
            >>> abjad.show(lilypond_file, strict=89) # doctest: +SKIP

            ..  docs::

                >>> abjad.f(lilypond_file[abjad.Score], strict=89)
                \context Score = "Score" <<
                    \context GlobalContext = "GlobalContext" <<
                        \context GlobalSkips = "GlobalSkips" {
                <BLANKLINE>
                            % GlobalSkips [measure 1]                                                    %! SM4
                            \time 4/8                                                                    %! EXPLICIT_TIME_SIGNATURE:SM8
                            \bar ""                                                                      %! EMPTY_START_BAR:SM2
                            \once \override Score.TimeSignature.color = #(x11-color 'blue)               %! EXPLICIT_TIME_SIGNATURE_COLOR:SM6
                            s1 * 1/2
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
                            \override Score.BarLine.transparent = ##f                                    %! SM5
                            \bar "||"                                                                    %! SM5
                <BLANKLINE>
                        }
                    >>
                    \context MusicContext = "MusicContext" <<
                        \context Staff = "MusicStaff" {
                            \context Voice = "MusicVoice" {
                                {
                <BLANKLINE>
                                    % MusicVoice [measure 1]                                             %! SM4
                                    c'8
                                    [
                <BLANKLINE>
                                    c'8
                <BLANKLINE>
                                    c'8
                <BLANKLINE>
                                    c'8
                                    ]
                                }
                                {
                <BLANKLINE>
                                    % MusicVoice [measure 2]                                             %! SM4
                                    c'8
                                    [
                <BLANKLINE>
                                    c'8
                <BLANKLINE>
                                    c'8
                                    ]
                                }
                                {
                <BLANKLINE>
                                    % MusicVoice [measure 3]                                             %! SM4
                                    c'8
                                    [
                <BLANKLINE>
                                    c'8
                <BLANKLINE>
                                    c'8
                <BLANKLINE>
                                    c'8
                                    ]
                                }
                                {
                <BLANKLINE>
                                    % MusicVoice [measure 4]                                             %! SM4
                                    c'8
                                    [
                <BLANKLINE>
                                    c'8
                <BLANKLINE>
                                    c'8
                                    ]
                <BLANKLINE>
                                }
                            }
                        }
                    >>
                >>

        Set to bar line string or none.

        Returns bar line string or none.
        '''
        return self._final_bar_line

    @property
    def final_markup(self):
        r'''Gets final markup.

        ..  container:: example

            Sets final markup:

            >>> maker = baca.SegmentMaker(
            ...     final_bar_line='|.',
            ...     final_markup=(['Madison, WI'], ['October 2016']),
            ...     final_markup_extra_offset=(-9, -2),
            ...     ignore_unpitched_notes=True,
            ...     score_template=baca.SingleStaffScoreTemplate(),
            ...     time_signatures=[(4, 8), (3, 8), (4, 8), (3, 8)],
            ...     )

            >>> maker(
            ...     baca.scope('MusicVoice', 1),
            ...     baca.make_even_runs(),
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
                            \bar ""                                                                      %! EMPTY_START_BAR:SM2
                            \once \override Score.TimeSignature.color = #(x11-color 'blue)               %! EXPLICIT_TIME_SIGNATURE_COLOR:SM6
                            s1 * 1/2
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
                            \override Score.BarLine.transparent = ##f                                    %! SM5
                            \bar "|."                                                                    %! SM5
                <BLANKLINE>
                        }
                    >>
                    \context MusicContext = "MusicContext" <<
                        \context Staff = "MusicStaff" {
                            \context Voice = "MusicVoice" {
                                {
                <BLANKLINE>
                                    % MusicVoice [measure 1]                                             %! SM4
                                    c'8
                                    [
                <BLANKLINE>
                                    c'8
                <BLANKLINE>
                                    c'8
                <BLANKLINE>
                                    c'8
                                    ]
                                }
                                {
                <BLANKLINE>
                                    % MusicVoice [measure 2]                                             %! SM4
                                    c'8
                                    [
                <BLANKLINE>
                                    c'8
                <BLANKLINE>
                                    c'8
                                    ]
                                }
                                {
                <BLANKLINE>
                                    % MusicVoice [measure 3]                                             %! SM4
                                    c'8
                                    [
                <BLANKLINE>
                                    c'8
                <BLANKLINE>
                                    c'8
                <BLANKLINE>
                                    c'8
                                    ]
                                }
                                {
                <BLANKLINE>
                                    % MusicVoice [measure 4]                                             %! SM4
                                    c'8
                                    [
                <BLANKLINE>
                                    c'8
                <BLANKLINE>
                                    \once \override TextScript.extra-offset = #'(-9 . -2)
                                    c'8
                                    ]
                                    _ \markup {                                                          %! SCORE2
                                        \whiteout                                                        %! SCORE2
                                            \upright                                                     %! SCORE2
                                                \with-color                                              %! SCORE2
                                                    #black                                               %! SCORE2
                                                    \right-column                                        %! SCORE2
                                                        {                                                %! SCORE2
                                                            \line                                        %! SCORE2
                                                                {                                        %! SCORE2
                                                                    "Madison, WI"                        %! SCORE2
                                                                }                                        %! SCORE2
                                                            \line                                        %! SCORE2
                                                                {                                        %! SCORE2
                                                                    "October 2016"                       %! SCORE2
                                                                }                                        %! SCORE2
                                                        }                                                %! SCORE2
                                        }                                                                %! SCORE2
                <BLANKLINE>
                                }
                            }
                        }
                    >>
                >>

        Defaults to none.

        Set to markup or none.

        Returns markup or none.
        '''
        return self._final_markup

    @property
    def final_markup_extra_offset(self):
        r'''Gets final markup extra offset.

        See example for final markup, above.

        Defaults to none.

        Set to pair or none.

        Returns pair or none.
        '''
        return self._final_markup_extra_offset

    @property
    def first_segment(self):
        r'''Is true when segment is first in score.

        Returns true or false.
        '''
        return self._get_segment_number() == 1

    @property
    def ignore_repeat_pitch_classes(self):
        r'''Is true when segment ignores repeat pitch-classes.

        Defaults to none.

        Set to true, false or none.

        Returns true, false or none.
        '''
        return self._ignore_repeat_pitch_classes

    @property
    def ignore_unpitched_notes(self):
        r'''Is true when segment ignores unpitched notes.

        ..  container:: example

            Ignores unpitched notes:

            >>> maker = baca.SegmentMaker(
            ...     ignore_unpitched_notes=True,
            ...     score_template=baca.SingleStaffScoreTemplate(),
            ...     time_signatures=[(4, 8), (3, 8), (4, 8), (3, 8)],
            ...     )

            >>> maker(
            ...     baca.scope('MusicVoice', 1),
            ...     baca.make_even_runs(),
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
                            \bar ""                                                                      %! EMPTY_START_BAR:SM2
                            \once \override Score.TimeSignature.color = #(x11-color 'blue)               %! EXPLICIT_TIME_SIGNATURE_COLOR:SM6
                            s1 * 1/2
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
                                    c'8
                                    [
                <BLANKLINE>
                                    c'8
                <BLANKLINE>
                                    c'8
                <BLANKLINE>
                                    c'8
                                    ]
                                }
                                {
                <BLANKLINE>
                                    % MusicVoice [measure 2]                                             %! SM4
                                    c'8
                                    [
                <BLANKLINE>
                                    c'8
                <BLANKLINE>
                                    c'8
                                    ]
                                }
                                {
                <BLANKLINE>
                                    % MusicVoice [measure 3]                                             %! SM4
                                    c'8
                                    [
                <BLANKLINE>
                                    c'8
                <BLANKLINE>
                                    c'8
                <BLANKLINE>
                                    c'8
                                    ]
                                }
                                {
                <BLANKLINE>
                                    % MusicVoice [measure 4]                                             %! SM4
                                    c'8
                                    [
                <BLANKLINE>
                                    c'8
                <BLANKLINE>
                                    c'8
                                    ]
                <BLANKLINE>
                                }
                            }
                        }
                    >>
                >>

        ..  container:: example

            Colors unpitched notes:

            >>> maker = baca.SegmentMaker(
            ...     score_template=baca.SingleStaffScoreTemplate(),
            ...     time_signatures=[(4, 8), (3, 8), (4, 8), (3, 8)],
            ...     )

            >>> maker(
            ...     baca.scope('MusicVoice', 1),
            ...     baca.make_even_runs(),
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
                            \bar ""                                                                      %! EMPTY_START_BAR:SM2
                            \once \override Score.TimeSignature.color = #(x11-color 'blue)               %! EXPLICIT_TIME_SIGNATURE_COLOR:SM6
                            s1 * 1/2
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
                                    \once \override Accidental.color = #blue                             %! SM24
                                    \once \override Beam.color = #blue                                   %! SM24
                                    \once \override Dots.color = #blue                                   %! SM24
                                    \once \override Flag.color = #blue                                   %! SM24
                                    \once \override NoteHead.color = #blue                               %! SM24
                                    \once \override Stem.color = #blue                                   %! SM24
                                    c'8
                                    [
                <BLANKLINE>
                                    \once \override Accidental.color = #blue                             %! SM24
                                    \once \override Beam.color = #blue                                   %! SM24
                                    \once \override Dots.color = #blue                                   %! SM24
                                    \once \override Flag.color = #blue                                   %! SM24
                                    \once \override NoteHead.color = #blue                               %! SM24
                                    \once \override Stem.color = #blue                                   %! SM24
                                    c'8
                <BLANKLINE>
                                    \once \override Accidental.color = #blue                             %! SM24
                                    \once \override Beam.color = #blue                                   %! SM24
                                    \once \override Dots.color = #blue                                   %! SM24
                                    \once \override Flag.color = #blue                                   %! SM24
                                    \once \override NoteHead.color = #blue                               %! SM24
                                    \once \override Stem.color = #blue                                   %! SM24
                                    c'8
                <BLANKLINE>
                                    \once \override Accidental.color = #blue                             %! SM24
                                    \once \override Beam.color = #blue                                   %! SM24
                                    \once \override Dots.color = #blue                                   %! SM24
                                    \once \override Flag.color = #blue                                   %! SM24
                                    \once \override NoteHead.color = #blue                               %! SM24
                                    \once \override Stem.color = #blue                                   %! SM24
                                    c'8
                                    ]
                                }
                                {
                <BLANKLINE>
                                    % MusicVoice [measure 2]                                             %! SM4
                                    \once \override Accidental.color = #blue                             %! SM24
                                    \once \override Beam.color = #blue                                   %! SM24
                                    \once \override Dots.color = #blue                                   %! SM24
                                    \once \override Flag.color = #blue                                   %! SM24
                                    \once \override NoteHead.color = #blue                               %! SM24
                                    \once \override Stem.color = #blue                                   %! SM24
                                    c'8
                                    [
                <BLANKLINE>
                                    \once \override Accidental.color = #blue                             %! SM24
                                    \once \override Beam.color = #blue                                   %! SM24
                                    \once \override Dots.color = #blue                                   %! SM24
                                    \once \override Flag.color = #blue                                   %! SM24
                                    \once \override NoteHead.color = #blue                               %! SM24
                                    \once \override Stem.color = #blue                                   %! SM24
                                    c'8
                <BLANKLINE>
                                    \once \override Accidental.color = #blue                             %! SM24
                                    \once \override Beam.color = #blue                                   %! SM24
                                    \once \override Dots.color = #blue                                   %! SM24
                                    \once \override Flag.color = #blue                                   %! SM24
                                    \once \override NoteHead.color = #blue                               %! SM24
                                    \once \override Stem.color = #blue                                   %! SM24
                                    c'8
                                    ]
                                }
                                {
                <BLANKLINE>
                                    % MusicVoice [measure 3]                                             %! SM4
                                    \once \override Accidental.color = #blue                             %! SM24
                                    \once \override Beam.color = #blue                                   %! SM24
                                    \once \override Dots.color = #blue                                   %! SM24
                                    \once \override Flag.color = #blue                                   %! SM24
                                    \once \override NoteHead.color = #blue                               %! SM24
                                    \once \override Stem.color = #blue                                   %! SM24
                                    c'8
                                    [
                <BLANKLINE>
                                    \once \override Accidental.color = #blue                             %! SM24
                                    \once \override Beam.color = #blue                                   %! SM24
                                    \once \override Dots.color = #blue                                   %! SM24
                                    \once \override Flag.color = #blue                                   %! SM24
                                    \once \override NoteHead.color = #blue                               %! SM24
                                    \once \override Stem.color = #blue                                   %! SM24
                                    c'8
                <BLANKLINE>
                                    \once \override Accidental.color = #blue                             %! SM24
                                    \once \override Beam.color = #blue                                   %! SM24
                                    \once \override Dots.color = #blue                                   %! SM24
                                    \once \override Flag.color = #blue                                   %! SM24
                                    \once \override NoteHead.color = #blue                               %! SM24
                                    \once \override Stem.color = #blue                                   %! SM24
                                    c'8
                <BLANKLINE>
                                    \once \override Accidental.color = #blue                             %! SM24
                                    \once \override Beam.color = #blue                                   %! SM24
                                    \once \override Dots.color = #blue                                   %! SM24
                                    \once \override Flag.color = #blue                                   %! SM24
                                    \once \override NoteHead.color = #blue                               %! SM24
                                    \once \override Stem.color = #blue                                   %! SM24
                                    c'8
                                    ]
                                }
                                {
                <BLANKLINE>
                                    % MusicVoice [measure 4]                                             %! SM4
                                    \once \override Accidental.color = #blue                             %! SM24
                                    \once \override Beam.color = #blue                                   %! SM24
                                    \once \override Dots.color = #blue                                   %! SM24
                                    \once \override Flag.color = #blue                                   %! SM24
                                    \once \override NoteHead.color = #blue                               %! SM24
                                    \once \override Stem.color = #blue                                   %! SM24
                                    c'8
                                    [
                <BLANKLINE>
                                    \once \override Accidental.color = #blue                             %! SM24
                                    \once \override Beam.color = #blue                                   %! SM24
                                    \once \override Dots.color = #blue                                   %! SM24
                                    \once \override Flag.color = #blue                                   %! SM24
                                    \once \override NoteHead.color = #blue                               %! SM24
                                    \once \override Stem.color = #blue                                   %! SM24
                                    c'8
                <BLANKLINE>
                                    \once \override Accidental.color = #blue                             %! SM24
                                    \once \override Beam.color = #blue                                   %! SM24
                                    \once \override Dots.color = #blue                                   %! SM24
                                    \once \override Flag.color = #blue                                   %! SM24
                                    \once \override NoteHead.color = #blue                               %! SM24
                                    \once \override Stem.color = #blue                                   %! SM24
                                    c'8
                                    ]
                <BLANKLINE>
                                }
                            }
                        }
                    >>
                >>

        Defaults to none.

        Set to true, false or none.

        Returns true, false or none.
        '''
        return self._ignore_unpitched_notes

    @property
    def ignore_unregistered_pitches(self):
        r'''Is true when segment ignores unregistered pitches.

        ..  container:: example

            Ignores unregistered pitches:

                >>> music_maker = baca.MusicMaker(
                ...     baca.PitchFirstRhythmCommand(
                ...         rhythm_maker=baca.PitchFirstRhythmMaker(
                ...             acciaccatura_specifiers=[
                ...                 baca.AcciaccaturaSpecifier(),
                ...                 ],
                ...             talea=rhythmos.Talea(
                ...                 counts=[3],
                ...                 denominator=16,
                ...                 ),
                ...             ),
                ...         ),
                ...     color_unregistered_pitches=True,
                ...     denominator=8,
                ...     )

            >>> collection_lists = [
            ...     [[4]],
            ...     [[6, 2, 3, 5, 9, 8, 0]],
            ...     [[11]],
            ...     [[10, 7, 9, 8, 0, 5]],
            ...     ]
            >>> figures, time_signatures = [], []
            >>> for collections in collection_lists:
            ...     contribution = music_maker('Voice 1', collections)
            ...     figures.append(contribution['Voice 1'])
            ...     time_signatures.append(contribution.time_signature)
            ...
            >>> figures_ = []
            >>> for figure in figures:
            ...     figures_.extend(figure)
            ...
            >>> figures = abjad.select(figures_)

            >>> maker = baca.SegmentMaker(
            ...     ignore_unregistered_pitches=True,
            ...     score_template=baca.SingleStaffScoreTemplate(),
            ...     spacing_specifier=baca.minimum_width((1, 24)),
            ...     time_signatures=time_signatures,
            ...     )
            >>> maker(
            ...     baca.scope('MusicVoice', 1),
            ...     baca.rhythm(figures),
            ...     )

            >>> lilypond_file = maker.run(environment='docs')
            >>> score = lilypond_file[abjad.Score]
            >>> abjad.override(score).spacing_spanner.strict_grace_spacing = False
            >>> abjad.override(score).spacing_spanner.strict_note_spacing = False
            >>> abjad.show(lilypond_file, strict=89) # doctest: +SKIP

            ..  docs::

                >>> abjad.f(lilypond_file[abjad.Score], strict=89)
                \context Score = "Score" \with {
                    \override SpacingSpanner.strict-grace-spacing = ##f
                    \override SpacingSpanner.strict-note-spacing = ##f
                } <<
                    \context GlobalContext = "GlobalContext" <<
                        \context GlobalSkips = "GlobalSkips" {
                <BLANKLINE>
                            % GlobalSkips [measure 1]                                                    %! SM4
                            \time 3/16                                                                   %! EXPLICIT_TIME_SIGNATURE:SM8
                            \bar ""                                                                      %! EMPTY_START_BAR:SM2
                            \once \override Score.TimeSignature.color = #(x11-color 'blue)               %! EXPLICIT_TIME_SIGNATURE_COLOR:SM6
                            \newSpacingSection                                                           %! SEGMENT:SPACING:HSS1
                            \set Score.proportionalNotationDuration = #(ly:make-moment 1 24)             %! SEGMENT:SPACING:HSS1
                            s1 * 3/16
                            ^ \markup {
                                \column
                                    {
                                        \line                                                            %! STAGE_NUMBER_MARKUP:SM3
                                            {                                                            %! STAGE_NUMBER_MARKUP:SM3
                                                \fontsize                                                %! STAGE_NUMBER_MARKUP:SM3
                                                    #-3                                                  %! STAGE_NUMBER_MARKUP:SM3
                                                    \with-color                                          %! STAGE_NUMBER_MARKUP:SM3
                                                        #(x11-color 'DarkCyan)                           %! STAGE_NUMBER_MARKUP:SM3
                                                        [1]                                              %! STAGE_NUMBER_MARKUP:SM3
                                            }                                                            %! STAGE_NUMBER_MARKUP:SM3
                                        \line                                                            %! SEGMENT:SPACING_MARKUP:HSS2
                                            {                                                            %! SEGMENT:SPACING_MARKUP:HSS2
                                                \with-color                                              %! SEGMENT:SPACING_MARKUP:HSS2
                                                    #(x11-color 'DarkCyan)                               %! SEGMENT:SPACING_MARKUP:HSS2
                                                    \fontsize                                            %! SEGMENT:SPACING_MARKUP:HSS2
                                                        #-3                                              %! SEGMENT:SPACING_MARKUP:HSS2
                                                        (1/24)                                           %! SEGMENT:SPACING_MARKUP:HSS2
                                            }                                                            %! SEGMENT:SPACING_MARKUP:HSS2
                                    }
                                }
                <BLANKLINE>
                            % GlobalSkips [measure 2]                                                    %! SM4
                            \once \override Score.TimeSignature.color = #(x11-color 'DeepPink1)          %! REDUNDANT_TIME_SIGNATURE_COLOR:SM6
                            \newSpacingSection                                                           %! SEGMENT:SPACING:HSS1
                            \set Score.proportionalNotationDuration = #(ly:make-moment 1 24)             %! SEGMENT:SPACING:HSS1
                            s1 * 3/16
                            ^ \markup {                                                                  %! SEGMENT:SPACING_MARKUP:HSS2
                                \with-color                                                              %! SEGMENT:SPACING_MARKUP:HSS2
                                    #(x11-color 'DarkCyan)                                               %! SEGMENT:SPACING_MARKUP:HSS2
                                    \fontsize                                                            %! SEGMENT:SPACING_MARKUP:HSS2
                                        #-3                                                              %! SEGMENT:SPACING_MARKUP:HSS2
                                        (1/24)                                                           %! SEGMENT:SPACING_MARKUP:HSS2
                                }                                                                        %! SEGMENT:SPACING_MARKUP:HSS2
                <BLANKLINE>
                            % GlobalSkips [measure 3]                                                    %! SM4
                            \once \override Score.TimeSignature.color = #(x11-color 'DeepPink1)          %! REDUNDANT_TIME_SIGNATURE_COLOR:SM6
                            \newSpacingSection                                                           %! SEGMENT:SPACING:HSS1
                            \set Score.proportionalNotationDuration = #(ly:make-moment 1 24)             %! SEGMENT:SPACING:HSS1
                            s1 * 3/16
                            ^ \markup {                                                                  %! SEGMENT:SPACING_MARKUP:HSS2
                                \with-color                                                              %! SEGMENT:SPACING_MARKUP:HSS2
                                    #(x11-color 'DarkCyan)                                               %! SEGMENT:SPACING_MARKUP:HSS2
                                    \fontsize                                                            %! SEGMENT:SPACING_MARKUP:HSS2
                                        #-3                                                              %! SEGMENT:SPACING_MARKUP:HSS2
                                        (1/24)                                                           %! SEGMENT:SPACING_MARKUP:HSS2
                                }                                                                        %! SEGMENT:SPACING_MARKUP:HSS2
                <BLANKLINE>
                            % GlobalSkips [measure 4]                                                    %! SM4
                            \once \override Score.TimeSignature.color = #(x11-color 'DeepPink1)          %! REDUNDANT_TIME_SIGNATURE_COLOR:SM6
                            \newSpacingSection                                                           %! SEGMENT:SPACING:HSS1
                            \set Score.proportionalNotationDuration = #(ly:make-moment 1 24)             %! SEGMENT:SPACING:HSS1
                            s1 * 3/16
                            ^ \markup {                                                                  %! SEGMENT:SPACING_MARKUP:HSS2
                                \with-color                                                              %! SEGMENT:SPACING_MARKUP:HSS2
                                    #(x11-color 'DarkCyan)                                               %! SEGMENT:SPACING_MARKUP:HSS2
                                    \fontsize                                                            %! SEGMENT:SPACING_MARKUP:HSS2
                                        #-3                                                              %! SEGMENT:SPACING_MARKUP:HSS2
                                        (1/24)                                                           %! SEGMENT:SPACING_MARKUP:HSS2
                                }                                                                        %! SEGMENT:SPACING_MARKUP:HSS2
                            \override Score.BarLine.transparent = ##f                                    %! SM5
                            \bar "|"                                                                     %! SM5
                <BLANKLINE>
                        }
                    >>
                    \context MusicContext = "MusicContext" <<
                        \context Staff = "MusicStaff" {
                            \context Voice = "MusicVoice" {
                                {
                                    {
                <BLANKLINE>
                                        % MusicVoice [measure 1]                                         %! SM4
                                        e'8.
                                    }
                                }
                                {
                                    {
                <BLANKLINE>
                                        % MusicVoice [measure 2]                                         %! SM4
                                        \acciaccatura {
                <BLANKLINE>
                                            fs'16 [
                <BLANKLINE>
                                            d'16
                <BLANKLINE>
                                            ef'16
                <BLANKLINE>
                                            f'16
                <BLANKLINE>
                                            a'16
                <BLANKLINE>
                                            af'16 ]
                <BLANKLINE>
                                        }
                                        c'8.
                                    }
                                }
                                {
                                    {
                <BLANKLINE>
                                        % MusicVoice [measure 3]                                         %! SM4
                                        b'8.
                                    }
                                }
                                {
                                    {
                <BLANKLINE>
                                        % MusicVoice [measure 4]                                         %! SM4
                                        \acciaccatura {
                <BLANKLINE>
                                            bf'16 [
                <BLANKLINE>
                                            g'16
                <BLANKLINE>
                                            a'16
                <BLANKLINE>
                                            af'16
                <BLANKLINE>
                                            c'16 ]
                <BLANKLINE>
                                        }
                                        f'8.
                <BLANKLINE>
                                    }
                                }
                            }
                        }
                    >>
                >>

        ..  container:: example

            Colors unregistered pitches:

                >>> music_maker = baca.MusicMaker(
                ...     baca.PitchFirstRhythmCommand(
                ...         rhythm_maker=baca.PitchFirstRhythmMaker(
                ...             acciaccatura_specifiers=[
                ...                 baca.AcciaccaturaSpecifier(),
                ...                 ],
                ...             talea=rhythmos.Talea(
                ...                 counts=[3],
                ...                 denominator=16,
                ...                 ),
                ...             ),
                ...         ),
                ...     color_unregistered_pitches=True,
                ...     denominator=8,
                ...     )

            >>> collection_lists = [
            ...     [[4]],
            ...     [[6, 2, 3, 5, 9, 8, 0]],
            ...     [[11]],
            ...     [[10, 7, 9, 8, 0, 5]],
            ...     ]
            >>> figures, time_signatures = [], []
            >>> for collections in collection_lists:
            ...     contribution = music_maker('Voice 1', collections)
            ...     figures.append(contribution['Voice 1'])
            ...     time_signatures.append(contribution.time_signature)
            ...
            >>> figures_ = []
            >>> for figure in figures:
            ...     figures_.extend(figure)
            ...
            >>> figures = abjad.select(figures_)

            >>> maker = baca.SegmentMaker(
            ...     score_template=baca.SingleStaffScoreTemplate(),
            ...     spacing_specifier=baca.minimum_width((1, 24)),
            ...     time_signatures=time_signatures,
            ...     )
            >>> maker(
            ...     baca.scope('MusicVoice', 1),
            ...     baca.rhythm(figures),
            ...     )

            >>> lilypond_file = maker.run(environment='docs')
            >>> score = lilypond_file[abjad.Score]
            >>> abjad.override(score).spacing_spanner.strict_grace_spacing = False
            >>> abjad.override(score).spacing_spanner.strict_note_spacing = False
            >>> abjad.show(lilypond_file, strict=89) # doctest: +SKIP

            ..  docs::

                >>> abjad.f(lilypond_file[abjad.Score], strict=89)
                \context Score = "Score" \with {
                    \override SpacingSpanner.strict-grace-spacing = ##f
                    \override SpacingSpanner.strict-note-spacing = ##f
                } <<
                    \context GlobalContext = "GlobalContext" <<
                        \context GlobalSkips = "GlobalSkips" {
                <BLANKLINE>
                            % GlobalSkips [measure 1]                                                    %! SM4
                            \time 3/16                                                                   %! EXPLICIT_TIME_SIGNATURE:SM8
                            \bar ""                                                                      %! EMPTY_START_BAR:SM2
                            \once \override Score.TimeSignature.color = #(x11-color 'blue)               %! EXPLICIT_TIME_SIGNATURE_COLOR:SM6
                            \newSpacingSection                                                           %! SEGMENT:SPACING:HSS1
                            \set Score.proportionalNotationDuration = #(ly:make-moment 1 24)             %! SEGMENT:SPACING:HSS1
                            s1 * 3/16
                            ^ \markup {
                                \column
                                    {
                                        \line                                                            %! STAGE_NUMBER_MARKUP:SM3
                                            {                                                            %! STAGE_NUMBER_MARKUP:SM3
                                                \fontsize                                                %! STAGE_NUMBER_MARKUP:SM3
                                                    #-3                                                  %! STAGE_NUMBER_MARKUP:SM3
                                                    \with-color                                          %! STAGE_NUMBER_MARKUP:SM3
                                                        #(x11-color 'DarkCyan)                           %! STAGE_NUMBER_MARKUP:SM3
                                                        [1]                                              %! STAGE_NUMBER_MARKUP:SM3
                                            }                                                            %! STAGE_NUMBER_MARKUP:SM3
                                        \line                                                            %! SEGMENT:SPACING_MARKUP:HSS2
                                            {                                                            %! SEGMENT:SPACING_MARKUP:HSS2
                                                \with-color                                              %! SEGMENT:SPACING_MARKUP:HSS2
                                                    #(x11-color 'DarkCyan)                               %! SEGMENT:SPACING_MARKUP:HSS2
                                                    \fontsize                                            %! SEGMENT:SPACING_MARKUP:HSS2
                                                        #-3                                              %! SEGMENT:SPACING_MARKUP:HSS2
                                                        (1/24)                                           %! SEGMENT:SPACING_MARKUP:HSS2
                                            }                                                            %! SEGMENT:SPACING_MARKUP:HSS2
                                    }
                                }
                <BLANKLINE>
                            % GlobalSkips [measure 2]                                                    %! SM4
                            \once \override Score.TimeSignature.color = #(x11-color 'DeepPink1)          %! REDUNDANT_TIME_SIGNATURE_COLOR:SM6
                            \newSpacingSection                                                           %! SEGMENT:SPACING:HSS1
                            \set Score.proportionalNotationDuration = #(ly:make-moment 1 24)             %! SEGMENT:SPACING:HSS1
                            s1 * 3/16
                            ^ \markup {                                                                  %! SEGMENT:SPACING_MARKUP:HSS2
                                \with-color                                                              %! SEGMENT:SPACING_MARKUP:HSS2
                                    #(x11-color 'DarkCyan)                                               %! SEGMENT:SPACING_MARKUP:HSS2
                                    \fontsize                                                            %! SEGMENT:SPACING_MARKUP:HSS2
                                        #-3                                                              %! SEGMENT:SPACING_MARKUP:HSS2
                                        (1/24)                                                           %! SEGMENT:SPACING_MARKUP:HSS2
                                }                                                                        %! SEGMENT:SPACING_MARKUP:HSS2
                <BLANKLINE>
                            % GlobalSkips [measure 3]                                                    %! SM4
                            \once \override Score.TimeSignature.color = #(x11-color 'DeepPink1)          %! REDUNDANT_TIME_SIGNATURE_COLOR:SM6
                            \newSpacingSection                                                           %! SEGMENT:SPACING:HSS1
                            \set Score.proportionalNotationDuration = #(ly:make-moment 1 24)             %! SEGMENT:SPACING:HSS1
                            s1 * 3/16
                            ^ \markup {                                                                  %! SEGMENT:SPACING_MARKUP:HSS2
                                \with-color                                                              %! SEGMENT:SPACING_MARKUP:HSS2
                                    #(x11-color 'DarkCyan)                                               %! SEGMENT:SPACING_MARKUP:HSS2
                                    \fontsize                                                            %! SEGMENT:SPACING_MARKUP:HSS2
                                        #-3                                                              %! SEGMENT:SPACING_MARKUP:HSS2
                                        (1/24)                                                           %! SEGMENT:SPACING_MARKUP:HSS2
                                }                                                                        %! SEGMENT:SPACING_MARKUP:HSS2
                <BLANKLINE>
                            % GlobalSkips [measure 4]                                                    %! SM4
                            \once \override Score.TimeSignature.color = #(x11-color 'DeepPink1)          %! REDUNDANT_TIME_SIGNATURE_COLOR:SM6
                            \newSpacingSection                                                           %! SEGMENT:SPACING:HSS1
                            \set Score.proportionalNotationDuration = #(ly:make-moment 1 24)             %! SEGMENT:SPACING:HSS1
                            s1 * 3/16
                            ^ \markup {                                                                  %! SEGMENT:SPACING_MARKUP:HSS2
                                \with-color                                                              %! SEGMENT:SPACING_MARKUP:HSS2
                                    #(x11-color 'DarkCyan)                                               %! SEGMENT:SPACING_MARKUP:HSS2
                                    \fontsize                                                            %! SEGMENT:SPACING_MARKUP:HSS2
                                        #-3                                                              %! SEGMENT:SPACING_MARKUP:HSS2
                                        (1/24)                                                           %! SEGMENT:SPACING_MARKUP:HSS2
                                }                                                                        %! SEGMENT:SPACING_MARKUP:HSS2
                            \override Score.BarLine.transparent = ##f                                    %! SM5
                            \bar "|"                                                                     %! SM5
                <BLANKLINE>
                        }
                    >>
                    \context MusicContext = "MusicContext" <<
                        \context Staff = "MusicStaff" {
                            \context Voice = "MusicVoice" {
                                {
                                    {
                <BLANKLINE>
                                        % MusicVoice [measure 1]                                         %! SM4
                                        \once \override Accidental.color = #magenta                      %! SM25
                                        \once \override Beam.color = #magenta                            %! SM25
                                        \once \override Dots.color = #magenta                            %! SM25
                                        \once \override Flag.color = #magenta                            %! SM25
                                        \once \override NoteHead.color = #magenta                        %! SM25
                                        \once \override Stem.color = #magenta                            %! SM25
                                        e'8.
                                    }
                                }
                                {
                                    {
                <BLANKLINE>
                                        % MusicVoice [measure 2]                                         %! SM4
                                        \acciaccatura {
                <BLANKLINE>
                                            \once \override Accidental.color = #magenta                  %! SM25
                                            \once \override Beam.color = #magenta                        %! SM25
                                            \once \override Dots.color = #magenta                        %! SM25
                                            \once \override Flag.color = #magenta                        %! SM25
                                            \once \override NoteHead.color = #magenta                    %! SM25
                                            \once \override Stem.color = #magenta                        %! SM25
                                            fs'16 [
                <BLANKLINE>
                                            \once \override Accidental.color = #magenta                  %! SM25
                                            \once \override Beam.color = #magenta                        %! SM25
                                            \once \override Dots.color = #magenta                        %! SM25
                                            \once \override Flag.color = #magenta                        %! SM25
                                            \once \override NoteHead.color = #magenta                    %! SM25
                                            \once \override Stem.color = #magenta                        %! SM25
                                            d'16
                <BLANKLINE>
                                            \once \override Accidental.color = #magenta                  %! SM25
                                            \once \override Beam.color = #magenta                        %! SM25
                                            \once \override Dots.color = #magenta                        %! SM25
                                            \once \override Flag.color = #magenta                        %! SM25
                                            \once \override NoteHead.color = #magenta                    %! SM25
                                            \once \override Stem.color = #magenta                        %! SM25
                                            ef'16
                <BLANKLINE>
                                            \once \override Accidental.color = #magenta                  %! SM25
                                            \once \override Beam.color = #magenta                        %! SM25
                                            \once \override Dots.color = #magenta                        %! SM25
                                            \once \override Flag.color = #magenta                        %! SM25
                                            \once \override NoteHead.color = #magenta                    %! SM25
                                            \once \override Stem.color = #magenta                        %! SM25
                                            f'16
                <BLANKLINE>
                                            \once \override Accidental.color = #magenta                  %! SM25
                                            \once \override Beam.color = #magenta                        %! SM25
                                            \once \override Dots.color = #magenta                        %! SM25
                                            \once \override Flag.color = #magenta                        %! SM25
                                            \once \override NoteHead.color = #magenta                    %! SM25
                                            \once \override Stem.color = #magenta                        %! SM25
                                            a'16
                <BLANKLINE>
                                            \once \override Accidental.color = #magenta                  %! SM25
                                            \once \override Beam.color = #magenta                        %! SM25
                                            \once \override Dots.color = #magenta                        %! SM25
                                            \once \override Flag.color = #magenta                        %! SM25
                                            \once \override NoteHead.color = #magenta                    %! SM25
                                            \once \override Stem.color = #magenta                        %! SM25
                                            af'16 ]
                <BLANKLINE>
                                        }
                                        \once \override Accidental.color = #magenta                      %! SM25
                                        \once \override Beam.color = #magenta                            %! SM25
                                        \once \override Dots.color = #magenta                            %! SM25
                                        \once \override Flag.color = #magenta                            %! SM25
                                        \once \override NoteHead.color = #magenta                        %! SM25
                                        \once \override Stem.color = #magenta                            %! SM25
                                        c'8.
                                    }
                                }
                                {
                                    {
                <BLANKLINE>
                                        % MusicVoice [measure 3]                                         %! SM4
                                        \once \override Accidental.color = #magenta                      %! SM25
                                        \once \override Beam.color = #magenta                            %! SM25
                                        \once \override Dots.color = #magenta                            %! SM25
                                        \once \override Flag.color = #magenta                            %! SM25
                                        \once \override NoteHead.color = #magenta                        %! SM25
                                        \once \override Stem.color = #magenta                            %! SM25
                                        b'8.
                                    }
                                }
                                {
                                    {
                <BLANKLINE>
                                        % MusicVoice [measure 4]                                         %! SM4
                                        \acciaccatura {
                <BLANKLINE>
                                            \once \override Accidental.color = #magenta                  %! SM25
                                            \once \override Beam.color = #magenta                        %! SM25
                                            \once \override Dots.color = #magenta                        %! SM25
                                            \once \override Flag.color = #magenta                        %! SM25
                                            \once \override NoteHead.color = #magenta                    %! SM25
                                            \once \override Stem.color = #magenta                        %! SM25
                                            bf'16 [
                <BLANKLINE>
                                            \once \override Accidental.color = #magenta                  %! SM25
                                            \once \override Beam.color = #magenta                        %! SM25
                                            \once \override Dots.color = #magenta                        %! SM25
                                            \once \override Flag.color = #magenta                        %! SM25
                                            \once \override NoteHead.color = #magenta                    %! SM25
                                            \once \override Stem.color = #magenta                        %! SM25
                                            g'16
                <BLANKLINE>
                                            \once \override Accidental.color = #magenta                  %! SM25
                                            \once \override Beam.color = #magenta                        %! SM25
                                            \once \override Dots.color = #magenta                        %! SM25
                                            \once \override Flag.color = #magenta                        %! SM25
                                            \once \override NoteHead.color = #magenta                    %! SM25
                                            \once \override Stem.color = #magenta                        %! SM25
                                            a'16
                <BLANKLINE>
                                            \once \override Accidental.color = #magenta                  %! SM25
                                            \once \override Beam.color = #magenta                        %! SM25
                                            \once \override Dots.color = #magenta                        %! SM25
                                            \once \override Flag.color = #magenta                        %! SM25
                                            \once \override NoteHead.color = #magenta                    %! SM25
                                            \once \override Stem.color = #magenta                        %! SM25
                                            af'16
                <BLANKLINE>
                                            \once \override Accidental.color = #magenta                  %! SM25
                                            \once \override Beam.color = #magenta                        %! SM25
                                            \once \override Dots.color = #magenta                        %! SM25
                                            \once \override Flag.color = #magenta                        %! SM25
                                            \once \override NoteHead.color = #magenta                    %! SM25
                                            \once \override Stem.color = #magenta                        %! SM25
                                            c'16 ]
                <BLANKLINE>
                                        }
                                        \once \override Accidental.color = #magenta                      %! SM25
                                        \once \override Beam.color = #magenta                            %! SM25
                                        \once \override Dots.color = #magenta                            %! SM25
                                        \once \override Flag.color = #magenta                            %! SM25
                                        \once \override NoteHead.color = #magenta                        %! SM25
                                        \once \override Stem.color = #magenta                            %! SM25
                                        f'8.
                <BLANKLINE>
                                    }
                                }
                            }
                        }
                    >>
                >>

        Defaults to none.

        Set to true, false or none.

        Returns true, false or none.
        '''
        return self._ignore_unregistered_pitches

    @property
    def instruments(self):
        r'''Gets instruments.

        ..  container:: example

            >>> instruments = abjad.InstrumentDictionary()
            >>> instruments['Flute'] = abjad.Flute()
            >>> instruments['Piccolo'] = abjad.Piccolo()
            >>> layout_measure_map = baca.layout(
            ...     baca.page(
            ...         [1, 0, (11,)],
            ...         [5, 25, (11,)],
            ...         [9, 50, (7,)],
            ...         ),
            ...     )
            >>> remove = [
            ...     baca.Tags.build(baca.Tags.SPACING_MARKUP),
            ...     baca.Tags.STAGE_NUMBER_MARKUP,
            ...     ]

        ..  container:: example

            Default instruments color purple and redraw dull purple:

            >>> layout_measure_map_ = baca.layout(
            ...     baca.page(
            ...         [1, 0, (11,)],
            ...         [2, 20, (11,)],
            ...         ),
            ...     )
            >>> score_template = baca.SingleStaffScoreTemplate()
            >>> triple = ('MusicStaff', 'default_instrument', abjad.Flute())
            >>> score_template.defaults.append(triple)
            >>> maker = baca.SegmentMaker(
            ...     ignore_unpitched_notes=True,
            ...     instruments=instruments,
            ...     layout_measure_map=layout_measure_map_,
            ...     score_template=score_template,
            ...     spacing_specifier=baca.minimum_width((1, 24)),
            ...     time_signatures=[(3, 8), (3, 8)],
            ...     )
            >>> maker(
            ...     baca.scope('MusicVoice', 1),
            ...     baca.make_notes(),
            ...     )

            >>> lilypond_file = maker.run(
            ...     environment='docs',
            ...     remove=remove,
            ...     )
            >>> block = abjad.Block(name='layout')
            >>> block.indent = 0
            >>> lilypond_file.items.insert(0, block)
            >>> abjad.show(lilypond_file, strict=89) # doctest: +SKIP

            ..  docs::

                >>> abjad.f(lilypond_file[abjad.Score], strict=89)
                \context Score = "Score" <<
                    \context GlobalContext = "GlobalContext" <<
                        \context GlobalSkips = "GlobalSkips" {
                <BLANKLINE>
                            % GlobalSkips [measure 1]                                                    %! SM4
                            \autoPageBreaksOff                                                           %! SEGMENT:LAYOUT:LMM1
                            \noBreak                                                                     %! SEGMENT:LAYOUT:LMM2
                            \overrideProperty Score.NonMusicalPaperColumn.line-break-system-details      %! SEGMENT:LAYOUT:LMM3
                            #'((Y-offset . 0) (alignment-distances . (11)))                              %! SEGMENT:LAYOUT:LMM3
                            \time 3/8                                                                    %! EXPLICIT_TIME_SIGNATURE:SM8
                            \bar ""                                                                      %! EMPTY_START_BAR:SM2
                            \once \override Score.TimeSignature.color = #(x11-color 'blue)               %! EXPLICIT_TIME_SIGNATURE_COLOR:SM6
                            \newSpacingSection                                                           %! SEGMENT:SPACING:HSS1
                            \set Score.proportionalNotationDuration = #(ly:make-moment 1 24)             %! SEGMENT:SPACING:HSS1
                            \pageBreak                                                                   %! SEGMENT:LAYOUT:LMM3
                            s1 * 3/8
                <BLANKLINE>
                            % GlobalSkips [measure 2]                                                    %! SM4
                            \noBreak                                                                     %! SEGMENT:LAYOUT:LMM2
                            \overrideProperty Score.NonMusicalPaperColumn.line-break-system-details      %! SEGMENT:LAYOUT:LMM3
                            #'((Y-offset . 20) (alignment-distances . (11)))                             %! SEGMENT:LAYOUT:LMM3
                            \once \override Score.TimeSignature.color = #(x11-color 'DeepPink1)          %! REDUNDANT_TIME_SIGNATURE_COLOR:SM6
                            \newSpacingSection                                                           %! SEGMENT:SPACING:HSS1
                            \set Score.proportionalNotationDuration = #(ly:make-moment 1 24)             %! SEGMENT:SPACING:HSS1
                            \break                                                                       %! SEGMENT:LAYOUT:LMM3
                            s1 * 3/8
                            \override Score.BarLine.transparent = ##f                                    %! SM5
                            \bar "|"                                                                     %! SM5
                <BLANKLINE>
                        }
                    >>
                    \context MusicContext = "MusicContext" <<
                        \context Staff = "MusicStaff" {
                            \context Voice = "MusicVoice" {
                <BLANKLINE>
                                % MusicVoice [measure 1]                                                 %! SM4
                                \set Staff.instrumentName = \markup { Flute }                            %! DEFAULT_INSTRUMENT:SM8
                                \set Staff.shortInstrumentName = \markup { Fl. }                         %! DEFAULT_INSTRUMENT:SM8
                                \once \override Staff.InstrumentName.color = #(x11-color 'DarkViolet)    %! DEFAULT_INSTRUMENT_COLOR:SM6
                                c'4.
                                ^ \markup {
                                    \column
                                        {
                                            %%% \line                                                    %! DEFAULT_INSTRUMENT_ALERT:SM10
                                            %%%     {                                                    %! DEFAULT_INSTRUMENT_ALERT:SM10
                                            %%%         \vcenter                                         %! DEFAULT_INSTRUMENT_ALERT:SM10
                                            %%%             (“Flute”                                     %! DEFAULT_INSTRUMENT_ALERT:SM10
                                            %%%         \vcenter                                         %! DEFAULT_INSTRUMENT_ALERT:SM10
                                            %%%             Flute                                        %! DEFAULT_INSTRUMENT_ALERT:SM10
                                            %%%         \concat                                          %! DEFAULT_INSTRUMENT_ALERT:SM10
                                            %%%             {                                            %! DEFAULT_INSTRUMENT_ALERT:SM10
                                            %%%                 \vcenter                                 %! DEFAULT_INSTRUMENT_ALERT:SM10
                                            %%%                     Fl.                                  %! DEFAULT_INSTRUMENT_ALERT:SM10
                                            %%%                 \vcenter                                 %! DEFAULT_INSTRUMENT_ALERT:SM10
                                            %%%                     )                                    %! DEFAULT_INSTRUMENT_ALERT:SM10
                                            %%%             }                                            %! DEFAULT_INSTRUMENT_ALERT:SM10
                                            %%%     }                                                    %! DEFAULT_INSTRUMENT_ALERT:SM10
                                            \line                                                        %! DEFAULT_INSTRUMENT_ALERT_WITH_COLOR:SM11
                                                {                                                        %! DEFAULT_INSTRUMENT_ALERT_WITH_COLOR:SM11
                                                    \with-color                                          %! DEFAULT_INSTRUMENT_ALERT_WITH_COLOR:SM11
                                                        #(x11-color 'DarkViolet)                         %! DEFAULT_INSTRUMENT_ALERT_WITH_COLOR:SM11
                                                        {                                                %! DEFAULT_INSTRUMENT_ALERT_WITH_COLOR:SM11
                                                            \vcenter                                     %! DEFAULT_INSTRUMENT_ALERT_WITH_COLOR:SM11
                                                                (“Flute”                                 %! DEFAULT_INSTRUMENT_ALERT_WITH_COLOR:SM11
                                                            \vcenter                                     %! DEFAULT_INSTRUMENT_ALERT_WITH_COLOR:SM11
                                                                Flute                                    %! DEFAULT_INSTRUMENT_ALERT_WITH_COLOR:SM11
                                                            \concat                                      %! DEFAULT_INSTRUMENT_ALERT_WITH_COLOR:SM11
                                                                {                                        %! DEFAULT_INSTRUMENT_ALERT_WITH_COLOR:SM11
                                                                    \vcenter                             %! DEFAULT_INSTRUMENT_ALERT_WITH_COLOR:SM11
                                                                        Fl.                              %! DEFAULT_INSTRUMENT_ALERT_WITH_COLOR:SM11
                                                                    \vcenter                             %! DEFAULT_INSTRUMENT_ALERT_WITH_COLOR:SM11
                                                                        )                                %! DEFAULT_INSTRUMENT_ALERT_WITH_COLOR:SM11
                                                                }                                        %! DEFAULT_INSTRUMENT_ALERT_WITH_COLOR:SM11
                                                        }                                                %! DEFAULT_INSTRUMENT_ALERT_WITH_COLOR:SM11
                                                }                                                        %! DEFAULT_INSTRUMENT_ALERT_WITH_COLOR:SM11
                                        }
                                    }
                                \set Staff.instrumentName = \markup { Flute }                            %! REDRAWN_DEFAULT_INSTRUMENT:SM8
                                \set Staff.shortInstrumentName = \markup { Fl. }                         %! REDRAWN_DEFAULT_INSTRUMENT:SM8
                                \override Staff.InstrumentName.color = #(x11-color 'violet)              %! REDRAWN_DEFAULT_INSTRUMENT_COLOR:SM6
                <BLANKLINE>
                                % MusicVoice [measure 2]                                                 %! SM4
                                c'4.
                <BLANKLINE>
                            }
                        }
                    >>
                >>

        ..  container:: example

            Explicit instruments color blue and redraw dull blue:

            >>> layout_measure_map_ = baca.layout(
            ...     baca.page(
            ...         [1, 0, (11,)],
            ...         [2, 20, (11,)],
            ...         ),
            ...     )
            >>> maker = baca.SegmentMaker(
            ...     ignore_unpitched_notes=True,
            ...     instruments=instruments,
            ...     layout_measure_map=layout_measure_map_,
            ...     score_template=baca.SingleStaffScoreTemplate(),
            ...     spacing_specifier=baca.minimum_width((1, 24)),
            ...     time_signatures=[(3, 8), (3, 8)],
            ...     )
            >>> maker(
            ...     baca.scope('MusicVoice', 1),
            ...     baca.instrument(instruments['Flute']),
            ...     baca.make_notes(),
            ...     )

            >>> lilypond_file = maker.run(
            ...     environment='docs',
            ...     remove=remove,
            ...     )
            >>> block = abjad.Block(name='layout')
            >>> block.indent = 0
            >>> lilypond_file.items.insert(0, block)
            >>> abjad.show(lilypond_file, strict=89) # doctest: +SKIP

            ..  docs::

                >>> abjad.f(lilypond_file[abjad.Score], strict=89)
                \context Score = "Score" <<
                    \context GlobalContext = "GlobalContext" <<
                        \context GlobalSkips = "GlobalSkips" {
                <BLANKLINE>
                            % GlobalSkips [measure 1]                                                    %! SM4
                            \autoPageBreaksOff                                                           %! SEGMENT:LAYOUT:LMM1
                            \noBreak                                                                     %! SEGMENT:LAYOUT:LMM2
                            \overrideProperty Score.NonMusicalPaperColumn.line-break-system-details      %! SEGMENT:LAYOUT:LMM3
                            #'((Y-offset . 0) (alignment-distances . (11)))                              %! SEGMENT:LAYOUT:LMM3
                            \time 3/8                                                                    %! EXPLICIT_TIME_SIGNATURE:SM8
                            \bar ""                                                                      %! EMPTY_START_BAR:SM2
                            \once \override Score.TimeSignature.color = #(x11-color 'blue)               %! EXPLICIT_TIME_SIGNATURE_COLOR:SM6
                            \newSpacingSection                                                           %! SEGMENT:SPACING:HSS1
                            \set Score.proportionalNotationDuration = #(ly:make-moment 1 24)             %! SEGMENT:SPACING:HSS1
                            \pageBreak                                                                   %! SEGMENT:LAYOUT:LMM3
                            s1 * 3/8
                <BLANKLINE>
                            % GlobalSkips [measure 2]                                                    %! SM4
                            \noBreak                                                                     %! SEGMENT:LAYOUT:LMM2
                            \overrideProperty Score.NonMusicalPaperColumn.line-break-system-details      %! SEGMENT:LAYOUT:LMM3
                            #'((Y-offset . 20) (alignment-distances . (11)))                             %! SEGMENT:LAYOUT:LMM3
                            \once \override Score.TimeSignature.color = #(x11-color 'DeepPink1)          %! REDUNDANT_TIME_SIGNATURE_COLOR:SM6
                            \newSpacingSection                                                           %! SEGMENT:SPACING:HSS1
                            \set Score.proportionalNotationDuration = #(ly:make-moment 1 24)             %! SEGMENT:SPACING:HSS1
                            \break                                                                       %! SEGMENT:LAYOUT:LMM3
                            s1 * 3/8
                            \override Score.BarLine.transparent = ##f                                    %! SM5
                            \bar "|"                                                                     %! SM5
                <BLANKLINE>
                        }
                    >>
                    \context MusicContext = "MusicContext" <<
                        \context Staff = "MusicStaff" {
                            \context Voice = "MusicVoice" {
                <BLANKLINE>
                                % MusicVoice [measure 1]                                                 %! SM4
                                \set Staff.instrumentName = \markup { Flute }                            %! EXPLICIT_INSTRUMENT:SM8
                                \set Staff.shortInstrumentName = \markup { Fl. }                         %! EXPLICIT_INSTRUMENT:SM8
                                \once \override Staff.InstrumentName.color = #(x11-color 'blue)          %! EXPLICIT_INSTRUMENT_COLOR:SM6
                                c'4.
                                ^ \markup {
                                    \column
                                        {
                                            %%% \line                                                    %! EXPLICIT_INSTRUMENT_ALERT:SM10
                                            %%%     {                                                    %! EXPLICIT_INSTRUMENT_ALERT:SM10
                                            %%%         \vcenter                                         %! EXPLICIT_INSTRUMENT_ALERT:SM10
                                            %%%             (“Flute”                                     %! EXPLICIT_INSTRUMENT_ALERT:SM10
                                            %%%         \vcenter                                         %! EXPLICIT_INSTRUMENT_ALERT:SM10
                                            %%%             Flute                                        %! EXPLICIT_INSTRUMENT_ALERT:SM10
                                            %%%         \concat                                          %! EXPLICIT_INSTRUMENT_ALERT:SM10
                                            %%%             {                                            %! EXPLICIT_INSTRUMENT_ALERT:SM10
                                            %%%                 \vcenter                                 %! EXPLICIT_INSTRUMENT_ALERT:SM10
                                            %%%                     Fl.                                  %! EXPLICIT_INSTRUMENT_ALERT:SM10
                                            %%%                 \vcenter                                 %! EXPLICIT_INSTRUMENT_ALERT:SM10
                                            %%%                     )                                    %! EXPLICIT_INSTRUMENT_ALERT:SM10
                                            %%%             }                                            %! EXPLICIT_INSTRUMENT_ALERT:SM10
                                            %%%     }                                                    %! EXPLICIT_INSTRUMENT_ALERT:SM10
                                            \line                                                        %! EXPLICIT_INSTRUMENT_ALERT_WITH_COLOR:SM11
                                                {                                                        %! EXPLICIT_INSTRUMENT_ALERT_WITH_COLOR:SM11
                                                    \with-color                                          %! EXPLICIT_INSTRUMENT_ALERT_WITH_COLOR:SM11
                                                        #(x11-color 'blue)                               %! EXPLICIT_INSTRUMENT_ALERT_WITH_COLOR:SM11
                                                        {                                                %! EXPLICIT_INSTRUMENT_ALERT_WITH_COLOR:SM11
                                                            \vcenter                                     %! EXPLICIT_INSTRUMENT_ALERT_WITH_COLOR:SM11
                                                                (“Flute”                                 %! EXPLICIT_INSTRUMENT_ALERT_WITH_COLOR:SM11
                                                            \vcenter                                     %! EXPLICIT_INSTRUMENT_ALERT_WITH_COLOR:SM11
                                                                Flute                                    %! EXPLICIT_INSTRUMENT_ALERT_WITH_COLOR:SM11
                                                            \concat                                      %! EXPLICIT_INSTRUMENT_ALERT_WITH_COLOR:SM11
                                                                {                                        %! EXPLICIT_INSTRUMENT_ALERT_WITH_COLOR:SM11
                                                                    \vcenter                             %! EXPLICIT_INSTRUMENT_ALERT_WITH_COLOR:SM11
                                                                        Fl.                              %! EXPLICIT_INSTRUMENT_ALERT_WITH_COLOR:SM11
                                                                    \vcenter                             %! EXPLICIT_INSTRUMENT_ALERT_WITH_COLOR:SM11
                                                                        )                                %! EXPLICIT_INSTRUMENT_ALERT_WITH_COLOR:SM11
                                                                }                                        %! EXPLICIT_INSTRUMENT_ALERT_WITH_COLOR:SM11
                                                        }                                                %! EXPLICIT_INSTRUMENT_ALERT_WITH_COLOR:SM11
                                                }                                                        %! EXPLICIT_INSTRUMENT_ALERT_WITH_COLOR:SM11
                                        }
                                    }
                                \set Staff.instrumentName = \markup { Flute }                            %! REDRAWN_EXPLICIT_INSTRUMENT:SM8
                                \set Staff.shortInstrumentName = \markup { Fl. }                         %! REDRAWN_EXPLICIT_INSTRUMENT:SM8
                                \override Staff.InstrumentName.color = #(x11-color 'DeepSkyBlue2)        %! REDRAWN_EXPLICIT_INSTRUMENT_COLOR:SM6
                <BLANKLINE>
                                % MusicVoice [measure 2]                                                 %! SM4
                                c'4.
                <BLANKLINE>
                            }
                        }
                    >>
                >>

            Even after a previous instrument:

            >>> layout_measure_map_ = baca.layout(
            ...     baca.page(
            ...         [1, 0, (11,)],
            ...         [2, 25, (11,)],
            ...         ),
            ...     )
            >>> maker = baca.SegmentMaker(
            ...     ignore_unpitched_notes=True,
            ...     instruments=instruments,
            ...     layout_measure_map=layout_measure_map_,
            ...     score_template=baca.SingleStaffScoreTemplate(),
            ...     spacing_specifier=baca.minimum_width((1, 24)),
            ...     time_signatures=[(3, 8), (3, 8)],
            ...     )
            >>> maker(
            ...     baca.scope('MusicVoice', 1),
            ...     baca.instrument(instruments['Flute']),
            ...     baca.make_notes(),
            ...     )

            >>> metadata = {}
            >>> metadata['persistent_indicators'] = {}
            >>> metadata['persistent_indicators']['MusicStaff'] = [
            ...     abjad.Momento(
            ...         context='MusicVoice',
            ...         prototype='abjad.Instrument',
            ...         value='Piccolo',
            ...         )
            ...     ]
            >>> metadata['segment_number'] = 1
            >>> lilypond_file = maker.run(
            ...     environment='docs',
            ...     previous_metadata=metadata,
            ...     remove=remove,
            ...     )
            >>> block = abjad.Block(name='layout')
            >>> block.indent = 0
            >>> lilypond_file.items.insert(0, block)
            >>> abjad.show(lilypond_file, strict=89) # doctest: +SKIP

            ..  docs::

                >>> abjad.f(lilypond_file[abjad.Score], strict=89)
                \context Score = "Score" <<
                    \context GlobalContext = "GlobalContext" <<
                        \context GlobalSkips = "GlobalSkips" {
                <BLANKLINE>
                            % GlobalSkips [measure 1]                                                    %! SM4
                            \autoPageBreaksOff                                                           %! SEGMENT:LAYOUT:LMM1
                            \noBreak                                                                     %! SEGMENT:LAYOUT:LMM2
                            \overrideProperty Score.NonMusicalPaperColumn.line-break-system-details      %! SEGMENT:LAYOUT:LMM3
                            #'((Y-offset . 0) (alignment-distances . (11)))                              %! SEGMENT:LAYOUT:LMM3
                            \time 3/8                                                                    %! EXPLICIT_TIME_SIGNATURE:SM8
                            \mark #1                                                                     %! SM9
                            \bar ""                                                                      %! EMPTY_START_BAR:SM2
                            \once \override Score.TimeSignature.color = #(x11-color 'blue)               %! EXPLICIT_TIME_SIGNATURE_COLOR:SM6
                            \newSpacingSection                                                           %! SEGMENT:SPACING:HSS1
                            \set Score.proportionalNotationDuration = #(ly:make-moment 1 24)             %! SEGMENT:SPACING:HSS1
                            \pageBreak                                                                   %! SEGMENT:LAYOUT:LMM3
                            s1 * 3/8
                <BLANKLINE>
                            % GlobalSkips [measure 2]                                                    %! SM4
                            \noBreak                                                                     %! SEGMENT:LAYOUT:LMM2
                            \overrideProperty Score.NonMusicalPaperColumn.line-break-system-details      %! SEGMENT:LAYOUT:LMM3
                            #'((Y-offset . 25) (alignment-distances . (11)))                             %! SEGMENT:LAYOUT:LMM3
                            \once \override Score.TimeSignature.color = #(x11-color 'DeepPink1)          %! REDUNDANT_TIME_SIGNATURE_COLOR:SM6
                            \newSpacingSection                                                           %! SEGMENT:SPACING:HSS1
                            \set Score.proportionalNotationDuration = #(ly:make-moment 1 24)             %! SEGMENT:SPACING:HSS1
                            \break                                                                       %! SEGMENT:LAYOUT:LMM3
                            s1 * 3/8
                            \override Score.BarLine.transparent = ##f                                    %! SM5
                            \bar "|"                                                                     %! SM5
                <BLANKLINE>
                        }
                    >>
                    \context MusicContext = "MusicContext" <<
                        \context Staff = "MusicStaff" {
                            \context Voice = "MusicVoice" {
                <BLANKLINE>
                                % MusicVoice [measure 1]                                                 %! SM4
                                \set Staff.instrumentName = \markup { Flute }                            %! EXPLICIT_INSTRUMENT:SM8
                                \set Staff.shortInstrumentName = \markup { Fl. }                         %! EXPLICIT_INSTRUMENT:SM8
                                \once \override Staff.InstrumentName.color = #(x11-color 'blue)          %! EXPLICIT_INSTRUMENT_COLOR:SM6
                                c'4.
                                ^ \markup {
                                    \column
                                        {
                                            %%% \line                                                    %! EXPLICIT_INSTRUMENT_ALERT:SM10
                                            %%%     {                                                    %! EXPLICIT_INSTRUMENT_ALERT:SM10
                                            %%%         \vcenter                                         %! EXPLICIT_INSTRUMENT_ALERT:SM10
                                            %%%             (“Flute”                                     %! EXPLICIT_INSTRUMENT_ALERT:SM10
                                            %%%         \vcenter                                         %! EXPLICIT_INSTRUMENT_ALERT:SM10
                                            %%%             Flute                                        %! EXPLICIT_INSTRUMENT_ALERT:SM10
                                            %%%         \concat                                          %! EXPLICIT_INSTRUMENT_ALERT:SM10
                                            %%%             {                                            %! EXPLICIT_INSTRUMENT_ALERT:SM10
                                            %%%                 \vcenter                                 %! EXPLICIT_INSTRUMENT_ALERT:SM10
                                            %%%                     Fl.                                  %! EXPLICIT_INSTRUMENT_ALERT:SM10
                                            %%%                 \vcenter                                 %! EXPLICIT_INSTRUMENT_ALERT:SM10
                                            %%%                     )                                    %! EXPLICIT_INSTRUMENT_ALERT:SM10
                                            %%%             }                                            %! EXPLICIT_INSTRUMENT_ALERT:SM10
                                            %%%     }                                                    %! EXPLICIT_INSTRUMENT_ALERT:SM10
                                            \line                                                        %! EXPLICIT_INSTRUMENT_ALERT_WITH_COLOR:SM11
                                                {                                                        %! EXPLICIT_INSTRUMENT_ALERT_WITH_COLOR:SM11
                                                    \with-color                                          %! EXPLICIT_INSTRUMENT_ALERT_WITH_COLOR:SM11
                                                        #(x11-color 'blue)                               %! EXPLICIT_INSTRUMENT_ALERT_WITH_COLOR:SM11
                                                        {                                                %! EXPLICIT_INSTRUMENT_ALERT_WITH_COLOR:SM11
                                                            \vcenter                                     %! EXPLICIT_INSTRUMENT_ALERT_WITH_COLOR:SM11
                                                                (“Flute”                                 %! EXPLICIT_INSTRUMENT_ALERT_WITH_COLOR:SM11
                                                            \vcenter                                     %! EXPLICIT_INSTRUMENT_ALERT_WITH_COLOR:SM11
                                                                Flute                                    %! EXPLICIT_INSTRUMENT_ALERT_WITH_COLOR:SM11
                                                            \concat                                      %! EXPLICIT_INSTRUMENT_ALERT_WITH_COLOR:SM11
                                                                {                                        %! EXPLICIT_INSTRUMENT_ALERT_WITH_COLOR:SM11
                                                                    \vcenter                             %! EXPLICIT_INSTRUMENT_ALERT_WITH_COLOR:SM11
                                                                        Fl.                              %! EXPLICIT_INSTRUMENT_ALERT_WITH_COLOR:SM11
                                                                    \vcenter                             %! EXPLICIT_INSTRUMENT_ALERT_WITH_COLOR:SM11
                                                                        )                                %! EXPLICIT_INSTRUMENT_ALERT_WITH_COLOR:SM11
                                                                }                                        %! EXPLICIT_INSTRUMENT_ALERT_WITH_COLOR:SM11
                                                        }                                                %! EXPLICIT_INSTRUMENT_ALERT_WITH_COLOR:SM11
                                                }                                                        %! EXPLICIT_INSTRUMENT_ALERT_WITH_COLOR:SM11
                                        }
                                    }
                                \set Staff.instrumentName = \markup { Flute }                            %! REDRAWN_EXPLICIT_INSTRUMENT:SM8
                                \set Staff.shortInstrumentName = \markup { Fl. }                         %! REDRAWN_EXPLICIT_INSTRUMENT:SM8
                                \override Staff.InstrumentName.color = #(x11-color 'DeepSkyBlue2)        %! REDRAWN_EXPLICIT_INSTRUMENT_COLOR:SM6
                <BLANKLINE>
                                % MusicVoice [measure 2]                                                 %! SM4
                                c'4.
                <BLANKLINE>
                            }
                        }
                    >>
                >>

        ..  container:: example

            Reapplied instruments color green and redraw dull green:

            >>> maker = baca.SegmentMaker(
            ...     ignore_unpitched_notes=True,
            ...     instruments=instruments,
            ...     layout_measure_map=layout_measure_map_,
            ...     score_template=baca.SingleStaffScoreTemplate(),
            ...     spacing_specifier=baca.minimum_width((1, 24)),
            ...     time_signatures=[(3, 8), (3, 8)],
            ...     )
            >>> maker(
            ...     baca.scope('MusicVoice', 1),
            ...     baca.make_notes(),
            ...     )

            >>> metadata = {}
            >>> metadata['persistent_indicators'] = {}
            >>> metadata['persistent_indicators']['MusicStaff'] = [
            ...     abjad.Momento(
            ...         context='MusicVoice',
            ...         prototype='abjad.Instrument',
            ...         value='Flute',
            ...         )
            ...     ]
            >>> metadata['segment_number'] = 1
            >>> lilypond_file = maker.run(
            ...     environment='docs',
            ...     previous_metadata=metadata,
            ...     remove=remove,
            ...     )
            >>> block = abjad.Block(name='layout')
            >>> block.indent = 0
            >>> lilypond_file.items.insert(0, block)
            >>> abjad.show(lilypond_file, strict=89) # doctest: +SKIP

            ..  docs::

                >>> abjad.f(lilypond_file[abjad.Score], strict=89)
                \context Score = "Score" <<
                    \context GlobalContext = "GlobalContext" <<
                        \context GlobalSkips = "GlobalSkips" {
                <BLANKLINE>
                            % GlobalSkips [measure 1]                                                    %! SM4
                            \autoPageBreaksOff                                                           %! SEGMENT:LAYOUT:LMM1
                            \noBreak                                                                     %! SEGMENT:LAYOUT:LMM2
                            \overrideProperty Score.NonMusicalPaperColumn.line-break-system-details      %! SEGMENT:LAYOUT:LMM3
                            #'((Y-offset . 0) (alignment-distances . (11)))                              %! SEGMENT:LAYOUT:LMM3
                            \time 3/8                                                                    %! EXPLICIT_TIME_SIGNATURE:SM8
                            \mark #1                                                                     %! SM9
                            \bar ""                                                                      %! EMPTY_START_BAR:SM2
                            \once \override Score.TimeSignature.color = #(x11-color 'blue)               %! EXPLICIT_TIME_SIGNATURE_COLOR:SM6
                            \newSpacingSection                                                           %! SEGMENT:SPACING:HSS1
                            \set Score.proportionalNotationDuration = #(ly:make-moment 1 24)             %! SEGMENT:SPACING:HSS1
                            \pageBreak                                                                   %! SEGMENT:LAYOUT:LMM3
                            s1 * 3/8
                <BLANKLINE>
                            % GlobalSkips [measure 2]                                                    %! SM4
                            \noBreak                                                                     %! SEGMENT:LAYOUT:LMM2
                            \overrideProperty Score.NonMusicalPaperColumn.line-break-system-details      %! SEGMENT:LAYOUT:LMM3
                            #'((Y-offset . 25) (alignment-distances . (11)))                             %! SEGMENT:LAYOUT:LMM3
                            \once \override Score.TimeSignature.color = #(x11-color 'DeepPink1)          %! REDUNDANT_TIME_SIGNATURE_COLOR:SM6
                            \newSpacingSection                                                           %! SEGMENT:SPACING:HSS1
                            \set Score.proportionalNotationDuration = #(ly:make-moment 1 24)             %! SEGMENT:SPACING:HSS1
                            \break                                                                       %! SEGMENT:LAYOUT:LMM3
                            s1 * 3/8
                            \override Score.BarLine.transparent = ##f                                    %! SM5
                            \bar "|"                                                                     %! SM5
                <BLANKLINE>
                        }
                    >>
                    \context MusicContext = "MusicContext" <<
                        \context Staff = "MusicStaff" {
                            \context Voice = "MusicVoice" {
                <BLANKLINE>
                                % MusicVoice [measure 1]                                                 %! SM4
                                \set Staff.instrumentName = \markup { Flute }                            %! REAPPLIED_INSTRUMENT:SM8
                                \set Staff.shortInstrumentName = \markup { Fl. }                         %! REAPPLIED_INSTRUMENT:SM8
                                \once \override Staff.InstrumentName.color = #(x11-color 'green4)        %! REAPPLIED_INSTRUMENT_COLOR:SM6
                                c'4.
                                ^ \markup {
                                    \column
                                        {
                                            %%% \line                                                    %! REAPPLIED_INSTRUMENT_ALERT:SM10
                                            %%%     {                                                    %! REAPPLIED_INSTRUMENT_ALERT:SM10
                                            %%%         \vcenter                                         %! REAPPLIED_INSTRUMENT_ALERT:SM10
                                            %%%             (“Flute”                                     %! REAPPLIED_INSTRUMENT_ALERT:SM10
                                            %%%         \vcenter                                         %! REAPPLIED_INSTRUMENT_ALERT:SM10
                                            %%%             Flute                                        %! REAPPLIED_INSTRUMENT_ALERT:SM10
                                            %%%         \concat                                          %! REAPPLIED_INSTRUMENT_ALERT:SM10
                                            %%%             {                                            %! REAPPLIED_INSTRUMENT_ALERT:SM10
                                            %%%                 \vcenter                                 %! REAPPLIED_INSTRUMENT_ALERT:SM10
                                            %%%                     Fl.                                  %! REAPPLIED_INSTRUMENT_ALERT:SM10
                                            %%%                 \vcenter                                 %! REAPPLIED_INSTRUMENT_ALERT:SM10
                                            %%%                     )                                    %! REAPPLIED_INSTRUMENT_ALERT:SM10
                                            %%%             }                                            %! REAPPLIED_INSTRUMENT_ALERT:SM10
                                            %%%     }                                                    %! REAPPLIED_INSTRUMENT_ALERT:SM10
                                            \line                                                        %! REAPPLIED_INSTRUMENT_ALERT_WITH_COLOR:SM11
                                                {                                                        %! REAPPLIED_INSTRUMENT_ALERT_WITH_COLOR:SM11
                                                    \with-color                                          %! REAPPLIED_INSTRUMENT_ALERT_WITH_COLOR:SM11
                                                        #(x11-color 'green4)                             %! REAPPLIED_INSTRUMENT_ALERT_WITH_COLOR:SM11
                                                        {                                                %! REAPPLIED_INSTRUMENT_ALERT_WITH_COLOR:SM11
                                                            \vcenter                                     %! REAPPLIED_INSTRUMENT_ALERT_WITH_COLOR:SM11
                                                                (“Flute”                                 %! REAPPLIED_INSTRUMENT_ALERT_WITH_COLOR:SM11
                                                            \vcenter                                     %! REAPPLIED_INSTRUMENT_ALERT_WITH_COLOR:SM11
                                                                Flute                                    %! REAPPLIED_INSTRUMENT_ALERT_WITH_COLOR:SM11
                                                            \concat                                      %! REAPPLIED_INSTRUMENT_ALERT_WITH_COLOR:SM11
                                                                {                                        %! REAPPLIED_INSTRUMENT_ALERT_WITH_COLOR:SM11
                                                                    \vcenter                             %! REAPPLIED_INSTRUMENT_ALERT_WITH_COLOR:SM11
                                                                        Fl.                              %! REAPPLIED_INSTRUMENT_ALERT_WITH_COLOR:SM11
                                                                    \vcenter                             %! REAPPLIED_INSTRUMENT_ALERT_WITH_COLOR:SM11
                                                                        )                                %! REAPPLIED_INSTRUMENT_ALERT_WITH_COLOR:SM11
                                                                }                                        %! REAPPLIED_INSTRUMENT_ALERT_WITH_COLOR:SM11
                                                        }                                                %! REAPPLIED_INSTRUMENT_ALERT_WITH_COLOR:SM11
                                                }                                                        %! REAPPLIED_INSTRUMENT_ALERT_WITH_COLOR:SM11
                                        }
                                    }
                                \set Staff.instrumentName = \markup { Flute }                            %! REDRAWN_REAPPLIED_INSTRUMENT:SM8
                                \set Staff.shortInstrumentName = \markup { Fl. }                         %! REDRAWN_REAPPLIED_INSTRUMENT:SM8
                                \override Staff.InstrumentName.color = #(x11-color 'OliveDrab)           %! REDRAWN_REAPPLIED_INSTRUMENT_COLOR:SM6
                <BLANKLINE>
                                % MusicVoice [measure 2]                                                 %! SM4
                                c'4.
                <BLANKLINE>
                            }
                        }
                    >>
                >>

        ..  container:: example

            Redundant instruments color pink and redraw dull pink:

            >>> layout_measure_map = baca.layout(
            ...     baca.page(
            ...         [1, 0, (11,)],
            ...         [3, 20, (11,)],
            ...         ),
            ...     )
            >>> maker = baca.SegmentMaker(
            ...     ignore_unpitched_notes=True,
            ...     instruments=instruments,
            ...     layout_measure_map=layout_measure_map,
            ...     score_template=baca.SingleStaffScoreTemplate(),
            ...     spacing_specifier=baca.minimum_width((1, 24)),
            ...     time_signatures=[(4, 8), (4, 8), (4, 8)],
            ...     )
            >>> maker(
            ...     baca.scope('MusicVoice', 1),
            ...     baca.instrument(instruments['Flute']),
            ...     baca.map(
            ...         baca.instrument(instruments['Flute']),
            ...         baca.leaves()[1],
            ...         ),
            ...     baca.make_notes(),
            ...     )

            >>> lilypond_file = maker.run(
            ...     environment='docs',
            ...     remove=remove,
            ...     )
            >>> block = abjad.Block(name='layout')
            >>> block.indent = 0
            >>> lilypond_file.items.insert(0, block)
            >>> abjad.show(lilypond_file, strict=89) # doctest: +SKIP

            ..  docs::

                >>> abjad.f(lilypond_file[abjad.Score], strict=89)
                \context Score = "Score" <<
                    \context GlobalContext = "GlobalContext" <<
                        \context GlobalSkips = "GlobalSkips" {
                <BLANKLINE>
                            % GlobalSkips [measure 1]                                                    %! SM4
                            \autoPageBreaksOff                                                           %! SEGMENT:LAYOUT:LMM1
                            \noBreak                                                                     %! SEGMENT:LAYOUT:LMM2
                            \overrideProperty Score.NonMusicalPaperColumn.line-break-system-details      %! SEGMENT:LAYOUT:LMM3
                            #'((Y-offset . 0) (alignment-distances . (11)))                              %! SEGMENT:LAYOUT:LMM3
                            \time 4/8                                                                    %! EXPLICIT_TIME_SIGNATURE:SM8
                            \bar ""                                                                      %! EMPTY_START_BAR:SM2
                            \once \override Score.TimeSignature.color = #(x11-color 'blue)               %! EXPLICIT_TIME_SIGNATURE_COLOR:SM6
                            \newSpacingSection                                                           %! SEGMENT:SPACING:HSS1
                            \set Score.proportionalNotationDuration = #(ly:make-moment 1 24)             %! SEGMENT:SPACING:HSS1
                            \pageBreak                                                                   %! SEGMENT:LAYOUT:LMM3
                            s1 * 1/2
                <BLANKLINE>
                            % GlobalSkips [measure 2]                                                    %! SM4
                            \noBreak                                                                     %! SEGMENT:LAYOUT:LMM2
                            \once \override Score.TimeSignature.color = #(x11-color 'DeepPink1)          %! REDUNDANT_TIME_SIGNATURE_COLOR:SM6
                            \newSpacingSection                                                           %! SEGMENT:SPACING:HSS1
                            \set Score.proportionalNotationDuration = #(ly:make-moment 1 24)             %! SEGMENT:SPACING:HSS1
                            s1 * 1/2
                <BLANKLINE>
                            % GlobalSkips [measure 3]                                                    %! SM4
                            \noBreak                                                                     %! SEGMENT:LAYOUT:LMM2
                            \overrideProperty Score.NonMusicalPaperColumn.line-break-system-details      %! SEGMENT:LAYOUT:LMM3
                            #'((Y-offset . 20) (alignment-distances . (11)))                             %! SEGMENT:LAYOUT:LMM3
                            \once \override Score.TimeSignature.color = #(x11-color 'DeepPink1)          %! REDUNDANT_TIME_SIGNATURE_COLOR:SM6
                            \newSpacingSection                                                           %! SEGMENT:SPACING:HSS1
                            \set Score.proportionalNotationDuration = #(ly:make-moment 1 24)             %! SEGMENT:SPACING:HSS1
                            \break                                                                       %! SEGMENT:LAYOUT:LMM3
                            s1 * 1/2
                            \override Score.BarLine.transparent = ##f                                    %! SM5
                            \bar "|"                                                                     %! SM5
                <BLANKLINE>
                        }
                    >>
                    \context MusicContext = "MusicContext" <<
                        \context Staff = "MusicStaff" {
                            \context Voice = "MusicVoice" {
                <BLANKLINE>
                                % MusicVoice [measure 1]                                                 %! SM4
                                \set Staff.instrumentName = \markup { Flute }                            %! EXPLICIT_INSTRUMENT:SM8
                                \set Staff.shortInstrumentName = \markup { Fl. }                         %! EXPLICIT_INSTRUMENT:SM8
                                \once \override Staff.InstrumentName.color = #(x11-color 'blue)          %! EXPLICIT_INSTRUMENT_COLOR:SM6
                                c'2
                                ^ \markup {
                                    \column
                                        {
                                            %%% \line                                                    %! EXPLICIT_INSTRUMENT_ALERT:SM10
                                            %%%     {                                                    %! EXPLICIT_INSTRUMENT_ALERT:SM10
                                            %%%         \vcenter                                         %! EXPLICIT_INSTRUMENT_ALERT:SM10
                                            %%%             (“Flute”                                     %! EXPLICIT_INSTRUMENT_ALERT:SM10
                                            %%%         \vcenter                                         %! EXPLICIT_INSTRUMENT_ALERT:SM10
                                            %%%             Flute                                        %! EXPLICIT_INSTRUMENT_ALERT:SM10
                                            %%%         \concat                                          %! EXPLICIT_INSTRUMENT_ALERT:SM10
                                            %%%             {                                            %! EXPLICIT_INSTRUMENT_ALERT:SM10
                                            %%%                 \vcenter                                 %! EXPLICIT_INSTRUMENT_ALERT:SM10
                                            %%%                     Fl.                                  %! EXPLICIT_INSTRUMENT_ALERT:SM10
                                            %%%                 \vcenter                                 %! EXPLICIT_INSTRUMENT_ALERT:SM10
                                            %%%                     )                                    %! EXPLICIT_INSTRUMENT_ALERT:SM10
                                            %%%             }                                            %! EXPLICIT_INSTRUMENT_ALERT:SM10
                                            %%%     }                                                    %! EXPLICIT_INSTRUMENT_ALERT:SM10
                                            \line                                                        %! EXPLICIT_INSTRUMENT_ALERT_WITH_COLOR:SM11
                                                {                                                        %! EXPLICIT_INSTRUMENT_ALERT_WITH_COLOR:SM11
                                                    \with-color                                          %! EXPLICIT_INSTRUMENT_ALERT_WITH_COLOR:SM11
                                                        #(x11-color 'blue)                               %! EXPLICIT_INSTRUMENT_ALERT_WITH_COLOR:SM11
                                                        {                                                %! EXPLICIT_INSTRUMENT_ALERT_WITH_COLOR:SM11
                                                            \vcenter                                     %! EXPLICIT_INSTRUMENT_ALERT_WITH_COLOR:SM11
                                                                (“Flute”                                 %! EXPLICIT_INSTRUMENT_ALERT_WITH_COLOR:SM11
                                                            \vcenter                                     %! EXPLICIT_INSTRUMENT_ALERT_WITH_COLOR:SM11
                                                                Flute                                    %! EXPLICIT_INSTRUMENT_ALERT_WITH_COLOR:SM11
                                                            \concat                                      %! EXPLICIT_INSTRUMENT_ALERT_WITH_COLOR:SM11
                                                                {                                        %! EXPLICIT_INSTRUMENT_ALERT_WITH_COLOR:SM11
                                                                    \vcenter                             %! EXPLICIT_INSTRUMENT_ALERT_WITH_COLOR:SM11
                                                                        Fl.                              %! EXPLICIT_INSTRUMENT_ALERT_WITH_COLOR:SM11
                                                                    \vcenter                             %! EXPLICIT_INSTRUMENT_ALERT_WITH_COLOR:SM11
                                                                        )                                %! EXPLICIT_INSTRUMENT_ALERT_WITH_COLOR:SM11
                                                                }                                        %! EXPLICIT_INSTRUMENT_ALERT_WITH_COLOR:SM11
                                                        }                                                %! EXPLICIT_INSTRUMENT_ALERT_WITH_COLOR:SM11
                                                }                                                        %! EXPLICIT_INSTRUMENT_ALERT_WITH_COLOR:SM11
                                        }
                                    }
                                \set Staff.instrumentName = \markup { Flute }                            %! REDRAWN_EXPLICIT_INSTRUMENT:SM8
                                \set Staff.shortInstrumentName = \markup { Fl. }                         %! REDRAWN_EXPLICIT_INSTRUMENT:SM8
                                \override Staff.InstrumentName.color = #(x11-color 'DeepSkyBlue2)        %! REDRAWN_EXPLICIT_INSTRUMENT_COLOR:SM6
                <BLANKLINE>
                                % MusicVoice [measure 2]                                                 %! SM4
                                \set Staff.instrumentName = \markup { Flute }                            %! REDUNDANT_INSTRUMENT:SM8
                                \set Staff.shortInstrumentName = \markup { Fl. }                         %! REDUNDANT_INSTRUMENT:SM8
                                \once \override Staff.InstrumentName.color = #(x11-color 'DeepPink1)     %! REDUNDANT_INSTRUMENT_COLOR:SM6
                                c'2
                                ^ \markup {
                                    \column
                                        {
                                            %%% \line                                                    %! REDUNDANT_INSTRUMENT_ALERT:SM10
                                            %%%     {                                                    %! REDUNDANT_INSTRUMENT_ALERT:SM10
                                            %%%         \vcenter                                         %! REDUNDANT_INSTRUMENT_ALERT:SM10
                                            %%%             (“Flute”                                     %! REDUNDANT_INSTRUMENT_ALERT:SM10
                                            %%%         \vcenter                                         %! REDUNDANT_INSTRUMENT_ALERT:SM10
                                            %%%             Flute                                        %! REDUNDANT_INSTRUMENT_ALERT:SM10
                                            %%%         \concat                                          %! REDUNDANT_INSTRUMENT_ALERT:SM10
                                            %%%             {                                            %! REDUNDANT_INSTRUMENT_ALERT:SM10
                                            %%%                 \vcenter                                 %! REDUNDANT_INSTRUMENT_ALERT:SM10
                                            %%%                     Fl.                                  %! REDUNDANT_INSTRUMENT_ALERT:SM10
                                            %%%                 \vcenter                                 %! REDUNDANT_INSTRUMENT_ALERT:SM10
                                            %%%                     )                                    %! REDUNDANT_INSTRUMENT_ALERT:SM10
                                            %%%             }                                            %! REDUNDANT_INSTRUMENT_ALERT:SM10
                                            %%%     }                                                    %! REDUNDANT_INSTRUMENT_ALERT:SM10
                                            \line                                                        %! REDUNDANT_INSTRUMENT_ALERT_WITH_COLOR:SM11
                                                {                                                        %! REDUNDANT_INSTRUMENT_ALERT_WITH_COLOR:SM11
                                                    \with-color                                          %! REDUNDANT_INSTRUMENT_ALERT_WITH_COLOR:SM11
                                                        #(x11-color 'DeepPink1)                          %! REDUNDANT_INSTRUMENT_ALERT_WITH_COLOR:SM11
                                                        {                                                %! REDUNDANT_INSTRUMENT_ALERT_WITH_COLOR:SM11
                                                            \vcenter                                     %! REDUNDANT_INSTRUMENT_ALERT_WITH_COLOR:SM11
                                                                (“Flute”                                 %! REDUNDANT_INSTRUMENT_ALERT_WITH_COLOR:SM11
                                                            \vcenter                                     %! REDUNDANT_INSTRUMENT_ALERT_WITH_COLOR:SM11
                                                                Flute                                    %! REDUNDANT_INSTRUMENT_ALERT_WITH_COLOR:SM11
                                                            \concat                                      %! REDUNDANT_INSTRUMENT_ALERT_WITH_COLOR:SM11
                                                                {                                        %! REDUNDANT_INSTRUMENT_ALERT_WITH_COLOR:SM11
                                                                    \vcenter                             %! REDUNDANT_INSTRUMENT_ALERT_WITH_COLOR:SM11
                                                                        Fl.                              %! REDUNDANT_INSTRUMENT_ALERT_WITH_COLOR:SM11
                                                                    \vcenter                             %! REDUNDANT_INSTRUMENT_ALERT_WITH_COLOR:SM11
                                                                        )                                %! REDUNDANT_INSTRUMENT_ALERT_WITH_COLOR:SM11
                                                                }                                        %! REDUNDANT_INSTRUMENT_ALERT_WITH_COLOR:SM11
                                                        }                                                %! REDUNDANT_INSTRUMENT_ALERT_WITH_COLOR:SM11
                                                }                                                        %! REDUNDANT_INSTRUMENT_ALERT_WITH_COLOR:SM11
                                        }
                                    }
                                \set Staff.instrumentName = \markup { Flute }                            %! REDRAWN_REDUNDANT_INSTRUMENT:SM8
                                \set Staff.shortInstrumentName = \markup { Fl. }                         %! REDRAWN_REDUNDANT_INSTRUMENT:SM8
                                \override Staff.InstrumentName.color = #(x11-color 'DeepPink4)           %! REDRAWN_REDUNDANT_INSTRUMENT_COLOR:SM6
                <BLANKLINE>
                                % MusicVoice [measure 3]                                                 %! SM4
                                c'2
                <BLANKLINE>
                            }
                        }
                    >>
                >>

            Even at the beginning of a segment:

            >>> layout_measure_map = baca.layout(
            ...     baca.page(
            ...         [1, 0, (11,)],
            ...         [2, 20, (11,)],
            ...         ),
            ...     )
            >>> maker = baca.SegmentMaker(
            ...     ignore_unpitched_notes=True,
            ...     instruments=instruments,
            ...     layout_measure_map=layout_measure_map,
            ...     score_template=baca.SingleStaffScoreTemplate(),
            ...     spacing_specifier=baca.minimum_width((1, 24)),
            ...     time_signatures=[(3, 8), (3, 8)],
            ...     )
            >>> maker(
            ...     baca.scope('MusicVoice', 1),
            ...     baca.instrument(instruments['Flute']),
            ...     baca.make_notes(),
            ...     )

            >>> metadata = {}
            >>> metadata['persistent_indicators'] = {}
            >>> metadata['persistent_indicators']['MusicStaff'] = [
            ...     abjad.Momento(
            ...         context='MusicVoice',
            ...         prototype='abjad.Instrument',
            ...         value='Flute',
            ...         )
            ...     ]
            >>> metadata['segment_number'] = 1
            >>> lilypond_file = maker.run(
            ...     environment='docs',
            ...     previous_metadata=metadata,
            ...     remove=remove,
            ...     )
            >>> block = abjad.Block(name='layout')
            >>> block.indent = 0
            >>> lilypond_file.items.insert(0, block)
            >>> abjad.show(lilypond_file, strict=89) # doctest: +SKIP

            ..  docs::

                >>> abjad.f(lilypond_file[abjad.Score], strict=89)
                \context Score = "Score" <<
                    \context GlobalContext = "GlobalContext" <<
                        \context GlobalSkips = "GlobalSkips" {
                <BLANKLINE>
                            % GlobalSkips [measure 1]                                                    %! SM4
                            \autoPageBreaksOff                                                           %! SEGMENT:LAYOUT:LMM1
                            \noBreak                                                                     %! SEGMENT:LAYOUT:LMM2
                            \overrideProperty Score.NonMusicalPaperColumn.line-break-system-details      %! SEGMENT:LAYOUT:LMM3
                            #'((Y-offset . 0) (alignment-distances . (11)))                              %! SEGMENT:LAYOUT:LMM3
                            \time 3/8                                                                    %! EXPLICIT_TIME_SIGNATURE:SM8
                            \mark #1                                                                     %! SM9
                            \bar ""                                                                      %! EMPTY_START_BAR:SM2
                            \once \override Score.TimeSignature.color = #(x11-color 'blue)               %! EXPLICIT_TIME_SIGNATURE_COLOR:SM6
                            \newSpacingSection                                                           %! SEGMENT:SPACING:HSS1
                            \set Score.proportionalNotationDuration = #(ly:make-moment 1 24)             %! SEGMENT:SPACING:HSS1
                            \pageBreak                                                                   %! SEGMENT:LAYOUT:LMM3
                            s1 * 3/8
                <BLANKLINE>
                            % GlobalSkips [measure 2]                                                    %! SM4
                            \noBreak                                                                     %! SEGMENT:LAYOUT:LMM2
                            \overrideProperty Score.NonMusicalPaperColumn.line-break-system-details      %! SEGMENT:LAYOUT:LMM3
                            #'((Y-offset . 20) (alignment-distances . (11)))                             %! SEGMENT:LAYOUT:LMM3
                            \once \override Score.TimeSignature.color = #(x11-color 'DeepPink1)          %! REDUNDANT_TIME_SIGNATURE_COLOR:SM6
                            \newSpacingSection                                                           %! SEGMENT:SPACING:HSS1
                            \set Score.proportionalNotationDuration = #(ly:make-moment 1 24)             %! SEGMENT:SPACING:HSS1
                            \break                                                                       %! SEGMENT:LAYOUT:LMM3
                            s1 * 3/8
                            \override Score.BarLine.transparent = ##f                                    %! SM5
                            \bar "|"                                                                     %! SM5
                <BLANKLINE>
                        }
                    >>
                    \context MusicContext = "MusicContext" <<
                        \context Staff = "MusicStaff" {
                            \context Voice = "MusicVoice" {
                <BLANKLINE>
                                % MusicVoice [measure 1]                                                 %! SM4
                                \set Staff.instrumentName = \markup { Flute }                            %! REDUNDANT_INSTRUMENT:SM8
                                \set Staff.shortInstrumentName = \markup { Fl. }                         %! REDUNDANT_INSTRUMENT:SM8
                                \once \override Staff.InstrumentName.color = #(x11-color 'DeepPink1)     %! REDUNDANT_INSTRUMENT_COLOR:SM6
                                c'4.
                                ^ \markup {
                                    \column
                                        {
                                            %%% \line                                                    %! REDUNDANT_INSTRUMENT_ALERT:SM10
                                            %%%     {                                                    %! REDUNDANT_INSTRUMENT_ALERT:SM10
                                            %%%         \vcenter                                         %! REDUNDANT_INSTRUMENT_ALERT:SM10
                                            %%%             (“Flute”                                     %! REDUNDANT_INSTRUMENT_ALERT:SM10
                                            %%%         \vcenter                                         %! REDUNDANT_INSTRUMENT_ALERT:SM10
                                            %%%             Flute                                        %! REDUNDANT_INSTRUMENT_ALERT:SM10
                                            %%%         \concat                                          %! REDUNDANT_INSTRUMENT_ALERT:SM10
                                            %%%             {                                            %! REDUNDANT_INSTRUMENT_ALERT:SM10
                                            %%%                 \vcenter                                 %! REDUNDANT_INSTRUMENT_ALERT:SM10
                                            %%%                     Fl.                                  %! REDUNDANT_INSTRUMENT_ALERT:SM10
                                            %%%                 \vcenter                                 %! REDUNDANT_INSTRUMENT_ALERT:SM10
                                            %%%                     )                                    %! REDUNDANT_INSTRUMENT_ALERT:SM10
                                            %%%             }                                            %! REDUNDANT_INSTRUMENT_ALERT:SM10
                                            %%%     }                                                    %! REDUNDANT_INSTRUMENT_ALERT:SM10
                                            \line                                                        %! REDUNDANT_INSTRUMENT_ALERT_WITH_COLOR:SM11
                                                {                                                        %! REDUNDANT_INSTRUMENT_ALERT_WITH_COLOR:SM11
                                                    \with-color                                          %! REDUNDANT_INSTRUMENT_ALERT_WITH_COLOR:SM11
                                                        #(x11-color 'DeepPink1)                          %! REDUNDANT_INSTRUMENT_ALERT_WITH_COLOR:SM11
                                                        {                                                %! REDUNDANT_INSTRUMENT_ALERT_WITH_COLOR:SM11
                                                            \vcenter                                     %! REDUNDANT_INSTRUMENT_ALERT_WITH_COLOR:SM11
                                                                (“Flute”                                 %! REDUNDANT_INSTRUMENT_ALERT_WITH_COLOR:SM11
                                                            \vcenter                                     %! REDUNDANT_INSTRUMENT_ALERT_WITH_COLOR:SM11
                                                                Flute                                    %! REDUNDANT_INSTRUMENT_ALERT_WITH_COLOR:SM11
                                                            \concat                                      %! REDUNDANT_INSTRUMENT_ALERT_WITH_COLOR:SM11
                                                                {                                        %! REDUNDANT_INSTRUMENT_ALERT_WITH_COLOR:SM11
                                                                    \vcenter                             %! REDUNDANT_INSTRUMENT_ALERT_WITH_COLOR:SM11
                                                                        Fl.                              %! REDUNDANT_INSTRUMENT_ALERT_WITH_COLOR:SM11
                                                                    \vcenter                             %! REDUNDANT_INSTRUMENT_ALERT_WITH_COLOR:SM11
                                                                        )                                %! REDUNDANT_INSTRUMENT_ALERT_WITH_COLOR:SM11
                                                                }                                        %! REDUNDANT_INSTRUMENT_ALERT_WITH_COLOR:SM11
                                                        }                                                %! REDUNDANT_INSTRUMENT_ALERT_WITH_COLOR:SM11
                                                }                                                        %! REDUNDANT_INSTRUMENT_ALERT_WITH_COLOR:SM11
                                        }
                                    }
                                \set Staff.instrumentName = \markup { Flute }                            %! REDRAWN_REDUNDANT_INSTRUMENT:SM8
                                \set Staff.shortInstrumentName = \markup { Fl. }                         %! REDRAWN_REDUNDANT_INSTRUMENT:SM8
                                \override Staff.InstrumentName.color = #(x11-color 'DeepPink4)           %! REDRAWN_REDUNDANT_INSTRUMENT_COLOR:SM6
                <BLANKLINE>
                                % MusicVoice [measure 2]                                                 %! SM4
                                c'4.
                <BLANKLINE>
                            }
                        }
                    >>
                >>

        Returns instrument dictionary or none.
        '''
        return self._instruments

    @property
    def last_segment(self):
        r'''Is true when composer declares segment to be last in score.

        Defaults to none.

        Set to true, false or none.

        Returns true, false or none.
        '''
        return self._last_segment

    @property
    def layout_measure_map(self):
        r'''Gets layout measure map.

        Set to layout measure map or none.

        Returns layout measure map or none.
        '''
        return self._layout_measure_map

    @property
    def manifests(self):
        r'''Gets manifests.

        Returns ordered dictionary of ordered dictionaries.
        '''
        manifests = abjad.TypedOrderedDict()
        manifests['abjad.Instrument'] = self.instruments
        manifests['abjad.MetronomeMark'] = self.metronome_marks
        manifests['baca.MarginMarkup'] = self.margin_markup
        return manifests

    @property
    def margin_markup(self):
        r'''Gets margin markup.

        ..  container:: example

            >>> margin_markup = abjad.TypedOrderedDict()
            >>> margin_markup['I+II'] = baca.MarginMarkup(
            ...     markup=abjad.Markup('I+II'),
            ...     short_markup=abjad.Markup('I+II'),
            ...     )
            >>> margin_markup['III+IV'] = baca.MarginMarkup(
            ...     markup=abjad.Markup('III+IV'),
            ...     short_markup=abjad.Markup('III+IV'),
            ...     )
            >>> layout_measure_map = baca.layout(
            ...     baca.page(
            ...         [1, 0, (11,)],
            ...         [2, 20, (11,)],
            ...         ),
            ...     )
            >>> remove = [
            ...     baca.Tags.build(baca.Tags.SPACING_MARKUP),
            ...     baca.Tags.STAGE_NUMBER_MARKUP,
            ...     ]

        ..  container:: example

            Default margin markup color purple and redraw dull purple:

            >>> score_template = baca.SingleStaffScoreTemplate()
            >>> triple = (
            ...     'MusicStaff',
            ...     'default_margin_markup',
            ...     margin_markup['I+II'],
            ...     )
            >>> score_template.defaults.append(triple)
            >>> maker = baca.SegmentMaker(
            ...     ignore_unpitched_notes=True,
            ...     margin_markup=margin_markup,
            ...     layout_measure_map=layout_measure_map,
            ...     score_template=score_template,
            ...     spacing_specifier=baca.minimum_width((1, 24)),
            ...     time_signatures=[(3, 8), (3, 8)],
            ...     )
            >>> maker(
            ...     baca.scope('MusicVoice', 1),
            ...     baca.make_notes(),
            ...     )

            >>> lilypond_file = maker.run(
            ...     environment='docs',
            ...     remove=remove,
            ...     )
            >>> block = abjad.Block(name='layout')
            >>> block.indent = 0
            >>> lilypond_file.items.insert(0, block)
            >>> abjad.show(lilypond_file, strict=89) # doctest: +SKIP

            ..  docs::

                >>> abjad.f(lilypond_file[abjad.Score], strict=89)
                \context Score = "Score" <<
                    \context GlobalContext = "GlobalContext" <<
                        \context GlobalSkips = "GlobalSkips" {
                <BLANKLINE>
                            % GlobalSkips [measure 1]                                                    %! SM4
                            \autoPageBreaksOff                                                           %! SEGMENT:LAYOUT:LMM1
                            \noBreak                                                                     %! SEGMENT:LAYOUT:LMM2
                            \overrideProperty Score.NonMusicalPaperColumn.line-break-system-details      %! SEGMENT:LAYOUT:LMM3
                            #'((Y-offset . 0) (alignment-distances . (11)))                              %! SEGMENT:LAYOUT:LMM3
                            \time 3/8                                                                    %! EXPLICIT_TIME_SIGNATURE:SM8
                            \bar ""                                                                      %! EMPTY_START_BAR:SM2
                            \once \override Score.TimeSignature.color = #(x11-color 'blue)               %! EXPLICIT_TIME_SIGNATURE_COLOR:SM6
                            \newSpacingSection                                                           %! SEGMENT:SPACING:HSS1
                            \set Score.proportionalNotationDuration = #(ly:make-moment 1 24)             %! SEGMENT:SPACING:HSS1
                            \pageBreak                                                                   %! SEGMENT:LAYOUT:LMM3
                            s1 * 3/8
                <BLANKLINE>
                            % GlobalSkips [measure 2]                                                    %! SM4
                            \noBreak                                                                     %! SEGMENT:LAYOUT:LMM2
                            \overrideProperty Score.NonMusicalPaperColumn.line-break-system-details      %! SEGMENT:LAYOUT:LMM3
                            #'((Y-offset . 20) (alignment-distances . (11)))                             %! SEGMENT:LAYOUT:LMM3
                            \once \override Score.TimeSignature.color = #(x11-color 'DeepPink1)          %! REDUNDANT_TIME_SIGNATURE_COLOR:SM6
                            \newSpacingSection                                                           %! SEGMENT:SPACING:HSS1
                            \set Score.proportionalNotationDuration = #(ly:make-moment 1 24)             %! SEGMENT:SPACING:HSS1
                            \break                                                                       %! SEGMENT:LAYOUT:LMM3
                            s1 * 3/8
                            \override Score.BarLine.transparent = ##f                                    %! SM5
                            \bar "|"                                                                     %! SM5
                <BLANKLINE>
                        }
                    >>
                    \context MusicContext = "MusicContext" <<
                        \context Staff = "MusicStaff" {
                            \context Voice = "MusicVoice" {
                <BLANKLINE>
                                % MusicVoice [measure 1]                                                 %! SM4
                                \set Staff.instrumentName = \markup { I+II }                             %! DEFAULT_MARGIN_MARKUP:SM8
                                \set Staff.shortInstrumentName = \markup { I+II }                        %! DEFAULT_MARGIN_MARKUP:SM8
                                \once \override Staff.InstrumentName.color = #(x11-color 'DarkViolet)    %! DEFAULT_MARGIN_MARKUP_COLOR:SM6
                                c'4.
                                ^ \markup {
                                    \column
                                        {
                                            %%% \line                                                    %! DEFAULT_MARGIN_MARKUP_ALERT:SM10
                                            %%%     {                                                    %! DEFAULT_MARGIN_MARKUP_ALERT:SM10
                                            %%%         \vcenter                                         %! DEFAULT_MARGIN_MARKUP_ALERT:SM10
                                            %%%             [“I+II”                                      %! DEFAULT_MARGIN_MARKUP_ALERT:SM10
                                            %%%         \vcenter                                         %! DEFAULT_MARGIN_MARKUP_ALERT:SM10
                                            %%%             I+II                                         %! DEFAULT_MARGIN_MARKUP_ALERT:SM10
                                            %%%         \concat                                          %! DEFAULT_MARGIN_MARKUP_ALERT:SM10
                                            %%%             {                                            %! DEFAULT_MARGIN_MARKUP_ALERT:SM10
                                            %%%                 \vcenter                                 %! DEFAULT_MARGIN_MARKUP_ALERT:SM10
                                            %%%                     I+II                                 %! DEFAULT_MARGIN_MARKUP_ALERT:SM10
                                            %%%                 \vcenter                                 %! DEFAULT_MARGIN_MARKUP_ALERT:SM10
                                            %%%                     ]                                    %! DEFAULT_MARGIN_MARKUP_ALERT:SM10
                                            %%%             }                                            %! DEFAULT_MARGIN_MARKUP_ALERT:SM10
                                            %%%     }                                                    %! DEFAULT_MARGIN_MARKUP_ALERT:SM10
                                            \line                                                        %! DEFAULT_MARGIN_MARKUP_ALERT_WITH_COLOR:SM11
                                                {                                                        %! DEFAULT_MARGIN_MARKUP_ALERT_WITH_COLOR:SM11
                                                    \with-color                                          %! DEFAULT_MARGIN_MARKUP_ALERT_WITH_COLOR:SM11
                                                        #(x11-color 'DarkViolet)                         %! DEFAULT_MARGIN_MARKUP_ALERT_WITH_COLOR:SM11
                                                        {                                                %! DEFAULT_MARGIN_MARKUP_ALERT_WITH_COLOR:SM11
                                                            \vcenter                                     %! DEFAULT_MARGIN_MARKUP_ALERT_WITH_COLOR:SM11
                                                                [“I+II”                                  %! DEFAULT_MARGIN_MARKUP_ALERT_WITH_COLOR:SM11
                                                            \vcenter                                     %! DEFAULT_MARGIN_MARKUP_ALERT_WITH_COLOR:SM11
                                                                I+II                                     %! DEFAULT_MARGIN_MARKUP_ALERT_WITH_COLOR:SM11
                                                            \concat                                      %! DEFAULT_MARGIN_MARKUP_ALERT_WITH_COLOR:SM11
                                                                {                                        %! DEFAULT_MARGIN_MARKUP_ALERT_WITH_COLOR:SM11
                                                                    \vcenter                             %! DEFAULT_MARGIN_MARKUP_ALERT_WITH_COLOR:SM11
                                                                        I+II                             %! DEFAULT_MARGIN_MARKUP_ALERT_WITH_COLOR:SM11
                                                                    \vcenter                             %! DEFAULT_MARGIN_MARKUP_ALERT_WITH_COLOR:SM11
                                                                        ]                                %! DEFAULT_MARGIN_MARKUP_ALERT_WITH_COLOR:SM11
                                                                }                                        %! DEFAULT_MARGIN_MARKUP_ALERT_WITH_COLOR:SM11
                                                        }                                                %! DEFAULT_MARGIN_MARKUP_ALERT_WITH_COLOR:SM11
                                                }                                                        %! DEFAULT_MARGIN_MARKUP_ALERT_WITH_COLOR:SM11
                                        }
                                    }
                                \set Staff.instrumentName = \markup { I+II }                             %! REDRAWN_DEFAULT_MARGIN_MARKUP:SM8
                                \set Staff.shortInstrumentName = \markup { I+II }                        %! REDRAWN_DEFAULT_MARGIN_MARKUP:SM8
                                \override Staff.InstrumentName.color = #(x11-color 'violet)              %! REDRAWN_DEFAULT_MARGIN_MARKUP_COLOR:SM6
                <BLANKLINE>
                                % MusicVoice [measure 2]                                                 %! SM4
                                c'4.
                <BLANKLINE>
                            }
                        }
                    >>
                >>

        ..  container:: example

            Explicit margin markup color blue and redraw dull blue:

            >>> maker = baca.SegmentMaker(
            ...     ignore_unpitched_notes=True,
            ...     layout_measure_map=layout_measure_map,
            ...     margin_markup=margin_markup,
            ...     score_template=baca.SingleStaffScoreTemplate(),
            ...     spacing_specifier=baca.minimum_width((1, 24)),
            ...     time_signatures=[(3, 8), (3, 8)],
            ...     )
            >>> maker(
            ...     baca.scope('MusicVoice', 1),
            ...     baca.margin_markup(margin_markup['I+II']),
            ...     baca.make_notes(),
            ...     )

            >>> lilypond_file = maker.run(
            ...     environment='docs',
            ...     remove=remove,
            ...     )
            >>> block = abjad.Block(name='layout')
            >>> block.indent = 0
            >>> lilypond_file.items.insert(0, block)
            >>> abjad.show(lilypond_file, strict=89) # doctest: +SKIP

            ..  docs::

                >>> abjad.f(lilypond_file[abjad.Score], strict=89)
                \context Score = "Score" <<
                    \context GlobalContext = "GlobalContext" <<
                        \context GlobalSkips = "GlobalSkips" {
                <BLANKLINE>
                            % GlobalSkips [measure 1]                                                    %! SM4
                            \autoPageBreaksOff                                                           %! SEGMENT:LAYOUT:LMM1
                            \noBreak                                                                     %! SEGMENT:LAYOUT:LMM2
                            \overrideProperty Score.NonMusicalPaperColumn.line-break-system-details      %! SEGMENT:LAYOUT:LMM3
                            #'((Y-offset . 0) (alignment-distances . (11)))                              %! SEGMENT:LAYOUT:LMM3
                            \time 3/8                                                                    %! EXPLICIT_TIME_SIGNATURE:SM8
                            \bar ""                                                                      %! EMPTY_START_BAR:SM2
                            \once \override Score.TimeSignature.color = #(x11-color 'blue)               %! EXPLICIT_TIME_SIGNATURE_COLOR:SM6
                            \newSpacingSection                                                           %! SEGMENT:SPACING:HSS1
                            \set Score.proportionalNotationDuration = #(ly:make-moment 1 24)             %! SEGMENT:SPACING:HSS1
                            \pageBreak                                                                   %! SEGMENT:LAYOUT:LMM3
                            s1 * 3/8
                <BLANKLINE>
                            % GlobalSkips [measure 2]                                                    %! SM4
                            \noBreak                                                                     %! SEGMENT:LAYOUT:LMM2
                            \overrideProperty Score.NonMusicalPaperColumn.line-break-system-details      %! SEGMENT:LAYOUT:LMM3
                            #'((Y-offset . 20) (alignment-distances . (11)))                             %! SEGMENT:LAYOUT:LMM3
                            \once \override Score.TimeSignature.color = #(x11-color 'DeepPink1)          %! REDUNDANT_TIME_SIGNATURE_COLOR:SM6
                            \newSpacingSection                                                           %! SEGMENT:SPACING:HSS1
                            \set Score.proportionalNotationDuration = #(ly:make-moment 1 24)             %! SEGMENT:SPACING:HSS1
                            \break                                                                       %! SEGMENT:LAYOUT:LMM3
                            s1 * 3/8
                            \override Score.BarLine.transparent = ##f                                    %! SM5
                            \bar "|"                                                                     %! SM5
                <BLANKLINE>
                        }
                    >>
                    \context MusicContext = "MusicContext" <<
                        \context Staff = "MusicStaff" {
                            \context Voice = "MusicVoice" {
                <BLANKLINE>
                                % MusicVoice [measure 1]                                                 %! SM4
                                \set Staff.instrumentName = \markup { I+II }                             %! EXPLICIT_MARGIN_MARKUP:SM8
                                \set Staff.shortInstrumentName = \markup { I+II }                        %! EXPLICIT_MARGIN_MARKUP:SM8
                                \once \override Staff.InstrumentName.color = #(x11-color 'blue)          %! EXPLICIT_MARGIN_MARKUP_COLOR:SM6
                                c'4.
                                ^ \markup {
                                    \column
                                        {
                                            %%% \line                                                    %! EXPLICIT_MARGIN_MARKUP_ALERT:SM10
                                            %%%     {                                                    %! EXPLICIT_MARGIN_MARKUP_ALERT:SM10
                                            %%%         \vcenter                                         %! EXPLICIT_MARGIN_MARKUP_ALERT:SM10
                                            %%%             [“I+II”                                      %! EXPLICIT_MARGIN_MARKUP_ALERT:SM10
                                            %%%         \vcenter                                         %! EXPLICIT_MARGIN_MARKUP_ALERT:SM10
                                            %%%             I+II                                         %! EXPLICIT_MARGIN_MARKUP_ALERT:SM10
                                            %%%         \concat                                          %! EXPLICIT_MARGIN_MARKUP_ALERT:SM10
                                            %%%             {                                            %! EXPLICIT_MARGIN_MARKUP_ALERT:SM10
                                            %%%                 \vcenter                                 %! EXPLICIT_MARGIN_MARKUP_ALERT:SM10
                                            %%%                     I+II                                 %! EXPLICIT_MARGIN_MARKUP_ALERT:SM10
                                            %%%                 \vcenter                                 %! EXPLICIT_MARGIN_MARKUP_ALERT:SM10
                                            %%%                     ]                                    %! EXPLICIT_MARGIN_MARKUP_ALERT:SM10
                                            %%%             }                                            %! EXPLICIT_MARGIN_MARKUP_ALERT:SM10
                                            %%%     }                                                    %! EXPLICIT_MARGIN_MARKUP_ALERT:SM10
                                            \line                                                        %! EXPLICIT_MARGIN_MARKUP_ALERT_WITH_COLOR:SM11
                                                {                                                        %! EXPLICIT_MARGIN_MARKUP_ALERT_WITH_COLOR:SM11
                                                    \with-color                                          %! EXPLICIT_MARGIN_MARKUP_ALERT_WITH_COLOR:SM11
                                                        #(x11-color 'blue)                               %! EXPLICIT_MARGIN_MARKUP_ALERT_WITH_COLOR:SM11
                                                        {                                                %! EXPLICIT_MARGIN_MARKUP_ALERT_WITH_COLOR:SM11
                                                            \vcenter                                     %! EXPLICIT_MARGIN_MARKUP_ALERT_WITH_COLOR:SM11
                                                                [“I+II”                                  %! EXPLICIT_MARGIN_MARKUP_ALERT_WITH_COLOR:SM11
                                                            \vcenter                                     %! EXPLICIT_MARGIN_MARKUP_ALERT_WITH_COLOR:SM11
                                                                I+II                                     %! EXPLICIT_MARGIN_MARKUP_ALERT_WITH_COLOR:SM11
                                                            \concat                                      %! EXPLICIT_MARGIN_MARKUP_ALERT_WITH_COLOR:SM11
                                                                {                                        %! EXPLICIT_MARGIN_MARKUP_ALERT_WITH_COLOR:SM11
                                                                    \vcenter                             %! EXPLICIT_MARGIN_MARKUP_ALERT_WITH_COLOR:SM11
                                                                        I+II                             %! EXPLICIT_MARGIN_MARKUP_ALERT_WITH_COLOR:SM11
                                                                    \vcenter                             %! EXPLICIT_MARGIN_MARKUP_ALERT_WITH_COLOR:SM11
                                                                        ]                                %! EXPLICIT_MARGIN_MARKUP_ALERT_WITH_COLOR:SM11
                                                                }                                        %! EXPLICIT_MARGIN_MARKUP_ALERT_WITH_COLOR:SM11
                                                        }                                                %! EXPLICIT_MARGIN_MARKUP_ALERT_WITH_COLOR:SM11
                                                }                                                        %! EXPLICIT_MARGIN_MARKUP_ALERT_WITH_COLOR:SM11
                                        }
                                    }
                                \set Staff.instrumentName = \markup { I+II }                             %! REDRAWN_EXPLICIT_MARGIN_MARKUP:SM8
                                \set Staff.shortInstrumentName = \markup { I+II }                        %! REDRAWN_EXPLICIT_MARGIN_MARKUP:SM8
                                \override Staff.InstrumentName.color = #(x11-color 'DeepSkyBlue2)        %! REDRAWN_EXPLICIT_MARGIN_MARKUP_COLOR:SM6
                <BLANKLINE>
                                % MusicVoice [measure 2]                                                 %! SM4
                                c'4.
                <BLANKLINE>
                            }
                        }
                    >>
                >>

            Even after previous margin markup:

            >>> maker = baca.SegmentMaker(
            ...     ignore_unpitched_notes=True,
            ...     layout_measure_map=layout_measure_map,
            ...     margin_markup=margin_markup,
            ...     score_template=baca.SingleStaffScoreTemplate(),
            ...     spacing_specifier=baca.minimum_width((1, 24)),
            ...     time_signatures=[(3, 8), (3, 8)],
            ...     )
            >>> maker(
            ...     baca.scope('MusicVoice', 1),
            ...     baca.margin_markup(margin_markup['III+IV']),
            ...     baca.make_notes(),
            ...     )

            >>> metadata = {}
            >>> metadata['persistent_indicators'] = {}
            >>> metadata['persistent_indicators']['MusicStaff'] = [
            ...     abjad.Momento(
            ...         context='MusicVoice',
            ...         prototype='baca.MarginMarkup',
            ...         value='I+II',
            ...         )
            ...     ]
            >>> metadata['segment_number'] = 1
            >>> lilypond_file = maker.run(
            ...     environment='docs',
            ...     previous_metadata=metadata,
            ...     remove=remove,
            ...     )
            >>> block = abjad.Block(name='layout')
            >>> block.indent = 0
            >>> lilypond_file.items.insert(0, block)
            >>> abjad.show(lilypond_file, strict=89) # doctest: +SKIP

            ..  docs::

                >>> abjad.f(lilypond_file[abjad.Score], strict=89)
                \context Score = "Score" <<
                    \context GlobalContext = "GlobalContext" <<
                        \context GlobalSkips = "GlobalSkips" {
                <BLANKLINE>
                            % GlobalSkips [measure 1]                                                    %! SM4
                            \autoPageBreaksOff                                                           %! SEGMENT:LAYOUT:LMM1
                            \noBreak                                                                     %! SEGMENT:LAYOUT:LMM2
                            \overrideProperty Score.NonMusicalPaperColumn.line-break-system-details      %! SEGMENT:LAYOUT:LMM3
                            #'((Y-offset . 0) (alignment-distances . (11)))                              %! SEGMENT:LAYOUT:LMM3
                            \time 3/8                                                                    %! EXPLICIT_TIME_SIGNATURE:SM8
                            \mark #1                                                                     %! SM9
                            \bar ""                                                                      %! EMPTY_START_BAR:SM2
                            \once \override Score.TimeSignature.color = #(x11-color 'blue)               %! EXPLICIT_TIME_SIGNATURE_COLOR:SM6
                            \newSpacingSection                                                           %! SEGMENT:SPACING:HSS1
                            \set Score.proportionalNotationDuration = #(ly:make-moment 1 24)             %! SEGMENT:SPACING:HSS1
                            \pageBreak                                                                   %! SEGMENT:LAYOUT:LMM3
                            s1 * 3/8
                <BLANKLINE>
                            % GlobalSkips [measure 2]                                                    %! SM4
                            \noBreak                                                                     %! SEGMENT:LAYOUT:LMM2
                            \overrideProperty Score.NonMusicalPaperColumn.line-break-system-details      %! SEGMENT:LAYOUT:LMM3
                            #'((Y-offset . 20) (alignment-distances . (11)))                             %! SEGMENT:LAYOUT:LMM3
                            \once \override Score.TimeSignature.color = #(x11-color 'DeepPink1)          %! REDUNDANT_TIME_SIGNATURE_COLOR:SM6
                            \newSpacingSection                                                           %! SEGMENT:SPACING:HSS1
                            \set Score.proportionalNotationDuration = #(ly:make-moment 1 24)             %! SEGMENT:SPACING:HSS1
                            \break                                                                       %! SEGMENT:LAYOUT:LMM3
                            s1 * 3/8
                            \override Score.BarLine.transparent = ##f                                    %! SM5
                            \bar "|"                                                                     %! SM5
                <BLANKLINE>
                        }
                    >>
                    \context MusicContext = "MusicContext" <<
                        \context Staff = "MusicStaff" {
                            \context Voice = "MusicVoice" {
                <BLANKLINE>
                                % MusicVoice [measure 1]                                                 %! SM4
                                \set Staff.instrumentName = \markup { III+IV }                           %! EXPLICIT_MARGIN_MARKUP:SM8
                                \set Staff.shortInstrumentName = \markup { III+IV }                      %! EXPLICIT_MARGIN_MARKUP:SM8
                                \once \override Staff.InstrumentName.color = #(x11-color 'blue)          %! EXPLICIT_MARGIN_MARKUP_COLOR:SM6
                                c'4.
                                ^ \markup {
                                    \column
                                        {
                                            %%% \line                                                    %! EXPLICIT_MARGIN_MARKUP_ALERT:SM10
                                            %%%     {                                                    %! EXPLICIT_MARGIN_MARKUP_ALERT:SM10
                                            %%%         \vcenter                                         %! EXPLICIT_MARGIN_MARKUP_ALERT:SM10
                                            %%%             [“III+IV”                                    %! EXPLICIT_MARGIN_MARKUP_ALERT:SM10
                                            %%%         \vcenter                                         %! EXPLICIT_MARGIN_MARKUP_ALERT:SM10
                                            %%%             III+IV                                       %! EXPLICIT_MARGIN_MARKUP_ALERT:SM10
                                            %%%         \concat                                          %! EXPLICIT_MARGIN_MARKUP_ALERT:SM10
                                            %%%             {                                            %! EXPLICIT_MARGIN_MARKUP_ALERT:SM10
                                            %%%                 \vcenter                                 %! EXPLICIT_MARGIN_MARKUP_ALERT:SM10
                                            %%%                     III+IV                               %! EXPLICIT_MARGIN_MARKUP_ALERT:SM10
                                            %%%                 \vcenter                                 %! EXPLICIT_MARGIN_MARKUP_ALERT:SM10
                                            %%%                     ]                                    %! EXPLICIT_MARGIN_MARKUP_ALERT:SM10
                                            %%%             }                                            %! EXPLICIT_MARGIN_MARKUP_ALERT:SM10
                                            %%%     }                                                    %! EXPLICIT_MARGIN_MARKUP_ALERT:SM10
                                            \line                                                        %! EXPLICIT_MARGIN_MARKUP_ALERT_WITH_COLOR:SM11
                                                {                                                        %! EXPLICIT_MARGIN_MARKUP_ALERT_WITH_COLOR:SM11
                                                    \with-color                                          %! EXPLICIT_MARGIN_MARKUP_ALERT_WITH_COLOR:SM11
                                                        #(x11-color 'blue)                               %! EXPLICIT_MARGIN_MARKUP_ALERT_WITH_COLOR:SM11
                                                        {                                                %! EXPLICIT_MARGIN_MARKUP_ALERT_WITH_COLOR:SM11
                                                            \vcenter                                     %! EXPLICIT_MARGIN_MARKUP_ALERT_WITH_COLOR:SM11
                                                                [“III+IV”                                %! EXPLICIT_MARGIN_MARKUP_ALERT_WITH_COLOR:SM11
                                                            \vcenter                                     %! EXPLICIT_MARGIN_MARKUP_ALERT_WITH_COLOR:SM11
                                                                III+IV                                   %! EXPLICIT_MARGIN_MARKUP_ALERT_WITH_COLOR:SM11
                                                            \concat                                      %! EXPLICIT_MARGIN_MARKUP_ALERT_WITH_COLOR:SM11
                                                                {                                        %! EXPLICIT_MARGIN_MARKUP_ALERT_WITH_COLOR:SM11
                                                                    \vcenter                             %! EXPLICIT_MARGIN_MARKUP_ALERT_WITH_COLOR:SM11
                                                                        III+IV                           %! EXPLICIT_MARGIN_MARKUP_ALERT_WITH_COLOR:SM11
                                                                    \vcenter                             %! EXPLICIT_MARGIN_MARKUP_ALERT_WITH_COLOR:SM11
                                                                        ]                                %! EXPLICIT_MARGIN_MARKUP_ALERT_WITH_COLOR:SM11
                                                                }                                        %! EXPLICIT_MARGIN_MARKUP_ALERT_WITH_COLOR:SM11
                                                        }                                                %! EXPLICIT_MARGIN_MARKUP_ALERT_WITH_COLOR:SM11
                                                }                                                        %! EXPLICIT_MARGIN_MARKUP_ALERT_WITH_COLOR:SM11
                                        }
                                    }
                                \set Staff.instrumentName = \markup { III+IV }                           %! REDRAWN_EXPLICIT_MARGIN_MARKUP:SM8
                                \set Staff.shortInstrumentName = \markup { III+IV }                      %! REDRAWN_EXPLICIT_MARGIN_MARKUP:SM8
                                \override Staff.InstrumentName.color = #(x11-color 'DeepSkyBlue2)        %! REDRAWN_EXPLICIT_MARGIN_MARKUP_COLOR:SM6
                <BLANKLINE>
                                % MusicVoice [measure 2]                                                 %! SM4
                                c'4.
                <BLANKLINE>
                            }
                        }
                    >>
                >>

        ..  container:: example

            Reapplied margin markup color green and redraw dull green:

            >>> maker = baca.SegmentMaker(
            ...     ignore_unpitched_notes=True,
            ...     layout_measure_map=layout_measure_map,
            ...     margin_markup=margin_markup,
            ...     score_template=baca.SingleStaffScoreTemplate(),
            ...     spacing_specifier=baca.minimum_width((1, 24)),
            ...     time_signatures=[(3, 8), (3, 8)],
            ...     )
            >>> maker(
            ...     baca.scope('MusicVoice', 1),
            ...     baca.make_notes(),
            ...     )

            >>> metadata = {}
            >>> metadata['persistent_indicators'] = {}
            >>> metadata['persistent_indicators']['MusicStaff'] = [
            ...     abjad.Momento(
            ...         context='MusicVoice',
            ...         prototype='baca.MarginMarkup',
            ...         value='I+II',
            ...         )
            ...     ]
            >>> metadata['segment_number'] = 1
            >>> lilypond_file = maker.run(
            ...     environment='docs',
            ...     previous_metadata=metadata,
            ...     remove=remove,
            ...     )
            >>> block = abjad.Block(name='layout')
            >>> block.indent = 0
            >>> lilypond_file.items.insert(0, block)
            >>> abjad.show(lilypond_file, strict=89) # doctest: +SKIP

            ..  docs::

                >>> abjad.f(lilypond_file[abjad.Score], strict=89)
                \context Score = "Score" <<
                    \context GlobalContext = "GlobalContext" <<
                        \context GlobalSkips = "GlobalSkips" {
                <BLANKLINE>
                            % GlobalSkips [measure 1]                                                    %! SM4
                            \autoPageBreaksOff                                                           %! SEGMENT:LAYOUT:LMM1
                            \noBreak                                                                     %! SEGMENT:LAYOUT:LMM2
                            \overrideProperty Score.NonMusicalPaperColumn.line-break-system-details      %! SEGMENT:LAYOUT:LMM3
                            #'((Y-offset . 0) (alignment-distances . (11)))                              %! SEGMENT:LAYOUT:LMM3
                            \time 3/8                                                                    %! EXPLICIT_TIME_SIGNATURE:SM8
                            \mark #1                                                                     %! SM9
                            \bar ""                                                                      %! EMPTY_START_BAR:SM2
                            \once \override Score.TimeSignature.color = #(x11-color 'blue)               %! EXPLICIT_TIME_SIGNATURE_COLOR:SM6
                            \newSpacingSection                                                           %! SEGMENT:SPACING:HSS1
                            \set Score.proportionalNotationDuration = #(ly:make-moment 1 24)             %! SEGMENT:SPACING:HSS1
                            \pageBreak                                                                   %! SEGMENT:LAYOUT:LMM3
                            s1 * 3/8
                <BLANKLINE>
                            % GlobalSkips [measure 2]                                                    %! SM4
                            \noBreak                                                                     %! SEGMENT:LAYOUT:LMM2
                            \overrideProperty Score.NonMusicalPaperColumn.line-break-system-details      %! SEGMENT:LAYOUT:LMM3
                            #'((Y-offset . 20) (alignment-distances . (11)))                             %! SEGMENT:LAYOUT:LMM3
                            \once \override Score.TimeSignature.color = #(x11-color 'DeepPink1)          %! REDUNDANT_TIME_SIGNATURE_COLOR:SM6
                            \newSpacingSection                                                           %! SEGMENT:SPACING:HSS1
                            \set Score.proportionalNotationDuration = #(ly:make-moment 1 24)             %! SEGMENT:SPACING:HSS1
                            \break                                                                       %! SEGMENT:LAYOUT:LMM3
                            s1 * 3/8
                            \override Score.BarLine.transparent = ##f                                    %! SM5
                            \bar "|"                                                                     %! SM5
                <BLANKLINE>
                        }
                    >>
                    \context MusicContext = "MusicContext" <<
                        \context Staff = "MusicStaff" {
                            \context Voice = "MusicVoice" {
                <BLANKLINE>
                                % MusicVoice [measure 1]                                                 %! SM4
                                \set Staff.instrumentName = \markup { I+II }                             %! REAPPLIED_MARGIN_MARKUP:SM8
                                \set Staff.shortInstrumentName = \markup { I+II }                        %! REAPPLIED_MARGIN_MARKUP:SM8
                                \once \override Staff.InstrumentName.color = #(x11-color 'green4)        %! REAPPLIED_MARGIN_MARKUP_COLOR:SM6
                                c'4.
                                ^ \markup {
                                    \column
                                        {
                                            %%% \line                                                    %! REAPPLIED_MARGIN_MARKUP_ALERT:SM10
                                            %%%     {                                                    %! REAPPLIED_MARGIN_MARKUP_ALERT:SM10
                                            %%%         \vcenter                                         %! REAPPLIED_MARGIN_MARKUP_ALERT:SM10
                                            %%%             [“I+II”                                      %! REAPPLIED_MARGIN_MARKUP_ALERT:SM10
                                            %%%         \vcenter                                         %! REAPPLIED_MARGIN_MARKUP_ALERT:SM10
                                            %%%             I+II                                         %! REAPPLIED_MARGIN_MARKUP_ALERT:SM10
                                            %%%         \concat                                          %! REAPPLIED_MARGIN_MARKUP_ALERT:SM10
                                            %%%             {                                            %! REAPPLIED_MARGIN_MARKUP_ALERT:SM10
                                            %%%                 \vcenter                                 %! REAPPLIED_MARGIN_MARKUP_ALERT:SM10
                                            %%%                     I+II                                 %! REAPPLIED_MARGIN_MARKUP_ALERT:SM10
                                            %%%                 \vcenter                                 %! REAPPLIED_MARGIN_MARKUP_ALERT:SM10
                                            %%%                     ]                                    %! REAPPLIED_MARGIN_MARKUP_ALERT:SM10
                                            %%%             }                                            %! REAPPLIED_MARGIN_MARKUP_ALERT:SM10
                                            %%%     }                                                    %! REAPPLIED_MARGIN_MARKUP_ALERT:SM10
                                            \line                                                        %! REAPPLIED_MARGIN_MARKUP_ALERT_WITH_COLOR:SM11
                                                {                                                        %! REAPPLIED_MARGIN_MARKUP_ALERT_WITH_COLOR:SM11
                                                    \with-color                                          %! REAPPLIED_MARGIN_MARKUP_ALERT_WITH_COLOR:SM11
                                                        #(x11-color 'green4)                             %! REAPPLIED_MARGIN_MARKUP_ALERT_WITH_COLOR:SM11
                                                        {                                                %! REAPPLIED_MARGIN_MARKUP_ALERT_WITH_COLOR:SM11
                                                            \vcenter                                     %! REAPPLIED_MARGIN_MARKUP_ALERT_WITH_COLOR:SM11
                                                                [“I+II”                                  %! REAPPLIED_MARGIN_MARKUP_ALERT_WITH_COLOR:SM11
                                                            \vcenter                                     %! REAPPLIED_MARGIN_MARKUP_ALERT_WITH_COLOR:SM11
                                                                I+II                                     %! REAPPLIED_MARGIN_MARKUP_ALERT_WITH_COLOR:SM11
                                                            \concat                                      %! REAPPLIED_MARGIN_MARKUP_ALERT_WITH_COLOR:SM11
                                                                {                                        %! REAPPLIED_MARGIN_MARKUP_ALERT_WITH_COLOR:SM11
                                                                    \vcenter                             %! REAPPLIED_MARGIN_MARKUP_ALERT_WITH_COLOR:SM11
                                                                        I+II                             %! REAPPLIED_MARGIN_MARKUP_ALERT_WITH_COLOR:SM11
                                                                    \vcenter                             %! REAPPLIED_MARGIN_MARKUP_ALERT_WITH_COLOR:SM11
                                                                        ]                                %! REAPPLIED_MARGIN_MARKUP_ALERT_WITH_COLOR:SM11
                                                                }                                        %! REAPPLIED_MARGIN_MARKUP_ALERT_WITH_COLOR:SM11
                                                        }                                                %! REAPPLIED_MARGIN_MARKUP_ALERT_WITH_COLOR:SM11
                                                }                                                        %! REAPPLIED_MARGIN_MARKUP_ALERT_WITH_COLOR:SM11
                                        }
                                    }
                                \set Staff.instrumentName = \markup { I+II }                             %! REDRAWN_REAPPLIED_MARGIN_MARKUP:SM8
                                \set Staff.shortInstrumentName = \markup { I+II }                        %! REDRAWN_REAPPLIED_MARGIN_MARKUP:SM8
                                \override Staff.InstrumentName.color = #(x11-color 'OliveDrab)           %! REDRAWN_REAPPLIED_MARGIN_MARKUP_COLOR:SM6
                <BLANKLINE>
                                % MusicVoice [measure 2]                                                 %! SM4
                                c'4.
                <BLANKLINE>
                            }
                        }
                    >>
                >>

        ..  container:: example

            Redundant margin markup color pink and redraw dull pink:

            >>> layout_measure_map = baca.layout(
            ...     baca.page(
            ...         [1, 0, (11,)],
            ...         [3, 20, (11,)],
            ...         ),
            ...     )
            >>> maker = baca.SegmentMaker(
            ...     ignore_unpitched_notes=True,
            ...     layout_measure_map=layout_measure_map,
            ...     margin_markup=margin_markup,
            ...     score_template=baca.SingleStaffScoreTemplate(),
            ...     spacing_specifier=baca.minimum_width((1, 24)),
            ...     time_signatures=[(4, 8), (4, 8), (4, 8)],
            ...     )
            >>> maker(
            ...     baca.scope('MusicVoice', 1),
            ...     baca.margin_markup(margin_markup['I+II']),
            ...     baca.map(
            ...         baca.margin_markup(margin_markup['I+II']),
            ...         baca.leaves()[1],
            ...         ),
            ...     baca.make_notes(),
            ...     )

            >>> lilypond_file = maker.run(
            ...     environment='docs',
            ...     remove=remove,
            ...     )
            >>> block = abjad.Block(name='layout')
            >>> block.indent = 0
            >>> lilypond_file.items.insert(0, block)
            >>> abjad.show(lilypond_file, strict=89) # doctest: +SKIP

            ..  docs::

                >>> abjad.f(lilypond_file[abjad.Score], strict=89)
                \context Score = "Score" <<
                    \context GlobalContext = "GlobalContext" <<
                        \context GlobalSkips = "GlobalSkips" {
                <BLANKLINE>
                            % GlobalSkips [measure 1]                                                    %! SM4
                            \autoPageBreaksOff                                                           %! SEGMENT:LAYOUT:LMM1
                            \noBreak                                                                     %! SEGMENT:LAYOUT:LMM2
                            \overrideProperty Score.NonMusicalPaperColumn.line-break-system-details      %! SEGMENT:LAYOUT:LMM3
                            #'((Y-offset . 0) (alignment-distances . (11)))                              %! SEGMENT:LAYOUT:LMM3
                            \time 4/8                                                                    %! EXPLICIT_TIME_SIGNATURE:SM8
                            \bar ""                                                                      %! EMPTY_START_BAR:SM2
                            \once \override Score.TimeSignature.color = #(x11-color 'blue)               %! EXPLICIT_TIME_SIGNATURE_COLOR:SM6
                            \newSpacingSection                                                           %! SEGMENT:SPACING:HSS1
                            \set Score.proportionalNotationDuration = #(ly:make-moment 1 24)             %! SEGMENT:SPACING:HSS1
                            \pageBreak                                                                   %! SEGMENT:LAYOUT:LMM3
                            s1 * 1/2
                <BLANKLINE>
                            % GlobalSkips [measure 2]                                                    %! SM4
                            \noBreak                                                                     %! SEGMENT:LAYOUT:LMM2
                            \once \override Score.TimeSignature.color = #(x11-color 'DeepPink1)          %! REDUNDANT_TIME_SIGNATURE_COLOR:SM6
                            \newSpacingSection                                                           %! SEGMENT:SPACING:HSS1
                            \set Score.proportionalNotationDuration = #(ly:make-moment 1 24)             %! SEGMENT:SPACING:HSS1
                            s1 * 1/2
                <BLANKLINE>
                            % GlobalSkips [measure 3]                                                    %! SM4
                            \noBreak                                                                     %! SEGMENT:LAYOUT:LMM2
                            \overrideProperty Score.NonMusicalPaperColumn.line-break-system-details      %! SEGMENT:LAYOUT:LMM3
                            #'((Y-offset . 20) (alignment-distances . (11)))                             %! SEGMENT:LAYOUT:LMM3
                            \once \override Score.TimeSignature.color = #(x11-color 'DeepPink1)          %! REDUNDANT_TIME_SIGNATURE_COLOR:SM6
                            \newSpacingSection                                                           %! SEGMENT:SPACING:HSS1
                            \set Score.proportionalNotationDuration = #(ly:make-moment 1 24)             %! SEGMENT:SPACING:HSS1
                            \break                                                                       %! SEGMENT:LAYOUT:LMM3
                            s1 * 1/2
                            \override Score.BarLine.transparent = ##f                                    %! SM5
                            \bar "|"                                                                     %! SM5
                <BLANKLINE>
                        }
                    >>
                    \context MusicContext = "MusicContext" <<
                        \context Staff = "MusicStaff" {
                            \context Voice = "MusicVoice" {
                <BLANKLINE>
                                % MusicVoice [measure 1]                                                 %! SM4
                                \set Staff.instrumentName = \markup { I+II }                             %! EXPLICIT_MARGIN_MARKUP:SM8
                                \set Staff.shortInstrumentName = \markup { I+II }                        %! EXPLICIT_MARGIN_MARKUP:SM8
                                \once \override Staff.InstrumentName.color = #(x11-color 'blue)          %! EXPLICIT_MARGIN_MARKUP_COLOR:SM6
                                c'2
                                ^ \markup {
                                    \column
                                        {
                                            %%% \line                                                    %! EXPLICIT_MARGIN_MARKUP_ALERT:SM10
                                            %%%     {                                                    %! EXPLICIT_MARGIN_MARKUP_ALERT:SM10
                                            %%%         \vcenter                                         %! EXPLICIT_MARGIN_MARKUP_ALERT:SM10
                                            %%%             [“I+II”                                      %! EXPLICIT_MARGIN_MARKUP_ALERT:SM10
                                            %%%         \vcenter                                         %! EXPLICIT_MARGIN_MARKUP_ALERT:SM10
                                            %%%             I+II                                         %! EXPLICIT_MARGIN_MARKUP_ALERT:SM10
                                            %%%         \concat                                          %! EXPLICIT_MARGIN_MARKUP_ALERT:SM10
                                            %%%             {                                            %! EXPLICIT_MARGIN_MARKUP_ALERT:SM10
                                            %%%                 \vcenter                                 %! EXPLICIT_MARGIN_MARKUP_ALERT:SM10
                                            %%%                     I+II                                 %! EXPLICIT_MARGIN_MARKUP_ALERT:SM10
                                            %%%                 \vcenter                                 %! EXPLICIT_MARGIN_MARKUP_ALERT:SM10
                                            %%%                     ]                                    %! EXPLICIT_MARGIN_MARKUP_ALERT:SM10
                                            %%%             }                                            %! EXPLICIT_MARGIN_MARKUP_ALERT:SM10
                                            %%%     }                                                    %! EXPLICIT_MARGIN_MARKUP_ALERT:SM10
                                            \line                                                        %! EXPLICIT_MARGIN_MARKUP_ALERT_WITH_COLOR:SM11
                                                {                                                        %! EXPLICIT_MARGIN_MARKUP_ALERT_WITH_COLOR:SM11
                                                    \with-color                                          %! EXPLICIT_MARGIN_MARKUP_ALERT_WITH_COLOR:SM11
                                                        #(x11-color 'blue)                               %! EXPLICIT_MARGIN_MARKUP_ALERT_WITH_COLOR:SM11
                                                        {                                                %! EXPLICIT_MARGIN_MARKUP_ALERT_WITH_COLOR:SM11
                                                            \vcenter                                     %! EXPLICIT_MARGIN_MARKUP_ALERT_WITH_COLOR:SM11
                                                                [“I+II”                                  %! EXPLICIT_MARGIN_MARKUP_ALERT_WITH_COLOR:SM11
                                                            \vcenter                                     %! EXPLICIT_MARGIN_MARKUP_ALERT_WITH_COLOR:SM11
                                                                I+II                                     %! EXPLICIT_MARGIN_MARKUP_ALERT_WITH_COLOR:SM11
                                                            \concat                                      %! EXPLICIT_MARGIN_MARKUP_ALERT_WITH_COLOR:SM11
                                                                {                                        %! EXPLICIT_MARGIN_MARKUP_ALERT_WITH_COLOR:SM11
                                                                    \vcenter                             %! EXPLICIT_MARGIN_MARKUP_ALERT_WITH_COLOR:SM11
                                                                        I+II                             %! EXPLICIT_MARGIN_MARKUP_ALERT_WITH_COLOR:SM11
                                                                    \vcenter                             %! EXPLICIT_MARGIN_MARKUP_ALERT_WITH_COLOR:SM11
                                                                        ]                                %! EXPLICIT_MARGIN_MARKUP_ALERT_WITH_COLOR:SM11
                                                                }                                        %! EXPLICIT_MARGIN_MARKUP_ALERT_WITH_COLOR:SM11
                                                        }                                                %! EXPLICIT_MARGIN_MARKUP_ALERT_WITH_COLOR:SM11
                                                }                                                        %! EXPLICIT_MARGIN_MARKUP_ALERT_WITH_COLOR:SM11
                                        }
                                    }
                                \set Staff.instrumentName = \markup { I+II }                             %! REDRAWN_EXPLICIT_MARGIN_MARKUP:SM8
                                \set Staff.shortInstrumentName = \markup { I+II }                        %! REDRAWN_EXPLICIT_MARGIN_MARKUP:SM8
                                \override Staff.InstrumentName.color = #(x11-color 'DeepSkyBlue2)        %! REDRAWN_EXPLICIT_MARGIN_MARKUP_COLOR:SM6
                <BLANKLINE>
                                % MusicVoice [measure 2]                                                 %! SM4
                                \set Staff.instrumentName = \markup { I+II }                             %! REDUNDANT_MARGIN_MARKUP:SM8
                                \set Staff.shortInstrumentName = \markup { I+II }                        %! REDUNDANT_MARGIN_MARKUP:SM8
                                \once \override Staff.InstrumentName.color = #(x11-color 'DeepPink1)     %! REDUNDANT_MARGIN_MARKUP_COLOR:SM6
                                c'2
                                ^ \markup {
                                    \column
                                        {
                                            %%% \line                                                    %! REDUNDANT_MARGIN_MARKUP_ALERT:SM10
                                            %%%     {                                                    %! REDUNDANT_MARGIN_MARKUP_ALERT:SM10
                                            %%%         \vcenter                                         %! REDUNDANT_MARGIN_MARKUP_ALERT:SM10
                                            %%%             [“I+II”                                      %! REDUNDANT_MARGIN_MARKUP_ALERT:SM10
                                            %%%         \vcenter                                         %! REDUNDANT_MARGIN_MARKUP_ALERT:SM10
                                            %%%             I+II                                         %! REDUNDANT_MARGIN_MARKUP_ALERT:SM10
                                            %%%         \concat                                          %! REDUNDANT_MARGIN_MARKUP_ALERT:SM10
                                            %%%             {                                            %! REDUNDANT_MARGIN_MARKUP_ALERT:SM10
                                            %%%                 \vcenter                                 %! REDUNDANT_MARGIN_MARKUP_ALERT:SM10
                                            %%%                     I+II                                 %! REDUNDANT_MARGIN_MARKUP_ALERT:SM10
                                            %%%                 \vcenter                                 %! REDUNDANT_MARGIN_MARKUP_ALERT:SM10
                                            %%%                     ]                                    %! REDUNDANT_MARGIN_MARKUP_ALERT:SM10
                                            %%%             }                                            %! REDUNDANT_MARGIN_MARKUP_ALERT:SM10
                                            %%%     }                                                    %! REDUNDANT_MARGIN_MARKUP_ALERT:SM10
                                            \line                                                        %! REDUNDANT_MARGIN_MARKUP_ALERT_WITH_COLOR:SM11
                                                {                                                        %! REDUNDANT_MARGIN_MARKUP_ALERT_WITH_COLOR:SM11
                                                    \with-color                                          %! REDUNDANT_MARGIN_MARKUP_ALERT_WITH_COLOR:SM11
                                                        #(x11-color 'DeepPink1)                          %! REDUNDANT_MARGIN_MARKUP_ALERT_WITH_COLOR:SM11
                                                        {                                                %! REDUNDANT_MARGIN_MARKUP_ALERT_WITH_COLOR:SM11
                                                            \vcenter                                     %! REDUNDANT_MARGIN_MARKUP_ALERT_WITH_COLOR:SM11
                                                                [“I+II”                                  %! REDUNDANT_MARGIN_MARKUP_ALERT_WITH_COLOR:SM11
                                                            \vcenter                                     %! REDUNDANT_MARGIN_MARKUP_ALERT_WITH_COLOR:SM11
                                                                I+II                                     %! REDUNDANT_MARGIN_MARKUP_ALERT_WITH_COLOR:SM11
                                                            \concat                                      %! REDUNDANT_MARGIN_MARKUP_ALERT_WITH_COLOR:SM11
                                                                {                                        %! REDUNDANT_MARGIN_MARKUP_ALERT_WITH_COLOR:SM11
                                                                    \vcenter                             %! REDUNDANT_MARGIN_MARKUP_ALERT_WITH_COLOR:SM11
                                                                        I+II                             %! REDUNDANT_MARGIN_MARKUP_ALERT_WITH_COLOR:SM11
                                                                    \vcenter                             %! REDUNDANT_MARGIN_MARKUP_ALERT_WITH_COLOR:SM11
                                                                        ]                                %! REDUNDANT_MARGIN_MARKUP_ALERT_WITH_COLOR:SM11
                                                                }                                        %! REDUNDANT_MARGIN_MARKUP_ALERT_WITH_COLOR:SM11
                                                        }                                                %! REDUNDANT_MARGIN_MARKUP_ALERT_WITH_COLOR:SM11
                                                }                                                        %! REDUNDANT_MARGIN_MARKUP_ALERT_WITH_COLOR:SM11
                                        }
                                    }
                                \set Staff.instrumentName = \markup { I+II }                             %! REDRAWN_REDUNDANT_MARGIN_MARKUP:SM8
                                \set Staff.shortInstrumentName = \markup { I+II }                        %! REDRAWN_REDUNDANT_MARGIN_MARKUP:SM8
                                \override Staff.InstrumentName.color = #(x11-color 'DeepPink4)           %! REDRAWN_REDUNDANT_MARGIN_MARKUP_COLOR:SM6
                <BLANKLINE>
                                % MusicVoice [measure 3]                                                 %! SM4
                                c'2
                <BLANKLINE>
                            }
                        }
                    >>
                >>

            Even at the beginning of a segment:

            >>> layout_measure_map = baca.layout(
            ...     baca.page(
            ...         [1, 0, (11,)],
            ...         [2, 20, (11,)],
            ...         ),
            ...     )
            >>> maker = baca.SegmentMaker(
            ...     ignore_unpitched_notes=True,
            ...     layout_measure_map=layout_measure_map,
            ...     margin_markup=margin_markup,
            ...     score_template=baca.SingleStaffScoreTemplate(),
            ...     spacing_specifier=baca.minimum_width((1, 24)),
            ...     time_signatures=[(3, 8), (3, 8)],
            ...     )
            >>> maker(
            ...     baca.scope('MusicVoice', 1),
            ...     baca.margin_markup(margin_markup['I+II']),
            ...     baca.make_notes(),
            ...     )

            >>> metadata = {}
            >>> metadata['persistent_indicators'] = {}
            >>> metadata['persistent_indicators']['MusicStaff'] = [
            ...     abjad.Momento(
            ...         context='MusicVoice',
            ...         prototype='baca.MarginMarkup',
            ...         value='I+II',
            ...         )
            ...     ]
            >>> metadata['segment_number'] = 1
            >>> lilypond_file = maker.run(
            ...     environment='docs',
            ...     previous_metadata=metadata,
            ...     remove=remove,
            ...     )
            >>> block = abjad.Block(name='layout')
            >>> block.indent = 0
            >>> lilypond_file.items.insert(0, block)
            >>> abjad.show(lilypond_file, strict=89) # doctest: +SKIP

            ..  docs::

                >>> abjad.f(lilypond_file[abjad.Score], strict=89)
                \context Score = "Score" <<
                    \context GlobalContext = "GlobalContext" <<
                        \context GlobalSkips = "GlobalSkips" {
                <BLANKLINE>
                            % GlobalSkips [measure 1]                                                    %! SM4
                            \autoPageBreaksOff                                                           %! SEGMENT:LAYOUT:LMM1
                            \noBreak                                                                     %! SEGMENT:LAYOUT:LMM2
                            \overrideProperty Score.NonMusicalPaperColumn.line-break-system-details      %! SEGMENT:LAYOUT:LMM3
                            #'((Y-offset . 0) (alignment-distances . (11)))                              %! SEGMENT:LAYOUT:LMM3
                            \time 3/8                                                                    %! EXPLICIT_TIME_SIGNATURE:SM8
                            \mark #1                                                                     %! SM9
                            \bar ""                                                                      %! EMPTY_START_BAR:SM2
                            \once \override Score.TimeSignature.color = #(x11-color 'blue)               %! EXPLICIT_TIME_SIGNATURE_COLOR:SM6
                            \newSpacingSection                                                           %! SEGMENT:SPACING:HSS1
                            \set Score.proportionalNotationDuration = #(ly:make-moment 1 24)             %! SEGMENT:SPACING:HSS1
                            \pageBreak                                                                   %! SEGMENT:LAYOUT:LMM3
                            s1 * 3/8
                <BLANKLINE>
                            % GlobalSkips [measure 2]                                                    %! SM4
                            \noBreak                                                                     %! SEGMENT:LAYOUT:LMM2
                            \overrideProperty Score.NonMusicalPaperColumn.line-break-system-details      %! SEGMENT:LAYOUT:LMM3
                            #'((Y-offset . 20) (alignment-distances . (11)))                             %! SEGMENT:LAYOUT:LMM3
                            \once \override Score.TimeSignature.color = #(x11-color 'DeepPink1)          %! REDUNDANT_TIME_SIGNATURE_COLOR:SM6
                            \newSpacingSection                                                           %! SEGMENT:SPACING:HSS1
                            \set Score.proportionalNotationDuration = #(ly:make-moment 1 24)             %! SEGMENT:SPACING:HSS1
                            \break                                                                       %! SEGMENT:LAYOUT:LMM3
                            s1 * 3/8
                            \override Score.BarLine.transparent = ##f                                    %! SM5
                            \bar "|"                                                                     %! SM5
                <BLANKLINE>
                        }
                    >>
                    \context MusicContext = "MusicContext" <<
                        \context Staff = "MusicStaff" {
                            \context Voice = "MusicVoice" {
                <BLANKLINE>
                                % MusicVoice [measure 1]                                                 %! SM4
                                \set Staff.instrumentName = \markup { I+II }                             %! REDUNDANT_MARGIN_MARKUP:SM8
                                \set Staff.shortInstrumentName = \markup { I+II }                        %! REDUNDANT_MARGIN_MARKUP:SM8
                                \once \override Staff.InstrumentName.color = #(x11-color 'DeepPink1)     %! REDUNDANT_MARGIN_MARKUP_COLOR:SM6
                                c'4.
                                ^ \markup {
                                    \column
                                        {
                                            %%% \line                                                    %! REDUNDANT_MARGIN_MARKUP_ALERT:SM10
                                            %%%     {                                                    %! REDUNDANT_MARGIN_MARKUP_ALERT:SM10
                                            %%%         \vcenter                                         %! REDUNDANT_MARGIN_MARKUP_ALERT:SM10
                                            %%%             [“I+II”                                      %! REDUNDANT_MARGIN_MARKUP_ALERT:SM10
                                            %%%         \vcenter                                         %! REDUNDANT_MARGIN_MARKUP_ALERT:SM10
                                            %%%             I+II                                         %! REDUNDANT_MARGIN_MARKUP_ALERT:SM10
                                            %%%         \concat                                          %! REDUNDANT_MARGIN_MARKUP_ALERT:SM10
                                            %%%             {                                            %! REDUNDANT_MARGIN_MARKUP_ALERT:SM10
                                            %%%                 \vcenter                                 %! REDUNDANT_MARGIN_MARKUP_ALERT:SM10
                                            %%%                     I+II                                 %! REDUNDANT_MARGIN_MARKUP_ALERT:SM10
                                            %%%                 \vcenter                                 %! REDUNDANT_MARGIN_MARKUP_ALERT:SM10
                                            %%%                     ]                                    %! REDUNDANT_MARGIN_MARKUP_ALERT:SM10
                                            %%%             }                                            %! REDUNDANT_MARGIN_MARKUP_ALERT:SM10
                                            %%%     }                                                    %! REDUNDANT_MARGIN_MARKUP_ALERT:SM10
                                            \line                                                        %! REDUNDANT_MARGIN_MARKUP_ALERT_WITH_COLOR:SM11
                                                {                                                        %! REDUNDANT_MARGIN_MARKUP_ALERT_WITH_COLOR:SM11
                                                    \with-color                                          %! REDUNDANT_MARGIN_MARKUP_ALERT_WITH_COLOR:SM11
                                                        #(x11-color 'DeepPink1)                          %! REDUNDANT_MARGIN_MARKUP_ALERT_WITH_COLOR:SM11
                                                        {                                                %! REDUNDANT_MARGIN_MARKUP_ALERT_WITH_COLOR:SM11
                                                            \vcenter                                     %! REDUNDANT_MARGIN_MARKUP_ALERT_WITH_COLOR:SM11
                                                                [“I+II”                                  %! REDUNDANT_MARGIN_MARKUP_ALERT_WITH_COLOR:SM11
                                                            \vcenter                                     %! REDUNDANT_MARGIN_MARKUP_ALERT_WITH_COLOR:SM11
                                                                I+II                                     %! REDUNDANT_MARGIN_MARKUP_ALERT_WITH_COLOR:SM11
                                                            \concat                                      %! REDUNDANT_MARGIN_MARKUP_ALERT_WITH_COLOR:SM11
                                                                {                                        %! REDUNDANT_MARGIN_MARKUP_ALERT_WITH_COLOR:SM11
                                                                    \vcenter                             %! REDUNDANT_MARGIN_MARKUP_ALERT_WITH_COLOR:SM11
                                                                        I+II                             %! REDUNDANT_MARGIN_MARKUP_ALERT_WITH_COLOR:SM11
                                                                    \vcenter                             %! REDUNDANT_MARGIN_MARKUP_ALERT_WITH_COLOR:SM11
                                                                        ]                                %! REDUNDANT_MARGIN_MARKUP_ALERT_WITH_COLOR:SM11
                                                                }                                        %! REDUNDANT_MARGIN_MARKUP_ALERT_WITH_COLOR:SM11
                                                        }                                                %! REDUNDANT_MARGIN_MARKUP_ALERT_WITH_COLOR:SM11
                                                }                                                        %! REDUNDANT_MARGIN_MARKUP_ALERT_WITH_COLOR:SM11
                                        }
                                    }
                                \set Staff.instrumentName = \markup { I+II }                             %! REDRAWN_REDUNDANT_MARGIN_MARKUP:SM8
                                \set Staff.shortInstrumentName = \markup { I+II }                        %! REDRAWN_REDUNDANT_MARGIN_MARKUP:SM8
                                \override Staff.InstrumentName.color = #(x11-color 'DeepPink4)           %! REDRAWN_REDUNDANT_MARGIN_MARKUP_COLOR:SM6
                <BLANKLINE>
                                % MusicVoice [measure 2]                                                 %! SM4
                                c'4.
                <BLANKLINE>
                            }
                        }
                    >>
                >>

        Returns ordered dictionary or none.
        '''
        return self._margin_markup

    @property
    def measure_count(self):
        r'''Gets measure count.

        Returns nonnegative integer.
        '''
        return len(self.time_signatures)

    @property
    def measures_per_stage(self):
        r'''Gets measures per stage.

        Groups all measures into a single stage when `measures_per_stage` is
        none.

        Set to list of positive integers or none.

        Returns list of positive integers or none.
        '''
        if self._measures_per_stage is None:
            return [len(self.time_signatures)]
        return self._measures_per_stage

    @property
    def metadata(self):
        r'''Gets segment metadata.

        ..  container:: example

            >>> metadata = {}
            >>> metadata['persistent_indicators'] = {}
            >>> metadata['persistent_indicators']['MusicStaff'] = [
            ...     abjad.Momento(
            ...         context='MusicVoice',
            ...         prototype='abjad.Clef',
            ...         value='alto',
            ...         )
            ...     ]
            >>> metadata['segment_number'] = 1
            >>> maker = baca.SegmentMaker(
            ...     score_template=baca.SingleStaffScoreTemplate(),
            ...     time_signatures=[(4, 8), (3, 8), (4, 8), (3, 8)],
            ...     )

            >>> lilypond_file = maker.run(
            ...     environment='docs',
            ...     previous_metadata=metadata,
            ...     )

            >>> abjad.show(lilypond_file, strict=89) # doctest: +SKIP

            ..  docs::

                >>> abjad.f(lilypond_file[abjad.Score], strict=89)
                \context Score = "Score" <<
                    \context GlobalContext = "GlobalContext" <<
                        \context GlobalSkips = "GlobalSkips" {
                <BLANKLINE>
                            % GlobalSkips [measure 1]                                                    %! SM4
                            \time 4/8                                                                    %! EXPLICIT_TIME_SIGNATURE:SM8
                            \mark #1                                                                     %! SM9
                            \bar ""                                                                      %! EMPTY_START_BAR:SM2
                            \once \override Score.TimeSignature.color = #(x11-color 'blue)               %! EXPLICIT_TIME_SIGNATURE_COLOR:SM6
                            s1 * 1/2
                            ^ \markup {                                                                  %! STAGE_NUMBER_MARKUP:SM3
                                \fontsize                                                                %! STAGE_NUMBER_MARKUP:SM3
                                    #-3                                                                  %! STAGE_NUMBER_MARKUP:SM3
                                    \with-color                                                          %! STAGE_NUMBER_MARKUP:SM3
                                        #(x11-color 'DarkCyan)                                           %! STAGE_NUMBER_MARKUP:SM3
                                        [A.1]                                                            %! STAGE_NUMBER_MARKUP:SM3
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
                            \override Score.BarLine.transparent = ##f                                    %! SM5
                            \bar "|"                                                                     %! SM5
                <BLANKLINE>
                        }
                    >>
                    \context MusicContext = "MusicContext" <<
                        \context Staff = "MusicStaff" {
                            \context Voice = "MusicVoice" {
                <BLANKLINE>
                                % MusicVoice [measure 1]                                                 %! SM4
                                \set Staff.forceClef = ##t                                               %! REAPPLIED_CLEF:SM8
                                \clef "alto"                                                             %! REAPPLIED_CLEF:SM8
                                \once \override Staff.Clef.color = #(x11-color 'green4)                  %! REAPPLIED_CLEF_COLOR:SM6
                                %%% \override Staff.Clef.color = ##f                                     %! REAPPLIED_CLEF_COLOR_CANCELLATION:SM7
                                R1 * 1/2
                                \override Staff.Clef.color = #(x11-color 'OliveDrab)                     %! REAPPLIED_CLEF_REDRAW_COLOR:SM6
                <BLANKLINE>
                                % MusicVoice [measure 2]                                                 %! SM4
                                R1 * 3/8
                <BLANKLINE>
                                % MusicVoice [measure 3]                                                 %! SM4
                                R1 * 1/2
                <BLANKLINE>
                                % MusicVoice [measure 4]                                                 %! SM4
                                R1 * 3/8
                <BLANKLINE>
                            }
                        }
                    >>
                >>

            >>> abjad.f(maker.metadata, strict=89)
            abjad.TypedOrderedDict(
                [
                    ('duration', None),
                    ('first_measure_number', 1),
                    (
                        'persistent_indicators',
                        abjad.TypedOrderedDict(
                            [
                                (
                                    'MusicStaff',
                                    [
                                        abjad.Momento(
                                            context='MusicVoice',
                                            prototype='abjad.Clef',
                                            value='alto',
                                            ),
                                        ],
                                    ),
                                (
                                    'Score',
                                    [
                                        abjad.Momento(
                                            context='GlobalSkips',
                                            prototype='abjad.TimeSignature',
                                            value='3/8',
                                            ),
                                        ],
                                    ),
                                ]
                            ),
                        ),
                    ('segment_number', 2),
                    ('start_clock_time', None),
                    ('stop_clock_time', None),
                    (
                        'time_signatures',
                        ['4/8', '3/8', '4/8', '3/8'],
                        ),
                    ]
                )

        Returns ordered dictionary.
        '''
        return self._metadata

    @property
    def metronome_mark_measure_map(self):
        r'''Gets metronome mark measure map.

        ..  container:: example

            With metronome mark measure map:

            >>> metronome_marks = abjad.MetronomeMarkDictionary()
            >>> metronome_marks['90'] = abjad.MetronomeMark((1, 4), 90)
            >>> maker = baca.SegmentMaker(
            ...     ignore_unpitched_notes=True,
            ...     metronome_mark_measure_map=baca.MetronomeMarkMeasureMap([
            ...         (1, metronome_marks['90']),
            ...         ]),
            ...     metronome_marks=metronome_marks,
            ...     score_template=baca.SingleStaffScoreTemplate(),
            ...     time_signatures=[(4, 8), (3, 8), (4, 8), (3, 8)],
            ...     )

            >>> maker(
            ...     baca.scope('MusicVoice', 1),
            ...     baca.make_even_runs(),
            ...     )

            >>> lilypond_file = maker.run(
            ...     environment='docs',
            ...     remove=[baca.Tags.CLOCK_TIME_MARKUP],
            ...     )
            >>> abjad.show(lilypond_file, strict=89) # doctest: +SKIP

            ..  docs::

                >>> abjad.f(lilypond_file[abjad.Score], strict=89)
                \context Score = "Score" <<
                    \context GlobalContext = "GlobalContext" <<
                        \context GlobalSkips = "GlobalSkips" {
                <BLANKLINE>
                            % GlobalSkips [measure 1]                                                    %! SM4
                            \time 4/8                                                                    %! EXPLICIT_TIME_SIGNATURE:SM8
                            \bar ""                                                                      %! EMPTY_START_BAR:SM2
                            \once \override Score.TimeSignature.color = #(x11-color 'blue)               %! EXPLICIT_TIME_SIGNATURE_COLOR:SM6
                            s1 * 1/2
                            ^ \markup {
                                \column
                                    {
                                        \line                                                            %! STAGE_NUMBER_MARKUP:SM3
                                            {                                                            %! STAGE_NUMBER_MARKUP:SM3
                                                \fontsize                                                %! STAGE_NUMBER_MARKUP:SM3
                                                    #-3                                                  %! STAGE_NUMBER_MARKUP:SM3
                                                    \with-color                                          %! STAGE_NUMBER_MARKUP:SM3
                                                        #(x11-color 'DarkCyan)                           %! STAGE_NUMBER_MARKUP:SM3
                                                        [1]                                              %! STAGE_NUMBER_MARKUP:SM3
                                            }                                                            %! STAGE_NUMBER_MARKUP:SM3
                                        \line                                                            %! EXPLICIT_METRONOME_MARK_WITH_COLOR:SM15
                                            {                                                            %! EXPLICIT_METRONOME_MARK_WITH_COLOR:SM15
                                                \with-color                                              %! EXPLICIT_METRONOME_MARK_WITH_COLOR:SM15
                                                    #(x11-color 'blue)                                   %! EXPLICIT_METRONOME_MARK_WITH_COLOR:SM15
                                                    {                                                    %! EXPLICIT_METRONOME_MARK_WITH_COLOR:SM15
                                                        \fontsize                                        %! EXPLICIT_METRONOME_MARK_WITH_COLOR:SM15
                                                            #-6                                          %! EXPLICIT_METRONOME_MARK_WITH_COLOR:SM15
                                                            \general-align                               %! EXPLICIT_METRONOME_MARK_WITH_COLOR:SM15
                                                                #Y                                       %! EXPLICIT_METRONOME_MARK_WITH_COLOR:SM15
                                                                #DOWN                                    %! EXPLICIT_METRONOME_MARK_WITH_COLOR:SM15
                                                                \note-by-number                          %! EXPLICIT_METRONOME_MARK_WITH_COLOR:SM15
                                                                    #2                                   %! EXPLICIT_METRONOME_MARK_WITH_COLOR:SM15
                                                                    #0                                   %! EXPLICIT_METRONOME_MARK_WITH_COLOR:SM15
                                                                    #1                                   %! EXPLICIT_METRONOME_MARK_WITH_COLOR:SM15
                                                        \upright                                         %! EXPLICIT_METRONOME_MARK_WITH_COLOR:SM15
                                                            {                                            %! EXPLICIT_METRONOME_MARK_WITH_COLOR:SM15
                                                                =                                        %! EXPLICIT_METRONOME_MARK_WITH_COLOR:SM15
                                                                90                                       %! EXPLICIT_METRONOME_MARK_WITH_COLOR:SM15
                                                            }                                            %! EXPLICIT_METRONOME_MARK_WITH_COLOR:SM15
                                                    }                                                    %! EXPLICIT_METRONOME_MARK_WITH_COLOR:SM15
                                            }                                                            %! EXPLICIT_METRONOME_MARK_WITH_COLOR:SM15
                                    }
                                }
                            %%% ^ \markup {                                                              %! EXPLICIT_METRONOME_MARK:SM27
                            %%%     \fontsize                                                            %! EXPLICIT_METRONOME_MARK:SM27
                            %%%         #-6                                                              %! EXPLICIT_METRONOME_MARK:SM27
                            %%%         \general-align                                                   %! EXPLICIT_METRONOME_MARK:SM27
                            %%%             #Y                                                           %! EXPLICIT_METRONOME_MARK:SM27
                            %%%             #DOWN                                                        %! EXPLICIT_METRONOME_MARK:SM27
                            %%%             \note-by-number                                              %! EXPLICIT_METRONOME_MARK:SM27
                            %%%                 #2                                                       %! EXPLICIT_METRONOME_MARK:SM27
                            %%%                 #0                                                       %! EXPLICIT_METRONOME_MARK:SM27
                            %%%                 #1                                                       %! EXPLICIT_METRONOME_MARK:SM27
                            %%%     \upright                                                             %! EXPLICIT_METRONOME_MARK:SM27
                            %%%         {                                                                %! EXPLICIT_METRONOME_MARK:SM27
                            %%%             =                                                            %! EXPLICIT_METRONOME_MARK:SM27
                            %%%             90                                                           %! EXPLICIT_METRONOME_MARK:SM27
                            %%%         }                                                                %! EXPLICIT_METRONOME_MARK:SM27
                            %%%     }                                                                    %! EXPLICIT_METRONOME_MARK:SM27
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
                                    c'8
                                    [
                <BLANKLINE>
                                    c'8
                <BLANKLINE>
                                    c'8
                <BLANKLINE>
                                    c'8
                                    ]
                                }
                                {
                <BLANKLINE>
                                    % MusicVoice [measure 2]                                             %! SM4
                                    c'8
                                    [
                <BLANKLINE>
                                    c'8
                <BLANKLINE>
                                    c'8
                                    ]
                                }
                                {
                <BLANKLINE>
                                    % MusicVoice [measure 3]                                             %! SM4
                                    c'8
                                    [
                <BLANKLINE>
                                    c'8
                <BLANKLINE>
                                    c'8
                <BLANKLINE>
                                    c'8
                                    ]
                                }
                                {
                <BLANKLINE>
                                    % MusicVoice [measure 4]                                             %! SM4
                                    c'8
                                    [
                <BLANKLINE>
                                    c'8
                <BLANKLINE>
                                    c'8
                                    ]
                <BLANKLINE>
                                }
                            }
                        }
                    >>
                >>

        Defaults to none.

        Set to metronome mark measure map or none.

        Returns metronome mark measure map or none.
        '''
        return self._metronome_mark_measure_map

    @property
    def metronome_marks(self):
        r'''Gets metronome marks.

        ..  container:: example

            >>> layout = baca.layout(baca.page([1, 0, (8,)]))
            >>> metronome_marks = abjad.MetronomeMarkDictionary()
            >>> metronome_marks['90'] = abjad.MetronomeMark((1, 4), 90)
            >>> metronome_marks['112'] = abjad.MetronomeMark((1, 4), 112)
            >>> remove = [
            ...     baca.Tags.build(baca.Tags.SPACING_MARKUP),
            ...     baca.Tags.CLOCK_TIME_MARKUP,
            ...     baca.Tags.EMPTY_START_BAR,
            ...     baca.Tags.STAGE_NUMBER_MARKUP,
            ...     ]

        ..  container:: example

            Explicit metronome marks color blue and redraw dull blue:

            >>> maker = baca.SegmentMaker(
            ...     ignore_unpitched_notes=True,
            ...     layout_measure_map=layout,
            ...     metronome_marks=metronome_marks,
            ...     score_template=baca.SingleStaffScoreTemplate(),
            ...     spacing_specifier=baca.minimum_width((1, 24)),
            ...     time_signatures=[(3, 8)],
            ...     )
            >>> maker(
            ...     baca.scope('GlobalSkips', 1),
            ...     baca.metronome_mark('112'),
            ...     )
            >>> maker(
            ...     baca.scope('MusicVoice', 1),
            ...     baca.make_notes(),
            ...     )

            >>> lilypond_file = maker.run(
            ...     environment='docs',
            ...     remove=remove,
            ...     )
            >>> block = abjad.Block(name='layout')
            >>> block.indent = 0
            >>> lilypond_file.items.insert(0, block)
            >>> abjad.show(lilypond_file, strict=89) # doctest: +SKIP

            ..  docs::

                >>> abjad.f(lilypond_file[abjad.Score], strict=89)
                \context Score = "Score" <<
                    \context GlobalContext = "GlobalContext" <<
                        \context GlobalSkips = "GlobalSkips" {
                <BLANKLINE>
                            % GlobalSkips [measure 1]                                                    %! SM4
                            \autoPageBreaksOff                                                           %! SEGMENT:LAYOUT:LMM1
                            \noBreak                                                                     %! SEGMENT:LAYOUT:LMM2
                            \overrideProperty Score.NonMusicalPaperColumn.line-break-system-details      %! SEGMENT:LAYOUT:LMM3
                            #'((Y-offset . 0) (alignment-distances . (8)))                               %! SEGMENT:LAYOUT:LMM3
                            \time 3/8                                                                    %! EXPLICIT_TIME_SIGNATURE:SM8
                            \once \override Score.TimeSignature.color = #(x11-color 'blue)               %! EXPLICIT_TIME_SIGNATURE_COLOR:SM6
                            \newSpacingSection                                                           %! SEGMENT:SPACING:HSS1
                            \set Score.proportionalNotationDuration = #(ly:make-moment 1 24)             %! SEGMENT:SPACING:HSS1
                            \pageBreak                                                                   %! SEGMENT:LAYOUT:LMM3
                            s1 * 3/8
                            ^ \markup {                                                                  %! EXPLICIT_METRONOME_MARK_WITH_COLOR:SM15
                                \with-color                                                              %! EXPLICIT_METRONOME_MARK_WITH_COLOR:SM15
                                    #(x11-color 'blue)                                                   %! EXPLICIT_METRONOME_MARK_WITH_COLOR:SM15
                                    {                                                                    %! EXPLICIT_METRONOME_MARK_WITH_COLOR:SM15
                                        \fontsize                                                        %! EXPLICIT_METRONOME_MARK_WITH_COLOR:SM15
                                            #-6                                                          %! EXPLICIT_METRONOME_MARK_WITH_COLOR:SM15
                                            \general-align                                               %! EXPLICIT_METRONOME_MARK_WITH_COLOR:SM15
                                                #Y                                                       %! EXPLICIT_METRONOME_MARK_WITH_COLOR:SM15
                                                #DOWN                                                    %! EXPLICIT_METRONOME_MARK_WITH_COLOR:SM15
                                                \note-by-number                                          %! EXPLICIT_METRONOME_MARK_WITH_COLOR:SM15
                                                    #2                                                   %! EXPLICIT_METRONOME_MARK_WITH_COLOR:SM15
                                                    #0                                                   %! EXPLICIT_METRONOME_MARK_WITH_COLOR:SM15
                                                    #1                                                   %! EXPLICIT_METRONOME_MARK_WITH_COLOR:SM15
                                        \upright                                                         %! EXPLICIT_METRONOME_MARK_WITH_COLOR:SM15
                                            {                                                            %! EXPLICIT_METRONOME_MARK_WITH_COLOR:SM15
                                                =                                                        %! EXPLICIT_METRONOME_MARK_WITH_COLOR:SM15
                                                112                                                      %! EXPLICIT_METRONOME_MARK_WITH_COLOR:SM15
                                            }                                                            %! EXPLICIT_METRONOME_MARK_WITH_COLOR:SM15
                                    }                                                                    %! EXPLICIT_METRONOME_MARK_WITH_COLOR:SM15
                                }                                                                        %! EXPLICIT_METRONOME_MARK_WITH_COLOR:SM15
                            %%% ^ \markup {                                                              %! EXPLICIT_METRONOME_MARK:SM27
                            %%%     \fontsize                                                            %! EXPLICIT_METRONOME_MARK:SM27
                            %%%         #-6                                                              %! EXPLICIT_METRONOME_MARK:SM27
                            %%%         \general-align                                                   %! EXPLICIT_METRONOME_MARK:SM27
                            %%%             #Y                                                           %! EXPLICIT_METRONOME_MARK:SM27
                            %%%             #DOWN                                                        %! EXPLICIT_METRONOME_MARK:SM27
                            %%%             \note-by-number                                              %! EXPLICIT_METRONOME_MARK:SM27
                            %%%                 #2                                                       %! EXPLICIT_METRONOME_MARK:SM27
                            %%%                 #0                                                       %! EXPLICIT_METRONOME_MARK:SM27
                            %%%                 #1                                                       %! EXPLICIT_METRONOME_MARK:SM27
                            %%%     \upright                                                             %! EXPLICIT_METRONOME_MARK:SM27
                            %%%         {                                                                %! EXPLICIT_METRONOME_MARK:SM27
                            %%%             =                                                            %! EXPLICIT_METRONOME_MARK:SM27
                            %%%             112                                                          %! EXPLICIT_METRONOME_MARK:SM27
                            %%%         }                                                                %! EXPLICIT_METRONOME_MARK:SM27
                            %%%     }                                                                    %! EXPLICIT_METRONOME_MARK:SM27
                            \override Score.BarLine.transparent = ##f                                    %! SM5
                            \bar "|"                                                                     %! SM5
                <BLANKLINE>
                        }
                    >>
                    \context MusicContext = "MusicContext" <<
                        \context Staff = "MusicStaff" {
                            \context Voice = "MusicVoice" {
                <BLANKLINE>
                                % MusicVoice [measure 1]                                                 %! SM4
                                c'4.
                <BLANKLINE>
                            }
                        }
                    >>
                >>

            Even after a previous metronome mark:

            >>> maker = baca.SegmentMaker(
            ...     ignore_unpitched_notes=True,
            ...     layout_measure_map=layout,
            ...     metronome_marks=metronome_marks,
            ...     score_template=baca.SingleStaffScoreTemplate(),
            ...     spacing_specifier=baca.minimum_width((1, 24)),
            ...     time_signatures=[(3, 8)],
            ...     )
            >>> maker(
            ...     baca.scope('GlobalSkips', 1),
            ...     baca.metronome_mark('112'),
            ...     )
            >>> maker(
            ...     baca.scope('MusicVoice', 1),
            ...     baca.make_notes(),
            ...     )

            >>> metadata = {}
            >>> metadata['persistent_indicators'] = {}
            >>> metadata['persistent_indicators']['Score'] = [
            ...     abjad.Momento(
            ...         context='GlobalSkips',
            ...         prototype='abjad.MetronomeMark',
            ...         value='90',
            ...         )
            ...     ]
            >>> metadata['segment_number'] = 1
            >>> lilypond_file = maker.run(
            ...     environment='docs',
            ...     previous_metadata=metadata,
            ...     remove=remove,
            ...     )
            >>> block = abjad.Block(name='layout')
            >>> block.indent = 0
            >>> lilypond_file.items.insert(0, block)
            >>> abjad.show(lilypond_file, strict=89) # doctest: +SKIP

            ..  docs::

                >>> abjad.f(lilypond_file[abjad.Score], strict=89)
                \context Score = "Score" <<
                    \context GlobalContext = "GlobalContext" <<
                        \context GlobalSkips = "GlobalSkips" {
                <BLANKLINE>
                            % GlobalSkips [measure 1]                                                    %! SM4
                            \autoPageBreaksOff                                                           %! SEGMENT:LAYOUT:LMM1
                            \noBreak                                                                     %! SEGMENT:LAYOUT:LMM2
                            \overrideProperty Score.NonMusicalPaperColumn.line-break-system-details      %! SEGMENT:LAYOUT:LMM3
                            #'((Y-offset . 0) (alignment-distances . (8)))                               %! SEGMENT:LAYOUT:LMM3
                            \time 3/8                                                                    %! EXPLICIT_TIME_SIGNATURE:SM8
                            \mark #1                                                                     %! SM9
                            \once \override Score.TimeSignature.color = #(x11-color 'blue)               %! EXPLICIT_TIME_SIGNATURE_COLOR:SM6
                            \newSpacingSection                                                           %! SEGMENT:SPACING:HSS1
                            \set Score.proportionalNotationDuration = #(ly:make-moment 1 24)             %! SEGMENT:SPACING:HSS1
                            \pageBreak                                                                   %! SEGMENT:LAYOUT:LMM3
                            s1 * 3/8
                            ^ \markup {                                                                  %! EXPLICIT_METRONOME_MARK_WITH_COLOR:SM15
                                \with-color                                                              %! EXPLICIT_METRONOME_MARK_WITH_COLOR:SM15
                                    #(x11-color 'blue)                                                   %! EXPLICIT_METRONOME_MARK_WITH_COLOR:SM15
                                    {                                                                    %! EXPLICIT_METRONOME_MARK_WITH_COLOR:SM15
                                        \fontsize                                                        %! EXPLICIT_METRONOME_MARK_WITH_COLOR:SM15
                                            #-6                                                          %! EXPLICIT_METRONOME_MARK_WITH_COLOR:SM15
                                            \general-align                                               %! EXPLICIT_METRONOME_MARK_WITH_COLOR:SM15
                                                #Y                                                       %! EXPLICIT_METRONOME_MARK_WITH_COLOR:SM15
                                                #DOWN                                                    %! EXPLICIT_METRONOME_MARK_WITH_COLOR:SM15
                                                \note-by-number                                          %! EXPLICIT_METRONOME_MARK_WITH_COLOR:SM15
                                                    #2                                                   %! EXPLICIT_METRONOME_MARK_WITH_COLOR:SM15
                                                    #0                                                   %! EXPLICIT_METRONOME_MARK_WITH_COLOR:SM15
                                                    #1                                                   %! EXPLICIT_METRONOME_MARK_WITH_COLOR:SM15
                                        \upright                                                         %! EXPLICIT_METRONOME_MARK_WITH_COLOR:SM15
                                            {                                                            %! EXPLICIT_METRONOME_MARK_WITH_COLOR:SM15
                                                =                                                        %! EXPLICIT_METRONOME_MARK_WITH_COLOR:SM15
                                                112                                                      %! EXPLICIT_METRONOME_MARK_WITH_COLOR:SM15
                                            }                                                            %! EXPLICIT_METRONOME_MARK_WITH_COLOR:SM15
                                    }                                                                    %! EXPLICIT_METRONOME_MARK_WITH_COLOR:SM15
                                }                                                                        %! EXPLICIT_METRONOME_MARK_WITH_COLOR:SM15
                            %%% ^ \markup {                                                              %! EXPLICIT_METRONOME_MARK:SM27
                            %%%     \fontsize                                                            %! EXPLICIT_METRONOME_MARK:SM27
                            %%%         #-6                                                              %! EXPLICIT_METRONOME_MARK:SM27
                            %%%         \general-align                                                   %! EXPLICIT_METRONOME_MARK:SM27
                            %%%             #Y                                                           %! EXPLICIT_METRONOME_MARK:SM27
                            %%%             #DOWN                                                        %! EXPLICIT_METRONOME_MARK:SM27
                            %%%             \note-by-number                                              %! EXPLICIT_METRONOME_MARK:SM27
                            %%%                 #2                                                       %! EXPLICIT_METRONOME_MARK:SM27
                            %%%                 #0                                                       %! EXPLICIT_METRONOME_MARK:SM27
                            %%%                 #1                                                       %! EXPLICIT_METRONOME_MARK:SM27
                            %%%     \upright                                                             %! EXPLICIT_METRONOME_MARK:SM27
                            %%%         {                                                                %! EXPLICIT_METRONOME_MARK:SM27
                            %%%             =                                                            %! EXPLICIT_METRONOME_MARK:SM27
                            %%%             112                                                          %! EXPLICIT_METRONOME_MARK:SM27
                            %%%         }                                                                %! EXPLICIT_METRONOME_MARK:SM27
                            %%%     }                                                                    %! EXPLICIT_METRONOME_MARK:SM27
                            \override Score.BarLine.transparent = ##f                                    %! SM5
                            \bar "|"                                                                     %! SM5
                <BLANKLINE>
                        }
                    >>
                    \context MusicContext = "MusicContext" <<
                        \context Staff = "MusicStaff" {
                            \context Voice = "MusicVoice" {
                <BLANKLINE>
                                % MusicVoice [measure 1]                                                 %! SM4
                                c'4.
                <BLANKLINE>
                            }
                        }
                    >>
                >>

        ..  container:: example

            Reapplied metronome marks color green and redraw dull green:

            >>> maker = baca.SegmentMaker(
            ...     ignore_unpitched_notes=True,
            ...     layout_measure_map=layout,
            ...     metronome_marks=metronome_marks,
            ...     score_template=baca.SingleStaffScoreTemplate(),
            ...     spacing_specifier=baca.minimum_width((1, 24)),
            ...     time_signatures=[(3, 8)],
            ...     )
            >>> maker(
            ...     baca.scope('MusicVoice', 1),
            ...     baca.make_notes(),
            ...     )

            >>> metadata = {}
            >>> metadata['persistent_indicators'] = {}
            >>> metadata['persistent_indicators']['Score'] = [
            ...     abjad.Momento(
            ...         context='GlobalSkips',
            ...         prototype='abjad.MetronomeMark',
            ...         value='90',
            ...         )
            ...     ]
            >>> metadata['segment_number'] = 1
            >>> lilypond_file = maker.run(
            ...     environment='docs',
            ...     previous_metadata=metadata,
            ...     remove=remove,
            ...     )
            >>> block = abjad.Block(name='layout')
            >>> block.indent = 0
            >>> lilypond_file.items.insert(0, block)
            >>> abjad.show(lilypond_file, strict=89) # doctest: +SKIP

            ..  docs::

                >>> abjad.f(lilypond_file[abjad.Score], strict=89)
                \context Score = "Score" <<
                    \context GlobalContext = "GlobalContext" <<
                        \context GlobalSkips = "GlobalSkips" {
                <BLANKLINE>
                            % GlobalSkips [measure 1]                                                    %! SM4
                            \autoPageBreaksOff                                                           %! SEGMENT:LAYOUT:LMM1
                            \noBreak                                                                     %! SEGMENT:LAYOUT:LMM2
                            \overrideProperty Score.NonMusicalPaperColumn.line-break-system-details      %! SEGMENT:LAYOUT:LMM3
                            #'((Y-offset . 0) (alignment-distances . (8)))                               %! SEGMENT:LAYOUT:LMM3
                            \time 3/8                                                                    %! EXPLICIT_TIME_SIGNATURE:SM8
                            \mark #1                                                                     %! SM9
                            \once \override Score.TimeSignature.color = #(x11-color 'blue)               %! EXPLICIT_TIME_SIGNATURE_COLOR:SM6
                            \newSpacingSection                                                           %! SEGMENT:SPACING:HSS1
                            \set Score.proportionalNotationDuration = #(ly:make-moment 1 24)             %! SEGMENT:SPACING:HSS1
                            \pageBreak                                                                   %! SEGMENT:LAYOUT:LMM3
                            s1 * 3/8
                            ^ \markup {                                                                  %! REAPPLIED_METRONOME_MARK_WITH_COLOR:SM15
                                \with-color                                                              %! REAPPLIED_METRONOME_MARK_WITH_COLOR:SM15
                                    #(x11-color 'green4)                                                 %! REAPPLIED_METRONOME_MARK_WITH_COLOR:SM15
                                    {                                                                    %! REAPPLIED_METRONOME_MARK_WITH_COLOR:SM15
                                        \fontsize                                                        %! REAPPLIED_METRONOME_MARK_WITH_COLOR:SM15
                                            #-6                                                          %! REAPPLIED_METRONOME_MARK_WITH_COLOR:SM15
                                            \general-align                                               %! REAPPLIED_METRONOME_MARK_WITH_COLOR:SM15
                                                #Y                                                       %! REAPPLIED_METRONOME_MARK_WITH_COLOR:SM15
                                                #DOWN                                                    %! REAPPLIED_METRONOME_MARK_WITH_COLOR:SM15
                                                \note-by-number                                          %! REAPPLIED_METRONOME_MARK_WITH_COLOR:SM15
                                                    #2                                                   %! REAPPLIED_METRONOME_MARK_WITH_COLOR:SM15
                                                    #0                                                   %! REAPPLIED_METRONOME_MARK_WITH_COLOR:SM15
                                                    #1                                                   %! REAPPLIED_METRONOME_MARK_WITH_COLOR:SM15
                                        \upright                                                         %! REAPPLIED_METRONOME_MARK_WITH_COLOR:SM15
                                            {                                                            %! REAPPLIED_METRONOME_MARK_WITH_COLOR:SM15
                                                =                                                        %! REAPPLIED_METRONOME_MARK_WITH_COLOR:SM15
                                                90                                                       %! REAPPLIED_METRONOME_MARK_WITH_COLOR:SM15
                                            }                                                            %! REAPPLIED_METRONOME_MARK_WITH_COLOR:SM15
                                    }                                                                    %! REAPPLIED_METRONOME_MARK_WITH_COLOR:SM15
                                }                                                                        %! REAPPLIED_METRONOME_MARK_WITH_COLOR:SM15
                            %%% ^ \markup {                                                              %! REAPPLIED_METRONOME_MARK:SM27
                            %%%     \fontsize                                                            %! REAPPLIED_METRONOME_MARK:SM27
                            %%%         #-6                                                              %! REAPPLIED_METRONOME_MARK:SM27
                            %%%         \general-align                                                   %! REAPPLIED_METRONOME_MARK:SM27
                            %%%             #Y                                                           %! REAPPLIED_METRONOME_MARK:SM27
                            %%%             #DOWN                                                        %! REAPPLIED_METRONOME_MARK:SM27
                            %%%             \note-by-number                                              %! REAPPLIED_METRONOME_MARK:SM27
                            %%%                 #2                                                       %! REAPPLIED_METRONOME_MARK:SM27
                            %%%                 #0                                                       %! REAPPLIED_METRONOME_MARK:SM27
                            %%%                 #1                                                       %! REAPPLIED_METRONOME_MARK:SM27
                            %%%     \upright                                                             %! REAPPLIED_METRONOME_MARK:SM27
                            %%%         {                                                                %! REAPPLIED_METRONOME_MARK:SM27
                            %%%             =                                                            %! REAPPLIED_METRONOME_MARK:SM27
                            %%%             90                                                           %! REAPPLIED_METRONOME_MARK:SM27
                            %%%         }                                                                %! REAPPLIED_METRONOME_MARK:SM27
                            %%%     }                                                                    %! REAPPLIED_METRONOME_MARK:SM27
                            \override Score.BarLine.transparent = ##f                                    %! SM5
                            \bar "|"                                                                     %! SM5
                <BLANKLINE>
                        }
                    >>
                    \context MusicContext = "MusicContext" <<
                        \context Staff = "MusicStaff" {
                            \context Voice = "MusicVoice" {
                <BLANKLINE>
                                % MusicVoice [measure 1]                                                 %! SM4
                                c'4.
                <BLANKLINE>
                            }
                        }
                    >>
                >>

        ..  container:: example

            Redundant metronome marks color pink and redraw dull pink:

            >>> maker = baca.SegmentMaker(
            ...     ignore_unpitched_notes=True,
            ...     layout_measure_map=layout,
            ...     metronome_marks=metronome_marks,
            ...     score_template=baca.SingleStaffScoreTemplate(),
            ...     spacing_specifier=baca.minimum_width((1, 24)),
            ...     time_signatures=[(3, 8), (3, 8)],
            ...     )
            >>> maker(
            ...     baca.scope('GlobalSkips', 1),
            ...     baca.metronome_mark('112'),
            ...     baca.metronome_mark('112', baca.leaf(1)),
            ...     )
            >>> maker(
            ...     baca.scope('MusicVoice', 1),
            ...     baca.make_notes(),
            ...     )

            >>> lilypond_file = maker.run(
            ...     environment='docs',
            ...     remove=remove,
            ...     )
            >>> block = abjad.Block(name='layout')
            >>> block.indent = 0
            >>> lilypond_file.items.insert(0, block)
            >>> abjad.show(lilypond_file, strict=89) # doctest: +SKIP

            ..  docs::

                >>> abjad.f(lilypond_file[abjad.Score], strict=89)
                \context Score = "Score" <<
                    \context GlobalContext = "GlobalContext" <<
                        \context GlobalSkips = "GlobalSkips" {
                <BLANKLINE>
                            % GlobalSkips [measure 1]                                                    %! SM4
                            \autoPageBreaksOff                                                           %! SEGMENT:LAYOUT:LMM1
                            \noBreak                                                                     %! SEGMENT:LAYOUT:LMM2
                            \overrideProperty Score.NonMusicalPaperColumn.line-break-system-details      %! SEGMENT:LAYOUT:LMM3
                            #'((Y-offset . 0) (alignment-distances . (8)))                               %! SEGMENT:LAYOUT:LMM3
                            \time 3/8                                                                    %! EXPLICIT_TIME_SIGNATURE:SM8
                            \once \override Score.TimeSignature.color = #(x11-color 'blue)               %! EXPLICIT_TIME_SIGNATURE_COLOR:SM6
                            \newSpacingSection                                                           %! SEGMENT:SPACING:HSS1
                            \set Score.proportionalNotationDuration = #(ly:make-moment 1 24)             %! SEGMENT:SPACING:HSS1
                            \pageBreak                                                                   %! SEGMENT:LAYOUT:LMM3
                            s1 * 3/8
                            ^ \markup {                                                                  %! EXPLICIT_METRONOME_MARK_WITH_COLOR:SM15
                                \with-color                                                              %! EXPLICIT_METRONOME_MARK_WITH_COLOR:SM15
                                    #(x11-color 'blue)                                                   %! EXPLICIT_METRONOME_MARK_WITH_COLOR:SM15
                                    {                                                                    %! EXPLICIT_METRONOME_MARK_WITH_COLOR:SM15
                                        \fontsize                                                        %! EXPLICIT_METRONOME_MARK_WITH_COLOR:SM15
                                            #-6                                                          %! EXPLICIT_METRONOME_MARK_WITH_COLOR:SM15
                                            \general-align                                               %! EXPLICIT_METRONOME_MARK_WITH_COLOR:SM15
                                                #Y                                                       %! EXPLICIT_METRONOME_MARK_WITH_COLOR:SM15
                                                #DOWN                                                    %! EXPLICIT_METRONOME_MARK_WITH_COLOR:SM15
                                                \note-by-number                                          %! EXPLICIT_METRONOME_MARK_WITH_COLOR:SM15
                                                    #2                                                   %! EXPLICIT_METRONOME_MARK_WITH_COLOR:SM15
                                                    #0                                                   %! EXPLICIT_METRONOME_MARK_WITH_COLOR:SM15
                                                    #1                                                   %! EXPLICIT_METRONOME_MARK_WITH_COLOR:SM15
                                        \upright                                                         %! EXPLICIT_METRONOME_MARK_WITH_COLOR:SM15
                                            {                                                            %! EXPLICIT_METRONOME_MARK_WITH_COLOR:SM15
                                                =                                                        %! EXPLICIT_METRONOME_MARK_WITH_COLOR:SM15
                                                112                                                      %! EXPLICIT_METRONOME_MARK_WITH_COLOR:SM15
                                            }                                                            %! EXPLICIT_METRONOME_MARK_WITH_COLOR:SM15
                                    }                                                                    %! EXPLICIT_METRONOME_MARK_WITH_COLOR:SM15
                                }                                                                        %! EXPLICIT_METRONOME_MARK_WITH_COLOR:SM15
                            %%% ^ \markup {                                                              %! EXPLICIT_METRONOME_MARK:SM27
                            %%%     \fontsize                                                            %! EXPLICIT_METRONOME_MARK:SM27
                            %%%         #-6                                                              %! EXPLICIT_METRONOME_MARK:SM27
                            %%%         \general-align                                                   %! EXPLICIT_METRONOME_MARK:SM27
                            %%%             #Y                                                           %! EXPLICIT_METRONOME_MARK:SM27
                            %%%             #DOWN                                                        %! EXPLICIT_METRONOME_MARK:SM27
                            %%%             \note-by-number                                              %! EXPLICIT_METRONOME_MARK:SM27
                            %%%                 #2                                                       %! EXPLICIT_METRONOME_MARK:SM27
                            %%%                 #0                                                       %! EXPLICIT_METRONOME_MARK:SM27
                            %%%                 #1                                                       %! EXPLICIT_METRONOME_MARK:SM27
                            %%%     \upright                                                             %! EXPLICIT_METRONOME_MARK:SM27
                            %%%         {                                                                %! EXPLICIT_METRONOME_MARK:SM27
                            %%%             =                                                            %! EXPLICIT_METRONOME_MARK:SM27
                            %%%             112                                                          %! EXPLICIT_METRONOME_MARK:SM27
                            %%%         }                                                                %! EXPLICIT_METRONOME_MARK:SM27
                            %%%     }                                                                    %! EXPLICIT_METRONOME_MARK:SM27
                <BLANKLINE>
                            % GlobalSkips [measure 2]                                                    %! SM4
                            \noBreak                                                                     %! SEGMENT:LAYOUT:LMM2
                            \once \override Score.TimeSignature.color = #(x11-color 'DeepPink1)          %! REDUNDANT_TIME_SIGNATURE_COLOR:SM6
                            \newSpacingSection                                                           %! SEGMENT:SPACING:HSS1
                            \set Score.proportionalNotationDuration = #(ly:make-moment 1 24)             %! SEGMENT:SPACING:HSS1
                            s1 * 3/8
                            ^ \markup {                                                                  %! REDUNDANT_METRONOME_MARK_WITH_COLOR:SM15
                                \with-color                                                              %! REDUNDANT_METRONOME_MARK_WITH_COLOR:SM15
                                    #(x11-color 'DeepPink1)                                              %! REDUNDANT_METRONOME_MARK_WITH_COLOR:SM15
                                    {                                                                    %! REDUNDANT_METRONOME_MARK_WITH_COLOR:SM15
                                        \fontsize                                                        %! REDUNDANT_METRONOME_MARK_WITH_COLOR:SM15
                                            #-6                                                          %! REDUNDANT_METRONOME_MARK_WITH_COLOR:SM15
                                            \general-align                                               %! REDUNDANT_METRONOME_MARK_WITH_COLOR:SM15
                                                #Y                                                       %! REDUNDANT_METRONOME_MARK_WITH_COLOR:SM15
                                                #DOWN                                                    %! REDUNDANT_METRONOME_MARK_WITH_COLOR:SM15
                                                \note-by-number                                          %! REDUNDANT_METRONOME_MARK_WITH_COLOR:SM15
                                                    #2                                                   %! REDUNDANT_METRONOME_MARK_WITH_COLOR:SM15
                                                    #0                                                   %! REDUNDANT_METRONOME_MARK_WITH_COLOR:SM15
                                                    #1                                                   %! REDUNDANT_METRONOME_MARK_WITH_COLOR:SM15
                                        \upright                                                         %! REDUNDANT_METRONOME_MARK_WITH_COLOR:SM15
                                            {                                                            %! REDUNDANT_METRONOME_MARK_WITH_COLOR:SM15
                                                =                                                        %! REDUNDANT_METRONOME_MARK_WITH_COLOR:SM15
                                                112                                                      %! REDUNDANT_METRONOME_MARK_WITH_COLOR:SM15
                                            }                                                            %! REDUNDANT_METRONOME_MARK_WITH_COLOR:SM15
                                    }                                                                    %! REDUNDANT_METRONOME_MARK_WITH_COLOR:SM15
                                }                                                                        %! REDUNDANT_METRONOME_MARK_WITH_COLOR:SM15
                            %%% ^ \markup {                                                              %! REDUNDANT_METRONOME_MARK:SM27
                            %%%     \fontsize                                                            %! REDUNDANT_METRONOME_MARK:SM27
                            %%%         #-6                                                              %! REDUNDANT_METRONOME_MARK:SM27
                            %%%         \general-align                                                   %! REDUNDANT_METRONOME_MARK:SM27
                            %%%             #Y                                                           %! REDUNDANT_METRONOME_MARK:SM27
                            %%%             #DOWN                                                        %! REDUNDANT_METRONOME_MARK:SM27
                            %%%             \note-by-number                                              %! REDUNDANT_METRONOME_MARK:SM27
                            %%%                 #2                                                       %! REDUNDANT_METRONOME_MARK:SM27
                            %%%                 #0                                                       %! REDUNDANT_METRONOME_MARK:SM27
                            %%%                 #1                                                       %! REDUNDANT_METRONOME_MARK:SM27
                            %%%     \upright                                                             %! REDUNDANT_METRONOME_MARK:SM27
                            %%%         {                                                                %! REDUNDANT_METRONOME_MARK:SM27
                            %%%             =                                                            %! REDUNDANT_METRONOME_MARK:SM27
                            %%%             112                                                          %! REDUNDANT_METRONOME_MARK:SM27
                            %%%         }                                                                %! REDUNDANT_METRONOME_MARK:SM27
                            %%%     }                                                                    %! REDUNDANT_METRONOME_MARK:SM27
                            \override Score.BarLine.transparent = ##f                                    %! SM5
                            \bar "|"                                                                     %! SM5
                <BLANKLINE>
                        }
                    >>
                    \context MusicContext = "MusicContext" <<
                        \context Staff = "MusicStaff" {
                            \context Voice = "MusicVoice" {
                <BLANKLINE>
                                % MusicVoice [measure 1]                                                 %! SM4
                                c'4.
                <BLANKLINE>
                                % MusicVoice [measure 2]                                                 %! SM4
                                c'4.
                <BLANKLINE>
                            }
                        }
                    >>
                >>

            Even at the beginning of a segment:

            >>> maker = baca.SegmentMaker(
            ...     ignore_unpitched_notes=True,
            ...     layout_measure_map=layout,
            ...     metronome_marks=metronome_marks,
            ...     score_template=baca.SingleStaffScoreTemplate(),
            ...     spacing_specifier=baca.minimum_width((1, 24)),
            ...     time_signatures=[(3, 8)],
            ...     )
            >>> maker(
            ...     baca.scope('GlobalSkips', 1),
            ...     baca.metronome_mark('112'),
            ...     )
            >>> maker(
            ...     baca.scope('MusicVoice', 1),
            ...     baca.make_notes(),
            ...     )

            >>> metadata = {}
            >>> metadata['persistent_indicators'] = {}
            >>> metadata['persistent_indicators']['Score'] = [
            ...     abjad.Momento(
            ...         context='GlobalSkips',
            ...         prototype='abjad.MetronomeMark',
            ...         value='112',
            ...         )
            ...     ]
            >>> metadata['segment_number'] = 1
            >>> lilypond_file = maker.run(
            ...     environment='docs',
            ...     previous_metadata=metadata,
            ...     remove=remove,
            ...     )
            >>> block = abjad.Block(name='layout')
            >>> block.indent = 0
            >>> lilypond_file.items.insert(0, block)
            >>> abjad.show(lilypond_file, strict=89) # doctest: +SKIP

            ..  docs::

                >>> abjad.f(lilypond_file[abjad.Score], strict=89)
                \context Score = "Score" <<
                    \context GlobalContext = "GlobalContext" <<
                        \context GlobalSkips = "GlobalSkips" {
                <BLANKLINE>
                            % GlobalSkips [measure 1]                                                    %! SM4
                            \autoPageBreaksOff                                                           %! SEGMENT:LAYOUT:LMM1
                            \noBreak                                                                     %! SEGMENT:LAYOUT:LMM2
                            \overrideProperty Score.NonMusicalPaperColumn.line-break-system-details      %! SEGMENT:LAYOUT:LMM3
                            #'((Y-offset . 0) (alignment-distances . (8)))                               %! SEGMENT:LAYOUT:LMM3
                            \time 3/8                                                                    %! EXPLICIT_TIME_SIGNATURE:SM8
                            \mark #1                                                                     %! SM9
                            \once \override Score.TimeSignature.color = #(x11-color 'blue)               %! EXPLICIT_TIME_SIGNATURE_COLOR:SM6
                            \newSpacingSection                                                           %! SEGMENT:SPACING:HSS1
                            \set Score.proportionalNotationDuration = #(ly:make-moment 1 24)             %! SEGMENT:SPACING:HSS1
                            \pageBreak                                                                   %! SEGMENT:LAYOUT:LMM3
                            s1 * 3/8
                            ^ \markup {                                                                  %! REDUNDANT_METRONOME_MARK_WITH_COLOR:SM15
                                \with-color                                                              %! REDUNDANT_METRONOME_MARK_WITH_COLOR:SM15
                                    #(x11-color 'DeepPink1)                                              %! REDUNDANT_METRONOME_MARK_WITH_COLOR:SM15
                                    {                                                                    %! REDUNDANT_METRONOME_MARK_WITH_COLOR:SM15
                                        \fontsize                                                        %! REDUNDANT_METRONOME_MARK_WITH_COLOR:SM15
                                            #-6                                                          %! REDUNDANT_METRONOME_MARK_WITH_COLOR:SM15
                                            \general-align                                               %! REDUNDANT_METRONOME_MARK_WITH_COLOR:SM15
                                                #Y                                                       %! REDUNDANT_METRONOME_MARK_WITH_COLOR:SM15
                                                #DOWN                                                    %! REDUNDANT_METRONOME_MARK_WITH_COLOR:SM15
                                                \note-by-number                                          %! REDUNDANT_METRONOME_MARK_WITH_COLOR:SM15
                                                    #2                                                   %! REDUNDANT_METRONOME_MARK_WITH_COLOR:SM15
                                                    #0                                                   %! REDUNDANT_METRONOME_MARK_WITH_COLOR:SM15
                                                    #1                                                   %! REDUNDANT_METRONOME_MARK_WITH_COLOR:SM15
                                        \upright                                                         %! REDUNDANT_METRONOME_MARK_WITH_COLOR:SM15
                                            {                                                            %! REDUNDANT_METRONOME_MARK_WITH_COLOR:SM15
                                                =                                                        %! REDUNDANT_METRONOME_MARK_WITH_COLOR:SM15
                                                112                                                      %! REDUNDANT_METRONOME_MARK_WITH_COLOR:SM15
                                            }                                                            %! REDUNDANT_METRONOME_MARK_WITH_COLOR:SM15
                                    }                                                                    %! REDUNDANT_METRONOME_MARK_WITH_COLOR:SM15
                                }                                                                        %! REDUNDANT_METRONOME_MARK_WITH_COLOR:SM15
                            %%% ^ \markup {                                                              %! REDUNDANT_METRONOME_MARK:SM27
                            %%%     \fontsize                                                            %! REDUNDANT_METRONOME_MARK:SM27
                            %%%         #-6                                                              %! REDUNDANT_METRONOME_MARK:SM27
                            %%%         \general-align                                                   %! REDUNDANT_METRONOME_MARK:SM27
                            %%%             #Y                                                           %! REDUNDANT_METRONOME_MARK:SM27
                            %%%             #DOWN                                                        %! REDUNDANT_METRONOME_MARK:SM27
                            %%%             \note-by-number                                              %! REDUNDANT_METRONOME_MARK:SM27
                            %%%                 #2                                                       %! REDUNDANT_METRONOME_MARK:SM27
                            %%%                 #0                                                       %! REDUNDANT_METRONOME_MARK:SM27
                            %%%                 #1                                                       %! REDUNDANT_METRONOME_MARK:SM27
                            %%%     \upright                                                             %! REDUNDANT_METRONOME_MARK:SM27
                            %%%         {                                                                %! REDUNDANT_METRONOME_MARK:SM27
                            %%%             =                                                            %! REDUNDANT_METRONOME_MARK:SM27
                            %%%             112                                                          %! REDUNDANT_METRONOME_MARK:SM27
                            %%%         }                                                                %! REDUNDANT_METRONOME_MARK:SM27
                            %%%     }                                                                    %! REDUNDANT_METRONOME_MARK:SM27
                            \override Score.BarLine.transparent = ##f                                    %! SM5
                            \bar "|"                                                                     %! SM5
                <BLANKLINE>
                        }
                    >>
                    \context MusicContext = "MusicContext" <<
                        \context Staff = "MusicStaff" {
                            \context Voice = "MusicVoice" {
                <BLANKLINE>
                                % MusicVoice [measure 1]                                                 %! SM4
                                c'4.
                <BLANKLINE>
                            }
                        }
                    >>
                >>

        Returns ordered dictionary or none.
        '''
        return self._metronome_marks

    @property
    def midi(self):
        r'''Is true when segment-maker outputs MIDI.

        Returns true, false or none.
        '''
        return self._midi

    @property
    def omit_empty_start_bar(self):
        r'''Is true when segment-mark omits empty start bar.

        Returns true, false or none.
        '''
        return self._omit_empty_start_bar

    @property
    def omit_stage_number_markup(self):
        r'''Is true when segment-mark omits stage number markup.

        Returns true, false or none.
        '''
        return self._omit_stage_number_markup

    @property
    def print_segment_duration(self):
        r'''Is true when segment prints duration in seconds.

        Defaults to none.

        Set to true, false or none.

        Returns true, false or none.
        '''
        return self._print_segment_duration

    @property
    def print_timings(self):
        r'''Is true when segment prints interpreter timings.

        Defaults to none.

        Set to true, false or none.

        Returns true, false or none.
        '''
        return self._print_timings

    @property
    def range_checker(self):
        r'''Gets range checker.

        Defaults to none.

        Set to pitch range, true, false or none.

        Returns pitch range, true, false or none.
        '''
        return self._range_checker

    @property
    def rehearsal_letter(self):
        r'''Gets rehearsal letter.

        Defaults to none.

        Set to string or none.

        Calculates rehearsal letter automatically when none.

        Suppresses rehearsal letter when set to empty string.

        Sets rehearsal letter explicitly when set to nonempty string.

        Returns string or none.
        '''
        return self._rehearsal_letter

    @property
    def score(self):
        r'''Gets score.

        Returns score or none.
        '''
        return self._score

    @property
    def score_template(self):
        r'''Gets score template.

        ..  container:: example

            Gets score template:

            >>> maker = baca.SegmentMaker(
            ...     score_template=baca.SingleStaffScoreTemplate(),
            ...     )

            >>> maker.score_template
            SingleStaffScoreTemplate()

        Defaults to none.

        Set to score template or none.

        Returns score template or none.
        '''
        return self._score_template

    @property
    def skip_wellformedness_checks(self):
        r'''Is true when segment skips wellformedness checks.

        Returns true, false or none.
        '''
        return self._skip_wellformedness_checks

    @property
    def skips_instead_of_rests(self):
        r'''Is true when segment fills empty measures with skips.

        ..  container:: example

            Fills empty measures with multimeasure rests:

            >>> maker = baca.SegmentMaker(
            ...     score_template=baca.SingleStaffScoreTemplate(),
            ...     time_signatures=[(4, 8), (3, 8), (4, 8), (3, 8)],
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
                            \bar ""                                                                      %! EMPTY_START_BAR:SM2
                            \once \override Score.TimeSignature.color = #(x11-color 'blue)               %! EXPLICIT_TIME_SIGNATURE_COLOR:SM6
                            s1 * 1/2
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
                            \override Score.BarLine.transparent = ##f                                    %! SM5
                            \bar "|"                                                                     %! SM5
                <BLANKLINE>
                        }
                    >>
                    \context MusicContext = "MusicContext" <<
                        \context Staff = "MusicStaff" {
                            \context Voice = "MusicVoice" {
                <BLANKLINE>
                                % MusicVoice [measure 1]                                                 %! SM4
                                R1 * 1/2
                <BLANKLINE>
                                % MusicVoice [measure 2]                                                 %! SM4
                                R1 * 3/8
                <BLANKLINE>
                                % MusicVoice [measure 3]                                                 %! SM4
                                R1 * 1/2
                <BLANKLINE>
                                % MusicVoice [measure 4]                                                 %! SM4
                                R1 * 3/8
                <BLANKLINE>
                            }
                        }
                    >>
                >>

        ..  container:: example

            Fills empty measures with skips:

            >>> maker = baca.SegmentMaker(
            ...     score_template=baca.SingleStaffScoreTemplate(),
            ...     skips_instead_of_rests=True,
            ...     time_signatures=[(4, 8), (3, 8), (4, 8), (3, 8)],
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
                            \bar ""                                                                      %! EMPTY_START_BAR:SM2
                            \once \override Score.TimeSignature.color = #(x11-color 'blue)               %! EXPLICIT_TIME_SIGNATURE_COLOR:SM6
                            s1 * 1/2
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
                            \override Score.BarLine.transparent = ##f                                    %! SM5
                            \bar "|"                                                                     %! SM5
                <BLANKLINE>
                        }
                    >>
                    \context MusicContext = "MusicContext" <<
                        \context Staff = "MusicStaff" {
                            \context Voice = "MusicVoice" {
                <BLANKLINE>
                                % MusicVoice [measure 1]                                                 %! SM4
                                s1 * 1/2
                <BLANKLINE>
                                % MusicVoice [measure 2]                                                 %! SM4
                                s1 * 3/8
                <BLANKLINE>
                                % MusicVoice [measure 3]                                                 %! SM4
                                s1 * 1/2
                <BLANKLINE>
                                % MusicVoice [measure 4]                                                 %! SM4
                                s1 * 3/8
                <BLANKLINE>
                            }
                        }
                    >>
                >>

        Defaults to none.

        Set to true, false or none.

        Returns true, false or none.
        '''
        return self._skips_instead_of_rests

    @property
    def spacing_specifier(self):
        r'''Gets spacing specifier.

        Defaults to none.

        Set to spacing specifier or none.

        Returns spacing specifier or none.
        '''
        return self._spacing_specifier

    @property
    def stage_count(self):
        r'''Gets stage count.

        Defined equal to 1 when `self.measures_per_stage` is none.

        Returns nonnegative integer.
        '''
        if self.measures_per_stage is None:
            return 1
        return len(self.measures_per_stage)

    @property
    def stage_label_base_string(self):
        r'''Gets stage label base string.

        ..  container:: example

            Sets stage label base string explicitly:

            >>> maker = baca.SegmentMaker(
            ...     ignore_unpitched_notes=True,
            ...     score_template=baca.SingleStaffScoreTemplate(),
            ...     stage_label_base_string='intermezzo',
            ...     time_signatures=[(4, 8), (3, 8), (4, 8), (3, 8)],
            ...     )

            >>> maker(
            ...     baca.scope('MusicVoice', 1),
            ...     baca.make_even_runs(),
            ...     )

            >>> metadata = {'name': 'K'}
            >>> lilypond_file = maker.run(
            ...     environment='docs',
            ...     metadata=metadata,
            ...     )
            >>> abjad.show(lilypond_file, strict=89) # doctest: +SKIP

            ..  docs::

                >>> abjad.f(lilypond_file[abjad.Score], strict=89)
                \context Score = "Score" <<
                    \context GlobalContext = "GlobalContext" <<
                        \context GlobalSkips = "GlobalSkips" {
                <BLANKLINE>
                            % GlobalSkips [measure 1]                                                    %! SM4
                            \time 4/8                                                                    %! EXPLICIT_TIME_SIGNATURE:SM8
                            \bar ""                                                                      %! EMPTY_START_BAR:SM2
                            \once \override Score.TimeSignature.color = #(x11-color 'blue)               %! EXPLICIT_TIME_SIGNATURE_COLOR:SM6
                            s1 * 1/2
                            ^ \markup {                                                                  %! STAGE_NUMBER_MARKUP:SM3
                                \fontsize                                                                %! STAGE_NUMBER_MARKUP:SM3
                                    #-3                                                                  %! STAGE_NUMBER_MARKUP:SM3
                                    \with-color                                                          %! STAGE_NUMBER_MARKUP:SM3
                                        #(x11-color 'DarkCyan)                                           %! STAGE_NUMBER_MARKUP:SM3
                                        [intermezzo.1]                                                   %! STAGE_NUMBER_MARKUP:SM3
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
                                    c'8
                                    [
                <BLANKLINE>
                                    c'8
                <BLANKLINE>
                                    c'8
                <BLANKLINE>
                                    c'8
                                    ]
                                }
                                {
                <BLANKLINE>
                                    % MusicVoice [measure 2]                                             %! SM4
                                    c'8
                                    [
                <BLANKLINE>
                                    c'8
                <BLANKLINE>
                                    c'8
                                    ]
                                }
                                {
                <BLANKLINE>
                                    % MusicVoice [measure 3]                                             %! SM4
                                    c'8
                                    [
                <BLANKLINE>
                                    c'8
                <BLANKLINE>
                                    c'8
                <BLANKLINE>
                                    c'8
                                    ]
                                }
                                {
                <BLANKLINE>
                                    % MusicVoice [measure 4]                                             %! SM4
                                    c'8
                                    [
                <BLANKLINE>
                                    c'8
                <BLANKLINE>
                                    c'8
                                    ]
                <BLANKLINE>
                                }
                            }
                        }
                    >>
                >>

        Defaults to none.

        Set to string or none.

        Returns string or none.
        '''
        return self._stage_label_base_string

    @property
    def time_signatures(self):
        r'''Gets time signatures.

        Set to time signatures.

        Returns tuple of time signatures.
        '''
        return self._time_signatures

    @property
    def transpose_score(self):
        r'''Is true when segment transposes score.

        ..  container:: example

            Transposes score:

            >>> instruments = abjad.InstrumentDictionary()
            >>> instruments['clarinet'] = abjad.ClarinetInBFlat()
            >>> maker = baca.SegmentMaker(
            ...     instruments=instruments,
            ...     score_template=baca.SingleStaffScoreTemplate(),
            ...     time_signatures=[(4, 8), (3, 8), (4, 8), (3, 8)],
            ...     transpose_score=True,
            ...     )

            >>> maker(
            ...     baca.scope('MusicVoice', 1),
            ...     baca.instrument(instruments['clarinet']),
            ...     baca.make_even_runs(),
            ...     baca.pitches('E4 F4'),
            ...     )

            >>> lilypond_file = maker.run(environment='docs')

            ..  docs::

                >>> abjad.f(lilypond_file[abjad.Score], strict=89)
                \context Score = "Score" <<
                    \context GlobalContext = "GlobalContext" <<
                        \context GlobalSkips = "GlobalSkips" {
                <BLANKLINE>
                            % GlobalSkips [measure 1]                                                    %! SM4
                            \time 4/8                                                                    %! EXPLICIT_TIME_SIGNATURE:SM8
                            \bar ""                                                                      %! EMPTY_START_BAR:SM2
                            \once \override Score.TimeSignature.color = #(x11-color 'blue)               %! EXPLICIT_TIME_SIGNATURE_COLOR:SM6
                            s1 * 1/2
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
                                    \set Staff.instrumentName = \markup { "Clarinet in B-flat" }         %! EXPLICIT_INSTRUMENT:SM8
                                    \set Staff.shortInstrumentName = \markup { "Cl. in B-flat" }         %! EXPLICIT_INSTRUMENT:SM8
                                    \once \override Staff.InstrumentName.color = #(x11-color 'blue)      %! EXPLICIT_INSTRUMENT_COLOR:SM6
                                    fs'8
                                    [
                                    ^ \markup {
                                        \column
                                            {
                                                %%% \line                                                %! EXPLICIT_INSTRUMENT_ALERT:SM10
                                                %%%     {                                                %! EXPLICIT_INSTRUMENT_ALERT:SM10
                                                %%%         \vcenter                                     %! EXPLICIT_INSTRUMENT_ALERT:SM10
                                                %%%             (“clarinet”                              %! EXPLICIT_INSTRUMENT_ALERT:SM10
                                                %%%         \vcenter                                     %! EXPLICIT_INSTRUMENT_ALERT:SM10
                                                %%%             "Clarinet in B-flat"                     %! EXPLICIT_INSTRUMENT_ALERT:SM10
                                                %%%         \concat                                      %! EXPLICIT_INSTRUMENT_ALERT:SM10
                                                %%%             {                                        %! EXPLICIT_INSTRUMENT_ALERT:SM10
                                                %%%                 \vcenter                             %! EXPLICIT_INSTRUMENT_ALERT:SM10
                                                %%%                     "Cl. in B-flat"                  %! EXPLICIT_INSTRUMENT_ALERT:SM10
                                                %%%                 \vcenter                             %! EXPLICIT_INSTRUMENT_ALERT:SM10
                                                %%%                     )                                %! EXPLICIT_INSTRUMENT_ALERT:SM10
                                                %%%             }                                        %! EXPLICIT_INSTRUMENT_ALERT:SM10
                                                %%%     }                                                %! EXPLICIT_INSTRUMENT_ALERT:SM10
                                                \line                                                    %! EXPLICIT_INSTRUMENT_ALERT_WITH_COLOR:SM11
                                                    {                                                    %! EXPLICIT_INSTRUMENT_ALERT_WITH_COLOR:SM11
                                                        \with-color                                      %! EXPLICIT_INSTRUMENT_ALERT_WITH_COLOR:SM11
                                                            #(x11-color 'blue)                           %! EXPLICIT_INSTRUMENT_ALERT_WITH_COLOR:SM11
                                                            {                                            %! EXPLICIT_INSTRUMENT_ALERT_WITH_COLOR:SM11
                                                                \vcenter                                 %! EXPLICIT_INSTRUMENT_ALERT_WITH_COLOR:SM11
                                                                    (“clarinet”                          %! EXPLICIT_INSTRUMENT_ALERT_WITH_COLOR:SM11
                                                                \vcenter                                 %! EXPLICIT_INSTRUMENT_ALERT_WITH_COLOR:SM11
                                                                    "Clarinet in B-flat"                 %! EXPLICIT_INSTRUMENT_ALERT_WITH_COLOR:SM11
                                                                \concat                                  %! EXPLICIT_INSTRUMENT_ALERT_WITH_COLOR:SM11
                                                                    {                                    %! EXPLICIT_INSTRUMENT_ALERT_WITH_COLOR:SM11
                                                                        \vcenter                         %! EXPLICIT_INSTRUMENT_ALERT_WITH_COLOR:SM11
                                                                            "Cl. in B-flat"              %! EXPLICIT_INSTRUMENT_ALERT_WITH_COLOR:SM11
                                                                        \vcenter                         %! EXPLICIT_INSTRUMENT_ALERT_WITH_COLOR:SM11
                                                                            )                            %! EXPLICIT_INSTRUMENT_ALERT_WITH_COLOR:SM11
                                                                    }                                    %! EXPLICIT_INSTRUMENT_ALERT_WITH_COLOR:SM11
                                                            }                                            %! EXPLICIT_INSTRUMENT_ALERT_WITH_COLOR:SM11
                                                    }                                                    %! EXPLICIT_INSTRUMENT_ALERT_WITH_COLOR:SM11
                                            }
                                        }
                                    \set Staff.instrumentName = \markup { "Clarinet in B-flat" }         %! REDRAWN_EXPLICIT_INSTRUMENT:SM8
                                    \set Staff.shortInstrumentName = \markup { "Cl. in B-flat" }         %! REDRAWN_EXPLICIT_INSTRUMENT:SM8
                                    \override Staff.InstrumentName.color = #(x11-color 'DeepSkyBlue2)    %! REDRAWN_EXPLICIT_INSTRUMENT_COLOR:SM6
                <BLANKLINE>
                                    g'8
                <BLANKLINE>
                                    fs'8
                <BLANKLINE>
                                    g'8
                                    ]
                                }
                                {
                <BLANKLINE>
                                    % MusicVoice [measure 2]                                             %! SM4
                                    fs'8
                                    [
                <BLANKLINE>
                                    g'8
                <BLANKLINE>
                                    fs'8
                                    ]
                                }
                                {
                <BLANKLINE>
                                    % MusicVoice [measure 3]                                             %! SM4
                                    g'8
                                    [
                <BLANKLINE>
                                    fs'8
                <BLANKLINE>
                                    g'8
                <BLANKLINE>
                                    fs'8
                                    ]
                                }
                                {
                <BLANKLINE>
                                    % MusicVoice [measure 4]                                             %! SM4
                                    g'8
                                    [
                <BLANKLINE>
                                    fs'8
                <BLANKLINE>
                                    g'8
                                    ]
                <BLANKLINE>
                                }
                            }
                        }
                    >>
                >>

        ..  container:: example

            Does not transpose score:

            >>> instruments = abjad.InstrumentDictionary()
            >>> instruments['clarinet'] = abjad.ClarinetInBFlat()
            >>> maker = baca.SegmentMaker(
            ...     instruments=instruments,
            ...     score_template=baca.SingleStaffScoreTemplate(),
            ...     time_signatures=[(4, 8), (3, 8), (4, 8), (3, 8)],
            ...     transpose_score=False,
            ...     )

            >>> maker(
            ...     baca.scope('MusicVoice', 1),
            ...     baca.instrument(instruments['clarinet']),
            ...     baca.make_even_runs(),
            ...     baca.pitches('E4 F4'),
            ...     )

            >>> lilypond_file = maker.run(environment='docs')

            ..  docs::

                >>> abjad.f(lilypond_file[abjad.Score], strict=89)
                \context Score = "Score" <<
                    \context GlobalContext = "GlobalContext" <<
                        \context GlobalSkips = "GlobalSkips" {
                <BLANKLINE>
                            % GlobalSkips [measure 1]                                                    %! SM4
                            \time 4/8                                                                    %! EXPLICIT_TIME_SIGNATURE:SM8
                            \bar ""                                                                      %! EMPTY_START_BAR:SM2
                            \once \override Score.TimeSignature.color = #(x11-color 'blue)               %! EXPLICIT_TIME_SIGNATURE_COLOR:SM6
                            s1 * 1/2
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
                                    \set Staff.instrumentName = \markup { "Clarinet in B-flat" }         %! EXPLICIT_INSTRUMENT:SM8
                                    \set Staff.shortInstrumentName = \markup { "Cl. in B-flat" }         %! EXPLICIT_INSTRUMENT:SM8
                                    \once \override Staff.InstrumentName.color = #(x11-color 'blue)      %! EXPLICIT_INSTRUMENT_COLOR:SM6
                                    e'8
                                    [
                                    ^ \markup {
                                        \column
                                            {
                                                %%% \line                                                %! EXPLICIT_INSTRUMENT_ALERT:SM10
                                                %%%     {                                                %! EXPLICIT_INSTRUMENT_ALERT:SM10
                                                %%%         \vcenter                                     %! EXPLICIT_INSTRUMENT_ALERT:SM10
                                                %%%             (“clarinet”                              %! EXPLICIT_INSTRUMENT_ALERT:SM10
                                                %%%         \vcenter                                     %! EXPLICIT_INSTRUMENT_ALERT:SM10
                                                %%%             "Clarinet in B-flat"                     %! EXPLICIT_INSTRUMENT_ALERT:SM10
                                                %%%         \concat                                      %! EXPLICIT_INSTRUMENT_ALERT:SM10
                                                %%%             {                                        %! EXPLICIT_INSTRUMENT_ALERT:SM10
                                                %%%                 \vcenter                             %! EXPLICIT_INSTRUMENT_ALERT:SM10
                                                %%%                     "Cl. in B-flat"                  %! EXPLICIT_INSTRUMENT_ALERT:SM10
                                                %%%                 \vcenter                             %! EXPLICIT_INSTRUMENT_ALERT:SM10
                                                %%%                     )                                %! EXPLICIT_INSTRUMENT_ALERT:SM10
                                                %%%             }                                        %! EXPLICIT_INSTRUMENT_ALERT:SM10
                                                %%%     }                                                %! EXPLICIT_INSTRUMENT_ALERT:SM10
                                                \line                                                    %! EXPLICIT_INSTRUMENT_ALERT_WITH_COLOR:SM11
                                                    {                                                    %! EXPLICIT_INSTRUMENT_ALERT_WITH_COLOR:SM11
                                                        \with-color                                      %! EXPLICIT_INSTRUMENT_ALERT_WITH_COLOR:SM11
                                                            #(x11-color 'blue)                           %! EXPLICIT_INSTRUMENT_ALERT_WITH_COLOR:SM11
                                                            {                                            %! EXPLICIT_INSTRUMENT_ALERT_WITH_COLOR:SM11
                                                                \vcenter                                 %! EXPLICIT_INSTRUMENT_ALERT_WITH_COLOR:SM11
                                                                    (“clarinet”                          %! EXPLICIT_INSTRUMENT_ALERT_WITH_COLOR:SM11
                                                                \vcenter                                 %! EXPLICIT_INSTRUMENT_ALERT_WITH_COLOR:SM11
                                                                    "Clarinet in B-flat"                 %! EXPLICIT_INSTRUMENT_ALERT_WITH_COLOR:SM11
                                                                \concat                                  %! EXPLICIT_INSTRUMENT_ALERT_WITH_COLOR:SM11
                                                                    {                                    %! EXPLICIT_INSTRUMENT_ALERT_WITH_COLOR:SM11
                                                                        \vcenter                         %! EXPLICIT_INSTRUMENT_ALERT_WITH_COLOR:SM11
                                                                            "Cl. in B-flat"              %! EXPLICIT_INSTRUMENT_ALERT_WITH_COLOR:SM11
                                                                        \vcenter                         %! EXPLICIT_INSTRUMENT_ALERT_WITH_COLOR:SM11
                                                                            )                            %! EXPLICIT_INSTRUMENT_ALERT_WITH_COLOR:SM11
                                                                    }                                    %! EXPLICIT_INSTRUMENT_ALERT_WITH_COLOR:SM11
                                                            }                                            %! EXPLICIT_INSTRUMENT_ALERT_WITH_COLOR:SM11
                                                    }                                                    %! EXPLICIT_INSTRUMENT_ALERT_WITH_COLOR:SM11
                                            }
                                        }
                                    \set Staff.instrumentName = \markup { "Clarinet in B-flat" }         %! REDRAWN_EXPLICIT_INSTRUMENT:SM8
                                    \set Staff.shortInstrumentName = \markup { "Cl. in B-flat" }         %! REDRAWN_EXPLICIT_INSTRUMENT:SM8
                                    \override Staff.InstrumentName.color = #(x11-color 'DeepSkyBlue2)    %! REDRAWN_EXPLICIT_INSTRUMENT_COLOR:SM6
                <BLANKLINE>
                                    f'8
                <BLANKLINE>
                                    e'8
                <BLANKLINE>
                                    f'8
                                    ]
                                }
                                {
                <BLANKLINE>
                                    % MusicVoice [measure 2]                                             %! SM4
                                    e'8
                                    [
                <BLANKLINE>
                                    f'8
                <BLANKLINE>
                                    e'8
                                    ]
                                }
                                {
                <BLANKLINE>
                                    % MusicVoice [measure 3]                                             %! SM4
                                    f'8
                                    [
                <BLANKLINE>
                                    e'8
                <BLANKLINE>
                                    f'8
                <BLANKLINE>
                                    e'8
                                    ]
                                }
                                {
                <BLANKLINE>
                                    % MusicVoice [measure 4]                                             %! SM4
                                    f'8
                                    [
                <BLANKLINE>
                                    e'8
                <BLANKLINE>
                                    f'8
                                    ]
                <BLANKLINE>
                                }
                            }
                        }
                    >>
                >>

        Defaults to none.

        Set to true, false or none.

        Returns true, false or none.
        '''
        return self._transpose_score

    @property
    def wrappers(self):
        r'''Gets wrappers.

        Returns list of wrappers.
        '''
        return self._wrappers

    ### PUBLIC METHODS ###

    def copy_rhythm(self, source, target, **keywords):
        r'''Copies rhythm.

        Gets rhythm command defined at `source` scope start.

        Makes new rhythm command for `target` scope with optional `keywords`.

        Returns none.
        '''
        assert isinstance(source, baca.Scope)
        assert isinstance(target, baca.Scope)
        for wrapper in self.wrappers:
            if not isinstance(wrapper.command, baca.RhythmCommand):
                continue
            if wrapper.scope.voice_name != source.voice_name:
                continue
            assert isinstance(wrapper.scope.stages, tuple)
            start = wrapper.scope.stages[0]
            stop = wrapper.scope.stages[1] + 1
            stages = range(start, stop)
            if source.stages[0] in stages:
                break
        else:
            raise Exception(f'no {voice_name!r} rhythm command for {stage}.')
        assert isinstance(wrapper, baca.CommandWrapper)
        assert isinstance(wrapper.command, baca.RhythmCommand)
        command = abjad.new(wrapper.command, **keywords)
        wrapper = baca.CommandWrapper(command, target)
        self.wrappers.append(wrapper)

    def run(
        self,
        builds_metadata=None,
        deactivate=None,
        environment=None,
        metadata=None,
        midi=None,
        previous_metadata=None,
        remove=None,
        ):
        r'''Runs segment-maker.

        Leave `environment` set to none to render segments in real score.

        Set `environment` to `'docs'` for API examples.
        
        Set `environment` to `'external'` to debug API examples in an external
        file.

        Returns LilyPond file.
        '''
        deactivate = deactivate or []
        assert all(isinstance(_, str) for _ in deactivate), repr(deactivate)
        self._builds_metadata = abjad.TypedOrderedDict(builds_metadata)
        self._environment = environment
        self._midi = midi
        self._previous_metadata = abjad.TypedOrderedDict(previous_metadata)
        self._make_score()
        self._make_lilypond_file()
        self._make_global_skips()
        self._label_stage_numbers()
        self._call_rhythm_commands()
        self._extend_beams()
        self._reapply_persistent_indicators()
        self._call_commands()
        self._shorten_long_repeat_ties()
        self._attach_score_template_defaults()
        #self._reapply_persistent_indicators()
        self._categorize_uncategorized_persistent_indicators()
        self._tag_clock_time()
        self._apply_spacing_specifier()
        self._transpose_score_()
        self._attach_rehearsal_mark()
        self._add_final_bar_line()
        self._add_final_markup()
        self._color_unregistered_pitches()
        self._color_unpitched_notes()
        self._check_wellformedness()
        self._check_design()
        self._check_range()
        self._color_repeat_pitch_classes_()
        self._color_octaves_()
        self._remove_redundant_time_signatures()
        self._whitespace_leaves()
        self._comment_measure_numbers()
        self._apply_layout_measure_map()
        self._cache_break_offsets()
        self._apply_fermata_measure_staff_line_count()
        self._deactivate_tags(deactivate)
        self._remove_tags(remove)
        self._collect_metadata()
        self._print_segment_duration_()
        return self._lilypond_file

    def validate_measure_count(self, measure_count):
        r'''Validates measure count.

        Raises exception when `measure_count` is incorrect.

        Returns none.
        '''
        if not measure_count == self.measure_count:
            message = f'segment measure count is not {measure_count}'
            message += f' but {self.measure_count}.'
            raise Exception(message)

    def validate_measures_per_stage(self):
        r'''Validates measures per stage.

        Raises exception when measures per stage do not match measure count.

        Returns none.
        '''
        if self.measures_per_stage is None:
            return
        if not sum(self.measures_per_stage) == self.measure_count:
            message = f'measures per stage {self.measures_per_stage}'
            message += f' do not match measure count {self.measure_count}.'
            raise Exception(message)

    def validate_stage_count(self, stage_count):
        r'''Validates stage count.

        Raises exception when `stage_count` is incorrect.

        Returns none.
        '''
        if not stage_count == self.stage_count:
            message = f'stage count is not {stage_count}'
            message += f' but {self.stage_count}.'
            raise Exception(message)
