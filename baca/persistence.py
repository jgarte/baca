r"""
..  container:: example

    Clefs.

    ..  container:: example

        Default clefs color purple and redraw dull purple:

        >>> breaks = baca.breaks(
        ...     baca.page(
        ...         [1, 0, (11,)],
        ...         [2, 15, (11,)],
        ...         ),
        ...     )
        >>> score_template = baca.SingleStaffScoreTemplate()
        >>> triple = ('Music_Staff', 'default_clef', abjad.Clef('treble'))
        >>> score_template.defaults.append(triple)
        >>> maker = baca.SegmentMaker(
        ...     breaks=breaks,
        ...     score_template=score_template,
        ...     spacing=baca.minimum_duration((1, 24)),
        ...     time_signatures=[(3, 8), (3, 8)],
        ...     )

        >>> lilypond_file = maker.run(environment='docs')
        >>> block = abjad.Block(name='layout')
        >>> block.indent = 0
        >>> lilypond_file.items.insert(0, block)
        >>> abjad.show(lilypond_file, strict=89) # doctest: +SKIP

        ..  docs::

            >>> abjad.f(lilypond_file[abjad.Score], strict=89)
            <BLANKLINE>
            \context Score = "Score"                                                                 %! baca.SingleStaffScoreTemplate.__call__()
            <<                                                                                       %! baca.SingleStaffScoreTemplate.__call__()
            <BLANKLINE>
                \context GlobalContext = "Global_Context"                                            %! abjad.ScoreTemplate._make_global_context()
                <<                                                                                   %! abjad.ScoreTemplate._make_global_context()
            <BLANKLINE>
                    \context GlobalSkips = "Global_Skips"                                            %! abjad.ScoreTemplate._make_global_context()
                    {                                                                                %! abjad.ScoreTemplate._make_global_context()
            <BLANKLINE>
                        % [Global_Skips measure 1]                                                   %! baca.SegmentMaker._comment_measure_numbers()
                        \baca-new-spacing-section #1 #24                                             %! SPACING_COMMAND:baca.HorizontalSpacingSpecifier.__call__(1)
                        \autoPageBreaksOff                                                           %! BREAK:baca.BreakMeasureMap.__call__(1)
                        \noBreak                                                                     %! BREAK:baca.BreakMeasureMap.__call__(2)
                        \baca-lbsd #0 #'(11)                                                         %! BREAK:baca.IndicatorCommand._call()
                        \time 3/8                                                                    %! baca.SegmentMaker._make_global_skips(2):baca.SegmentMaker._set_status_tag():EXPLICIT_TIME_SIGNATURE
                        \baca-time-signature-color #'blue                                            %! baca.SegmentMaker._attach_color_literal(2):EXPLICIT_TIME_SIGNATURE_COLOR
                        \pageBreak                                                                   %! BREAK:baca.IndicatorCommand._call()
                        s1 * 3/8                                                                     %! baca.SegmentMaker._make_global_skips(1)
            <BLANKLINE>
                        % [Global_Skips measure 2]                                                   %! baca.SegmentMaker._comment_measure_numbers()
                        \baca-new-spacing-section #1 #24                                             %! SPACING_COMMAND:baca.HorizontalSpacingSpecifier.__call__(1)
                        \noBreak                                                                     %! BREAK:baca.BreakMeasureMap.__call__(2)
                        \baca-lbsd #15 #'(11)                                                        %! BREAK:baca.IndicatorCommand._call()
                        \break                                                                       %! BREAK:baca.IndicatorCommand._call()
                        s1 * 3/8                                                                     %! baca.SegmentMaker._make_global_skips(1)
            <BLANKLINE>
                        % [Global_Skips measure 3]                                                   %! baca.SegmentMaker._comment_measure_numbers():baca.SegmentMaker._style_phantom_measures(1):PHANTOM
                        \baca-new-spacing-section #1 #4                                              %! SPACING_COMMAND:baca.HorizontalSpacingSpecifier.__call__(1):baca.SegmentMaker._style_phantom_measures(1):PHANTOM
                        \noBreak                                                                     %! BREAK:baca.BreakMeasureMap.__call__(2):baca.SegmentMaker._style_phantom_measures(1):PHANTOM
                        \time 1/4                                                                    %! baca.SegmentMaker._make_global_skips(3):PHANTOM:baca.SegmentMaker._set_status_tag():EXPLICIT_TIME_SIGNATURE:baca.SegmentMaker._style_phantom_measures(1)
                        \baca-time-signature-transparent                                             %! baca.SegmentMaker._style_phantom_measures(2):PHANTOM
                        s1 * 1/4                                                                     %! baca.SegmentMaker._make_global_skips(3):PHANTOM
                        \once \override Score.BarLine.transparent = ##t                              %! baca.SegmentMaker._style_phantom_measures(3):PHANTOM
                        \once \override Score.SpanBar.transparent = ##t                              %! baca.SegmentMaker._style_phantom_measures(3):PHANTOM
            <BLANKLINE>
                    }                                                                                %! abjad.ScoreTemplate._make_global_context()
            <BLANKLINE>
                >>                                                                                   %! abjad.ScoreTemplate._make_global_context()
            <BLANKLINE>
                \context MusicContext = "Music_Context"                                              %! baca.SingleStaffScoreTemplate.__call__()
                <<                                                                                   %! baca.SingleStaffScoreTemplate.__call__()
            <BLANKLINE>
                    \context Staff = "Music_Staff"                                                   %! baca.SingleStaffScoreTemplate.__call__()
                    {                                                                                %! baca.SingleStaffScoreTemplate.__call__()
            <BLANKLINE>
                        \context Voice = "Music_Voice"                                               %! baca.SingleStaffScoreTemplate.__call__()
                        {                                                                            %! baca.SingleStaffScoreTemplate.__call__()
            <BLANKLINE>
                            % [Music_Voice measure 1]                                                %! baca.SegmentMaker._comment_measure_numbers()
                            \clef "treble"                                                           %! abjad.ScoreTemplate.attach_defaults(3):baca.SegmentMaker._set_status_tag():DEFAULT_CLEF
                            \once \override Staff.Clef.color = #(x11-color 'DarkViolet)              %! baca.SegmentMaker._attach_color_literal(2):DEFAULT_CLEF_COLOR
                        %@% \override Staff.Clef.color = ##f                                         %! baca.SegmentMaker._attach_color_literal(1):DEFAULT_CLEF_COLOR_CANCELLATION
                            \set Staff.forceClef = ##t                                               %! abjad.ScoreTemplate.attach_defaults(3):baca.SegmentMaker._treat_persistent_wrapper(2):baca.SegmentMaker._set_status_tag():DEFAULT_CLEF
                            R1 * 3/8                                                                 %! baca.SegmentMaker._call_rhythm_commands()
                        %@% ^ \baca-duration-multiplier-markup #"3" #"8"                             %! baca.SegmentMaker._label_duration_multipliers():DURATION_MULTIPLIER
                            \override Staff.Clef.color = #(x11-color 'violet)                        %! baca.SegmentMaker._attach_color_literal(2):DEFAULT_CLEF_REDRAW_COLOR
            <BLANKLINE>
                            % [Music_Voice measure 2]                                                %! baca.SegmentMaker._comment_measure_numbers()
                            R1 * 3/8                                                                 %! baca.SegmentMaker._call_rhythm_commands()
                        %@% ^ \baca-duration-multiplier-markup #"3" #"8"                             %! baca.SegmentMaker._label_duration_multipliers():DURATION_MULTIPLIER
            <BLANKLINE>
                            <<                                                                       %! baca.SegmentMaker._make_multimeasure_rest_container(7):PHANTOM
            <BLANKLINE>
                                \context Voice = "Music_Voice"                                       %! baca.SegmentMaker._make_multimeasure_rest_container(4):PHANTOM
                                {                                                                    %! baca.SegmentMaker._make_multimeasure_rest_container(4):PHANTOM
            <BLANKLINE>
                                    % [Music_Voice measure 3]                                        %! baca.SegmentMaker._comment_measure_numbers():baca.SegmentMaker._style_phantom_measures(5):PHANTOM
                                    \abjad-invisible-music-coloring                                  %! baca.SegmentMaker._make_multimeasure_rest_container(2):PHANTOM:MULTIMEASURE_REST:INVISIBLE_MUSIC_COLORING:baca.SegmentMaker._style_phantom_measures(5)
                                %@% \abjad-invisible-music                                           %! baca.SegmentMaker._make_multimeasure_rest_container(3):PHANTOM:MULTIMEASURE_REST:INVISIBLE_MUSIC_COMMAND:baca.SegmentMaker._style_phantom_measures(5)
                                    R1 * 1/4                                                         %! baca.SegmentMaker._make_multimeasure_rest_container(1):PHANTOM:HIDDEN:MULTIMEASURE_REST
                                %@% ^ \baca-duration-multiplier-markup #"1" #"4"                     %! baca.SegmentMaker._label_duration_multipliers():DURATION_MULTIPLIER:HIDDEN:MULTIMEASURE_REST:PHANTOM:baca.SegmentMaker._style_phantom_measures(5)
            <BLANKLINE>
                                }                                                                    %! baca.SegmentMaker._make_multimeasure_rest_container(4):PHANTOM
            <BLANKLINE>
                                \context Voice = "Rest_Voice"                                        %! baca.SegmentMaker._make_multimeasure_rest_container(6):PHANTOM
                                {                                                                    %! baca.SegmentMaker._make_multimeasure_rest_container(6):PHANTOM
            <BLANKLINE>
                                    % [Rest_Voice measure 3]                                         %! baca.SegmentMaker._comment_measure_numbers():baca.SegmentMaker._style_phantom_measures(5):PHANTOM
                                    \once \override Score.TimeSignature.X-extent = ##f               %! baca.SegmentMaker._style_phantom_measures(6):PHANTOM
                                    \once \override MultiMeasureRest.transparent = ##t               %! baca.SegmentMaker._style_phantom_measures(7):PHANTOM
                                    \stopStaff                                                       %! baca.SegmentMaker._style_phantom_measures(8):PHANTOM
                                    \once \override Staff.StaffSymbol.transparent = ##t              %! baca.SegmentMaker._style_phantom_measures(8):PHANTOM
                                    \startStaff                                                      %! baca.SegmentMaker._style_phantom_measures(8):PHANTOM
                                    R1 * 1/4                                                         %! baca.SegmentMaker._make_multimeasure_rest_container(5):PHANTOM:REST_VOICE:MULTIMEASURE_REST
                                %@% ^ \baca-duration-multiplier-markup #"1" #"4"                     %! baca.SegmentMaker._label_duration_multipliers():DURATION_MULTIPLIER:MULTIMEASURE_REST:PHANTOM:REST_VOICE:baca.SegmentMaker._style_phantom_measures(5)
            <BLANKLINE>
                                }                                                                    %! baca.SegmentMaker._make_multimeasure_rest_container(6):PHANTOM
            <BLANKLINE>
                            >>                                                                       %! baca.SegmentMaker._make_multimeasure_rest_container(7):PHANTOM
            <BLANKLINE>
                        }                                                                            %! baca.SingleStaffScoreTemplate.__call__()
            <BLANKLINE>
                    }                                                                                %! baca.SingleStaffScoreTemplate.__call__()
            <BLANKLINE>
                >>                                                                                   %! baca.SingleStaffScoreTemplate.__call__()
            <BLANKLINE>
            >>                                                                                       %! baca.SingleStaffScoreTemplate.__call__()

    ..  container:: example

        Explicit clefs color blue and redraw dull blue:

        >>> breaks = baca.breaks(
        ...     baca.page(
        ...         [1, 0, (11,)],
        ...         [2, 15, (11,)],
        ...         ),
        ...     )
        >>> maker = baca.SegmentMaker(
        ...     breaks=breaks,
        ...     score_template=baca.SingleStaffScoreTemplate(),
        ...     spacing=baca.minimum_duration((1, 24)),
        ...     time_signatures=[(3, 8), (3, 8)],
        ...     )
        >>> maker(
        ...     'Music_Voice',
        ...     baca.clef('treble'),
        ...     )

        >>> lilypond_file = maker.run(environment='docs')
        >>> block = abjad.Block(name='layout')
        >>> block.indent = 0
        >>> lilypond_file.items.insert(0, block)
        >>> abjad.show(lilypond_file, strict=89) # doctest: +SKIP

        ..  docs::

            >>> abjad.f(lilypond_file[abjad.Score], strict=89)
            <BLANKLINE>
            \context Score = "Score"                                                                 %! baca.SingleStaffScoreTemplate.__call__()
            <<                                                                                       %! baca.SingleStaffScoreTemplate.__call__()
            <BLANKLINE>
                \context GlobalContext = "Global_Context"                                            %! abjad.ScoreTemplate._make_global_context()
                <<                                                                                   %! abjad.ScoreTemplate._make_global_context()
            <BLANKLINE>
                    \context GlobalSkips = "Global_Skips"                                            %! abjad.ScoreTemplate._make_global_context()
                    {                                                                                %! abjad.ScoreTemplate._make_global_context()
            <BLANKLINE>
                        % [Global_Skips measure 1]                                                   %! baca.SegmentMaker._comment_measure_numbers()
                        \baca-new-spacing-section #1 #24                                             %! SPACING_COMMAND:baca.HorizontalSpacingSpecifier.__call__(1)
                        \autoPageBreaksOff                                                           %! BREAK:baca.BreakMeasureMap.__call__(1)
                        \noBreak                                                                     %! BREAK:baca.BreakMeasureMap.__call__(2)
                        \baca-lbsd #0 #'(11)                                                         %! BREAK:baca.IndicatorCommand._call()
                        \time 3/8                                                                    %! baca.SegmentMaker._make_global_skips(2):baca.SegmentMaker._set_status_tag():EXPLICIT_TIME_SIGNATURE
                        \baca-time-signature-color #'blue                                            %! baca.SegmentMaker._attach_color_literal(2):EXPLICIT_TIME_SIGNATURE_COLOR
                        \pageBreak                                                                   %! BREAK:baca.IndicatorCommand._call()
                        s1 * 3/8                                                                     %! baca.SegmentMaker._make_global_skips(1)
            <BLANKLINE>
                        % [Global_Skips measure 2]                                                   %! baca.SegmentMaker._comment_measure_numbers()
                        \baca-new-spacing-section #1 #24                                             %! SPACING_COMMAND:baca.HorizontalSpacingSpecifier.__call__(1)
                        \noBreak                                                                     %! BREAK:baca.BreakMeasureMap.__call__(2)
                        \baca-lbsd #15 #'(11)                                                        %! BREAK:baca.IndicatorCommand._call()
                        \break                                                                       %! BREAK:baca.IndicatorCommand._call()
                        s1 * 3/8                                                                     %! baca.SegmentMaker._make_global_skips(1)
            <BLANKLINE>
                        % [Global_Skips measure 3]                                                   %! baca.SegmentMaker._comment_measure_numbers():baca.SegmentMaker._style_phantom_measures(1):PHANTOM
                        \baca-new-spacing-section #1 #4                                              %! SPACING_COMMAND:baca.HorizontalSpacingSpecifier.__call__(1):baca.SegmentMaker._style_phantom_measures(1):PHANTOM
                        \noBreak                                                                     %! BREAK:baca.BreakMeasureMap.__call__(2):baca.SegmentMaker._style_phantom_measures(1):PHANTOM
                        \time 1/4                                                                    %! baca.SegmentMaker._make_global_skips(3):PHANTOM:baca.SegmentMaker._set_status_tag():EXPLICIT_TIME_SIGNATURE:baca.SegmentMaker._style_phantom_measures(1)
                        \baca-time-signature-transparent                                             %! baca.SegmentMaker._style_phantom_measures(2):PHANTOM
                        s1 * 1/4                                                                     %! baca.SegmentMaker._make_global_skips(3):PHANTOM
                        \once \override Score.BarLine.transparent = ##t                              %! baca.SegmentMaker._style_phantom_measures(3):PHANTOM
                        \once \override Score.SpanBar.transparent = ##t                              %! baca.SegmentMaker._style_phantom_measures(3):PHANTOM
            <BLANKLINE>
                    }                                                                                %! abjad.ScoreTemplate._make_global_context()
            <BLANKLINE>
                >>                                                                                   %! abjad.ScoreTemplate._make_global_context()
            <BLANKLINE>
                \context MusicContext = "Music_Context"                                              %! baca.SingleStaffScoreTemplate.__call__()
                <<                                                                                   %! baca.SingleStaffScoreTemplate.__call__()
            <BLANKLINE>
                    \context Staff = "Music_Staff"                                                   %! baca.SingleStaffScoreTemplate.__call__()
                    {                                                                                %! baca.SingleStaffScoreTemplate.__call__()
            <BLANKLINE>
                        \context Voice = "Music_Voice"                                               %! baca.SingleStaffScoreTemplate.__call__()
                        {                                                                            %! baca.SingleStaffScoreTemplate.__call__()
            <BLANKLINE>
                            % [Music_Voice measure 1]                                                %! baca.SegmentMaker._comment_measure_numbers()
                            \clef "treble"                                                           %! baca.clef():baca.IndicatorCommand._call():baca.SegmentMaker._set_status_tag():EXPLICIT_CLEF
                            \once \override Staff.Clef.color = #(x11-color 'blue)                    %! baca.SegmentMaker._attach_color_literal(2):EXPLICIT_CLEF_COLOR
                        %@% \override Staff.Clef.color = ##f                                         %! baca.SegmentMaker._attach_color_literal(1):EXPLICIT_CLEF_COLOR_CANCELLATION
                            \set Staff.forceClef = ##t                                               %! baca.clef():baca.IndicatorCommand._call():baca.SegmentMaker._treat_persistent_wrapper(2):baca.SegmentMaker._set_status_tag():EXPLICIT_CLEF
                            R1 * 3/8                                                                 %! baca.SegmentMaker._call_rhythm_commands()
                        %@% ^ \baca-duration-multiplier-markup #"3" #"8"                             %! baca.SegmentMaker._label_duration_multipliers():DURATION_MULTIPLIER
                            \override Staff.Clef.color = #(x11-color 'DeepSkyBlue2)                  %! baca.SegmentMaker._attach_color_literal(2):EXPLICIT_CLEF_REDRAW_COLOR
            <BLANKLINE>
                            % [Music_Voice measure 2]                                                %! baca.SegmentMaker._comment_measure_numbers()
                            R1 * 3/8                                                                 %! baca.SegmentMaker._call_rhythm_commands()
                        %@% ^ \baca-duration-multiplier-markup #"3" #"8"                             %! baca.SegmentMaker._label_duration_multipliers():DURATION_MULTIPLIER
            <BLANKLINE>
                            <<                                                                       %! baca.SegmentMaker._make_multimeasure_rest_container(7):PHANTOM
            <BLANKLINE>
                                \context Voice = "Music_Voice"                                       %! baca.SegmentMaker._make_multimeasure_rest_container(4):PHANTOM
                                {                                                                    %! baca.SegmentMaker._make_multimeasure_rest_container(4):PHANTOM
            <BLANKLINE>
                                    % [Music_Voice measure 3]                                        %! baca.SegmentMaker._comment_measure_numbers():baca.SegmentMaker._style_phantom_measures(5):PHANTOM
                                    \abjad-invisible-music-coloring                                  %! baca.SegmentMaker._make_multimeasure_rest_container(2):PHANTOM:MULTIMEASURE_REST:INVISIBLE_MUSIC_COLORING:baca.SegmentMaker._style_phantom_measures(5)
                                %@% \abjad-invisible-music                                           %! baca.SegmentMaker._make_multimeasure_rest_container(3):PHANTOM:MULTIMEASURE_REST:INVISIBLE_MUSIC_COMMAND:baca.SegmentMaker._style_phantom_measures(5)
                                    R1 * 1/4                                                         %! baca.SegmentMaker._make_multimeasure_rest_container(1):PHANTOM:HIDDEN:MULTIMEASURE_REST
                                %@% ^ \baca-duration-multiplier-markup #"1" #"4"                     %! baca.SegmentMaker._label_duration_multipliers():DURATION_MULTIPLIER:HIDDEN:MULTIMEASURE_REST:PHANTOM:baca.SegmentMaker._style_phantom_measures(5)
            <BLANKLINE>
                                }                                                                    %! baca.SegmentMaker._make_multimeasure_rest_container(4):PHANTOM
            <BLANKLINE>
                                \context Voice = "Rest_Voice"                                        %! baca.SegmentMaker._make_multimeasure_rest_container(6):PHANTOM
                                {                                                                    %! baca.SegmentMaker._make_multimeasure_rest_container(6):PHANTOM
            <BLANKLINE>
                                    % [Rest_Voice measure 3]                                         %! baca.SegmentMaker._comment_measure_numbers():baca.SegmentMaker._style_phantom_measures(5):PHANTOM
                                    \once \override Score.TimeSignature.X-extent = ##f               %! baca.SegmentMaker._style_phantom_measures(6):PHANTOM
                                    \once \override MultiMeasureRest.transparent = ##t               %! baca.SegmentMaker._style_phantom_measures(7):PHANTOM
                                    \stopStaff                                                       %! baca.SegmentMaker._style_phantom_measures(8):PHANTOM
                                    \once \override Staff.StaffSymbol.transparent = ##t              %! baca.SegmentMaker._style_phantom_measures(8):PHANTOM
                                    \startStaff                                                      %! baca.SegmentMaker._style_phantom_measures(8):PHANTOM
                                    R1 * 1/4                                                         %! baca.SegmentMaker._make_multimeasure_rest_container(5):PHANTOM:REST_VOICE:MULTIMEASURE_REST
                                %@% ^ \baca-duration-multiplier-markup #"1" #"4"                     %! baca.SegmentMaker._label_duration_multipliers():DURATION_MULTIPLIER:MULTIMEASURE_REST:PHANTOM:REST_VOICE:baca.SegmentMaker._style_phantom_measures(5)
            <BLANKLINE>
                                }                                                                    %! baca.SegmentMaker._make_multimeasure_rest_container(6):PHANTOM
            <BLANKLINE>
                            >>                                                                       %! baca.SegmentMaker._make_multimeasure_rest_container(7):PHANTOM
            <BLANKLINE>
                        }                                                                            %! baca.SingleStaffScoreTemplate.__call__()
            <BLANKLINE>
                    }                                                                                %! baca.SingleStaffScoreTemplate.__call__()
            <BLANKLINE>
                >>                                                                                   %! baca.SingleStaffScoreTemplate.__call__()
            <BLANKLINE>
            >>                                                                                       %! baca.SingleStaffScoreTemplate.__call__()

        Even after a previous clef:

        >>> breaks = baca.breaks(
        ...     baca.page(
        ...         [1, 0, (11,)],
        ...         [2, 15, (11,)],
        ...         ),
        ...     )
        >>> maker = baca.SegmentMaker(
        ...     breaks=breaks,
        ...     score_template=baca.SingleStaffScoreTemplate(),
        ...     spacing=baca.minimum_duration((1, 24)),
        ...     time_signatures=[(3, 8), (3, 8)],
        ...     )
        >>> maker(
        ...     'Music_Voice',
        ...     baca.clef('alto'),
        ...     )

        >>> metadata, persist = {}, {}
        >>> persist['persistent_indicators'] = {}
        >>> persist['persistent_indicators']['Music_Staff'] = [
        ...     abjad.Momento(
        ...         context='Music_Voice',
        ...         prototype='abjad.Clef',
        ...         value='treble',
        ...         )
        ...     ]
        >>> metadata['segment_number'] = 1
        >>> lilypond_file = maker.run(
        ...     environment='docs',
        ...     previous_metadata=metadata,
        ...     previous_persist=persist,
        ...     )
        >>> block = abjad.Block(name='layout')
        >>> block.indent = 0
        >>> lilypond_file.items.insert(0, block)
        >>> abjad.show(lilypond_file, strict=89) # doctest: +SKIP

        ..  docs::

            >>> abjad.f(lilypond_file[abjad.Score], strict=89)
            <BLANKLINE>
            \context Score = "Score"                                                                 %! baca.SingleStaffScoreTemplate.__call__()
            <<                                                                                       %! baca.SingleStaffScoreTemplate.__call__()
            <BLANKLINE>
                \context GlobalContext = "Global_Context"                                            %! abjad.ScoreTemplate._make_global_context()
                <<                                                                                   %! abjad.ScoreTemplate._make_global_context()
            <BLANKLINE>
                    \context GlobalSkips = "Global_Skips"                                            %! abjad.ScoreTemplate._make_global_context()
                    {                                                                                %! abjad.ScoreTemplate._make_global_context()
            <BLANKLINE>
                        % [Global_Skips measure 1]                                                   %! baca.SegmentMaker._comment_measure_numbers()
                        \baca-new-spacing-section #1 #24                                             %! SPACING_COMMAND:baca.HorizontalSpacingSpecifier.__call__(1)
                        \autoPageBreaksOff                                                           %! BREAK:baca.BreakMeasureMap.__call__(1)
                        \noBreak                                                                     %! BREAK:baca.BreakMeasureMap.__call__(2)
                        \baca-lbsd #0 #'(11)                                                         %! BREAK:baca.IndicatorCommand._call()
                        \time 3/8                                                                    %! baca.SegmentMaker._make_global_skips(2):baca.SegmentMaker._set_status_tag():EXPLICIT_TIME_SIGNATURE
                        \bar ""                                                                      %! EMPTY_START_BAR:+SEGMENT:baca.SegmentMaker._make_global_skips(4)
                        \baca-time-signature-color #'blue                                            %! baca.SegmentMaker._attach_color_literal(2):EXPLICIT_TIME_SIGNATURE_COLOR
                        \pageBreak                                                                   %! BREAK:baca.IndicatorCommand._call()
                        s1 * 3/8                                                                     %! baca.SegmentMaker._make_global_skips(1)
            <BLANKLINE>
                        % [Global_Skips measure 2]                                                   %! baca.SegmentMaker._comment_measure_numbers()
                        \baca-new-spacing-section #1 #24                                             %! SPACING_COMMAND:baca.HorizontalSpacingSpecifier.__call__(1)
                        \noBreak                                                                     %! BREAK:baca.BreakMeasureMap.__call__(2)
                        \baca-lbsd #15 #'(11)                                                        %! BREAK:baca.IndicatorCommand._call()
                        \break                                                                       %! BREAK:baca.IndicatorCommand._call()
                        s1 * 3/8                                                                     %! baca.SegmentMaker._make_global_skips(1)
            <BLANKLINE>
                        % [Global_Skips measure 3]                                                   %! baca.SegmentMaker._comment_measure_numbers():baca.SegmentMaker._style_phantom_measures(1):PHANTOM
                        \baca-new-spacing-section #1 #4                                              %! SPACING_COMMAND:baca.HorizontalSpacingSpecifier.__call__(1):baca.SegmentMaker._style_phantom_measures(1):PHANTOM
                        \noBreak                                                                     %! BREAK:baca.BreakMeasureMap.__call__(2):baca.SegmentMaker._style_phantom_measures(1):PHANTOM
                        \time 1/4                                                                    %! baca.SegmentMaker._make_global_skips(3):PHANTOM:baca.SegmentMaker._set_status_tag():EXPLICIT_TIME_SIGNATURE:baca.SegmentMaker._style_phantom_measures(1)
                        \baca-time-signature-transparent                                             %! baca.SegmentMaker._style_phantom_measures(2):PHANTOM
                        s1 * 1/4                                                                     %! baca.SegmentMaker._make_global_skips(3):PHANTOM
                        \once \override Score.BarLine.transparent = ##t                              %! baca.SegmentMaker._style_phantom_measures(3):PHANTOM
                        \once \override Score.SpanBar.transparent = ##t                              %! baca.SegmentMaker._style_phantom_measures(3):PHANTOM
            <BLANKLINE>
                    }                                                                                %! abjad.ScoreTemplate._make_global_context()
            <BLANKLINE>
                >>                                                                                   %! abjad.ScoreTemplate._make_global_context()
            <BLANKLINE>
                \context MusicContext = "Music_Context"                                              %! baca.SingleStaffScoreTemplate.__call__()
                <<                                                                                   %! baca.SingleStaffScoreTemplate.__call__()
            <BLANKLINE>
                    \context Staff = "Music_Staff"                                                   %! baca.SingleStaffScoreTemplate.__call__()
                    {                                                                                %! baca.SingleStaffScoreTemplate.__call__()
            <BLANKLINE>
                        \context Voice = "Music_Voice"                                               %! baca.SingleStaffScoreTemplate.__call__()
                        {                                                                            %! baca.SingleStaffScoreTemplate.__call__()
            <BLANKLINE>
                            % [Music_Voice measure 1]                                                %! baca.SegmentMaker._comment_measure_numbers()
                            \clef "alto"                                                             %! baca.clef():baca.IndicatorCommand._call():baca.SegmentMaker._set_status_tag():EXPLICIT_CLEF
                            \once \override Staff.Clef.color = #(x11-color 'blue)                    %! baca.SegmentMaker._attach_color_literal(2):EXPLICIT_CLEF_COLOR
                        %@% \override Staff.Clef.color = ##f                                         %! baca.SegmentMaker._attach_color_literal(1):EXPLICIT_CLEF_COLOR_CANCELLATION
                            \set Staff.forceClef = ##t                                               %! baca.clef():baca.IndicatorCommand._call():baca.SegmentMaker._treat_persistent_wrapper(2):baca.SegmentMaker._set_status_tag():EXPLICIT_CLEF
                            R1 * 3/8                                                                 %! baca.SegmentMaker._call_rhythm_commands()
                        %@% ^ \baca-duration-multiplier-markup #"3" #"8"                             %! baca.SegmentMaker._label_duration_multipliers():DURATION_MULTIPLIER
                            \override Staff.Clef.color = #(x11-color 'DeepSkyBlue2)                  %! baca.SegmentMaker._attach_color_literal(2):EXPLICIT_CLEF_REDRAW_COLOR
            <BLANKLINE>
                            % [Music_Voice measure 2]                                                %! baca.SegmentMaker._comment_measure_numbers()
                            R1 * 3/8                                                                 %! baca.SegmentMaker._call_rhythm_commands()
                        %@% ^ \baca-duration-multiplier-markup #"3" #"8"                             %! baca.SegmentMaker._label_duration_multipliers():DURATION_MULTIPLIER
            <BLANKLINE>
                            <<                                                                       %! baca.SegmentMaker._make_multimeasure_rest_container(7):PHANTOM
            <BLANKLINE>
                                \context Voice = "Music_Voice"                                       %! baca.SegmentMaker._make_multimeasure_rest_container(4):PHANTOM
                                {                                                                    %! baca.SegmentMaker._make_multimeasure_rest_container(4):PHANTOM
            <BLANKLINE>
                                    % [Music_Voice measure 3]                                        %! baca.SegmentMaker._comment_measure_numbers():baca.SegmentMaker._style_phantom_measures(5):PHANTOM
                                    \abjad-invisible-music-coloring                                  %! baca.SegmentMaker._make_multimeasure_rest_container(2):PHANTOM:MULTIMEASURE_REST:INVISIBLE_MUSIC_COLORING:baca.SegmentMaker._style_phantom_measures(5)
                                %@% \abjad-invisible-music                                           %! baca.SegmentMaker._make_multimeasure_rest_container(3):PHANTOM:MULTIMEASURE_REST:INVISIBLE_MUSIC_COMMAND:baca.SegmentMaker._style_phantom_measures(5)
                                    R1 * 1/4                                                         %! baca.SegmentMaker._make_multimeasure_rest_container(1):PHANTOM:HIDDEN:MULTIMEASURE_REST
                                %@% ^ \baca-duration-multiplier-markup #"1" #"4"                     %! baca.SegmentMaker._label_duration_multipliers():DURATION_MULTIPLIER:HIDDEN:MULTIMEASURE_REST:PHANTOM:baca.SegmentMaker._style_phantom_measures(5)
            <BLANKLINE>
                                }                                                                    %! baca.SegmentMaker._make_multimeasure_rest_container(4):PHANTOM
            <BLANKLINE>
                                \context Voice = "Rest_Voice"                                        %! baca.SegmentMaker._make_multimeasure_rest_container(6):PHANTOM
                                {                                                                    %! baca.SegmentMaker._make_multimeasure_rest_container(6):PHANTOM
            <BLANKLINE>
                                    % [Rest_Voice measure 3]                                         %! baca.SegmentMaker._comment_measure_numbers():baca.SegmentMaker._style_phantom_measures(5):PHANTOM
                                    \once \override Score.TimeSignature.X-extent = ##f               %! baca.SegmentMaker._style_phantom_measures(6):PHANTOM
                                    \once \override MultiMeasureRest.transparent = ##t               %! baca.SegmentMaker._style_phantom_measures(7):PHANTOM
                                    \stopStaff                                                       %! baca.SegmentMaker._style_phantom_measures(8):PHANTOM
                                    \once \override Staff.StaffSymbol.transparent = ##t              %! baca.SegmentMaker._style_phantom_measures(8):PHANTOM
                                    \startStaff                                                      %! baca.SegmentMaker._style_phantom_measures(8):PHANTOM
                                    R1 * 1/4                                                         %! baca.SegmentMaker._make_multimeasure_rest_container(5):PHANTOM:REST_VOICE:MULTIMEASURE_REST
                                %@% ^ \baca-duration-multiplier-markup #"1" #"4"                     %! baca.SegmentMaker._label_duration_multipliers():DURATION_MULTIPLIER:MULTIMEASURE_REST:PHANTOM:REST_VOICE:baca.SegmentMaker._style_phantom_measures(5)
            <BLANKLINE>
                                }                                                                    %! baca.SegmentMaker._make_multimeasure_rest_container(6):PHANTOM
            <BLANKLINE>
                            >>                                                                       %! baca.SegmentMaker._make_multimeasure_rest_container(7):PHANTOM
            <BLANKLINE>
                        }                                                                            %! baca.SingleStaffScoreTemplate.__call__()
            <BLANKLINE>
                    }                                                                                %! baca.SingleStaffScoreTemplate.__call__()
            <BLANKLINE>
                >>                                                                                   %! baca.SingleStaffScoreTemplate.__call__()
            <BLANKLINE>
            >>                                                                                       %! baca.SingleStaffScoreTemplate.__call__()

    ..  container:: example

        Reapplied clefs color green and redraw dull green:

        >>> breaks = baca.breaks(
        ...     baca.page(
        ...         [1, 0, (11,)],
        ...         [2, 15, (11,)],
        ...         ),
        ...     )
        >>> maker = baca.SegmentMaker(
        ...     breaks=breaks,
        ...     score_template=baca.SingleStaffScoreTemplate(),
        ...     spacing=baca.minimum_duration((1, 24)),
        ...     time_signatures=[(3, 8), (3, 8)],
        ...     )

        >>> metadata, persist = {}, {}
        >>> persist['persistent_indicators'] = {}
        >>> persist['persistent_indicators']['Music_Staff'] = [
        ...     abjad.Momento(
        ...         context='Music_Voice',
        ...         prototype='abjad.Clef',
        ...         value='treble',
        ...         )
        ...     ]
        >>> metadata['segment_number'] = 1
        >>> lilypond_file = maker.run(
        ...     environment='docs',
        ...     previous_metadata=metadata,
        ...     previous_persist=persist,
        ...     )
        >>> block = abjad.Block(name='layout')
        >>> block.indent = 0
        >>> lilypond_file.items.insert(0, block)

        >>> abjad.show(lilypond_file, strict=89) # doctest: +SKIP

        ..  docs::

            >>> abjad.f(lilypond_file[abjad.Score], strict=89)
            <BLANKLINE>
            \context Score = "Score"                                                                 %! baca.SingleStaffScoreTemplate.__call__()
            <<                                                                                       %! baca.SingleStaffScoreTemplate.__call__()
            <BLANKLINE>
                \context GlobalContext = "Global_Context"                                            %! abjad.ScoreTemplate._make_global_context()
                <<                                                                                   %! abjad.ScoreTemplate._make_global_context()
            <BLANKLINE>
                    \context GlobalSkips = "Global_Skips"                                            %! abjad.ScoreTemplate._make_global_context()
                    {                                                                                %! abjad.ScoreTemplate._make_global_context()
            <BLANKLINE>
                        % [Global_Skips measure 1]                                                   %! baca.SegmentMaker._comment_measure_numbers()
                        \baca-new-spacing-section #1 #24                                             %! SPACING_COMMAND:baca.HorizontalSpacingSpecifier.__call__(1)
                        \autoPageBreaksOff                                                           %! BREAK:baca.BreakMeasureMap.__call__(1)
                        \noBreak                                                                     %! BREAK:baca.BreakMeasureMap.__call__(2)
                        \baca-lbsd #0 #'(11)                                                         %! BREAK:baca.IndicatorCommand._call()
                        \time 3/8                                                                    %! baca.SegmentMaker._make_global_skips(2):baca.SegmentMaker._set_status_tag():EXPLICIT_TIME_SIGNATURE
                        \bar ""                                                                      %! EMPTY_START_BAR:+SEGMENT:baca.SegmentMaker._make_global_skips(4)
                        \baca-time-signature-color #'blue                                            %! baca.SegmentMaker._attach_color_literal(2):EXPLICIT_TIME_SIGNATURE_COLOR
                        \pageBreak                                                                   %! BREAK:baca.IndicatorCommand._call()
                        s1 * 3/8                                                                     %! baca.SegmentMaker._make_global_skips(1)
            <BLANKLINE>
                        % [Global_Skips measure 2]                                                   %! baca.SegmentMaker._comment_measure_numbers()
                        \baca-new-spacing-section #1 #24                                             %! SPACING_COMMAND:baca.HorizontalSpacingSpecifier.__call__(1)
                        \noBreak                                                                     %! BREAK:baca.BreakMeasureMap.__call__(2)
                        \baca-lbsd #15 #'(11)                                                        %! BREAK:baca.IndicatorCommand._call()
                        \break                                                                       %! BREAK:baca.IndicatorCommand._call()
                        s1 * 3/8                                                                     %! baca.SegmentMaker._make_global_skips(1)
            <BLANKLINE>
                        % [Global_Skips measure 3]                                                   %! baca.SegmentMaker._comment_measure_numbers():baca.SegmentMaker._style_phantom_measures(1):PHANTOM
                        \baca-new-spacing-section #1 #4                                              %! SPACING_COMMAND:baca.HorizontalSpacingSpecifier.__call__(1):baca.SegmentMaker._style_phantom_measures(1):PHANTOM
                        \noBreak                                                                     %! BREAK:baca.BreakMeasureMap.__call__(2):baca.SegmentMaker._style_phantom_measures(1):PHANTOM
                        \time 1/4                                                                    %! baca.SegmentMaker._make_global_skips(3):PHANTOM:baca.SegmentMaker._set_status_tag():EXPLICIT_TIME_SIGNATURE:baca.SegmentMaker._style_phantom_measures(1)
                        \baca-time-signature-transparent                                             %! baca.SegmentMaker._style_phantom_measures(2):PHANTOM
                        s1 * 1/4                                                                     %! baca.SegmentMaker._make_global_skips(3):PHANTOM
                        \once \override Score.BarLine.transparent = ##t                              %! baca.SegmentMaker._style_phantom_measures(3):PHANTOM
                        \once \override Score.SpanBar.transparent = ##t                              %! baca.SegmentMaker._style_phantom_measures(3):PHANTOM
            <BLANKLINE>
                    }                                                                                %! abjad.ScoreTemplate._make_global_context()
            <BLANKLINE>
                >>                                                                                   %! abjad.ScoreTemplate._make_global_context()
            <BLANKLINE>
                \context MusicContext = "Music_Context"                                              %! baca.SingleStaffScoreTemplate.__call__()
                <<                                                                                   %! baca.SingleStaffScoreTemplate.__call__()
            <BLANKLINE>
                    \context Staff = "Music_Staff"                                                   %! baca.SingleStaffScoreTemplate.__call__()
                    {                                                                                %! baca.SingleStaffScoreTemplate.__call__()
            <BLANKLINE>
                        \context Voice = "Music_Voice"                                               %! baca.SingleStaffScoreTemplate.__call__()
                        {                                                                            %! baca.SingleStaffScoreTemplate.__call__()
            <BLANKLINE>
                            % [Music_Voice measure 1]                                                %! baca.SegmentMaker._comment_measure_numbers()
                            \clef "treble"                                                           %! baca.SegmentMaker._reapply_persistent_indicators(3):baca.SegmentMaker._set_status_tag():REAPPLIED_CLEF
                            \once \override Staff.Clef.color = #(x11-color 'green4)                  %! baca.SegmentMaker._attach_color_literal(2):REAPPLIED_CLEF_COLOR
                        %@% \override Staff.Clef.color = ##f                                         %! baca.SegmentMaker._attach_color_literal(1):REAPPLIED_CLEF_COLOR_CANCELLATION
                            \set Staff.forceClef = ##t                                               %! baca.SegmentMaker._reapply_persistent_indicators(3):baca.SegmentMaker._treat_persistent_wrapper(2):baca.SegmentMaker._set_status_tag():REAPPLIED_CLEF
                            R1 * 3/8                                                                 %! baca.SegmentMaker._call_rhythm_commands()
                        %@% ^ \baca-duration-multiplier-markup #"3" #"8"                             %! baca.SegmentMaker._label_duration_multipliers():DURATION_MULTIPLIER
                            \override Staff.Clef.color = #(x11-color 'OliveDrab)                     %! baca.SegmentMaker._attach_color_literal(2):REAPPLIED_CLEF_REDRAW_COLOR
            <BLANKLINE>
                            % [Music_Voice measure 2]                                                %! baca.SegmentMaker._comment_measure_numbers()
                            R1 * 3/8                                                                 %! baca.SegmentMaker._call_rhythm_commands()
                        %@% ^ \baca-duration-multiplier-markup #"3" #"8"                             %! baca.SegmentMaker._label_duration_multipliers():DURATION_MULTIPLIER
            <BLANKLINE>
                            <<                                                                       %! baca.SegmentMaker._make_multimeasure_rest_container(7):PHANTOM
            <BLANKLINE>
                                \context Voice = "Music_Voice"                                       %! baca.SegmentMaker._make_multimeasure_rest_container(4):PHANTOM
                                {                                                                    %! baca.SegmentMaker._make_multimeasure_rest_container(4):PHANTOM
            <BLANKLINE>
                                    % [Music_Voice measure 3]                                        %! baca.SegmentMaker._comment_measure_numbers():baca.SegmentMaker._style_phantom_measures(5):PHANTOM
                                    \abjad-invisible-music-coloring                                  %! baca.SegmentMaker._make_multimeasure_rest_container(2):PHANTOM:MULTIMEASURE_REST:INVISIBLE_MUSIC_COLORING:baca.SegmentMaker._style_phantom_measures(5)
                                %@% \abjad-invisible-music                                           %! baca.SegmentMaker._make_multimeasure_rest_container(3):PHANTOM:MULTIMEASURE_REST:INVISIBLE_MUSIC_COMMAND:baca.SegmentMaker._style_phantom_measures(5)
                                    R1 * 1/4                                                         %! baca.SegmentMaker._make_multimeasure_rest_container(1):PHANTOM:HIDDEN:MULTIMEASURE_REST
                                %@% ^ \baca-duration-multiplier-markup #"1" #"4"                     %! baca.SegmentMaker._label_duration_multipliers():DURATION_MULTIPLIER:HIDDEN:MULTIMEASURE_REST:PHANTOM:baca.SegmentMaker._style_phantom_measures(5)
            <BLANKLINE>
                                }                                                                    %! baca.SegmentMaker._make_multimeasure_rest_container(4):PHANTOM
            <BLANKLINE>
                                \context Voice = "Rest_Voice"                                        %! baca.SegmentMaker._make_multimeasure_rest_container(6):PHANTOM
                                {                                                                    %! baca.SegmentMaker._make_multimeasure_rest_container(6):PHANTOM
            <BLANKLINE>
                                    % [Rest_Voice measure 3]                                         %! baca.SegmentMaker._comment_measure_numbers():baca.SegmentMaker._style_phantom_measures(5):PHANTOM
                                    \once \override Score.TimeSignature.X-extent = ##f               %! baca.SegmentMaker._style_phantom_measures(6):PHANTOM
                                    \once \override MultiMeasureRest.transparent = ##t               %! baca.SegmentMaker._style_phantom_measures(7):PHANTOM
                                    \stopStaff                                                       %! baca.SegmentMaker._style_phantom_measures(8):PHANTOM
                                    \once \override Staff.StaffSymbol.transparent = ##t              %! baca.SegmentMaker._style_phantom_measures(8):PHANTOM
                                    \startStaff                                                      %! baca.SegmentMaker._style_phantom_measures(8):PHANTOM
                                    R1 * 1/4                                                         %! baca.SegmentMaker._make_multimeasure_rest_container(5):PHANTOM:REST_VOICE:MULTIMEASURE_REST
                                %@% ^ \baca-duration-multiplier-markup #"1" #"4"                     %! baca.SegmentMaker._label_duration_multipliers():DURATION_MULTIPLIER:MULTIMEASURE_REST:PHANTOM:REST_VOICE:baca.SegmentMaker._style_phantom_measures(5)
            <BLANKLINE>
                                }                                                                    %! baca.SegmentMaker._make_multimeasure_rest_container(6):PHANTOM
            <BLANKLINE>
                            >>                                                                       %! baca.SegmentMaker._make_multimeasure_rest_container(7):PHANTOM
            <BLANKLINE>
                        }                                                                            %! baca.SingleStaffScoreTemplate.__call__()
            <BLANKLINE>
                    }                                                                                %! baca.SingleStaffScoreTemplate.__call__()
            <BLANKLINE>
                >>                                                                                   %! baca.SingleStaffScoreTemplate.__call__()
            <BLANKLINE>
            >>                                                                                       %! baca.SingleStaffScoreTemplate.__call__()

    ..  container:: example

        Redundant clefs color pink and redraw dull pink:

        >>> breaks = baca.breaks(
        ...     baca.page(
        ...         [1, 0, (11,)],
        ...         [3, 15, (11,)],
        ...         ),
        ...     )
        >>> maker = baca.SegmentMaker(
        ...     breaks=breaks,
        ...     score_template=baca.SingleStaffScoreTemplate(),
        ...     spacing=baca.minimum_duration((1, 24)),
        ...     time_signatures=[(3, 8), (3, 8), (3, 8)],
        ...     )
        >>> maker(
        ...     'Music_Voice',
        ...     baca.clef('treble', selector=baca.leaf(0)),
        ...     baca.clef('treble', selector=baca.leaf(1)),
        ...     )
        >>> lilypond_file = maker.run(environment='docs')
        >>> block = abjad.Block(name='layout')
        >>> block.indent = 0
        >>> lilypond_file.items.insert(0, block)

        >>> abjad.show(lilypond_file, strict=89) # doctest: +SKIP

        ..  docs::

            >>> abjad.f(lilypond_file[abjad.Score], strict=89)
            <BLANKLINE>
            \context Score = "Score"                                                                 %! baca.SingleStaffScoreTemplate.__call__()
            <<                                                                                       %! baca.SingleStaffScoreTemplate.__call__()
            <BLANKLINE>
                \context GlobalContext = "Global_Context"                                            %! abjad.ScoreTemplate._make_global_context()
                <<                                                                                   %! abjad.ScoreTemplate._make_global_context()
            <BLANKLINE>
                    \context GlobalSkips = "Global_Skips"                                            %! abjad.ScoreTemplate._make_global_context()
                    {                                                                                %! abjad.ScoreTemplate._make_global_context()
            <BLANKLINE>
                        % [Global_Skips measure 1]                                                   %! baca.SegmentMaker._comment_measure_numbers()
                        \baca-new-spacing-section #1 #24                                             %! SPACING_COMMAND:baca.HorizontalSpacingSpecifier.__call__(1)
                        \autoPageBreaksOff                                                           %! BREAK:baca.BreakMeasureMap.__call__(1)
                        \noBreak                                                                     %! BREAK:baca.BreakMeasureMap.__call__(2)
                        \baca-lbsd #0 #'(11)                                                         %! BREAK:baca.IndicatorCommand._call()
                        \time 3/8                                                                    %! baca.SegmentMaker._make_global_skips(2):baca.SegmentMaker._set_status_tag():EXPLICIT_TIME_SIGNATURE
                        \baca-time-signature-color #'blue                                            %! baca.SegmentMaker._attach_color_literal(2):EXPLICIT_TIME_SIGNATURE_COLOR
                        \pageBreak                                                                   %! BREAK:baca.IndicatorCommand._call()
                        s1 * 3/8                                                                     %! baca.SegmentMaker._make_global_skips(1)
            <BLANKLINE>
                        % [Global_Skips measure 2]                                                   %! baca.SegmentMaker._comment_measure_numbers()
                        \baca-new-spacing-section #1 #24                                             %! SPACING_COMMAND:baca.HorizontalSpacingSpecifier.__call__(1)
                        \noBreak                                                                     %! BREAK:baca.BreakMeasureMap.__call__(2)
                        s1 * 3/8                                                                     %! baca.SegmentMaker._make_global_skips(1)
            <BLANKLINE>
                        % [Global_Skips measure 3]                                                   %! baca.SegmentMaker._comment_measure_numbers()
                        \baca-new-spacing-section #1 #24                                             %! SPACING_COMMAND:baca.HorizontalSpacingSpecifier.__call__(1)
                        \noBreak                                                                     %! BREAK:baca.BreakMeasureMap.__call__(2)
                        \baca-lbsd #15 #'(11)                                                        %! BREAK:baca.IndicatorCommand._call()
                        \break                                                                       %! BREAK:baca.IndicatorCommand._call()
                        s1 * 3/8                                                                     %! baca.SegmentMaker._make_global_skips(1)
            <BLANKLINE>
                        % [Global_Skips measure 4]                                                   %! baca.SegmentMaker._comment_measure_numbers():baca.SegmentMaker._style_phantom_measures(1):PHANTOM
                        \baca-new-spacing-section #1 #4                                              %! SPACING_COMMAND:baca.HorizontalSpacingSpecifier.__call__(1):baca.SegmentMaker._style_phantom_measures(1):PHANTOM
                        \noBreak                                                                     %! BREAK:baca.BreakMeasureMap.__call__(2):baca.SegmentMaker._style_phantom_measures(1):PHANTOM
                        \time 1/4                                                                    %! baca.SegmentMaker._make_global_skips(3):PHANTOM:baca.SegmentMaker._set_status_tag():EXPLICIT_TIME_SIGNATURE:baca.SegmentMaker._style_phantom_measures(1)
                        \baca-time-signature-transparent                                             %! baca.SegmentMaker._style_phantom_measures(2):PHANTOM
                        s1 * 1/4                                                                     %! baca.SegmentMaker._make_global_skips(3):PHANTOM
                        \once \override Score.BarLine.transparent = ##t                              %! baca.SegmentMaker._style_phantom_measures(3):PHANTOM
                        \once \override Score.SpanBar.transparent = ##t                              %! baca.SegmentMaker._style_phantom_measures(3):PHANTOM
            <BLANKLINE>
                    }                                                                                %! abjad.ScoreTemplate._make_global_context()
            <BLANKLINE>
                >>                                                                                   %! abjad.ScoreTemplate._make_global_context()
            <BLANKLINE>
                \context MusicContext = "Music_Context"                                              %! baca.SingleStaffScoreTemplate.__call__()
                <<                                                                                   %! baca.SingleStaffScoreTemplate.__call__()
            <BLANKLINE>
                    \context Staff = "Music_Staff"                                                   %! baca.SingleStaffScoreTemplate.__call__()
                    {                                                                                %! baca.SingleStaffScoreTemplate.__call__()
            <BLANKLINE>
                        \context Voice = "Music_Voice"                                               %! baca.SingleStaffScoreTemplate.__call__()
                        {                                                                            %! baca.SingleStaffScoreTemplate.__call__()
            <BLANKLINE>
                            % [Music_Voice measure 1]                                                %! baca.SegmentMaker._comment_measure_numbers()
                            \clef "treble"                                                           %! baca.clef():baca.IndicatorCommand._call():baca.SegmentMaker._set_status_tag():EXPLICIT_CLEF
                            \once \override Staff.Clef.color = #(x11-color 'blue)                    %! baca.SegmentMaker._attach_color_literal(2):EXPLICIT_CLEF_COLOR
                        %@% \override Staff.Clef.color = ##f                                         %! baca.SegmentMaker._attach_color_literal(1):EXPLICIT_CLEF_COLOR_CANCELLATION
                            \set Staff.forceClef = ##t                                               %! baca.clef():baca.IndicatorCommand._call():baca.SegmentMaker._treat_persistent_wrapper(2):baca.SegmentMaker._set_status_tag():EXPLICIT_CLEF
                            R1 * 3/8                                                                 %! baca.SegmentMaker._call_rhythm_commands()
                        %@% ^ \baca-duration-multiplier-markup #"3" #"8"                             %! baca.SegmentMaker._label_duration_multipliers():DURATION_MULTIPLIER
                            \override Staff.Clef.color = #(x11-color 'DeepSkyBlue2)                  %! baca.SegmentMaker._attach_color_literal(2):EXPLICIT_CLEF_REDRAW_COLOR
            <BLANKLINE>
                            % [Music_Voice measure 2]                                                %! baca.SegmentMaker._comment_measure_numbers()
                            \clef "treble"                                                           %! baca.clef():baca.IndicatorCommand._call():baca.SegmentMaker._set_status_tag():REDUNDANT_CLEF
                            \once \override Staff.Clef.color = #(x11-color 'DeepPink1)               %! baca.SegmentMaker._attach_color_literal(2):REDUNDANT_CLEF_COLOR
                        %@% \override Staff.Clef.color = ##f                                         %! baca.SegmentMaker._attach_color_literal(1):REDUNDANT_CLEF_COLOR_CANCELLATION
                            \set Staff.forceClef = ##t                                               %! baca.clef():baca.IndicatorCommand._call():baca.SegmentMaker._treat_persistent_wrapper(2):baca.SegmentMaker._set_status_tag():REDUNDANT_CLEF
                            R1 * 3/8                                                                 %! baca.SegmentMaker._call_rhythm_commands()
                        %@% ^ \baca-duration-multiplier-markup #"3" #"8"                             %! baca.SegmentMaker._label_duration_multipliers():DURATION_MULTIPLIER
                            \override Staff.Clef.color = #(x11-color 'DeepPink4)                     %! baca.SegmentMaker._attach_color_literal(2):REDUNDANT_CLEF_REDRAW_COLOR
            <BLANKLINE>
                            % [Music_Voice measure 3]                                                %! baca.SegmentMaker._comment_measure_numbers()
                            R1 * 3/8                                                                 %! baca.SegmentMaker._call_rhythm_commands()
                        %@% ^ \baca-duration-multiplier-markup #"3" #"8"                             %! baca.SegmentMaker._label_duration_multipliers():DURATION_MULTIPLIER
            <BLANKLINE>
                            <<                                                                       %! baca.SegmentMaker._make_multimeasure_rest_container(7):PHANTOM
            <BLANKLINE>
                                \context Voice = "Music_Voice"                                       %! baca.SegmentMaker._make_multimeasure_rest_container(4):PHANTOM
                                {                                                                    %! baca.SegmentMaker._make_multimeasure_rest_container(4):PHANTOM
            <BLANKLINE>
                                    % [Music_Voice measure 4]                                        %! baca.SegmentMaker._comment_measure_numbers():baca.SegmentMaker._style_phantom_measures(5):PHANTOM
                                    \abjad-invisible-music-coloring                                  %! baca.SegmentMaker._make_multimeasure_rest_container(2):PHANTOM:MULTIMEASURE_REST:INVISIBLE_MUSIC_COLORING:baca.SegmentMaker._style_phantom_measures(5)
                                %@% \abjad-invisible-music                                           %! baca.SegmentMaker._make_multimeasure_rest_container(3):PHANTOM:MULTIMEASURE_REST:INVISIBLE_MUSIC_COMMAND:baca.SegmentMaker._style_phantom_measures(5)
                                    R1 * 1/4                                                         %! baca.SegmentMaker._make_multimeasure_rest_container(1):PHANTOM:HIDDEN:MULTIMEASURE_REST
                                %@% ^ \baca-duration-multiplier-markup #"1" #"4"                     %! baca.SegmentMaker._label_duration_multipliers():DURATION_MULTIPLIER:HIDDEN:MULTIMEASURE_REST:PHANTOM:baca.SegmentMaker._style_phantom_measures(5)
            <BLANKLINE>
                                }                                                                    %! baca.SegmentMaker._make_multimeasure_rest_container(4):PHANTOM
            <BLANKLINE>
                                \context Voice = "Rest_Voice"                                        %! baca.SegmentMaker._make_multimeasure_rest_container(6):PHANTOM
                                {                                                                    %! baca.SegmentMaker._make_multimeasure_rest_container(6):PHANTOM
            <BLANKLINE>
                                    % [Rest_Voice measure 4]                                         %! baca.SegmentMaker._comment_measure_numbers():baca.SegmentMaker._style_phantom_measures(5):PHANTOM
                                    \once \override Score.TimeSignature.X-extent = ##f               %! baca.SegmentMaker._style_phantom_measures(6):PHANTOM
                                    \once \override MultiMeasureRest.transparent = ##t               %! baca.SegmentMaker._style_phantom_measures(7):PHANTOM
                                    \stopStaff                                                       %! baca.SegmentMaker._style_phantom_measures(8):PHANTOM
                                    \once \override Staff.StaffSymbol.transparent = ##t              %! baca.SegmentMaker._style_phantom_measures(8):PHANTOM
                                    \startStaff                                                      %! baca.SegmentMaker._style_phantom_measures(8):PHANTOM
                                    R1 * 1/4                                                         %! baca.SegmentMaker._make_multimeasure_rest_container(5):PHANTOM:REST_VOICE:MULTIMEASURE_REST
                                %@% ^ \baca-duration-multiplier-markup #"1" #"4"                     %! baca.SegmentMaker._label_duration_multipliers():DURATION_MULTIPLIER:MULTIMEASURE_REST:PHANTOM:REST_VOICE:baca.SegmentMaker._style_phantom_measures(5)
            <BLANKLINE>
                                }                                                                    %! baca.SegmentMaker._make_multimeasure_rest_container(6):PHANTOM
            <BLANKLINE>
                            >>                                                                       %! baca.SegmentMaker._make_multimeasure_rest_container(7):PHANTOM
            <BLANKLINE>
                        }                                                                            %! baca.SingleStaffScoreTemplate.__call__()
            <BLANKLINE>
                    }                                                                                %! baca.SingleStaffScoreTemplate.__call__()
            <BLANKLINE>
                >>                                                                                   %! baca.SingleStaffScoreTemplate.__call__()
            <BLANKLINE>
            >>                                                                                       %! baca.SingleStaffScoreTemplate.__call__()

        Even at the beginning of a segment:

        >>> breaks = baca.breaks(
        ...     baca.page(
        ...         [1, 0, (11,)],
        ...         [2, 15, (11,)],
        ...         ),
        ...     )
        >>> maker = baca.SegmentMaker(
        ...     breaks=breaks,
        ...     score_template=baca.SingleStaffScoreTemplate(),
        ...     spacing=baca.minimum_duration((1, 24)),
        ...     time_signatures=[(3, 8), (3, 8)],
        ...     )
        >>> maker(
        ...     'Music_Voice',
        ...     baca.clef('treble'),
        ...     )

        >>> metadata, persist = {}, {}
        >>> persist['persistent_indicators'] = {}
        >>> persist['persistent_indicators']['Music_Staff'] = [
        ...     abjad.Momento(
        ...         context='Music_Voice',
        ...         prototype='abjad.Clef',
        ...         value='treble',
        ...         )
        ...     ]
        >>> metadata['segment_number'] = 1
        >>> lilypond_file = maker.run(
        ...     environment='docs',
        ...     previous_metadata=metadata,
        ...     previous_persist=persist,
        ...     )
        >>> block = abjad.Block(name='layout')
        >>> block.indent = 0
        >>> lilypond_file.items.insert(0, block)

        >>> abjad.show(lilypond_file, strict=89) # doctest: +SKIP

        ..  docs::

            >>> abjad.f(lilypond_file[abjad.Score], strict=89)
            <BLANKLINE>
            \context Score = "Score"                                                                 %! baca.SingleStaffScoreTemplate.__call__()
            <<                                                                                       %! baca.SingleStaffScoreTemplate.__call__()
            <BLANKLINE>
                \context GlobalContext = "Global_Context"                                            %! abjad.ScoreTemplate._make_global_context()
                <<                                                                                   %! abjad.ScoreTemplate._make_global_context()
            <BLANKLINE>
                    \context GlobalSkips = "Global_Skips"                                            %! abjad.ScoreTemplate._make_global_context()
                    {                                                                                %! abjad.ScoreTemplate._make_global_context()
            <BLANKLINE>
                        % [Global_Skips measure 1]                                                   %! baca.SegmentMaker._comment_measure_numbers()
                        \baca-new-spacing-section #1 #24                                             %! SPACING_COMMAND:baca.HorizontalSpacingSpecifier.__call__(1)
                        \autoPageBreaksOff                                                           %! BREAK:baca.BreakMeasureMap.__call__(1)
                        \noBreak                                                                     %! BREAK:baca.BreakMeasureMap.__call__(2)
                        \baca-lbsd #0 #'(11)                                                         %! BREAK:baca.IndicatorCommand._call()
                        \time 3/8                                                                    %! baca.SegmentMaker._make_global_skips(2):baca.SegmentMaker._set_status_tag():EXPLICIT_TIME_SIGNATURE
                        \bar ""                                                                      %! EMPTY_START_BAR:+SEGMENT:baca.SegmentMaker._make_global_skips(4)
                        \baca-time-signature-color #'blue                                            %! baca.SegmentMaker._attach_color_literal(2):EXPLICIT_TIME_SIGNATURE_COLOR
                        \pageBreak                                                                   %! BREAK:baca.IndicatorCommand._call()
                        s1 * 3/8                                                                     %! baca.SegmentMaker._make_global_skips(1)
            <BLANKLINE>
                        % [Global_Skips measure 2]                                                   %! baca.SegmentMaker._comment_measure_numbers()
                        \baca-new-spacing-section #1 #24                                             %! SPACING_COMMAND:baca.HorizontalSpacingSpecifier.__call__(1)
                        \noBreak                                                                     %! BREAK:baca.BreakMeasureMap.__call__(2)
                        \baca-lbsd #15 #'(11)                                                        %! BREAK:baca.IndicatorCommand._call()
                        \break                                                                       %! BREAK:baca.IndicatorCommand._call()
                        s1 * 3/8                                                                     %! baca.SegmentMaker._make_global_skips(1)
            <BLANKLINE>
                        % [Global_Skips measure 3]                                                   %! baca.SegmentMaker._comment_measure_numbers():baca.SegmentMaker._style_phantom_measures(1):PHANTOM
                        \baca-new-spacing-section #1 #4                                              %! SPACING_COMMAND:baca.HorizontalSpacingSpecifier.__call__(1):baca.SegmentMaker._style_phantom_measures(1):PHANTOM
                        \noBreak                                                                     %! BREAK:baca.BreakMeasureMap.__call__(2):baca.SegmentMaker._style_phantom_measures(1):PHANTOM
                        \time 1/4                                                                    %! baca.SegmentMaker._make_global_skips(3):PHANTOM:baca.SegmentMaker._set_status_tag():EXPLICIT_TIME_SIGNATURE:baca.SegmentMaker._style_phantom_measures(1)
                        \baca-time-signature-transparent                                             %! baca.SegmentMaker._style_phantom_measures(2):PHANTOM
                        s1 * 1/4                                                                     %! baca.SegmentMaker._make_global_skips(3):PHANTOM
                        \once \override Score.BarLine.transparent = ##t                              %! baca.SegmentMaker._style_phantom_measures(3):PHANTOM
                        \once \override Score.SpanBar.transparent = ##t                              %! baca.SegmentMaker._style_phantom_measures(3):PHANTOM
            <BLANKLINE>
                    }                                                                                %! abjad.ScoreTemplate._make_global_context()
            <BLANKLINE>
                >>                                                                                   %! abjad.ScoreTemplate._make_global_context()
            <BLANKLINE>
                \context MusicContext = "Music_Context"                                              %! baca.SingleStaffScoreTemplate.__call__()
                <<                                                                                   %! baca.SingleStaffScoreTemplate.__call__()
            <BLANKLINE>
                    \context Staff = "Music_Staff"                                                   %! baca.SingleStaffScoreTemplate.__call__()
                    {                                                                                %! baca.SingleStaffScoreTemplate.__call__()
            <BLANKLINE>
                        \context Voice = "Music_Voice"                                               %! baca.SingleStaffScoreTemplate.__call__()
                        {                                                                            %! baca.SingleStaffScoreTemplate.__call__()
            <BLANKLINE>
                            % [Music_Voice measure 1]                                                %! baca.SegmentMaker._comment_measure_numbers()
                            \clef "treble"                                                           %! baca.clef():baca.IndicatorCommand._call():baca.SegmentMaker._set_status_tag():REDUNDANT_CLEF
                            \once \override Staff.Clef.color = #(x11-color 'DeepPink1)               %! baca.SegmentMaker._attach_color_literal(2):REDUNDANT_CLEF_COLOR
                        %@% \override Staff.Clef.color = ##f                                         %! baca.SegmentMaker._attach_color_literal(1):REDUNDANT_CLEF_COLOR_CANCELLATION
                            \set Staff.forceClef = ##t                                               %! baca.clef():baca.IndicatorCommand._call():baca.SegmentMaker._treat_persistent_wrapper(2):baca.SegmentMaker._set_status_tag():REDUNDANT_CLEF
                            R1 * 3/8                                                                 %! baca.SegmentMaker._call_rhythm_commands()
                        %@% ^ \baca-duration-multiplier-markup #"3" #"8"                             %! baca.SegmentMaker._label_duration_multipliers():DURATION_MULTIPLIER
                            \override Staff.Clef.color = #(x11-color 'DeepPink4)                     %! baca.SegmentMaker._attach_color_literal(2):REDUNDANT_CLEF_REDRAW_COLOR
            <BLANKLINE>
                            % [Music_Voice measure 2]                                                %! baca.SegmentMaker._comment_measure_numbers()
                            R1 * 3/8                                                                 %! baca.SegmentMaker._call_rhythm_commands()
                        %@% ^ \baca-duration-multiplier-markup #"3" #"8"                             %! baca.SegmentMaker._label_duration_multipliers():DURATION_MULTIPLIER
            <BLANKLINE>
                            <<                                                                       %! baca.SegmentMaker._make_multimeasure_rest_container(7):PHANTOM
            <BLANKLINE>
                                \context Voice = "Music_Voice"                                       %! baca.SegmentMaker._make_multimeasure_rest_container(4):PHANTOM
                                {                                                                    %! baca.SegmentMaker._make_multimeasure_rest_container(4):PHANTOM
            <BLANKLINE>
                                    % [Music_Voice measure 3]                                        %! baca.SegmentMaker._comment_measure_numbers():baca.SegmentMaker._style_phantom_measures(5):PHANTOM
                                    \abjad-invisible-music-coloring                                  %! baca.SegmentMaker._make_multimeasure_rest_container(2):PHANTOM:MULTIMEASURE_REST:INVISIBLE_MUSIC_COLORING:baca.SegmentMaker._style_phantom_measures(5)
                                %@% \abjad-invisible-music                                           %! baca.SegmentMaker._make_multimeasure_rest_container(3):PHANTOM:MULTIMEASURE_REST:INVISIBLE_MUSIC_COMMAND:baca.SegmentMaker._style_phantom_measures(5)
                                    R1 * 1/4                                                         %! baca.SegmentMaker._make_multimeasure_rest_container(1):PHANTOM:HIDDEN:MULTIMEASURE_REST
                                %@% ^ \baca-duration-multiplier-markup #"1" #"4"                     %! baca.SegmentMaker._label_duration_multipliers():DURATION_MULTIPLIER:HIDDEN:MULTIMEASURE_REST:PHANTOM:baca.SegmentMaker._style_phantom_measures(5)
            <BLANKLINE>
                                }                                                                    %! baca.SegmentMaker._make_multimeasure_rest_container(4):PHANTOM
            <BLANKLINE>
                                \context Voice = "Rest_Voice"                                        %! baca.SegmentMaker._make_multimeasure_rest_container(6):PHANTOM
                                {                                                                    %! baca.SegmentMaker._make_multimeasure_rest_container(6):PHANTOM
            <BLANKLINE>
                                    % [Rest_Voice measure 3]                                         %! baca.SegmentMaker._comment_measure_numbers():baca.SegmentMaker._style_phantom_measures(5):PHANTOM
                                    \once \override Score.TimeSignature.X-extent = ##f               %! baca.SegmentMaker._style_phantom_measures(6):PHANTOM
                                    \once \override MultiMeasureRest.transparent = ##t               %! baca.SegmentMaker._style_phantom_measures(7):PHANTOM
                                    \stopStaff                                                       %! baca.SegmentMaker._style_phantom_measures(8):PHANTOM
                                    \once \override Staff.StaffSymbol.transparent = ##t              %! baca.SegmentMaker._style_phantom_measures(8):PHANTOM
                                    \startStaff                                                      %! baca.SegmentMaker._style_phantom_measures(8):PHANTOM
                                    R1 * 1/4                                                         %! baca.SegmentMaker._make_multimeasure_rest_container(5):PHANTOM:REST_VOICE:MULTIMEASURE_REST
                                %@% ^ \baca-duration-multiplier-markup #"1" #"4"                     %! baca.SegmentMaker._label_duration_multipliers():DURATION_MULTIPLIER:MULTIMEASURE_REST:PHANTOM:REST_VOICE:baca.SegmentMaker._style_phantom_measures(5)
            <BLANKLINE>
                                }                                                                    %! baca.SegmentMaker._make_multimeasure_rest_container(6):PHANTOM
            <BLANKLINE>
                            >>                                                                       %! baca.SegmentMaker._make_multimeasure_rest_container(7):PHANTOM
            <BLANKLINE>
                        }                                                                            %! baca.SingleStaffScoreTemplate.__call__()
            <BLANKLINE>
                    }                                                                                %! baca.SingleStaffScoreTemplate.__call__()
            <BLANKLINE>
                >>                                                                                   %! baca.SingleStaffScoreTemplate.__call__()
            <BLANKLINE>
            >>                                                                                       %! baca.SingleStaffScoreTemplate.__call__()

..  container:: example

    Dynamics.

    ..  container:: example

        Explicit dynamics color blue:

        >>> maker = baca.SegmentMaker(
        ...     deactivate=[abjad.tags.NOT_YET_PITCHED_COLORING],
        ...     score_template=baca.SingleStaffScoreTemplate(),
        ...     spacing=baca.minimum_duration((1, 24)),
        ...     time_signatures=[(3, 8), (3, 8)],
        ...     )
        >>> maker(
        ...     'Music_Voice',
        ...     baca.dynamic('f'),
        ...     baca.make_notes(),
        ...     )

        >>> lilypond_file = maker.run(environment='docs')
        >>> block = abjad.Block(name='layout')
        >>> block.indent = 0
        >>> lilypond_file.items.insert(0, block)
        >>> abjad.show(lilypond_file, strict=89) # doctest: +SKIP

        ..  docs::

            >>> abjad.f(lilypond_file[abjad.Score], strict=89)
            <BLANKLINE>
            \context Score = "Score"                                                                 %! baca.SingleStaffScoreTemplate.__call__()
            <<                                                                                       %! baca.SingleStaffScoreTemplate.__call__()
            <BLANKLINE>
                \context GlobalContext = "Global_Context"                                            %! abjad.ScoreTemplate._make_global_context()
                <<                                                                                   %! abjad.ScoreTemplate._make_global_context()
            <BLANKLINE>
                    \context GlobalSkips = "Global_Skips"                                            %! abjad.ScoreTemplate._make_global_context()
                    {                                                                                %! abjad.ScoreTemplate._make_global_context()
            <BLANKLINE>
                        % [Global_Skips measure 1]                                                   %! baca.SegmentMaker._comment_measure_numbers()
                        \baca-new-spacing-section #1 #24                                             %! SPACING_COMMAND:baca.HorizontalSpacingSpecifier.__call__(1)
                        \time 3/8                                                                    %! baca.SegmentMaker._make_global_skips(2):baca.SegmentMaker._set_status_tag():EXPLICIT_TIME_SIGNATURE
                        \baca-time-signature-color #'blue                                            %! baca.SegmentMaker._attach_color_literal(2):EXPLICIT_TIME_SIGNATURE_COLOR
                        s1 * 3/8                                                                     %! baca.SegmentMaker._make_global_skips(1)
            <BLANKLINE>
                        % [Global_Skips measure 2]                                                   %! baca.SegmentMaker._comment_measure_numbers()
                        \baca-new-spacing-section #1 #24                                             %! SPACING_COMMAND:baca.HorizontalSpacingSpecifier.__call__(1)
                        s1 * 3/8                                                                     %! baca.SegmentMaker._make_global_skips(1)
            <BLANKLINE>
                        % [Global_Skips measure 3]                                                   %! baca.SegmentMaker._comment_measure_numbers():baca.SegmentMaker._style_phantom_measures(1):PHANTOM
                        \baca-new-spacing-section #1 #4                                              %! SPACING_COMMAND:baca.HorizontalSpacingSpecifier.__call__(1):baca.SegmentMaker._style_phantom_measures(1):PHANTOM
                        \time 1/4                                                                    %! baca.SegmentMaker._make_global_skips(3):PHANTOM:baca.SegmentMaker._set_status_tag():EXPLICIT_TIME_SIGNATURE:baca.SegmentMaker._style_phantom_measures(1)
                        \baca-time-signature-transparent                                             %! baca.SegmentMaker._style_phantom_measures(2):PHANTOM
                        s1 * 1/4                                                                     %! baca.SegmentMaker._make_global_skips(3):PHANTOM
                        \once \override Score.BarLine.transparent = ##t                              %! baca.SegmentMaker._style_phantom_measures(3):PHANTOM
                        \once \override Score.SpanBar.transparent = ##t                              %! baca.SegmentMaker._style_phantom_measures(3):PHANTOM
            <BLANKLINE>
                    }                                                                                %! abjad.ScoreTemplate._make_global_context()
            <BLANKLINE>
                >>                                                                                   %! abjad.ScoreTemplate._make_global_context()
            <BLANKLINE>
                \context MusicContext = "Music_Context"                                              %! baca.SingleStaffScoreTemplate.__call__()
                <<                                                                                   %! baca.SingleStaffScoreTemplate.__call__()
            <BLANKLINE>
                    \context Staff = "Music_Staff"                                                   %! baca.SingleStaffScoreTemplate.__call__()
                    {                                                                                %! baca.SingleStaffScoreTemplate.__call__()
            <BLANKLINE>
                        \context Voice = "Music_Voice"                                               %! baca.SingleStaffScoreTemplate.__call__()
                        {                                                                            %! baca.SingleStaffScoreTemplate.__call__()
            <BLANKLINE>
                            % [Music_Voice measure 1]                                                %! baca.SegmentMaker._comment_measure_numbers()
                        %@% \baca-not-yet-pitched-coloring                                           %! baca.SegmentMaker._color_not_yet_pitched():NOT_YET_PITCHED_COLORING
                            b'4.                                                                     %! baca.make_notes()
                            - \tweak color #(x11-color 'blue)                                        %! EXPLICIT_DYNAMIC_COLOR:_treat_persistent_wrapper(1)
                            \f                                                                       %! baca.dynamic():baca.IndicatorCommand._call():baca.SegmentMaker._set_status_tag():EXPLICIT_DYNAMIC
            <BLANKLINE>
                            % [Music_Voice measure 2]                                                %! baca.SegmentMaker._comment_measure_numbers()
                        %@% \baca-not-yet-pitched-coloring                                           %! baca.SegmentMaker._color_not_yet_pitched():NOT_YET_PITCHED_COLORING
                            b'4.                                                                     %! baca.make_notes()
            <BLANKLINE>
                            <<                                                                       %! baca.SegmentMaker._make_multimeasure_rest_container(7):PHANTOM
            <BLANKLINE>
                                \context Voice = "Music_Voice"                                       %! baca.SegmentMaker._make_multimeasure_rest_container(4):PHANTOM
                                {                                                                    %! baca.SegmentMaker._make_multimeasure_rest_container(4):PHANTOM
            <BLANKLINE>
                                    % [Music_Voice measure 3]                                        %! baca.SegmentMaker._comment_measure_numbers():baca.SegmentMaker._style_phantom_measures(5):PHANTOM
                                    \abjad-invisible-music-coloring                                  %! baca.SegmentMaker._make_multimeasure_rest_container(2):PHANTOM:NOTE:INVISIBLE_MUSIC_COLORING:baca.SegmentMaker._style_phantom_measures(5)
                                %@% \abjad-invisible-music                                           %! baca.SegmentMaker._make_multimeasure_rest_container(3):PHANTOM:NOTE:INVISIBLE_MUSIC_COMMAND:baca.SegmentMaker._style_phantom_measures(5)
                                %@% \baca-not-yet-pitched-coloring                                   %! baca.SegmentMaker._color_not_yet_pitched():NOT_YET_PITCHED_COLORING:HIDDEN:NOTE:baca.SegmentMaker._style_phantom_measures(5):PHANTOM
                                    b'1 * 1/4                                                        %! baca.SegmentMaker._make_multimeasure_rest_container(1):PHANTOM:HIDDEN:NOTE
                                %@% ^ \baca-duration-multiplier-markup #"1" #"4"                     %! baca.SegmentMaker._label_duration_multipliers():DURATION_MULTIPLIER:HIDDEN:NOTE:PHANTOM:baca.SegmentMaker._style_phantom_measures(5)
            <BLANKLINE>
                                }                                                                    %! baca.SegmentMaker._make_multimeasure_rest_container(4):PHANTOM
            <BLANKLINE>
                                \context Voice = "Rest_Voice"                                        %! baca.SegmentMaker._make_multimeasure_rest_container(6):PHANTOM
                                {                                                                    %! baca.SegmentMaker._make_multimeasure_rest_container(6):PHANTOM
            <BLANKLINE>
                                    % [Rest_Voice measure 3]                                         %! baca.SegmentMaker._comment_measure_numbers():baca.SegmentMaker._style_phantom_measures(5):PHANTOM
                                    \once \override Score.TimeSignature.X-extent = ##f               %! baca.SegmentMaker._style_phantom_measures(6):PHANTOM
                                    \once \override MultiMeasureRest.transparent = ##t               %! baca.SegmentMaker._style_phantom_measures(7):PHANTOM
                                    \stopStaff                                                       %! baca.SegmentMaker._style_phantom_measures(8):PHANTOM
                                    \once \override Staff.StaffSymbol.transparent = ##t              %! baca.SegmentMaker._style_phantom_measures(8):PHANTOM
                                    \startStaff                                                      %! baca.SegmentMaker._style_phantom_measures(8):PHANTOM
                                    R1 * 1/4                                                         %! baca.SegmentMaker._make_multimeasure_rest_container(5):PHANTOM:REST_VOICE:MULTIMEASURE_REST
                                %@% ^ \baca-duration-multiplier-markup #"1" #"4"                     %! baca.SegmentMaker._label_duration_multipliers():DURATION_MULTIPLIER:MULTIMEASURE_REST:PHANTOM:REST_VOICE:baca.SegmentMaker._style_phantom_measures(5)
            <BLANKLINE>
                                }                                                                    %! baca.SegmentMaker._make_multimeasure_rest_container(6):PHANTOM
            <BLANKLINE>
                            >>                                                                       %! baca.SegmentMaker._make_multimeasure_rest_container(7):PHANTOM
            <BLANKLINE>
                        }                                                                            %! baca.SingleStaffScoreTemplate.__call__()
            <BLANKLINE>
                    }                                                                                %! baca.SingleStaffScoreTemplate.__call__()
            <BLANKLINE>
                >>                                                                                   %! baca.SingleStaffScoreTemplate.__call__()
            <BLANKLINE>
            >>                                                                                       %! baca.SingleStaffScoreTemplate.__call__()

        Even after a previous dynamic:

        >>> maker = baca.SegmentMaker(
        ...     deactivate=[abjad.tags.NOT_YET_PITCHED_COLORING],
        ...     score_template=baca.SingleStaffScoreTemplate(),
        ...     spacing=baca.minimum_duration((1, 24)),
        ...     time_signatures=[(3, 8), (3, 8)],
        ...     )
        >>> maker(
        ...     'Music_Voice',
        ...     baca.make_notes(),
        ...     baca.dynamic('p'),
        ...     )

        >>> metadata, persist = {}, {}
        >>> persist['persistent_indicators'] = {}
        >>> persist['persistent_indicators']['Music_Voice'] = [
        ...     abjad.Momento(
        ...         context='Music_Voice',
        ...         prototype='abjad.Dynamic',
        ...         value='f',
        ...         )
        ...     ]
        >>> metadata['segment_number'] = 1
        >>> lilypond_file = maker.run(
        ...     environment='docs',
        ...     previous_metadata=metadata,
        ...     previous_persist=persist,
        ...     )
        >>> block = abjad.Block(name='layout')
        >>> block.indent = 0
        >>> lilypond_file.items.insert(0, block)
        >>> abjad.show(lilypond_file, strict=89) # doctest: +SKIP

        ..  docs::

            >>> abjad.f(lilypond_file[abjad.Score], strict=89)
            <BLANKLINE>
            \context Score = "Score"                                                                 %! baca.SingleStaffScoreTemplate.__call__()
            <<                                                                                       %! baca.SingleStaffScoreTemplate.__call__()
            <BLANKLINE>
                \context GlobalContext = "Global_Context"                                            %! abjad.ScoreTemplate._make_global_context()
                <<                                                                                   %! abjad.ScoreTemplate._make_global_context()
            <BLANKLINE>
                    \context GlobalSkips = "Global_Skips"                                            %! abjad.ScoreTemplate._make_global_context()
                    {                                                                                %! abjad.ScoreTemplate._make_global_context()
            <BLANKLINE>
                        % [Global_Skips measure 1]                                                   %! baca.SegmentMaker._comment_measure_numbers()
                        \baca-new-spacing-section #1 #24                                             %! SPACING_COMMAND:baca.HorizontalSpacingSpecifier.__call__(1)
                        \time 3/8                                                                    %! baca.SegmentMaker._make_global_skips(2):baca.SegmentMaker._set_status_tag():EXPLICIT_TIME_SIGNATURE
                        \bar ""                                                                      %! EMPTY_START_BAR:+SEGMENT:baca.SegmentMaker._make_global_skips(4)
                        \baca-time-signature-color #'blue                                            %! baca.SegmentMaker._attach_color_literal(2):EXPLICIT_TIME_SIGNATURE_COLOR
                        s1 * 3/8                                                                     %! baca.SegmentMaker._make_global_skips(1)
            <BLANKLINE>
                        % [Global_Skips measure 2]                                                   %! baca.SegmentMaker._comment_measure_numbers()
                        \baca-new-spacing-section #1 #24                                             %! SPACING_COMMAND:baca.HorizontalSpacingSpecifier.__call__(1)
                        s1 * 3/8                                                                     %! baca.SegmentMaker._make_global_skips(1)
            <BLANKLINE>
                        % [Global_Skips measure 3]                                                   %! baca.SegmentMaker._comment_measure_numbers():baca.SegmentMaker._style_phantom_measures(1):PHANTOM
                        \baca-new-spacing-section #1 #4                                              %! SPACING_COMMAND:baca.HorizontalSpacingSpecifier.__call__(1):baca.SegmentMaker._style_phantom_measures(1):PHANTOM
                        \time 1/4                                                                    %! baca.SegmentMaker._make_global_skips(3):PHANTOM:baca.SegmentMaker._set_status_tag():EXPLICIT_TIME_SIGNATURE:baca.SegmentMaker._style_phantom_measures(1)
                        \baca-time-signature-transparent                                             %! baca.SegmentMaker._style_phantom_measures(2):PHANTOM
                        s1 * 1/4                                                                     %! baca.SegmentMaker._make_global_skips(3):PHANTOM
                        \once \override Score.BarLine.transparent = ##t                              %! baca.SegmentMaker._style_phantom_measures(3):PHANTOM
                        \once \override Score.SpanBar.transparent = ##t                              %! baca.SegmentMaker._style_phantom_measures(3):PHANTOM
            <BLANKLINE>
                    }                                                                                %! abjad.ScoreTemplate._make_global_context()
            <BLANKLINE>
                >>                                                                                   %! abjad.ScoreTemplate._make_global_context()
            <BLANKLINE>
                \context MusicContext = "Music_Context"                                              %! baca.SingleStaffScoreTemplate.__call__()
                <<                                                                                   %! baca.SingleStaffScoreTemplate.__call__()
            <BLANKLINE>
                    \context Staff = "Music_Staff"                                                   %! baca.SingleStaffScoreTemplate.__call__()
                    {                                                                                %! baca.SingleStaffScoreTemplate.__call__()
            <BLANKLINE>
                        \context Voice = "Music_Voice"                                               %! baca.SingleStaffScoreTemplate.__call__()
                        {                                                                            %! baca.SingleStaffScoreTemplate.__call__()
            <BLANKLINE>
                            % [Music_Voice measure 1]                                                %! baca.SegmentMaker._comment_measure_numbers()
                        %@% \baca-not-yet-pitched-coloring                                           %! baca.SegmentMaker._color_not_yet_pitched():NOT_YET_PITCHED_COLORING
                            b'4.                                                                     %! baca.make_notes()
                            - \tweak color #(x11-color 'blue)                                        %! EXPLICIT_DYNAMIC_COLOR:_treat_persistent_wrapper(1)
                            \p                                                                       %! baca.dynamic():baca.IndicatorCommand._call():baca.SegmentMaker._set_status_tag():EXPLICIT_DYNAMIC
            <BLANKLINE>
                            % [Music_Voice measure 2]                                                %! baca.SegmentMaker._comment_measure_numbers()
                        %@% \baca-not-yet-pitched-coloring                                           %! baca.SegmentMaker._color_not_yet_pitched():NOT_YET_PITCHED_COLORING
                            b'4.                                                                     %! baca.make_notes()
            <BLANKLINE>
                            <<                                                                       %! baca.SegmentMaker._make_multimeasure_rest_container(7):PHANTOM
            <BLANKLINE>
                                \context Voice = "Music_Voice"                                       %! baca.SegmentMaker._make_multimeasure_rest_container(4):PHANTOM
                                {                                                                    %! baca.SegmentMaker._make_multimeasure_rest_container(4):PHANTOM
            <BLANKLINE>
                                    % [Music_Voice measure 3]                                        %! baca.SegmentMaker._comment_measure_numbers():baca.SegmentMaker._style_phantom_measures(5):PHANTOM
                                    \abjad-invisible-music-coloring                                  %! baca.SegmentMaker._make_multimeasure_rest_container(2):PHANTOM:NOTE:INVISIBLE_MUSIC_COLORING:baca.SegmentMaker._style_phantom_measures(5)
                                %@% \abjad-invisible-music                                           %! baca.SegmentMaker._make_multimeasure_rest_container(3):PHANTOM:NOTE:INVISIBLE_MUSIC_COMMAND:baca.SegmentMaker._style_phantom_measures(5)
                                %@% \baca-not-yet-pitched-coloring                                   %! baca.SegmentMaker._color_not_yet_pitched():NOT_YET_PITCHED_COLORING:HIDDEN:NOTE:baca.SegmentMaker._style_phantom_measures(5):PHANTOM
                                    b'1 * 1/4                                                        %! baca.SegmentMaker._make_multimeasure_rest_container(1):PHANTOM:HIDDEN:NOTE
                                %@% ^ \baca-duration-multiplier-markup #"1" #"4"                     %! baca.SegmentMaker._label_duration_multipliers():DURATION_MULTIPLIER:HIDDEN:NOTE:PHANTOM:baca.SegmentMaker._style_phantom_measures(5)
            <BLANKLINE>
                                }                                                                    %! baca.SegmentMaker._make_multimeasure_rest_container(4):PHANTOM
            <BLANKLINE>
                                \context Voice = "Rest_Voice"                                        %! baca.SegmentMaker._make_multimeasure_rest_container(6):PHANTOM
                                {                                                                    %! baca.SegmentMaker._make_multimeasure_rest_container(6):PHANTOM
            <BLANKLINE>
                                    % [Rest_Voice measure 3]                                         %! baca.SegmentMaker._comment_measure_numbers():baca.SegmentMaker._style_phantom_measures(5):PHANTOM
                                    \once \override Score.TimeSignature.X-extent = ##f               %! baca.SegmentMaker._style_phantom_measures(6):PHANTOM
                                    \once \override MultiMeasureRest.transparent = ##t               %! baca.SegmentMaker._style_phantom_measures(7):PHANTOM
                                    \stopStaff                                                       %! baca.SegmentMaker._style_phantom_measures(8):PHANTOM
                                    \once \override Staff.StaffSymbol.transparent = ##t              %! baca.SegmentMaker._style_phantom_measures(8):PHANTOM
                                    \startStaff                                                      %! baca.SegmentMaker._style_phantom_measures(8):PHANTOM
                                    R1 * 1/4                                                         %! baca.SegmentMaker._make_multimeasure_rest_container(5):PHANTOM:REST_VOICE:MULTIMEASURE_REST
                                %@% ^ \baca-duration-multiplier-markup #"1" #"4"                     %! baca.SegmentMaker._label_duration_multipliers():DURATION_MULTIPLIER:MULTIMEASURE_REST:PHANTOM:REST_VOICE:baca.SegmentMaker._style_phantom_measures(5)
            <BLANKLINE>
                                }                                                                    %! baca.SegmentMaker._make_multimeasure_rest_container(6):PHANTOM
            <BLANKLINE>
                            >>                                                                       %! baca.SegmentMaker._make_multimeasure_rest_container(7):PHANTOM
            <BLANKLINE>
                        }                                                                            %! baca.SingleStaffScoreTemplate.__call__()
            <BLANKLINE>
                    }                                                                                %! baca.SingleStaffScoreTemplate.__call__()
            <BLANKLINE>
                >>                                                                                   %! baca.SingleStaffScoreTemplate.__call__()
            <BLANKLINE>
            >>                                                                                       %! baca.SingleStaffScoreTemplate.__call__()

    ..  container:: example

        Reapplied dynamics color green:

        >>> maker = baca.SegmentMaker(
        ...     deactivate=[abjad.tags.NOT_YET_PITCHED_COLORING],
        ...     score_template=baca.SingleStaffScoreTemplate(),
        ...     spacing=baca.minimum_duration((1, 24)),
        ...     time_signatures=[(3, 8), (3, 8)],
        ...     )
        >>> maker(
        ...     'Music_Voice',
        ...     baca.make_notes(),
        ...     )

        >>> metadata, persist = {}, {}
        >>> persist['persistent_indicators'] = {}
        >>> persist['persistent_indicators']['Music_Voice'] = [
        ...     abjad.Momento(
        ...         context='Music_Voice',
        ...         prototype='abjad.Dynamic',
        ...         value='f',
        ...         )
        ...     ]
        >>> metadata['segment_number'] = 1
        >>> lilypond_file = maker.run(
        ...     environment='docs',
        ...     previous_metadata=metadata,
        ...     previous_persist=persist,
        ...     )
        >>> block = abjad.Block(name='layout')
        >>> block.indent = 0
        >>> lilypond_file.items.insert(0, block)
        >>> abjad.show(lilypond_file, strict=89) # doctest: +SKIP

        ..  docs::

            >>> abjad.f(lilypond_file[abjad.Score], strict=89)
            <BLANKLINE>
            \context Score = "Score"                                                                 %! baca.SingleStaffScoreTemplate.__call__()
            <<                                                                                       %! baca.SingleStaffScoreTemplate.__call__()
            <BLANKLINE>
                \context GlobalContext = "Global_Context"                                            %! abjad.ScoreTemplate._make_global_context()
                <<                                                                                   %! abjad.ScoreTemplate._make_global_context()
            <BLANKLINE>
                    \context GlobalSkips = "Global_Skips"                                            %! abjad.ScoreTemplate._make_global_context()
                    {                                                                                %! abjad.ScoreTemplate._make_global_context()
            <BLANKLINE>
                        % [Global_Skips measure 1]                                                   %! baca.SegmentMaker._comment_measure_numbers()
                        \baca-new-spacing-section #1 #24                                             %! SPACING_COMMAND:baca.HorizontalSpacingSpecifier.__call__(1)
                        \time 3/8                                                                    %! baca.SegmentMaker._make_global_skips(2):baca.SegmentMaker._set_status_tag():EXPLICIT_TIME_SIGNATURE
                        \bar ""                                                                      %! EMPTY_START_BAR:+SEGMENT:baca.SegmentMaker._make_global_skips(4)
                        \baca-time-signature-color #'blue                                            %! baca.SegmentMaker._attach_color_literal(2):EXPLICIT_TIME_SIGNATURE_COLOR
                        s1 * 3/8                                                                     %! baca.SegmentMaker._make_global_skips(1)
            <BLANKLINE>
                        % [Global_Skips measure 2]                                                   %! baca.SegmentMaker._comment_measure_numbers()
                        \baca-new-spacing-section #1 #24                                             %! SPACING_COMMAND:baca.HorizontalSpacingSpecifier.__call__(1)
                        s1 * 3/8                                                                     %! baca.SegmentMaker._make_global_skips(1)
            <BLANKLINE>
                        % [Global_Skips measure 3]                                                   %! baca.SegmentMaker._comment_measure_numbers():baca.SegmentMaker._style_phantom_measures(1):PHANTOM
                        \baca-new-spacing-section #1 #4                                              %! SPACING_COMMAND:baca.HorizontalSpacingSpecifier.__call__(1):baca.SegmentMaker._style_phantom_measures(1):PHANTOM
                        \time 1/4                                                                    %! baca.SegmentMaker._make_global_skips(3):PHANTOM:baca.SegmentMaker._set_status_tag():EXPLICIT_TIME_SIGNATURE:baca.SegmentMaker._style_phantom_measures(1)
                        \baca-time-signature-transparent                                             %! baca.SegmentMaker._style_phantom_measures(2):PHANTOM
                        s1 * 1/4                                                                     %! baca.SegmentMaker._make_global_skips(3):PHANTOM
                        \once \override Score.BarLine.transparent = ##t                              %! baca.SegmentMaker._style_phantom_measures(3):PHANTOM
                        \once \override Score.SpanBar.transparent = ##t                              %! baca.SegmentMaker._style_phantom_measures(3):PHANTOM
            <BLANKLINE>
                    }                                                                                %! abjad.ScoreTemplate._make_global_context()
            <BLANKLINE>
                >>                                                                                   %! abjad.ScoreTemplate._make_global_context()
            <BLANKLINE>
                \context MusicContext = "Music_Context"                                              %! baca.SingleStaffScoreTemplate.__call__()
                <<                                                                                   %! baca.SingleStaffScoreTemplate.__call__()
            <BLANKLINE>
                    \context Staff = "Music_Staff"                                                   %! baca.SingleStaffScoreTemplate.__call__()
                    {                                                                                %! baca.SingleStaffScoreTemplate.__call__()
            <BLANKLINE>
                        \context Voice = "Music_Voice"                                               %! baca.SingleStaffScoreTemplate.__call__()
                        {                                                                            %! baca.SingleStaffScoreTemplate.__call__()
            <BLANKLINE>
                            % [Music_Voice measure 1]                                                %! baca.SegmentMaker._comment_measure_numbers()
                        %@% \baca-not-yet-pitched-coloring                                           %! baca.SegmentMaker._color_not_yet_pitched():NOT_YET_PITCHED_COLORING
                            b'4.                                                                     %! baca.make_notes()
                            - \tweak color #(x11-color 'green4)                                      %! REAPPLIED_DYNAMIC_COLOR:_treat_persistent_wrapper(1)
                            \f                                                                       %! baca.SegmentMaker._reapply_persistent_indicators(3):baca.SegmentMaker._set_status_tag():REAPPLIED_DYNAMIC
            <BLANKLINE>
                            % [Music_Voice measure 2]                                                %! baca.SegmentMaker._comment_measure_numbers()
                        %@% \baca-not-yet-pitched-coloring                                           %! baca.SegmentMaker._color_not_yet_pitched():NOT_YET_PITCHED_COLORING
                            b'4.                                                                     %! baca.make_notes()
            <BLANKLINE>
                            <<                                                                       %! baca.SegmentMaker._make_multimeasure_rest_container(7):PHANTOM
            <BLANKLINE>
                                \context Voice = "Music_Voice"                                       %! baca.SegmentMaker._make_multimeasure_rest_container(4):PHANTOM
                                {                                                                    %! baca.SegmentMaker._make_multimeasure_rest_container(4):PHANTOM
            <BLANKLINE>
                                    % [Music_Voice measure 3]                                        %! baca.SegmentMaker._comment_measure_numbers():baca.SegmentMaker._style_phantom_measures(5):PHANTOM
                                    \abjad-invisible-music-coloring                                  %! baca.SegmentMaker._make_multimeasure_rest_container(2):PHANTOM:NOTE:INVISIBLE_MUSIC_COLORING:baca.SegmentMaker._style_phantom_measures(5)
                                %@% \abjad-invisible-music                                           %! baca.SegmentMaker._make_multimeasure_rest_container(3):PHANTOM:NOTE:INVISIBLE_MUSIC_COMMAND:baca.SegmentMaker._style_phantom_measures(5)
                                %@% \baca-not-yet-pitched-coloring                                   %! baca.SegmentMaker._color_not_yet_pitched():NOT_YET_PITCHED_COLORING:HIDDEN:NOTE:baca.SegmentMaker._style_phantom_measures(5):PHANTOM
                                    b'1 * 1/4                                                        %! baca.SegmentMaker._make_multimeasure_rest_container(1):PHANTOM:HIDDEN:NOTE
                                %@% ^ \baca-duration-multiplier-markup #"1" #"4"                     %! baca.SegmentMaker._label_duration_multipliers():DURATION_MULTIPLIER:HIDDEN:NOTE:PHANTOM:baca.SegmentMaker._style_phantom_measures(5)
            <BLANKLINE>
                                }                                                                    %! baca.SegmentMaker._make_multimeasure_rest_container(4):PHANTOM
            <BLANKLINE>
                                \context Voice = "Rest_Voice"                                        %! baca.SegmentMaker._make_multimeasure_rest_container(6):PHANTOM
                                {                                                                    %! baca.SegmentMaker._make_multimeasure_rest_container(6):PHANTOM
            <BLANKLINE>
                                    % [Rest_Voice measure 3]                                         %! baca.SegmentMaker._comment_measure_numbers():baca.SegmentMaker._style_phantom_measures(5):PHANTOM
                                    \once \override Score.TimeSignature.X-extent = ##f               %! baca.SegmentMaker._style_phantom_measures(6):PHANTOM
                                    \once \override MultiMeasureRest.transparent = ##t               %! baca.SegmentMaker._style_phantom_measures(7):PHANTOM
                                    \stopStaff                                                       %! baca.SegmentMaker._style_phantom_measures(8):PHANTOM
                                    \once \override Staff.StaffSymbol.transparent = ##t              %! baca.SegmentMaker._style_phantom_measures(8):PHANTOM
                                    \startStaff                                                      %! baca.SegmentMaker._style_phantom_measures(8):PHANTOM
                                    R1 * 1/4                                                         %! baca.SegmentMaker._make_multimeasure_rest_container(5):PHANTOM:REST_VOICE:MULTIMEASURE_REST
                                %@% ^ \baca-duration-multiplier-markup #"1" #"4"                     %! baca.SegmentMaker._label_duration_multipliers():DURATION_MULTIPLIER:MULTIMEASURE_REST:PHANTOM:REST_VOICE:baca.SegmentMaker._style_phantom_measures(5)
            <BLANKLINE>
                                }                                                                    %! baca.SegmentMaker._make_multimeasure_rest_container(6):PHANTOM
            <BLANKLINE>
                            >>                                                                       %! baca.SegmentMaker._make_multimeasure_rest_container(7):PHANTOM
            <BLANKLINE>
                        }                                                                            %! baca.SingleStaffScoreTemplate.__call__()
            <BLANKLINE>
                    }                                                                                %! baca.SingleStaffScoreTemplate.__call__()
            <BLANKLINE>
                >>                                                                                   %! baca.SingleStaffScoreTemplate.__call__()
            <BLANKLINE>
            >>                                                                                       %! baca.SingleStaffScoreTemplate.__call__()

    ..  container:: example

        Redundant dynamics color pink:

        >>> maker = baca.SegmentMaker(
        ...     deactivate=[abjad.tags.NOT_YET_PITCHED_COLORING],
        ...     score_template=baca.SingleStaffScoreTemplate(),
        ...     spacing=baca.minimum_duration((1, 24)),
        ...     time_signatures=[(3, 8), (3, 8)],
        ...     )
        >>> maker(
        ...     'Music_Voice',
        ...     baca.make_notes(),
        ...     baca.dynamic('f'),
        ...     baca.dynamic('f', selector=baca.leaf(1)),
        ...     )

        >>> lilypond_file = maker.run(environment='docs')
        >>> block = abjad.Block(name='layout')
        >>> block.indent = 0
        >>> lilypond_file.items.insert(0, block)
        >>> abjad.show(lilypond_file, strict=89) # doctest: +SKIP

        ..  docs::

            >>> abjad.f(lilypond_file[abjad.Score], strict=89)
            <BLANKLINE>
            \context Score = "Score"                                                                 %! baca.SingleStaffScoreTemplate.__call__()
            <<                                                                                       %! baca.SingleStaffScoreTemplate.__call__()
            <BLANKLINE>
                \context GlobalContext = "Global_Context"                                            %! abjad.ScoreTemplate._make_global_context()
                <<                                                                                   %! abjad.ScoreTemplate._make_global_context()
            <BLANKLINE>
                    \context GlobalSkips = "Global_Skips"                                            %! abjad.ScoreTemplate._make_global_context()
                    {                                                                                %! abjad.ScoreTemplate._make_global_context()
            <BLANKLINE>
                        % [Global_Skips measure 1]                                                   %! baca.SegmentMaker._comment_measure_numbers()
                        \baca-new-spacing-section #1 #24                                             %! SPACING_COMMAND:baca.HorizontalSpacingSpecifier.__call__(1)
                        \time 3/8                                                                    %! baca.SegmentMaker._make_global_skips(2):baca.SegmentMaker._set_status_tag():EXPLICIT_TIME_SIGNATURE
                        \baca-time-signature-color #'blue                                            %! baca.SegmentMaker._attach_color_literal(2):EXPLICIT_TIME_SIGNATURE_COLOR
                        s1 * 3/8                                                                     %! baca.SegmentMaker._make_global_skips(1)
            <BLANKLINE>
                        % [Global_Skips measure 2]                                                   %! baca.SegmentMaker._comment_measure_numbers()
                        \baca-new-spacing-section #1 #24                                             %! SPACING_COMMAND:baca.HorizontalSpacingSpecifier.__call__(1)
                        s1 * 3/8                                                                     %! baca.SegmentMaker._make_global_skips(1)
            <BLANKLINE>
                        % [Global_Skips measure 3]                                                   %! baca.SegmentMaker._comment_measure_numbers():baca.SegmentMaker._style_phantom_measures(1):PHANTOM
                        \baca-new-spacing-section #1 #4                                              %! SPACING_COMMAND:baca.HorizontalSpacingSpecifier.__call__(1):baca.SegmentMaker._style_phantom_measures(1):PHANTOM
                        \time 1/4                                                                    %! baca.SegmentMaker._make_global_skips(3):PHANTOM:baca.SegmentMaker._set_status_tag():EXPLICIT_TIME_SIGNATURE:baca.SegmentMaker._style_phantom_measures(1)
                        \baca-time-signature-transparent                                             %! baca.SegmentMaker._style_phantom_measures(2):PHANTOM
                        s1 * 1/4                                                                     %! baca.SegmentMaker._make_global_skips(3):PHANTOM
                        \once \override Score.BarLine.transparent = ##t                              %! baca.SegmentMaker._style_phantom_measures(3):PHANTOM
                        \once \override Score.SpanBar.transparent = ##t                              %! baca.SegmentMaker._style_phantom_measures(3):PHANTOM
            <BLANKLINE>
                    }                                                                                %! abjad.ScoreTemplate._make_global_context()
            <BLANKLINE>
                >>                                                                                   %! abjad.ScoreTemplate._make_global_context()
            <BLANKLINE>
                \context MusicContext = "Music_Context"                                              %! baca.SingleStaffScoreTemplate.__call__()
                <<                                                                                   %! baca.SingleStaffScoreTemplate.__call__()
            <BLANKLINE>
                    \context Staff = "Music_Staff"                                                   %! baca.SingleStaffScoreTemplate.__call__()
                    {                                                                                %! baca.SingleStaffScoreTemplate.__call__()
            <BLANKLINE>
                        \context Voice = "Music_Voice"                                               %! baca.SingleStaffScoreTemplate.__call__()
                        {                                                                            %! baca.SingleStaffScoreTemplate.__call__()
            <BLANKLINE>
                            % [Music_Voice measure 1]                                                %! baca.SegmentMaker._comment_measure_numbers()
                        %@% \baca-not-yet-pitched-coloring                                           %! baca.SegmentMaker._color_not_yet_pitched():NOT_YET_PITCHED_COLORING
                            b'4.                                                                     %! baca.make_notes()
                            - \tweak color #(x11-color 'blue)                                        %! EXPLICIT_DYNAMIC_COLOR:_treat_persistent_wrapper(1)
                            \f                                                                       %! baca.dynamic():baca.IndicatorCommand._call():baca.SegmentMaker._set_status_tag():EXPLICIT_DYNAMIC
            <BLANKLINE>
                            % [Music_Voice measure 2]                                                %! baca.SegmentMaker._comment_measure_numbers()
                        %@% \baca-not-yet-pitched-coloring                                           %! baca.SegmentMaker._color_not_yet_pitched():NOT_YET_PITCHED_COLORING
                            b'4.                                                                     %! baca.make_notes()
                            - \tweak color #(x11-color 'DeepPink1)                                   %! REDUNDANT_DYNAMIC_COLOR:_treat_persistent_wrapper(1)
                            \f                                                                       %! baca.dynamic():baca.IndicatorCommand._call():baca.SegmentMaker._set_status_tag():REDUNDANT_DYNAMIC
            <BLANKLINE>
                            <<                                                                       %! baca.SegmentMaker._make_multimeasure_rest_container(7):PHANTOM
            <BLANKLINE>
                                \context Voice = "Music_Voice"                                       %! baca.SegmentMaker._make_multimeasure_rest_container(4):PHANTOM
                                {                                                                    %! baca.SegmentMaker._make_multimeasure_rest_container(4):PHANTOM
            <BLANKLINE>
                                    % [Music_Voice measure 3]                                        %! baca.SegmentMaker._comment_measure_numbers():baca.SegmentMaker._style_phantom_measures(5):PHANTOM
                                    \abjad-invisible-music-coloring                                  %! baca.SegmentMaker._make_multimeasure_rest_container(2):PHANTOM:NOTE:INVISIBLE_MUSIC_COLORING:baca.SegmentMaker._style_phantom_measures(5)
                                %@% \abjad-invisible-music                                           %! baca.SegmentMaker._make_multimeasure_rest_container(3):PHANTOM:NOTE:INVISIBLE_MUSIC_COMMAND:baca.SegmentMaker._style_phantom_measures(5)
                                %@% \baca-not-yet-pitched-coloring                                   %! baca.SegmentMaker._color_not_yet_pitched():NOT_YET_PITCHED_COLORING:HIDDEN:NOTE:baca.SegmentMaker._style_phantom_measures(5):PHANTOM
                                    b'1 * 1/4                                                        %! baca.SegmentMaker._make_multimeasure_rest_container(1):PHANTOM:HIDDEN:NOTE
                                %@% ^ \baca-duration-multiplier-markup #"1" #"4"                     %! baca.SegmentMaker._label_duration_multipliers():DURATION_MULTIPLIER:HIDDEN:NOTE:PHANTOM:baca.SegmentMaker._style_phantom_measures(5)
            <BLANKLINE>
                                }                                                                    %! baca.SegmentMaker._make_multimeasure_rest_container(4):PHANTOM
            <BLANKLINE>
                                \context Voice = "Rest_Voice"                                        %! baca.SegmentMaker._make_multimeasure_rest_container(6):PHANTOM
                                {                                                                    %! baca.SegmentMaker._make_multimeasure_rest_container(6):PHANTOM
            <BLANKLINE>
                                    % [Rest_Voice measure 3]                                         %! baca.SegmentMaker._comment_measure_numbers():baca.SegmentMaker._style_phantom_measures(5):PHANTOM
                                    \once \override Score.TimeSignature.X-extent = ##f               %! baca.SegmentMaker._style_phantom_measures(6):PHANTOM
                                    \once \override MultiMeasureRest.transparent = ##t               %! baca.SegmentMaker._style_phantom_measures(7):PHANTOM
                                    \stopStaff                                                       %! baca.SegmentMaker._style_phantom_measures(8):PHANTOM
                                    \once \override Staff.StaffSymbol.transparent = ##t              %! baca.SegmentMaker._style_phantom_measures(8):PHANTOM
                                    \startStaff                                                      %! baca.SegmentMaker._style_phantom_measures(8):PHANTOM
                                    R1 * 1/4                                                         %! baca.SegmentMaker._make_multimeasure_rest_container(5):PHANTOM:REST_VOICE:MULTIMEASURE_REST
                                %@% ^ \baca-duration-multiplier-markup #"1" #"4"                     %! baca.SegmentMaker._label_duration_multipliers():DURATION_MULTIPLIER:MULTIMEASURE_REST:PHANTOM:REST_VOICE:baca.SegmentMaker._style_phantom_measures(5)
            <BLANKLINE>
                                }                                                                    %! baca.SegmentMaker._make_multimeasure_rest_container(6):PHANTOM
            <BLANKLINE>
                            >>                                                                       %! baca.SegmentMaker._make_multimeasure_rest_container(7):PHANTOM
            <BLANKLINE>
                        }                                                                            %! baca.SingleStaffScoreTemplate.__call__()
            <BLANKLINE>
                    }                                                                                %! baca.SingleStaffScoreTemplate.__call__()
            <BLANKLINE>
                >>                                                                                   %! baca.SingleStaffScoreTemplate.__call__()
            <BLANKLINE>
            >>                                                                                       %! baca.SingleStaffScoreTemplate.__call__()

        Even at the beginning of a segment:

        >>> maker = baca.SegmentMaker(
        ...     deactivate=[abjad.tags.NOT_YET_PITCHED_COLORING],
        ...     score_template=baca.SingleStaffScoreTemplate(),
        ...     spacing=baca.minimum_duration((1, 24)),
        ...     time_signatures=[(3, 8), (3, 8)],
        ...     )
        >>> maker(
        ...     'Music_Voice',
        ...     baca.make_notes(),
        ...     baca.dynamic('f'),
        ...     )

        >>> metadata, persist = {}, {}
        >>> persist['persistent_indicators'] = {}
        >>> persist['persistent_indicators']['Music_Voice'] = [
        ...     abjad.Momento(
        ...         context='Music_Voice',
        ...         prototype='abjad.Dynamic',
        ...         value='f',
        ...         )
        ...     ]
        >>> metadata['segment_number'] = 1
        >>> lilypond_file = maker.run(
        ...     environment='docs',
        ...     previous_metadata=metadata,
        ...     previous_persist=persist,
        ...     )
        >>> block = abjad.Block(name='layout')
        >>> block.indent = 0
        >>> lilypond_file.items.insert(0, block)
        >>> abjad.show(lilypond_file, strict=89) # doctest: +SKIP

        ..  docs::

            >>> abjad.f(lilypond_file[abjad.Score], strict=89)
            <BLANKLINE>
            \context Score = "Score"                                                                 %! baca.SingleStaffScoreTemplate.__call__()
            <<                                                                                       %! baca.SingleStaffScoreTemplate.__call__()
            <BLANKLINE>
                \context GlobalContext = "Global_Context"                                            %! abjad.ScoreTemplate._make_global_context()
                <<                                                                                   %! abjad.ScoreTemplate._make_global_context()
            <BLANKLINE>
                    \context GlobalSkips = "Global_Skips"                                            %! abjad.ScoreTemplate._make_global_context()
                    {                                                                                %! abjad.ScoreTemplate._make_global_context()
            <BLANKLINE>
                        % [Global_Skips measure 1]                                                   %! baca.SegmentMaker._comment_measure_numbers()
                        \baca-new-spacing-section #1 #24                                             %! SPACING_COMMAND:baca.HorizontalSpacingSpecifier.__call__(1)
                        \time 3/8                                                                    %! baca.SegmentMaker._make_global_skips(2):baca.SegmentMaker._set_status_tag():EXPLICIT_TIME_SIGNATURE
                        \bar ""                                                                      %! EMPTY_START_BAR:+SEGMENT:baca.SegmentMaker._make_global_skips(4)
                        \baca-time-signature-color #'blue                                            %! baca.SegmentMaker._attach_color_literal(2):EXPLICIT_TIME_SIGNATURE_COLOR
                        s1 * 3/8                                                                     %! baca.SegmentMaker._make_global_skips(1)
            <BLANKLINE>
                        % [Global_Skips measure 2]                                                   %! baca.SegmentMaker._comment_measure_numbers()
                        \baca-new-spacing-section #1 #24                                             %! SPACING_COMMAND:baca.HorizontalSpacingSpecifier.__call__(1)
                        s1 * 3/8                                                                     %! baca.SegmentMaker._make_global_skips(1)
            <BLANKLINE>
                        % [Global_Skips measure 3]                                                   %! baca.SegmentMaker._comment_measure_numbers():baca.SegmentMaker._style_phantom_measures(1):PHANTOM
                        \baca-new-spacing-section #1 #4                                              %! SPACING_COMMAND:baca.HorizontalSpacingSpecifier.__call__(1):baca.SegmentMaker._style_phantom_measures(1):PHANTOM
                        \time 1/4                                                                    %! baca.SegmentMaker._make_global_skips(3):PHANTOM:baca.SegmentMaker._set_status_tag():EXPLICIT_TIME_SIGNATURE:baca.SegmentMaker._style_phantom_measures(1)
                        \baca-time-signature-transparent                                             %! baca.SegmentMaker._style_phantom_measures(2):PHANTOM
                        s1 * 1/4                                                                     %! baca.SegmentMaker._make_global_skips(3):PHANTOM
                        \once \override Score.BarLine.transparent = ##t                              %! baca.SegmentMaker._style_phantom_measures(3):PHANTOM
                        \once \override Score.SpanBar.transparent = ##t                              %! baca.SegmentMaker._style_phantom_measures(3):PHANTOM
            <BLANKLINE>
                    }                                                                                %! abjad.ScoreTemplate._make_global_context()
            <BLANKLINE>
                >>                                                                                   %! abjad.ScoreTemplate._make_global_context()
            <BLANKLINE>
                \context MusicContext = "Music_Context"                                              %! baca.SingleStaffScoreTemplate.__call__()
                <<                                                                                   %! baca.SingleStaffScoreTemplate.__call__()
            <BLANKLINE>
                    \context Staff = "Music_Staff"                                                   %! baca.SingleStaffScoreTemplate.__call__()
                    {                                                                                %! baca.SingleStaffScoreTemplate.__call__()
            <BLANKLINE>
                        \context Voice = "Music_Voice"                                               %! baca.SingleStaffScoreTemplate.__call__()
                        {                                                                            %! baca.SingleStaffScoreTemplate.__call__()
            <BLANKLINE>
                            % [Music_Voice measure 1]                                                %! baca.SegmentMaker._comment_measure_numbers()
                        %@% \baca-not-yet-pitched-coloring                                           %! baca.SegmentMaker._color_not_yet_pitched():NOT_YET_PITCHED_COLORING
                            b'4.                                                                     %! baca.make_notes()
                            - \tweak color #(x11-color 'DeepPink1)                                   %! REDUNDANT_DYNAMIC_COLOR:_treat_persistent_wrapper(1)
                            \f                                                                       %! baca.dynamic():baca.IndicatorCommand._call():baca.SegmentMaker._set_status_tag():REDUNDANT_DYNAMIC
            <BLANKLINE>
                            % [Music_Voice measure 2]                                                %! baca.SegmentMaker._comment_measure_numbers()
                        %@% \baca-not-yet-pitched-coloring                                           %! baca.SegmentMaker._color_not_yet_pitched():NOT_YET_PITCHED_COLORING
                            b'4.                                                                     %! baca.make_notes()
            <BLANKLINE>
                            <<                                                                       %! baca.SegmentMaker._make_multimeasure_rest_container(7):PHANTOM
            <BLANKLINE>
                                \context Voice = "Music_Voice"                                       %! baca.SegmentMaker._make_multimeasure_rest_container(4):PHANTOM
                                {                                                                    %! baca.SegmentMaker._make_multimeasure_rest_container(4):PHANTOM
            <BLANKLINE>
                                    % [Music_Voice measure 3]                                        %! baca.SegmentMaker._comment_measure_numbers():baca.SegmentMaker._style_phantom_measures(5):PHANTOM
                                    \abjad-invisible-music-coloring                                  %! baca.SegmentMaker._make_multimeasure_rest_container(2):PHANTOM:NOTE:INVISIBLE_MUSIC_COLORING:baca.SegmentMaker._style_phantom_measures(5)
                                %@% \abjad-invisible-music                                           %! baca.SegmentMaker._make_multimeasure_rest_container(3):PHANTOM:NOTE:INVISIBLE_MUSIC_COMMAND:baca.SegmentMaker._style_phantom_measures(5)
                                %@% \baca-not-yet-pitched-coloring                                   %! baca.SegmentMaker._color_not_yet_pitched():NOT_YET_PITCHED_COLORING:HIDDEN:NOTE:baca.SegmentMaker._style_phantom_measures(5):PHANTOM
                                    b'1 * 1/4                                                        %! baca.SegmentMaker._make_multimeasure_rest_container(1):PHANTOM:HIDDEN:NOTE
                                %@% ^ \baca-duration-multiplier-markup #"1" #"4"                     %! baca.SegmentMaker._label_duration_multipliers():DURATION_MULTIPLIER:HIDDEN:NOTE:PHANTOM:baca.SegmentMaker._style_phantom_measures(5)
            <BLANKLINE>
                                }                                                                    %! baca.SegmentMaker._make_multimeasure_rest_container(4):PHANTOM
            <BLANKLINE>
                                \context Voice = "Rest_Voice"                                        %! baca.SegmentMaker._make_multimeasure_rest_container(6):PHANTOM
                                {                                                                    %! baca.SegmentMaker._make_multimeasure_rest_container(6):PHANTOM
            <BLANKLINE>
                                    % [Rest_Voice measure 3]                                         %! baca.SegmentMaker._comment_measure_numbers():baca.SegmentMaker._style_phantom_measures(5):PHANTOM
                                    \once \override Score.TimeSignature.X-extent = ##f               %! baca.SegmentMaker._style_phantom_measures(6):PHANTOM
                                    \once \override MultiMeasureRest.transparent = ##t               %! baca.SegmentMaker._style_phantom_measures(7):PHANTOM
                                    \stopStaff                                                       %! baca.SegmentMaker._style_phantom_measures(8):PHANTOM
                                    \once \override Staff.StaffSymbol.transparent = ##t              %! baca.SegmentMaker._style_phantom_measures(8):PHANTOM
                                    \startStaff                                                      %! baca.SegmentMaker._style_phantom_measures(8):PHANTOM
                                    R1 * 1/4                                                         %! baca.SegmentMaker._make_multimeasure_rest_container(5):PHANTOM:REST_VOICE:MULTIMEASURE_REST
                                %@% ^ \baca-duration-multiplier-markup #"1" #"4"                     %! baca.SegmentMaker._label_duration_multipliers():DURATION_MULTIPLIER:MULTIMEASURE_REST:PHANTOM:REST_VOICE:baca.SegmentMaker._style_phantom_measures(5)
            <BLANKLINE>
                                }                                                                    %! baca.SegmentMaker._make_multimeasure_rest_container(6):PHANTOM
            <BLANKLINE>
                            >>                                                                       %! baca.SegmentMaker._make_multimeasure_rest_container(7):PHANTOM
            <BLANKLINE>
                        }                                                                            %! baca.SingleStaffScoreTemplate.__call__()
            <BLANKLINE>
                    }                                                                                %! baca.SingleStaffScoreTemplate.__call__()
            <BLANKLINE>
                >>                                                                                   %! baca.SingleStaffScoreTemplate.__call__()
            <BLANKLINE>
            >>                                                                                       %! baca.SingleStaffScoreTemplate.__call__()

        Sforzando dynamics do not count as redundant:

        >>> maker = baca.SegmentMaker(
        ...     deactivate=[abjad.tags.NOT_YET_PITCHED_COLORING],
        ...     score_template=baca.SingleStaffScoreTemplate(),
        ...     spacing=baca.minimum_duration((1, 24)),
        ...     time_signatures=[(3, 8), (3, 8)],
        ...     )
        >>> maker(
        ...     'Music_Voice',
        ...     baca.make_notes(),
        ...     baca.dynamic('sfz'),
        ...     baca.dynamic('sfz', selector=baca.leaf(1)),
        ...     )

        >>> lilypond_file = maker.run(environment='docs')
        >>> block = abjad.Block(name='layout')
        >>> block.indent = 0
        >>> lilypond_file.items.insert(0, block)
        >>> abjad.show(lilypond_file, strict=89) # doctest: +SKIP

        ..  docs::

            >>> abjad.f(lilypond_file[abjad.Score], strict=89)
            <BLANKLINE>
            \context Score = "Score"                                                                 %! baca.SingleStaffScoreTemplate.__call__()
            <<                                                                                       %! baca.SingleStaffScoreTemplate.__call__()
            <BLANKLINE>
                \context GlobalContext = "Global_Context"                                            %! abjad.ScoreTemplate._make_global_context()
                <<                                                                                   %! abjad.ScoreTemplate._make_global_context()
            <BLANKLINE>
                    \context GlobalSkips = "Global_Skips"                                            %! abjad.ScoreTemplate._make_global_context()
                    {                                                                                %! abjad.ScoreTemplate._make_global_context()
            <BLANKLINE>
                        % [Global_Skips measure 1]                                                   %! baca.SegmentMaker._comment_measure_numbers()
                        \baca-new-spacing-section #1 #24                                             %! SPACING_COMMAND:baca.HorizontalSpacingSpecifier.__call__(1)
                        \time 3/8                                                                    %! baca.SegmentMaker._make_global_skips(2):baca.SegmentMaker._set_status_tag():EXPLICIT_TIME_SIGNATURE
                        \baca-time-signature-color #'blue                                            %! baca.SegmentMaker._attach_color_literal(2):EXPLICIT_TIME_SIGNATURE_COLOR
                        s1 * 3/8                                                                     %! baca.SegmentMaker._make_global_skips(1)
            <BLANKLINE>
                        % [Global_Skips measure 2]                                                   %! baca.SegmentMaker._comment_measure_numbers()
                        \baca-new-spacing-section #1 #24                                             %! SPACING_COMMAND:baca.HorizontalSpacingSpecifier.__call__(1)
                        s1 * 3/8                                                                     %! baca.SegmentMaker._make_global_skips(1)
            <BLANKLINE>
                        % [Global_Skips measure 3]                                                   %! baca.SegmentMaker._comment_measure_numbers():baca.SegmentMaker._style_phantom_measures(1):PHANTOM
                        \baca-new-spacing-section #1 #4                                              %! SPACING_COMMAND:baca.HorizontalSpacingSpecifier.__call__(1):baca.SegmentMaker._style_phantom_measures(1):PHANTOM
                        \time 1/4                                                                    %! baca.SegmentMaker._make_global_skips(3):PHANTOM:baca.SegmentMaker._set_status_tag():EXPLICIT_TIME_SIGNATURE:baca.SegmentMaker._style_phantom_measures(1)
                        \baca-time-signature-transparent                                             %! baca.SegmentMaker._style_phantom_measures(2):PHANTOM
                        s1 * 1/4                                                                     %! baca.SegmentMaker._make_global_skips(3):PHANTOM
                        \once \override Score.BarLine.transparent = ##t                              %! baca.SegmentMaker._style_phantom_measures(3):PHANTOM
                        \once \override Score.SpanBar.transparent = ##t                              %! baca.SegmentMaker._style_phantom_measures(3):PHANTOM
            <BLANKLINE>
                    }                                                                                %! abjad.ScoreTemplate._make_global_context()
            <BLANKLINE>
                >>                                                                                   %! abjad.ScoreTemplate._make_global_context()
            <BLANKLINE>
                \context MusicContext = "Music_Context"                                              %! baca.SingleStaffScoreTemplate.__call__()
                <<                                                                                   %! baca.SingleStaffScoreTemplate.__call__()
            <BLANKLINE>
                    \context Staff = "Music_Staff"                                                   %! baca.SingleStaffScoreTemplate.__call__()
                    {                                                                                %! baca.SingleStaffScoreTemplate.__call__()
            <BLANKLINE>
                        \context Voice = "Music_Voice"                                               %! baca.SingleStaffScoreTemplate.__call__()
                        {                                                                            %! baca.SingleStaffScoreTemplate.__call__()
            <BLANKLINE>
                            % [Music_Voice measure 1]                                                %! baca.SegmentMaker._comment_measure_numbers()
                        %@% \baca-not-yet-pitched-coloring                                           %! baca.SegmentMaker._color_not_yet_pitched():NOT_YET_PITCHED_COLORING
                            b'4.                                                                     %! baca.make_notes()
                            - \tweak color #(x11-color 'blue)                                        %! EXPLICIT_DYNAMIC_COLOR:_treat_persistent_wrapper(1)
                            \sfz                                                                     %! baca.dynamic():baca.IndicatorCommand._call():baca.SegmentMaker._set_status_tag():EXPLICIT_DYNAMIC
            <BLANKLINE>
                            % [Music_Voice measure 2]                                                %! baca.SegmentMaker._comment_measure_numbers()
                        %@% \baca-not-yet-pitched-coloring                                           %! baca.SegmentMaker._color_not_yet_pitched():NOT_YET_PITCHED_COLORING
                            b'4.                                                                     %! baca.make_notes()
                            - \tweak color #(x11-color 'blue)                                        %! EXPLICIT_DYNAMIC_COLOR:_treat_persistent_wrapper(1)
                            \sfz                                                                     %! baca.dynamic():baca.IndicatorCommand._call():baca.SegmentMaker._set_status_tag():EXPLICIT_DYNAMIC
            <BLANKLINE>
                            <<                                                                       %! baca.SegmentMaker._make_multimeasure_rest_container(7):PHANTOM
            <BLANKLINE>
                                \context Voice = "Music_Voice"                                       %! baca.SegmentMaker._make_multimeasure_rest_container(4):PHANTOM
                                {                                                                    %! baca.SegmentMaker._make_multimeasure_rest_container(4):PHANTOM
            <BLANKLINE>
                                    % [Music_Voice measure 3]                                        %! baca.SegmentMaker._comment_measure_numbers():baca.SegmentMaker._style_phantom_measures(5):PHANTOM
                                    \abjad-invisible-music-coloring                                  %! baca.SegmentMaker._make_multimeasure_rest_container(2):PHANTOM:NOTE:INVISIBLE_MUSIC_COLORING:baca.SegmentMaker._style_phantom_measures(5)
                                %@% \abjad-invisible-music                                           %! baca.SegmentMaker._make_multimeasure_rest_container(3):PHANTOM:NOTE:INVISIBLE_MUSIC_COMMAND:baca.SegmentMaker._style_phantom_measures(5)
                                %@% \baca-not-yet-pitched-coloring                                   %! baca.SegmentMaker._color_not_yet_pitched():NOT_YET_PITCHED_COLORING:HIDDEN:NOTE:baca.SegmentMaker._style_phantom_measures(5):PHANTOM
                                    b'1 * 1/4                                                        %! baca.SegmentMaker._make_multimeasure_rest_container(1):PHANTOM:HIDDEN:NOTE
                                %@% ^ \baca-duration-multiplier-markup #"1" #"4"                     %! baca.SegmentMaker._label_duration_multipliers():DURATION_MULTIPLIER:HIDDEN:NOTE:PHANTOM:baca.SegmentMaker._style_phantom_measures(5)
            <BLANKLINE>
                                }                                                                    %! baca.SegmentMaker._make_multimeasure_rest_container(4):PHANTOM
            <BLANKLINE>
                                \context Voice = "Rest_Voice"                                        %! baca.SegmentMaker._make_multimeasure_rest_container(6):PHANTOM
                                {                                                                    %! baca.SegmentMaker._make_multimeasure_rest_container(6):PHANTOM
            <BLANKLINE>
                                    % [Rest_Voice measure 3]                                         %! baca.SegmentMaker._comment_measure_numbers():baca.SegmentMaker._style_phantom_measures(5):PHANTOM
                                    \once \override Score.TimeSignature.X-extent = ##f               %! baca.SegmentMaker._style_phantom_measures(6):PHANTOM
                                    \once \override MultiMeasureRest.transparent = ##t               %! baca.SegmentMaker._style_phantom_measures(7):PHANTOM
                                    \stopStaff                                                       %! baca.SegmentMaker._style_phantom_measures(8):PHANTOM
                                    \once \override Staff.StaffSymbol.transparent = ##t              %! baca.SegmentMaker._style_phantom_measures(8):PHANTOM
                                    \startStaff                                                      %! baca.SegmentMaker._style_phantom_measures(8):PHANTOM
                                    R1 * 1/4                                                         %! baca.SegmentMaker._make_multimeasure_rest_container(5):PHANTOM:REST_VOICE:MULTIMEASURE_REST
                                %@% ^ \baca-duration-multiplier-markup #"1" #"4"                     %! baca.SegmentMaker._label_duration_multipliers():DURATION_MULTIPLIER:MULTIMEASURE_REST:PHANTOM:REST_VOICE:baca.SegmentMaker._style_phantom_measures(5)
            <BLANKLINE>
                                }                                                                    %! baca.SegmentMaker._make_multimeasure_rest_container(6):PHANTOM
            <BLANKLINE>
                            >>                                                                       %! baca.SegmentMaker._make_multimeasure_rest_container(7):PHANTOM
            <BLANKLINE>
                        }                                                                            %! baca.SingleStaffScoreTemplate.__call__()
            <BLANKLINE>
                    }                                                                                %! baca.SingleStaffScoreTemplate.__call__()
            <BLANKLINE>
                >>                                                                                   %! baca.SingleStaffScoreTemplate.__call__()
            <BLANKLINE>
            >>                                                                                       %! baca.SingleStaffScoreTemplate.__call__()

        Even at the beginning of a segment:

        >>> maker = baca.SegmentMaker(
        ...     deactivate=[abjad.tags.NOT_YET_PITCHED_COLORING],
        ...     score_template=baca.SingleStaffScoreTemplate(),
        ...     spacing=baca.minimum_duration((1, 24)),
        ...     time_signatures=[(3, 8), (3, 8)],
        ...     )
        >>> maker(
        ...     'Music_Voice',
        ...     baca.make_notes(),
        ...     baca.dynamic('sfz'),
        ...     )

        >>> metadata, persist = {}, {}
        >>> persist['persistent_indicators'] = {}
        >>> persist['persistent_indicators']['Music_Voice'] = [
        ...     abjad.Momento(
        ...         context='Music_Voice',
        ...         prototype='abjad.Dynamic',
        ...         value='sfz',
        ...         )
        ...     ]
        >>> metadata['segment_number'] = 1
        >>> lilypond_file = maker.run(
        ...     environment='docs',
        ...     previous_metadata=metadata,
        ...     previous_persist=persist,
        ...     )
        >>> block = abjad.Block(name='layout')
        >>> block.indent = 0
        >>> lilypond_file.items.insert(0, block)
        >>> abjad.show(lilypond_file, strict=89) # doctest: +SKIP

        ..  docs::

            >>> abjad.f(lilypond_file[abjad.Score], strict=89)
            <BLANKLINE>
            \context Score = "Score"                                                                 %! baca.SingleStaffScoreTemplate.__call__()
            <<                                                                                       %! baca.SingleStaffScoreTemplate.__call__()
            <BLANKLINE>
                \context GlobalContext = "Global_Context"                                            %! abjad.ScoreTemplate._make_global_context()
                <<                                                                                   %! abjad.ScoreTemplate._make_global_context()
            <BLANKLINE>
                    \context GlobalSkips = "Global_Skips"                                            %! abjad.ScoreTemplate._make_global_context()
                    {                                                                                %! abjad.ScoreTemplate._make_global_context()
            <BLANKLINE>
                        % [Global_Skips measure 1]                                                   %! baca.SegmentMaker._comment_measure_numbers()
                        \baca-new-spacing-section #1 #24                                             %! SPACING_COMMAND:baca.HorizontalSpacingSpecifier.__call__(1)
                        \time 3/8                                                                    %! baca.SegmentMaker._make_global_skips(2):baca.SegmentMaker._set_status_tag():EXPLICIT_TIME_SIGNATURE
                        \bar ""                                                                      %! EMPTY_START_BAR:+SEGMENT:baca.SegmentMaker._make_global_skips(4)
                        \baca-time-signature-color #'blue                                            %! baca.SegmentMaker._attach_color_literal(2):EXPLICIT_TIME_SIGNATURE_COLOR
                        s1 * 3/8                                                                     %! baca.SegmentMaker._make_global_skips(1)
            <BLANKLINE>
                        % [Global_Skips measure 2]                                                   %! baca.SegmentMaker._comment_measure_numbers()
                        \baca-new-spacing-section #1 #24                                             %! SPACING_COMMAND:baca.HorizontalSpacingSpecifier.__call__(1)
                        s1 * 3/8                                                                     %! baca.SegmentMaker._make_global_skips(1)
            <BLANKLINE>
                        % [Global_Skips measure 3]                                                   %! baca.SegmentMaker._comment_measure_numbers():baca.SegmentMaker._style_phantom_measures(1):PHANTOM
                        \baca-new-spacing-section #1 #4                                              %! SPACING_COMMAND:baca.HorizontalSpacingSpecifier.__call__(1):baca.SegmentMaker._style_phantom_measures(1):PHANTOM
                        \time 1/4                                                                    %! baca.SegmentMaker._make_global_skips(3):PHANTOM:baca.SegmentMaker._set_status_tag():EXPLICIT_TIME_SIGNATURE:baca.SegmentMaker._style_phantom_measures(1)
                        \baca-time-signature-transparent                                             %! baca.SegmentMaker._style_phantom_measures(2):PHANTOM
                        s1 * 1/4                                                                     %! baca.SegmentMaker._make_global_skips(3):PHANTOM
                        \once \override Score.BarLine.transparent = ##t                              %! baca.SegmentMaker._style_phantom_measures(3):PHANTOM
                        \once \override Score.SpanBar.transparent = ##t                              %! baca.SegmentMaker._style_phantom_measures(3):PHANTOM
            <BLANKLINE>
                    }                                                                                %! abjad.ScoreTemplate._make_global_context()
            <BLANKLINE>
                >>                                                                                   %! abjad.ScoreTemplate._make_global_context()
            <BLANKLINE>
                \context MusicContext = "Music_Context"                                              %! baca.SingleStaffScoreTemplate.__call__()
                <<                                                                                   %! baca.SingleStaffScoreTemplate.__call__()
            <BLANKLINE>
                    \context Staff = "Music_Staff"                                                   %! baca.SingleStaffScoreTemplate.__call__()
                    {                                                                                %! baca.SingleStaffScoreTemplate.__call__()
            <BLANKLINE>
                        \context Voice = "Music_Voice"                                               %! baca.SingleStaffScoreTemplate.__call__()
                        {                                                                            %! baca.SingleStaffScoreTemplate.__call__()
            <BLANKLINE>
                            % [Music_Voice measure 1]                                                %! baca.SegmentMaker._comment_measure_numbers()
                        %@% \baca-not-yet-pitched-coloring                                           %! baca.SegmentMaker._color_not_yet_pitched():NOT_YET_PITCHED_COLORING
                            b'4.                                                                     %! baca.make_notes()
                            - \tweak color #(x11-color 'blue)                                        %! EXPLICIT_DYNAMIC_COLOR:_treat_persistent_wrapper(1)
                            \sfz                                                                     %! baca.dynamic():baca.IndicatorCommand._call():baca.SegmentMaker._set_status_tag():EXPLICIT_DYNAMIC
            <BLANKLINE>
                            % [Music_Voice measure 2]                                                %! baca.SegmentMaker._comment_measure_numbers()
                        %@% \baca-not-yet-pitched-coloring                                           %! baca.SegmentMaker._color_not_yet_pitched():NOT_YET_PITCHED_COLORING
                            b'4.                                                                     %! baca.make_notes()
            <BLANKLINE>
                            <<                                                                       %! baca.SegmentMaker._make_multimeasure_rest_container(7):PHANTOM
            <BLANKLINE>
                                \context Voice = "Music_Voice"                                       %! baca.SegmentMaker._make_multimeasure_rest_container(4):PHANTOM
                                {                                                                    %! baca.SegmentMaker._make_multimeasure_rest_container(4):PHANTOM
            <BLANKLINE>
                                    % [Music_Voice measure 3]                                        %! baca.SegmentMaker._comment_measure_numbers():baca.SegmentMaker._style_phantom_measures(5):PHANTOM
                                    \abjad-invisible-music-coloring                                  %! baca.SegmentMaker._make_multimeasure_rest_container(2):PHANTOM:NOTE:INVISIBLE_MUSIC_COLORING:baca.SegmentMaker._style_phantom_measures(5)
                                %@% \abjad-invisible-music                                           %! baca.SegmentMaker._make_multimeasure_rest_container(3):PHANTOM:NOTE:INVISIBLE_MUSIC_COMMAND:baca.SegmentMaker._style_phantom_measures(5)
                                %@% \baca-not-yet-pitched-coloring                                   %! baca.SegmentMaker._color_not_yet_pitched():NOT_YET_PITCHED_COLORING:HIDDEN:NOTE:baca.SegmentMaker._style_phantom_measures(5):PHANTOM
                                    b'1 * 1/4                                                        %! baca.SegmentMaker._make_multimeasure_rest_container(1):PHANTOM:HIDDEN:NOTE
                                %@% ^ \baca-duration-multiplier-markup #"1" #"4"                     %! baca.SegmentMaker._label_duration_multipliers():DURATION_MULTIPLIER:HIDDEN:NOTE:PHANTOM:baca.SegmentMaker._style_phantom_measures(5)
            <BLANKLINE>
                                }                                                                    %! baca.SegmentMaker._make_multimeasure_rest_container(4):PHANTOM
            <BLANKLINE>
                                \context Voice = "Rest_Voice"                                        %! baca.SegmentMaker._make_multimeasure_rest_container(6):PHANTOM
                                {                                                                    %! baca.SegmentMaker._make_multimeasure_rest_container(6):PHANTOM
            <BLANKLINE>
                                    % [Rest_Voice measure 3]                                         %! baca.SegmentMaker._comment_measure_numbers():baca.SegmentMaker._style_phantom_measures(5):PHANTOM
                                    \once \override Score.TimeSignature.X-extent = ##f               %! baca.SegmentMaker._style_phantom_measures(6):PHANTOM
                                    \once \override MultiMeasureRest.transparent = ##t               %! baca.SegmentMaker._style_phantom_measures(7):PHANTOM
                                    \stopStaff                                                       %! baca.SegmentMaker._style_phantom_measures(8):PHANTOM
                                    \once \override Staff.StaffSymbol.transparent = ##t              %! baca.SegmentMaker._style_phantom_measures(8):PHANTOM
                                    \startStaff                                                      %! baca.SegmentMaker._style_phantom_measures(8):PHANTOM
                                    R1 * 1/4                                                         %! baca.SegmentMaker._make_multimeasure_rest_container(5):PHANTOM:REST_VOICE:MULTIMEASURE_REST
                                %@% ^ \baca-duration-multiplier-markup #"1" #"4"                     %! baca.SegmentMaker._label_duration_multipliers():DURATION_MULTIPLIER:MULTIMEASURE_REST:PHANTOM:REST_VOICE:baca.SegmentMaker._style_phantom_measures(5)
            <BLANKLINE>
                                }                                                                    %! baca.SegmentMaker._make_multimeasure_rest_container(6):PHANTOM
            <BLANKLINE>
                            >>                                                                       %! baca.SegmentMaker._make_multimeasure_rest_container(7):PHANTOM
            <BLANKLINE>
                        }                                                                            %! baca.SingleStaffScoreTemplate.__call__()
            <BLANKLINE>
                    }                                                                                %! baca.SingleStaffScoreTemplate.__call__()
            <BLANKLINE>
                >>                                                                                   %! baca.SingleStaffScoreTemplate.__call__()
            <BLANKLINE>
            >>                                                                                       %! baca.SingleStaffScoreTemplate.__call__()

    ..  container:: example

        REGRESSION. Conventional and effort dynamics analyze
        nonredundantly:

        >>> maker = baca.SegmentMaker(
        ...     deactivate=[abjad.tags.NOT_YET_PITCHED_COLORING],
        ...     score_template=baca.SingleStaffScoreTemplate(),
        ...     spacing=baca.minimum_duration((1, 24)),
        ...     time_signatures=[(3, 8), (3, 8)],
        ...     )
        >>> maker(
        ...     'Music_Voice',
        ...     baca.make_notes(),
        ...     baca.dynamic('mf'),
        ...     baca.dynamic('"mf"', selector=baca.leaf(1)),
        ...     )

        >>> lilypond_file = maker.run(environment='docs')
        >>> block = abjad.Block(name='layout')
        >>> block.indent = 0
        >>> lilypond_file.items.insert(0, block)
        >>> abjad.show(lilypond_file, strict=89) # doctest: +SKIP

        ..  docs::

            >>> abjad.f(lilypond_file[abjad.Score], strict=89)
            <BLANKLINE>
            \context Score = "Score"                                                                 %! baca.SingleStaffScoreTemplate.__call__()
            <<                                                                                       %! baca.SingleStaffScoreTemplate.__call__()
            <BLANKLINE>
                \context GlobalContext = "Global_Context"                                            %! abjad.ScoreTemplate._make_global_context()
                <<                                                                                   %! abjad.ScoreTemplate._make_global_context()
            <BLANKLINE>
                    \context GlobalSkips = "Global_Skips"                                            %! abjad.ScoreTemplate._make_global_context()
                    {                                                                                %! abjad.ScoreTemplate._make_global_context()
            <BLANKLINE>
                        % [Global_Skips measure 1]                                                   %! baca.SegmentMaker._comment_measure_numbers()
                        \baca-new-spacing-section #1 #24                                             %! SPACING_COMMAND:baca.HorizontalSpacingSpecifier.__call__(1)
                        \time 3/8                                                                    %! baca.SegmentMaker._make_global_skips(2):baca.SegmentMaker._set_status_tag():EXPLICIT_TIME_SIGNATURE
                        \baca-time-signature-color #'blue                                            %! baca.SegmentMaker._attach_color_literal(2):EXPLICIT_TIME_SIGNATURE_COLOR
                        s1 * 3/8                                                                     %! baca.SegmentMaker._make_global_skips(1)
            <BLANKLINE>
                        % [Global_Skips measure 2]                                                   %! baca.SegmentMaker._comment_measure_numbers()
                        \baca-new-spacing-section #1 #24                                             %! SPACING_COMMAND:baca.HorizontalSpacingSpecifier.__call__(1)
                        s1 * 3/8                                                                     %! baca.SegmentMaker._make_global_skips(1)
            <BLANKLINE>
                        % [Global_Skips measure 3]                                                   %! baca.SegmentMaker._comment_measure_numbers():baca.SegmentMaker._style_phantom_measures(1):PHANTOM
                        \baca-new-spacing-section #1 #4                                              %! SPACING_COMMAND:baca.HorizontalSpacingSpecifier.__call__(1):baca.SegmentMaker._style_phantom_measures(1):PHANTOM
                        \time 1/4                                                                    %! baca.SegmentMaker._make_global_skips(3):PHANTOM:baca.SegmentMaker._set_status_tag():EXPLICIT_TIME_SIGNATURE:baca.SegmentMaker._style_phantom_measures(1)
                        \baca-time-signature-transparent                                             %! baca.SegmentMaker._style_phantom_measures(2):PHANTOM
                        s1 * 1/4                                                                     %! baca.SegmentMaker._make_global_skips(3):PHANTOM
                        \once \override Score.BarLine.transparent = ##t                              %! baca.SegmentMaker._style_phantom_measures(3):PHANTOM
                        \once \override Score.SpanBar.transparent = ##t                              %! baca.SegmentMaker._style_phantom_measures(3):PHANTOM
            <BLANKLINE>
                    }                                                                                %! abjad.ScoreTemplate._make_global_context()
            <BLANKLINE>
                >>                                                                                   %! abjad.ScoreTemplate._make_global_context()
            <BLANKLINE>
                \context MusicContext = "Music_Context"                                              %! baca.SingleStaffScoreTemplate.__call__()
                <<                                                                                   %! baca.SingleStaffScoreTemplate.__call__()
            <BLANKLINE>
                    \context Staff = "Music_Staff"                                                   %! baca.SingleStaffScoreTemplate.__call__()
                    {                                                                                %! baca.SingleStaffScoreTemplate.__call__()
            <BLANKLINE>
                        \context Voice = "Music_Voice"                                               %! baca.SingleStaffScoreTemplate.__call__()
                        {                                                                            %! baca.SingleStaffScoreTemplate.__call__()
            <BLANKLINE>
                            % [Music_Voice measure 1]                                                %! baca.SegmentMaker._comment_measure_numbers()
                        %@% \baca-not-yet-pitched-coloring                                           %! baca.SegmentMaker._color_not_yet_pitched():NOT_YET_PITCHED_COLORING
                            b'4.                                                                     %! baca.make_notes()
                            - \tweak color #(x11-color 'blue)                                        %! EXPLICIT_DYNAMIC_COLOR:_treat_persistent_wrapper(1)
                            \mf                                                                      %! baca.dynamic():baca.IndicatorCommand._call():baca.SegmentMaker._set_status_tag():EXPLICIT_DYNAMIC
            <BLANKLINE>
                            % [Music_Voice measure 2]                                                %! baca.SegmentMaker._comment_measure_numbers()
                        %@% \baca-not-yet-pitched-coloring                                           %! baca.SegmentMaker._color_not_yet_pitched():NOT_YET_PITCHED_COLORING
                            b'4.                                                                     %! baca.make_notes()
                            - \tweak color #(x11-color 'blue)                                        %! EXPLICIT_DYNAMIC_COLOR:_treat_persistent_wrapper(1)
                            \baca-effort-mf                                                          %! baca.dynamic():baca.IndicatorCommand._call():baca.SegmentMaker._set_status_tag():EXPLICIT_DYNAMIC
            <BLANKLINE>
                            <<                                                                       %! baca.SegmentMaker._make_multimeasure_rest_container(7):PHANTOM
            <BLANKLINE>
                                \context Voice = "Music_Voice"                                       %! baca.SegmentMaker._make_multimeasure_rest_container(4):PHANTOM
                                {                                                                    %! baca.SegmentMaker._make_multimeasure_rest_container(4):PHANTOM
            <BLANKLINE>
                                    % [Music_Voice measure 3]                                        %! baca.SegmentMaker._comment_measure_numbers():baca.SegmentMaker._style_phantom_measures(5):PHANTOM
                                    \abjad-invisible-music-coloring                                  %! baca.SegmentMaker._make_multimeasure_rest_container(2):PHANTOM:NOTE:INVISIBLE_MUSIC_COLORING:baca.SegmentMaker._style_phantom_measures(5)
                                %@% \abjad-invisible-music                                           %! baca.SegmentMaker._make_multimeasure_rest_container(3):PHANTOM:NOTE:INVISIBLE_MUSIC_COMMAND:baca.SegmentMaker._style_phantom_measures(5)
                                %@% \baca-not-yet-pitched-coloring                                   %! baca.SegmentMaker._color_not_yet_pitched():NOT_YET_PITCHED_COLORING:HIDDEN:NOTE:baca.SegmentMaker._style_phantom_measures(5):PHANTOM
                                    b'1 * 1/4                                                        %! baca.SegmentMaker._make_multimeasure_rest_container(1):PHANTOM:HIDDEN:NOTE
                                %@% ^ \baca-duration-multiplier-markup #"1" #"4"                     %! baca.SegmentMaker._label_duration_multipliers():DURATION_MULTIPLIER:HIDDEN:NOTE:PHANTOM:baca.SegmentMaker._style_phantom_measures(5)
            <BLANKLINE>
                                }                                                                    %! baca.SegmentMaker._make_multimeasure_rest_container(4):PHANTOM
            <BLANKLINE>
                                \context Voice = "Rest_Voice"                                        %! baca.SegmentMaker._make_multimeasure_rest_container(6):PHANTOM
                                {                                                                    %! baca.SegmentMaker._make_multimeasure_rest_container(6):PHANTOM
            <BLANKLINE>
                                    % [Rest_Voice measure 3]                                         %! baca.SegmentMaker._comment_measure_numbers():baca.SegmentMaker._style_phantom_measures(5):PHANTOM
                                    \once \override Score.TimeSignature.X-extent = ##f               %! baca.SegmentMaker._style_phantom_measures(6):PHANTOM
                                    \once \override MultiMeasureRest.transparent = ##t               %! baca.SegmentMaker._style_phantom_measures(7):PHANTOM
                                    \stopStaff                                                       %! baca.SegmentMaker._style_phantom_measures(8):PHANTOM
                                    \once \override Staff.StaffSymbol.transparent = ##t              %! baca.SegmentMaker._style_phantom_measures(8):PHANTOM
                                    \startStaff                                                      %! baca.SegmentMaker._style_phantom_measures(8):PHANTOM
                                    R1 * 1/4                                                         %! baca.SegmentMaker._make_multimeasure_rest_container(5):PHANTOM:REST_VOICE:MULTIMEASURE_REST
                                %@% ^ \baca-duration-multiplier-markup #"1" #"4"                     %! baca.SegmentMaker._label_duration_multipliers():DURATION_MULTIPLIER:MULTIMEASURE_REST:PHANTOM:REST_VOICE:baca.SegmentMaker._style_phantom_measures(5)
            <BLANKLINE>
                                }                                                                    %! baca.SegmentMaker._make_multimeasure_rest_container(6):PHANTOM
            <BLANKLINE>
                            >>                                                                       %! baca.SegmentMaker._make_multimeasure_rest_container(7):PHANTOM
            <BLANKLINE>
                        }                                                                            %! baca.SingleStaffScoreTemplate.__call__()
            <BLANKLINE>
                    }                                                                                %! baca.SingleStaffScoreTemplate.__call__()
            <BLANKLINE>
                >>                                                                                   %! baca.SingleStaffScoreTemplate.__call__()
            <BLANKLINE>
            >>                                                                                       %! baca.SingleStaffScoreTemplate.__call__()

..  container:: example

    Instruments.

    ..  container:: example

        Example instruments:

        >>> instruments = abjad.OrderedDict()
        >>> instruments['Flute'] = abjad.Flute()
        >>> instruments['Piccolo'] = abjad.Piccolo()
        >>> breaks = baca.breaks(
        ...     baca.page(
        ...         [1, 0, (11,)],
        ...         [2, 15, (11,)],
        ...         ),
        ...     )

    ..  container:: example

        Default instruments color purple and redraw dull purple:

        >>> score_template = baca.SingleStaffScoreTemplate()
        >>> triple = ('Music_Staff', 'default_instrument', abjad.Flute())
        >>> score_template.defaults.append(triple)
        >>> maker = baca.SegmentMaker(
        ...     breaks=breaks,
        ...     deactivate=[abjad.tags.NOT_YET_PITCHED_COLORING],
        ...     instruments=instruments,
        ...     score_template=score_template,
        ...     spacing=baca.minimum_duration((1, 24)),
        ...     time_signatures=[(3, 8), (3, 8)],
        ...     )
        >>> maker(
        ...     'Music_Voice',
        ...     baca.make_notes(),
        ...     )

        >>> lilypond_file = maker.run(environment='docs')
        >>> block = abjad.Block(name='layout')
        >>> block.indent = 0
        >>> lilypond_file.items.insert(0, block)
        >>> abjad.show(lilypond_file, strict=89) # doctest: +SKIP

        ..  docs::

            >>> abjad.f(lilypond_file[abjad.Score], strict=89)
            <BLANKLINE>
            \context Score = "Score"                                                                 %! baca.SingleStaffScoreTemplate.__call__()
            <<                                                                                       %! baca.SingleStaffScoreTemplate.__call__()
            <BLANKLINE>
                \context GlobalContext = "Global_Context"                                            %! abjad.ScoreTemplate._make_global_context()
                <<                                                                                   %! abjad.ScoreTemplate._make_global_context()
            <BLANKLINE>
                    \context GlobalSkips = "Global_Skips"                                            %! abjad.ScoreTemplate._make_global_context()
                    {                                                                                %! abjad.ScoreTemplate._make_global_context()
            <BLANKLINE>
                        % [Global_Skips measure 1]                                                   %! baca.SegmentMaker._comment_measure_numbers()
                        \baca-new-spacing-section #1 #24                                             %! SPACING_COMMAND:baca.HorizontalSpacingSpecifier.__call__(1)
                        \autoPageBreaksOff                                                           %! BREAK:baca.BreakMeasureMap.__call__(1)
                        \noBreak                                                                     %! BREAK:baca.BreakMeasureMap.__call__(2)
                        \baca-lbsd #0 #'(11)                                                         %! BREAK:baca.IndicatorCommand._call()
                        \time 3/8                                                                    %! baca.SegmentMaker._make_global_skips(2):baca.SegmentMaker._set_status_tag():EXPLICIT_TIME_SIGNATURE
                        \baca-time-signature-color #'blue                                            %! baca.SegmentMaker._attach_color_literal(2):EXPLICIT_TIME_SIGNATURE_COLOR
                        \pageBreak                                                                   %! BREAK:baca.IndicatorCommand._call()
                        s1 * 3/8                                                                     %! baca.SegmentMaker._make_global_skips(1)
            <BLANKLINE>
                        % [Global_Skips measure 2]                                                   %! baca.SegmentMaker._comment_measure_numbers()
                        \baca-new-spacing-section #1 #24                                             %! SPACING_COMMAND:baca.HorizontalSpacingSpecifier.__call__(1)
                        \noBreak                                                                     %! BREAK:baca.BreakMeasureMap.__call__(2)
                        \baca-lbsd #15 #'(11)                                                        %! BREAK:baca.IndicatorCommand._call()
                        \break                                                                       %! BREAK:baca.IndicatorCommand._call()
                        s1 * 3/8                                                                     %! baca.SegmentMaker._make_global_skips(1)
            <BLANKLINE>
                        % [Global_Skips measure 3]                                                   %! baca.SegmentMaker._comment_measure_numbers():baca.SegmentMaker._style_phantom_measures(1):PHANTOM
                        \baca-new-spacing-section #1 #4                                              %! SPACING_COMMAND:baca.HorizontalSpacingSpecifier.__call__(1):baca.SegmentMaker._style_phantom_measures(1):PHANTOM
                        \noBreak                                                                     %! BREAK:baca.BreakMeasureMap.__call__(2):baca.SegmentMaker._style_phantom_measures(1):PHANTOM
                        \time 1/4                                                                    %! baca.SegmentMaker._make_global_skips(3):PHANTOM:baca.SegmentMaker._set_status_tag():EXPLICIT_TIME_SIGNATURE:baca.SegmentMaker._style_phantom_measures(1)
                        \baca-time-signature-transparent                                             %! baca.SegmentMaker._style_phantom_measures(2):PHANTOM
                        s1 * 1/4                                                                     %! baca.SegmentMaker._make_global_skips(3):PHANTOM
                        \once \override Score.BarLine.transparent = ##t                              %! baca.SegmentMaker._style_phantom_measures(3):PHANTOM
                        \once \override Score.SpanBar.transparent = ##t                              %! baca.SegmentMaker._style_phantom_measures(3):PHANTOM
            <BLANKLINE>
                    }                                                                                %! abjad.ScoreTemplate._make_global_context()
            <BLANKLINE>
                >>                                                                                   %! abjad.ScoreTemplate._make_global_context()
            <BLANKLINE>
                \context MusicContext = "Music_Context"                                              %! baca.SingleStaffScoreTemplate.__call__()
                <<                                                                                   %! baca.SingleStaffScoreTemplate.__call__()
            <BLANKLINE>
                    \context Staff = "Music_Staff"                                                   %! baca.SingleStaffScoreTemplate.__call__()
                    {                                                                                %! baca.SingleStaffScoreTemplate.__call__()
            <BLANKLINE>
                        \context Voice = "Music_Voice"                                               %! baca.SingleStaffScoreTemplate.__call__()
                        {                                                                            %! baca.SingleStaffScoreTemplate.__call__()
            <BLANKLINE>
                            % [Music_Voice measure 1]                                                %! baca.SegmentMaker._comment_measure_numbers()
                        %@% \baca-not-yet-pitched-coloring                                           %! baca.SegmentMaker._color_not_yet_pitched():NOT_YET_PITCHED_COLORING
                            b'4.                                                                     %! baca.make_notes()
                            ^ \baca-default-indicator-markup "(“Flute”)"                             %! DEFAULT_INSTRUMENT_ALERT:baca.SegmentMaker._attach_latent_indicator_alert()
            <BLANKLINE>
                            % [Music_Voice measure 2]                                                %! baca.SegmentMaker._comment_measure_numbers()
                        %@% \baca-not-yet-pitched-coloring                                           %! baca.SegmentMaker._color_not_yet_pitched():NOT_YET_PITCHED_COLORING
                            b'4.                                                                     %! baca.make_notes()
            <BLANKLINE>
                            <<                                                                       %! baca.SegmentMaker._make_multimeasure_rest_container(7):PHANTOM
            <BLANKLINE>
                                \context Voice = "Music_Voice"                                       %! baca.SegmentMaker._make_multimeasure_rest_container(4):PHANTOM
                                {                                                                    %! baca.SegmentMaker._make_multimeasure_rest_container(4):PHANTOM
            <BLANKLINE>
                                    % [Music_Voice measure 3]                                        %! baca.SegmentMaker._comment_measure_numbers():baca.SegmentMaker._style_phantom_measures(5):PHANTOM
                                    \abjad-invisible-music-coloring                                  %! baca.SegmentMaker._make_multimeasure_rest_container(2):PHANTOM:NOTE:INVISIBLE_MUSIC_COLORING:baca.SegmentMaker._style_phantom_measures(5)
                                %@% \abjad-invisible-music                                           %! baca.SegmentMaker._make_multimeasure_rest_container(3):PHANTOM:NOTE:INVISIBLE_MUSIC_COMMAND:baca.SegmentMaker._style_phantom_measures(5)
                                %@% \baca-not-yet-pitched-coloring                                   %! baca.SegmentMaker._color_not_yet_pitched():NOT_YET_PITCHED_COLORING:HIDDEN:NOTE:baca.SegmentMaker._style_phantom_measures(5):PHANTOM
                                    b'1 * 1/4                                                        %! baca.SegmentMaker._make_multimeasure_rest_container(1):PHANTOM:HIDDEN:NOTE
                                %@% ^ \baca-duration-multiplier-markup #"1" #"4"                     %! baca.SegmentMaker._label_duration_multipliers():DURATION_MULTIPLIER:HIDDEN:NOTE:PHANTOM:baca.SegmentMaker._style_phantom_measures(5)
            <BLANKLINE>
                                }                                                                    %! baca.SegmentMaker._make_multimeasure_rest_container(4):PHANTOM
            <BLANKLINE>
                                \context Voice = "Rest_Voice"                                        %! baca.SegmentMaker._make_multimeasure_rest_container(6):PHANTOM
                                {                                                                    %! baca.SegmentMaker._make_multimeasure_rest_container(6):PHANTOM
            <BLANKLINE>
                                    % [Rest_Voice measure 3]                                         %! baca.SegmentMaker._comment_measure_numbers():baca.SegmentMaker._style_phantom_measures(5):PHANTOM
                                    \once \override Score.TimeSignature.X-extent = ##f               %! baca.SegmentMaker._style_phantom_measures(6):PHANTOM
                                    \once \override MultiMeasureRest.transparent = ##t               %! baca.SegmentMaker._style_phantom_measures(7):PHANTOM
                                    \stopStaff                                                       %! baca.SegmentMaker._style_phantom_measures(8):PHANTOM
                                    \once \override Staff.StaffSymbol.transparent = ##t              %! baca.SegmentMaker._style_phantom_measures(8):PHANTOM
                                    \startStaff                                                      %! baca.SegmentMaker._style_phantom_measures(8):PHANTOM
                                    R1 * 1/4                                                         %! baca.SegmentMaker._make_multimeasure_rest_container(5):PHANTOM:REST_VOICE:MULTIMEASURE_REST
                                %@% ^ \baca-duration-multiplier-markup #"1" #"4"                     %! baca.SegmentMaker._label_duration_multipliers():DURATION_MULTIPLIER:MULTIMEASURE_REST:PHANTOM:REST_VOICE:baca.SegmentMaker._style_phantom_measures(5)
            <BLANKLINE>
                                }                                                                    %! baca.SegmentMaker._make_multimeasure_rest_container(6):PHANTOM
            <BLANKLINE>
                            >>                                                                       %! baca.SegmentMaker._make_multimeasure_rest_container(7):PHANTOM
            <BLANKLINE>
                        }                                                                            %! baca.SingleStaffScoreTemplate.__call__()
            <BLANKLINE>
                    }                                                                                %! baca.SingleStaffScoreTemplate.__call__()
            <BLANKLINE>
                >>                                                                                   %! baca.SingleStaffScoreTemplate.__call__()
            <BLANKLINE>
            >>                                                                                       %! baca.SingleStaffScoreTemplate.__call__()

        >>> score = lilypond_file[abjad.Score]
        >>> text = format(score, 'lilypond')
        >>> text = abjad.LilyPondFormatManager.left_shift_tags(text)
        >>> tags_ = abjad.tags.instrument_color_tags()
        >>> match = lambda tags: bool(set(tags) & set(tags_))
        >>> text, count = abjad.deactivate(text, match)
        >>> text = abjad.LilyPondFormatManager.left_shift_tags(text, 89)
        >>> lines = [_.strip('\n') for _ in text.split('\n')]
        >>> lilypond_file.score_block.items[:] = lines
        >>> abjad.show(lilypond_file, strict=89) # doctest: +SKIP

        ..  docs::

            >>> print(text)
            <BLANKLINE>
            \context Score = "Score"                                                                 %! baca.SingleStaffScoreTemplate.__call__()
            <<                                                                                       %! baca.SingleStaffScoreTemplate.__call__()
            <BLANKLINE>
                \context GlobalContext = "Global_Context"                                            %! abjad.ScoreTemplate._make_global_context()
                <<                                                                                   %! abjad.ScoreTemplate._make_global_context()
            <BLANKLINE>
                    \context GlobalSkips = "Global_Skips"                                            %! abjad.ScoreTemplate._make_global_context()
                    {                                                                                %! abjad.ScoreTemplate._make_global_context()
            <BLANKLINE>
                        % [Global_Skips measure 1]                                                   %! baca.SegmentMaker._comment_measure_numbers()
                        \baca-new-spacing-section #1 #24                                             %! SPACING_COMMAND:baca.HorizontalSpacingSpecifier.__call__(1)
                        \autoPageBreaksOff                                                           %! BREAK:baca.BreakMeasureMap.__call__(1)
                        \noBreak                                                                     %! BREAK:baca.BreakMeasureMap.__call__(2)
                        \baca-lbsd #0 #'(11)                                                         %! BREAK:baca.IndicatorCommand._call()
                        \time 3/8                                                                    %! baca.SegmentMaker._make_global_skips(2):baca.SegmentMaker._set_status_tag():EXPLICIT_TIME_SIGNATURE
                        \baca-time-signature-color #'blue                                            %! baca.SegmentMaker._attach_color_literal(2):EXPLICIT_TIME_SIGNATURE_COLOR
                        \pageBreak                                                                   %! BREAK:baca.IndicatorCommand._call()
                        s1 * 3/8                                                                     %! baca.SegmentMaker._make_global_skips(1)
            <BLANKLINE>
                        % [Global_Skips measure 2]                                                   %! baca.SegmentMaker._comment_measure_numbers()
                        \baca-new-spacing-section #1 #24                                             %! SPACING_COMMAND:baca.HorizontalSpacingSpecifier.__call__(1)
                        \noBreak                                                                     %! BREAK:baca.BreakMeasureMap.__call__(2)
                        \baca-lbsd #15 #'(11)                                                        %! BREAK:baca.IndicatorCommand._call()
                        \break                                                                       %! BREAK:baca.IndicatorCommand._call()
                        s1 * 3/8                                                                     %! baca.SegmentMaker._make_global_skips(1)
            <BLANKLINE>
                        % [Global_Skips measure 3]                                                   %! baca.SegmentMaker._comment_measure_numbers():baca.SegmentMaker._style_phantom_measures(1):PHANTOM
                        \baca-new-spacing-section #1 #4                                              %! SPACING_COMMAND:baca.HorizontalSpacingSpecifier.__call__(1):baca.SegmentMaker._style_phantom_measures(1):PHANTOM
                        \noBreak                                                                     %! BREAK:baca.BreakMeasureMap.__call__(2):baca.SegmentMaker._style_phantom_measures(1):PHANTOM
                        \time 1/4                                                                    %! baca.SegmentMaker._make_global_skips(3):PHANTOM:baca.SegmentMaker._set_status_tag():EXPLICIT_TIME_SIGNATURE:baca.SegmentMaker._style_phantom_measures(1)
                        \baca-time-signature-transparent                                             %! baca.SegmentMaker._style_phantom_measures(2):PHANTOM
                        s1 * 1/4                                                                     %! baca.SegmentMaker._make_global_skips(3):PHANTOM
                        \once \override Score.BarLine.transparent = ##t                              %! baca.SegmentMaker._style_phantom_measures(3):PHANTOM
                        \once \override Score.SpanBar.transparent = ##t                              %! baca.SegmentMaker._style_phantom_measures(3):PHANTOM
            <BLANKLINE>
                    }                                                                                %! abjad.ScoreTemplate._make_global_context()
            <BLANKLINE>
                >>                                                                                   %! abjad.ScoreTemplate._make_global_context()
            <BLANKLINE>
                \context MusicContext = "Music_Context"                                              %! baca.SingleStaffScoreTemplate.__call__()
                <<                                                                                   %! baca.SingleStaffScoreTemplate.__call__()
            <BLANKLINE>
                    \context Staff = "Music_Staff"                                                   %! baca.SingleStaffScoreTemplate.__call__()
                    {                                                                                %! baca.SingleStaffScoreTemplate.__call__()
            <BLANKLINE>
                        \context Voice = "Music_Voice"                                               %! baca.SingleStaffScoreTemplate.__call__()
                        {                                                                            %! baca.SingleStaffScoreTemplate.__call__()
            <BLANKLINE>
                            % [Music_Voice measure 1]                                                %! baca.SegmentMaker._comment_measure_numbers()
                    %@% \baca-not-yet-pitched-coloring                                               %! baca.SegmentMaker._color_not_yet_pitched():NOT_YET_PITCHED_COLORING
                            b'4.                                                                     %! baca.make_notes()
                        %%% ^ \baca-default-indicator-markup "(“Flute”)"                             %! DEFAULT_INSTRUMENT_ALERT:baca.SegmentMaker._attach_latent_indicator_alert()
            <BLANKLINE>
                            % [Music_Voice measure 2]                                                %! baca.SegmentMaker._comment_measure_numbers()
                    %@% \baca-not-yet-pitched-coloring                                               %! baca.SegmentMaker._color_not_yet_pitched():NOT_YET_PITCHED_COLORING
                            b'4.                                                                     %! baca.make_notes()
            <BLANKLINE>
                            <<                                                                       %! baca.SegmentMaker._make_multimeasure_rest_container(7):PHANTOM
            <BLANKLINE>
                                \context Voice = "Music_Voice"                                       %! baca.SegmentMaker._make_multimeasure_rest_container(4):PHANTOM
                                {                                                                    %! baca.SegmentMaker._make_multimeasure_rest_container(4):PHANTOM
            <BLANKLINE>
                                    % [Music_Voice measure 3]                                        %! baca.SegmentMaker._comment_measure_numbers():baca.SegmentMaker._style_phantom_measures(5):PHANTOM
                                    \abjad-invisible-music-coloring                                  %! baca.SegmentMaker._make_multimeasure_rest_container(2):PHANTOM:NOTE:INVISIBLE_MUSIC_COLORING:baca.SegmentMaker._style_phantom_measures(5)
                            %@% \abjad-invisible-music                                               %! baca.SegmentMaker._make_multimeasure_rest_container(3):PHANTOM:NOTE:INVISIBLE_MUSIC_COMMAND:baca.SegmentMaker._style_phantom_measures(5)
                            %@% \baca-not-yet-pitched-coloring                                       %! baca.SegmentMaker._color_not_yet_pitched():NOT_YET_PITCHED_COLORING:HIDDEN:NOTE:baca.SegmentMaker._style_phantom_measures(5):PHANTOM
                                    b'1 * 1/4                                                        %! baca.SegmentMaker._make_multimeasure_rest_container(1):PHANTOM:HIDDEN:NOTE
                            %@% ^ \baca-duration-multiplier-markup #"1" #"4"                         %! baca.SegmentMaker._label_duration_multipliers():DURATION_MULTIPLIER:HIDDEN:NOTE:PHANTOM:baca.SegmentMaker._style_phantom_measures(5)
            <BLANKLINE>
                                }                                                                    %! baca.SegmentMaker._make_multimeasure_rest_container(4):PHANTOM
            <BLANKLINE>
                                \context Voice = "Rest_Voice"                                        %! baca.SegmentMaker._make_multimeasure_rest_container(6):PHANTOM
                                {                                                                    %! baca.SegmentMaker._make_multimeasure_rest_container(6):PHANTOM
            <BLANKLINE>
                                    % [Rest_Voice measure 3]                                         %! baca.SegmentMaker._comment_measure_numbers():baca.SegmentMaker._style_phantom_measures(5):PHANTOM
                                    \once \override Score.TimeSignature.X-extent = ##f               %! baca.SegmentMaker._style_phantom_measures(6):PHANTOM
                                    \once \override MultiMeasureRest.transparent = ##t               %! baca.SegmentMaker._style_phantom_measures(7):PHANTOM
                                    \stopStaff                                                       %! baca.SegmentMaker._style_phantom_measures(8):PHANTOM
                                    \once \override Staff.StaffSymbol.transparent = ##t              %! baca.SegmentMaker._style_phantom_measures(8):PHANTOM
                                    \startStaff                                                      %! baca.SegmentMaker._style_phantom_measures(8):PHANTOM
                                    R1 * 1/4                                                         %! baca.SegmentMaker._make_multimeasure_rest_container(5):PHANTOM:REST_VOICE:MULTIMEASURE_REST
                            %@% ^ \baca-duration-multiplier-markup #"1" #"4"                         %! baca.SegmentMaker._label_duration_multipliers():DURATION_MULTIPLIER:MULTIMEASURE_REST:PHANTOM:REST_VOICE:baca.SegmentMaker._style_phantom_measures(5)
            <BLANKLINE>
                                }                                                                    %! baca.SegmentMaker._make_multimeasure_rest_container(6):PHANTOM
            <BLANKLINE>
                            >>                                                                       %! baca.SegmentMaker._make_multimeasure_rest_container(7):PHANTOM
            <BLANKLINE>
                        }                                                                            %! baca.SingleStaffScoreTemplate.__call__()
            <BLANKLINE>
                    }                                                                                %! baca.SingleStaffScoreTemplate.__call__()
            <BLANKLINE>
                >>                                                                                   %! baca.SingleStaffScoreTemplate.__call__()
            <BLANKLINE>
            >>                                                                                       %! baca.SingleStaffScoreTemplate.__call__()

        >>> tags_ = abjad.tags.instrument_color_tags()
        >>> match = lambda tags: bool(set(tags) & set(tags_))
        >>> text, count = abjad.activate(text, match)
        >>> lines = [_.strip('\n') for _ in text.split('\n')]
        >>> lilypond_file.score_block.items[:] = lines
        >>> abjad.show(lilypond_file, strict=89) # doctest: +SKIP

        ..  docs::

            >>> print(text)
            <BLANKLINE>
            \context Score = "Score"                                                                 %! baca.SingleStaffScoreTemplate.__call__()
            <<                                                                                       %! baca.SingleStaffScoreTemplate.__call__()
            <BLANKLINE>
                \context GlobalContext = "Global_Context"                                            %! abjad.ScoreTemplate._make_global_context()
                <<                                                                                   %! abjad.ScoreTemplate._make_global_context()
            <BLANKLINE>
                    \context GlobalSkips = "Global_Skips"                                            %! abjad.ScoreTemplate._make_global_context()
                    {                                                                                %! abjad.ScoreTemplate._make_global_context()
            <BLANKLINE>
                        % [Global_Skips measure 1]                                                   %! baca.SegmentMaker._comment_measure_numbers()
                        \baca-new-spacing-section #1 #24                                             %! SPACING_COMMAND:baca.HorizontalSpacingSpecifier.__call__(1)
                        \autoPageBreaksOff                                                           %! BREAK:baca.BreakMeasureMap.__call__(1)
                        \noBreak                                                                     %! BREAK:baca.BreakMeasureMap.__call__(2)
                        \baca-lbsd #0 #'(11)                                                         %! BREAK:baca.IndicatorCommand._call()
                        \time 3/8                                                                    %! baca.SegmentMaker._make_global_skips(2):baca.SegmentMaker._set_status_tag():EXPLICIT_TIME_SIGNATURE
                        \baca-time-signature-color #'blue                                            %! baca.SegmentMaker._attach_color_literal(2):EXPLICIT_TIME_SIGNATURE_COLOR
                        \pageBreak                                                                   %! BREAK:baca.IndicatorCommand._call()
                        s1 * 3/8                                                                     %! baca.SegmentMaker._make_global_skips(1)
            <BLANKLINE>
                        % [Global_Skips measure 2]                                                   %! baca.SegmentMaker._comment_measure_numbers()
                        \baca-new-spacing-section #1 #24                                             %! SPACING_COMMAND:baca.HorizontalSpacingSpecifier.__call__(1)
                        \noBreak                                                                     %! BREAK:baca.BreakMeasureMap.__call__(2)
                        \baca-lbsd #15 #'(11)                                                        %! BREAK:baca.IndicatorCommand._call()
                        \break                                                                       %! BREAK:baca.IndicatorCommand._call()
                        s1 * 3/8                                                                     %! baca.SegmentMaker._make_global_skips(1)
            <BLANKLINE>
                        % [Global_Skips measure 3]                                                   %! baca.SegmentMaker._comment_measure_numbers():baca.SegmentMaker._style_phantom_measures(1):PHANTOM
                        \baca-new-spacing-section #1 #4                                              %! SPACING_COMMAND:baca.HorizontalSpacingSpecifier.__call__(1):baca.SegmentMaker._style_phantom_measures(1):PHANTOM
                        \noBreak                                                                     %! BREAK:baca.BreakMeasureMap.__call__(2):baca.SegmentMaker._style_phantom_measures(1):PHANTOM
                        \time 1/4                                                                    %! baca.SegmentMaker._make_global_skips(3):PHANTOM:baca.SegmentMaker._set_status_tag():EXPLICIT_TIME_SIGNATURE:baca.SegmentMaker._style_phantom_measures(1)
                        \baca-time-signature-transparent                                             %! baca.SegmentMaker._style_phantom_measures(2):PHANTOM
                        s1 * 1/4                                                                     %! baca.SegmentMaker._make_global_skips(3):PHANTOM
                        \once \override Score.BarLine.transparent = ##t                              %! baca.SegmentMaker._style_phantom_measures(3):PHANTOM
                        \once \override Score.SpanBar.transparent = ##t                              %! baca.SegmentMaker._style_phantom_measures(3):PHANTOM
            <BLANKLINE>
                    }                                                                                %! abjad.ScoreTemplate._make_global_context()
            <BLANKLINE>
                >>                                                                                   %! abjad.ScoreTemplate._make_global_context()
            <BLANKLINE>
                \context MusicContext = "Music_Context"                                              %! baca.SingleStaffScoreTemplate.__call__()
                <<                                                                                   %! baca.SingleStaffScoreTemplate.__call__()
            <BLANKLINE>
                    \context Staff = "Music_Staff"                                                   %! baca.SingleStaffScoreTemplate.__call__()
                    {                                                                                %! baca.SingleStaffScoreTemplate.__call__()
            <BLANKLINE>
                        \context Voice = "Music_Voice"                                               %! baca.SingleStaffScoreTemplate.__call__()
                        {                                                                            %! baca.SingleStaffScoreTemplate.__call__()
            <BLANKLINE>
                            % [Music_Voice measure 1]                                                %! baca.SegmentMaker._comment_measure_numbers()
                    %@% \baca-not-yet-pitched-coloring                                               %! baca.SegmentMaker._color_not_yet_pitched():NOT_YET_PITCHED_COLORING
                            b'4.                                                                     %! baca.make_notes()
                            ^ \baca-default-indicator-markup "(“Flute”)"                             %! DEFAULT_INSTRUMENT_ALERT:baca.SegmentMaker._attach_latent_indicator_alert()
            <BLANKLINE>
                            % [Music_Voice measure 2]                                                %! baca.SegmentMaker._comment_measure_numbers()
                    %@% \baca-not-yet-pitched-coloring                                               %! baca.SegmentMaker._color_not_yet_pitched():NOT_YET_PITCHED_COLORING
                            b'4.                                                                     %! baca.make_notes()
            <BLANKLINE>
                            <<                                                                       %! baca.SegmentMaker._make_multimeasure_rest_container(7):PHANTOM
            <BLANKLINE>
                                \context Voice = "Music_Voice"                                       %! baca.SegmentMaker._make_multimeasure_rest_container(4):PHANTOM
                                {                                                                    %! baca.SegmentMaker._make_multimeasure_rest_container(4):PHANTOM
            <BLANKLINE>
                                    % [Music_Voice measure 3]                                        %! baca.SegmentMaker._comment_measure_numbers():baca.SegmentMaker._style_phantom_measures(5):PHANTOM
                                    \abjad-invisible-music-coloring                                  %! baca.SegmentMaker._make_multimeasure_rest_container(2):PHANTOM:NOTE:INVISIBLE_MUSIC_COLORING:baca.SegmentMaker._style_phantom_measures(5)
                            %@% \abjad-invisible-music                                               %! baca.SegmentMaker._make_multimeasure_rest_container(3):PHANTOM:NOTE:INVISIBLE_MUSIC_COMMAND:baca.SegmentMaker._style_phantom_measures(5)
                            %@% \baca-not-yet-pitched-coloring                                       %! baca.SegmentMaker._color_not_yet_pitched():NOT_YET_PITCHED_COLORING:HIDDEN:NOTE:baca.SegmentMaker._style_phantom_measures(5):PHANTOM
                                    b'1 * 1/4                                                        %! baca.SegmentMaker._make_multimeasure_rest_container(1):PHANTOM:HIDDEN:NOTE
                            %@% ^ \baca-duration-multiplier-markup #"1" #"4"                         %! baca.SegmentMaker._label_duration_multipliers():DURATION_MULTIPLIER:HIDDEN:NOTE:PHANTOM:baca.SegmentMaker._style_phantom_measures(5)
            <BLANKLINE>
                                }                                                                    %! baca.SegmentMaker._make_multimeasure_rest_container(4):PHANTOM
            <BLANKLINE>
                                \context Voice = "Rest_Voice"                                        %! baca.SegmentMaker._make_multimeasure_rest_container(6):PHANTOM
                                {                                                                    %! baca.SegmentMaker._make_multimeasure_rest_container(6):PHANTOM
            <BLANKLINE>
                                    % [Rest_Voice measure 3]                                         %! baca.SegmentMaker._comment_measure_numbers():baca.SegmentMaker._style_phantom_measures(5):PHANTOM
                                    \once \override Score.TimeSignature.X-extent = ##f               %! baca.SegmentMaker._style_phantom_measures(6):PHANTOM
                                    \once \override MultiMeasureRest.transparent = ##t               %! baca.SegmentMaker._style_phantom_measures(7):PHANTOM
                                    \stopStaff                                                       %! baca.SegmentMaker._style_phantom_measures(8):PHANTOM
                                    \once \override Staff.StaffSymbol.transparent = ##t              %! baca.SegmentMaker._style_phantom_measures(8):PHANTOM
                                    \startStaff                                                      %! baca.SegmentMaker._style_phantom_measures(8):PHANTOM
                                    R1 * 1/4                                                         %! baca.SegmentMaker._make_multimeasure_rest_container(5):PHANTOM:REST_VOICE:MULTIMEASURE_REST
                            %@% ^ \baca-duration-multiplier-markup #"1" #"4"                         %! baca.SegmentMaker._label_duration_multipliers():DURATION_MULTIPLIER:MULTIMEASURE_REST:PHANTOM:REST_VOICE:baca.SegmentMaker._style_phantom_measures(5)
            <BLANKLINE>
                                }                                                                    %! baca.SegmentMaker._make_multimeasure_rest_container(6):PHANTOM
            <BLANKLINE>
                            >>                                                                       %! baca.SegmentMaker._make_multimeasure_rest_container(7):PHANTOM
            <BLANKLINE>
                        }                                                                            %! baca.SingleStaffScoreTemplate.__call__()
            <BLANKLINE>
                    }                                                                                %! baca.SingleStaffScoreTemplate.__call__()
            <BLANKLINE>
                >>                                                                                   %! baca.SingleStaffScoreTemplate.__call__()
            <BLANKLINE>
            >>                                                                                       %! baca.SingleStaffScoreTemplate.__call__()

    ..  container:: example

        Explicit instruments color blue and redraw dull blue:

        >>> maker = baca.SegmentMaker(
        ...     breaks=breaks,
        ...     deactivate=[abjad.tags.NOT_YET_PITCHED_COLORING],
        ...     instruments=instruments,
        ...     score_template=baca.SingleStaffScoreTemplate(),
        ...     spacing=baca.minimum_duration((1, 24)),
        ...     time_signatures=[(3, 8), (3, 8)],
        ...     )
        >>> maker(
        ...     'Music_Voice',
        ...     baca.instrument(instruments['Flute']),
        ...     baca.make_notes(),
        ...     )

        >>> lilypond_file = maker.run(environment='docs')
        >>> block = abjad.Block(name='layout')
        >>> block.indent = 0
        >>> lilypond_file.items.insert(0, block)
        >>> abjad.show(lilypond_file, strict=89) # doctest: +SKIP

        ..  docs::

            >>> abjad.f(lilypond_file[abjad.Score], strict=89)
            <BLANKLINE>
            \context Score = "Score"                                                                 %! baca.SingleStaffScoreTemplate.__call__()
            <<                                                                                       %! baca.SingleStaffScoreTemplate.__call__()
            <BLANKLINE>
                \context GlobalContext = "Global_Context"                                            %! abjad.ScoreTemplate._make_global_context()
                <<                                                                                   %! abjad.ScoreTemplate._make_global_context()
            <BLANKLINE>
                    \context GlobalSkips = "Global_Skips"                                            %! abjad.ScoreTemplate._make_global_context()
                    {                                                                                %! abjad.ScoreTemplate._make_global_context()
            <BLANKLINE>
                        % [Global_Skips measure 1]                                                   %! baca.SegmentMaker._comment_measure_numbers()
                        \baca-new-spacing-section #1 #24                                             %! SPACING_COMMAND:baca.HorizontalSpacingSpecifier.__call__(1)
                        \autoPageBreaksOff                                                           %! BREAK:baca.BreakMeasureMap.__call__(1)
                        \noBreak                                                                     %! BREAK:baca.BreakMeasureMap.__call__(2)
                        \baca-lbsd #0 #'(11)                                                         %! BREAK:baca.IndicatorCommand._call()
                        \time 3/8                                                                    %! baca.SegmentMaker._make_global_skips(2):baca.SegmentMaker._set_status_tag():EXPLICIT_TIME_SIGNATURE
                        \baca-time-signature-color #'blue                                            %! baca.SegmentMaker._attach_color_literal(2):EXPLICIT_TIME_SIGNATURE_COLOR
                        \pageBreak                                                                   %! BREAK:baca.IndicatorCommand._call()
                        s1 * 3/8                                                                     %! baca.SegmentMaker._make_global_skips(1)
            <BLANKLINE>
                        % [Global_Skips measure 2]                                                   %! baca.SegmentMaker._comment_measure_numbers()
                        \baca-new-spacing-section #1 #24                                             %! SPACING_COMMAND:baca.HorizontalSpacingSpecifier.__call__(1)
                        \noBreak                                                                     %! BREAK:baca.BreakMeasureMap.__call__(2)
                        \baca-lbsd #15 #'(11)                                                        %! BREAK:baca.IndicatorCommand._call()
                        \break                                                                       %! BREAK:baca.IndicatorCommand._call()
                        s1 * 3/8                                                                     %! baca.SegmentMaker._make_global_skips(1)
            <BLANKLINE>
                        % [Global_Skips measure 3]                                                   %! baca.SegmentMaker._comment_measure_numbers():baca.SegmentMaker._style_phantom_measures(1):PHANTOM
                        \baca-new-spacing-section #1 #4                                              %! SPACING_COMMAND:baca.HorizontalSpacingSpecifier.__call__(1):baca.SegmentMaker._style_phantom_measures(1):PHANTOM
                        \noBreak                                                                     %! BREAK:baca.BreakMeasureMap.__call__(2):baca.SegmentMaker._style_phantom_measures(1):PHANTOM
                        \time 1/4                                                                    %! baca.SegmentMaker._make_global_skips(3):PHANTOM:baca.SegmentMaker._set_status_tag():EXPLICIT_TIME_SIGNATURE:baca.SegmentMaker._style_phantom_measures(1)
                        \baca-time-signature-transparent                                             %! baca.SegmentMaker._style_phantom_measures(2):PHANTOM
                        s1 * 1/4                                                                     %! baca.SegmentMaker._make_global_skips(3):PHANTOM
                        \once \override Score.BarLine.transparent = ##t                              %! baca.SegmentMaker._style_phantom_measures(3):PHANTOM
                        \once \override Score.SpanBar.transparent = ##t                              %! baca.SegmentMaker._style_phantom_measures(3):PHANTOM
            <BLANKLINE>
                    }                                                                                %! abjad.ScoreTemplate._make_global_context()
            <BLANKLINE>
                >>                                                                                   %! abjad.ScoreTemplate._make_global_context()
            <BLANKLINE>
                \context MusicContext = "Music_Context"                                              %! baca.SingleStaffScoreTemplate.__call__()
                <<                                                                                   %! baca.SingleStaffScoreTemplate.__call__()
            <BLANKLINE>
                    \context Staff = "Music_Staff"                                                   %! baca.SingleStaffScoreTemplate.__call__()
                    {                                                                                %! baca.SingleStaffScoreTemplate.__call__()
            <BLANKLINE>
                        \context Voice = "Music_Voice"                                               %! baca.SingleStaffScoreTemplate.__call__()
                        {                                                                            %! baca.SingleStaffScoreTemplate.__call__()
            <BLANKLINE>
                            % [Music_Voice measure 1]                                                %! baca.SegmentMaker._comment_measure_numbers()
                        %@% \baca-not-yet-pitched-coloring                                           %! baca.SegmentMaker._color_not_yet_pitched():NOT_YET_PITCHED_COLORING
                            b'4.                                                                     %! baca.make_notes()
                            ^ \baca-explicit-indicator-markup "(“Flute”)"                            %! EXPLICIT_INSTRUMENT_ALERT:baca.SegmentMaker._attach_latent_indicator_alert()
            <BLANKLINE>
                            % [Music_Voice measure 2]                                                %! baca.SegmentMaker._comment_measure_numbers()
                        %@% \baca-not-yet-pitched-coloring                                           %! baca.SegmentMaker._color_not_yet_pitched():NOT_YET_PITCHED_COLORING
                            b'4.                                                                     %! baca.make_notes()
            <BLANKLINE>
                            <<                                                                       %! baca.SegmentMaker._make_multimeasure_rest_container(7):PHANTOM
            <BLANKLINE>
                                \context Voice = "Music_Voice"                                       %! baca.SegmentMaker._make_multimeasure_rest_container(4):PHANTOM
                                {                                                                    %! baca.SegmentMaker._make_multimeasure_rest_container(4):PHANTOM
            <BLANKLINE>
                                    % [Music_Voice measure 3]                                        %! baca.SegmentMaker._comment_measure_numbers():baca.SegmentMaker._style_phantom_measures(5):PHANTOM
                                    \abjad-invisible-music-coloring                                  %! baca.SegmentMaker._make_multimeasure_rest_container(2):PHANTOM:NOTE:INVISIBLE_MUSIC_COLORING:baca.SegmentMaker._style_phantom_measures(5)
                                %@% \abjad-invisible-music                                           %! baca.SegmentMaker._make_multimeasure_rest_container(3):PHANTOM:NOTE:INVISIBLE_MUSIC_COMMAND:baca.SegmentMaker._style_phantom_measures(5)
                                %@% \baca-not-yet-pitched-coloring                                   %! baca.SegmentMaker._color_not_yet_pitched():NOT_YET_PITCHED_COLORING:HIDDEN:NOTE:baca.SegmentMaker._style_phantom_measures(5):PHANTOM
                                    b'1 * 1/4                                                        %! baca.SegmentMaker._make_multimeasure_rest_container(1):PHANTOM:HIDDEN:NOTE
                                %@% ^ \baca-duration-multiplier-markup #"1" #"4"                     %! baca.SegmentMaker._label_duration_multipliers():DURATION_MULTIPLIER:HIDDEN:NOTE:PHANTOM:baca.SegmentMaker._style_phantom_measures(5)
            <BLANKLINE>
                                }                                                                    %! baca.SegmentMaker._make_multimeasure_rest_container(4):PHANTOM
            <BLANKLINE>
                                \context Voice = "Rest_Voice"                                        %! baca.SegmentMaker._make_multimeasure_rest_container(6):PHANTOM
                                {                                                                    %! baca.SegmentMaker._make_multimeasure_rest_container(6):PHANTOM
            <BLANKLINE>
                                    % [Rest_Voice measure 3]                                         %! baca.SegmentMaker._comment_measure_numbers():baca.SegmentMaker._style_phantom_measures(5):PHANTOM
                                    \once \override Score.TimeSignature.X-extent = ##f               %! baca.SegmentMaker._style_phantom_measures(6):PHANTOM
                                    \once \override MultiMeasureRest.transparent = ##t               %! baca.SegmentMaker._style_phantom_measures(7):PHANTOM
                                    \stopStaff                                                       %! baca.SegmentMaker._style_phantom_measures(8):PHANTOM
                                    \once \override Staff.StaffSymbol.transparent = ##t              %! baca.SegmentMaker._style_phantom_measures(8):PHANTOM
                                    \startStaff                                                      %! baca.SegmentMaker._style_phantom_measures(8):PHANTOM
                                    R1 * 1/4                                                         %! baca.SegmentMaker._make_multimeasure_rest_container(5):PHANTOM:REST_VOICE:MULTIMEASURE_REST
                                %@% ^ \baca-duration-multiplier-markup #"1" #"4"                     %! baca.SegmentMaker._label_duration_multipliers():DURATION_MULTIPLIER:MULTIMEASURE_REST:PHANTOM:REST_VOICE:baca.SegmentMaker._style_phantom_measures(5)
            <BLANKLINE>
                                }                                                                    %! baca.SegmentMaker._make_multimeasure_rest_container(6):PHANTOM
            <BLANKLINE>
                            >>                                                                       %! baca.SegmentMaker._make_multimeasure_rest_container(7):PHANTOM
            <BLANKLINE>
                        }                                                                            %! baca.SingleStaffScoreTemplate.__call__()
            <BLANKLINE>
                    }                                                                                %! baca.SingleStaffScoreTemplate.__call__()
            <BLANKLINE>
                >>                                                                                   %! baca.SingleStaffScoreTemplate.__call__()
            <BLANKLINE>
            >>                                                                                       %! baca.SingleStaffScoreTemplate.__call__()

        >>> score = lilypond_file[abjad.Score]
        >>> text = format(score, 'lilypond')
        >>> text = abjad.LilyPondFormatManager.left_shift_tags(text)
        >>> tags_ = abjad.tags.instrument_color_tags()
        >>> match = lambda tags: bool(set(tags) & set(tags_))
        >>> text, count = abjad.deactivate(text, match)
        >>> text = abjad.LilyPondFormatManager.left_shift_tags(text, 89)
        >>> lines = [_.strip('\n') for _ in text.split('\n')]
        >>> lilypond_file.score_block.items[:] = lines
        >>> abjad.show(lilypond_file, strict=89) # doctest: +SKIP

        ..  docs::

            >>> print(text)
            <BLANKLINE>
            \context Score = "Score"                                                                 %! baca.SingleStaffScoreTemplate.__call__()
            <<                                                                                       %! baca.SingleStaffScoreTemplate.__call__()
            <BLANKLINE>
                \context GlobalContext = "Global_Context"                                            %! abjad.ScoreTemplate._make_global_context()
                <<                                                                                   %! abjad.ScoreTemplate._make_global_context()
            <BLANKLINE>
                    \context GlobalSkips = "Global_Skips"                                            %! abjad.ScoreTemplate._make_global_context()
                    {                                                                                %! abjad.ScoreTemplate._make_global_context()
            <BLANKLINE>
                        % [Global_Skips measure 1]                                                   %! baca.SegmentMaker._comment_measure_numbers()
                        \baca-new-spacing-section #1 #24                                             %! SPACING_COMMAND:baca.HorizontalSpacingSpecifier.__call__(1)
                        \autoPageBreaksOff                                                           %! BREAK:baca.BreakMeasureMap.__call__(1)
                        \noBreak                                                                     %! BREAK:baca.BreakMeasureMap.__call__(2)
                        \baca-lbsd #0 #'(11)                                                         %! BREAK:baca.IndicatorCommand._call()
                        \time 3/8                                                                    %! baca.SegmentMaker._make_global_skips(2):baca.SegmentMaker._set_status_tag():EXPLICIT_TIME_SIGNATURE
                        \baca-time-signature-color #'blue                                            %! baca.SegmentMaker._attach_color_literal(2):EXPLICIT_TIME_SIGNATURE_COLOR
                        \pageBreak                                                                   %! BREAK:baca.IndicatorCommand._call()
                        s1 * 3/8                                                                     %! baca.SegmentMaker._make_global_skips(1)
            <BLANKLINE>
                        % [Global_Skips measure 2]                                                   %! baca.SegmentMaker._comment_measure_numbers()
                        \baca-new-spacing-section #1 #24                                             %! SPACING_COMMAND:baca.HorizontalSpacingSpecifier.__call__(1)
                        \noBreak                                                                     %! BREAK:baca.BreakMeasureMap.__call__(2)
                        \baca-lbsd #15 #'(11)                                                        %! BREAK:baca.IndicatorCommand._call()
                        \break                                                                       %! BREAK:baca.IndicatorCommand._call()
                        s1 * 3/8                                                                     %! baca.SegmentMaker._make_global_skips(1)
            <BLANKLINE>
                        % [Global_Skips measure 3]                                                   %! baca.SegmentMaker._comment_measure_numbers():baca.SegmentMaker._style_phantom_measures(1):PHANTOM
                        \baca-new-spacing-section #1 #4                                              %! SPACING_COMMAND:baca.HorizontalSpacingSpecifier.__call__(1):baca.SegmentMaker._style_phantom_measures(1):PHANTOM
                        \noBreak                                                                     %! BREAK:baca.BreakMeasureMap.__call__(2):baca.SegmentMaker._style_phantom_measures(1):PHANTOM
                        \time 1/4                                                                    %! baca.SegmentMaker._make_global_skips(3):PHANTOM:baca.SegmentMaker._set_status_tag():EXPLICIT_TIME_SIGNATURE:baca.SegmentMaker._style_phantom_measures(1)
                        \baca-time-signature-transparent                                             %! baca.SegmentMaker._style_phantom_measures(2):PHANTOM
                        s1 * 1/4                                                                     %! baca.SegmentMaker._make_global_skips(3):PHANTOM
                        \once \override Score.BarLine.transparent = ##t                              %! baca.SegmentMaker._style_phantom_measures(3):PHANTOM
                        \once \override Score.SpanBar.transparent = ##t                              %! baca.SegmentMaker._style_phantom_measures(3):PHANTOM
            <BLANKLINE>
                    }                                                                                %! abjad.ScoreTemplate._make_global_context()
            <BLANKLINE>
                >>                                                                                   %! abjad.ScoreTemplate._make_global_context()
            <BLANKLINE>
                \context MusicContext = "Music_Context"                                              %! baca.SingleStaffScoreTemplate.__call__()
                <<                                                                                   %! baca.SingleStaffScoreTemplate.__call__()
            <BLANKLINE>
                    \context Staff = "Music_Staff"                                                   %! baca.SingleStaffScoreTemplate.__call__()
                    {                                                                                %! baca.SingleStaffScoreTemplate.__call__()
            <BLANKLINE>
                        \context Voice = "Music_Voice"                                               %! baca.SingleStaffScoreTemplate.__call__()
                        {                                                                            %! baca.SingleStaffScoreTemplate.__call__()
            <BLANKLINE>
                            % [Music_Voice measure 1]                                                %! baca.SegmentMaker._comment_measure_numbers()
                    %@% \baca-not-yet-pitched-coloring                                               %! baca.SegmentMaker._color_not_yet_pitched():NOT_YET_PITCHED_COLORING
                            b'4.                                                                     %! baca.make_notes()
                        %%% ^ \baca-explicit-indicator-markup "(“Flute”)"                            %! EXPLICIT_INSTRUMENT_ALERT:baca.SegmentMaker._attach_latent_indicator_alert()
            <BLANKLINE>
                            % [Music_Voice measure 2]                                                %! baca.SegmentMaker._comment_measure_numbers()
                    %@% \baca-not-yet-pitched-coloring                                               %! baca.SegmentMaker._color_not_yet_pitched():NOT_YET_PITCHED_COLORING
                            b'4.                                                                     %! baca.make_notes()
            <BLANKLINE>
                            <<                                                                       %! baca.SegmentMaker._make_multimeasure_rest_container(7):PHANTOM
            <BLANKLINE>
                                \context Voice = "Music_Voice"                                       %! baca.SegmentMaker._make_multimeasure_rest_container(4):PHANTOM
                                {                                                                    %! baca.SegmentMaker._make_multimeasure_rest_container(4):PHANTOM
            <BLANKLINE>
                                    % [Music_Voice measure 3]                                        %! baca.SegmentMaker._comment_measure_numbers():baca.SegmentMaker._style_phantom_measures(5):PHANTOM
                                    \abjad-invisible-music-coloring                                  %! baca.SegmentMaker._make_multimeasure_rest_container(2):PHANTOM:NOTE:INVISIBLE_MUSIC_COLORING:baca.SegmentMaker._style_phantom_measures(5)
                            %@% \abjad-invisible-music                                               %! baca.SegmentMaker._make_multimeasure_rest_container(3):PHANTOM:NOTE:INVISIBLE_MUSIC_COMMAND:baca.SegmentMaker._style_phantom_measures(5)
                            %@% \baca-not-yet-pitched-coloring                                       %! baca.SegmentMaker._color_not_yet_pitched():NOT_YET_PITCHED_COLORING:HIDDEN:NOTE:baca.SegmentMaker._style_phantom_measures(5):PHANTOM
                                    b'1 * 1/4                                                        %! baca.SegmentMaker._make_multimeasure_rest_container(1):PHANTOM:HIDDEN:NOTE
                            %@% ^ \baca-duration-multiplier-markup #"1" #"4"                         %! baca.SegmentMaker._label_duration_multipliers():DURATION_MULTIPLIER:HIDDEN:NOTE:PHANTOM:baca.SegmentMaker._style_phantom_measures(5)
            <BLANKLINE>
                                }                                                                    %! baca.SegmentMaker._make_multimeasure_rest_container(4):PHANTOM
            <BLANKLINE>
                                \context Voice = "Rest_Voice"                                        %! baca.SegmentMaker._make_multimeasure_rest_container(6):PHANTOM
                                {                                                                    %! baca.SegmentMaker._make_multimeasure_rest_container(6):PHANTOM
            <BLANKLINE>
                                    % [Rest_Voice measure 3]                                         %! baca.SegmentMaker._comment_measure_numbers():baca.SegmentMaker._style_phantom_measures(5):PHANTOM
                                    \once \override Score.TimeSignature.X-extent = ##f               %! baca.SegmentMaker._style_phantom_measures(6):PHANTOM
                                    \once \override MultiMeasureRest.transparent = ##t               %! baca.SegmentMaker._style_phantom_measures(7):PHANTOM
                                    \stopStaff                                                       %! baca.SegmentMaker._style_phantom_measures(8):PHANTOM
                                    \once \override Staff.StaffSymbol.transparent = ##t              %! baca.SegmentMaker._style_phantom_measures(8):PHANTOM
                                    \startStaff                                                      %! baca.SegmentMaker._style_phantom_measures(8):PHANTOM
                                    R1 * 1/4                                                         %! baca.SegmentMaker._make_multimeasure_rest_container(5):PHANTOM:REST_VOICE:MULTIMEASURE_REST
                            %@% ^ \baca-duration-multiplier-markup #"1" #"4"                         %! baca.SegmentMaker._label_duration_multipliers():DURATION_MULTIPLIER:MULTIMEASURE_REST:PHANTOM:REST_VOICE:baca.SegmentMaker._style_phantom_measures(5)
            <BLANKLINE>
                                }                                                                    %! baca.SegmentMaker._make_multimeasure_rest_container(6):PHANTOM
            <BLANKLINE>
                            >>                                                                       %! baca.SegmentMaker._make_multimeasure_rest_container(7):PHANTOM
            <BLANKLINE>
                        }                                                                            %! baca.SingleStaffScoreTemplate.__call__()
            <BLANKLINE>
                    }                                                                                %! baca.SingleStaffScoreTemplate.__call__()
            <BLANKLINE>
                >>                                                                                   %! baca.SingleStaffScoreTemplate.__call__()
            <BLANKLINE>
            >>                                                                                       %! baca.SingleStaffScoreTemplate.__call__()

        >>> tags_ = abjad.tags.instrument_color_tags()
        >>> match = lambda tags: bool(set(tags) & set(tags_))
        >>> text, count = abjad.activate(text, match)
        >>> text = abjad.LilyPondFormatManager.left_shift_tags(text, 89)
        >>> lines = [_.strip('\n') for _ in text.split('\n')]
        >>> lilypond_file.score_block.items[:] = lines
        >>> abjad.show(lilypond_file, strict=89) # doctest: +SKIP

        ..  docs::

            >>> print(text)
            <BLANKLINE>
            \context Score = "Score"                                                                 %! baca.SingleStaffScoreTemplate.__call__()
            <<                                                                                       %! baca.SingleStaffScoreTemplate.__call__()
            <BLANKLINE>
                \context GlobalContext = "Global_Context"                                            %! abjad.ScoreTemplate._make_global_context()
                <<                                                                                   %! abjad.ScoreTemplate._make_global_context()
            <BLANKLINE>
                    \context GlobalSkips = "Global_Skips"                                            %! abjad.ScoreTemplate._make_global_context()
                    {                                                                                %! abjad.ScoreTemplate._make_global_context()
            <BLANKLINE>
                        % [Global_Skips measure 1]                                                   %! baca.SegmentMaker._comment_measure_numbers()
                        \baca-new-spacing-section #1 #24                                             %! SPACING_COMMAND:baca.HorizontalSpacingSpecifier.__call__(1)
                        \autoPageBreaksOff                                                           %! BREAK:baca.BreakMeasureMap.__call__(1)
                        \noBreak                                                                     %! BREAK:baca.BreakMeasureMap.__call__(2)
                        \baca-lbsd #0 #'(11)                                                         %! BREAK:baca.IndicatorCommand._call()
                        \time 3/8                                                                    %! baca.SegmentMaker._make_global_skips(2):baca.SegmentMaker._set_status_tag():EXPLICIT_TIME_SIGNATURE
                        \baca-time-signature-color #'blue                                            %! baca.SegmentMaker._attach_color_literal(2):EXPLICIT_TIME_SIGNATURE_COLOR
                        \pageBreak                                                                   %! BREAK:baca.IndicatorCommand._call()
                        s1 * 3/8                                                                     %! baca.SegmentMaker._make_global_skips(1)
            <BLANKLINE>
                        % [Global_Skips measure 2]                                                   %! baca.SegmentMaker._comment_measure_numbers()
                        \baca-new-spacing-section #1 #24                                             %! SPACING_COMMAND:baca.HorizontalSpacingSpecifier.__call__(1)
                        \noBreak                                                                     %! BREAK:baca.BreakMeasureMap.__call__(2)
                        \baca-lbsd #15 #'(11)                                                        %! BREAK:baca.IndicatorCommand._call()
                        \break                                                                       %! BREAK:baca.IndicatorCommand._call()
                        s1 * 3/8                                                                     %! baca.SegmentMaker._make_global_skips(1)
            <BLANKLINE>
                        % [Global_Skips measure 3]                                                   %! baca.SegmentMaker._comment_measure_numbers():baca.SegmentMaker._style_phantom_measures(1):PHANTOM
                        \baca-new-spacing-section #1 #4                                              %! SPACING_COMMAND:baca.HorizontalSpacingSpecifier.__call__(1):baca.SegmentMaker._style_phantom_measures(1):PHANTOM
                        \noBreak                                                                     %! BREAK:baca.BreakMeasureMap.__call__(2):baca.SegmentMaker._style_phantom_measures(1):PHANTOM
                        \time 1/4                                                                    %! baca.SegmentMaker._make_global_skips(3):PHANTOM:baca.SegmentMaker._set_status_tag():EXPLICIT_TIME_SIGNATURE:baca.SegmentMaker._style_phantom_measures(1)
                        \baca-time-signature-transparent                                             %! baca.SegmentMaker._style_phantom_measures(2):PHANTOM
                        s1 * 1/4                                                                     %! baca.SegmentMaker._make_global_skips(3):PHANTOM
                        \once \override Score.BarLine.transparent = ##t                              %! baca.SegmentMaker._style_phantom_measures(3):PHANTOM
                        \once \override Score.SpanBar.transparent = ##t                              %! baca.SegmentMaker._style_phantom_measures(3):PHANTOM
            <BLANKLINE>
                    }                                                                                %! abjad.ScoreTemplate._make_global_context()
            <BLANKLINE>
                >>                                                                                   %! abjad.ScoreTemplate._make_global_context()
            <BLANKLINE>
                \context MusicContext = "Music_Context"                                              %! baca.SingleStaffScoreTemplate.__call__()
                <<                                                                                   %! baca.SingleStaffScoreTemplate.__call__()
            <BLANKLINE>
                    \context Staff = "Music_Staff"                                                   %! baca.SingleStaffScoreTemplate.__call__()
                    {                                                                                %! baca.SingleStaffScoreTemplate.__call__()
            <BLANKLINE>
                        \context Voice = "Music_Voice"                                               %! baca.SingleStaffScoreTemplate.__call__()
                        {                                                                            %! baca.SingleStaffScoreTemplate.__call__()
            <BLANKLINE>
                            % [Music_Voice measure 1]                                                %! baca.SegmentMaker._comment_measure_numbers()
                %@% \baca-not-yet-pitched-coloring                                                   %! baca.SegmentMaker._color_not_yet_pitched():NOT_YET_PITCHED_COLORING
                            b'4.                                                                     %! baca.make_notes()
                            ^ \baca-explicit-indicator-markup "(“Flute”)"                            %! EXPLICIT_INSTRUMENT_ALERT:baca.SegmentMaker._attach_latent_indicator_alert()
            <BLANKLINE>
                            % [Music_Voice measure 2]                                                %! baca.SegmentMaker._comment_measure_numbers()
                %@% \baca-not-yet-pitched-coloring                                                   %! baca.SegmentMaker._color_not_yet_pitched():NOT_YET_PITCHED_COLORING
                            b'4.                                                                     %! baca.make_notes()
            <BLANKLINE>
                            <<                                                                       %! baca.SegmentMaker._make_multimeasure_rest_container(7):PHANTOM
            <BLANKLINE>
                                \context Voice = "Music_Voice"                                       %! baca.SegmentMaker._make_multimeasure_rest_container(4):PHANTOM
                                {                                                                    %! baca.SegmentMaker._make_multimeasure_rest_container(4):PHANTOM
            <BLANKLINE>
                                    % [Music_Voice measure 3]                                        %! baca.SegmentMaker._comment_measure_numbers():baca.SegmentMaker._style_phantom_measures(5):PHANTOM
                                    \abjad-invisible-music-coloring                                  %! baca.SegmentMaker._make_multimeasure_rest_container(2):PHANTOM:NOTE:INVISIBLE_MUSIC_COLORING:baca.SegmentMaker._style_phantom_measures(5)
                        %@% \abjad-invisible-music                                                   %! baca.SegmentMaker._make_multimeasure_rest_container(3):PHANTOM:NOTE:INVISIBLE_MUSIC_COMMAND:baca.SegmentMaker._style_phantom_measures(5)
                        %@% \baca-not-yet-pitched-coloring                                           %! baca.SegmentMaker._color_not_yet_pitched():NOT_YET_PITCHED_COLORING:HIDDEN:NOTE:baca.SegmentMaker._style_phantom_measures(5):PHANTOM
                                    b'1 * 1/4                                                        %! baca.SegmentMaker._make_multimeasure_rest_container(1):PHANTOM:HIDDEN:NOTE
                        %@% ^ \baca-duration-multiplier-markup #"1" #"4"                             %! baca.SegmentMaker._label_duration_multipliers():DURATION_MULTIPLIER:HIDDEN:NOTE:PHANTOM:baca.SegmentMaker._style_phantom_measures(5)
            <BLANKLINE>
                                }                                                                    %! baca.SegmentMaker._make_multimeasure_rest_container(4):PHANTOM
            <BLANKLINE>
                                \context Voice = "Rest_Voice"                                        %! baca.SegmentMaker._make_multimeasure_rest_container(6):PHANTOM
                                {                                                                    %! baca.SegmentMaker._make_multimeasure_rest_container(6):PHANTOM
            <BLANKLINE>
                                    % [Rest_Voice measure 3]                                         %! baca.SegmentMaker._comment_measure_numbers():baca.SegmentMaker._style_phantom_measures(5):PHANTOM
                                    \once \override Score.TimeSignature.X-extent = ##f               %! baca.SegmentMaker._style_phantom_measures(6):PHANTOM
                                    \once \override MultiMeasureRest.transparent = ##t               %! baca.SegmentMaker._style_phantom_measures(7):PHANTOM
                                    \stopStaff                                                       %! baca.SegmentMaker._style_phantom_measures(8):PHANTOM
                                    \once \override Staff.StaffSymbol.transparent = ##t              %! baca.SegmentMaker._style_phantom_measures(8):PHANTOM
                                    \startStaff                                                      %! baca.SegmentMaker._style_phantom_measures(8):PHANTOM
                                    R1 * 1/4                                                         %! baca.SegmentMaker._make_multimeasure_rest_container(5):PHANTOM:REST_VOICE:MULTIMEASURE_REST
                        %@% ^ \baca-duration-multiplier-markup #"1" #"4"                             %! baca.SegmentMaker._label_duration_multipliers():DURATION_MULTIPLIER:MULTIMEASURE_REST:PHANTOM:REST_VOICE:baca.SegmentMaker._style_phantom_measures(5)
            <BLANKLINE>
                                }                                                                    %! baca.SegmentMaker._make_multimeasure_rest_container(6):PHANTOM
            <BLANKLINE>
                            >>                                                                       %! baca.SegmentMaker._make_multimeasure_rest_container(7):PHANTOM
            <BLANKLINE>
                        }                                                                            %! baca.SingleStaffScoreTemplate.__call__()
            <BLANKLINE>
                    }                                                                                %! baca.SingleStaffScoreTemplate.__call__()
            <BLANKLINE>
                >>                                                                                   %! baca.SingleStaffScoreTemplate.__call__()
            <BLANKLINE>
            >>                                                                                       %! baca.SingleStaffScoreTemplate.__call__()

        Even after a previous instrument:

        >>> maker = baca.SegmentMaker(
        ...     breaks=breaks,
        ...     deactivate=[abjad.tags.NOT_YET_PITCHED_COLORING],
        ...     instruments=instruments,
        ...     score_template=baca.SingleStaffScoreTemplate(),
        ...     spacing=baca.minimum_duration((1, 24)),
        ...     time_signatures=[(3, 8), (3, 8)],
        ...     )
        >>> maker(
        ...     'Music_Voice',
        ...     baca.instrument(instruments['Flute']),
        ...     baca.make_notes(),
        ...     )

        >>> metadata, persist = {}, {}
        >>> persist['persistent_indicators'] = {}
        >>> persist['persistent_indicators']['Music_Staff'] = [
        ...     abjad.Momento(
        ...         context='Music_Voice',
        ...         manifest='instruments',
        ...         value='Piccolo',
        ...         )
        ...     ]
        >>> metadata['segment_number'] = 1
        >>> lilypond_file = maker.run(
        ...     environment='docs',
        ...     previous_metadata=metadata,
        ...     previous_persist=persist,
        ...     )
        >>> block = abjad.Block(name='layout')
        >>> block.indent = 0
        >>> lilypond_file.items.insert(0, block)
        >>> abjad.show(lilypond_file, strict=89) # doctest: +SKIP

        ..  docs::

            >>> abjad.f(lilypond_file[abjad.Score], strict=89)
            <BLANKLINE>
            \context Score = "Score"                                                                 %! baca.SingleStaffScoreTemplate.__call__()
            <<                                                                                       %! baca.SingleStaffScoreTemplate.__call__()
            <BLANKLINE>
                \context GlobalContext = "Global_Context"                                            %! abjad.ScoreTemplate._make_global_context()
                <<                                                                                   %! abjad.ScoreTemplate._make_global_context()
            <BLANKLINE>
                    \context GlobalSkips = "Global_Skips"                                            %! abjad.ScoreTemplate._make_global_context()
                    {                                                                                %! abjad.ScoreTemplate._make_global_context()
            <BLANKLINE>
                        % [Global_Skips measure 1]                                                   %! baca.SegmentMaker._comment_measure_numbers()
                        \baca-new-spacing-section #1 #24                                             %! SPACING_COMMAND:baca.HorizontalSpacingSpecifier.__call__(1)
                        \autoPageBreaksOff                                                           %! BREAK:baca.BreakMeasureMap.__call__(1)
                        \noBreak                                                                     %! BREAK:baca.BreakMeasureMap.__call__(2)
                        \baca-lbsd #0 #'(11)                                                         %! BREAK:baca.IndicatorCommand._call()
                        \time 3/8                                                                    %! baca.SegmentMaker._make_global_skips(2):baca.SegmentMaker._set_status_tag():EXPLICIT_TIME_SIGNATURE
                        \bar ""                                                                      %! EMPTY_START_BAR:+SEGMENT:baca.SegmentMaker._make_global_skips(4)
                        \baca-time-signature-color #'blue                                            %! baca.SegmentMaker._attach_color_literal(2):EXPLICIT_TIME_SIGNATURE_COLOR
                        \pageBreak                                                                   %! BREAK:baca.IndicatorCommand._call()
                        s1 * 3/8                                                                     %! baca.SegmentMaker._make_global_skips(1)
            <BLANKLINE>
                        % [Global_Skips measure 2]                                                   %! baca.SegmentMaker._comment_measure_numbers()
                        \baca-new-spacing-section #1 #24                                             %! SPACING_COMMAND:baca.HorizontalSpacingSpecifier.__call__(1)
                        \noBreak                                                                     %! BREAK:baca.BreakMeasureMap.__call__(2)
                        \baca-lbsd #15 #'(11)                                                        %! BREAK:baca.IndicatorCommand._call()
                        \break                                                                       %! BREAK:baca.IndicatorCommand._call()
                        s1 * 3/8                                                                     %! baca.SegmentMaker._make_global_skips(1)
            <BLANKLINE>
                        % [Global_Skips measure 3]                                                   %! baca.SegmentMaker._comment_measure_numbers():baca.SegmentMaker._style_phantom_measures(1):PHANTOM
                        \baca-new-spacing-section #1 #4                                              %! SPACING_COMMAND:baca.HorizontalSpacingSpecifier.__call__(1):baca.SegmentMaker._style_phantom_measures(1):PHANTOM
                        \noBreak                                                                     %! BREAK:baca.BreakMeasureMap.__call__(2):baca.SegmentMaker._style_phantom_measures(1):PHANTOM
                        \time 1/4                                                                    %! baca.SegmentMaker._make_global_skips(3):PHANTOM:baca.SegmentMaker._set_status_tag():EXPLICIT_TIME_SIGNATURE:baca.SegmentMaker._style_phantom_measures(1)
                        \baca-time-signature-transparent                                             %! baca.SegmentMaker._style_phantom_measures(2):PHANTOM
                        s1 * 1/4                                                                     %! baca.SegmentMaker._make_global_skips(3):PHANTOM
                        \once \override Score.BarLine.transparent = ##t                              %! baca.SegmentMaker._style_phantom_measures(3):PHANTOM
                        \once \override Score.SpanBar.transparent = ##t                              %! baca.SegmentMaker._style_phantom_measures(3):PHANTOM
            <BLANKLINE>
                    }                                                                                %! abjad.ScoreTemplate._make_global_context()
            <BLANKLINE>
                >>                                                                                   %! abjad.ScoreTemplate._make_global_context()
            <BLANKLINE>
                \context MusicContext = "Music_Context"                                              %! baca.SingleStaffScoreTemplate.__call__()
                <<                                                                                   %! baca.SingleStaffScoreTemplate.__call__()
            <BLANKLINE>
                    \context Staff = "Music_Staff"                                                   %! baca.SingleStaffScoreTemplate.__call__()
                    {                                                                                %! baca.SingleStaffScoreTemplate.__call__()
            <BLANKLINE>
                        \context Voice = "Music_Voice"                                               %! baca.SingleStaffScoreTemplate.__call__()
                        {                                                                            %! baca.SingleStaffScoreTemplate.__call__()
            <BLANKLINE>
                            % [Music_Voice measure 1]                                                %! baca.SegmentMaker._comment_measure_numbers()
                        %@% \baca-not-yet-pitched-coloring                                           %! baca.SegmentMaker._color_not_yet_pitched():NOT_YET_PITCHED_COLORING
                            b'4.                                                                     %! baca.make_notes()
                            ^ \baca-explicit-indicator-markup "(“Flute”)"                            %! EXPLICIT_INSTRUMENT_ALERT:baca.SegmentMaker._attach_latent_indicator_alert()
            <BLANKLINE>
                            % [Music_Voice measure 2]                                                %! baca.SegmentMaker._comment_measure_numbers()
                        %@% \baca-not-yet-pitched-coloring                                           %! baca.SegmentMaker._color_not_yet_pitched():NOT_YET_PITCHED_COLORING
                            b'4.                                                                     %! baca.make_notes()
            <BLANKLINE>
                            <<                                                                       %! baca.SegmentMaker._make_multimeasure_rest_container(7):PHANTOM
            <BLANKLINE>
                                \context Voice = "Music_Voice"                                       %! baca.SegmentMaker._make_multimeasure_rest_container(4):PHANTOM
                                {                                                                    %! baca.SegmentMaker._make_multimeasure_rest_container(4):PHANTOM
            <BLANKLINE>
                                    % [Music_Voice measure 3]                                        %! baca.SegmentMaker._comment_measure_numbers():baca.SegmentMaker._style_phantom_measures(5):PHANTOM
                                    \abjad-invisible-music-coloring                                  %! baca.SegmentMaker._make_multimeasure_rest_container(2):PHANTOM:NOTE:INVISIBLE_MUSIC_COLORING:baca.SegmentMaker._style_phantom_measures(5)
                                %@% \abjad-invisible-music                                           %! baca.SegmentMaker._make_multimeasure_rest_container(3):PHANTOM:NOTE:INVISIBLE_MUSIC_COMMAND:baca.SegmentMaker._style_phantom_measures(5)
                                %@% \baca-not-yet-pitched-coloring                                   %! baca.SegmentMaker._color_not_yet_pitched():NOT_YET_PITCHED_COLORING:HIDDEN:NOTE:baca.SegmentMaker._style_phantom_measures(5):PHANTOM
                                    b'1 * 1/4                                                        %! baca.SegmentMaker._make_multimeasure_rest_container(1):PHANTOM:HIDDEN:NOTE
                                %@% ^ \baca-duration-multiplier-markup #"1" #"4"                     %! baca.SegmentMaker._label_duration_multipliers():DURATION_MULTIPLIER:HIDDEN:NOTE:PHANTOM:baca.SegmentMaker._style_phantom_measures(5)
            <BLANKLINE>
                                }                                                                    %! baca.SegmentMaker._make_multimeasure_rest_container(4):PHANTOM
            <BLANKLINE>
                                \context Voice = "Rest_Voice"                                        %! baca.SegmentMaker._make_multimeasure_rest_container(6):PHANTOM
                                {                                                                    %! baca.SegmentMaker._make_multimeasure_rest_container(6):PHANTOM
            <BLANKLINE>
                                    % [Rest_Voice measure 3]                                         %! baca.SegmentMaker._comment_measure_numbers():baca.SegmentMaker._style_phantom_measures(5):PHANTOM
                                    \once \override Score.TimeSignature.X-extent = ##f               %! baca.SegmentMaker._style_phantom_measures(6):PHANTOM
                                    \once \override MultiMeasureRest.transparent = ##t               %! baca.SegmentMaker._style_phantom_measures(7):PHANTOM
                                    \stopStaff                                                       %! baca.SegmentMaker._style_phantom_measures(8):PHANTOM
                                    \once \override Staff.StaffSymbol.transparent = ##t              %! baca.SegmentMaker._style_phantom_measures(8):PHANTOM
                                    \startStaff                                                      %! baca.SegmentMaker._style_phantom_measures(8):PHANTOM
                                    R1 * 1/4                                                         %! baca.SegmentMaker._make_multimeasure_rest_container(5):PHANTOM:REST_VOICE:MULTIMEASURE_REST
                                %@% ^ \baca-duration-multiplier-markup #"1" #"4"                     %! baca.SegmentMaker._label_duration_multipliers():DURATION_MULTIPLIER:MULTIMEASURE_REST:PHANTOM:REST_VOICE:baca.SegmentMaker._style_phantom_measures(5)
            <BLANKLINE>
                                }                                                                    %! baca.SegmentMaker._make_multimeasure_rest_container(6):PHANTOM
            <BLANKLINE>
                            >>                                                                       %! baca.SegmentMaker._make_multimeasure_rest_container(7):PHANTOM
            <BLANKLINE>
                        }                                                                            %! baca.SingleStaffScoreTemplate.__call__()
            <BLANKLINE>
                    }                                                                                %! baca.SingleStaffScoreTemplate.__call__()
            <BLANKLINE>
                >>                                                                                   %! baca.SingleStaffScoreTemplate.__call__()
            <BLANKLINE>
            >>                                                                                       %! baca.SingleStaffScoreTemplate.__call__()

        >>> score = lilypond_file[abjad.Score]
        >>> text = format(score, 'lilypond')
        >>> text = abjad.LilyPondFormatManager.left_shift_tags(text)
        >>> tags_ = abjad.tags.instrument_color_tags()
        >>> match = lambda tags: bool(set(tags) & set(tags_))
        >>> text, count = abjad.deactivate(text, match)
        >>> text = abjad.LilyPondFormatManager.left_shift_tags(text, 89)
        >>> lines = [_.strip('\n') for _ in text.split('\n')]
        >>> lilypond_file.score_block.items[:] = lines
        >>> abjad.show(lilypond_file, strict=89) # doctest: +SKIP

        ..  docs::

            >>> print(text)
            <BLANKLINE>
            \context Score = "Score"                                                                 %! baca.SingleStaffScoreTemplate.__call__()
            <<                                                                                       %! baca.SingleStaffScoreTemplate.__call__()
            <BLANKLINE>
                \context GlobalContext = "Global_Context"                                            %! abjad.ScoreTemplate._make_global_context()
                <<                                                                                   %! abjad.ScoreTemplate._make_global_context()
            <BLANKLINE>
                    \context GlobalSkips = "Global_Skips"                                            %! abjad.ScoreTemplate._make_global_context()
                    {                                                                                %! abjad.ScoreTemplate._make_global_context()
            <BLANKLINE>
                        % [Global_Skips measure 1]                                                   %! baca.SegmentMaker._comment_measure_numbers()
                        \baca-new-spacing-section #1 #24                                             %! SPACING_COMMAND:baca.HorizontalSpacingSpecifier.__call__(1)
                        \autoPageBreaksOff                                                           %! BREAK:baca.BreakMeasureMap.__call__(1)
                        \noBreak                                                                     %! BREAK:baca.BreakMeasureMap.__call__(2)
                        \baca-lbsd #0 #'(11)                                                         %! BREAK:baca.IndicatorCommand._call()
                        \time 3/8                                                                    %! baca.SegmentMaker._make_global_skips(2):baca.SegmentMaker._set_status_tag():EXPLICIT_TIME_SIGNATURE
                        \bar ""                                                                      %! EMPTY_START_BAR:+SEGMENT:baca.SegmentMaker._make_global_skips(4)
                        \baca-time-signature-color #'blue                                            %! baca.SegmentMaker._attach_color_literal(2):EXPLICIT_TIME_SIGNATURE_COLOR
                        \pageBreak                                                                   %! BREAK:baca.IndicatorCommand._call()
                        s1 * 3/8                                                                     %! baca.SegmentMaker._make_global_skips(1)
            <BLANKLINE>
                        % [Global_Skips measure 2]                                                   %! baca.SegmentMaker._comment_measure_numbers()
                        \baca-new-spacing-section #1 #24                                             %! SPACING_COMMAND:baca.HorizontalSpacingSpecifier.__call__(1)
                        \noBreak                                                                     %! BREAK:baca.BreakMeasureMap.__call__(2)
                        \baca-lbsd #15 #'(11)                                                        %! BREAK:baca.IndicatorCommand._call()
                        \break                                                                       %! BREAK:baca.IndicatorCommand._call()
                        s1 * 3/8                                                                     %! baca.SegmentMaker._make_global_skips(1)
            <BLANKLINE>
                        % [Global_Skips measure 3]                                                   %! baca.SegmentMaker._comment_measure_numbers():baca.SegmentMaker._style_phantom_measures(1):PHANTOM
                        \baca-new-spacing-section #1 #4                                              %! SPACING_COMMAND:baca.HorizontalSpacingSpecifier.__call__(1):baca.SegmentMaker._style_phantom_measures(1):PHANTOM
                        \noBreak                                                                     %! BREAK:baca.BreakMeasureMap.__call__(2):baca.SegmentMaker._style_phantom_measures(1):PHANTOM
                        \time 1/4                                                                    %! baca.SegmentMaker._make_global_skips(3):PHANTOM:baca.SegmentMaker._set_status_tag():EXPLICIT_TIME_SIGNATURE:baca.SegmentMaker._style_phantom_measures(1)
                        \baca-time-signature-transparent                                             %! baca.SegmentMaker._style_phantom_measures(2):PHANTOM
                        s1 * 1/4                                                                     %! baca.SegmentMaker._make_global_skips(3):PHANTOM
                        \once \override Score.BarLine.transparent = ##t                              %! baca.SegmentMaker._style_phantom_measures(3):PHANTOM
                        \once \override Score.SpanBar.transparent = ##t                              %! baca.SegmentMaker._style_phantom_measures(3):PHANTOM
            <BLANKLINE>
                    }                                                                                %! abjad.ScoreTemplate._make_global_context()
            <BLANKLINE>
                >>                                                                                   %! abjad.ScoreTemplate._make_global_context()
            <BLANKLINE>
                \context MusicContext = "Music_Context"                                              %! baca.SingleStaffScoreTemplate.__call__()
                <<                                                                                   %! baca.SingleStaffScoreTemplate.__call__()
            <BLANKLINE>
                    \context Staff = "Music_Staff"                                                   %! baca.SingleStaffScoreTemplate.__call__()
                    {                                                                                %! baca.SingleStaffScoreTemplate.__call__()
            <BLANKLINE>
                        \context Voice = "Music_Voice"                                               %! baca.SingleStaffScoreTemplate.__call__()
                        {                                                                            %! baca.SingleStaffScoreTemplate.__call__()
            <BLANKLINE>
                            % [Music_Voice measure 1]                                                %! baca.SegmentMaker._comment_measure_numbers()
                    %@% \baca-not-yet-pitched-coloring                                               %! baca.SegmentMaker._color_not_yet_pitched():NOT_YET_PITCHED_COLORING
                            b'4.                                                                     %! baca.make_notes()
                        %%% ^ \baca-explicit-indicator-markup "(“Flute”)"                            %! EXPLICIT_INSTRUMENT_ALERT:baca.SegmentMaker._attach_latent_indicator_alert()
            <BLANKLINE>
                            % [Music_Voice measure 2]                                                %! baca.SegmentMaker._comment_measure_numbers()
                    %@% \baca-not-yet-pitched-coloring                                               %! baca.SegmentMaker._color_not_yet_pitched():NOT_YET_PITCHED_COLORING
                            b'4.                                                                     %! baca.make_notes()
            <BLANKLINE>
                            <<                                                                       %! baca.SegmentMaker._make_multimeasure_rest_container(7):PHANTOM
            <BLANKLINE>
                                \context Voice = "Music_Voice"                                       %! baca.SegmentMaker._make_multimeasure_rest_container(4):PHANTOM
                                {                                                                    %! baca.SegmentMaker._make_multimeasure_rest_container(4):PHANTOM
            <BLANKLINE>
                                    % [Music_Voice measure 3]                                        %! baca.SegmentMaker._comment_measure_numbers():baca.SegmentMaker._style_phantom_measures(5):PHANTOM
                                    \abjad-invisible-music-coloring                                  %! baca.SegmentMaker._make_multimeasure_rest_container(2):PHANTOM:NOTE:INVISIBLE_MUSIC_COLORING:baca.SegmentMaker._style_phantom_measures(5)
                            %@% \abjad-invisible-music                                               %! baca.SegmentMaker._make_multimeasure_rest_container(3):PHANTOM:NOTE:INVISIBLE_MUSIC_COMMAND:baca.SegmentMaker._style_phantom_measures(5)
                            %@% \baca-not-yet-pitched-coloring                                       %! baca.SegmentMaker._color_not_yet_pitched():NOT_YET_PITCHED_COLORING:HIDDEN:NOTE:baca.SegmentMaker._style_phantom_measures(5):PHANTOM
                                    b'1 * 1/4                                                        %! baca.SegmentMaker._make_multimeasure_rest_container(1):PHANTOM:HIDDEN:NOTE
                            %@% ^ \baca-duration-multiplier-markup #"1" #"4"                         %! baca.SegmentMaker._label_duration_multipliers():DURATION_MULTIPLIER:HIDDEN:NOTE:PHANTOM:baca.SegmentMaker._style_phantom_measures(5)
            <BLANKLINE>
                                }                                                                    %! baca.SegmentMaker._make_multimeasure_rest_container(4):PHANTOM
            <BLANKLINE>
                                \context Voice = "Rest_Voice"                                        %! baca.SegmentMaker._make_multimeasure_rest_container(6):PHANTOM
                                {                                                                    %! baca.SegmentMaker._make_multimeasure_rest_container(6):PHANTOM
            <BLANKLINE>
                                    % [Rest_Voice measure 3]                                         %! baca.SegmentMaker._comment_measure_numbers():baca.SegmentMaker._style_phantom_measures(5):PHANTOM
                                    \once \override Score.TimeSignature.X-extent = ##f               %! baca.SegmentMaker._style_phantom_measures(6):PHANTOM
                                    \once \override MultiMeasureRest.transparent = ##t               %! baca.SegmentMaker._style_phantom_measures(7):PHANTOM
                                    \stopStaff                                                       %! baca.SegmentMaker._style_phantom_measures(8):PHANTOM
                                    \once \override Staff.StaffSymbol.transparent = ##t              %! baca.SegmentMaker._style_phantom_measures(8):PHANTOM
                                    \startStaff                                                      %! baca.SegmentMaker._style_phantom_measures(8):PHANTOM
                                    R1 * 1/4                                                         %! baca.SegmentMaker._make_multimeasure_rest_container(5):PHANTOM:REST_VOICE:MULTIMEASURE_REST
                            %@% ^ \baca-duration-multiplier-markup #"1" #"4"                         %! baca.SegmentMaker._label_duration_multipliers():DURATION_MULTIPLIER:MULTIMEASURE_REST:PHANTOM:REST_VOICE:baca.SegmentMaker._style_phantom_measures(5)
            <BLANKLINE>
                                }                                                                    %! baca.SegmentMaker._make_multimeasure_rest_container(6):PHANTOM
            <BLANKLINE>
                            >>                                                                       %! baca.SegmentMaker._make_multimeasure_rest_container(7):PHANTOM
            <BLANKLINE>
                        }                                                                            %! baca.SingleStaffScoreTemplate.__call__()
            <BLANKLINE>
                    }                                                                                %! baca.SingleStaffScoreTemplate.__call__()
            <BLANKLINE>
                >>                                                                                   %! baca.SingleStaffScoreTemplate.__call__()
            <BLANKLINE>
            >>                                                                                       %! baca.SingleStaffScoreTemplate.__call__()

        >>> tags_ = abjad.tags.instrument_color_tags()
        >>> match = lambda tags: bool(set(tags) & set(tags_))
        >>> text, count = abjad.activate(text, match)
        >>> lines = [_.strip('\n') for _ in text.split('\n')]
        >>> lilypond_file.score_block.items[:] = lines
        >>> abjad.show(lilypond_file, strict=89) # doctest: +SKIP

        ..  docs::

            >>> print(text)
            <BLANKLINE>
            \context Score = "Score"                                                                 %! baca.SingleStaffScoreTemplate.__call__()
            <<                                                                                       %! baca.SingleStaffScoreTemplate.__call__()
            <BLANKLINE>
                \context GlobalContext = "Global_Context"                                            %! abjad.ScoreTemplate._make_global_context()
                <<                                                                                   %! abjad.ScoreTemplate._make_global_context()
            <BLANKLINE>
                    \context GlobalSkips = "Global_Skips"                                            %! abjad.ScoreTemplate._make_global_context()
                    {                                                                                %! abjad.ScoreTemplate._make_global_context()
            <BLANKLINE>
                        % [Global_Skips measure 1]                                                   %! baca.SegmentMaker._comment_measure_numbers()
                        \baca-new-spacing-section #1 #24                                             %! SPACING_COMMAND:baca.HorizontalSpacingSpecifier.__call__(1)
                        \autoPageBreaksOff                                                           %! BREAK:baca.BreakMeasureMap.__call__(1)
                        \noBreak                                                                     %! BREAK:baca.BreakMeasureMap.__call__(2)
                        \baca-lbsd #0 #'(11)                                                         %! BREAK:baca.IndicatorCommand._call()
                        \time 3/8                                                                    %! baca.SegmentMaker._make_global_skips(2):baca.SegmentMaker._set_status_tag():EXPLICIT_TIME_SIGNATURE
                        \bar ""                                                                      %! EMPTY_START_BAR:+SEGMENT:baca.SegmentMaker._make_global_skips(4)
                        \baca-time-signature-color #'blue                                            %! baca.SegmentMaker._attach_color_literal(2):EXPLICIT_TIME_SIGNATURE_COLOR
                        \pageBreak                                                                   %! BREAK:baca.IndicatorCommand._call()
                        s1 * 3/8                                                                     %! baca.SegmentMaker._make_global_skips(1)
            <BLANKLINE>
                        % [Global_Skips measure 2]                                                   %! baca.SegmentMaker._comment_measure_numbers()
                        \baca-new-spacing-section #1 #24                                             %! SPACING_COMMAND:baca.HorizontalSpacingSpecifier.__call__(1)
                        \noBreak                                                                     %! BREAK:baca.BreakMeasureMap.__call__(2)
                        \baca-lbsd #15 #'(11)                                                        %! BREAK:baca.IndicatorCommand._call()
                        \break                                                                       %! BREAK:baca.IndicatorCommand._call()
                        s1 * 3/8                                                                     %! baca.SegmentMaker._make_global_skips(1)
            <BLANKLINE>
                        % [Global_Skips measure 3]                                                   %! baca.SegmentMaker._comment_measure_numbers():baca.SegmentMaker._style_phantom_measures(1):PHANTOM
                        \baca-new-spacing-section #1 #4                                              %! SPACING_COMMAND:baca.HorizontalSpacingSpecifier.__call__(1):baca.SegmentMaker._style_phantom_measures(1):PHANTOM
                        \noBreak                                                                     %! BREAK:baca.BreakMeasureMap.__call__(2):baca.SegmentMaker._style_phantom_measures(1):PHANTOM
                        \time 1/4                                                                    %! baca.SegmentMaker._make_global_skips(3):PHANTOM:baca.SegmentMaker._set_status_tag():EXPLICIT_TIME_SIGNATURE:baca.SegmentMaker._style_phantom_measures(1)
                        \baca-time-signature-transparent                                             %! baca.SegmentMaker._style_phantom_measures(2):PHANTOM
                        s1 * 1/4                                                                     %! baca.SegmentMaker._make_global_skips(3):PHANTOM
                        \once \override Score.BarLine.transparent = ##t                              %! baca.SegmentMaker._style_phantom_measures(3):PHANTOM
                        \once \override Score.SpanBar.transparent = ##t                              %! baca.SegmentMaker._style_phantom_measures(3):PHANTOM
            <BLANKLINE>
                    }                                                                                %! abjad.ScoreTemplate._make_global_context()
            <BLANKLINE>
                >>                                                                                   %! abjad.ScoreTemplate._make_global_context()
            <BLANKLINE>
                \context MusicContext = "Music_Context"                                              %! baca.SingleStaffScoreTemplate.__call__()
                <<                                                                                   %! baca.SingleStaffScoreTemplate.__call__()
            <BLANKLINE>
                    \context Staff = "Music_Staff"                                                   %! baca.SingleStaffScoreTemplate.__call__()
                    {                                                                                %! baca.SingleStaffScoreTemplate.__call__()
            <BLANKLINE>
                        \context Voice = "Music_Voice"                                               %! baca.SingleStaffScoreTemplate.__call__()
                        {                                                                            %! baca.SingleStaffScoreTemplate.__call__()
            <BLANKLINE>
                            % [Music_Voice measure 1]                                                %! baca.SegmentMaker._comment_measure_numbers()
                    %@% \baca-not-yet-pitched-coloring                                               %! baca.SegmentMaker._color_not_yet_pitched():NOT_YET_PITCHED_COLORING
                            b'4.                                                                     %! baca.make_notes()
                            ^ \baca-explicit-indicator-markup "(“Flute”)"                            %! EXPLICIT_INSTRUMENT_ALERT:baca.SegmentMaker._attach_latent_indicator_alert()
            <BLANKLINE>
                            % [Music_Voice measure 2]                                                %! baca.SegmentMaker._comment_measure_numbers()
                    %@% \baca-not-yet-pitched-coloring                                               %! baca.SegmentMaker._color_not_yet_pitched():NOT_YET_PITCHED_COLORING
                            b'4.                                                                     %! baca.make_notes()
            <BLANKLINE>
                            <<                                                                       %! baca.SegmentMaker._make_multimeasure_rest_container(7):PHANTOM
            <BLANKLINE>
                                \context Voice = "Music_Voice"                                       %! baca.SegmentMaker._make_multimeasure_rest_container(4):PHANTOM
                                {                                                                    %! baca.SegmentMaker._make_multimeasure_rest_container(4):PHANTOM
            <BLANKLINE>
                                    % [Music_Voice measure 3]                                        %! baca.SegmentMaker._comment_measure_numbers():baca.SegmentMaker._style_phantom_measures(5):PHANTOM
                                    \abjad-invisible-music-coloring                                  %! baca.SegmentMaker._make_multimeasure_rest_container(2):PHANTOM:NOTE:INVISIBLE_MUSIC_COLORING:baca.SegmentMaker._style_phantom_measures(5)
                            %@% \abjad-invisible-music                                               %! baca.SegmentMaker._make_multimeasure_rest_container(3):PHANTOM:NOTE:INVISIBLE_MUSIC_COMMAND:baca.SegmentMaker._style_phantom_measures(5)
                            %@% \baca-not-yet-pitched-coloring                                       %! baca.SegmentMaker._color_not_yet_pitched():NOT_YET_PITCHED_COLORING:HIDDEN:NOTE:baca.SegmentMaker._style_phantom_measures(5):PHANTOM
                                    b'1 * 1/4                                                        %! baca.SegmentMaker._make_multimeasure_rest_container(1):PHANTOM:HIDDEN:NOTE
                            %@% ^ \baca-duration-multiplier-markup #"1" #"4"                         %! baca.SegmentMaker._label_duration_multipliers():DURATION_MULTIPLIER:HIDDEN:NOTE:PHANTOM:baca.SegmentMaker._style_phantom_measures(5)
            <BLANKLINE>
                                }                                                                    %! baca.SegmentMaker._make_multimeasure_rest_container(4):PHANTOM
            <BLANKLINE>
                                \context Voice = "Rest_Voice"                                        %! baca.SegmentMaker._make_multimeasure_rest_container(6):PHANTOM
                                {                                                                    %! baca.SegmentMaker._make_multimeasure_rest_container(6):PHANTOM
            <BLANKLINE>
                                    % [Rest_Voice measure 3]                                         %! baca.SegmentMaker._comment_measure_numbers():baca.SegmentMaker._style_phantom_measures(5):PHANTOM
                                    \once \override Score.TimeSignature.X-extent = ##f               %! baca.SegmentMaker._style_phantom_measures(6):PHANTOM
                                    \once \override MultiMeasureRest.transparent = ##t               %! baca.SegmentMaker._style_phantom_measures(7):PHANTOM
                                    \stopStaff                                                       %! baca.SegmentMaker._style_phantom_measures(8):PHANTOM
                                    \once \override Staff.StaffSymbol.transparent = ##t              %! baca.SegmentMaker._style_phantom_measures(8):PHANTOM
                                    \startStaff                                                      %! baca.SegmentMaker._style_phantom_measures(8):PHANTOM
                                    R1 * 1/4                                                         %! baca.SegmentMaker._make_multimeasure_rest_container(5):PHANTOM:REST_VOICE:MULTIMEASURE_REST
                            %@% ^ \baca-duration-multiplier-markup #"1" #"4"                         %! baca.SegmentMaker._label_duration_multipliers():DURATION_MULTIPLIER:MULTIMEASURE_REST:PHANTOM:REST_VOICE:baca.SegmentMaker._style_phantom_measures(5)
            <BLANKLINE>
                                }                                                                    %! baca.SegmentMaker._make_multimeasure_rest_container(6):PHANTOM
            <BLANKLINE>
                            >>                                                                       %! baca.SegmentMaker._make_multimeasure_rest_container(7):PHANTOM
            <BLANKLINE>
                        }                                                                            %! baca.SingleStaffScoreTemplate.__call__()
            <BLANKLINE>
                    }                                                                                %! baca.SingleStaffScoreTemplate.__call__()
            <BLANKLINE>
                >>                                                                                   %! baca.SingleStaffScoreTemplate.__call__()
            <BLANKLINE>
            >>                                                                                       %! baca.SingleStaffScoreTemplate.__call__()

    ..  container:: example

        Reapplied instruments color green and redraw dull green:

        >>> maker = baca.SegmentMaker(
        ...     breaks=breaks,
        ...     deactivate=[abjad.tags.NOT_YET_PITCHED_COLORING],
        ...     instruments=instruments,
        ...     score_template=baca.SingleStaffScoreTemplate(),
        ...     spacing=baca.minimum_duration((1, 24)),
        ...     time_signatures=[(3, 8), (3, 8)],
        ...     )
        >>> maker(
        ...     'Music_Voice',
        ...     baca.make_notes(),
        ...     )

        >>> metadata, persist = {}, {}
        >>> persist['persistent_indicators'] = {}
        >>> persist['persistent_indicators']['Music_Staff'] = [
        ...     abjad.Momento(
        ...         context='Music_Voice',
        ...         manifest='instruments',
        ...         value='Flute',
        ...         )
        ...     ]
        >>> metadata['segment_number'] = 1
        >>> lilypond_file = maker.run(
        ...     environment='docs',
        ...     previous_metadata=metadata,
        ...     previous_persist=persist,
        ...     )
        >>> block = abjad.Block(name='layout')
        >>> block.indent = 0
        >>> lilypond_file.items.insert(0, block)
        >>> abjad.show(lilypond_file, strict=89) # doctest: +SKIP

        ..  docs::

            >>> abjad.f(lilypond_file[abjad.Score], strict=89)
            <BLANKLINE>
            \context Score = "Score"                                                                 %! baca.SingleStaffScoreTemplate.__call__()
            <<                                                                                       %! baca.SingleStaffScoreTemplate.__call__()
            <BLANKLINE>
                \context GlobalContext = "Global_Context"                                            %! abjad.ScoreTemplate._make_global_context()
                <<                                                                                   %! abjad.ScoreTemplate._make_global_context()
            <BLANKLINE>
                    \context GlobalSkips = "Global_Skips"                                            %! abjad.ScoreTemplate._make_global_context()
                    {                                                                                %! abjad.ScoreTemplate._make_global_context()
            <BLANKLINE>
                        % [Global_Skips measure 1]                                                   %! baca.SegmentMaker._comment_measure_numbers()
                        \baca-new-spacing-section #1 #24                                             %! SPACING_COMMAND:baca.HorizontalSpacingSpecifier.__call__(1)
                        \autoPageBreaksOff                                                           %! BREAK:baca.BreakMeasureMap.__call__(1)
                        \noBreak                                                                     %! BREAK:baca.BreakMeasureMap.__call__(2)
                        \baca-lbsd #0 #'(11)                                                         %! BREAK:baca.IndicatorCommand._call()
                        \time 3/8                                                                    %! baca.SegmentMaker._make_global_skips(2):baca.SegmentMaker._set_status_tag():EXPLICIT_TIME_SIGNATURE
                        \bar ""                                                                      %! EMPTY_START_BAR:+SEGMENT:baca.SegmentMaker._make_global_skips(4)
                        \baca-time-signature-color #'blue                                            %! baca.SegmentMaker._attach_color_literal(2):EXPLICIT_TIME_SIGNATURE_COLOR
                        \pageBreak                                                                   %! BREAK:baca.IndicatorCommand._call()
                        s1 * 3/8                                                                     %! baca.SegmentMaker._make_global_skips(1)
            <BLANKLINE>
                        % [Global_Skips measure 2]                                                   %! baca.SegmentMaker._comment_measure_numbers()
                        \baca-new-spacing-section #1 #24                                             %! SPACING_COMMAND:baca.HorizontalSpacingSpecifier.__call__(1)
                        \noBreak                                                                     %! BREAK:baca.BreakMeasureMap.__call__(2)
                        \baca-lbsd #15 #'(11)                                                        %! BREAK:baca.IndicatorCommand._call()
                        \break                                                                       %! BREAK:baca.IndicatorCommand._call()
                        s1 * 3/8                                                                     %! baca.SegmentMaker._make_global_skips(1)
            <BLANKLINE>
                        % [Global_Skips measure 3]                                                   %! baca.SegmentMaker._comment_measure_numbers():baca.SegmentMaker._style_phantom_measures(1):PHANTOM
                        \baca-new-spacing-section #1 #4                                              %! SPACING_COMMAND:baca.HorizontalSpacingSpecifier.__call__(1):baca.SegmentMaker._style_phantom_measures(1):PHANTOM
                        \noBreak                                                                     %! BREAK:baca.BreakMeasureMap.__call__(2):baca.SegmentMaker._style_phantom_measures(1):PHANTOM
                        \time 1/4                                                                    %! baca.SegmentMaker._make_global_skips(3):PHANTOM:baca.SegmentMaker._set_status_tag():EXPLICIT_TIME_SIGNATURE:baca.SegmentMaker._style_phantom_measures(1)
                        \baca-time-signature-transparent                                             %! baca.SegmentMaker._style_phantom_measures(2):PHANTOM
                        s1 * 1/4                                                                     %! baca.SegmentMaker._make_global_skips(3):PHANTOM
                        \once \override Score.BarLine.transparent = ##t                              %! baca.SegmentMaker._style_phantom_measures(3):PHANTOM
                        \once \override Score.SpanBar.transparent = ##t                              %! baca.SegmentMaker._style_phantom_measures(3):PHANTOM
            <BLANKLINE>
                    }                                                                                %! abjad.ScoreTemplate._make_global_context()
            <BLANKLINE>
                >>                                                                                   %! abjad.ScoreTemplate._make_global_context()
            <BLANKLINE>
                \context MusicContext = "Music_Context"                                              %! baca.SingleStaffScoreTemplate.__call__()
                <<                                                                                   %! baca.SingleStaffScoreTemplate.__call__()
            <BLANKLINE>
                    \context Staff = "Music_Staff"                                                   %! baca.SingleStaffScoreTemplate.__call__()
                    {                                                                                %! baca.SingleStaffScoreTemplate.__call__()
            <BLANKLINE>
                        \context Voice = "Music_Voice"                                               %! baca.SingleStaffScoreTemplate.__call__()
                        {                                                                            %! baca.SingleStaffScoreTemplate.__call__()
            <BLANKLINE>
                            % [Music_Voice measure 1]                                                %! baca.SegmentMaker._comment_measure_numbers()
                        %@% \baca-not-yet-pitched-coloring                                           %! baca.SegmentMaker._color_not_yet_pitched():NOT_YET_PITCHED_COLORING
                            b'4.                                                                     %! baca.make_notes()
                            ^ \baca-reapplied-indicator-markup "(“Flute”)"                           %! REAPPLIED_INSTRUMENT_ALERT:baca.SegmentMaker._attach_latent_indicator_alert()
            <BLANKLINE>
                            % [Music_Voice measure 2]                                                %! baca.SegmentMaker._comment_measure_numbers()
                        %@% \baca-not-yet-pitched-coloring                                           %! baca.SegmentMaker._color_not_yet_pitched():NOT_YET_PITCHED_COLORING
                            b'4.                                                                     %! baca.make_notes()
            <BLANKLINE>
                            <<                                                                       %! baca.SegmentMaker._make_multimeasure_rest_container(7):PHANTOM
            <BLANKLINE>
                                \context Voice = "Music_Voice"                                       %! baca.SegmentMaker._make_multimeasure_rest_container(4):PHANTOM
                                {                                                                    %! baca.SegmentMaker._make_multimeasure_rest_container(4):PHANTOM
            <BLANKLINE>
                                    % [Music_Voice measure 3]                                        %! baca.SegmentMaker._comment_measure_numbers():baca.SegmentMaker._style_phantom_measures(5):PHANTOM
                                    \abjad-invisible-music-coloring                                  %! baca.SegmentMaker._make_multimeasure_rest_container(2):PHANTOM:NOTE:INVISIBLE_MUSIC_COLORING:baca.SegmentMaker._style_phantom_measures(5)
                                %@% \abjad-invisible-music                                           %! baca.SegmentMaker._make_multimeasure_rest_container(3):PHANTOM:NOTE:INVISIBLE_MUSIC_COMMAND:baca.SegmentMaker._style_phantom_measures(5)
                                %@% \baca-not-yet-pitched-coloring                                   %! baca.SegmentMaker._color_not_yet_pitched():NOT_YET_PITCHED_COLORING:HIDDEN:NOTE:baca.SegmentMaker._style_phantom_measures(5):PHANTOM
                                    b'1 * 1/4                                                        %! baca.SegmentMaker._make_multimeasure_rest_container(1):PHANTOM:HIDDEN:NOTE
                                %@% ^ \baca-duration-multiplier-markup #"1" #"4"                     %! baca.SegmentMaker._label_duration_multipliers():DURATION_MULTIPLIER:HIDDEN:NOTE:PHANTOM:baca.SegmentMaker._style_phantom_measures(5)
            <BLANKLINE>
                                }                                                                    %! baca.SegmentMaker._make_multimeasure_rest_container(4):PHANTOM
            <BLANKLINE>
                                \context Voice = "Rest_Voice"                                        %! baca.SegmentMaker._make_multimeasure_rest_container(6):PHANTOM
                                {                                                                    %! baca.SegmentMaker._make_multimeasure_rest_container(6):PHANTOM
            <BLANKLINE>
                                    % [Rest_Voice measure 3]                                         %! baca.SegmentMaker._comment_measure_numbers():baca.SegmentMaker._style_phantom_measures(5):PHANTOM
                                    \once \override Score.TimeSignature.X-extent = ##f               %! baca.SegmentMaker._style_phantom_measures(6):PHANTOM
                                    \once \override MultiMeasureRest.transparent = ##t               %! baca.SegmentMaker._style_phantom_measures(7):PHANTOM
                                    \stopStaff                                                       %! baca.SegmentMaker._style_phantom_measures(8):PHANTOM
                                    \once \override Staff.StaffSymbol.transparent = ##t              %! baca.SegmentMaker._style_phantom_measures(8):PHANTOM
                                    \startStaff                                                      %! baca.SegmentMaker._style_phantom_measures(8):PHANTOM
                                    R1 * 1/4                                                         %! baca.SegmentMaker._make_multimeasure_rest_container(5):PHANTOM:REST_VOICE:MULTIMEASURE_REST
                                %@% ^ \baca-duration-multiplier-markup #"1" #"4"                     %! baca.SegmentMaker._label_duration_multipliers():DURATION_MULTIPLIER:MULTIMEASURE_REST:PHANTOM:REST_VOICE:baca.SegmentMaker._style_phantom_measures(5)
            <BLANKLINE>
                                }                                                                    %! baca.SegmentMaker._make_multimeasure_rest_container(6):PHANTOM
            <BLANKLINE>
                            >>                                                                       %! baca.SegmentMaker._make_multimeasure_rest_container(7):PHANTOM
            <BLANKLINE>
                        }                                                                            %! baca.SingleStaffScoreTemplate.__call__()
            <BLANKLINE>
                    }                                                                                %! baca.SingleStaffScoreTemplate.__call__()
            <BLANKLINE>
                >>                                                                                   %! baca.SingleStaffScoreTemplate.__call__()
            <BLANKLINE>
            >>                                                                                       %! baca.SingleStaffScoreTemplate.__call__()

        >>> score = lilypond_file[abjad.Score]
        >>> text = format(score, 'lilypond')
        >>> text = abjad.LilyPondFormatManager.left_shift_tags(text)
        >>> tags_ = abjad.tags.instrument_color_tags()
        >>> match = lambda tags: bool(set(tags) & set(tags_))
        >>> text, count = abjad.deactivate(text, match)
        >>> text = abjad.LilyPondFormatManager.left_shift_tags(text, 89)
        >>> lines = [_.strip('\n') for _ in text.split('\n')]
        >>> lilypond_file.score_block.items[:] = lines
        >>> abjad.show(lilypond_file, strict=89) # doctest: +SKIP

        ..  docs::

            >>> print(text)
            <BLANKLINE>
            \context Score = "Score"                                                                 %! baca.SingleStaffScoreTemplate.__call__()
            <<                                                                                       %! baca.SingleStaffScoreTemplate.__call__()
            <BLANKLINE>
                \context GlobalContext = "Global_Context"                                            %! abjad.ScoreTemplate._make_global_context()
                <<                                                                                   %! abjad.ScoreTemplate._make_global_context()
            <BLANKLINE>
                    \context GlobalSkips = "Global_Skips"                                            %! abjad.ScoreTemplate._make_global_context()
                    {                                                                                %! abjad.ScoreTemplate._make_global_context()
            <BLANKLINE>
                        % [Global_Skips measure 1]                                                   %! baca.SegmentMaker._comment_measure_numbers()
                        \baca-new-spacing-section #1 #24                                             %! SPACING_COMMAND:baca.HorizontalSpacingSpecifier.__call__(1)
                        \autoPageBreaksOff                                                           %! BREAK:baca.BreakMeasureMap.__call__(1)
                        \noBreak                                                                     %! BREAK:baca.BreakMeasureMap.__call__(2)
                        \baca-lbsd #0 #'(11)                                                         %! BREAK:baca.IndicatorCommand._call()
                        \time 3/8                                                                    %! baca.SegmentMaker._make_global_skips(2):baca.SegmentMaker._set_status_tag():EXPLICIT_TIME_SIGNATURE
                        \bar ""                                                                      %! EMPTY_START_BAR:+SEGMENT:baca.SegmentMaker._make_global_skips(4)
                        \baca-time-signature-color #'blue                                            %! baca.SegmentMaker._attach_color_literal(2):EXPLICIT_TIME_SIGNATURE_COLOR
                        \pageBreak                                                                   %! BREAK:baca.IndicatorCommand._call()
                        s1 * 3/8                                                                     %! baca.SegmentMaker._make_global_skips(1)
            <BLANKLINE>
                        % [Global_Skips measure 2]                                                   %! baca.SegmentMaker._comment_measure_numbers()
                        \baca-new-spacing-section #1 #24                                             %! SPACING_COMMAND:baca.HorizontalSpacingSpecifier.__call__(1)
                        \noBreak                                                                     %! BREAK:baca.BreakMeasureMap.__call__(2)
                        \baca-lbsd #15 #'(11)                                                        %! BREAK:baca.IndicatorCommand._call()
                        \break                                                                       %! BREAK:baca.IndicatorCommand._call()
                        s1 * 3/8                                                                     %! baca.SegmentMaker._make_global_skips(1)
            <BLANKLINE>
                        % [Global_Skips measure 3]                                                   %! baca.SegmentMaker._comment_measure_numbers():baca.SegmentMaker._style_phantom_measures(1):PHANTOM
                        \baca-new-spacing-section #1 #4                                              %! SPACING_COMMAND:baca.HorizontalSpacingSpecifier.__call__(1):baca.SegmentMaker._style_phantom_measures(1):PHANTOM
                        \noBreak                                                                     %! BREAK:baca.BreakMeasureMap.__call__(2):baca.SegmentMaker._style_phantom_measures(1):PHANTOM
                        \time 1/4                                                                    %! baca.SegmentMaker._make_global_skips(3):PHANTOM:baca.SegmentMaker._set_status_tag():EXPLICIT_TIME_SIGNATURE:baca.SegmentMaker._style_phantom_measures(1)
                        \baca-time-signature-transparent                                             %! baca.SegmentMaker._style_phantom_measures(2):PHANTOM
                        s1 * 1/4                                                                     %! baca.SegmentMaker._make_global_skips(3):PHANTOM
                        \once \override Score.BarLine.transparent = ##t                              %! baca.SegmentMaker._style_phantom_measures(3):PHANTOM
                        \once \override Score.SpanBar.transparent = ##t                              %! baca.SegmentMaker._style_phantom_measures(3):PHANTOM
            <BLANKLINE>
                    }                                                                                %! abjad.ScoreTemplate._make_global_context()
            <BLANKLINE>
                >>                                                                                   %! abjad.ScoreTemplate._make_global_context()
            <BLANKLINE>
                \context MusicContext = "Music_Context"                                              %! baca.SingleStaffScoreTemplate.__call__()
                <<                                                                                   %! baca.SingleStaffScoreTemplate.__call__()
            <BLANKLINE>
                    \context Staff = "Music_Staff"                                                   %! baca.SingleStaffScoreTemplate.__call__()
                    {                                                                                %! baca.SingleStaffScoreTemplate.__call__()
            <BLANKLINE>
                        \context Voice = "Music_Voice"                                               %! baca.SingleStaffScoreTemplate.__call__()
                        {                                                                            %! baca.SingleStaffScoreTemplate.__call__()
            <BLANKLINE>
                            % [Music_Voice measure 1]                                                %! baca.SegmentMaker._comment_measure_numbers()
                    %@% \baca-not-yet-pitched-coloring                                               %! baca.SegmentMaker._color_not_yet_pitched():NOT_YET_PITCHED_COLORING
                            b'4.                                                                     %! baca.make_notes()
                        %%% ^ \baca-reapplied-indicator-markup "(“Flute”)"                           %! REAPPLIED_INSTRUMENT_ALERT:baca.SegmentMaker._attach_latent_indicator_alert()
            <BLANKLINE>
                            % [Music_Voice measure 2]                                                %! baca.SegmentMaker._comment_measure_numbers()
                    %@% \baca-not-yet-pitched-coloring                                               %! baca.SegmentMaker._color_not_yet_pitched():NOT_YET_PITCHED_COLORING
                            b'4.                                                                     %! baca.make_notes()
            <BLANKLINE>
                            <<                                                                       %! baca.SegmentMaker._make_multimeasure_rest_container(7):PHANTOM
            <BLANKLINE>
                                \context Voice = "Music_Voice"                                       %! baca.SegmentMaker._make_multimeasure_rest_container(4):PHANTOM
                                {                                                                    %! baca.SegmentMaker._make_multimeasure_rest_container(4):PHANTOM
            <BLANKLINE>
                                    % [Music_Voice measure 3]                                        %! baca.SegmentMaker._comment_measure_numbers():baca.SegmentMaker._style_phantom_measures(5):PHANTOM
                                    \abjad-invisible-music-coloring                                  %! baca.SegmentMaker._make_multimeasure_rest_container(2):PHANTOM:NOTE:INVISIBLE_MUSIC_COLORING:baca.SegmentMaker._style_phantom_measures(5)
                            %@% \abjad-invisible-music                                               %! baca.SegmentMaker._make_multimeasure_rest_container(3):PHANTOM:NOTE:INVISIBLE_MUSIC_COMMAND:baca.SegmentMaker._style_phantom_measures(5)
                            %@% \baca-not-yet-pitched-coloring                                       %! baca.SegmentMaker._color_not_yet_pitched():NOT_YET_PITCHED_COLORING:HIDDEN:NOTE:baca.SegmentMaker._style_phantom_measures(5):PHANTOM
                                    b'1 * 1/4                                                        %! baca.SegmentMaker._make_multimeasure_rest_container(1):PHANTOM:HIDDEN:NOTE
                            %@% ^ \baca-duration-multiplier-markup #"1" #"4"                         %! baca.SegmentMaker._label_duration_multipliers():DURATION_MULTIPLIER:HIDDEN:NOTE:PHANTOM:baca.SegmentMaker._style_phantom_measures(5)
            <BLANKLINE>
                                }                                                                    %! baca.SegmentMaker._make_multimeasure_rest_container(4):PHANTOM
            <BLANKLINE>
                                \context Voice = "Rest_Voice"                                        %! baca.SegmentMaker._make_multimeasure_rest_container(6):PHANTOM
                                {                                                                    %! baca.SegmentMaker._make_multimeasure_rest_container(6):PHANTOM
            <BLANKLINE>
                                    % [Rest_Voice measure 3]                                         %! baca.SegmentMaker._comment_measure_numbers():baca.SegmentMaker._style_phantom_measures(5):PHANTOM
                                    \once \override Score.TimeSignature.X-extent = ##f               %! baca.SegmentMaker._style_phantom_measures(6):PHANTOM
                                    \once \override MultiMeasureRest.transparent = ##t               %! baca.SegmentMaker._style_phantom_measures(7):PHANTOM
                                    \stopStaff                                                       %! baca.SegmentMaker._style_phantom_measures(8):PHANTOM
                                    \once \override Staff.StaffSymbol.transparent = ##t              %! baca.SegmentMaker._style_phantom_measures(8):PHANTOM
                                    \startStaff                                                      %! baca.SegmentMaker._style_phantom_measures(8):PHANTOM
                                    R1 * 1/4                                                         %! baca.SegmentMaker._make_multimeasure_rest_container(5):PHANTOM:REST_VOICE:MULTIMEASURE_REST
                            %@% ^ \baca-duration-multiplier-markup #"1" #"4"                         %! baca.SegmentMaker._label_duration_multipliers():DURATION_MULTIPLIER:MULTIMEASURE_REST:PHANTOM:REST_VOICE:baca.SegmentMaker._style_phantom_measures(5)
            <BLANKLINE>
                                }                                                                    %! baca.SegmentMaker._make_multimeasure_rest_container(6):PHANTOM
            <BLANKLINE>
                            >>                                                                       %! baca.SegmentMaker._make_multimeasure_rest_container(7):PHANTOM
            <BLANKLINE>
                        }                                                                            %! baca.SingleStaffScoreTemplate.__call__()
            <BLANKLINE>
                    }                                                                                %! baca.SingleStaffScoreTemplate.__call__()
            <BLANKLINE>
                >>                                                                                   %! baca.SingleStaffScoreTemplate.__call__()
            <BLANKLINE>
            >>                                                                                       %! baca.SingleStaffScoreTemplate.__call__()

        >>> tags_ = abjad.tags.instrument_color_tags()
        >>> match = lambda tags: bool(set(tags) & set(tags_))
        >>> text, count = abjad.activate(text, match)
        >>> text = abjad.LilyPondFormatManager.left_shift_tags(text, 89)
        >>> lines = [_.strip('\n') for _ in text.split('\n')]
        >>> lilypond_file.score_block.items[:] = lines
        >>> abjad.show(lilypond_file, strict=89) # doctest: +SKIP

        ..  docs::

            >>> print(text)
            <BLANKLINE>
            \context Score = "Score"                                                                 %! baca.SingleStaffScoreTemplate.__call__()
            <<                                                                                       %! baca.SingleStaffScoreTemplate.__call__()
            <BLANKLINE>
                \context GlobalContext = "Global_Context"                                            %! abjad.ScoreTemplate._make_global_context()
                <<                                                                                   %! abjad.ScoreTemplate._make_global_context()
            <BLANKLINE>
                    \context GlobalSkips = "Global_Skips"                                            %! abjad.ScoreTemplate._make_global_context()
                    {                                                                                %! abjad.ScoreTemplate._make_global_context()
            <BLANKLINE>
                        % [Global_Skips measure 1]                                                   %! baca.SegmentMaker._comment_measure_numbers()
                        \baca-new-spacing-section #1 #24                                             %! SPACING_COMMAND:baca.HorizontalSpacingSpecifier.__call__(1)
                        \autoPageBreaksOff                                                           %! BREAK:baca.BreakMeasureMap.__call__(1)
                        \noBreak                                                                     %! BREAK:baca.BreakMeasureMap.__call__(2)
                        \baca-lbsd #0 #'(11)                                                         %! BREAK:baca.IndicatorCommand._call()
                        \time 3/8                                                                    %! baca.SegmentMaker._make_global_skips(2):baca.SegmentMaker._set_status_tag():EXPLICIT_TIME_SIGNATURE
                        \bar ""                                                                      %! EMPTY_START_BAR:+SEGMENT:baca.SegmentMaker._make_global_skips(4)
                        \baca-time-signature-color #'blue                                            %! baca.SegmentMaker._attach_color_literal(2):EXPLICIT_TIME_SIGNATURE_COLOR
                        \pageBreak                                                                   %! BREAK:baca.IndicatorCommand._call()
                        s1 * 3/8                                                                     %! baca.SegmentMaker._make_global_skips(1)
            <BLANKLINE>
                        % [Global_Skips measure 2]                                                   %! baca.SegmentMaker._comment_measure_numbers()
                        \baca-new-spacing-section #1 #24                                             %! SPACING_COMMAND:baca.HorizontalSpacingSpecifier.__call__(1)
                        \noBreak                                                                     %! BREAK:baca.BreakMeasureMap.__call__(2)
                        \baca-lbsd #15 #'(11)                                                        %! BREAK:baca.IndicatorCommand._call()
                        \break                                                                       %! BREAK:baca.IndicatorCommand._call()
                        s1 * 3/8                                                                     %! baca.SegmentMaker._make_global_skips(1)
            <BLANKLINE>
                        % [Global_Skips measure 3]                                                   %! baca.SegmentMaker._comment_measure_numbers():baca.SegmentMaker._style_phantom_measures(1):PHANTOM
                        \baca-new-spacing-section #1 #4                                              %! SPACING_COMMAND:baca.HorizontalSpacingSpecifier.__call__(1):baca.SegmentMaker._style_phantom_measures(1):PHANTOM
                        \noBreak                                                                     %! BREAK:baca.BreakMeasureMap.__call__(2):baca.SegmentMaker._style_phantom_measures(1):PHANTOM
                        \time 1/4                                                                    %! baca.SegmentMaker._make_global_skips(3):PHANTOM:baca.SegmentMaker._set_status_tag():EXPLICIT_TIME_SIGNATURE:baca.SegmentMaker._style_phantom_measures(1)
                        \baca-time-signature-transparent                                             %! baca.SegmentMaker._style_phantom_measures(2):PHANTOM
                        s1 * 1/4                                                                     %! baca.SegmentMaker._make_global_skips(3):PHANTOM
                        \once \override Score.BarLine.transparent = ##t                              %! baca.SegmentMaker._style_phantom_measures(3):PHANTOM
                        \once \override Score.SpanBar.transparent = ##t                              %! baca.SegmentMaker._style_phantom_measures(3):PHANTOM
            <BLANKLINE>
                    }                                                                                %! abjad.ScoreTemplate._make_global_context()
            <BLANKLINE>
                >>                                                                                   %! abjad.ScoreTemplate._make_global_context()
            <BLANKLINE>
                \context MusicContext = "Music_Context"                                              %! baca.SingleStaffScoreTemplate.__call__()
                <<                                                                                   %! baca.SingleStaffScoreTemplate.__call__()
            <BLANKLINE>
                    \context Staff = "Music_Staff"                                                   %! baca.SingleStaffScoreTemplate.__call__()
                    {                                                                                %! baca.SingleStaffScoreTemplate.__call__()
            <BLANKLINE>
                        \context Voice = "Music_Voice"                                               %! baca.SingleStaffScoreTemplate.__call__()
                        {                                                                            %! baca.SingleStaffScoreTemplate.__call__()
            <BLANKLINE>
                            % [Music_Voice measure 1]                                                %! baca.SegmentMaker._comment_measure_numbers()
                %@% \baca-not-yet-pitched-coloring                                                   %! baca.SegmentMaker._color_not_yet_pitched():NOT_YET_PITCHED_COLORING
                            b'4.                                                                     %! baca.make_notes()
                            ^ \baca-reapplied-indicator-markup "(“Flute”)"                           %! REAPPLIED_INSTRUMENT_ALERT:baca.SegmentMaker._attach_latent_indicator_alert()
            <BLANKLINE>
                            % [Music_Voice measure 2]                                                %! baca.SegmentMaker._comment_measure_numbers()
                %@% \baca-not-yet-pitched-coloring                                                   %! baca.SegmentMaker._color_not_yet_pitched():NOT_YET_PITCHED_COLORING
                            b'4.                                                                     %! baca.make_notes()
            <BLANKLINE>
                            <<                                                                       %! baca.SegmentMaker._make_multimeasure_rest_container(7):PHANTOM
            <BLANKLINE>
                                \context Voice = "Music_Voice"                                       %! baca.SegmentMaker._make_multimeasure_rest_container(4):PHANTOM
                                {                                                                    %! baca.SegmentMaker._make_multimeasure_rest_container(4):PHANTOM
            <BLANKLINE>
                                    % [Music_Voice measure 3]                                        %! baca.SegmentMaker._comment_measure_numbers():baca.SegmentMaker._style_phantom_measures(5):PHANTOM
                                    \abjad-invisible-music-coloring                                  %! baca.SegmentMaker._make_multimeasure_rest_container(2):PHANTOM:NOTE:INVISIBLE_MUSIC_COLORING:baca.SegmentMaker._style_phantom_measures(5)
                        %@% \abjad-invisible-music                                                   %! baca.SegmentMaker._make_multimeasure_rest_container(3):PHANTOM:NOTE:INVISIBLE_MUSIC_COMMAND:baca.SegmentMaker._style_phantom_measures(5)
                        %@% \baca-not-yet-pitched-coloring                                           %! baca.SegmentMaker._color_not_yet_pitched():NOT_YET_PITCHED_COLORING:HIDDEN:NOTE:baca.SegmentMaker._style_phantom_measures(5):PHANTOM
                                    b'1 * 1/4                                                        %! baca.SegmentMaker._make_multimeasure_rest_container(1):PHANTOM:HIDDEN:NOTE
                        %@% ^ \baca-duration-multiplier-markup #"1" #"4"                             %! baca.SegmentMaker._label_duration_multipliers():DURATION_MULTIPLIER:HIDDEN:NOTE:PHANTOM:baca.SegmentMaker._style_phantom_measures(5)
            <BLANKLINE>
                                }                                                                    %! baca.SegmentMaker._make_multimeasure_rest_container(4):PHANTOM
            <BLANKLINE>
                                \context Voice = "Rest_Voice"                                        %! baca.SegmentMaker._make_multimeasure_rest_container(6):PHANTOM
                                {                                                                    %! baca.SegmentMaker._make_multimeasure_rest_container(6):PHANTOM
            <BLANKLINE>
                                    % [Rest_Voice measure 3]                                         %! baca.SegmentMaker._comment_measure_numbers():baca.SegmentMaker._style_phantom_measures(5):PHANTOM
                                    \once \override Score.TimeSignature.X-extent = ##f               %! baca.SegmentMaker._style_phantom_measures(6):PHANTOM
                                    \once \override MultiMeasureRest.transparent = ##t               %! baca.SegmentMaker._style_phantom_measures(7):PHANTOM
                                    \stopStaff                                                       %! baca.SegmentMaker._style_phantom_measures(8):PHANTOM
                                    \once \override Staff.StaffSymbol.transparent = ##t              %! baca.SegmentMaker._style_phantom_measures(8):PHANTOM
                                    \startStaff                                                      %! baca.SegmentMaker._style_phantom_measures(8):PHANTOM
                                    R1 * 1/4                                                         %! baca.SegmentMaker._make_multimeasure_rest_container(5):PHANTOM:REST_VOICE:MULTIMEASURE_REST
                        %@% ^ \baca-duration-multiplier-markup #"1" #"4"                             %! baca.SegmentMaker._label_duration_multipliers():DURATION_MULTIPLIER:MULTIMEASURE_REST:PHANTOM:REST_VOICE:baca.SegmentMaker._style_phantom_measures(5)
            <BLANKLINE>
                                }                                                                    %! baca.SegmentMaker._make_multimeasure_rest_container(6):PHANTOM
            <BLANKLINE>
                            >>                                                                       %! baca.SegmentMaker._make_multimeasure_rest_container(7):PHANTOM
            <BLANKLINE>
                        }                                                                            %! baca.SingleStaffScoreTemplate.__call__()
            <BLANKLINE>
                    }                                                                                %! baca.SingleStaffScoreTemplate.__call__()
            <BLANKLINE>
                >>                                                                                   %! baca.SingleStaffScoreTemplate.__call__()
            <BLANKLINE>
            >>                                                                                       %! baca.SingleStaffScoreTemplate.__call__()

    ..  container:: example

        Redundant instruments color pink and redraw dull pink:

        >>> breaks = baca.breaks(
        ...     baca.page(
        ...         [1, 0, (11,)],
        ...         [3, 15, (11,)],
        ...         ),
        ...     )
        >>> maker = baca.SegmentMaker(
        ...     breaks=breaks,
        ...     deactivate=[abjad.tags.NOT_YET_PITCHED_COLORING],
        ...     instruments=instruments,
        ...     score_template=baca.SingleStaffScoreTemplate(),
        ...     spacing=baca.minimum_duration((1, 24)),
        ...     time_signatures=[(4, 8), (4, 8), (4, 8)],
        ...     )
        >>> maker(
        ...     'Music_Voice',
        ...     baca.instrument(instruments['Flute']),
        ...     baca.new(
        ...         baca.instrument(instruments['Flute']),
        ...         map=baca.leaves()[1],
        ...         ),
        ...     baca.make_notes(),
        ...     )

        >>> lilypond_file = maker.run(environment='docs')
        >>> block = abjad.Block(name='layout')
        >>> block.indent = 0
        >>> lilypond_file.items.insert(0, block)
        >>> abjad.show(lilypond_file, strict=89) # doctest: +SKIP

        ..  docs::

            >>> abjad.f(lilypond_file[abjad.Score], strict=89)
            <BLANKLINE>
            \context Score = "Score"                                                                 %! baca.SingleStaffScoreTemplate.__call__()
            <<                                                                                       %! baca.SingleStaffScoreTemplate.__call__()
            <BLANKLINE>
                \context GlobalContext = "Global_Context"                                            %! abjad.ScoreTemplate._make_global_context()
                <<                                                                                   %! abjad.ScoreTemplate._make_global_context()
            <BLANKLINE>
                    \context GlobalSkips = "Global_Skips"                                            %! abjad.ScoreTemplate._make_global_context()
                    {                                                                                %! abjad.ScoreTemplate._make_global_context()
            <BLANKLINE>
                        % [Global_Skips measure 1]                                                   %! baca.SegmentMaker._comment_measure_numbers()
                        \baca-new-spacing-section #1 #24                                             %! SPACING_COMMAND:baca.HorizontalSpacingSpecifier.__call__(1)
                        \autoPageBreaksOff                                                           %! BREAK:baca.BreakMeasureMap.__call__(1)
                        \noBreak                                                                     %! BREAK:baca.BreakMeasureMap.__call__(2)
                        \baca-lbsd #0 #'(11)                                                         %! BREAK:baca.IndicatorCommand._call()
                        \time 4/8                                                                    %! baca.SegmentMaker._make_global_skips(2):baca.SegmentMaker._set_status_tag():EXPLICIT_TIME_SIGNATURE
                        \baca-time-signature-color #'blue                                            %! baca.SegmentMaker._attach_color_literal(2):EXPLICIT_TIME_SIGNATURE_COLOR
                        \pageBreak                                                                   %! BREAK:baca.IndicatorCommand._call()
                        s1 * 1/2                                                                     %! baca.SegmentMaker._make_global_skips(1)
            <BLANKLINE>
                        % [Global_Skips measure 2]                                                   %! baca.SegmentMaker._comment_measure_numbers()
                        \baca-new-spacing-section #1 #24                                             %! SPACING_COMMAND:baca.HorizontalSpacingSpecifier.__call__(1)
                        \noBreak                                                                     %! BREAK:baca.BreakMeasureMap.__call__(2)
                        s1 * 1/2                                                                     %! baca.SegmentMaker._make_global_skips(1)
            <BLANKLINE>
                        % [Global_Skips measure 3]                                                   %! baca.SegmentMaker._comment_measure_numbers()
                        \baca-new-spacing-section #1 #24                                             %! SPACING_COMMAND:baca.HorizontalSpacingSpecifier.__call__(1)
                        \noBreak                                                                     %! BREAK:baca.BreakMeasureMap.__call__(2)
                        \baca-lbsd #15 #'(11)                                                        %! BREAK:baca.IndicatorCommand._call()
                        \break                                                                       %! BREAK:baca.IndicatorCommand._call()
                        s1 * 1/2                                                                     %! baca.SegmentMaker._make_global_skips(1)
            <BLANKLINE>
                        % [Global_Skips measure 4]                                                   %! baca.SegmentMaker._comment_measure_numbers():baca.SegmentMaker._style_phantom_measures(1):PHANTOM
                        \baca-new-spacing-section #1 #4                                              %! SPACING_COMMAND:baca.HorizontalSpacingSpecifier.__call__(1):baca.SegmentMaker._style_phantom_measures(1):PHANTOM
                        \noBreak                                                                     %! BREAK:baca.BreakMeasureMap.__call__(2):baca.SegmentMaker._style_phantom_measures(1):PHANTOM
                        \time 1/4                                                                    %! baca.SegmentMaker._make_global_skips(3):PHANTOM:baca.SegmentMaker._set_status_tag():EXPLICIT_TIME_SIGNATURE:baca.SegmentMaker._style_phantom_measures(1)
                        \baca-time-signature-transparent                                             %! baca.SegmentMaker._style_phantom_measures(2):PHANTOM
                        s1 * 1/4                                                                     %! baca.SegmentMaker._make_global_skips(3):PHANTOM
                        \once \override Score.BarLine.transparent = ##t                              %! baca.SegmentMaker._style_phantom_measures(3):PHANTOM
                        \once \override Score.SpanBar.transparent = ##t                              %! baca.SegmentMaker._style_phantom_measures(3):PHANTOM
            <BLANKLINE>
                    }                                                                                %! abjad.ScoreTemplate._make_global_context()
            <BLANKLINE>
                >>                                                                                   %! abjad.ScoreTemplate._make_global_context()
            <BLANKLINE>
                \context MusicContext = "Music_Context"                                              %! baca.SingleStaffScoreTemplate.__call__()
                <<                                                                                   %! baca.SingleStaffScoreTemplate.__call__()
            <BLANKLINE>
                    \context Staff = "Music_Staff"                                                   %! baca.SingleStaffScoreTemplate.__call__()
                    {                                                                                %! baca.SingleStaffScoreTemplate.__call__()
            <BLANKLINE>
                        \context Voice = "Music_Voice"                                               %! baca.SingleStaffScoreTemplate.__call__()
                        {                                                                            %! baca.SingleStaffScoreTemplate.__call__()
            <BLANKLINE>
                            % [Music_Voice measure 1]                                                %! baca.SegmentMaker._comment_measure_numbers()
                        %@% \baca-not-yet-pitched-coloring                                           %! baca.SegmentMaker._color_not_yet_pitched():NOT_YET_PITCHED_COLORING
                            b'2                                                                      %! baca.make_notes()
                            ^ \baca-explicit-indicator-markup "(“Flute”)"                            %! EXPLICIT_INSTRUMENT_ALERT:baca.SegmentMaker._attach_latent_indicator_alert()
            <BLANKLINE>
                            % [Music_Voice measure 2]                                                %! baca.SegmentMaker._comment_measure_numbers()
                        %@% \baca-not-yet-pitched-coloring                                           %! baca.SegmentMaker._color_not_yet_pitched():NOT_YET_PITCHED_COLORING
                            b'2                                                                      %! baca.make_notes()
                            ^ \baca-redundant-indicator-markup "(“Flute”)"                           %! REDUNDANT_INSTRUMENT_ALERT:baca.SegmentMaker._attach_latent_indicator_alert()
            <BLANKLINE>
                            % [Music_Voice measure 3]                                                %! baca.SegmentMaker._comment_measure_numbers()
                        %@% \baca-not-yet-pitched-coloring                                           %! baca.SegmentMaker._color_not_yet_pitched():NOT_YET_PITCHED_COLORING
                            b'2                                                                      %! baca.make_notes()
            <BLANKLINE>
                            <<                                                                       %! baca.SegmentMaker._make_multimeasure_rest_container(7):PHANTOM
            <BLANKLINE>
                                \context Voice = "Music_Voice"                                       %! baca.SegmentMaker._make_multimeasure_rest_container(4):PHANTOM
                                {                                                                    %! baca.SegmentMaker._make_multimeasure_rest_container(4):PHANTOM
            <BLANKLINE>
                                    % [Music_Voice measure 4]                                        %! baca.SegmentMaker._comment_measure_numbers():baca.SegmentMaker._style_phantom_measures(5):PHANTOM
                                    \abjad-invisible-music-coloring                                  %! baca.SegmentMaker._make_multimeasure_rest_container(2):PHANTOM:NOTE:INVISIBLE_MUSIC_COLORING:baca.SegmentMaker._style_phantom_measures(5)
                                %@% \abjad-invisible-music                                           %! baca.SegmentMaker._make_multimeasure_rest_container(3):PHANTOM:NOTE:INVISIBLE_MUSIC_COMMAND:baca.SegmentMaker._style_phantom_measures(5)
                                %@% \baca-not-yet-pitched-coloring                                   %! baca.SegmentMaker._color_not_yet_pitched():NOT_YET_PITCHED_COLORING:HIDDEN:NOTE:baca.SegmentMaker._style_phantom_measures(5):PHANTOM
                                    b'1 * 1/4                                                        %! baca.SegmentMaker._make_multimeasure_rest_container(1):PHANTOM:HIDDEN:NOTE
                                %@% ^ \baca-duration-multiplier-markup #"1" #"4"                     %! baca.SegmentMaker._label_duration_multipliers():DURATION_MULTIPLIER:HIDDEN:NOTE:PHANTOM:baca.SegmentMaker._style_phantom_measures(5)
            <BLANKLINE>
                                }                                                                    %! baca.SegmentMaker._make_multimeasure_rest_container(4):PHANTOM
            <BLANKLINE>
                                \context Voice = "Rest_Voice"                                        %! baca.SegmentMaker._make_multimeasure_rest_container(6):PHANTOM
                                {                                                                    %! baca.SegmentMaker._make_multimeasure_rest_container(6):PHANTOM
            <BLANKLINE>
                                    % [Rest_Voice measure 4]                                         %! baca.SegmentMaker._comment_measure_numbers():baca.SegmentMaker._style_phantom_measures(5):PHANTOM
                                    \once \override Score.TimeSignature.X-extent = ##f               %! baca.SegmentMaker._style_phantom_measures(6):PHANTOM
                                    \once \override MultiMeasureRest.transparent = ##t               %! baca.SegmentMaker._style_phantom_measures(7):PHANTOM
                                    \stopStaff                                                       %! baca.SegmentMaker._style_phantom_measures(8):PHANTOM
                                    \once \override Staff.StaffSymbol.transparent = ##t              %! baca.SegmentMaker._style_phantom_measures(8):PHANTOM
                                    \startStaff                                                      %! baca.SegmentMaker._style_phantom_measures(8):PHANTOM
                                    R1 * 1/4                                                         %! baca.SegmentMaker._make_multimeasure_rest_container(5):PHANTOM:REST_VOICE:MULTIMEASURE_REST
                                %@% ^ \baca-duration-multiplier-markup #"1" #"4"                     %! baca.SegmentMaker._label_duration_multipliers():DURATION_MULTIPLIER:MULTIMEASURE_REST:PHANTOM:REST_VOICE:baca.SegmentMaker._style_phantom_measures(5)
            <BLANKLINE>
                                }                                                                    %! baca.SegmentMaker._make_multimeasure_rest_container(6):PHANTOM
            <BLANKLINE>
                            >>                                                                       %! baca.SegmentMaker._make_multimeasure_rest_container(7):PHANTOM
            <BLANKLINE>
                        }                                                                            %! baca.SingleStaffScoreTemplate.__call__()
            <BLANKLINE>
                    }                                                                                %! baca.SingleStaffScoreTemplate.__call__()
            <BLANKLINE>
                >>                                                                                   %! baca.SingleStaffScoreTemplate.__call__()
            <BLANKLINE>
            >>                                                                                       %! baca.SingleStaffScoreTemplate.__call__()

        >>> score = lilypond_file[abjad.Score]
        >>> text = format(score, 'lilypond')
        >>> text = abjad.LilyPondFormatManager.left_shift_tags(text)
        >>> tags_ = abjad.tags.instrument_color_tags()
        >>> match = lambda tags: bool(set(tags) & set(tags_))
        >>> text, count = abjad.deactivate(text, match)
        >>> text = abjad.LilyPondFormatManager.left_shift_tags(text, 89)
        >>> lines = [_.strip('\n') for _ in text.split('\n')]
        >>> lilypond_file.score_block.items[:] = lines
        >>> abjad.show(lilypond_file, strict=89) # doctest: +SKIP

        ..  docs::

            >>> print(text)
            <BLANKLINE>
            \context Score = "Score"                                                                 %! baca.SingleStaffScoreTemplate.__call__()
            <<                                                                                       %! baca.SingleStaffScoreTemplate.__call__()
            <BLANKLINE>
                \context GlobalContext = "Global_Context"                                            %! abjad.ScoreTemplate._make_global_context()
                <<                                                                                   %! abjad.ScoreTemplate._make_global_context()
            <BLANKLINE>
                    \context GlobalSkips = "Global_Skips"                                            %! abjad.ScoreTemplate._make_global_context()
                    {                                                                                %! abjad.ScoreTemplate._make_global_context()
            <BLANKLINE>
                        % [Global_Skips measure 1]                                                   %! baca.SegmentMaker._comment_measure_numbers()
                        \baca-new-spacing-section #1 #24                                             %! SPACING_COMMAND:baca.HorizontalSpacingSpecifier.__call__(1)
                        \autoPageBreaksOff                                                           %! BREAK:baca.BreakMeasureMap.__call__(1)
                        \noBreak                                                                     %! BREAK:baca.BreakMeasureMap.__call__(2)
                        \baca-lbsd #0 #'(11)                                                         %! BREAK:baca.IndicatorCommand._call()
                        \time 4/8                                                                    %! baca.SegmentMaker._make_global_skips(2):baca.SegmentMaker._set_status_tag():EXPLICIT_TIME_SIGNATURE
                        \baca-time-signature-color #'blue                                            %! baca.SegmentMaker._attach_color_literal(2):EXPLICIT_TIME_SIGNATURE_COLOR
                        \pageBreak                                                                   %! BREAK:baca.IndicatorCommand._call()
                        s1 * 1/2                                                                     %! baca.SegmentMaker._make_global_skips(1)
            <BLANKLINE>
                        % [Global_Skips measure 2]                                                   %! baca.SegmentMaker._comment_measure_numbers()
                        \baca-new-spacing-section #1 #24                                             %! SPACING_COMMAND:baca.HorizontalSpacingSpecifier.__call__(1)
                        \noBreak                                                                     %! BREAK:baca.BreakMeasureMap.__call__(2)
                        s1 * 1/2                                                                     %! baca.SegmentMaker._make_global_skips(1)
            <BLANKLINE>
                        % [Global_Skips measure 3]                                                   %! baca.SegmentMaker._comment_measure_numbers()
                        \baca-new-spacing-section #1 #24                                             %! SPACING_COMMAND:baca.HorizontalSpacingSpecifier.__call__(1)
                        \noBreak                                                                     %! BREAK:baca.BreakMeasureMap.__call__(2)
                        \baca-lbsd #15 #'(11)                                                        %! BREAK:baca.IndicatorCommand._call()
                        \break                                                                       %! BREAK:baca.IndicatorCommand._call()
                        s1 * 1/2                                                                     %! baca.SegmentMaker._make_global_skips(1)
            <BLANKLINE>
                        % [Global_Skips measure 4]                                                   %! baca.SegmentMaker._comment_measure_numbers():baca.SegmentMaker._style_phantom_measures(1):PHANTOM
                        \baca-new-spacing-section #1 #4                                              %! SPACING_COMMAND:baca.HorizontalSpacingSpecifier.__call__(1):baca.SegmentMaker._style_phantom_measures(1):PHANTOM
                        \noBreak                                                                     %! BREAK:baca.BreakMeasureMap.__call__(2):baca.SegmentMaker._style_phantom_measures(1):PHANTOM
                        \time 1/4                                                                    %! baca.SegmentMaker._make_global_skips(3):PHANTOM:baca.SegmentMaker._set_status_tag():EXPLICIT_TIME_SIGNATURE:baca.SegmentMaker._style_phantom_measures(1)
                        \baca-time-signature-transparent                                             %! baca.SegmentMaker._style_phantom_measures(2):PHANTOM
                        s1 * 1/4                                                                     %! baca.SegmentMaker._make_global_skips(3):PHANTOM
                        \once \override Score.BarLine.transparent = ##t                              %! baca.SegmentMaker._style_phantom_measures(3):PHANTOM
                        \once \override Score.SpanBar.transparent = ##t                              %! baca.SegmentMaker._style_phantom_measures(3):PHANTOM
            <BLANKLINE>
                    }                                                                                %! abjad.ScoreTemplate._make_global_context()
            <BLANKLINE>
                >>                                                                                   %! abjad.ScoreTemplate._make_global_context()
            <BLANKLINE>
                \context MusicContext = "Music_Context"                                              %! baca.SingleStaffScoreTemplate.__call__()
                <<                                                                                   %! baca.SingleStaffScoreTemplate.__call__()
            <BLANKLINE>
                    \context Staff = "Music_Staff"                                                   %! baca.SingleStaffScoreTemplate.__call__()
                    {                                                                                %! baca.SingleStaffScoreTemplate.__call__()
            <BLANKLINE>
                        \context Voice = "Music_Voice"                                               %! baca.SingleStaffScoreTemplate.__call__()
                        {                                                                            %! baca.SingleStaffScoreTemplate.__call__()
            <BLANKLINE>
                            % [Music_Voice measure 1]                                                %! baca.SegmentMaker._comment_measure_numbers()
                    %@% \baca-not-yet-pitched-coloring                                               %! baca.SegmentMaker._color_not_yet_pitched():NOT_YET_PITCHED_COLORING
                            b'2                                                                      %! baca.make_notes()
                        %%% ^ \baca-explicit-indicator-markup "(“Flute”)"                            %! EXPLICIT_INSTRUMENT_ALERT:baca.SegmentMaker._attach_latent_indicator_alert()
            <BLANKLINE>
                            % [Music_Voice measure 2]                                                %! baca.SegmentMaker._comment_measure_numbers()
                    %@% \baca-not-yet-pitched-coloring                                               %! baca.SegmentMaker._color_not_yet_pitched():NOT_YET_PITCHED_COLORING
                            b'2                                                                      %! baca.make_notes()
                        %%% ^ \baca-redundant-indicator-markup "(“Flute”)"                           %! REDUNDANT_INSTRUMENT_ALERT:baca.SegmentMaker._attach_latent_indicator_alert()
            <BLANKLINE>
                            % [Music_Voice measure 3]                                                %! baca.SegmentMaker._comment_measure_numbers()
                    %@% \baca-not-yet-pitched-coloring                                               %! baca.SegmentMaker._color_not_yet_pitched():NOT_YET_PITCHED_COLORING
                            b'2                                                                      %! baca.make_notes()
            <BLANKLINE>
                            <<                                                                       %! baca.SegmentMaker._make_multimeasure_rest_container(7):PHANTOM
            <BLANKLINE>
                                \context Voice = "Music_Voice"                                       %! baca.SegmentMaker._make_multimeasure_rest_container(4):PHANTOM
                                {                                                                    %! baca.SegmentMaker._make_multimeasure_rest_container(4):PHANTOM
            <BLANKLINE>
                                    % [Music_Voice measure 4]                                        %! baca.SegmentMaker._comment_measure_numbers():baca.SegmentMaker._style_phantom_measures(5):PHANTOM
                                    \abjad-invisible-music-coloring                                  %! baca.SegmentMaker._make_multimeasure_rest_container(2):PHANTOM:NOTE:INVISIBLE_MUSIC_COLORING:baca.SegmentMaker._style_phantom_measures(5)
                            %@% \abjad-invisible-music                                               %! baca.SegmentMaker._make_multimeasure_rest_container(3):PHANTOM:NOTE:INVISIBLE_MUSIC_COMMAND:baca.SegmentMaker._style_phantom_measures(5)
                            %@% \baca-not-yet-pitched-coloring                                       %! baca.SegmentMaker._color_not_yet_pitched():NOT_YET_PITCHED_COLORING:HIDDEN:NOTE:baca.SegmentMaker._style_phantom_measures(5):PHANTOM
                                    b'1 * 1/4                                                        %! baca.SegmentMaker._make_multimeasure_rest_container(1):PHANTOM:HIDDEN:NOTE
                            %@% ^ \baca-duration-multiplier-markup #"1" #"4"                         %! baca.SegmentMaker._label_duration_multipliers():DURATION_MULTIPLIER:HIDDEN:NOTE:PHANTOM:baca.SegmentMaker._style_phantom_measures(5)
            <BLANKLINE>
                                }                                                                    %! baca.SegmentMaker._make_multimeasure_rest_container(4):PHANTOM
            <BLANKLINE>
                                \context Voice = "Rest_Voice"                                        %! baca.SegmentMaker._make_multimeasure_rest_container(6):PHANTOM
                                {                                                                    %! baca.SegmentMaker._make_multimeasure_rest_container(6):PHANTOM
            <BLANKLINE>
                                    % [Rest_Voice measure 4]                                         %! baca.SegmentMaker._comment_measure_numbers():baca.SegmentMaker._style_phantom_measures(5):PHANTOM
                                    \once \override Score.TimeSignature.X-extent = ##f               %! baca.SegmentMaker._style_phantom_measures(6):PHANTOM
                                    \once \override MultiMeasureRest.transparent = ##t               %! baca.SegmentMaker._style_phantom_measures(7):PHANTOM
                                    \stopStaff                                                       %! baca.SegmentMaker._style_phantom_measures(8):PHANTOM
                                    \once \override Staff.StaffSymbol.transparent = ##t              %! baca.SegmentMaker._style_phantom_measures(8):PHANTOM
                                    \startStaff                                                      %! baca.SegmentMaker._style_phantom_measures(8):PHANTOM
                                    R1 * 1/4                                                         %! baca.SegmentMaker._make_multimeasure_rest_container(5):PHANTOM:REST_VOICE:MULTIMEASURE_REST
                            %@% ^ \baca-duration-multiplier-markup #"1" #"4"                         %! baca.SegmentMaker._label_duration_multipliers():DURATION_MULTIPLIER:MULTIMEASURE_REST:PHANTOM:REST_VOICE:baca.SegmentMaker._style_phantom_measures(5)
            <BLANKLINE>
                                }                                                                    %! baca.SegmentMaker._make_multimeasure_rest_container(6):PHANTOM
            <BLANKLINE>
                            >>                                                                       %! baca.SegmentMaker._make_multimeasure_rest_container(7):PHANTOM
            <BLANKLINE>
                        }                                                                            %! baca.SingleStaffScoreTemplate.__call__()
            <BLANKLINE>
                    }                                                                                %! baca.SingleStaffScoreTemplate.__call__()
            <BLANKLINE>
                >>                                                                                   %! baca.SingleStaffScoreTemplate.__call__()
            <BLANKLINE>
            >>                                                                                       %! baca.SingleStaffScoreTemplate.__call__()

        >>> tags_ = abjad.tags.instrument_color_tags()
        >>> match = lambda tags: bool(set(tags) & set(tags_))
        >>> text, count = abjad.activate(text, match)
        >>> lines = [_.strip('\n') for _ in text.split('\n')]
        >>> lilypond_file.score_block.items[:] = lines
        >>> abjad.show(lilypond_file, strict=89) # doctest: +SKIP

        ..  docs::

            >>> print(text)
            <BLANKLINE>
            \context Score = "Score"                                                                 %! baca.SingleStaffScoreTemplate.__call__()
            <<                                                                                       %! baca.SingleStaffScoreTemplate.__call__()
            <BLANKLINE>
                \context GlobalContext = "Global_Context"                                            %! abjad.ScoreTemplate._make_global_context()
                <<                                                                                   %! abjad.ScoreTemplate._make_global_context()
            <BLANKLINE>
                    \context GlobalSkips = "Global_Skips"                                            %! abjad.ScoreTemplate._make_global_context()
                    {                                                                                %! abjad.ScoreTemplate._make_global_context()
            <BLANKLINE>
                        % [Global_Skips measure 1]                                                   %! baca.SegmentMaker._comment_measure_numbers()
                        \baca-new-spacing-section #1 #24                                             %! SPACING_COMMAND:baca.HorizontalSpacingSpecifier.__call__(1)
                        \autoPageBreaksOff                                                           %! BREAK:baca.BreakMeasureMap.__call__(1)
                        \noBreak                                                                     %! BREAK:baca.BreakMeasureMap.__call__(2)
                        \baca-lbsd #0 #'(11)                                                         %! BREAK:baca.IndicatorCommand._call()
                        \time 4/8                                                                    %! baca.SegmentMaker._make_global_skips(2):baca.SegmentMaker._set_status_tag():EXPLICIT_TIME_SIGNATURE
                        \baca-time-signature-color #'blue                                            %! baca.SegmentMaker._attach_color_literal(2):EXPLICIT_TIME_SIGNATURE_COLOR
                        \pageBreak                                                                   %! BREAK:baca.IndicatorCommand._call()
                        s1 * 1/2                                                                     %! baca.SegmentMaker._make_global_skips(1)
            <BLANKLINE>
                        % [Global_Skips measure 2]                                                   %! baca.SegmentMaker._comment_measure_numbers()
                        \baca-new-spacing-section #1 #24                                             %! SPACING_COMMAND:baca.HorizontalSpacingSpecifier.__call__(1)
                        \noBreak                                                                     %! BREAK:baca.BreakMeasureMap.__call__(2)
                        s1 * 1/2                                                                     %! baca.SegmentMaker._make_global_skips(1)
            <BLANKLINE>
                        % [Global_Skips measure 3]                                                   %! baca.SegmentMaker._comment_measure_numbers()
                        \baca-new-spacing-section #1 #24                                             %! SPACING_COMMAND:baca.HorizontalSpacingSpecifier.__call__(1)
                        \noBreak                                                                     %! BREAK:baca.BreakMeasureMap.__call__(2)
                        \baca-lbsd #15 #'(11)                                                        %! BREAK:baca.IndicatorCommand._call()
                        \break                                                                       %! BREAK:baca.IndicatorCommand._call()
                        s1 * 1/2                                                                     %! baca.SegmentMaker._make_global_skips(1)
            <BLANKLINE>
                        % [Global_Skips measure 4]                                                   %! baca.SegmentMaker._comment_measure_numbers():baca.SegmentMaker._style_phantom_measures(1):PHANTOM
                        \baca-new-spacing-section #1 #4                                              %! SPACING_COMMAND:baca.HorizontalSpacingSpecifier.__call__(1):baca.SegmentMaker._style_phantom_measures(1):PHANTOM
                        \noBreak                                                                     %! BREAK:baca.BreakMeasureMap.__call__(2):baca.SegmentMaker._style_phantom_measures(1):PHANTOM
                        \time 1/4                                                                    %! baca.SegmentMaker._make_global_skips(3):PHANTOM:baca.SegmentMaker._set_status_tag():EXPLICIT_TIME_SIGNATURE:baca.SegmentMaker._style_phantom_measures(1)
                        \baca-time-signature-transparent                                             %! baca.SegmentMaker._style_phantom_measures(2):PHANTOM
                        s1 * 1/4                                                                     %! baca.SegmentMaker._make_global_skips(3):PHANTOM
                        \once \override Score.BarLine.transparent = ##t                              %! baca.SegmentMaker._style_phantom_measures(3):PHANTOM
                        \once \override Score.SpanBar.transparent = ##t                              %! baca.SegmentMaker._style_phantom_measures(3):PHANTOM
            <BLANKLINE>
                    }                                                                                %! abjad.ScoreTemplate._make_global_context()
            <BLANKLINE>
                >>                                                                                   %! abjad.ScoreTemplate._make_global_context()
            <BLANKLINE>
                \context MusicContext = "Music_Context"                                              %! baca.SingleStaffScoreTemplate.__call__()
                <<                                                                                   %! baca.SingleStaffScoreTemplate.__call__()
            <BLANKLINE>
                    \context Staff = "Music_Staff"                                                   %! baca.SingleStaffScoreTemplate.__call__()
                    {                                                                                %! baca.SingleStaffScoreTemplate.__call__()
            <BLANKLINE>
                        \context Voice = "Music_Voice"                                               %! baca.SingleStaffScoreTemplate.__call__()
                        {                                                                            %! baca.SingleStaffScoreTemplate.__call__()
            <BLANKLINE>
                            % [Music_Voice measure 1]                                                %! baca.SegmentMaker._comment_measure_numbers()
                    %@% \baca-not-yet-pitched-coloring                                               %! baca.SegmentMaker._color_not_yet_pitched():NOT_YET_PITCHED_COLORING
                            b'2                                                                      %! baca.make_notes()
                            ^ \baca-explicit-indicator-markup "(“Flute”)"                            %! EXPLICIT_INSTRUMENT_ALERT:baca.SegmentMaker._attach_latent_indicator_alert()
            <BLANKLINE>
                            % [Music_Voice measure 2]                                                %! baca.SegmentMaker._comment_measure_numbers()
                    %@% \baca-not-yet-pitched-coloring                                               %! baca.SegmentMaker._color_not_yet_pitched():NOT_YET_PITCHED_COLORING
                            b'2                                                                      %! baca.make_notes()
                            ^ \baca-redundant-indicator-markup "(“Flute”)"                           %! REDUNDANT_INSTRUMENT_ALERT:baca.SegmentMaker._attach_latent_indicator_alert()
            <BLANKLINE>
                            % [Music_Voice measure 3]                                                %! baca.SegmentMaker._comment_measure_numbers()
                    %@% \baca-not-yet-pitched-coloring                                               %! baca.SegmentMaker._color_not_yet_pitched():NOT_YET_PITCHED_COLORING
                            b'2                                                                      %! baca.make_notes()
            <BLANKLINE>
                            <<                                                                       %! baca.SegmentMaker._make_multimeasure_rest_container(7):PHANTOM
            <BLANKLINE>
                                \context Voice = "Music_Voice"                                       %! baca.SegmentMaker._make_multimeasure_rest_container(4):PHANTOM
                                {                                                                    %! baca.SegmentMaker._make_multimeasure_rest_container(4):PHANTOM
            <BLANKLINE>
                                    % [Music_Voice measure 4]                                        %! baca.SegmentMaker._comment_measure_numbers():baca.SegmentMaker._style_phantom_measures(5):PHANTOM
                                    \abjad-invisible-music-coloring                                  %! baca.SegmentMaker._make_multimeasure_rest_container(2):PHANTOM:NOTE:INVISIBLE_MUSIC_COLORING:baca.SegmentMaker._style_phantom_measures(5)
                            %@% \abjad-invisible-music                                               %! baca.SegmentMaker._make_multimeasure_rest_container(3):PHANTOM:NOTE:INVISIBLE_MUSIC_COMMAND:baca.SegmentMaker._style_phantom_measures(5)
                            %@% \baca-not-yet-pitched-coloring                                       %! baca.SegmentMaker._color_not_yet_pitched():NOT_YET_PITCHED_COLORING:HIDDEN:NOTE:baca.SegmentMaker._style_phantom_measures(5):PHANTOM
                                    b'1 * 1/4                                                        %! baca.SegmentMaker._make_multimeasure_rest_container(1):PHANTOM:HIDDEN:NOTE
                            %@% ^ \baca-duration-multiplier-markup #"1" #"4"                         %! baca.SegmentMaker._label_duration_multipliers():DURATION_MULTIPLIER:HIDDEN:NOTE:PHANTOM:baca.SegmentMaker._style_phantom_measures(5)
            <BLANKLINE>
                                }                                                                    %! baca.SegmentMaker._make_multimeasure_rest_container(4):PHANTOM
            <BLANKLINE>
                                \context Voice = "Rest_Voice"                                        %! baca.SegmentMaker._make_multimeasure_rest_container(6):PHANTOM
                                {                                                                    %! baca.SegmentMaker._make_multimeasure_rest_container(6):PHANTOM
            <BLANKLINE>
                                    % [Rest_Voice measure 4]                                         %! baca.SegmentMaker._comment_measure_numbers():baca.SegmentMaker._style_phantom_measures(5):PHANTOM
                                    \once \override Score.TimeSignature.X-extent = ##f               %! baca.SegmentMaker._style_phantom_measures(6):PHANTOM
                                    \once \override MultiMeasureRest.transparent = ##t               %! baca.SegmentMaker._style_phantom_measures(7):PHANTOM
                                    \stopStaff                                                       %! baca.SegmentMaker._style_phantom_measures(8):PHANTOM
                                    \once \override Staff.StaffSymbol.transparent = ##t              %! baca.SegmentMaker._style_phantom_measures(8):PHANTOM
                                    \startStaff                                                      %! baca.SegmentMaker._style_phantom_measures(8):PHANTOM
                                    R1 * 1/4                                                         %! baca.SegmentMaker._make_multimeasure_rest_container(5):PHANTOM:REST_VOICE:MULTIMEASURE_REST
                            %@% ^ \baca-duration-multiplier-markup #"1" #"4"                         %! baca.SegmentMaker._label_duration_multipliers():DURATION_MULTIPLIER:MULTIMEASURE_REST:PHANTOM:REST_VOICE:baca.SegmentMaker._style_phantom_measures(5)
            <BLANKLINE>
                                }                                                                    %! baca.SegmentMaker._make_multimeasure_rest_container(6):PHANTOM
            <BLANKLINE>
                            >>                                                                       %! baca.SegmentMaker._make_multimeasure_rest_container(7):PHANTOM
            <BLANKLINE>
                        }                                                                            %! baca.SingleStaffScoreTemplate.__call__()
            <BLANKLINE>
                    }                                                                                %! baca.SingleStaffScoreTemplate.__call__()
            <BLANKLINE>
                >>                                                                                   %! baca.SingleStaffScoreTemplate.__call__()
            <BLANKLINE>
            >>                                                                                       %! baca.SingleStaffScoreTemplate.__call__()

        Even at the beginning of a segment:

        >>> breaks = baca.breaks(
        ...     baca.page(
        ...         [1, 0, (11,)],
        ...         [2, 15, (11,)],
        ...         ),
        ...     )
        >>> maker = baca.SegmentMaker(
        ...     breaks=breaks,
        ...     deactivate=[abjad.tags.NOT_YET_PITCHED_COLORING],
        ...     instruments=instruments,
        ...     score_template=baca.SingleStaffScoreTemplate(),
        ...     spacing=baca.minimum_duration((1, 24)),
        ...     time_signatures=[(3, 8), (3, 8)],
        ...     )
        >>> maker(
        ...     'Music_Voice',
        ...     baca.instrument(instruments['Flute']),
        ...     baca.make_notes(),
        ...     )

        >>> metadata, persist = {}, {}
        >>> persist['persistent_indicators'] = {}
        >>> persist['persistent_indicators']['Music_Staff'] = [
        ...     abjad.Momento(
        ...         context='Music_Voice',
        ...         manifest='instruments',
        ...         value='Flute',
        ...         )
        ...     ]
        >>> metadata['segment_number'] = 1
        >>> lilypond_file = maker.run(
        ...     environment='docs',
        ...     previous_metadata=metadata,
        ...     previous_persist=persist,
        ...     )
        >>> block = abjad.Block(name='layout')
        >>> block.indent = 0
        >>> lilypond_file.items.insert(0, block)
        >>> abjad.show(lilypond_file, strict=89) # doctest: +SKIP

        ..  docs::

            >>> abjad.f(lilypond_file[abjad.Score], strict=89)
            <BLANKLINE>
            \context Score = "Score"                                                                 %! baca.SingleStaffScoreTemplate.__call__()
            <<                                                                                       %! baca.SingleStaffScoreTemplate.__call__()
            <BLANKLINE>
                \context GlobalContext = "Global_Context"                                            %! abjad.ScoreTemplate._make_global_context()
                <<                                                                                   %! abjad.ScoreTemplate._make_global_context()
            <BLANKLINE>
                    \context GlobalSkips = "Global_Skips"                                            %! abjad.ScoreTemplate._make_global_context()
                    {                                                                                %! abjad.ScoreTemplate._make_global_context()
            <BLANKLINE>
                        % [Global_Skips measure 1]                                                   %! baca.SegmentMaker._comment_measure_numbers()
                        \baca-new-spacing-section #1 #24                                             %! SPACING_COMMAND:baca.HorizontalSpacingSpecifier.__call__(1)
                        \autoPageBreaksOff                                                           %! BREAK:baca.BreakMeasureMap.__call__(1)
                        \noBreak                                                                     %! BREAK:baca.BreakMeasureMap.__call__(2)
                        \baca-lbsd #0 #'(11)                                                         %! BREAK:baca.IndicatorCommand._call()
                        \time 3/8                                                                    %! baca.SegmentMaker._make_global_skips(2):baca.SegmentMaker._set_status_tag():EXPLICIT_TIME_SIGNATURE
                        \bar ""                                                                      %! EMPTY_START_BAR:+SEGMENT:baca.SegmentMaker._make_global_skips(4)
                        \baca-time-signature-color #'blue                                            %! baca.SegmentMaker._attach_color_literal(2):EXPLICIT_TIME_SIGNATURE_COLOR
                        \pageBreak                                                                   %! BREAK:baca.IndicatorCommand._call()
                        s1 * 3/8                                                                     %! baca.SegmentMaker._make_global_skips(1)
            <BLANKLINE>
                        % [Global_Skips measure 2]                                                   %! baca.SegmentMaker._comment_measure_numbers()
                        \baca-new-spacing-section #1 #24                                             %! SPACING_COMMAND:baca.HorizontalSpacingSpecifier.__call__(1)
                        \noBreak                                                                     %! BREAK:baca.BreakMeasureMap.__call__(2)
                        \baca-lbsd #15 #'(11)                                                        %! BREAK:baca.IndicatorCommand._call()
                        \break                                                                       %! BREAK:baca.IndicatorCommand._call()
                        s1 * 3/8                                                                     %! baca.SegmentMaker._make_global_skips(1)
            <BLANKLINE>
                        % [Global_Skips measure 3]                                                   %! baca.SegmentMaker._comment_measure_numbers():baca.SegmentMaker._style_phantom_measures(1):PHANTOM
                        \baca-new-spacing-section #1 #4                                              %! SPACING_COMMAND:baca.HorizontalSpacingSpecifier.__call__(1):baca.SegmentMaker._style_phantom_measures(1):PHANTOM
                        \noBreak                                                                     %! BREAK:baca.BreakMeasureMap.__call__(2):baca.SegmentMaker._style_phantom_measures(1):PHANTOM
                        \time 1/4                                                                    %! baca.SegmentMaker._make_global_skips(3):PHANTOM:baca.SegmentMaker._set_status_tag():EXPLICIT_TIME_SIGNATURE:baca.SegmentMaker._style_phantom_measures(1)
                        \baca-time-signature-transparent                                             %! baca.SegmentMaker._style_phantom_measures(2):PHANTOM
                        s1 * 1/4                                                                     %! baca.SegmentMaker._make_global_skips(3):PHANTOM
                        \once \override Score.BarLine.transparent = ##t                              %! baca.SegmentMaker._style_phantom_measures(3):PHANTOM
                        \once \override Score.SpanBar.transparent = ##t                              %! baca.SegmentMaker._style_phantom_measures(3):PHANTOM
            <BLANKLINE>
                    }                                                                                %! abjad.ScoreTemplate._make_global_context()
            <BLANKLINE>
                >>                                                                                   %! abjad.ScoreTemplate._make_global_context()
            <BLANKLINE>
                \context MusicContext = "Music_Context"                                              %! baca.SingleStaffScoreTemplate.__call__()
                <<                                                                                   %! baca.SingleStaffScoreTemplate.__call__()
            <BLANKLINE>
                    \context Staff = "Music_Staff"                                                   %! baca.SingleStaffScoreTemplate.__call__()
                    {                                                                                %! baca.SingleStaffScoreTemplate.__call__()
            <BLANKLINE>
                        \context Voice = "Music_Voice"                                               %! baca.SingleStaffScoreTemplate.__call__()
                        {                                                                            %! baca.SingleStaffScoreTemplate.__call__()
            <BLANKLINE>
                            % [Music_Voice measure 1]                                                %! baca.SegmentMaker._comment_measure_numbers()
                        %@% \baca-not-yet-pitched-coloring                                           %! baca.SegmentMaker._color_not_yet_pitched():NOT_YET_PITCHED_COLORING
                            b'4.                                                                     %! baca.make_notes()
                            ^ \baca-redundant-indicator-markup "(“Flute”)"                           %! REDUNDANT_INSTRUMENT_ALERT:baca.SegmentMaker._attach_latent_indicator_alert()
            <BLANKLINE>
                            % [Music_Voice measure 2]                                                %! baca.SegmentMaker._comment_measure_numbers()
                        %@% \baca-not-yet-pitched-coloring                                           %! baca.SegmentMaker._color_not_yet_pitched():NOT_YET_PITCHED_COLORING
                            b'4.                                                                     %! baca.make_notes()
            <BLANKLINE>
                            <<                                                                       %! baca.SegmentMaker._make_multimeasure_rest_container(7):PHANTOM
            <BLANKLINE>
                                \context Voice = "Music_Voice"                                       %! baca.SegmentMaker._make_multimeasure_rest_container(4):PHANTOM
                                {                                                                    %! baca.SegmentMaker._make_multimeasure_rest_container(4):PHANTOM
            <BLANKLINE>
                                    % [Music_Voice measure 3]                                        %! baca.SegmentMaker._comment_measure_numbers():baca.SegmentMaker._style_phantom_measures(5):PHANTOM
                                    \abjad-invisible-music-coloring                                  %! baca.SegmentMaker._make_multimeasure_rest_container(2):PHANTOM:NOTE:INVISIBLE_MUSIC_COLORING:baca.SegmentMaker._style_phantom_measures(5)
                                %@% \abjad-invisible-music                                           %! baca.SegmentMaker._make_multimeasure_rest_container(3):PHANTOM:NOTE:INVISIBLE_MUSIC_COMMAND:baca.SegmentMaker._style_phantom_measures(5)
                                %@% \baca-not-yet-pitched-coloring                                   %! baca.SegmentMaker._color_not_yet_pitched():NOT_YET_PITCHED_COLORING:HIDDEN:NOTE:baca.SegmentMaker._style_phantom_measures(5):PHANTOM
                                    b'1 * 1/4                                                        %! baca.SegmentMaker._make_multimeasure_rest_container(1):PHANTOM:HIDDEN:NOTE
                                %@% ^ \baca-duration-multiplier-markup #"1" #"4"                     %! baca.SegmentMaker._label_duration_multipliers():DURATION_MULTIPLIER:HIDDEN:NOTE:PHANTOM:baca.SegmentMaker._style_phantom_measures(5)
            <BLANKLINE>
                                }                                                                    %! baca.SegmentMaker._make_multimeasure_rest_container(4):PHANTOM
            <BLANKLINE>
                                \context Voice = "Rest_Voice"                                        %! baca.SegmentMaker._make_multimeasure_rest_container(6):PHANTOM
                                {                                                                    %! baca.SegmentMaker._make_multimeasure_rest_container(6):PHANTOM
            <BLANKLINE>
                                    % [Rest_Voice measure 3]                                         %! baca.SegmentMaker._comment_measure_numbers():baca.SegmentMaker._style_phantom_measures(5):PHANTOM
                                    \once \override Score.TimeSignature.X-extent = ##f               %! baca.SegmentMaker._style_phantom_measures(6):PHANTOM
                                    \once \override MultiMeasureRest.transparent = ##t               %! baca.SegmentMaker._style_phantom_measures(7):PHANTOM
                                    \stopStaff                                                       %! baca.SegmentMaker._style_phantom_measures(8):PHANTOM
                                    \once \override Staff.StaffSymbol.transparent = ##t              %! baca.SegmentMaker._style_phantom_measures(8):PHANTOM
                                    \startStaff                                                      %! baca.SegmentMaker._style_phantom_measures(8):PHANTOM
                                    R1 * 1/4                                                         %! baca.SegmentMaker._make_multimeasure_rest_container(5):PHANTOM:REST_VOICE:MULTIMEASURE_REST
                                %@% ^ \baca-duration-multiplier-markup #"1" #"4"                     %! baca.SegmentMaker._label_duration_multipliers():DURATION_MULTIPLIER:MULTIMEASURE_REST:PHANTOM:REST_VOICE:baca.SegmentMaker._style_phantom_measures(5)
            <BLANKLINE>
                                }                                                                    %! baca.SegmentMaker._make_multimeasure_rest_container(6):PHANTOM
            <BLANKLINE>
                            >>                                                                       %! baca.SegmentMaker._make_multimeasure_rest_container(7):PHANTOM
            <BLANKLINE>
                        }                                                                            %! baca.SingleStaffScoreTemplate.__call__()
            <BLANKLINE>
                    }                                                                                %! baca.SingleStaffScoreTemplate.__call__()
            <BLANKLINE>
                >>                                                                                   %! baca.SingleStaffScoreTemplate.__call__()
            <BLANKLINE>
            >>                                                                                       %! baca.SingleStaffScoreTemplate.__call__()

        >>> score = lilypond_file[abjad.Score]
        >>> text = format(score, 'lilypond')
        >>> text = abjad.LilyPondFormatManager.left_shift_tags(text)
        >>> tags_ = abjad.tags.instrument_color_tags()
        >>> match = lambda tags: bool(set(tags) & set(tags_))
        >>> text, count = abjad.deactivate(text, match)
        >>> text = abjad.LilyPondFormatManager.left_shift_tags(text, 89)
        >>> lines = [_.strip('\n') for _ in text.split('\n')]
        >>> lilypond_file.score_block.items[:] = lines
        >>> abjad.show(lilypond_file, strict=89) # doctest: +SKIP

        ..  docs::

            >>> print(text)
            <BLANKLINE>
            \context Score = "Score"                                                                 %! baca.SingleStaffScoreTemplate.__call__()
            <<                                                                                       %! baca.SingleStaffScoreTemplate.__call__()
            <BLANKLINE>
                \context GlobalContext = "Global_Context"                                            %! abjad.ScoreTemplate._make_global_context()
                <<                                                                                   %! abjad.ScoreTemplate._make_global_context()
            <BLANKLINE>
                    \context GlobalSkips = "Global_Skips"                                            %! abjad.ScoreTemplate._make_global_context()
                    {                                                                                %! abjad.ScoreTemplate._make_global_context()
            <BLANKLINE>
                        % [Global_Skips measure 1]                                                   %! baca.SegmentMaker._comment_measure_numbers()
                        \baca-new-spacing-section #1 #24                                             %! SPACING_COMMAND:baca.HorizontalSpacingSpecifier.__call__(1)
                        \autoPageBreaksOff                                                           %! BREAK:baca.BreakMeasureMap.__call__(1)
                        \noBreak                                                                     %! BREAK:baca.BreakMeasureMap.__call__(2)
                        \baca-lbsd #0 #'(11)                                                         %! BREAK:baca.IndicatorCommand._call()
                        \time 3/8                                                                    %! baca.SegmentMaker._make_global_skips(2):baca.SegmentMaker._set_status_tag():EXPLICIT_TIME_SIGNATURE
                        \bar ""                                                                      %! EMPTY_START_BAR:+SEGMENT:baca.SegmentMaker._make_global_skips(4)
                        \baca-time-signature-color #'blue                                            %! baca.SegmentMaker._attach_color_literal(2):EXPLICIT_TIME_SIGNATURE_COLOR
                        \pageBreak                                                                   %! BREAK:baca.IndicatorCommand._call()
                        s1 * 3/8                                                                     %! baca.SegmentMaker._make_global_skips(1)
            <BLANKLINE>
                        % [Global_Skips measure 2]                                                   %! baca.SegmentMaker._comment_measure_numbers()
                        \baca-new-spacing-section #1 #24                                             %! SPACING_COMMAND:baca.HorizontalSpacingSpecifier.__call__(1)
                        \noBreak                                                                     %! BREAK:baca.BreakMeasureMap.__call__(2)
                        \baca-lbsd #15 #'(11)                                                        %! BREAK:baca.IndicatorCommand._call()
                        \break                                                                       %! BREAK:baca.IndicatorCommand._call()
                        s1 * 3/8                                                                     %! baca.SegmentMaker._make_global_skips(1)
            <BLANKLINE>
                        % [Global_Skips measure 3]                                                   %! baca.SegmentMaker._comment_measure_numbers():baca.SegmentMaker._style_phantom_measures(1):PHANTOM
                        \baca-new-spacing-section #1 #4                                              %! SPACING_COMMAND:baca.HorizontalSpacingSpecifier.__call__(1):baca.SegmentMaker._style_phantom_measures(1):PHANTOM
                        \noBreak                                                                     %! BREAK:baca.BreakMeasureMap.__call__(2):baca.SegmentMaker._style_phantom_measures(1):PHANTOM
                        \time 1/4                                                                    %! baca.SegmentMaker._make_global_skips(3):PHANTOM:baca.SegmentMaker._set_status_tag():EXPLICIT_TIME_SIGNATURE:baca.SegmentMaker._style_phantom_measures(1)
                        \baca-time-signature-transparent                                             %! baca.SegmentMaker._style_phantom_measures(2):PHANTOM
                        s1 * 1/4                                                                     %! baca.SegmentMaker._make_global_skips(3):PHANTOM
                        \once \override Score.BarLine.transparent = ##t                              %! baca.SegmentMaker._style_phantom_measures(3):PHANTOM
                        \once \override Score.SpanBar.transparent = ##t                              %! baca.SegmentMaker._style_phantom_measures(3):PHANTOM
            <BLANKLINE>
                    }                                                                                %! abjad.ScoreTemplate._make_global_context()
            <BLANKLINE>
                >>                                                                                   %! abjad.ScoreTemplate._make_global_context()
            <BLANKLINE>
                \context MusicContext = "Music_Context"                                              %! baca.SingleStaffScoreTemplate.__call__()
                <<                                                                                   %! baca.SingleStaffScoreTemplate.__call__()
            <BLANKLINE>
                    \context Staff = "Music_Staff"                                                   %! baca.SingleStaffScoreTemplate.__call__()
                    {                                                                                %! baca.SingleStaffScoreTemplate.__call__()
            <BLANKLINE>
                        \context Voice = "Music_Voice"                                               %! baca.SingleStaffScoreTemplate.__call__()
                        {                                                                            %! baca.SingleStaffScoreTemplate.__call__()
            <BLANKLINE>
                            % [Music_Voice measure 1]                                                %! baca.SegmentMaker._comment_measure_numbers()
                    %@% \baca-not-yet-pitched-coloring                                               %! baca.SegmentMaker._color_not_yet_pitched():NOT_YET_PITCHED_COLORING
                            b'4.                                                                     %! baca.make_notes()
                        %%% ^ \baca-redundant-indicator-markup "(“Flute”)"                           %! REDUNDANT_INSTRUMENT_ALERT:baca.SegmentMaker._attach_latent_indicator_alert()
            <BLANKLINE>
                            % [Music_Voice measure 2]                                                %! baca.SegmentMaker._comment_measure_numbers()
                    %@% \baca-not-yet-pitched-coloring                                               %! baca.SegmentMaker._color_not_yet_pitched():NOT_YET_PITCHED_COLORING
                            b'4.                                                                     %! baca.make_notes()
            <BLANKLINE>
                            <<                                                                       %! baca.SegmentMaker._make_multimeasure_rest_container(7):PHANTOM
            <BLANKLINE>
                                \context Voice = "Music_Voice"                                       %! baca.SegmentMaker._make_multimeasure_rest_container(4):PHANTOM
                                {                                                                    %! baca.SegmentMaker._make_multimeasure_rest_container(4):PHANTOM
            <BLANKLINE>
                                    % [Music_Voice measure 3]                                        %! baca.SegmentMaker._comment_measure_numbers():baca.SegmentMaker._style_phantom_measures(5):PHANTOM
                                    \abjad-invisible-music-coloring                                  %! baca.SegmentMaker._make_multimeasure_rest_container(2):PHANTOM:NOTE:INVISIBLE_MUSIC_COLORING:baca.SegmentMaker._style_phantom_measures(5)
                            %@% \abjad-invisible-music                                               %! baca.SegmentMaker._make_multimeasure_rest_container(3):PHANTOM:NOTE:INVISIBLE_MUSIC_COMMAND:baca.SegmentMaker._style_phantom_measures(5)
                            %@% \baca-not-yet-pitched-coloring                                       %! baca.SegmentMaker._color_not_yet_pitched():NOT_YET_PITCHED_COLORING:HIDDEN:NOTE:baca.SegmentMaker._style_phantom_measures(5):PHANTOM
                                    b'1 * 1/4                                                        %! baca.SegmentMaker._make_multimeasure_rest_container(1):PHANTOM:HIDDEN:NOTE
                            %@% ^ \baca-duration-multiplier-markup #"1" #"4"                         %! baca.SegmentMaker._label_duration_multipliers():DURATION_MULTIPLIER:HIDDEN:NOTE:PHANTOM:baca.SegmentMaker._style_phantom_measures(5)
            <BLANKLINE>
                                }                                                                    %! baca.SegmentMaker._make_multimeasure_rest_container(4):PHANTOM
            <BLANKLINE>
                                \context Voice = "Rest_Voice"                                        %! baca.SegmentMaker._make_multimeasure_rest_container(6):PHANTOM
                                {                                                                    %! baca.SegmentMaker._make_multimeasure_rest_container(6):PHANTOM
            <BLANKLINE>
                                    % [Rest_Voice measure 3]                                         %! baca.SegmentMaker._comment_measure_numbers():baca.SegmentMaker._style_phantom_measures(5):PHANTOM
                                    \once \override Score.TimeSignature.X-extent = ##f               %! baca.SegmentMaker._style_phantom_measures(6):PHANTOM
                                    \once \override MultiMeasureRest.transparent = ##t               %! baca.SegmentMaker._style_phantom_measures(7):PHANTOM
                                    \stopStaff                                                       %! baca.SegmentMaker._style_phantom_measures(8):PHANTOM
                                    \once \override Staff.StaffSymbol.transparent = ##t              %! baca.SegmentMaker._style_phantom_measures(8):PHANTOM
                                    \startStaff                                                      %! baca.SegmentMaker._style_phantom_measures(8):PHANTOM
                                    R1 * 1/4                                                         %! baca.SegmentMaker._make_multimeasure_rest_container(5):PHANTOM:REST_VOICE:MULTIMEASURE_REST
                            %@% ^ \baca-duration-multiplier-markup #"1" #"4"                         %! baca.SegmentMaker._label_duration_multipliers():DURATION_MULTIPLIER:MULTIMEASURE_REST:PHANTOM:REST_VOICE:baca.SegmentMaker._style_phantom_measures(5)
            <BLANKLINE>
                                }                                                                    %! baca.SegmentMaker._make_multimeasure_rest_container(6):PHANTOM
            <BLANKLINE>
                            >>                                                                       %! baca.SegmentMaker._make_multimeasure_rest_container(7):PHANTOM
            <BLANKLINE>
                        }                                                                            %! baca.SingleStaffScoreTemplate.__call__()
            <BLANKLINE>
                    }                                                                                %! baca.SingleStaffScoreTemplate.__call__()
            <BLANKLINE>
                >>                                                                                   %! baca.SingleStaffScoreTemplate.__call__()
            <BLANKLINE>
            >>                                                                                       %! baca.SingleStaffScoreTemplate.__call__()

        >>> tags_ = abjad.tags.instrument_color_tags()
        >>> match = lambda tags: bool(set(tags) & set(tags_))
        >>> text, count = abjad.activate(text, match)
        >>> lines = [_.strip('\n') for _ in text.split('\n')]
        >>> lilypond_file.score_block.items[:] = lines
        >>> abjad.show(lilypond_file, strict=89) # doctest: +SKIP

        ..  docs::

            >>> print(text)
            <BLANKLINE>
            \context Score = "Score"                                                                 %! baca.SingleStaffScoreTemplate.__call__()
            <<                                                                                       %! baca.SingleStaffScoreTemplate.__call__()
            <BLANKLINE>
                \context GlobalContext = "Global_Context"                                            %! abjad.ScoreTemplate._make_global_context()
                <<                                                                                   %! abjad.ScoreTemplate._make_global_context()
            <BLANKLINE>
                    \context GlobalSkips = "Global_Skips"                                            %! abjad.ScoreTemplate._make_global_context()
                    {                                                                                %! abjad.ScoreTemplate._make_global_context()
            <BLANKLINE>
                        % [Global_Skips measure 1]                                                   %! baca.SegmentMaker._comment_measure_numbers()
                        \baca-new-spacing-section #1 #24                                             %! SPACING_COMMAND:baca.HorizontalSpacingSpecifier.__call__(1)
                        \autoPageBreaksOff                                                           %! BREAK:baca.BreakMeasureMap.__call__(1)
                        \noBreak                                                                     %! BREAK:baca.BreakMeasureMap.__call__(2)
                        \baca-lbsd #0 #'(11)                                                         %! BREAK:baca.IndicatorCommand._call()
                        \time 3/8                                                                    %! baca.SegmentMaker._make_global_skips(2):baca.SegmentMaker._set_status_tag():EXPLICIT_TIME_SIGNATURE
                        \bar ""                                                                      %! EMPTY_START_BAR:+SEGMENT:baca.SegmentMaker._make_global_skips(4)
                        \baca-time-signature-color #'blue                                            %! baca.SegmentMaker._attach_color_literal(2):EXPLICIT_TIME_SIGNATURE_COLOR
                        \pageBreak                                                                   %! BREAK:baca.IndicatorCommand._call()
                        s1 * 3/8                                                                     %! baca.SegmentMaker._make_global_skips(1)
            <BLANKLINE>
                        % [Global_Skips measure 2]                                                   %! baca.SegmentMaker._comment_measure_numbers()
                        \baca-new-spacing-section #1 #24                                             %! SPACING_COMMAND:baca.HorizontalSpacingSpecifier.__call__(1)
                        \noBreak                                                                     %! BREAK:baca.BreakMeasureMap.__call__(2)
                        \baca-lbsd #15 #'(11)                                                        %! BREAK:baca.IndicatorCommand._call()
                        \break                                                                       %! BREAK:baca.IndicatorCommand._call()
                        s1 * 3/8                                                                     %! baca.SegmentMaker._make_global_skips(1)
            <BLANKLINE>
                        % [Global_Skips measure 3]                                                   %! baca.SegmentMaker._comment_measure_numbers():baca.SegmentMaker._style_phantom_measures(1):PHANTOM
                        \baca-new-spacing-section #1 #4                                              %! SPACING_COMMAND:baca.HorizontalSpacingSpecifier.__call__(1):baca.SegmentMaker._style_phantom_measures(1):PHANTOM
                        \noBreak                                                                     %! BREAK:baca.BreakMeasureMap.__call__(2):baca.SegmentMaker._style_phantom_measures(1):PHANTOM
                        \time 1/4                                                                    %! baca.SegmentMaker._make_global_skips(3):PHANTOM:baca.SegmentMaker._set_status_tag():EXPLICIT_TIME_SIGNATURE:baca.SegmentMaker._style_phantom_measures(1)
                        \baca-time-signature-transparent                                             %! baca.SegmentMaker._style_phantom_measures(2):PHANTOM
                        s1 * 1/4                                                                     %! baca.SegmentMaker._make_global_skips(3):PHANTOM
                        \once \override Score.BarLine.transparent = ##t                              %! baca.SegmentMaker._style_phantom_measures(3):PHANTOM
                        \once \override Score.SpanBar.transparent = ##t                              %! baca.SegmentMaker._style_phantom_measures(3):PHANTOM
            <BLANKLINE>
                    }                                                                                %! abjad.ScoreTemplate._make_global_context()
            <BLANKLINE>
                >>                                                                                   %! abjad.ScoreTemplate._make_global_context()
            <BLANKLINE>
                \context MusicContext = "Music_Context"                                              %! baca.SingleStaffScoreTemplate.__call__()
                <<                                                                                   %! baca.SingleStaffScoreTemplate.__call__()
            <BLANKLINE>
                    \context Staff = "Music_Staff"                                                   %! baca.SingleStaffScoreTemplate.__call__()
                    {                                                                                %! baca.SingleStaffScoreTemplate.__call__()
            <BLANKLINE>
                        \context Voice = "Music_Voice"                                               %! baca.SingleStaffScoreTemplate.__call__()
                        {                                                                            %! baca.SingleStaffScoreTemplate.__call__()
            <BLANKLINE>
                            % [Music_Voice measure 1]                                                %! baca.SegmentMaker._comment_measure_numbers()
                    %@% \baca-not-yet-pitched-coloring                                               %! baca.SegmentMaker._color_not_yet_pitched():NOT_YET_PITCHED_COLORING
                            b'4.                                                                     %! baca.make_notes()
                            ^ \baca-redundant-indicator-markup "(“Flute”)"                           %! REDUNDANT_INSTRUMENT_ALERT:baca.SegmentMaker._attach_latent_indicator_alert()
            <BLANKLINE>
                            % [Music_Voice measure 2]                                                %! baca.SegmentMaker._comment_measure_numbers()
                    %@% \baca-not-yet-pitched-coloring                                               %! baca.SegmentMaker._color_not_yet_pitched():NOT_YET_PITCHED_COLORING
                            b'4.                                                                     %! baca.make_notes()
            <BLANKLINE>
                            <<                                                                       %! baca.SegmentMaker._make_multimeasure_rest_container(7):PHANTOM
            <BLANKLINE>
                                \context Voice = "Music_Voice"                                       %! baca.SegmentMaker._make_multimeasure_rest_container(4):PHANTOM
                                {                                                                    %! baca.SegmentMaker._make_multimeasure_rest_container(4):PHANTOM
            <BLANKLINE>
                                    % [Music_Voice measure 3]                                        %! baca.SegmentMaker._comment_measure_numbers():baca.SegmentMaker._style_phantom_measures(5):PHANTOM
                                    \abjad-invisible-music-coloring                                  %! baca.SegmentMaker._make_multimeasure_rest_container(2):PHANTOM:NOTE:INVISIBLE_MUSIC_COLORING:baca.SegmentMaker._style_phantom_measures(5)
                            %@% \abjad-invisible-music                                               %! baca.SegmentMaker._make_multimeasure_rest_container(3):PHANTOM:NOTE:INVISIBLE_MUSIC_COMMAND:baca.SegmentMaker._style_phantom_measures(5)
                            %@% \baca-not-yet-pitched-coloring                                       %! baca.SegmentMaker._color_not_yet_pitched():NOT_YET_PITCHED_COLORING:HIDDEN:NOTE:baca.SegmentMaker._style_phantom_measures(5):PHANTOM
                                    b'1 * 1/4                                                        %! baca.SegmentMaker._make_multimeasure_rest_container(1):PHANTOM:HIDDEN:NOTE
                            %@% ^ \baca-duration-multiplier-markup #"1" #"4"                         %! baca.SegmentMaker._label_duration_multipliers():DURATION_MULTIPLIER:HIDDEN:NOTE:PHANTOM:baca.SegmentMaker._style_phantom_measures(5)
            <BLANKLINE>
                                }                                                                    %! baca.SegmentMaker._make_multimeasure_rest_container(4):PHANTOM
            <BLANKLINE>
                                \context Voice = "Rest_Voice"                                        %! baca.SegmentMaker._make_multimeasure_rest_container(6):PHANTOM
                                {                                                                    %! baca.SegmentMaker._make_multimeasure_rest_container(6):PHANTOM
            <BLANKLINE>
                                    % [Rest_Voice measure 3]                                         %! baca.SegmentMaker._comment_measure_numbers():baca.SegmentMaker._style_phantom_measures(5):PHANTOM
                                    \once \override Score.TimeSignature.X-extent = ##f               %! baca.SegmentMaker._style_phantom_measures(6):PHANTOM
                                    \once \override MultiMeasureRest.transparent = ##t               %! baca.SegmentMaker._style_phantom_measures(7):PHANTOM
                                    \stopStaff                                                       %! baca.SegmentMaker._style_phantom_measures(8):PHANTOM
                                    \once \override Staff.StaffSymbol.transparent = ##t              %! baca.SegmentMaker._style_phantom_measures(8):PHANTOM
                                    \startStaff                                                      %! baca.SegmentMaker._style_phantom_measures(8):PHANTOM
                                    R1 * 1/4                                                         %! baca.SegmentMaker._make_multimeasure_rest_container(5):PHANTOM:REST_VOICE:MULTIMEASURE_REST
                            %@% ^ \baca-duration-multiplier-markup #"1" #"4"                         %! baca.SegmentMaker._label_duration_multipliers():DURATION_MULTIPLIER:MULTIMEASURE_REST:PHANTOM:REST_VOICE:baca.SegmentMaker._style_phantom_measures(5)
            <BLANKLINE>
                                }                                                                    %! baca.SegmentMaker._make_multimeasure_rest_container(6):PHANTOM
            <BLANKLINE>
                            >>                                                                       %! baca.SegmentMaker._make_multimeasure_rest_container(7):PHANTOM
            <BLANKLINE>
                        }                                                                            %! baca.SingleStaffScoreTemplate.__call__()
            <BLANKLINE>
                    }                                                                                %! baca.SingleStaffScoreTemplate.__call__()
            <BLANKLINE>
                >>                                                                                   %! baca.SingleStaffScoreTemplate.__call__()
            <BLANKLINE>
            >>                                                                                       %! baca.SingleStaffScoreTemplate.__call__()

..  container:: example

    Margin markups.

    ..  container:: example

        Margin markup for examples:

        >>> margin_markups = abjad.OrderedDict()
        >>> margin_markups['I+II'] = abjad.MarginMarkup(
        ...     markup=abjad.Markup('I+II'),
        ...     )
        >>> margin_markups['III+IV'] = abjad.MarginMarkup(
        ...     markup=abjad.Markup('III+IV'),
        ...     )
        >>> breaks = baca.breaks(
        ...     baca.page(
        ...         [1, 0, (11,)],
        ...         [2, 15, (11,)],
        ...         ),
        ...     )

    ..  container:: example

        Default margin markup color purple and redraw dull purple:

        >>> score_template = baca.SingleStaffScoreTemplate()
        >>> triple = (
        ...     'Music_Staff',
        ...     'default_margin_markup',
        ...     margin_markups['I+II'],
        ...     )
        >>> score_template.defaults.append(triple)
        >>> maker = baca.SegmentMaker(
        ...     breaks=breaks,
        ...     deactivate=[abjad.tags.NOT_YET_PITCHED_COLORING],
        ...     margin_markups=margin_markups,
        ...     score_template=score_template,
        ...     spacing=baca.minimum_duration((1, 24)),
        ...     time_signatures=[(3, 8), (3, 8)],
        ...     )
        >>> maker(
        ...     'Music_Voice',
        ...     baca.make_notes(),
        ...     )

        >>> lilypond_file = maker.run(environment='docs')
        >>> block = abjad.Block(name='layout')
        >>> block.indent = 0
        >>> lilypond_file.items.insert(0, block)
        >>> abjad.show(lilypond_file, strict=89) # doctest: +SKIP

        ..  docs::

            >>> abjad.f(lilypond_file[abjad.Score], strict=89)
            <BLANKLINE>
            \context Score = "Score"                                                                 %! baca.SingleStaffScoreTemplate.__call__()
            <<                                                                                       %! baca.SingleStaffScoreTemplate.__call__()
            <BLANKLINE>
                \context GlobalContext = "Global_Context"                                            %! abjad.ScoreTemplate._make_global_context()
                <<                                                                                   %! abjad.ScoreTemplate._make_global_context()
            <BLANKLINE>
                    \context GlobalSkips = "Global_Skips"                                            %! abjad.ScoreTemplate._make_global_context()
                    {                                                                                %! abjad.ScoreTemplate._make_global_context()
            <BLANKLINE>
                        % [Global_Skips measure 1]                                                   %! baca.SegmentMaker._comment_measure_numbers()
                        \baca-new-spacing-section #1 #24                                             %! SPACING_COMMAND:baca.HorizontalSpacingSpecifier.__call__(1)
                        \autoPageBreaksOff                                                           %! BREAK:baca.BreakMeasureMap.__call__(1)
                        \noBreak                                                                     %! BREAK:baca.BreakMeasureMap.__call__(2)
                        \baca-lbsd #0 #'(11)                                                         %! BREAK:baca.IndicatorCommand._call()
                        \time 3/8                                                                    %! baca.SegmentMaker._make_global_skips(2):baca.SegmentMaker._set_status_tag():EXPLICIT_TIME_SIGNATURE
                        \baca-time-signature-color #'blue                                            %! baca.SegmentMaker._attach_color_literal(2):EXPLICIT_TIME_SIGNATURE_COLOR
                        \pageBreak                                                                   %! BREAK:baca.IndicatorCommand._call()
                        s1 * 3/8                                                                     %! baca.SegmentMaker._make_global_skips(1)
            <BLANKLINE>
                        % [Global_Skips measure 2]                                                   %! baca.SegmentMaker._comment_measure_numbers()
                        \baca-new-spacing-section #1 #24                                             %! SPACING_COMMAND:baca.HorizontalSpacingSpecifier.__call__(1)
                        \noBreak                                                                     %! BREAK:baca.BreakMeasureMap.__call__(2)
                        \baca-lbsd #15 #'(11)                                                        %! BREAK:baca.IndicatorCommand._call()
                        \break                                                                       %! BREAK:baca.IndicatorCommand._call()
                        s1 * 3/8                                                                     %! baca.SegmentMaker._make_global_skips(1)
            <BLANKLINE>
                        % [Global_Skips measure 3]                                                   %! baca.SegmentMaker._comment_measure_numbers():baca.SegmentMaker._style_phantom_measures(1):PHANTOM
                        \baca-new-spacing-section #1 #4                                              %! SPACING_COMMAND:baca.HorizontalSpacingSpecifier.__call__(1):baca.SegmentMaker._style_phantom_measures(1):PHANTOM
                        \noBreak                                                                     %! BREAK:baca.BreakMeasureMap.__call__(2):baca.SegmentMaker._style_phantom_measures(1):PHANTOM
                        \time 1/4                                                                    %! baca.SegmentMaker._make_global_skips(3):PHANTOM:baca.SegmentMaker._set_status_tag():EXPLICIT_TIME_SIGNATURE:baca.SegmentMaker._style_phantom_measures(1)
                        \baca-time-signature-transparent                                             %! baca.SegmentMaker._style_phantom_measures(2):PHANTOM
                        s1 * 1/4                                                                     %! baca.SegmentMaker._make_global_skips(3):PHANTOM
                        \once \override Score.BarLine.transparent = ##t                              %! baca.SegmentMaker._style_phantom_measures(3):PHANTOM
                        \once \override Score.SpanBar.transparent = ##t                              %! baca.SegmentMaker._style_phantom_measures(3):PHANTOM
            <BLANKLINE>
                    }                                                                                %! abjad.ScoreTemplate._make_global_context()
            <BLANKLINE>
                >>                                                                                   %! abjad.ScoreTemplate._make_global_context()
            <BLANKLINE>
                \context MusicContext = "Music_Context"                                              %! baca.SingleStaffScoreTemplate.__call__()
                <<                                                                                   %! baca.SingleStaffScoreTemplate.__call__()
            <BLANKLINE>
                    \context Staff = "Music_Staff"                                                   %! baca.SingleStaffScoreTemplate.__call__()
                    {                                                                                %! baca.SingleStaffScoreTemplate.__call__()
            <BLANKLINE>
                        \context Voice = "Music_Voice"                                               %! baca.SingleStaffScoreTemplate.__call__()
                        {                                                                            %! baca.SingleStaffScoreTemplate.__call__()
            <BLANKLINE>
                            % [Music_Voice measure 1]                                                %! baca.SegmentMaker._comment_measure_numbers()
                            \set Staff.shortInstrumentName =                                         %! -PARTS:abjad.ScoreTemplate.attach_defaults(2):baca.SegmentMaker._set_status_tag():DEFAULT_MARGIN_MARKUP
                            \markup { I+II }                                                         %! -PARTS:abjad.ScoreTemplate.attach_defaults(2):baca.SegmentMaker._set_status_tag():DEFAULT_MARGIN_MARKUP
                            \once \override Staff.InstrumentName.color = #(x11-color 'DarkViolet)    %! baca.SegmentMaker._attach_color_literal(2):DEFAULT_MARGIN_MARKUP_COLOR
                        %@% \baca-not-yet-pitched-coloring                                           %! baca.SegmentMaker._color_not_yet_pitched():NOT_YET_PITCHED_COLORING
                            b'4.                                                                     %! baca.make_notes()
                            ^ \baca-default-indicator-markup "[“I+II”]"                              %! DEFAULT_MARGIN_MARKUP_ALERT:baca.SegmentMaker._attach_latent_indicator_alert()
                            \override Staff.InstrumentName.color = #(x11-color 'violet)              %! baca.SegmentMaker._attach_color_literal(2):REDRAWN_DEFAULT_MARGIN_MARKUP_COLOR
                            \set Staff.shortInstrumentName =                                         %! -PARTS:abjad.ScoreTemplate.attach_defaults(2):baca.SegmentMaker._treat_persistent_wrapper(3):baca.SegmentMaker._set_status_tag():REDRAWN_DEFAULT_MARGIN_MARKUP
                            \markup { I+II }                                                         %! -PARTS:abjad.ScoreTemplate.attach_defaults(2):baca.SegmentMaker._treat_persistent_wrapper(3):baca.SegmentMaker._set_status_tag():REDRAWN_DEFAULT_MARGIN_MARKUP
            <BLANKLINE>
                            % [Music_Voice measure 2]                                                %! baca.SegmentMaker._comment_measure_numbers()
                        %@% \baca-not-yet-pitched-coloring                                           %! baca.SegmentMaker._color_not_yet_pitched():NOT_YET_PITCHED_COLORING
                            b'4.                                                                     %! baca.make_notes()
            <BLANKLINE>
                            <<                                                                       %! baca.SegmentMaker._make_multimeasure_rest_container(7):PHANTOM
            <BLANKLINE>
                                \context Voice = "Music_Voice"                                       %! baca.SegmentMaker._make_multimeasure_rest_container(4):PHANTOM
                                {                                                                    %! baca.SegmentMaker._make_multimeasure_rest_container(4):PHANTOM
            <BLANKLINE>
                                    % [Music_Voice measure 3]                                        %! baca.SegmentMaker._comment_measure_numbers():baca.SegmentMaker._style_phantom_measures(5):PHANTOM
                                    \abjad-invisible-music-coloring                                  %! baca.SegmentMaker._make_multimeasure_rest_container(2):PHANTOM:NOTE:INVISIBLE_MUSIC_COLORING:baca.SegmentMaker._style_phantom_measures(5)
                                %@% \abjad-invisible-music                                           %! baca.SegmentMaker._make_multimeasure_rest_container(3):PHANTOM:NOTE:INVISIBLE_MUSIC_COMMAND:baca.SegmentMaker._style_phantom_measures(5)
                                %@% \baca-not-yet-pitched-coloring                                   %! baca.SegmentMaker._color_not_yet_pitched():NOT_YET_PITCHED_COLORING:HIDDEN:NOTE:baca.SegmentMaker._style_phantom_measures(5):PHANTOM
                                    b'1 * 1/4                                                        %! baca.SegmentMaker._make_multimeasure_rest_container(1):PHANTOM:HIDDEN:NOTE
                                %@% ^ \baca-duration-multiplier-markup #"1" #"4"                     %! baca.SegmentMaker._label_duration_multipliers():DURATION_MULTIPLIER:HIDDEN:NOTE:PHANTOM:baca.SegmentMaker._style_phantom_measures(5)
            <BLANKLINE>
                                }                                                                    %! baca.SegmentMaker._make_multimeasure_rest_container(4):PHANTOM
            <BLANKLINE>
                                \context Voice = "Rest_Voice"                                        %! baca.SegmentMaker._make_multimeasure_rest_container(6):PHANTOM
                                {                                                                    %! baca.SegmentMaker._make_multimeasure_rest_container(6):PHANTOM
            <BLANKLINE>
                                    % [Rest_Voice measure 3]                                         %! baca.SegmentMaker._comment_measure_numbers():baca.SegmentMaker._style_phantom_measures(5):PHANTOM
                                    \once \override Score.TimeSignature.X-extent = ##f               %! baca.SegmentMaker._style_phantom_measures(6):PHANTOM
                                    \once \override MultiMeasureRest.transparent = ##t               %! baca.SegmentMaker._style_phantom_measures(7):PHANTOM
                                    \stopStaff                                                       %! baca.SegmentMaker._style_phantom_measures(8):PHANTOM
                                    \once \override Staff.StaffSymbol.transparent = ##t              %! baca.SegmentMaker._style_phantom_measures(8):PHANTOM
                                    \startStaff                                                      %! baca.SegmentMaker._style_phantom_measures(8):PHANTOM
                                    R1 * 1/4                                                         %! baca.SegmentMaker._make_multimeasure_rest_container(5):PHANTOM:REST_VOICE:MULTIMEASURE_REST
                                %@% ^ \baca-duration-multiplier-markup #"1" #"4"                     %! baca.SegmentMaker._label_duration_multipliers():DURATION_MULTIPLIER:MULTIMEASURE_REST:PHANTOM:REST_VOICE:baca.SegmentMaker._style_phantom_measures(5)
            <BLANKLINE>
                                }                                                                    %! baca.SegmentMaker._make_multimeasure_rest_container(6):PHANTOM
            <BLANKLINE>
                            >>                                                                       %! baca.SegmentMaker._make_multimeasure_rest_container(7):PHANTOM
            <BLANKLINE>
                        }                                                                            %! baca.SingleStaffScoreTemplate.__call__()
            <BLANKLINE>
                    }                                                                                %! baca.SingleStaffScoreTemplate.__call__()
            <BLANKLINE>
                >>                                                                                   %! baca.SingleStaffScoreTemplate.__call__()
            <BLANKLINE>
            >>                                                                                       %! baca.SingleStaffScoreTemplate.__call__()

        >>> score = lilypond_file[abjad.Score]
        >>> text = format(score, 'lilypond')
        >>> text = abjad.LilyPondFormatManager.left_shift_tags(text)
        >>> tags_ = abjad.tags.margin_markup_color_tags()
        >>> match = lambda tags: bool(set(tags) & set(tags_))
        >>> text, count = abjad.deactivate(text, match)
        >>> text = abjad.LilyPondFormatManager.left_shift_tags(text, 89)
        >>> lines = [_.strip('\n') for _ in text.split('\n')]
        >>> lilypond_file.score_block.items[:] = lines
        >>> abjad.show(lilypond_file, strict=89) # doctest: +SKIP

        ..  docs::

            >>> print(text)
            <BLANKLINE>
            \context Score = "Score"                                                                 %! baca.SingleStaffScoreTemplate.__call__()
            <<                                                                                       %! baca.SingleStaffScoreTemplate.__call__()
            <BLANKLINE>
                \context GlobalContext = "Global_Context"                                            %! abjad.ScoreTemplate._make_global_context()
                <<                                                                                   %! abjad.ScoreTemplate._make_global_context()
            <BLANKLINE>
                    \context GlobalSkips = "Global_Skips"                                            %! abjad.ScoreTemplate._make_global_context()
                    {                                                                                %! abjad.ScoreTemplate._make_global_context()
            <BLANKLINE>
                        % [Global_Skips measure 1]                                                   %! baca.SegmentMaker._comment_measure_numbers()
                        \baca-new-spacing-section #1 #24                                             %! SPACING_COMMAND:baca.HorizontalSpacingSpecifier.__call__(1)
                        \autoPageBreaksOff                                                           %! BREAK:baca.BreakMeasureMap.__call__(1)
                        \noBreak                                                                     %! BREAK:baca.BreakMeasureMap.__call__(2)
                        \baca-lbsd #0 #'(11)                                                         %! BREAK:baca.IndicatorCommand._call()
                        \time 3/8                                                                    %! baca.SegmentMaker._make_global_skips(2):baca.SegmentMaker._set_status_tag():EXPLICIT_TIME_SIGNATURE
                        \baca-time-signature-color #'blue                                            %! baca.SegmentMaker._attach_color_literal(2):EXPLICIT_TIME_SIGNATURE_COLOR
                        \pageBreak                                                                   %! BREAK:baca.IndicatorCommand._call()
                        s1 * 3/8                                                                     %! baca.SegmentMaker._make_global_skips(1)
            <BLANKLINE>
                        % [Global_Skips measure 2]                                                   %! baca.SegmentMaker._comment_measure_numbers()
                        \baca-new-spacing-section #1 #24                                             %! SPACING_COMMAND:baca.HorizontalSpacingSpecifier.__call__(1)
                        \noBreak                                                                     %! BREAK:baca.BreakMeasureMap.__call__(2)
                        \baca-lbsd #15 #'(11)                                                        %! BREAK:baca.IndicatorCommand._call()
                        \break                                                                       %! BREAK:baca.IndicatorCommand._call()
                        s1 * 3/8                                                                     %! baca.SegmentMaker._make_global_skips(1)
            <BLANKLINE>
                        % [Global_Skips measure 3]                                                   %! baca.SegmentMaker._comment_measure_numbers():baca.SegmentMaker._style_phantom_measures(1):PHANTOM
                        \baca-new-spacing-section #1 #4                                              %! SPACING_COMMAND:baca.HorizontalSpacingSpecifier.__call__(1):baca.SegmentMaker._style_phantom_measures(1):PHANTOM
                        \noBreak                                                                     %! BREAK:baca.BreakMeasureMap.__call__(2):baca.SegmentMaker._style_phantom_measures(1):PHANTOM
                        \time 1/4                                                                    %! baca.SegmentMaker._make_global_skips(3):PHANTOM:baca.SegmentMaker._set_status_tag():EXPLICIT_TIME_SIGNATURE:baca.SegmentMaker._style_phantom_measures(1)
                        \baca-time-signature-transparent                                             %! baca.SegmentMaker._style_phantom_measures(2):PHANTOM
                        s1 * 1/4                                                                     %! baca.SegmentMaker._make_global_skips(3):PHANTOM
                        \once \override Score.BarLine.transparent = ##t                              %! baca.SegmentMaker._style_phantom_measures(3):PHANTOM
                        \once \override Score.SpanBar.transparent = ##t                              %! baca.SegmentMaker._style_phantom_measures(3):PHANTOM
            <BLANKLINE>
                    }                                                                                %! abjad.ScoreTemplate._make_global_context()
            <BLANKLINE>
                >>                                                                                   %! abjad.ScoreTemplate._make_global_context()
            <BLANKLINE>
                \context MusicContext = "Music_Context"                                              %! baca.SingleStaffScoreTemplate.__call__()
                <<                                                                                   %! baca.SingleStaffScoreTemplate.__call__()
            <BLANKLINE>
                    \context Staff = "Music_Staff"                                                   %! baca.SingleStaffScoreTemplate.__call__()
                    {                                                                                %! baca.SingleStaffScoreTemplate.__call__()
            <BLANKLINE>
                        \context Voice = "Music_Voice"                                               %! baca.SingleStaffScoreTemplate.__call__()
                        {                                                                            %! baca.SingleStaffScoreTemplate.__call__()
            <BLANKLINE>
                            % [Music_Voice measure 1]                                                %! baca.SegmentMaker._comment_measure_numbers()
                            \set Staff.shortInstrumentName =                                         %! -PARTS:abjad.ScoreTemplate.attach_defaults(2):baca.SegmentMaker._set_status_tag():DEFAULT_MARGIN_MARKUP
                            \markup { I+II }                                                         %! -PARTS:abjad.ScoreTemplate.attach_defaults(2):baca.SegmentMaker._set_status_tag():DEFAULT_MARGIN_MARKUP
                        %%% \once \override Staff.InstrumentName.color = #(x11-color 'DarkViolet)    %! baca.SegmentMaker._attach_color_literal(2):DEFAULT_MARGIN_MARKUP_COLOR
                    %@% \baca-not-yet-pitched-coloring                                               %! baca.SegmentMaker._color_not_yet_pitched():NOT_YET_PITCHED_COLORING
                            b'4.                                                                     %! baca.make_notes()
                        %%% ^ \baca-default-indicator-markup "[“I+II”]"                              %! DEFAULT_MARGIN_MARKUP_ALERT:baca.SegmentMaker._attach_latent_indicator_alert()
                        %%% \override Staff.InstrumentName.color = #(x11-color 'violet)              %! baca.SegmentMaker._attach_color_literal(2):REDRAWN_DEFAULT_MARGIN_MARKUP_COLOR
                            \set Staff.shortInstrumentName =                                         %! -PARTS:abjad.ScoreTemplate.attach_defaults(2):baca.SegmentMaker._treat_persistent_wrapper(3):baca.SegmentMaker._set_status_tag():REDRAWN_DEFAULT_MARGIN_MARKUP
                            \markup { I+II }                                                         %! -PARTS:abjad.ScoreTemplate.attach_defaults(2):baca.SegmentMaker._treat_persistent_wrapper(3):baca.SegmentMaker._set_status_tag():REDRAWN_DEFAULT_MARGIN_MARKUP
            <BLANKLINE>
                            % [Music_Voice measure 2]                                                %! baca.SegmentMaker._comment_measure_numbers()
                    %@% \baca-not-yet-pitched-coloring                                               %! baca.SegmentMaker._color_not_yet_pitched():NOT_YET_PITCHED_COLORING
                            b'4.                                                                     %! baca.make_notes()
            <BLANKLINE>
                            <<                                                                       %! baca.SegmentMaker._make_multimeasure_rest_container(7):PHANTOM
            <BLANKLINE>
                                \context Voice = "Music_Voice"                                       %! baca.SegmentMaker._make_multimeasure_rest_container(4):PHANTOM
                                {                                                                    %! baca.SegmentMaker._make_multimeasure_rest_container(4):PHANTOM
            <BLANKLINE>
                                    % [Music_Voice measure 3]                                        %! baca.SegmentMaker._comment_measure_numbers():baca.SegmentMaker._style_phantom_measures(5):PHANTOM
                                    \abjad-invisible-music-coloring                                  %! baca.SegmentMaker._make_multimeasure_rest_container(2):PHANTOM:NOTE:INVISIBLE_MUSIC_COLORING:baca.SegmentMaker._style_phantom_measures(5)
                            %@% \abjad-invisible-music                                               %! baca.SegmentMaker._make_multimeasure_rest_container(3):PHANTOM:NOTE:INVISIBLE_MUSIC_COMMAND:baca.SegmentMaker._style_phantom_measures(5)
                            %@% \baca-not-yet-pitched-coloring                                       %! baca.SegmentMaker._color_not_yet_pitched():NOT_YET_PITCHED_COLORING:HIDDEN:NOTE:baca.SegmentMaker._style_phantom_measures(5):PHANTOM
                                    b'1 * 1/4                                                        %! baca.SegmentMaker._make_multimeasure_rest_container(1):PHANTOM:HIDDEN:NOTE
                            %@% ^ \baca-duration-multiplier-markup #"1" #"4"                         %! baca.SegmentMaker._label_duration_multipliers():DURATION_MULTIPLIER:HIDDEN:NOTE:PHANTOM:baca.SegmentMaker._style_phantom_measures(5)
            <BLANKLINE>
                                }                                                                    %! baca.SegmentMaker._make_multimeasure_rest_container(4):PHANTOM
            <BLANKLINE>
                                \context Voice = "Rest_Voice"                                        %! baca.SegmentMaker._make_multimeasure_rest_container(6):PHANTOM
                                {                                                                    %! baca.SegmentMaker._make_multimeasure_rest_container(6):PHANTOM
            <BLANKLINE>
                                    % [Rest_Voice measure 3]                                         %! baca.SegmentMaker._comment_measure_numbers():baca.SegmentMaker._style_phantom_measures(5):PHANTOM
                                    \once \override Score.TimeSignature.X-extent = ##f               %! baca.SegmentMaker._style_phantom_measures(6):PHANTOM
                                    \once \override MultiMeasureRest.transparent = ##t               %! baca.SegmentMaker._style_phantom_measures(7):PHANTOM
                                    \stopStaff                                                       %! baca.SegmentMaker._style_phantom_measures(8):PHANTOM
                                    \once \override Staff.StaffSymbol.transparent = ##t              %! baca.SegmentMaker._style_phantom_measures(8):PHANTOM
                                    \startStaff                                                      %! baca.SegmentMaker._style_phantom_measures(8):PHANTOM
                                    R1 * 1/4                                                         %! baca.SegmentMaker._make_multimeasure_rest_container(5):PHANTOM:REST_VOICE:MULTIMEASURE_REST
                            %@% ^ \baca-duration-multiplier-markup #"1" #"4"                         %! baca.SegmentMaker._label_duration_multipliers():DURATION_MULTIPLIER:MULTIMEASURE_REST:PHANTOM:REST_VOICE:baca.SegmentMaker._style_phantom_measures(5)
            <BLANKLINE>
                                }                                                                    %! baca.SegmentMaker._make_multimeasure_rest_container(6):PHANTOM
            <BLANKLINE>
                            >>                                                                       %! baca.SegmentMaker._make_multimeasure_rest_container(7):PHANTOM
            <BLANKLINE>
                        }                                                                            %! baca.SingleStaffScoreTemplate.__call__()
            <BLANKLINE>
                    }                                                                                %! baca.SingleStaffScoreTemplate.__call__()
            <BLANKLINE>
                >>                                                                                   %! baca.SingleStaffScoreTemplate.__call__()
            <BLANKLINE>
            >>                                                                                       %! baca.SingleStaffScoreTemplate.__call__()

        >>> tags_ = abjad.tags.margin_markup_color_tags()
        >>> match = lambda tags: bool(set(tags) & set(tags_))
        >>> text, count = abjad.activate(text, match)
        >>> lines = [_.strip('\n') for _ in text.split('\n')]
        >>> lilypond_file.score_block.items[:] = lines
        >>> abjad.show(lilypond_file, strict=89) # doctest: +SKIP

        ..  docs::

            >>> print(text)
            <BLANKLINE>
            \context Score = "Score"                                                                 %! baca.SingleStaffScoreTemplate.__call__()
            <<                                                                                       %! baca.SingleStaffScoreTemplate.__call__()
            <BLANKLINE>
                \context GlobalContext = "Global_Context"                                            %! abjad.ScoreTemplate._make_global_context()
                <<                                                                                   %! abjad.ScoreTemplate._make_global_context()
            <BLANKLINE>
                    \context GlobalSkips = "Global_Skips"                                            %! abjad.ScoreTemplate._make_global_context()
                    {                                                                                %! abjad.ScoreTemplate._make_global_context()
            <BLANKLINE>
                        % [Global_Skips measure 1]                                                   %! baca.SegmentMaker._comment_measure_numbers()
                        \baca-new-spacing-section #1 #24                                             %! SPACING_COMMAND:baca.HorizontalSpacingSpecifier.__call__(1)
                        \autoPageBreaksOff                                                           %! BREAK:baca.BreakMeasureMap.__call__(1)
                        \noBreak                                                                     %! BREAK:baca.BreakMeasureMap.__call__(2)
                        \baca-lbsd #0 #'(11)                                                         %! BREAK:baca.IndicatorCommand._call()
                        \time 3/8                                                                    %! baca.SegmentMaker._make_global_skips(2):baca.SegmentMaker._set_status_tag():EXPLICIT_TIME_SIGNATURE
                        \baca-time-signature-color #'blue                                            %! baca.SegmentMaker._attach_color_literal(2):EXPLICIT_TIME_SIGNATURE_COLOR
                        \pageBreak                                                                   %! BREAK:baca.IndicatorCommand._call()
                        s1 * 3/8                                                                     %! baca.SegmentMaker._make_global_skips(1)
            <BLANKLINE>
                        % [Global_Skips measure 2]                                                   %! baca.SegmentMaker._comment_measure_numbers()
                        \baca-new-spacing-section #1 #24                                             %! SPACING_COMMAND:baca.HorizontalSpacingSpecifier.__call__(1)
                        \noBreak                                                                     %! BREAK:baca.BreakMeasureMap.__call__(2)
                        \baca-lbsd #15 #'(11)                                                        %! BREAK:baca.IndicatorCommand._call()
                        \break                                                                       %! BREAK:baca.IndicatorCommand._call()
                        s1 * 3/8                                                                     %! baca.SegmentMaker._make_global_skips(1)
            <BLANKLINE>
                        % [Global_Skips measure 3]                                                   %! baca.SegmentMaker._comment_measure_numbers():baca.SegmentMaker._style_phantom_measures(1):PHANTOM
                        \baca-new-spacing-section #1 #4                                              %! SPACING_COMMAND:baca.HorizontalSpacingSpecifier.__call__(1):baca.SegmentMaker._style_phantom_measures(1):PHANTOM
                        \noBreak                                                                     %! BREAK:baca.BreakMeasureMap.__call__(2):baca.SegmentMaker._style_phantom_measures(1):PHANTOM
                        \time 1/4                                                                    %! baca.SegmentMaker._make_global_skips(3):PHANTOM:baca.SegmentMaker._set_status_tag():EXPLICIT_TIME_SIGNATURE:baca.SegmentMaker._style_phantom_measures(1)
                        \baca-time-signature-transparent                                             %! baca.SegmentMaker._style_phantom_measures(2):PHANTOM
                        s1 * 1/4                                                                     %! baca.SegmentMaker._make_global_skips(3):PHANTOM
                        \once \override Score.BarLine.transparent = ##t                              %! baca.SegmentMaker._style_phantom_measures(3):PHANTOM
                        \once \override Score.SpanBar.transparent = ##t                              %! baca.SegmentMaker._style_phantom_measures(3):PHANTOM
            <BLANKLINE>
                    }                                                                                %! abjad.ScoreTemplate._make_global_context()
            <BLANKLINE>
                >>                                                                                   %! abjad.ScoreTemplate._make_global_context()
            <BLANKLINE>
                \context MusicContext = "Music_Context"                                              %! baca.SingleStaffScoreTemplate.__call__()
                <<                                                                                   %! baca.SingleStaffScoreTemplate.__call__()
            <BLANKLINE>
                    \context Staff = "Music_Staff"                                                   %! baca.SingleStaffScoreTemplate.__call__()
                    {                                                                                %! baca.SingleStaffScoreTemplate.__call__()
            <BLANKLINE>
                        \context Voice = "Music_Voice"                                               %! baca.SingleStaffScoreTemplate.__call__()
                        {                                                                            %! baca.SingleStaffScoreTemplate.__call__()
            <BLANKLINE>
                            % [Music_Voice measure 1]                                                %! baca.SegmentMaker._comment_measure_numbers()
                            \set Staff.shortInstrumentName =                                         %! -PARTS:abjad.ScoreTemplate.attach_defaults(2):baca.SegmentMaker._set_status_tag():DEFAULT_MARGIN_MARKUP
                            \markup { I+II }                                                         %! -PARTS:abjad.ScoreTemplate.attach_defaults(2):baca.SegmentMaker._set_status_tag():DEFAULT_MARGIN_MARKUP
                            \once \override Staff.InstrumentName.color = #(x11-color 'DarkViolet)    %! baca.SegmentMaker._attach_color_literal(2):DEFAULT_MARGIN_MARKUP_COLOR
                    %@% \baca-not-yet-pitched-coloring                                               %! baca.SegmentMaker._color_not_yet_pitched():NOT_YET_PITCHED_COLORING
                            b'4.                                                                     %! baca.make_notes()
                            ^ \baca-default-indicator-markup "[“I+II”]"                              %! DEFAULT_MARGIN_MARKUP_ALERT:baca.SegmentMaker._attach_latent_indicator_alert()
                            \override Staff.InstrumentName.color = #(x11-color 'violet)              %! baca.SegmentMaker._attach_color_literal(2):REDRAWN_DEFAULT_MARGIN_MARKUP_COLOR
                            \set Staff.shortInstrumentName =                                         %! -PARTS:abjad.ScoreTemplate.attach_defaults(2):baca.SegmentMaker._treat_persistent_wrapper(3):baca.SegmentMaker._set_status_tag():REDRAWN_DEFAULT_MARGIN_MARKUP
                            \markup { I+II }                                                         %! -PARTS:abjad.ScoreTemplate.attach_defaults(2):baca.SegmentMaker._treat_persistent_wrapper(3):baca.SegmentMaker._set_status_tag():REDRAWN_DEFAULT_MARGIN_MARKUP
            <BLANKLINE>
                            % [Music_Voice measure 2]                                                %! baca.SegmentMaker._comment_measure_numbers()
                    %@% \baca-not-yet-pitched-coloring                                               %! baca.SegmentMaker._color_not_yet_pitched():NOT_YET_PITCHED_COLORING
                            b'4.                                                                     %! baca.make_notes()
            <BLANKLINE>
                            <<                                                                       %! baca.SegmentMaker._make_multimeasure_rest_container(7):PHANTOM
            <BLANKLINE>
                                \context Voice = "Music_Voice"                                       %! baca.SegmentMaker._make_multimeasure_rest_container(4):PHANTOM
                                {                                                                    %! baca.SegmentMaker._make_multimeasure_rest_container(4):PHANTOM
            <BLANKLINE>
                                    % [Music_Voice measure 3]                                        %! baca.SegmentMaker._comment_measure_numbers():baca.SegmentMaker._style_phantom_measures(5):PHANTOM
                                    \abjad-invisible-music-coloring                                  %! baca.SegmentMaker._make_multimeasure_rest_container(2):PHANTOM:NOTE:INVISIBLE_MUSIC_COLORING:baca.SegmentMaker._style_phantom_measures(5)
                            %@% \abjad-invisible-music                                               %! baca.SegmentMaker._make_multimeasure_rest_container(3):PHANTOM:NOTE:INVISIBLE_MUSIC_COMMAND:baca.SegmentMaker._style_phantom_measures(5)
                            %@% \baca-not-yet-pitched-coloring                                       %! baca.SegmentMaker._color_not_yet_pitched():NOT_YET_PITCHED_COLORING:HIDDEN:NOTE:baca.SegmentMaker._style_phantom_measures(5):PHANTOM
                                    b'1 * 1/4                                                        %! baca.SegmentMaker._make_multimeasure_rest_container(1):PHANTOM:HIDDEN:NOTE
                            %@% ^ \baca-duration-multiplier-markup #"1" #"4"                         %! baca.SegmentMaker._label_duration_multipliers():DURATION_MULTIPLIER:HIDDEN:NOTE:PHANTOM:baca.SegmentMaker._style_phantom_measures(5)
            <BLANKLINE>
                                }                                                                    %! baca.SegmentMaker._make_multimeasure_rest_container(4):PHANTOM
            <BLANKLINE>
                                \context Voice = "Rest_Voice"                                        %! baca.SegmentMaker._make_multimeasure_rest_container(6):PHANTOM
                                {                                                                    %! baca.SegmentMaker._make_multimeasure_rest_container(6):PHANTOM
            <BLANKLINE>
                                    % [Rest_Voice measure 3]                                         %! baca.SegmentMaker._comment_measure_numbers():baca.SegmentMaker._style_phantom_measures(5):PHANTOM
                                    \once \override Score.TimeSignature.X-extent = ##f               %! baca.SegmentMaker._style_phantom_measures(6):PHANTOM
                                    \once \override MultiMeasureRest.transparent = ##t               %! baca.SegmentMaker._style_phantom_measures(7):PHANTOM
                                    \stopStaff                                                       %! baca.SegmentMaker._style_phantom_measures(8):PHANTOM
                                    \once \override Staff.StaffSymbol.transparent = ##t              %! baca.SegmentMaker._style_phantom_measures(8):PHANTOM
                                    \startStaff                                                      %! baca.SegmentMaker._style_phantom_measures(8):PHANTOM
                                    R1 * 1/4                                                         %! baca.SegmentMaker._make_multimeasure_rest_container(5):PHANTOM:REST_VOICE:MULTIMEASURE_REST
                            %@% ^ \baca-duration-multiplier-markup #"1" #"4"                         %! baca.SegmentMaker._label_duration_multipliers():DURATION_MULTIPLIER:MULTIMEASURE_REST:PHANTOM:REST_VOICE:baca.SegmentMaker._style_phantom_measures(5)
            <BLANKLINE>
                                }                                                                    %! baca.SegmentMaker._make_multimeasure_rest_container(6):PHANTOM
            <BLANKLINE>
                            >>                                                                       %! baca.SegmentMaker._make_multimeasure_rest_container(7):PHANTOM
            <BLANKLINE>
                        }                                                                            %! baca.SingleStaffScoreTemplate.__call__()
            <BLANKLINE>
                    }                                                                                %! baca.SingleStaffScoreTemplate.__call__()
            <BLANKLINE>
                >>                                                                                   %! baca.SingleStaffScoreTemplate.__call__()
            <BLANKLINE>
            >>                                                                                       %! baca.SingleStaffScoreTemplate.__call__()

    ..  container:: example

        Explicit margin markup color blue and redraw dull blue:

        >>> maker = baca.SegmentMaker(
        ...     breaks=breaks,
        ...     deactivate=[abjad.tags.NOT_YET_PITCHED_COLORING],
        ...     margin_markups=margin_markups,
        ...     score_template=baca.SingleStaffScoreTemplate(),
        ...     spacing=baca.minimum_duration((1, 24)),
        ...     time_signatures=[(3, 8), (3, 8)],
        ...     )
        >>> maker(
        ...     'Music_Voice',
        ...     baca.margin_markup(margin_markups['I+II']),
        ...     baca.make_notes(),
        ...     )

        >>> lilypond_file = maker.run(environment='docs')
        >>> block = abjad.Block(name='layout')
        >>> block.indent = 0
        >>> lilypond_file.items.insert(0, block)
        >>> abjad.show(lilypond_file, strict=89) # doctest: +SKIP

        ..  docs::

            >>> abjad.f(lilypond_file[abjad.Score], strict=89)
            <BLANKLINE>
            \context Score = "Score"                                                                 %! baca.SingleStaffScoreTemplate.__call__()
            <<                                                                                       %! baca.SingleStaffScoreTemplate.__call__()
            <BLANKLINE>
                \context GlobalContext = "Global_Context"                                            %! abjad.ScoreTemplate._make_global_context()
                <<                                                                                   %! abjad.ScoreTemplate._make_global_context()
            <BLANKLINE>
                    \context GlobalSkips = "Global_Skips"                                            %! abjad.ScoreTemplate._make_global_context()
                    {                                                                                %! abjad.ScoreTemplate._make_global_context()
            <BLANKLINE>
                        % [Global_Skips measure 1]                                                   %! baca.SegmentMaker._comment_measure_numbers()
                        \baca-new-spacing-section #1 #24                                             %! SPACING_COMMAND:baca.HorizontalSpacingSpecifier.__call__(1)
                        \autoPageBreaksOff                                                           %! BREAK:baca.BreakMeasureMap.__call__(1)
                        \noBreak                                                                     %! BREAK:baca.BreakMeasureMap.__call__(2)
                        \baca-lbsd #0 #'(11)                                                         %! BREAK:baca.IndicatorCommand._call()
                        \time 3/8                                                                    %! baca.SegmentMaker._make_global_skips(2):baca.SegmentMaker._set_status_tag():EXPLICIT_TIME_SIGNATURE
                        \baca-time-signature-color #'blue                                            %! baca.SegmentMaker._attach_color_literal(2):EXPLICIT_TIME_SIGNATURE_COLOR
                        \pageBreak                                                                   %! BREAK:baca.IndicatorCommand._call()
                        s1 * 3/8                                                                     %! baca.SegmentMaker._make_global_skips(1)
            <BLANKLINE>
                        % [Global_Skips measure 2]                                                   %! baca.SegmentMaker._comment_measure_numbers()
                        \baca-new-spacing-section #1 #24                                             %! SPACING_COMMAND:baca.HorizontalSpacingSpecifier.__call__(1)
                        \noBreak                                                                     %! BREAK:baca.BreakMeasureMap.__call__(2)
                        \baca-lbsd #15 #'(11)                                                        %! BREAK:baca.IndicatorCommand._call()
                        \break                                                                       %! BREAK:baca.IndicatorCommand._call()
                        s1 * 3/8                                                                     %! baca.SegmentMaker._make_global_skips(1)
            <BLANKLINE>
                        % [Global_Skips measure 3]                                                   %! baca.SegmentMaker._comment_measure_numbers():baca.SegmentMaker._style_phantom_measures(1):PHANTOM
                        \baca-new-spacing-section #1 #4                                              %! SPACING_COMMAND:baca.HorizontalSpacingSpecifier.__call__(1):baca.SegmentMaker._style_phantom_measures(1):PHANTOM
                        \noBreak                                                                     %! BREAK:baca.BreakMeasureMap.__call__(2):baca.SegmentMaker._style_phantom_measures(1):PHANTOM
                        \time 1/4                                                                    %! baca.SegmentMaker._make_global_skips(3):PHANTOM:baca.SegmentMaker._set_status_tag():EXPLICIT_TIME_SIGNATURE:baca.SegmentMaker._style_phantom_measures(1)
                        \baca-time-signature-transparent                                             %! baca.SegmentMaker._style_phantom_measures(2):PHANTOM
                        s1 * 1/4                                                                     %! baca.SegmentMaker._make_global_skips(3):PHANTOM
                        \once \override Score.BarLine.transparent = ##t                              %! baca.SegmentMaker._style_phantom_measures(3):PHANTOM
                        \once \override Score.SpanBar.transparent = ##t                              %! baca.SegmentMaker._style_phantom_measures(3):PHANTOM
            <BLANKLINE>
                    }                                                                                %! abjad.ScoreTemplate._make_global_context()
            <BLANKLINE>
                >>                                                                                   %! abjad.ScoreTemplate._make_global_context()
            <BLANKLINE>
                \context MusicContext = "Music_Context"                                              %! baca.SingleStaffScoreTemplate.__call__()
                <<                                                                                   %! baca.SingleStaffScoreTemplate.__call__()
            <BLANKLINE>
                    \context Staff = "Music_Staff"                                                   %! baca.SingleStaffScoreTemplate.__call__()
                    {                                                                                %! baca.SingleStaffScoreTemplate.__call__()
            <BLANKLINE>
                        \context Voice = "Music_Voice"                                               %! baca.SingleStaffScoreTemplate.__call__()
                        {                                                                            %! baca.SingleStaffScoreTemplate.__call__()
            <BLANKLINE>
                            % [Music_Voice measure 1]                                                %! baca.SegmentMaker._comment_measure_numbers()
                            \set Staff.shortInstrumentName =                                         %! baca.margin_markup():baca.IndicatorCommand._call():baca.SegmentMaker._set_status_tag():EXPLICIT_MARGIN_MARKUP
                            \markup { I+II }                                                         %! baca.margin_markup():baca.IndicatorCommand._call():baca.SegmentMaker._set_status_tag():EXPLICIT_MARGIN_MARKUP
                            \once \override Staff.InstrumentName.color = #(x11-color 'blue)          %! baca.SegmentMaker._attach_color_literal(2):EXPLICIT_MARGIN_MARKUP_COLOR
                        %@% \baca-not-yet-pitched-coloring                                           %! baca.SegmentMaker._color_not_yet_pitched():NOT_YET_PITCHED_COLORING
                            b'4.                                                                     %! baca.make_notes()
                            ^ \baca-explicit-indicator-markup "[“I+II”]"                             %! EXPLICIT_MARGIN_MARKUP_ALERT:baca.SegmentMaker._attach_latent_indicator_alert()
                            \override Staff.InstrumentName.color = #(x11-color 'DeepSkyBlue2)        %! baca.SegmentMaker._attach_color_literal(2):REDRAWN_EXPLICIT_MARGIN_MARKUP_COLOR
                            \set Staff.shortInstrumentName =                                         %! baca.margin_markup():baca.IndicatorCommand._call():baca.SegmentMaker._treat_persistent_wrapper(3):baca.SegmentMaker._set_status_tag():REDRAWN_EXPLICIT_MARGIN_MARKUP
                            \markup { I+II }                                                         %! baca.margin_markup():baca.IndicatorCommand._call():baca.SegmentMaker._treat_persistent_wrapper(3):baca.SegmentMaker._set_status_tag():REDRAWN_EXPLICIT_MARGIN_MARKUP
            <BLANKLINE>
                            % [Music_Voice measure 2]                                                %! baca.SegmentMaker._comment_measure_numbers()
                        %@% \baca-not-yet-pitched-coloring                                           %! baca.SegmentMaker._color_not_yet_pitched():NOT_YET_PITCHED_COLORING
                            b'4.                                                                     %! baca.make_notes()
            <BLANKLINE>
                            <<                                                                       %! baca.SegmentMaker._make_multimeasure_rest_container(7):PHANTOM
            <BLANKLINE>
                                \context Voice = "Music_Voice"                                       %! baca.SegmentMaker._make_multimeasure_rest_container(4):PHANTOM
                                {                                                                    %! baca.SegmentMaker._make_multimeasure_rest_container(4):PHANTOM
            <BLANKLINE>
                                    % [Music_Voice measure 3]                                        %! baca.SegmentMaker._comment_measure_numbers():baca.SegmentMaker._style_phantom_measures(5):PHANTOM
                                    \abjad-invisible-music-coloring                                  %! baca.SegmentMaker._make_multimeasure_rest_container(2):PHANTOM:NOTE:INVISIBLE_MUSIC_COLORING:baca.SegmentMaker._style_phantom_measures(5)
                                %@% \abjad-invisible-music                                           %! baca.SegmentMaker._make_multimeasure_rest_container(3):PHANTOM:NOTE:INVISIBLE_MUSIC_COMMAND:baca.SegmentMaker._style_phantom_measures(5)
                                %@% \baca-not-yet-pitched-coloring                                   %! baca.SegmentMaker._color_not_yet_pitched():NOT_YET_PITCHED_COLORING:HIDDEN:NOTE:baca.SegmentMaker._style_phantom_measures(5):PHANTOM
                                    b'1 * 1/4                                                        %! baca.SegmentMaker._make_multimeasure_rest_container(1):PHANTOM:HIDDEN:NOTE
                                %@% ^ \baca-duration-multiplier-markup #"1" #"4"                     %! baca.SegmentMaker._label_duration_multipliers():DURATION_MULTIPLIER:HIDDEN:NOTE:PHANTOM:baca.SegmentMaker._style_phantom_measures(5)
            <BLANKLINE>
                                }                                                                    %! baca.SegmentMaker._make_multimeasure_rest_container(4):PHANTOM
            <BLANKLINE>
                                \context Voice = "Rest_Voice"                                        %! baca.SegmentMaker._make_multimeasure_rest_container(6):PHANTOM
                                {                                                                    %! baca.SegmentMaker._make_multimeasure_rest_container(6):PHANTOM
            <BLANKLINE>
                                    % [Rest_Voice measure 3]                                         %! baca.SegmentMaker._comment_measure_numbers():baca.SegmentMaker._style_phantom_measures(5):PHANTOM
                                    \once \override Score.TimeSignature.X-extent = ##f               %! baca.SegmentMaker._style_phantom_measures(6):PHANTOM
                                    \once \override MultiMeasureRest.transparent = ##t               %! baca.SegmentMaker._style_phantom_measures(7):PHANTOM
                                    \stopStaff                                                       %! baca.SegmentMaker._style_phantom_measures(8):PHANTOM
                                    \once \override Staff.StaffSymbol.transparent = ##t              %! baca.SegmentMaker._style_phantom_measures(8):PHANTOM
                                    \startStaff                                                      %! baca.SegmentMaker._style_phantom_measures(8):PHANTOM
                                    R1 * 1/4                                                         %! baca.SegmentMaker._make_multimeasure_rest_container(5):PHANTOM:REST_VOICE:MULTIMEASURE_REST
                                %@% ^ \baca-duration-multiplier-markup #"1" #"4"                     %! baca.SegmentMaker._label_duration_multipliers():DURATION_MULTIPLIER:MULTIMEASURE_REST:PHANTOM:REST_VOICE:baca.SegmentMaker._style_phantom_measures(5)
            <BLANKLINE>
                                }                                                                    %! baca.SegmentMaker._make_multimeasure_rest_container(6):PHANTOM
            <BLANKLINE>
                            >>                                                                       %! baca.SegmentMaker._make_multimeasure_rest_container(7):PHANTOM
            <BLANKLINE>
                        }                                                                            %! baca.SingleStaffScoreTemplate.__call__()
            <BLANKLINE>
                    }                                                                                %! baca.SingleStaffScoreTemplate.__call__()
            <BLANKLINE>
                >>                                                                                   %! baca.SingleStaffScoreTemplate.__call__()
            <BLANKLINE>
            >>                                                                                       %! baca.SingleStaffScoreTemplate.__call__()

        >>> score = lilypond_file[abjad.Score]
        >>> text = format(score, 'lilypond')
        >>> text = abjad.LilyPondFormatManager.left_shift_tags(text)
        >>> tags_ = abjad.tags.margin_markup_color_tags()
        >>> match = lambda tags: bool(set(tags) & set(tags_))
        >>> text, count = abjad.deactivate(text, match)
        >>> text = abjad.LilyPondFormatManager.left_shift_tags(text, 89)
        >>> lines = [_.strip('\n') for _ in text.split('\n')]
        >>> lilypond_file.score_block.items[:] = lines
        >>> abjad.show(lilypond_file, strict=89) # doctest: +SKIP

        ..  docs::

            >>> print(text)
            <BLANKLINE>
            \context Score = "Score"                                                                 %! baca.SingleStaffScoreTemplate.__call__()
            <<                                                                                       %! baca.SingleStaffScoreTemplate.__call__()
            <BLANKLINE>
                \context GlobalContext = "Global_Context"                                            %! abjad.ScoreTemplate._make_global_context()
                <<                                                                                   %! abjad.ScoreTemplate._make_global_context()
            <BLANKLINE>
                    \context GlobalSkips = "Global_Skips"                                            %! abjad.ScoreTemplate._make_global_context()
                    {                                                                                %! abjad.ScoreTemplate._make_global_context()
            <BLANKLINE>
                        % [Global_Skips measure 1]                                                   %! baca.SegmentMaker._comment_measure_numbers()
                        \baca-new-spacing-section #1 #24                                             %! SPACING_COMMAND:baca.HorizontalSpacingSpecifier.__call__(1)
                        \autoPageBreaksOff                                                           %! BREAK:baca.BreakMeasureMap.__call__(1)
                        \noBreak                                                                     %! BREAK:baca.BreakMeasureMap.__call__(2)
                        \baca-lbsd #0 #'(11)                                                         %! BREAK:baca.IndicatorCommand._call()
                        \time 3/8                                                                    %! baca.SegmentMaker._make_global_skips(2):baca.SegmentMaker._set_status_tag():EXPLICIT_TIME_SIGNATURE
                        \baca-time-signature-color #'blue                                            %! baca.SegmentMaker._attach_color_literal(2):EXPLICIT_TIME_SIGNATURE_COLOR
                        \pageBreak                                                                   %! BREAK:baca.IndicatorCommand._call()
                        s1 * 3/8                                                                     %! baca.SegmentMaker._make_global_skips(1)
            <BLANKLINE>
                        % [Global_Skips measure 2]                                                   %! baca.SegmentMaker._comment_measure_numbers()
                        \baca-new-spacing-section #1 #24                                             %! SPACING_COMMAND:baca.HorizontalSpacingSpecifier.__call__(1)
                        \noBreak                                                                     %! BREAK:baca.BreakMeasureMap.__call__(2)
                        \baca-lbsd #15 #'(11)                                                        %! BREAK:baca.IndicatorCommand._call()
                        \break                                                                       %! BREAK:baca.IndicatorCommand._call()
                        s1 * 3/8                                                                     %! baca.SegmentMaker._make_global_skips(1)
            <BLANKLINE>
                        % [Global_Skips measure 3]                                                   %! baca.SegmentMaker._comment_measure_numbers():baca.SegmentMaker._style_phantom_measures(1):PHANTOM
                        \baca-new-spacing-section #1 #4                                              %! SPACING_COMMAND:baca.HorizontalSpacingSpecifier.__call__(1):baca.SegmentMaker._style_phantom_measures(1):PHANTOM
                        \noBreak                                                                     %! BREAK:baca.BreakMeasureMap.__call__(2):baca.SegmentMaker._style_phantom_measures(1):PHANTOM
                        \time 1/4                                                                    %! baca.SegmentMaker._make_global_skips(3):PHANTOM:baca.SegmentMaker._set_status_tag():EXPLICIT_TIME_SIGNATURE:baca.SegmentMaker._style_phantom_measures(1)
                        \baca-time-signature-transparent                                             %! baca.SegmentMaker._style_phantom_measures(2):PHANTOM
                        s1 * 1/4                                                                     %! baca.SegmentMaker._make_global_skips(3):PHANTOM
                        \once \override Score.BarLine.transparent = ##t                              %! baca.SegmentMaker._style_phantom_measures(3):PHANTOM
                        \once \override Score.SpanBar.transparent = ##t                              %! baca.SegmentMaker._style_phantom_measures(3):PHANTOM
            <BLANKLINE>
                    }                                                                                %! abjad.ScoreTemplate._make_global_context()
            <BLANKLINE>
                >>                                                                                   %! abjad.ScoreTemplate._make_global_context()
            <BLANKLINE>
                \context MusicContext = "Music_Context"                                              %! baca.SingleStaffScoreTemplate.__call__()
                <<                                                                                   %! baca.SingleStaffScoreTemplate.__call__()
            <BLANKLINE>
                    \context Staff = "Music_Staff"                                                   %! baca.SingleStaffScoreTemplate.__call__()
                    {                                                                                %! baca.SingleStaffScoreTemplate.__call__()
            <BLANKLINE>
                        \context Voice = "Music_Voice"                                               %! baca.SingleStaffScoreTemplate.__call__()
                        {                                                                            %! baca.SingleStaffScoreTemplate.__call__()
            <BLANKLINE>
                            % [Music_Voice measure 1]                                                %! baca.SegmentMaker._comment_measure_numbers()
                            \set Staff.shortInstrumentName =                                         %! baca.margin_markup():baca.IndicatorCommand._call():baca.SegmentMaker._set_status_tag():EXPLICIT_MARGIN_MARKUP
                            \markup { I+II }                                                         %! baca.margin_markup():baca.IndicatorCommand._call():baca.SegmentMaker._set_status_tag():EXPLICIT_MARGIN_MARKUP
                        %%% \once \override Staff.InstrumentName.color = #(x11-color 'blue)          %! baca.SegmentMaker._attach_color_literal(2):EXPLICIT_MARGIN_MARKUP_COLOR
                    %@% \baca-not-yet-pitched-coloring                                               %! baca.SegmentMaker._color_not_yet_pitched():NOT_YET_PITCHED_COLORING
                            b'4.                                                                     %! baca.make_notes()
                        %%% ^ \baca-explicit-indicator-markup "[“I+II”]"                             %! EXPLICIT_MARGIN_MARKUP_ALERT:baca.SegmentMaker._attach_latent_indicator_alert()
                        %%% \override Staff.InstrumentName.color = #(x11-color 'DeepSkyBlue2)        %! baca.SegmentMaker._attach_color_literal(2):REDRAWN_EXPLICIT_MARGIN_MARKUP_COLOR
                            \set Staff.shortInstrumentName =                                         %! baca.margin_markup():baca.IndicatorCommand._call():baca.SegmentMaker._treat_persistent_wrapper(3):baca.SegmentMaker._set_status_tag():REDRAWN_EXPLICIT_MARGIN_MARKUP
                            \markup { I+II }                                                         %! baca.margin_markup():baca.IndicatorCommand._call():baca.SegmentMaker._treat_persistent_wrapper(3):baca.SegmentMaker._set_status_tag():REDRAWN_EXPLICIT_MARGIN_MARKUP
            <BLANKLINE>
                            % [Music_Voice measure 2]                                                %! baca.SegmentMaker._comment_measure_numbers()
                    %@% \baca-not-yet-pitched-coloring                                               %! baca.SegmentMaker._color_not_yet_pitched():NOT_YET_PITCHED_COLORING
                            b'4.                                                                     %! baca.make_notes()
            <BLANKLINE>
                            <<                                                                       %! baca.SegmentMaker._make_multimeasure_rest_container(7):PHANTOM
            <BLANKLINE>
                                \context Voice = "Music_Voice"                                       %! baca.SegmentMaker._make_multimeasure_rest_container(4):PHANTOM
                                {                                                                    %! baca.SegmentMaker._make_multimeasure_rest_container(4):PHANTOM
            <BLANKLINE>
                                    % [Music_Voice measure 3]                                        %! baca.SegmentMaker._comment_measure_numbers():baca.SegmentMaker._style_phantom_measures(5):PHANTOM
                                    \abjad-invisible-music-coloring                                  %! baca.SegmentMaker._make_multimeasure_rest_container(2):PHANTOM:NOTE:INVISIBLE_MUSIC_COLORING:baca.SegmentMaker._style_phantom_measures(5)
                            %@% \abjad-invisible-music                                               %! baca.SegmentMaker._make_multimeasure_rest_container(3):PHANTOM:NOTE:INVISIBLE_MUSIC_COMMAND:baca.SegmentMaker._style_phantom_measures(5)
                            %@% \baca-not-yet-pitched-coloring                                       %! baca.SegmentMaker._color_not_yet_pitched():NOT_YET_PITCHED_COLORING:HIDDEN:NOTE:baca.SegmentMaker._style_phantom_measures(5):PHANTOM
                                    b'1 * 1/4                                                        %! baca.SegmentMaker._make_multimeasure_rest_container(1):PHANTOM:HIDDEN:NOTE
                            %@% ^ \baca-duration-multiplier-markup #"1" #"4"                         %! baca.SegmentMaker._label_duration_multipliers():DURATION_MULTIPLIER:HIDDEN:NOTE:PHANTOM:baca.SegmentMaker._style_phantom_measures(5)
            <BLANKLINE>
                                }                                                                    %! baca.SegmentMaker._make_multimeasure_rest_container(4):PHANTOM
            <BLANKLINE>
                                \context Voice = "Rest_Voice"                                        %! baca.SegmentMaker._make_multimeasure_rest_container(6):PHANTOM
                                {                                                                    %! baca.SegmentMaker._make_multimeasure_rest_container(6):PHANTOM
            <BLANKLINE>
                                    % [Rest_Voice measure 3]                                         %! baca.SegmentMaker._comment_measure_numbers():baca.SegmentMaker._style_phantom_measures(5):PHANTOM
                                    \once \override Score.TimeSignature.X-extent = ##f               %! baca.SegmentMaker._style_phantom_measures(6):PHANTOM
                                    \once \override MultiMeasureRest.transparent = ##t               %! baca.SegmentMaker._style_phantom_measures(7):PHANTOM
                                    \stopStaff                                                       %! baca.SegmentMaker._style_phantom_measures(8):PHANTOM
                                    \once \override Staff.StaffSymbol.transparent = ##t              %! baca.SegmentMaker._style_phantom_measures(8):PHANTOM
                                    \startStaff                                                      %! baca.SegmentMaker._style_phantom_measures(8):PHANTOM
                                    R1 * 1/4                                                         %! baca.SegmentMaker._make_multimeasure_rest_container(5):PHANTOM:REST_VOICE:MULTIMEASURE_REST
                            %@% ^ \baca-duration-multiplier-markup #"1" #"4"                         %! baca.SegmentMaker._label_duration_multipliers():DURATION_MULTIPLIER:MULTIMEASURE_REST:PHANTOM:REST_VOICE:baca.SegmentMaker._style_phantom_measures(5)
            <BLANKLINE>
                                }                                                                    %! baca.SegmentMaker._make_multimeasure_rest_container(6):PHANTOM
            <BLANKLINE>
                            >>                                                                       %! baca.SegmentMaker._make_multimeasure_rest_container(7):PHANTOM
            <BLANKLINE>
                        }                                                                            %! baca.SingleStaffScoreTemplate.__call__()
            <BLANKLINE>
                    }                                                                                %! baca.SingleStaffScoreTemplate.__call__()
            <BLANKLINE>
                >>                                                                                   %! baca.SingleStaffScoreTemplate.__call__()
            <BLANKLINE>
            >>                                                                                       %! baca.SingleStaffScoreTemplate.__call__()

        >>> tags_ = abjad.tags.margin_markup_color_tags()
        >>> match = lambda tags: bool(set(tags) & set(tags_))
        >>> text, count = abjad.activate(text, match)
        >>> lines = [_.strip('\n') for _ in text.split('\n')]
        >>> lilypond_file.score_block.items[:] = lines
        >>> abjad.show(lilypond_file, strict=89) # doctest: +SKIP

        ..  docs::

            >>> print(text)
            <BLANKLINE>
            \context Score = "Score"                                                                 %! baca.SingleStaffScoreTemplate.__call__()
            <<                                                                                       %! baca.SingleStaffScoreTemplate.__call__()
            <BLANKLINE>
                \context GlobalContext = "Global_Context"                                            %! abjad.ScoreTemplate._make_global_context()
                <<                                                                                   %! abjad.ScoreTemplate._make_global_context()
            <BLANKLINE>
                    \context GlobalSkips = "Global_Skips"                                            %! abjad.ScoreTemplate._make_global_context()
                    {                                                                                %! abjad.ScoreTemplate._make_global_context()
            <BLANKLINE>
                        % [Global_Skips measure 1]                                                   %! baca.SegmentMaker._comment_measure_numbers()
                        \baca-new-spacing-section #1 #24                                             %! SPACING_COMMAND:baca.HorizontalSpacingSpecifier.__call__(1)
                        \autoPageBreaksOff                                                           %! BREAK:baca.BreakMeasureMap.__call__(1)
                        \noBreak                                                                     %! BREAK:baca.BreakMeasureMap.__call__(2)
                        \baca-lbsd #0 #'(11)                                                         %! BREAK:baca.IndicatorCommand._call()
                        \time 3/8                                                                    %! baca.SegmentMaker._make_global_skips(2):baca.SegmentMaker._set_status_tag():EXPLICIT_TIME_SIGNATURE
                        \baca-time-signature-color #'blue                                            %! baca.SegmentMaker._attach_color_literal(2):EXPLICIT_TIME_SIGNATURE_COLOR
                        \pageBreak                                                                   %! BREAK:baca.IndicatorCommand._call()
                        s1 * 3/8                                                                     %! baca.SegmentMaker._make_global_skips(1)
            <BLANKLINE>
                        % [Global_Skips measure 2]                                                   %! baca.SegmentMaker._comment_measure_numbers()
                        \baca-new-spacing-section #1 #24                                             %! SPACING_COMMAND:baca.HorizontalSpacingSpecifier.__call__(1)
                        \noBreak                                                                     %! BREAK:baca.BreakMeasureMap.__call__(2)
                        \baca-lbsd #15 #'(11)                                                        %! BREAK:baca.IndicatorCommand._call()
                        \break                                                                       %! BREAK:baca.IndicatorCommand._call()
                        s1 * 3/8                                                                     %! baca.SegmentMaker._make_global_skips(1)
            <BLANKLINE>
                        % [Global_Skips measure 3]                                                   %! baca.SegmentMaker._comment_measure_numbers():baca.SegmentMaker._style_phantom_measures(1):PHANTOM
                        \baca-new-spacing-section #1 #4                                              %! SPACING_COMMAND:baca.HorizontalSpacingSpecifier.__call__(1):baca.SegmentMaker._style_phantom_measures(1):PHANTOM
                        \noBreak                                                                     %! BREAK:baca.BreakMeasureMap.__call__(2):baca.SegmentMaker._style_phantom_measures(1):PHANTOM
                        \time 1/4                                                                    %! baca.SegmentMaker._make_global_skips(3):PHANTOM:baca.SegmentMaker._set_status_tag():EXPLICIT_TIME_SIGNATURE:baca.SegmentMaker._style_phantom_measures(1)
                        \baca-time-signature-transparent                                             %! baca.SegmentMaker._style_phantom_measures(2):PHANTOM
                        s1 * 1/4                                                                     %! baca.SegmentMaker._make_global_skips(3):PHANTOM
                        \once \override Score.BarLine.transparent = ##t                              %! baca.SegmentMaker._style_phantom_measures(3):PHANTOM
                        \once \override Score.SpanBar.transparent = ##t                              %! baca.SegmentMaker._style_phantom_measures(3):PHANTOM
            <BLANKLINE>
                    }                                                                                %! abjad.ScoreTemplate._make_global_context()
            <BLANKLINE>
                >>                                                                                   %! abjad.ScoreTemplate._make_global_context()
            <BLANKLINE>
                \context MusicContext = "Music_Context"                                              %! baca.SingleStaffScoreTemplate.__call__()
                <<                                                                                   %! baca.SingleStaffScoreTemplate.__call__()
            <BLANKLINE>
                    \context Staff = "Music_Staff"                                                   %! baca.SingleStaffScoreTemplate.__call__()
                    {                                                                                %! baca.SingleStaffScoreTemplate.__call__()
            <BLANKLINE>
                        \context Voice = "Music_Voice"                                               %! baca.SingleStaffScoreTemplate.__call__()
                        {                                                                            %! baca.SingleStaffScoreTemplate.__call__()
            <BLANKLINE>
                            % [Music_Voice measure 1]                                                %! baca.SegmentMaker._comment_measure_numbers()
                            \set Staff.shortInstrumentName =                                         %! baca.margin_markup():baca.IndicatorCommand._call():baca.SegmentMaker._set_status_tag():EXPLICIT_MARGIN_MARKUP
                            \markup { I+II }                                                         %! baca.margin_markup():baca.IndicatorCommand._call():baca.SegmentMaker._set_status_tag():EXPLICIT_MARGIN_MARKUP
                            \once \override Staff.InstrumentName.color = #(x11-color 'blue)          %! baca.SegmentMaker._attach_color_literal(2):EXPLICIT_MARGIN_MARKUP_COLOR
                    %@% \baca-not-yet-pitched-coloring                                               %! baca.SegmentMaker._color_not_yet_pitched():NOT_YET_PITCHED_COLORING
                            b'4.                                                                     %! baca.make_notes()
                            ^ \baca-explicit-indicator-markup "[“I+II”]"                             %! EXPLICIT_MARGIN_MARKUP_ALERT:baca.SegmentMaker._attach_latent_indicator_alert()
                            \override Staff.InstrumentName.color = #(x11-color 'DeepSkyBlue2)        %! baca.SegmentMaker._attach_color_literal(2):REDRAWN_EXPLICIT_MARGIN_MARKUP_COLOR
                            \set Staff.shortInstrumentName =                                         %! baca.margin_markup():baca.IndicatorCommand._call():baca.SegmentMaker._treat_persistent_wrapper(3):baca.SegmentMaker._set_status_tag():REDRAWN_EXPLICIT_MARGIN_MARKUP
                            \markup { I+II }                                                         %! baca.margin_markup():baca.IndicatorCommand._call():baca.SegmentMaker._treat_persistent_wrapper(3):baca.SegmentMaker._set_status_tag():REDRAWN_EXPLICIT_MARGIN_MARKUP
            <BLANKLINE>
                            % [Music_Voice measure 2]                                                %! baca.SegmentMaker._comment_measure_numbers()
                    %@% \baca-not-yet-pitched-coloring                                               %! baca.SegmentMaker._color_not_yet_pitched():NOT_YET_PITCHED_COLORING
                            b'4.                                                                     %! baca.make_notes()
            <BLANKLINE>
                            <<                                                                       %! baca.SegmentMaker._make_multimeasure_rest_container(7):PHANTOM
            <BLANKLINE>
                                \context Voice = "Music_Voice"                                       %! baca.SegmentMaker._make_multimeasure_rest_container(4):PHANTOM
                                {                                                                    %! baca.SegmentMaker._make_multimeasure_rest_container(4):PHANTOM
            <BLANKLINE>
                                    % [Music_Voice measure 3]                                        %! baca.SegmentMaker._comment_measure_numbers():baca.SegmentMaker._style_phantom_measures(5):PHANTOM
                                    \abjad-invisible-music-coloring                                  %! baca.SegmentMaker._make_multimeasure_rest_container(2):PHANTOM:NOTE:INVISIBLE_MUSIC_COLORING:baca.SegmentMaker._style_phantom_measures(5)
                            %@% \abjad-invisible-music                                               %! baca.SegmentMaker._make_multimeasure_rest_container(3):PHANTOM:NOTE:INVISIBLE_MUSIC_COMMAND:baca.SegmentMaker._style_phantom_measures(5)
                            %@% \baca-not-yet-pitched-coloring                                       %! baca.SegmentMaker._color_not_yet_pitched():NOT_YET_PITCHED_COLORING:HIDDEN:NOTE:baca.SegmentMaker._style_phantom_measures(5):PHANTOM
                                    b'1 * 1/4                                                        %! baca.SegmentMaker._make_multimeasure_rest_container(1):PHANTOM:HIDDEN:NOTE
                            %@% ^ \baca-duration-multiplier-markup #"1" #"4"                         %! baca.SegmentMaker._label_duration_multipliers():DURATION_MULTIPLIER:HIDDEN:NOTE:PHANTOM:baca.SegmentMaker._style_phantom_measures(5)
            <BLANKLINE>
                                }                                                                    %! baca.SegmentMaker._make_multimeasure_rest_container(4):PHANTOM
            <BLANKLINE>
                                \context Voice = "Rest_Voice"                                        %! baca.SegmentMaker._make_multimeasure_rest_container(6):PHANTOM
                                {                                                                    %! baca.SegmentMaker._make_multimeasure_rest_container(6):PHANTOM
            <BLANKLINE>
                                    % [Rest_Voice measure 3]                                         %! baca.SegmentMaker._comment_measure_numbers():baca.SegmentMaker._style_phantom_measures(5):PHANTOM
                                    \once \override Score.TimeSignature.X-extent = ##f               %! baca.SegmentMaker._style_phantom_measures(6):PHANTOM
                                    \once \override MultiMeasureRest.transparent = ##t               %! baca.SegmentMaker._style_phantom_measures(7):PHANTOM
                                    \stopStaff                                                       %! baca.SegmentMaker._style_phantom_measures(8):PHANTOM
                                    \once \override Staff.StaffSymbol.transparent = ##t              %! baca.SegmentMaker._style_phantom_measures(8):PHANTOM
                                    \startStaff                                                      %! baca.SegmentMaker._style_phantom_measures(8):PHANTOM
                                    R1 * 1/4                                                         %! baca.SegmentMaker._make_multimeasure_rest_container(5):PHANTOM:REST_VOICE:MULTIMEASURE_REST
                            %@% ^ \baca-duration-multiplier-markup #"1" #"4"                         %! baca.SegmentMaker._label_duration_multipliers():DURATION_MULTIPLIER:MULTIMEASURE_REST:PHANTOM:REST_VOICE:baca.SegmentMaker._style_phantom_measures(5)
            <BLANKLINE>
                                }                                                                    %! baca.SegmentMaker._make_multimeasure_rest_container(6):PHANTOM
            <BLANKLINE>
                            >>                                                                       %! baca.SegmentMaker._make_multimeasure_rest_container(7):PHANTOM
            <BLANKLINE>
                        }                                                                            %! baca.SingleStaffScoreTemplate.__call__()
            <BLANKLINE>
                    }                                                                                %! baca.SingleStaffScoreTemplate.__call__()
            <BLANKLINE>
                >>                                                                                   %! baca.SingleStaffScoreTemplate.__call__()
            <BLANKLINE>
            >>                                                                                       %! baca.SingleStaffScoreTemplate.__call__()

        Even after previous margin markup:

        >>> maker = baca.SegmentMaker(
        ...     breaks=breaks,
        ...     deactivate=[abjad.tags.NOT_YET_PITCHED_COLORING],
        ...     margin_markups=margin_markups,
        ...     score_template=baca.SingleStaffScoreTemplate(),
        ...     spacing=baca.minimum_duration((1, 24)),
        ...     time_signatures=[(3, 8), (3, 8)],
        ...     )
        >>> maker(
        ...     'Music_Voice',
        ...     baca.margin_markup(margin_markups['III+IV']),
        ...     baca.make_notes(),
        ...     )

        >>> metadata, persist = {}, {}
        >>> persist['persistent_indicators'] = {}
        >>> persist['persistent_indicators']['Music_Staff'] = [
        ...     abjad.Momento(
        ...         context='Music_Voice',
        ...         manifest='margin_markups',
        ...         value='I+II',
        ...         )
        ...     ]
        >>> metadata['segment_number'] = 1
        >>> lilypond_file = maker.run(
        ...     environment='docs',
        ...     previous_metadata=metadata,
        ...     previous_persist=persist,
        ...     )
        >>> block = abjad.Block(name='layout')
        >>> block.indent = 0
        >>> lilypond_file.items.insert(0, block)
        >>> abjad.show(lilypond_file, strict=89) # doctest: +SKIP

        ..  docs::

            >>> abjad.f(lilypond_file[abjad.Score], strict=89)
            <BLANKLINE>
            \context Score = "Score"                                                                 %! baca.SingleStaffScoreTemplate.__call__()
            <<                                                                                       %! baca.SingleStaffScoreTemplate.__call__()
            <BLANKLINE>
                \context GlobalContext = "Global_Context"                                            %! abjad.ScoreTemplate._make_global_context()
                <<                                                                                   %! abjad.ScoreTemplate._make_global_context()
            <BLANKLINE>
                    \context GlobalSkips = "Global_Skips"                                            %! abjad.ScoreTemplate._make_global_context()
                    {                                                                                %! abjad.ScoreTemplate._make_global_context()
            <BLANKLINE>
                        % [Global_Skips measure 1]                                                   %! baca.SegmentMaker._comment_measure_numbers()
                        \baca-new-spacing-section #1 #24                                             %! SPACING_COMMAND:baca.HorizontalSpacingSpecifier.__call__(1)
                        \autoPageBreaksOff                                                           %! BREAK:baca.BreakMeasureMap.__call__(1)
                        \noBreak                                                                     %! BREAK:baca.BreakMeasureMap.__call__(2)
                        \baca-lbsd #0 #'(11)                                                         %! BREAK:baca.IndicatorCommand._call()
                        \time 3/8                                                                    %! baca.SegmentMaker._make_global_skips(2):baca.SegmentMaker._set_status_tag():EXPLICIT_TIME_SIGNATURE
                        \bar ""                                                                      %! EMPTY_START_BAR:+SEGMENT:baca.SegmentMaker._make_global_skips(4)
                        \baca-time-signature-color #'blue                                            %! baca.SegmentMaker._attach_color_literal(2):EXPLICIT_TIME_SIGNATURE_COLOR
                        \pageBreak                                                                   %! BREAK:baca.IndicatorCommand._call()
                        s1 * 3/8                                                                     %! baca.SegmentMaker._make_global_skips(1)
            <BLANKLINE>
                        % [Global_Skips measure 2]                                                   %! baca.SegmentMaker._comment_measure_numbers()
                        \baca-new-spacing-section #1 #24                                             %! SPACING_COMMAND:baca.HorizontalSpacingSpecifier.__call__(1)
                        \noBreak                                                                     %! BREAK:baca.BreakMeasureMap.__call__(2)
                        \baca-lbsd #15 #'(11)                                                        %! BREAK:baca.IndicatorCommand._call()
                        \break                                                                       %! BREAK:baca.IndicatorCommand._call()
                        s1 * 3/8                                                                     %! baca.SegmentMaker._make_global_skips(1)
            <BLANKLINE>
                        % [Global_Skips measure 3]                                                   %! baca.SegmentMaker._comment_measure_numbers():baca.SegmentMaker._style_phantom_measures(1):PHANTOM
                        \baca-new-spacing-section #1 #4                                              %! SPACING_COMMAND:baca.HorizontalSpacingSpecifier.__call__(1):baca.SegmentMaker._style_phantom_measures(1):PHANTOM
                        \noBreak                                                                     %! BREAK:baca.BreakMeasureMap.__call__(2):baca.SegmentMaker._style_phantom_measures(1):PHANTOM
                        \time 1/4                                                                    %! baca.SegmentMaker._make_global_skips(3):PHANTOM:baca.SegmentMaker._set_status_tag():EXPLICIT_TIME_SIGNATURE:baca.SegmentMaker._style_phantom_measures(1)
                        \baca-time-signature-transparent                                             %! baca.SegmentMaker._style_phantom_measures(2):PHANTOM
                        s1 * 1/4                                                                     %! baca.SegmentMaker._make_global_skips(3):PHANTOM
                        \once \override Score.BarLine.transparent = ##t                              %! baca.SegmentMaker._style_phantom_measures(3):PHANTOM
                        \once \override Score.SpanBar.transparent = ##t                              %! baca.SegmentMaker._style_phantom_measures(3):PHANTOM
            <BLANKLINE>
                    }                                                                                %! abjad.ScoreTemplate._make_global_context()
            <BLANKLINE>
                >>                                                                                   %! abjad.ScoreTemplate._make_global_context()
            <BLANKLINE>
                \context MusicContext = "Music_Context"                                              %! baca.SingleStaffScoreTemplate.__call__()
                <<                                                                                   %! baca.SingleStaffScoreTemplate.__call__()
            <BLANKLINE>
                    \context Staff = "Music_Staff"                                                   %! baca.SingleStaffScoreTemplate.__call__()
                    {                                                                                %! baca.SingleStaffScoreTemplate.__call__()
            <BLANKLINE>
                        \context Voice = "Music_Voice"                                               %! baca.SingleStaffScoreTemplate.__call__()
                        {                                                                            %! baca.SingleStaffScoreTemplate.__call__()
            <BLANKLINE>
                            % [Music_Voice measure 1]                                                %! baca.SegmentMaker._comment_measure_numbers()
                            \set Staff.shortInstrumentName =                                         %! baca.margin_markup():baca.IndicatorCommand._call():baca.SegmentMaker._set_status_tag():EXPLICIT_MARGIN_MARKUP
                            \markup { III+IV }                                                       %! baca.margin_markup():baca.IndicatorCommand._call():baca.SegmentMaker._set_status_tag():EXPLICIT_MARGIN_MARKUP
                            \set Staff.instrumentName =                                              %! baca.SegmentMaker._clone_segment_initial_short_instrument_name()
                            \markup { III+IV }                                                       %! baca.SegmentMaker._clone_segment_initial_short_instrument_name()
                            \once \override Staff.InstrumentName.color = #(x11-color 'blue)          %! baca.SegmentMaker._attach_color_literal(2):EXPLICIT_MARGIN_MARKUP_COLOR
                        %@% \baca-not-yet-pitched-coloring                                           %! baca.SegmentMaker._color_not_yet_pitched():NOT_YET_PITCHED_COLORING
                            b'4.                                                                     %! baca.make_notes()
                            ^ \baca-explicit-indicator-markup "[“III+IV”]"                           %! EXPLICIT_MARGIN_MARKUP_ALERT:baca.SegmentMaker._attach_latent_indicator_alert()
                            \override Staff.InstrumentName.color = #(x11-color 'DeepSkyBlue2)        %! baca.SegmentMaker._attach_color_literal(2):REDRAWN_EXPLICIT_MARGIN_MARKUP_COLOR
                            \set Staff.shortInstrumentName =                                         %! baca.margin_markup():baca.IndicatorCommand._call():baca.SegmentMaker._treat_persistent_wrapper(3):baca.SegmentMaker._set_status_tag():REDRAWN_EXPLICIT_MARGIN_MARKUP
                            \markup { III+IV }                                                       %! baca.margin_markup():baca.IndicatorCommand._call():baca.SegmentMaker._treat_persistent_wrapper(3):baca.SegmentMaker._set_status_tag():REDRAWN_EXPLICIT_MARGIN_MARKUP
            <BLANKLINE>
                            % [Music_Voice measure 2]                                                %! baca.SegmentMaker._comment_measure_numbers()
                        %@% \baca-not-yet-pitched-coloring                                           %! baca.SegmentMaker._color_not_yet_pitched():NOT_YET_PITCHED_COLORING
                            b'4.                                                                     %! baca.make_notes()
            <BLANKLINE>
                            <<                                                                       %! baca.SegmentMaker._make_multimeasure_rest_container(7):PHANTOM
            <BLANKLINE>
                                \context Voice = "Music_Voice"                                       %! baca.SegmentMaker._make_multimeasure_rest_container(4):PHANTOM
                                {                                                                    %! baca.SegmentMaker._make_multimeasure_rest_container(4):PHANTOM
            <BLANKLINE>
                                    % [Music_Voice measure 3]                                        %! baca.SegmentMaker._comment_measure_numbers():baca.SegmentMaker._style_phantom_measures(5):PHANTOM
                                    \abjad-invisible-music-coloring                                  %! baca.SegmentMaker._make_multimeasure_rest_container(2):PHANTOM:NOTE:INVISIBLE_MUSIC_COLORING:baca.SegmentMaker._style_phantom_measures(5)
                                %@% \abjad-invisible-music                                           %! baca.SegmentMaker._make_multimeasure_rest_container(3):PHANTOM:NOTE:INVISIBLE_MUSIC_COMMAND:baca.SegmentMaker._style_phantom_measures(5)
                                %@% \baca-not-yet-pitched-coloring                                   %! baca.SegmentMaker._color_not_yet_pitched():NOT_YET_PITCHED_COLORING:HIDDEN:NOTE:baca.SegmentMaker._style_phantom_measures(5):PHANTOM
                                    b'1 * 1/4                                                        %! baca.SegmentMaker._make_multimeasure_rest_container(1):PHANTOM:HIDDEN:NOTE
                                %@% ^ \baca-duration-multiplier-markup #"1" #"4"                     %! baca.SegmentMaker._label_duration_multipliers():DURATION_MULTIPLIER:HIDDEN:NOTE:PHANTOM:baca.SegmentMaker._style_phantom_measures(5)
            <BLANKLINE>
                                }                                                                    %! baca.SegmentMaker._make_multimeasure_rest_container(4):PHANTOM
            <BLANKLINE>
                                \context Voice = "Rest_Voice"                                        %! baca.SegmentMaker._make_multimeasure_rest_container(6):PHANTOM
                                {                                                                    %! baca.SegmentMaker._make_multimeasure_rest_container(6):PHANTOM
            <BLANKLINE>
                                    % [Rest_Voice measure 3]                                         %! baca.SegmentMaker._comment_measure_numbers():baca.SegmentMaker._style_phantom_measures(5):PHANTOM
                                    \once \override Score.TimeSignature.X-extent = ##f               %! baca.SegmentMaker._style_phantom_measures(6):PHANTOM
                                    \once \override MultiMeasureRest.transparent = ##t               %! baca.SegmentMaker._style_phantom_measures(7):PHANTOM
                                    \stopStaff                                                       %! baca.SegmentMaker._style_phantom_measures(8):PHANTOM
                                    \once \override Staff.StaffSymbol.transparent = ##t              %! baca.SegmentMaker._style_phantom_measures(8):PHANTOM
                                    \startStaff                                                      %! baca.SegmentMaker._style_phantom_measures(8):PHANTOM
                                    R1 * 1/4                                                         %! baca.SegmentMaker._make_multimeasure_rest_container(5):PHANTOM:REST_VOICE:MULTIMEASURE_REST
                                %@% ^ \baca-duration-multiplier-markup #"1" #"4"                     %! baca.SegmentMaker._label_duration_multipliers():DURATION_MULTIPLIER:MULTIMEASURE_REST:PHANTOM:REST_VOICE:baca.SegmentMaker._style_phantom_measures(5)
            <BLANKLINE>
                                }                                                                    %! baca.SegmentMaker._make_multimeasure_rest_container(6):PHANTOM
            <BLANKLINE>
                            >>                                                                       %! baca.SegmentMaker._make_multimeasure_rest_container(7):PHANTOM
            <BLANKLINE>
                        }                                                                            %! baca.SingleStaffScoreTemplate.__call__()
            <BLANKLINE>
                    }                                                                                %! baca.SingleStaffScoreTemplate.__call__()
            <BLANKLINE>
                >>                                                                                   %! baca.SingleStaffScoreTemplate.__call__()
            <BLANKLINE>
            >>                                                                                       %! baca.SingleStaffScoreTemplate.__call__()

        >>> score = lilypond_file[abjad.Score]
        >>> text = format(score, 'lilypond')
        >>> text = abjad.LilyPondFormatManager.left_shift_tags(text)
        >>> tags_ = abjad.tags.margin_markup_color_tags()
        >>> match = lambda tags: bool(set(tags) & set(tags_))
        >>> text, count = abjad.deactivate(text, match)
        >>> text = abjad.LilyPondFormatManager.left_shift_tags(text, 89)
        >>> lines = [_.strip('\n') for _ in text.split('\n')]
        >>> lilypond_file.score_block.items[:] = lines
        >>> abjad.show(lilypond_file, strict=89) # doctest: +SKIP

        ..  docs::

            >>> print(text)
            <BLANKLINE>
            \context Score = "Score"                                                                 %! baca.SingleStaffScoreTemplate.__call__()
            <<                                                                                       %! baca.SingleStaffScoreTemplate.__call__()
            <BLANKLINE>
                \context GlobalContext = "Global_Context"                                            %! abjad.ScoreTemplate._make_global_context()
                <<                                                                                   %! abjad.ScoreTemplate._make_global_context()
            <BLANKLINE>
                    \context GlobalSkips = "Global_Skips"                                            %! abjad.ScoreTemplate._make_global_context()
                    {                                                                                %! abjad.ScoreTemplate._make_global_context()
            <BLANKLINE>
                        % [Global_Skips measure 1]                                                   %! baca.SegmentMaker._comment_measure_numbers()
                        \baca-new-spacing-section #1 #24                                             %! SPACING_COMMAND:baca.HorizontalSpacingSpecifier.__call__(1)
                        \autoPageBreaksOff                                                           %! BREAK:baca.BreakMeasureMap.__call__(1)
                        \noBreak                                                                     %! BREAK:baca.BreakMeasureMap.__call__(2)
                        \baca-lbsd #0 #'(11)                                                         %! BREAK:baca.IndicatorCommand._call()
                        \time 3/8                                                                    %! baca.SegmentMaker._make_global_skips(2):baca.SegmentMaker._set_status_tag():EXPLICIT_TIME_SIGNATURE
                        \bar ""                                                                      %! EMPTY_START_BAR:+SEGMENT:baca.SegmentMaker._make_global_skips(4)
                        \baca-time-signature-color #'blue                                            %! baca.SegmentMaker._attach_color_literal(2):EXPLICIT_TIME_SIGNATURE_COLOR
                        \pageBreak                                                                   %! BREAK:baca.IndicatorCommand._call()
                        s1 * 3/8                                                                     %! baca.SegmentMaker._make_global_skips(1)
            <BLANKLINE>
                        % [Global_Skips measure 2]                                                   %! baca.SegmentMaker._comment_measure_numbers()
                        \baca-new-spacing-section #1 #24                                             %! SPACING_COMMAND:baca.HorizontalSpacingSpecifier.__call__(1)
                        \noBreak                                                                     %! BREAK:baca.BreakMeasureMap.__call__(2)
                        \baca-lbsd #15 #'(11)                                                        %! BREAK:baca.IndicatorCommand._call()
                        \break                                                                       %! BREAK:baca.IndicatorCommand._call()
                        s1 * 3/8                                                                     %! baca.SegmentMaker._make_global_skips(1)
            <BLANKLINE>
                        % [Global_Skips measure 3]                                                   %! baca.SegmentMaker._comment_measure_numbers():baca.SegmentMaker._style_phantom_measures(1):PHANTOM
                        \baca-new-spacing-section #1 #4                                              %! SPACING_COMMAND:baca.HorizontalSpacingSpecifier.__call__(1):baca.SegmentMaker._style_phantom_measures(1):PHANTOM
                        \noBreak                                                                     %! BREAK:baca.BreakMeasureMap.__call__(2):baca.SegmentMaker._style_phantom_measures(1):PHANTOM
                        \time 1/4                                                                    %! baca.SegmentMaker._make_global_skips(3):PHANTOM:baca.SegmentMaker._set_status_tag():EXPLICIT_TIME_SIGNATURE:baca.SegmentMaker._style_phantom_measures(1)
                        \baca-time-signature-transparent                                             %! baca.SegmentMaker._style_phantom_measures(2):PHANTOM
                        s1 * 1/4                                                                     %! baca.SegmentMaker._make_global_skips(3):PHANTOM
                        \once \override Score.BarLine.transparent = ##t                              %! baca.SegmentMaker._style_phantom_measures(3):PHANTOM
                        \once \override Score.SpanBar.transparent = ##t                              %! baca.SegmentMaker._style_phantom_measures(3):PHANTOM
            <BLANKLINE>
                    }                                                                                %! abjad.ScoreTemplate._make_global_context()
            <BLANKLINE>
                >>                                                                                   %! abjad.ScoreTemplate._make_global_context()
            <BLANKLINE>
                \context MusicContext = "Music_Context"                                              %! baca.SingleStaffScoreTemplate.__call__()
                <<                                                                                   %! baca.SingleStaffScoreTemplate.__call__()
            <BLANKLINE>
                    \context Staff = "Music_Staff"                                                   %! baca.SingleStaffScoreTemplate.__call__()
                    {                                                                                %! baca.SingleStaffScoreTemplate.__call__()
            <BLANKLINE>
                        \context Voice = "Music_Voice"                                               %! baca.SingleStaffScoreTemplate.__call__()
                        {                                                                            %! baca.SingleStaffScoreTemplate.__call__()
            <BLANKLINE>
                            % [Music_Voice measure 1]                                                %! baca.SegmentMaker._comment_measure_numbers()
                            \set Staff.shortInstrumentName =                                         %! baca.margin_markup():baca.IndicatorCommand._call():baca.SegmentMaker._set_status_tag():EXPLICIT_MARGIN_MARKUP
                            \markup { III+IV }                                                       %! baca.margin_markup():baca.IndicatorCommand._call():baca.SegmentMaker._set_status_tag():EXPLICIT_MARGIN_MARKUP
                            \set Staff.instrumentName =                                              %! baca.SegmentMaker._clone_segment_initial_short_instrument_name()
                            \markup { III+IV }                                                       %! baca.SegmentMaker._clone_segment_initial_short_instrument_name()
                        %%% \once \override Staff.InstrumentName.color = #(x11-color 'blue)          %! baca.SegmentMaker._attach_color_literal(2):EXPLICIT_MARGIN_MARKUP_COLOR
                    %@% \baca-not-yet-pitched-coloring                                               %! baca.SegmentMaker._color_not_yet_pitched():NOT_YET_PITCHED_COLORING
                            b'4.                                                                     %! baca.make_notes()
                        %%% ^ \baca-explicit-indicator-markup "[“III+IV”]"                           %! EXPLICIT_MARGIN_MARKUP_ALERT:baca.SegmentMaker._attach_latent_indicator_alert()
                        %%% \override Staff.InstrumentName.color = #(x11-color 'DeepSkyBlue2)        %! baca.SegmentMaker._attach_color_literal(2):REDRAWN_EXPLICIT_MARGIN_MARKUP_COLOR
                            \set Staff.shortInstrumentName =                                         %! baca.margin_markup():baca.IndicatorCommand._call():baca.SegmentMaker._treat_persistent_wrapper(3):baca.SegmentMaker._set_status_tag():REDRAWN_EXPLICIT_MARGIN_MARKUP
                            \markup { III+IV }                                                       %! baca.margin_markup():baca.IndicatorCommand._call():baca.SegmentMaker._treat_persistent_wrapper(3):baca.SegmentMaker._set_status_tag():REDRAWN_EXPLICIT_MARGIN_MARKUP
            <BLANKLINE>
                            % [Music_Voice measure 2]                                                %! baca.SegmentMaker._comment_measure_numbers()
                    %@% \baca-not-yet-pitched-coloring                                               %! baca.SegmentMaker._color_not_yet_pitched():NOT_YET_PITCHED_COLORING
                            b'4.                                                                     %! baca.make_notes()
            <BLANKLINE>
                            <<                                                                       %! baca.SegmentMaker._make_multimeasure_rest_container(7):PHANTOM
            <BLANKLINE>
                                \context Voice = "Music_Voice"                                       %! baca.SegmentMaker._make_multimeasure_rest_container(4):PHANTOM
                                {                                                                    %! baca.SegmentMaker._make_multimeasure_rest_container(4):PHANTOM
            <BLANKLINE>
                                    % [Music_Voice measure 3]                                        %! baca.SegmentMaker._comment_measure_numbers():baca.SegmentMaker._style_phantom_measures(5):PHANTOM
                                    \abjad-invisible-music-coloring                                  %! baca.SegmentMaker._make_multimeasure_rest_container(2):PHANTOM:NOTE:INVISIBLE_MUSIC_COLORING:baca.SegmentMaker._style_phantom_measures(5)
                            %@% \abjad-invisible-music                                               %! baca.SegmentMaker._make_multimeasure_rest_container(3):PHANTOM:NOTE:INVISIBLE_MUSIC_COMMAND:baca.SegmentMaker._style_phantom_measures(5)
                            %@% \baca-not-yet-pitched-coloring                                       %! baca.SegmentMaker._color_not_yet_pitched():NOT_YET_PITCHED_COLORING:HIDDEN:NOTE:baca.SegmentMaker._style_phantom_measures(5):PHANTOM
                                    b'1 * 1/4                                                        %! baca.SegmentMaker._make_multimeasure_rest_container(1):PHANTOM:HIDDEN:NOTE
                            %@% ^ \baca-duration-multiplier-markup #"1" #"4"                         %! baca.SegmentMaker._label_duration_multipliers():DURATION_MULTIPLIER:HIDDEN:NOTE:PHANTOM:baca.SegmentMaker._style_phantom_measures(5)
            <BLANKLINE>
                                }                                                                    %! baca.SegmentMaker._make_multimeasure_rest_container(4):PHANTOM
            <BLANKLINE>
                                \context Voice = "Rest_Voice"                                        %! baca.SegmentMaker._make_multimeasure_rest_container(6):PHANTOM
                                {                                                                    %! baca.SegmentMaker._make_multimeasure_rest_container(6):PHANTOM
            <BLANKLINE>
                                    % [Rest_Voice measure 3]                                         %! baca.SegmentMaker._comment_measure_numbers():baca.SegmentMaker._style_phantom_measures(5):PHANTOM
                                    \once \override Score.TimeSignature.X-extent = ##f               %! baca.SegmentMaker._style_phantom_measures(6):PHANTOM
                                    \once \override MultiMeasureRest.transparent = ##t               %! baca.SegmentMaker._style_phantom_measures(7):PHANTOM
                                    \stopStaff                                                       %! baca.SegmentMaker._style_phantom_measures(8):PHANTOM
                                    \once \override Staff.StaffSymbol.transparent = ##t              %! baca.SegmentMaker._style_phantom_measures(8):PHANTOM
                                    \startStaff                                                      %! baca.SegmentMaker._style_phantom_measures(8):PHANTOM
                                    R1 * 1/4                                                         %! baca.SegmentMaker._make_multimeasure_rest_container(5):PHANTOM:REST_VOICE:MULTIMEASURE_REST
                            %@% ^ \baca-duration-multiplier-markup #"1" #"4"                         %! baca.SegmentMaker._label_duration_multipliers():DURATION_MULTIPLIER:MULTIMEASURE_REST:PHANTOM:REST_VOICE:baca.SegmentMaker._style_phantom_measures(5)
            <BLANKLINE>
                                }                                                                    %! baca.SegmentMaker._make_multimeasure_rest_container(6):PHANTOM
            <BLANKLINE>
                            >>                                                                       %! baca.SegmentMaker._make_multimeasure_rest_container(7):PHANTOM
            <BLANKLINE>
                        }                                                                            %! baca.SingleStaffScoreTemplate.__call__()
            <BLANKLINE>
                    }                                                                                %! baca.SingleStaffScoreTemplate.__call__()
            <BLANKLINE>
                >>                                                                                   %! baca.SingleStaffScoreTemplate.__call__()
            <BLANKLINE>
            >>                                                                                       %! baca.SingleStaffScoreTemplate.__call__()

        >>> tags_ = abjad.tags.margin_markup_color_tags()
        >>> match = lambda tags: bool(set(tags) & set(tags_))
        >>> text, count = abjad.activate(text, match)
        >>> lines = [_.strip('\n') for _ in text.split('\n')]
        >>> lilypond_file.score_block.items[:] = lines
        >>> abjad.show(lilypond_file, strict=89) # doctest: +SKIP

        ..  docs::

            >>> print(text)
            <BLANKLINE>
            \context Score = "Score"                                                                 %! baca.SingleStaffScoreTemplate.__call__()
            <<                                                                                       %! baca.SingleStaffScoreTemplate.__call__()
            <BLANKLINE>
                \context GlobalContext = "Global_Context"                                            %! abjad.ScoreTemplate._make_global_context()
                <<                                                                                   %! abjad.ScoreTemplate._make_global_context()
            <BLANKLINE>
                    \context GlobalSkips = "Global_Skips"                                            %! abjad.ScoreTemplate._make_global_context()
                    {                                                                                %! abjad.ScoreTemplate._make_global_context()
            <BLANKLINE>
                        % [Global_Skips measure 1]                                                   %! baca.SegmentMaker._comment_measure_numbers()
                        \baca-new-spacing-section #1 #24                                             %! SPACING_COMMAND:baca.HorizontalSpacingSpecifier.__call__(1)
                        \autoPageBreaksOff                                                           %! BREAK:baca.BreakMeasureMap.__call__(1)
                        \noBreak                                                                     %! BREAK:baca.BreakMeasureMap.__call__(2)
                        \baca-lbsd #0 #'(11)                                                         %! BREAK:baca.IndicatorCommand._call()
                        \time 3/8                                                                    %! baca.SegmentMaker._make_global_skips(2):baca.SegmentMaker._set_status_tag():EXPLICIT_TIME_SIGNATURE
                        \bar ""                                                                      %! EMPTY_START_BAR:+SEGMENT:baca.SegmentMaker._make_global_skips(4)
                        \baca-time-signature-color #'blue                                            %! baca.SegmentMaker._attach_color_literal(2):EXPLICIT_TIME_SIGNATURE_COLOR
                        \pageBreak                                                                   %! BREAK:baca.IndicatorCommand._call()
                        s1 * 3/8                                                                     %! baca.SegmentMaker._make_global_skips(1)
            <BLANKLINE>
                        % [Global_Skips measure 2]                                                   %! baca.SegmentMaker._comment_measure_numbers()
                        \baca-new-spacing-section #1 #24                                             %! SPACING_COMMAND:baca.HorizontalSpacingSpecifier.__call__(1)
                        \noBreak                                                                     %! BREAK:baca.BreakMeasureMap.__call__(2)
                        \baca-lbsd #15 #'(11)                                                        %! BREAK:baca.IndicatorCommand._call()
                        \break                                                                       %! BREAK:baca.IndicatorCommand._call()
                        s1 * 3/8                                                                     %! baca.SegmentMaker._make_global_skips(1)
            <BLANKLINE>
                        % [Global_Skips measure 3]                                                   %! baca.SegmentMaker._comment_measure_numbers():baca.SegmentMaker._style_phantom_measures(1):PHANTOM
                        \baca-new-spacing-section #1 #4                                              %! SPACING_COMMAND:baca.HorizontalSpacingSpecifier.__call__(1):baca.SegmentMaker._style_phantom_measures(1):PHANTOM
                        \noBreak                                                                     %! BREAK:baca.BreakMeasureMap.__call__(2):baca.SegmentMaker._style_phantom_measures(1):PHANTOM
                        \time 1/4                                                                    %! baca.SegmentMaker._make_global_skips(3):PHANTOM:baca.SegmentMaker._set_status_tag():EXPLICIT_TIME_SIGNATURE:baca.SegmentMaker._style_phantom_measures(1)
                        \baca-time-signature-transparent                                             %! baca.SegmentMaker._style_phantom_measures(2):PHANTOM
                        s1 * 1/4                                                                     %! baca.SegmentMaker._make_global_skips(3):PHANTOM
                        \once \override Score.BarLine.transparent = ##t                              %! baca.SegmentMaker._style_phantom_measures(3):PHANTOM
                        \once \override Score.SpanBar.transparent = ##t                              %! baca.SegmentMaker._style_phantom_measures(3):PHANTOM
            <BLANKLINE>
                    }                                                                                %! abjad.ScoreTemplate._make_global_context()
            <BLANKLINE>
                >>                                                                                   %! abjad.ScoreTemplate._make_global_context()
            <BLANKLINE>
                \context MusicContext = "Music_Context"                                              %! baca.SingleStaffScoreTemplate.__call__()
                <<                                                                                   %! baca.SingleStaffScoreTemplate.__call__()
            <BLANKLINE>
                    \context Staff = "Music_Staff"                                                   %! baca.SingleStaffScoreTemplate.__call__()
                    {                                                                                %! baca.SingleStaffScoreTemplate.__call__()
            <BLANKLINE>
                        \context Voice = "Music_Voice"                                               %! baca.SingleStaffScoreTemplate.__call__()
                        {                                                                            %! baca.SingleStaffScoreTemplate.__call__()
            <BLANKLINE>
                            % [Music_Voice measure 1]                                                %! baca.SegmentMaker._comment_measure_numbers()
                            \set Staff.shortInstrumentName =                                         %! baca.margin_markup():baca.IndicatorCommand._call():baca.SegmentMaker._set_status_tag():EXPLICIT_MARGIN_MARKUP
                            \markup { III+IV }                                                       %! baca.margin_markup():baca.IndicatorCommand._call():baca.SegmentMaker._set_status_tag():EXPLICIT_MARGIN_MARKUP
                            \set Staff.instrumentName =                                              %! baca.SegmentMaker._clone_segment_initial_short_instrument_name()
                            \markup { III+IV }                                                       %! baca.SegmentMaker._clone_segment_initial_short_instrument_name()
                            \once \override Staff.InstrumentName.color = #(x11-color 'blue)          %! baca.SegmentMaker._attach_color_literal(2):EXPLICIT_MARGIN_MARKUP_COLOR
                    %@% \baca-not-yet-pitched-coloring                                               %! baca.SegmentMaker._color_not_yet_pitched():NOT_YET_PITCHED_COLORING
                            b'4.                                                                     %! baca.make_notes()
                            ^ \baca-explicit-indicator-markup "[“III+IV”]"                           %! EXPLICIT_MARGIN_MARKUP_ALERT:baca.SegmentMaker._attach_latent_indicator_alert()
                            \override Staff.InstrumentName.color = #(x11-color 'DeepSkyBlue2)        %! baca.SegmentMaker._attach_color_literal(2):REDRAWN_EXPLICIT_MARGIN_MARKUP_COLOR
                            \set Staff.shortInstrumentName =                                         %! baca.margin_markup():baca.IndicatorCommand._call():baca.SegmentMaker._treat_persistent_wrapper(3):baca.SegmentMaker._set_status_tag():REDRAWN_EXPLICIT_MARGIN_MARKUP
                            \markup { III+IV }                                                       %! baca.margin_markup():baca.IndicatorCommand._call():baca.SegmentMaker._treat_persistent_wrapper(3):baca.SegmentMaker._set_status_tag():REDRAWN_EXPLICIT_MARGIN_MARKUP
            <BLANKLINE>
                            % [Music_Voice measure 2]                                                %! baca.SegmentMaker._comment_measure_numbers()
                    %@% \baca-not-yet-pitched-coloring                                               %! baca.SegmentMaker._color_not_yet_pitched():NOT_YET_PITCHED_COLORING
                            b'4.                                                                     %! baca.make_notes()
            <BLANKLINE>
                            <<                                                                       %! baca.SegmentMaker._make_multimeasure_rest_container(7):PHANTOM
            <BLANKLINE>
                                \context Voice = "Music_Voice"                                       %! baca.SegmentMaker._make_multimeasure_rest_container(4):PHANTOM
                                {                                                                    %! baca.SegmentMaker._make_multimeasure_rest_container(4):PHANTOM
            <BLANKLINE>
                                    % [Music_Voice measure 3]                                        %! baca.SegmentMaker._comment_measure_numbers():baca.SegmentMaker._style_phantom_measures(5):PHANTOM
                                    \abjad-invisible-music-coloring                                  %! baca.SegmentMaker._make_multimeasure_rest_container(2):PHANTOM:NOTE:INVISIBLE_MUSIC_COLORING:baca.SegmentMaker._style_phantom_measures(5)
                            %@% \abjad-invisible-music                                               %! baca.SegmentMaker._make_multimeasure_rest_container(3):PHANTOM:NOTE:INVISIBLE_MUSIC_COMMAND:baca.SegmentMaker._style_phantom_measures(5)
                            %@% \baca-not-yet-pitched-coloring                                       %! baca.SegmentMaker._color_not_yet_pitched():NOT_YET_PITCHED_COLORING:HIDDEN:NOTE:baca.SegmentMaker._style_phantom_measures(5):PHANTOM
                                    b'1 * 1/4                                                        %! baca.SegmentMaker._make_multimeasure_rest_container(1):PHANTOM:HIDDEN:NOTE
                            %@% ^ \baca-duration-multiplier-markup #"1" #"4"                         %! baca.SegmentMaker._label_duration_multipliers():DURATION_MULTIPLIER:HIDDEN:NOTE:PHANTOM:baca.SegmentMaker._style_phantom_measures(5)
            <BLANKLINE>
                                }                                                                    %! baca.SegmentMaker._make_multimeasure_rest_container(4):PHANTOM
            <BLANKLINE>
                                \context Voice = "Rest_Voice"                                        %! baca.SegmentMaker._make_multimeasure_rest_container(6):PHANTOM
                                {                                                                    %! baca.SegmentMaker._make_multimeasure_rest_container(6):PHANTOM
            <BLANKLINE>
                                    % [Rest_Voice measure 3]                                         %! baca.SegmentMaker._comment_measure_numbers():baca.SegmentMaker._style_phantom_measures(5):PHANTOM
                                    \once \override Score.TimeSignature.X-extent = ##f               %! baca.SegmentMaker._style_phantom_measures(6):PHANTOM
                                    \once \override MultiMeasureRest.transparent = ##t               %! baca.SegmentMaker._style_phantom_measures(7):PHANTOM
                                    \stopStaff                                                       %! baca.SegmentMaker._style_phantom_measures(8):PHANTOM
                                    \once \override Staff.StaffSymbol.transparent = ##t              %! baca.SegmentMaker._style_phantom_measures(8):PHANTOM
                                    \startStaff                                                      %! baca.SegmentMaker._style_phantom_measures(8):PHANTOM
                                    R1 * 1/4                                                         %! baca.SegmentMaker._make_multimeasure_rest_container(5):PHANTOM:REST_VOICE:MULTIMEASURE_REST
                            %@% ^ \baca-duration-multiplier-markup #"1" #"4"                         %! baca.SegmentMaker._label_duration_multipliers():DURATION_MULTIPLIER:MULTIMEASURE_REST:PHANTOM:REST_VOICE:baca.SegmentMaker._style_phantom_measures(5)
            <BLANKLINE>
                                }                                                                    %! baca.SegmentMaker._make_multimeasure_rest_container(6):PHANTOM
            <BLANKLINE>
                            >>                                                                       %! baca.SegmentMaker._make_multimeasure_rest_container(7):PHANTOM
            <BLANKLINE>
                        }                                                                            %! baca.SingleStaffScoreTemplate.__call__()
            <BLANKLINE>
                    }                                                                                %! baca.SingleStaffScoreTemplate.__call__()
            <BLANKLINE>
                >>                                                                                   %! baca.SingleStaffScoreTemplate.__call__()
            <BLANKLINE>
            >>                                                                                       %! baca.SingleStaffScoreTemplate.__call__()

    ..  container:: example

        Reapplied margin markup color green and redraw dull green:

        >>> maker = baca.SegmentMaker(
        ...     breaks=breaks,
        ...     deactivate=[abjad.tags.NOT_YET_PITCHED_COLORING],
        ...     margin_markups=margin_markups,
        ...     score_template=baca.SingleStaffScoreTemplate(),
        ...     spacing=baca.minimum_duration((1, 24)),
        ...     time_signatures=[(3, 8), (3, 8)],
        ...     )
        >>> maker(
        ...     'Music_Voice',
        ...     baca.make_notes(),
        ...     )

        >>> metadata, persist = {}, {}
        >>> persist['persistent_indicators'] = {}
        >>> persist['persistent_indicators']['Music_Staff'] = [
        ...     abjad.Momento(
        ...         context='Music_Voice',
        ...         manifest='margin_markups',
        ...         value='I+II',
        ...         )
        ...     ]
        >>> metadata['segment_number'] = 1
        >>> lilypond_file = maker.run(
        ...     environment='docs',
        ...     previous_metadata=metadata,
        ...     previous_persist=persist,
        ...     )
        >>> block = abjad.Block(name='layout')
        >>> block.indent = 0
        >>> lilypond_file.items.insert(0, block)
        >>> abjad.show(lilypond_file, strict=89) # doctest: +SKIP

        ..  docs::

            >>> abjad.f(lilypond_file[abjad.Score], strict=89)
            <BLANKLINE>
            \context Score = "Score"                                                                 %! baca.SingleStaffScoreTemplate.__call__()
            <<                                                                                       %! baca.SingleStaffScoreTemplate.__call__()
            <BLANKLINE>
                \context GlobalContext = "Global_Context"                                            %! abjad.ScoreTemplate._make_global_context()
                <<                                                                                   %! abjad.ScoreTemplate._make_global_context()
            <BLANKLINE>
                    \context GlobalSkips = "Global_Skips"                                            %! abjad.ScoreTemplate._make_global_context()
                    {                                                                                %! abjad.ScoreTemplate._make_global_context()
            <BLANKLINE>
                        % [Global_Skips measure 1]                                                   %! baca.SegmentMaker._comment_measure_numbers()
                        \baca-new-spacing-section #1 #24                                             %! SPACING_COMMAND:baca.HorizontalSpacingSpecifier.__call__(1)
                        \autoPageBreaksOff                                                           %! BREAK:baca.BreakMeasureMap.__call__(1)
                        \noBreak                                                                     %! BREAK:baca.BreakMeasureMap.__call__(2)
                        \baca-lbsd #0 #'(11)                                                         %! BREAK:baca.IndicatorCommand._call()
                        \time 3/8                                                                    %! baca.SegmentMaker._make_global_skips(2):baca.SegmentMaker._set_status_tag():EXPLICIT_TIME_SIGNATURE
                        \bar ""                                                                      %! EMPTY_START_BAR:+SEGMENT:baca.SegmentMaker._make_global_skips(4)
                        \baca-time-signature-color #'blue                                            %! baca.SegmentMaker._attach_color_literal(2):EXPLICIT_TIME_SIGNATURE_COLOR
                        \pageBreak                                                                   %! BREAK:baca.IndicatorCommand._call()
                        s1 * 3/8                                                                     %! baca.SegmentMaker._make_global_skips(1)
            <BLANKLINE>
                        % [Global_Skips measure 2]                                                   %! baca.SegmentMaker._comment_measure_numbers()
                        \baca-new-spacing-section #1 #24                                             %! SPACING_COMMAND:baca.HorizontalSpacingSpecifier.__call__(1)
                        \noBreak                                                                     %! BREAK:baca.BreakMeasureMap.__call__(2)
                        \baca-lbsd #15 #'(11)                                                        %! BREAK:baca.IndicatorCommand._call()
                        \break                                                                       %! BREAK:baca.IndicatorCommand._call()
                        s1 * 3/8                                                                     %! baca.SegmentMaker._make_global_skips(1)
            <BLANKLINE>
                        % [Global_Skips measure 3]                                                   %! baca.SegmentMaker._comment_measure_numbers():baca.SegmentMaker._style_phantom_measures(1):PHANTOM
                        \baca-new-spacing-section #1 #4                                              %! SPACING_COMMAND:baca.HorizontalSpacingSpecifier.__call__(1):baca.SegmentMaker._style_phantom_measures(1):PHANTOM
                        \noBreak                                                                     %! BREAK:baca.BreakMeasureMap.__call__(2):baca.SegmentMaker._style_phantom_measures(1):PHANTOM
                        \time 1/4                                                                    %! baca.SegmentMaker._make_global_skips(3):PHANTOM:baca.SegmentMaker._set_status_tag():EXPLICIT_TIME_SIGNATURE:baca.SegmentMaker._style_phantom_measures(1)
                        \baca-time-signature-transparent                                             %! baca.SegmentMaker._style_phantom_measures(2):PHANTOM
                        s1 * 1/4                                                                     %! baca.SegmentMaker._make_global_skips(3):PHANTOM
                        \once \override Score.BarLine.transparent = ##t                              %! baca.SegmentMaker._style_phantom_measures(3):PHANTOM
                        \once \override Score.SpanBar.transparent = ##t                              %! baca.SegmentMaker._style_phantom_measures(3):PHANTOM
            <BLANKLINE>
                    }                                                                                %! abjad.ScoreTemplate._make_global_context()
            <BLANKLINE>
                >>                                                                                   %! abjad.ScoreTemplate._make_global_context()
            <BLANKLINE>
                \context MusicContext = "Music_Context"                                              %! baca.SingleStaffScoreTemplate.__call__()
                <<                                                                                   %! baca.SingleStaffScoreTemplate.__call__()
            <BLANKLINE>
                    \context Staff = "Music_Staff"                                                   %! baca.SingleStaffScoreTemplate.__call__()
                    {                                                                                %! baca.SingleStaffScoreTemplate.__call__()
            <BLANKLINE>
                        \context Voice = "Music_Voice"                                               %! baca.SingleStaffScoreTemplate.__call__()
                        {                                                                            %! baca.SingleStaffScoreTemplate.__call__()
            <BLANKLINE>
                            % [Music_Voice measure 1]                                                %! baca.SegmentMaker._comment_measure_numbers()
                            \set Staff.shortInstrumentName =                                         %! baca.SegmentMaker._reapply_persistent_indicators(3):-PARTS:baca.SegmentMaker._set_status_tag():REAPPLIED_MARGIN_MARKUP
                            \markup { I+II }                                                         %! baca.SegmentMaker._reapply_persistent_indicators(3):-PARTS:baca.SegmentMaker._set_status_tag():REAPPLIED_MARGIN_MARKUP
                            \set Staff.instrumentName =                                              %! baca.SegmentMaker._clone_segment_initial_short_instrument_name()
                            \markup { I+II }                                                         %! baca.SegmentMaker._clone_segment_initial_short_instrument_name()
                            \once \override Staff.InstrumentName.color = #(x11-color 'green4)        %! baca.SegmentMaker._attach_color_literal(2):REAPPLIED_MARGIN_MARKUP_COLOR
                        %@% \baca-not-yet-pitched-coloring                                           %! baca.SegmentMaker._color_not_yet_pitched():NOT_YET_PITCHED_COLORING
                            b'4.                                                                     %! baca.make_notes()
                            ^ \baca-reapplied-indicator-markup "[“I+II”]"                            %! REAPPLIED_MARGIN_MARKUP_ALERT:baca.SegmentMaker._attach_latent_indicator_alert()
                            \override Staff.InstrumentName.color = #(x11-color 'OliveDrab)           %! baca.SegmentMaker._attach_color_literal(2):REDRAWN_REAPPLIED_MARGIN_MARKUP_COLOR
                            \set Staff.shortInstrumentName =                                         %! baca.SegmentMaker._reapply_persistent_indicators(3):-PARTS:baca.SegmentMaker._treat_persistent_wrapper(3):baca.SegmentMaker._set_status_tag():REDRAWN_REAPPLIED_MARGIN_MARKUP
                            \markup { I+II }                                                         %! baca.SegmentMaker._reapply_persistent_indicators(3):-PARTS:baca.SegmentMaker._treat_persistent_wrapper(3):baca.SegmentMaker._set_status_tag():REDRAWN_REAPPLIED_MARGIN_MARKUP
            <BLANKLINE>
                            % [Music_Voice measure 2]                                                %! baca.SegmentMaker._comment_measure_numbers()
                        %@% \baca-not-yet-pitched-coloring                                           %! baca.SegmentMaker._color_not_yet_pitched():NOT_YET_PITCHED_COLORING
                            b'4.                                                                     %! baca.make_notes()
            <BLANKLINE>
                            <<                                                                       %! baca.SegmentMaker._make_multimeasure_rest_container(7):PHANTOM
            <BLANKLINE>
                                \context Voice = "Music_Voice"                                       %! baca.SegmentMaker._make_multimeasure_rest_container(4):PHANTOM
                                {                                                                    %! baca.SegmentMaker._make_multimeasure_rest_container(4):PHANTOM
            <BLANKLINE>
                                    % [Music_Voice measure 3]                                        %! baca.SegmentMaker._comment_measure_numbers():baca.SegmentMaker._style_phantom_measures(5):PHANTOM
                                    \abjad-invisible-music-coloring                                  %! baca.SegmentMaker._make_multimeasure_rest_container(2):PHANTOM:NOTE:INVISIBLE_MUSIC_COLORING:baca.SegmentMaker._style_phantom_measures(5)
                                %@% \abjad-invisible-music                                           %! baca.SegmentMaker._make_multimeasure_rest_container(3):PHANTOM:NOTE:INVISIBLE_MUSIC_COMMAND:baca.SegmentMaker._style_phantom_measures(5)
                                %@% \baca-not-yet-pitched-coloring                                   %! baca.SegmentMaker._color_not_yet_pitched():NOT_YET_PITCHED_COLORING:HIDDEN:NOTE:baca.SegmentMaker._style_phantom_measures(5):PHANTOM
                                    b'1 * 1/4                                                        %! baca.SegmentMaker._make_multimeasure_rest_container(1):PHANTOM:HIDDEN:NOTE
                                %@% ^ \baca-duration-multiplier-markup #"1" #"4"                     %! baca.SegmentMaker._label_duration_multipliers():DURATION_MULTIPLIER:HIDDEN:NOTE:PHANTOM:baca.SegmentMaker._style_phantom_measures(5)
            <BLANKLINE>
                                }                                                                    %! baca.SegmentMaker._make_multimeasure_rest_container(4):PHANTOM
            <BLANKLINE>
                                \context Voice = "Rest_Voice"                                        %! baca.SegmentMaker._make_multimeasure_rest_container(6):PHANTOM
                                {                                                                    %! baca.SegmentMaker._make_multimeasure_rest_container(6):PHANTOM
            <BLANKLINE>
                                    % [Rest_Voice measure 3]                                         %! baca.SegmentMaker._comment_measure_numbers():baca.SegmentMaker._style_phantom_measures(5):PHANTOM
                                    \once \override Score.TimeSignature.X-extent = ##f               %! baca.SegmentMaker._style_phantom_measures(6):PHANTOM
                                    \once \override MultiMeasureRest.transparent = ##t               %! baca.SegmentMaker._style_phantom_measures(7):PHANTOM
                                    \stopStaff                                                       %! baca.SegmentMaker._style_phantom_measures(8):PHANTOM
                                    \once \override Staff.StaffSymbol.transparent = ##t              %! baca.SegmentMaker._style_phantom_measures(8):PHANTOM
                                    \startStaff                                                      %! baca.SegmentMaker._style_phantom_measures(8):PHANTOM
                                    R1 * 1/4                                                         %! baca.SegmentMaker._make_multimeasure_rest_container(5):PHANTOM:REST_VOICE:MULTIMEASURE_REST
                                %@% ^ \baca-duration-multiplier-markup #"1" #"4"                     %! baca.SegmentMaker._label_duration_multipliers():DURATION_MULTIPLIER:MULTIMEASURE_REST:PHANTOM:REST_VOICE:baca.SegmentMaker._style_phantom_measures(5)
            <BLANKLINE>
                                }                                                                    %! baca.SegmentMaker._make_multimeasure_rest_container(6):PHANTOM
            <BLANKLINE>
                            >>                                                                       %! baca.SegmentMaker._make_multimeasure_rest_container(7):PHANTOM
            <BLANKLINE>
                        }                                                                            %! baca.SingleStaffScoreTemplate.__call__()
            <BLANKLINE>
                    }                                                                                %! baca.SingleStaffScoreTemplate.__call__()
            <BLANKLINE>
                >>                                                                                   %! baca.SingleStaffScoreTemplate.__call__()
            <BLANKLINE>
            >>                                                                                       %! baca.SingleStaffScoreTemplate.__call__()

        >>> score = lilypond_file[abjad.Score]
        >>> text = format(score, 'lilypond')
        >>> text = abjad.LilyPondFormatManager.left_shift_tags(text)
        >>> tags_ = abjad.tags.margin_markup_color_tags()
        >>> match = lambda tags: bool(set(tags) & set(tags_))
        >>> text, count = abjad.deactivate(text, match)
        >>> text = abjad.LilyPondFormatManager.left_shift_tags(text, 89)
        >>> lines = [_.strip('\n') for _ in text.split('\n')]
        >>> lilypond_file.score_block.items[:] = lines
        >>> abjad.show(lilypond_file, strict=89) # doctest: +SKIP

        ..  docs::

            >>> print(text)
            <BLANKLINE>
            \context Score = "Score"                                                                 %! baca.SingleStaffScoreTemplate.__call__()
            <<                                                                                       %! baca.SingleStaffScoreTemplate.__call__()
            <BLANKLINE>
                \context GlobalContext = "Global_Context"                                            %! abjad.ScoreTemplate._make_global_context()
                <<                                                                                   %! abjad.ScoreTemplate._make_global_context()
            <BLANKLINE>
                    \context GlobalSkips = "Global_Skips"                                            %! abjad.ScoreTemplate._make_global_context()
                    {                                                                                %! abjad.ScoreTemplate._make_global_context()
            <BLANKLINE>
                        % [Global_Skips measure 1]                                                   %! baca.SegmentMaker._comment_measure_numbers()
                        \baca-new-spacing-section #1 #24                                             %! SPACING_COMMAND:baca.HorizontalSpacingSpecifier.__call__(1)
                        \autoPageBreaksOff                                                           %! BREAK:baca.BreakMeasureMap.__call__(1)
                        \noBreak                                                                     %! BREAK:baca.BreakMeasureMap.__call__(2)
                        \baca-lbsd #0 #'(11)                                                         %! BREAK:baca.IndicatorCommand._call()
                        \time 3/8                                                                    %! baca.SegmentMaker._make_global_skips(2):baca.SegmentMaker._set_status_tag():EXPLICIT_TIME_SIGNATURE
                        \bar ""                                                                      %! EMPTY_START_BAR:+SEGMENT:baca.SegmentMaker._make_global_skips(4)
                        \baca-time-signature-color #'blue                                            %! baca.SegmentMaker._attach_color_literal(2):EXPLICIT_TIME_SIGNATURE_COLOR
                        \pageBreak                                                                   %! BREAK:baca.IndicatorCommand._call()
                        s1 * 3/8                                                                     %! baca.SegmentMaker._make_global_skips(1)
            <BLANKLINE>
                        % [Global_Skips measure 2]                                                   %! baca.SegmentMaker._comment_measure_numbers()
                        \baca-new-spacing-section #1 #24                                             %! SPACING_COMMAND:baca.HorizontalSpacingSpecifier.__call__(1)
                        \noBreak                                                                     %! BREAK:baca.BreakMeasureMap.__call__(2)
                        \baca-lbsd #15 #'(11)                                                        %! BREAK:baca.IndicatorCommand._call()
                        \break                                                                       %! BREAK:baca.IndicatorCommand._call()
                        s1 * 3/8                                                                     %! baca.SegmentMaker._make_global_skips(1)
            <BLANKLINE>
                        % [Global_Skips measure 3]                                                   %! baca.SegmentMaker._comment_measure_numbers():baca.SegmentMaker._style_phantom_measures(1):PHANTOM
                        \baca-new-spacing-section #1 #4                                              %! SPACING_COMMAND:baca.HorizontalSpacingSpecifier.__call__(1):baca.SegmentMaker._style_phantom_measures(1):PHANTOM
                        \noBreak                                                                     %! BREAK:baca.BreakMeasureMap.__call__(2):baca.SegmentMaker._style_phantom_measures(1):PHANTOM
                        \time 1/4                                                                    %! baca.SegmentMaker._make_global_skips(3):PHANTOM:baca.SegmentMaker._set_status_tag():EXPLICIT_TIME_SIGNATURE:baca.SegmentMaker._style_phantom_measures(1)
                        \baca-time-signature-transparent                                             %! baca.SegmentMaker._style_phantom_measures(2):PHANTOM
                        s1 * 1/4                                                                     %! baca.SegmentMaker._make_global_skips(3):PHANTOM
                        \once \override Score.BarLine.transparent = ##t                              %! baca.SegmentMaker._style_phantom_measures(3):PHANTOM
                        \once \override Score.SpanBar.transparent = ##t                              %! baca.SegmentMaker._style_phantom_measures(3):PHANTOM
            <BLANKLINE>
                    }                                                                                %! abjad.ScoreTemplate._make_global_context()
            <BLANKLINE>
                >>                                                                                   %! abjad.ScoreTemplate._make_global_context()
            <BLANKLINE>
                \context MusicContext = "Music_Context"                                              %! baca.SingleStaffScoreTemplate.__call__()
                <<                                                                                   %! baca.SingleStaffScoreTemplate.__call__()
            <BLANKLINE>
                    \context Staff = "Music_Staff"                                                   %! baca.SingleStaffScoreTemplate.__call__()
                    {                                                                                %! baca.SingleStaffScoreTemplate.__call__()
            <BLANKLINE>
                        \context Voice = "Music_Voice"                                               %! baca.SingleStaffScoreTemplate.__call__()
                        {                                                                            %! baca.SingleStaffScoreTemplate.__call__()
            <BLANKLINE>
                            % [Music_Voice measure 1]                                                %! baca.SegmentMaker._comment_measure_numbers()
                            \set Staff.shortInstrumentName =                                         %! baca.SegmentMaker._reapply_persistent_indicators(3):-PARTS:baca.SegmentMaker._set_status_tag():REAPPLIED_MARGIN_MARKUP
                            \markup { I+II }                                                         %! baca.SegmentMaker._reapply_persistent_indicators(3):-PARTS:baca.SegmentMaker._set_status_tag():REAPPLIED_MARGIN_MARKUP
                            \set Staff.instrumentName =                                              %! baca.SegmentMaker._clone_segment_initial_short_instrument_name()
                            \markup { I+II }                                                         %! baca.SegmentMaker._clone_segment_initial_short_instrument_name()
                        %%% \once \override Staff.InstrumentName.color = #(x11-color 'green4)        %! baca.SegmentMaker._attach_color_literal(2):REAPPLIED_MARGIN_MARKUP_COLOR
                    %@% \baca-not-yet-pitched-coloring                                               %! baca.SegmentMaker._color_not_yet_pitched():NOT_YET_PITCHED_COLORING
                            b'4.                                                                     %! baca.make_notes()
                        %%% ^ \baca-reapplied-indicator-markup "[“I+II”]"                            %! REAPPLIED_MARGIN_MARKUP_ALERT:baca.SegmentMaker._attach_latent_indicator_alert()
                        %%% \override Staff.InstrumentName.color = #(x11-color 'OliveDrab)           %! baca.SegmentMaker._attach_color_literal(2):REDRAWN_REAPPLIED_MARGIN_MARKUP_COLOR
                            \set Staff.shortInstrumentName =                                         %! baca.SegmentMaker._reapply_persistent_indicators(3):-PARTS:baca.SegmentMaker._treat_persistent_wrapper(3):baca.SegmentMaker._set_status_tag():REDRAWN_REAPPLIED_MARGIN_MARKUP
                            \markup { I+II }                                                         %! baca.SegmentMaker._reapply_persistent_indicators(3):-PARTS:baca.SegmentMaker._treat_persistent_wrapper(3):baca.SegmentMaker._set_status_tag():REDRAWN_REAPPLIED_MARGIN_MARKUP
            <BLANKLINE>
                            % [Music_Voice measure 2]                                                %! baca.SegmentMaker._comment_measure_numbers()
                    %@% \baca-not-yet-pitched-coloring                                               %! baca.SegmentMaker._color_not_yet_pitched():NOT_YET_PITCHED_COLORING
                            b'4.                                                                     %! baca.make_notes()
            <BLANKLINE>
                            <<                                                                       %! baca.SegmentMaker._make_multimeasure_rest_container(7):PHANTOM
            <BLANKLINE>
                                \context Voice = "Music_Voice"                                       %! baca.SegmentMaker._make_multimeasure_rest_container(4):PHANTOM
                                {                                                                    %! baca.SegmentMaker._make_multimeasure_rest_container(4):PHANTOM
            <BLANKLINE>
                                    % [Music_Voice measure 3]                                        %! baca.SegmentMaker._comment_measure_numbers():baca.SegmentMaker._style_phantom_measures(5):PHANTOM
                                    \abjad-invisible-music-coloring                                  %! baca.SegmentMaker._make_multimeasure_rest_container(2):PHANTOM:NOTE:INVISIBLE_MUSIC_COLORING:baca.SegmentMaker._style_phantom_measures(5)
                            %@% \abjad-invisible-music                                               %! baca.SegmentMaker._make_multimeasure_rest_container(3):PHANTOM:NOTE:INVISIBLE_MUSIC_COMMAND:baca.SegmentMaker._style_phantom_measures(5)
                            %@% \baca-not-yet-pitched-coloring                                       %! baca.SegmentMaker._color_not_yet_pitched():NOT_YET_PITCHED_COLORING:HIDDEN:NOTE:baca.SegmentMaker._style_phantom_measures(5):PHANTOM
                                    b'1 * 1/4                                                        %! baca.SegmentMaker._make_multimeasure_rest_container(1):PHANTOM:HIDDEN:NOTE
                            %@% ^ \baca-duration-multiplier-markup #"1" #"4"                         %! baca.SegmentMaker._label_duration_multipliers():DURATION_MULTIPLIER:HIDDEN:NOTE:PHANTOM:baca.SegmentMaker._style_phantom_measures(5)
            <BLANKLINE>
                                }                                                                    %! baca.SegmentMaker._make_multimeasure_rest_container(4):PHANTOM
            <BLANKLINE>
                                \context Voice = "Rest_Voice"                                        %! baca.SegmentMaker._make_multimeasure_rest_container(6):PHANTOM
                                {                                                                    %! baca.SegmentMaker._make_multimeasure_rest_container(6):PHANTOM
            <BLANKLINE>
                                    % [Rest_Voice measure 3]                                         %! baca.SegmentMaker._comment_measure_numbers():baca.SegmentMaker._style_phantom_measures(5):PHANTOM
                                    \once \override Score.TimeSignature.X-extent = ##f               %! baca.SegmentMaker._style_phantom_measures(6):PHANTOM
                                    \once \override MultiMeasureRest.transparent = ##t               %! baca.SegmentMaker._style_phantom_measures(7):PHANTOM
                                    \stopStaff                                                       %! baca.SegmentMaker._style_phantom_measures(8):PHANTOM
                                    \once \override Staff.StaffSymbol.transparent = ##t              %! baca.SegmentMaker._style_phantom_measures(8):PHANTOM
                                    \startStaff                                                      %! baca.SegmentMaker._style_phantom_measures(8):PHANTOM
                                    R1 * 1/4                                                         %! baca.SegmentMaker._make_multimeasure_rest_container(5):PHANTOM:REST_VOICE:MULTIMEASURE_REST
                            %@% ^ \baca-duration-multiplier-markup #"1" #"4"                         %! baca.SegmentMaker._label_duration_multipliers():DURATION_MULTIPLIER:MULTIMEASURE_REST:PHANTOM:REST_VOICE:baca.SegmentMaker._style_phantom_measures(5)
            <BLANKLINE>
                                }                                                                    %! baca.SegmentMaker._make_multimeasure_rest_container(6):PHANTOM
            <BLANKLINE>
                            >>                                                                       %! baca.SegmentMaker._make_multimeasure_rest_container(7):PHANTOM
            <BLANKLINE>
                        }                                                                            %! baca.SingleStaffScoreTemplate.__call__()
            <BLANKLINE>
                    }                                                                                %! baca.SingleStaffScoreTemplate.__call__()
            <BLANKLINE>
                >>                                                                                   %! baca.SingleStaffScoreTemplate.__call__()
            <BLANKLINE>
            >>                                                                                       %! baca.SingleStaffScoreTemplate.__call__()

        >>> tags_ = abjad.tags.margin_markup_color_tags()
        >>> match = lambda tags: bool(set(tags) & set(tags_))
        >>> text, count = abjad.activate(text, match)
        >>> lines = [_.strip('\n') for _ in text.split('\n')]
        >>> lilypond_file.score_block.items[:] = lines
        >>> abjad.show(lilypond_file, strict=89) # doctest: +SKIP

        ..  docs::

            >>> print(text)
            <BLANKLINE>
            \context Score = "Score"                                                                 %! baca.SingleStaffScoreTemplate.__call__()
            <<                                                                                       %! baca.SingleStaffScoreTemplate.__call__()
            <BLANKLINE>
                \context GlobalContext = "Global_Context"                                            %! abjad.ScoreTemplate._make_global_context()
                <<                                                                                   %! abjad.ScoreTemplate._make_global_context()
            <BLANKLINE>
                    \context GlobalSkips = "Global_Skips"                                            %! abjad.ScoreTemplate._make_global_context()
                    {                                                                                %! abjad.ScoreTemplate._make_global_context()
            <BLANKLINE>
                        % [Global_Skips measure 1]                                                   %! baca.SegmentMaker._comment_measure_numbers()
                        \baca-new-spacing-section #1 #24                                             %! SPACING_COMMAND:baca.HorizontalSpacingSpecifier.__call__(1)
                        \autoPageBreaksOff                                                           %! BREAK:baca.BreakMeasureMap.__call__(1)
                        \noBreak                                                                     %! BREAK:baca.BreakMeasureMap.__call__(2)
                        \baca-lbsd #0 #'(11)                                                         %! BREAK:baca.IndicatorCommand._call()
                        \time 3/8                                                                    %! baca.SegmentMaker._make_global_skips(2):baca.SegmentMaker._set_status_tag():EXPLICIT_TIME_SIGNATURE
                        \bar ""                                                                      %! EMPTY_START_BAR:+SEGMENT:baca.SegmentMaker._make_global_skips(4)
                        \baca-time-signature-color #'blue                                            %! baca.SegmentMaker._attach_color_literal(2):EXPLICIT_TIME_SIGNATURE_COLOR
                        \pageBreak                                                                   %! BREAK:baca.IndicatorCommand._call()
                        s1 * 3/8                                                                     %! baca.SegmentMaker._make_global_skips(1)
            <BLANKLINE>
                        % [Global_Skips measure 2]                                                   %! baca.SegmentMaker._comment_measure_numbers()
                        \baca-new-spacing-section #1 #24                                             %! SPACING_COMMAND:baca.HorizontalSpacingSpecifier.__call__(1)
                        \noBreak                                                                     %! BREAK:baca.BreakMeasureMap.__call__(2)
                        \baca-lbsd #15 #'(11)                                                        %! BREAK:baca.IndicatorCommand._call()
                        \break                                                                       %! BREAK:baca.IndicatorCommand._call()
                        s1 * 3/8                                                                     %! baca.SegmentMaker._make_global_skips(1)
            <BLANKLINE>
                        % [Global_Skips measure 3]                                                   %! baca.SegmentMaker._comment_measure_numbers():baca.SegmentMaker._style_phantom_measures(1):PHANTOM
                        \baca-new-spacing-section #1 #4                                              %! SPACING_COMMAND:baca.HorizontalSpacingSpecifier.__call__(1):baca.SegmentMaker._style_phantom_measures(1):PHANTOM
                        \noBreak                                                                     %! BREAK:baca.BreakMeasureMap.__call__(2):baca.SegmentMaker._style_phantom_measures(1):PHANTOM
                        \time 1/4                                                                    %! baca.SegmentMaker._make_global_skips(3):PHANTOM:baca.SegmentMaker._set_status_tag():EXPLICIT_TIME_SIGNATURE:baca.SegmentMaker._style_phantom_measures(1)
                        \baca-time-signature-transparent                                             %! baca.SegmentMaker._style_phantom_measures(2):PHANTOM
                        s1 * 1/4                                                                     %! baca.SegmentMaker._make_global_skips(3):PHANTOM
                        \once \override Score.BarLine.transparent = ##t                              %! baca.SegmentMaker._style_phantom_measures(3):PHANTOM
                        \once \override Score.SpanBar.transparent = ##t                              %! baca.SegmentMaker._style_phantom_measures(3):PHANTOM
            <BLANKLINE>
                    }                                                                                %! abjad.ScoreTemplate._make_global_context()
            <BLANKLINE>
                >>                                                                                   %! abjad.ScoreTemplate._make_global_context()
            <BLANKLINE>
                \context MusicContext = "Music_Context"                                              %! baca.SingleStaffScoreTemplate.__call__()
                <<                                                                                   %! baca.SingleStaffScoreTemplate.__call__()
            <BLANKLINE>
                    \context Staff = "Music_Staff"                                                   %! baca.SingleStaffScoreTemplate.__call__()
                    {                                                                                %! baca.SingleStaffScoreTemplate.__call__()
            <BLANKLINE>
                        \context Voice = "Music_Voice"                                               %! baca.SingleStaffScoreTemplate.__call__()
                        {                                                                            %! baca.SingleStaffScoreTemplate.__call__()
            <BLANKLINE>
                            % [Music_Voice measure 1]                                                %! baca.SegmentMaker._comment_measure_numbers()
                            \set Staff.shortInstrumentName =                                         %! baca.SegmentMaker._reapply_persistent_indicators(3):-PARTS:baca.SegmentMaker._set_status_tag():REAPPLIED_MARGIN_MARKUP
                            \markup { I+II }                                                         %! baca.SegmentMaker._reapply_persistent_indicators(3):-PARTS:baca.SegmentMaker._set_status_tag():REAPPLIED_MARGIN_MARKUP
                            \set Staff.instrumentName =                                              %! baca.SegmentMaker._clone_segment_initial_short_instrument_name()
                            \markup { I+II }                                                         %! baca.SegmentMaker._clone_segment_initial_short_instrument_name()
                            \once \override Staff.InstrumentName.color = #(x11-color 'green4)        %! baca.SegmentMaker._attach_color_literal(2):REAPPLIED_MARGIN_MARKUP_COLOR
                    %@% \baca-not-yet-pitched-coloring                                               %! baca.SegmentMaker._color_not_yet_pitched():NOT_YET_PITCHED_COLORING
                            b'4.                                                                     %! baca.make_notes()
                            ^ \baca-reapplied-indicator-markup "[“I+II”]"                            %! REAPPLIED_MARGIN_MARKUP_ALERT:baca.SegmentMaker._attach_latent_indicator_alert()
                            \override Staff.InstrumentName.color = #(x11-color 'OliveDrab)           %! baca.SegmentMaker._attach_color_literal(2):REDRAWN_REAPPLIED_MARGIN_MARKUP_COLOR
                            \set Staff.shortInstrumentName =                                         %! baca.SegmentMaker._reapply_persistent_indicators(3):-PARTS:baca.SegmentMaker._treat_persistent_wrapper(3):baca.SegmentMaker._set_status_tag():REDRAWN_REAPPLIED_MARGIN_MARKUP
                            \markup { I+II }                                                         %! baca.SegmentMaker._reapply_persistent_indicators(3):-PARTS:baca.SegmentMaker._treat_persistent_wrapper(3):baca.SegmentMaker._set_status_tag():REDRAWN_REAPPLIED_MARGIN_MARKUP
            <BLANKLINE>
                            % [Music_Voice measure 2]                                                %! baca.SegmentMaker._comment_measure_numbers()
                    %@% \baca-not-yet-pitched-coloring                                               %! baca.SegmentMaker._color_not_yet_pitched():NOT_YET_PITCHED_COLORING
                            b'4.                                                                     %! baca.make_notes()
            <BLANKLINE>
                            <<                                                                       %! baca.SegmentMaker._make_multimeasure_rest_container(7):PHANTOM
            <BLANKLINE>
                                \context Voice = "Music_Voice"                                       %! baca.SegmentMaker._make_multimeasure_rest_container(4):PHANTOM
                                {                                                                    %! baca.SegmentMaker._make_multimeasure_rest_container(4):PHANTOM
            <BLANKLINE>
                                    % [Music_Voice measure 3]                                        %! baca.SegmentMaker._comment_measure_numbers():baca.SegmentMaker._style_phantom_measures(5):PHANTOM
                                    \abjad-invisible-music-coloring                                  %! baca.SegmentMaker._make_multimeasure_rest_container(2):PHANTOM:NOTE:INVISIBLE_MUSIC_COLORING:baca.SegmentMaker._style_phantom_measures(5)
                            %@% \abjad-invisible-music                                               %! baca.SegmentMaker._make_multimeasure_rest_container(3):PHANTOM:NOTE:INVISIBLE_MUSIC_COMMAND:baca.SegmentMaker._style_phantom_measures(5)
                            %@% \baca-not-yet-pitched-coloring                                       %! baca.SegmentMaker._color_not_yet_pitched():NOT_YET_PITCHED_COLORING:HIDDEN:NOTE:baca.SegmentMaker._style_phantom_measures(5):PHANTOM
                                    b'1 * 1/4                                                        %! baca.SegmentMaker._make_multimeasure_rest_container(1):PHANTOM:HIDDEN:NOTE
                            %@% ^ \baca-duration-multiplier-markup #"1" #"4"                         %! baca.SegmentMaker._label_duration_multipliers():DURATION_MULTIPLIER:HIDDEN:NOTE:PHANTOM:baca.SegmentMaker._style_phantom_measures(5)
            <BLANKLINE>
                                }                                                                    %! baca.SegmentMaker._make_multimeasure_rest_container(4):PHANTOM
            <BLANKLINE>
                                \context Voice = "Rest_Voice"                                        %! baca.SegmentMaker._make_multimeasure_rest_container(6):PHANTOM
                                {                                                                    %! baca.SegmentMaker._make_multimeasure_rest_container(6):PHANTOM
            <BLANKLINE>
                                    % [Rest_Voice measure 3]                                         %! baca.SegmentMaker._comment_measure_numbers():baca.SegmentMaker._style_phantom_measures(5):PHANTOM
                                    \once \override Score.TimeSignature.X-extent = ##f               %! baca.SegmentMaker._style_phantom_measures(6):PHANTOM
                                    \once \override MultiMeasureRest.transparent = ##t               %! baca.SegmentMaker._style_phantom_measures(7):PHANTOM
                                    \stopStaff                                                       %! baca.SegmentMaker._style_phantom_measures(8):PHANTOM
                                    \once \override Staff.StaffSymbol.transparent = ##t              %! baca.SegmentMaker._style_phantom_measures(8):PHANTOM
                                    \startStaff                                                      %! baca.SegmentMaker._style_phantom_measures(8):PHANTOM
                                    R1 * 1/4                                                         %! baca.SegmentMaker._make_multimeasure_rest_container(5):PHANTOM:REST_VOICE:MULTIMEASURE_REST
                            %@% ^ \baca-duration-multiplier-markup #"1" #"4"                         %! baca.SegmentMaker._label_duration_multipliers():DURATION_MULTIPLIER:MULTIMEASURE_REST:PHANTOM:REST_VOICE:baca.SegmentMaker._style_phantom_measures(5)
            <BLANKLINE>
                                }                                                                    %! baca.SegmentMaker._make_multimeasure_rest_container(6):PHANTOM
            <BLANKLINE>
                            >>                                                                       %! baca.SegmentMaker._make_multimeasure_rest_container(7):PHANTOM
            <BLANKLINE>
                        }                                                                            %! baca.SingleStaffScoreTemplate.__call__()
            <BLANKLINE>
                    }                                                                                %! baca.SingleStaffScoreTemplate.__call__()
            <BLANKLINE>
                >>                                                                                   %! baca.SingleStaffScoreTemplate.__call__()
            <BLANKLINE>
            >>                                                                                       %! baca.SingleStaffScoreTemplate.__call__()

    ..  container:: example

        Redundant margin markup color pink and redraw dull pink:

        >>> breaks = baca.breaks(
        ...     baca.page(
        ...         [1, 0, (11,)],
        ...         [3, 15, (11,)],
        ...         ),
        ...     )
        >>> maker = baca.SegmentMaker(
        ...     breaks=breaks,
        ...     deactivate=[abjad.tags.NOT_YET_PITCHED_COLORING],
        ...     margin_markups=margin_markups,
        ...     score_template=baca.SingleStaffScoreTemplate(),
        ...     spacing=baca.minimum_duration((1, 24)),
        ...     time_signatures=[(4, 8), (4, 8), (4, 8)],
        ...     )
        >>> maker(
        ...     'Music_Voice',
        ...     baca.margin_markup(margin_markups['I+II']),
        ...     baca.new(
        ...         baca.margin_markup(margin_markups['I+II']),
        ...         map=baca.leaves()[1],
        ...         ),
        ...     baca.make_notes(),
        ...     )

        >>> lilypond_file = maker.run(environment='docs')
        >>> block = abjad.Block(name='layout')
        >>> block.indent = 0
        >>> lilypond_file.items.insert(0, block)
        >>> abjad.show(lilypond_file, strict=89) # doctest: +SKIP

        ..  docs::

            >>> abjad.f(lilypond_file[abjad.Score], strict=89)
            <BLANKLINE>
            \context Score = "Score"                                                                 %! baca.SingleStaffScoreTemplate.__call__()
            <<                                                                                       %! baca.SingleStaffScoreTemplate.__call__()
            <BLANKLINE>
                \context GlobalContext = "Global_Context"                                            %! abjad.ScoreTemplate._make_global_context()
                <<                                                                                   %! abjad.ScoreTemplate._make_global_context()
            <BLANKLINE>
                    \context GlobalSkips = "Global_Skips"                                            %! abjad.ScoreTemplate._make_global_context()
                    {                                                                                %! abjad.ScoreTemplate._make_global_context()
            <BLANKLINE>
                        % [Global_Skips measure 1]                                                   %! baca.SegmentMaker._comment_measure_numbers()
                        \baca-new-spacing-section #1 #24                                             %! SPACING_COMMAND:baca.HorizontalSpacingSpecifier.__call__(1)
                        \autoPageBreaksOff                                                           %! BREAK:baca.BreakMeasureMap.__call__(1)
                        \noBreak                                                                     %! BREAK:baca.BreakMeasureMap.__call__(2)
                        \baca-lbsd #0 #'(11)                                                         %! BREAK:baca.IndicatorCommand._call()
                        \time 4/8                                                                    %! baca.SegmentMaker._make_global_skips(2):baca.SegmentMaker._set_status_tag():EXPLICIT_TIME_SIGNATURE
                        \baca-time-signature-color #'blue                                            %! baca.SegmentMaker._attach_color_literal(2):EXPLICIT_TIME_SIGNATURE_COLOR
                        \pageBreak                                                                   %! BREAK:baca.IndicatorCommand._call()
                        s1 * 1/2                                                                     %! baca.SegmentMaker._make_global_skips(1)
            <BLANKLINE>
                        % [Global_Skips measure 2]                                                   %! baca.SegmentMaker._comment_measure_numbers()
                        \baca-new-spacing-section #1 #24                                             %! SPACING_COMMAND:baca.HorizontalSpacingSpecifier.__call__(1)
                        \noBreak                                                                     %! BREAK:baca.BreakMeasureMap.__call__(2)
                        s1 * 1/2                                                                     %! baca.SegmentMaker._make_global_skips(1)
            <BLANKLINE>
                        % [Global_Skips measure 3]                                                   %! baca.SegmentMaker._comment_measure_numbers()
                        \baca-new-spacing-section #1 #24                                             %! SPACING_COMMAND:baca.HorizontalSpacingSpecifier.__call__(1)
                        \noBreak                                                                     %! BREAK:baca.BreakMeasureMap.__call__(2)
                        \baca-lbsd #15 #'(11)                                                        %! BREAK:baca.IndicatorCommand._call()
                        \break                                                                       %! BREAK:baca.IndicatorCommand._call()
                        s1 * 1/2                                                                     %! baca.SegmentMaker._make_global_skips(1)
            <BLANKLINE>
                        % [Global_Skips measure 4]                                                   %! baca.SegmentMaker._comment_measure_numbers():baca.SegmentMaker._style_phantom_measures(1):PHANTOM
                        \baca-new-spacing-section #1 #4                                              %! SPACING_COMMAND:baca.HorizontalSpacingSpecifier.__call__(1):baca.SegmentMaker._style_phantom_measures(1):PHANTOM
                        \noBreak                                                                     %! BREAK:baca.BreakMeasureMap.__call__(2):baca.SegmentMaker._style_phantom_measures(1):PHANTOM
                        \time 1/4                                                                    %! baca.SegmentMaker._make_global_skips(3):PHANTOM:baca.SegmentMaker._set_status_tag():EXPLICIT_TIME_SIGNATURE:baca.SegmentMaker._style_phantom_measures(1)
                        \baca-time-signature-transparent                                             %! baca.SegmentMaker._style_phantom_measures(2):PHANTOM
                        s1 * 1/4                                                                     %! baca.SegmentMaker._make_global_skips(3):PHANTOM
                        \once \override Score.BarLine.transparent = ##t                              %! baca.SegmentMaker._style_phantom_measures(3):PHANTOM
                        \once \override Score.SpanBar.transparent = ##t                              %! baca.SegmentMaker._style_phantom_measures(3):PHANTOM
            <BLANKLINE>
                    }                                                                                %! abjad.ScoreTemplate._make_global_context()
            <BLANKLINE>
                >>                                                                                   %! abjad.ScoreTemplate._make_global_context()
            <BLANKLINE>
                \context MusicContext = "Music_Context"                                              %! baca.SingleStaffScoreTemplate.__call__()
                <<                                                                                   %! baca.SingleStaffScoreTemplate.__call__()
            <BLANKLINE>
                    \context Staff = "Music_Staff"                                                   %! baca.SingleStaffScoreTemplate.__call__()
                    {                                                                                %! baca.SingleStaffScoreTemplate.__call__()
            <BLANKLINE>
                        \context Voice = "Music_Voice"                                               %! baca.SingleStaffScoreTemplate.__call__()
                        {                                                                            %! baca.SingleStaffScoreTemplate.__call__()
            <BLANKLINE>
                            % [Music_Voice measure 1]                                                %! baca.SegmentMaker._comment_measure_numbers()
                            \set Staff.shortInstrumentName =                                         %! baca.margin_markup():baca.IndicatorCommand._call():baca.SegmentMaker._set_status_tag():EXPLICIT_MARGIN_MARKUP
                            \markup { I+II }                                                         %! baca.margin_markup():baca.IndicatorCommand._call():baca.SegmentMaker._set_status_tag():EXPLICIT_MARGIN_MARKUP
                            \once \override Staff.InstrumentName.color = #(x11-color 'blue)          %! baca.SegmentMaker._attach_color_literal(2):EXPLICIT_MARGIN_MARKUP_COLOR
                        %@% \baca-not-yet-pitched-coloring                                           %! baca.SegmentMaker._color_not_yet_pitched():NOT_YET_PITCHED_COLORING
                            b'2                                                                      %! baca.make_notes()
                            ^ \baca-explicit-indicator-markup "[“I+II”]"                             %! EXPLICIT_MARGIN_MARKUP_ALERT:baca.SegmentMaker._attach_latent_indicator_alert()
                            \override Staff.InstrumentName.color = #(x11-color 'DeepSkyBlue2)        %! baca.SegmentMaker._attach_color_literal(2):REDRAWN_EXPLICIT_MARGIN_MARKUP_COLOR
                            \set Staff.shortInstrumentName =                                         %! baca.margin_markup():baca.IndicatorCommand._call():baca.SegmentMaker._treat_persistent_wrapper(3):baca.SegmentMaker._set_status_tag():REDRAWN_EXPLICIT_MARGIN_MARKUP
                            \markup { I+II }                                                         %! baca.margin_markup():baca.IndicatorCommand._call():baca.SegmentMaker._treat_persistent_wrapper(3):baca.SegmentMaker._set_status_tag():REDRAWN_EXPLICIT_MARGIN_MARKUP
            <BLANKLINE>
                            % [Music_Voice measure 2]                                                %! baca.SegmentMaker._comment_measure_numbers()
                            \set Staff.shortInstrumentName =                                         %! baca.margin_markup():baca.IndicatorCommand._call():baca.SegmentMaker._set_status_tag():REDUNDANT_MARGIN_MARKUP
                            \markup { I+II }                                                         %! baca.margin_markup():baca.IndicatorCommand._call():baca.SegmentMaker._set_status_tag():REDUNDANT_MARGIN_MARKUP
                            \once \override Staff.InstrumentName.color = #(x11-color 'DeepPink1)     %! baca.SegmentMaker._attach_color_literal(2):REDUNDANT_MARGIN_MARKUP_COLOR
                        %@% \baca-not-yet-pitched-coloring                                           %! baca.SegmentMaker._color_not_yet_pitched():NOT_YET_PITCHED_COLORING
                            b'2                                                                      %! baca.make_notes()
                            ^ \baca-redundant-indicator-markup "[“I+II”]"                            %! REDUNDANT_MARGIN_MARKUP_ALERT:baca.SegmentMaker._attach_latent_indicator_alert()
                            \override Staff.InstrumentName.color = #(x11-color 'DeepPink4)           %! baca.SegmentMaker._attach_color_literal(2):REDRAWN_REDUNDANT_MARGIN_MARKUP_COLOR
                            \set Staff.shortInstrumentName =                                         %! baca.margin_markup():baca.IndicatorCommand._call():baca.SegmentMaker._treat_persistent_wrapper(3):baca.SegmentMaker._set_status_tag():REDRAWN_REDUNDANT_MARGIN_MARKUP
                            \markup { I+II }                                                         %! baca.margin_markup():baca.IndicatorCommand._call():baca.SegmentMaker._treat_persistent_wrapper(3):baca.SegmentMaker._set_status_tag():REDRAWN_REDUNDANT_MARGIN_MARKUP
            <BLANKLINE>
                            % [Music_Voice measure 3]                                                %! baca.SegmentMaker._comment_measure_numbers()
                        %@% \baca-not-yet-pitched-coloring                                           %! baca.SegmentMaker._color_not_yet_pitched():NOT_YET_PITCHED_COLORING
                            b'2                                                                      %! baca.make_notes()
            <BLANKLINE>
                            <<                                                                       %! baca.SegmentMaker._make_multimeasure_rest_container(7):PHANTOM
            <BLANKLINE>
                                \context Voice = "Music_Voice"                                       %! baca.SegmentMaker._make_multimeasure_rest_container(4):PHANTOM
                                {                                                                    %! baca.SegmentMaker._make_multimeasure_rest_container(4):PHANTOM
            <BLANKLINE>
                                    % [Music_Voice measure 4]                                        %! baca.SegmentMaker._comment_measure_numbers():baca.SegmentMaker._style_phantom_measures(5):PHANTOM
                                    \abjad-invisible-music-coloring                                  %! baca.SegmentMaker._make_multimeasure_rest_container(2):PHANTOM:NOTE:INVISIBLE_MUSIC_COLORING:baca.SegmentMaker._style_phantom_measures(5)
                                %@% \abjad-invisible-music                                           %! baca.SegmentMaker._make_multimeasure_rest_container(3):PHANTOM:NOTE:INVISIBLE_MUSIC_COMMAND:baca.SegmentMaker._style_phantom_measures(5)
                                %@% \baca-not-yet-pitched-coloring                                   %! baca.SegmentMaker._color_not_yet_pitched():NOT_YET_PITCHED_COLORING:HIDDEN:NOTE:baca.SegmentMaker._style_phantom_measures(5):PHANTOM
                                    b'1 * 1/4                                                        %! baca.SegmentMaker._make_multimeasure_rest_container(1):PHANTOM:HIDDEN:NOTE
                                %@% ^ \baca-duration-multiplier-markup #"1" #"4"                     %! baca.SegmentMaker._label_duration_multipliers():DURATION_MULTIPLIER:HIDDEN:NOTE:PHANTOM:baca.SegmentMaker._style_phantom_measures(5)
            <BLANKLINE>
                                }                                                                    %! baca.SegmentMaker._make_multimeasure_rest_container(4):PHANTOM
            <BLANKLINE>
                                \context Voice = "Rest_Voice"                                        %! baca.SegmentMaker._make_multimeasure_rest_container(6):PHANTOM
                                {                                                                    %! baca.SegmentMaker._make_multimeasure_rest_container(6):PHANTOM
            <BLANKLINE>
                                    % [Rest_Voice measure 4]                                         %! baca.SegmentMaker._comment_measure_numbers():baca.SegmentMaker._style_phantom_measures(5):PHANTOM
                                    \once \override Score.TimeSignature.X-extent = ##f               %! baca.SegmentMaker._style_phantom_measures(6):PHANTOM
                                    \once \override MultiMeasureRest.transparent = ##t               %! baca.SegmentMaker._style_phantom_measures(7):PHANTOM
                                    \stopStaff                                                       %! baca.SegmentMaker._style_phantom_measures(8):PHANTOM
                                    \once \override Staff.StaffSymbol.transparent = ##t              %! baca.SegmentMaker._style_phantom_measures(8):PHANTOM
                                    \startStaff                                                      %! baca.SegmentMaker._style_phantom_measures(8):PHANTOM
                                    R1 * 1/4                                                         %! baca.SegmentMaker._make_multimeasure_rest_container(5):PHANTOM:REST_VOICE:MULTIMEASURE_REST
                                %@% ^ \baca-duration-multiplier-markup #"1" #"4"                     %! baca.SegmentMaker._label_duration_multipliers():DURATION_MULTIPLIER:MULTIMEASURE_REST:PHANTOM:REST_VOICE:baca.SegmentMaker._style_phantom_measures(5)
            <BLANKLINE>
                                }                                                                    %! baca.SegmentMaker._make_multimeasure_rest_container(6):PHANTOM
            <BLANKLINE>
                            >>                                                                       %! baca.SegmentMaker._make_multimeasure_rest_container(7):PHANTOM
            <BLANKLINE>
                        }                                                                            %! baca.SingleStaffScoreTemplate.__call__()
            <BLANKLINE>
                    }                                                                                %! baca.SingleStaffScoreTemplate.__call__()
            <BLANKLINE>
                >>                                                                                   %! baca.SingleStaffScoreTemplate.__call__()
            <BLANKLINE>
            >>                                                                                       %! baca.SingleStaffScoreTemplate.__call__()

        >>> score = lilypond_file[abjad.Score]
        >>> text = format(score, 'lilypond')
        >>> text = abjad.LilyPondFormatManager.left_shift_tags(text)
        >>> tags_ = abjad.tags.margin_markup_color_tags()
        >>> match = lambda tags: bool(set(tags) & set(tags_))
        >>> text, count = abjad.deactivate(text, match)
        >>> text = abjad.LilyPondFormatManager.left_shift_tags(text, 89)
        >>> lines = [_.strip('\n') for _ in text.split('\n')]
        >>> lilypond_file.score_block.items[:] = lines
        >>> abjad.show(lilypond_file, strict=89) # doctest: +SKIP

        ..  docs::

            >>> print(text)
            <BLANKLINE>
            \context Score = "Score"                                                                 %! baca.SingleStaffScoreTemplate.__call__()
            <<                                                                                       %! baca.SingleStaffScoreTemplate.__call__()
            <BLANKLINE>
                \context GlobalContext = "Global_Context"                                            %! abjad.ScoreTemplate._make_global_context()
                <<                                                                                   %! abjad.ScoreTemplate._make_global_context()
            <BLANKLINE>
                    \context GlobalSkips = "Global_Skips"                                            %! abjad.ScoreTemplate._make_global_context()
                    {                                                                                %! abjad.ScoreTemplate._make_global_context()
            <BLANKLINE>
                        % [Global_Skips measure 1]                                                   %! baca.SegmentMaker._comment_measure_numbers()
                        \baca-new-spacing-section #1 #24                                             %! SPACING_COMMAND:baca.HorizontalSpacingSpecifier.__call__(1)
                        \autoPageBreaksOff                                                           %! BREAK:baca.BreakMeasureMap.__call__(1)
                        \noBreak                                                                     %! BREAK:baca.BreakMeasureMap.__call__(2)
                        \baca-lbsd #0 #'(11)                                                         %! BREAK:baca.IndicatorCommand._call()
                        \time 4/8                                                                    %! baca.SegmentMaker._make_global_skips(2):baca.SegmentMaker._set_status_tag():EXPLICIT_TIME_SIGNATURE
                        \baca-time-signature-color #'blue                                            %! baca.SegmentMaker._attach_color_literal(2):EXPLICIT_TIME_SIGNATURE_COLOR
                        \pageBreak                                                                   %! BREAK:baca.IndicatorCommand._call()
                        s1 * 1/2                                                                     %! baca.SegmentMaker._make_global_skips(1)
            <BLANKLINE>
                        % [Global_Skips measure 2]                                                   %! baca.SegmentMaker._comment_measure_numbers()
                        \baca-new-spacing-section #1 #24                                             %! SPACING_COMMAND:baca.HorizontalSpacingSpecifier.__call__(1)
                        \noBreak                                                                     %! BREAK:baca.BreakMeasureMap.__call__(2)
                        s1 * 1/2                                                                     %! baca.SegmentMaker._make_global_skips(1)
            <BLANKLINE>
                        % [Global_Skips measure 3]                                                   %! baca.SegmentMaker._comment_measure_numbers()
                        \baca-new-spacing-section #1 #24                                             %! SPACING_COMMAND:baca.HorizontalSpacingSpecifier.__call__(1)
                        \noBreak                                                                     %! BREAK:baca.BreakMeasureMap.__call__(2)
                        \baca-lbsd #15 #'(11)                                                        %! BREAK:baca.IndicatorCommand._call()
                        \break                                                                       %! BREAK:baca.IndicatorCommand._call()
                        s1 * 1/2                                                                     %! baca.SegmentMaker._make_global_skips(1)
            <BLANKLINE>
                        % [Global_Skips measure 4]                                                   %! baca.SegmentMaker._comment_measure_numbers():baca.SegmentMaker._style_phantom_measures(1):PHANTOM
                        \baca-new-spacing-section #1 #4                                              %! SPACING_COMMAND:baca.HorizontalSpacingSpecifier.__call__(1):baca.SegmentMaker._style_phantom_measures(1):PHANTOM
                        \noBreak                                                                     %! BREAK:baca.BreakMeasureMap.__call__(2):baca.SegmentMaker._style_phantom_measures(1):PHANTOM
                        \time 1/4                                                                    %! baca.SegmentMaker._make_global_skips(3):PHANTOM:baca.SegmentMaker._set_status_tag():EXPLICIT_TIME_SIGNATURE:baca.SegmentMaker._style_phantom_measures(1)
                        \baca-time-signature-transparent                                             %! baca.SegmentMaker._style_phantom_measures(2):PHANTOM
                        s1 * 1/4                                                                     %! baca.SegmentMaker._make_global_skips(3):PHANTOM
                        \once \override Score.BarLine.transparent = ##t                              %! baca.SegmentMaker._style_phantom_measures(3):PHANTOM
                        \once \override Score.SpanBar.transparent = ##t                              %! baca.SegmentMaker._style_phantom_measures(3):PHANTOM
            <BLANKLINE>
                    }                                                                                %! abjad.ScoreTemplate._make_global_context()
            <BLANKLINE>
                >>                                                                                   %! abjad.ScoreTemplate._make_global_context()
            <BLANKLINE>
                \context MusicContext = "Music_Context"                                              %! baca.SingleStaffScoreTemplate.__call__()
                <<                                                                                   %! baca.SingleStaffScoreTemplate.__call__()
            <BLANKLINE>
                    \context Staff = "Music_Staff"                                                   %! baca.SingleStaffScoreTemplate.__call__()
                    {                                                                                %! baca.SingleStaffScoreTemplate.__call__()
            <BLANKLINE>
                        \context Voice = "Music_Voice"                                               %! baca.SingleStaffScoreTemplate.__call__()
                        {                                                                            %! baca.SingleStaffScoreTemplate.__call__()
            <BLANKLINE>
                            % [Music_Voice measure 1]                                                %! baca.SegmentMaker._comment_measure_numbers()
                            \set Staff.shortInstrumentName =                                         %! baca.margin_markup():baca.IndicatorCommand._call():baca.SegmentMaker._set_status_tag():EXPLICIT_MARGIN_MARKUP
                            \markup { I+II }                                                         %! baca.margin_markup():baca.IndicatorCommand._call():baca.SegmentMaker._set_status_tag():EXPLICIT_MARGIN_MARKUP
                        %%% \once \override Staff.InstrumentName.color = #(x11-color 'blue)          %! baca.SegmentMaker._attach_color_literal(2):EXPLICIT_MARGIN_MARKUP_COLOR
                    %@% \baca-not-yet-pitched-coloring                                               %! baca.SegmentMaker._color_not_yet_pitched():NOT_YET_PITCHED_COLORING
                            b'2                                                                      %! baca.make_notes()
                        %%% ^ \baca-explicit-indicator-markup "[“I+II”]"                             %! EXPLICIT_MARGIN_MARKUP_ALERT:baca.SegmentMaker._attach_latent_indicator_alert()
                        %%% \override Staff.InstrumentName.color = #(x11-color 'DeepSkyBlue2)        %! baca.SegmentMaker._attach_color_literal(2):REDRAWN_EXPLICIT_MARGIN_MARKUP_COLOR
                            \set Staff.shortInstrumentName =                                         %! baca.margin_markup():baca.IndicatorCommand._call():baca.SegmentMaker._treat_persistent_wrapper(3):baca.SegmentMaker._set_status_tag():REDRAWN_EXPLICIT_MARGIN_MARKUP
                            \markup { I+II }                                                         %! baca.margin_markup():baca.IndicatorCommand._call():baca.SegmentMaker._treat_persistent_wrapper(3):baca.SegmentMaker._set_status_tag():REDRAWN_EXPLICIT_MARGIN_MARKUP
            <BLANKLINE>
                            % [Music_Voice measure 2]                                                %! baca.SegmentMaker._comment_measure_numbers()
                            \set Staff.shortInstrumentName =                                         %! baca.margin_markup():baca.IndicatorCommand._call():baca.SegmentMaker._set_status_tag():REDUNDANT_MARGIN_MARKUP
                            \markup { I+II }                                                         %! baca.margin_markup():baca.IndicatorCommand._call():baca.SegmentMaker._set_status_tag():REDUNDANT_MARGIN_MARKUP
                        %%% \once \override Staff.InstrumentName.color = #(x11-color 'DeepPink1)     %! baca.SegmentMaker._attach_color_literal(2):REDUNDANT_MARGIN_MARKUP_COLOR
                    %@% \baca-not-yet-pitched-coloring                                               %! baca.SegmentMaker._color_not_yet_pitched():NOT_YET_PITCHED_COLORING
                            b'2                                                                      %! baca.make_notes()
                        %%% ^ \baca-redundant-indicator-markup "[“I+II”]"                            %! REDUNDANT_MARGIN_MARKUP_ALERT:baca.SegmentMaker._attach_latent_indicator_alert()
                        %%% \override Staff.InstrumentName.color = #(x11-color 'DeepPink4)           %! baca.SegmentMaker._attach_color_literal(2):REDRAWN_REDUNDANT_MARGIN_MARKUP_COLOR
                            \set Staff.shortInstrumentName =                                         %! baca.margin_markup():baca.IndicatorCommand._call():baca.SegmentMaker._treat_persistent_wrapper(3):baca.SegmentMaker._set_status_tag():REDRAWN_REDUNDANT_MARGIN_MARKUP
                            \markup { I+II }                                                         %! baca.margin_markup():baca.IndicatorCommand._call():baca.SegmentMaker._treat_persistent_wrapper(3):baca.SegmentMaker._set_status_tag():REDRAWN_REDUNDANT_MARGIN_MARKUP
            <BLANKLINE>
                            % [Music_Voice measure 3]                                                %! baca.SegmentMaker._comment_measure_numbers()
                    %@% \baca-not-yet-pitched-coloring                                               %! baca.SegmentMaker._color_not_yet_pitched():NOT_YET_PITCHED_COLORING
                            b'2                                                                      %! baca.make_notes()
            <BLANKLINE>
                            <<                                                                       %! baca.SegmentMaker._make_multimeasure_rest_container(7):PHANTOM
            <BLANKLINE>
                                \context Voice = "Music_Voice"                                       %! baca.SegmentMaker._make_multimeasure_rest_container(4):PHANTOM
                                {                                                                    %! baca.SegmentMaker._make_multimeasure_rest_container(4):PHANTOM
            <BLANKLINE>
                                    % [Music_Voice measure 4]                                        %! baca.SegmentMaker._comment_measure_numbers():baca.SegmentMaker._style_phantom_measures(5):PHANTOM
                                    \abjad-invisible-music-coloring                                  %! baca.SegmentMaker._make_multimeasure_rest_container(2):PHANTOM:NOTE:INVISIBLE_MUSIC_COLORING:baca.SegmentMaker._style_phantom_measures(5)
                            %@% \abjad-invisible-music                                               %! baca.SegmentMaker._make_multimeasure_rest_container(3):PHANTOM:NOTE:INVISIBLE_MUSIC_COMMAND:baca.SegmentMaker._style_phantom_measures(5)
                            %@% \baca-not-yet-pitched-coloring                                       %! baca.SegmentMaker._color_not_yet_pitched():NOT_YET_PITCHED_COLORING:HIDDEN:NOTE:baca.SegmentMaker._style_phantom_measures(5):PHANTOM
                                    b'1 * 1/4                                                        %! baca.SegmentMaker._make_multimeasure_rest_container(1):PHANTOM:HIDDEN:NOTE
                            %@% ^ \baca-duration-multiplier-markup #"1" #"4"                         %! baca.SegmentMaker._label_duration_multipliers():DURATION_MULTIPLIER:HIDDEN:NOTE:PHANTOM:baca.SegmentMaker._style_phantom_measures(5)
            <BLANKLINE>
                                }                                                                    %! baca.SegmentMaker._make_multimeasure_rest_container(4):PHANTOM
            <BLANKLINE>
                                \context Voice = "Rest_Voice"                                        %! baca.SegmentMaker._make_multimeasure_rest_container(6):PHANTOM
                                {                                                                    %! baca.SegmentMaker._make_multimeasure_rest_container(6):PHANTOM
            <BLANKLINE>
                                    % [Rest_Voice measure 4]                                         %! baca.SegmentMaker._comment_measure_numbers():baca.SegmentMaker._style_phantom_measures(5):PHANTOM
                                    \once \override Score.TimeSignature.X-extent = ##f               %! baca.SegmentMaker._style_phantom_measures(6):PHANTOM
                                    \once \override MultiMeasureRest.transparent = ##t               %! baca.SegmentMaker._style_phantom_measures(7):PHANTOM
                                    \stopStaff                                                       %! baca.SegmentMaker._style_phantom_measures(8):PHANTOM
                                    \once \override Staff.StaffSymbol.transparent = ##t              %! baca.SegmentMaker._style_phantom_measures(8):PHANTOM
                                    \startStaff                                                      %! baca.SegmentMaker._style_phantom_measures(8):PHANTOM
                                    R1 * 1/4                                                         %! baca.SegmentMaker._make_multimeasure_rest_container(5):PHANTOM:REST_VOICE:MULTIMEASURE_REST
                            %@% ^ \baca-duration-multiplier-markup #"1" #"4"                         %! baca.SegmentMaker._label_duration_multipliers():DURATION_MULTIPLIER:MULTIMEASURE_REST:PHANTOM:REST_VOICE:baca.SegmentMaker._style_phantom_measures(5)
            <BLANKLINE>
                                }                                                                    %! baca.SegmentMaker._make_multimeasure_rest_container(6):PHANTOM
            <BLANKLINE>
                            >>                                                                       %! baca.SegmentMaker._make_multimeasure_rest_container(7):PHANTOM
            <BLANKLINE>
                        }                                                                            %! baca.SingleStaffScoreTemplate.__call__()
            <BLANKLINE>
                    }                                                                                %! baca.SingleStaffScoreTemplate.__call__()
            <BLANKLINE>
                >>                                                                                   %! baca.SingleStaffScoreTemplate.__call__()
            <BLANKLINE>
            >>                                                                                       %! baca.SingleStaffScoreTemplate.__call__()

        >>> tags_ = abjad.tags.margin_markup_color_tags()
        >>> match = lambda tags: bool(set(tags) & set(tags_))
        >>> text, count = abjad.activate(text, match)
        >>> lines = [_.strip('\n') for _ in text.split('\n')]
        >>> lilypond_file.score_block.items[:] = lines
        >>> abjad.show(lilypond_file, strict=89) # doctest: +SKIP

        ..  docs::

            >>> print(text)
            <BLANKLINE>
            \context Score = "Score"                                                                 %! baca.SingleStaffScoreTemplate.__call__()
            <<                                                                                       %! baca.SingleStaffScoreTemplate.__call__()
            <BLANKLINE>
                \context GlobalContext = "Global_Context"                                            %! abjad.ScoreTemplate._make_global_context()
                <<                                                                                   %! abjad.ScoreTemplate._make_global_context()
            <BLANKLINE>
                    \context GlobalSkips = "Global_Skips"                                            %! abjad.ScoreTemplate._make_global_context()
                    {                                                                                %! abjad.ScoreTemplate._make_global_context()
            <BLANKLINE>
                        % [Global_Skips measure 1]                                                   %! baca.SegmentMaker._comment_measure_numbers()
                        \baca-new-spacing-section #1 #24                                             %! SPACING_COMMAND:baca.HorizontalSpacingSpecifier.__call__(1)
                        \autoPageBreaksOff                                                           %! BREAK:baca.BreakMeasureMap.__call__(1)
                        \noBreak                                                                     %! BREAK:baca.BreakMeasureMap.__call__(2)
                        \baca-lbsd #0 #'(11)                                                         %! BREAK:baca.IndicatorCommand._call()
                        \time 4/8                                                                    %! baca.SegmentMaker._make_global_skips(2):baca.SegmentMaker._set_status_tag():EXPLICIT_TIME_SIGNATURE
                        \baca-time-signature-color #'blue                                            %! baca.SegmentMaker._attach_color_literal(2):EXPLICIT_TIME_SIGNATURE_COLOR
                        \pageBreak                                                                   %! BREAK:baca.IndicatorCommand._call()
                        s1 * 1/2                                                                     %! baca.SegmentMaker._make_global_skips(1)
            <BLANKLINE>
                        % [Global_Skips measure 2]                                                   %! baca.SegmentMaker._comment_measure_numbers()
                        \baca-new-spacing-section #1 #24                                             %! SPACING_COMMAND:baca.HorizontalSpacingSpecifier.__call__(1)
                        \noBreak                                                                     %! BREAK:baca.BreakMeasureMap.__call__(2)
                        s1 * 1/2                                                                     %! baca.SegmentMaker._make_global_skips(1)
            <BLANKLINE>
                        % [Global_Skips measure 3]                                                   %! baca.SegmentMaker._comment_measure_numbers()
                        \baca-new-spacing-section #1 #24                                             %! SPACING_COMMAND:baca.HorizontalSpacingSpecifier.__call__(1)
                        \noBreak                                                                     %! BREAK:baca.BreakMeasureMap.__call__(2)
                        \baca-lbsd #15 #'(11)                                                        %! BREAK:baca.IndicatorCommand._call()
                        \break                                                                       %! BREAK:baca.IndicatorCommand._call()
                        s1 * 1/2                                                                     %! baca.SegmentMaker._make_global_skips(1)
            <BLANKLINE>
                        % [Global_Skips measure 4]                                                   %! baca.SegmentMaker._comment_measure_numbers():baca.SegmentMaker._style_phantom_measures(1):PHANTOM
                        \baca-new-spacing-section #1 #4                                              %! SPACING_COMMAND:baca.HorizontalSpacingSpecifier.__call__(1):baca.SegmentMaker._style_phantom_measures(1):PHANTOM
                        \noBreak                                                                     %! BREAK:baca.BreakMeasureMap.__call__(2):baca.SegmentMaker._style_phantom_measures(1):PHANTOM
                        \time 1/4                                                                    %! baca.SegmentMaker._make_global_skips(3):PHANTOM:baca.SegmentMaker._set_status_tag():EXPLICIT_TIME_SIGNATURE:baca.SegmentMaker._style_phantom_measures(1)
                        \baca-time-signature-transparent                                             %! baca.SegmentMaker._style_phantom_measures(2):PHANTOM
                        s1 * 1/4                                                                     %! baca.SegmentMaker._make_global_skips(3):PHANTOM
                        \once \override Score.BarLine.transparent = ##t                              %! baca.SegmentMaker._style_phantom_measures(3):PHANTOM
                        \once \override Score.SpanBar.transparent = ##t                              %! baca.SegmentMaker._style_phantom_measures(3):PHANTOM
            <BLANKLINE>
                    }                                                                                %! abjad.ScoreTemplate._make_global_context()
            <BLANKLINE>
                >>                                                                                   %! abjad.ScoreTemplate._make_global_context()
            <BLANKLINE>
                \context MusicContext = "Music_Context"                                              %! baca.SingleStaffScoreTemplate.__call__()
                <<                                                                                   %! baca.SingleStaffScoreTemplate.__call__()
            <BLANKLINE>
                    \context Staff = "Music_Staff"                                                   %! baca.SingleStaffScoreTemplate.__call__()
                    {                                                                                %! baca.SingleStaffScoreTemplate.__call__()
            <BLANKLINE>
                        \context Voice = "Music_Voice"                                               %! baca.SingleStaffScoreTemplate.__call__()
                        {                                                                            %! baca.SingleStaffScoreTemplate.__call__()
            <BLANKLINE>
                            % [Music_Voice measure 1]                                                %! baca.SegmentMaker._comment_measure_numbers()
                            \set Staff.shortInstrumentName =                                         %! baca.margin_markup():baca.IndicatorCommand._call():baca.SegmentMaker._set_status_tag():EXPLICIT_MARGIN_MARKUP
                            \markup { I+II }                                                         %! baca.margin_markup():baca.IndicatorCommand._call():baca.SegmentMaker._set_status_tag():EXPLICIT_MARGIN_MARKUP
                            \once \override Staff.InstrumentName.color = #(x11-color 'blue)          %! baca.SegmentMaker._attach_color_literal(2):EXPLICIT_MARGIN_MARKUP_COLOR
                    %@% \baca-not-yet-pitched-coloring                                               %! baca.SegmentMaker._color_not_yet_pitched():NOT_YET_PITCHED_COLORING
                            b'2                                                                      %! baca.make_notes()
                            ^ \baca-explicit-indicator-markup "[“I+II”]"                             %! EXPLICIT_MARGIN_MARKUP_ALERT:baca.SegmentMaker._attach_latent_indicator_alert()
                            \override Staff.InstrumentName.color = #(x11-color 'DeepSkyBlue2)        %! baca.SegmentMaker._attach_color_literal(2):REDRAWN_EXPLICIT_MARGIN_MARKUP_COLOR
                            \set Staff.shortInstrumentName =                                         %! baca.margin_markup():baca.IndicatorCommand._call():baca.SegmentMaker._treat_persistent_wrapper(3):baca.SegmentMaker._set_status_tag():REDRAWN_EXPLICIT_MARGIN_MARKUP
                            \markup { I+II }                                                         %! baca.margin_markup():baca.IndicatorCommand._call():baca.SegmentMaker._treat_persistent_wrapper(3):baca.SegmentMaker._set_status_tag():REDRAWN_EXPLICIT_MARGIN_MARKUP
            <BLANKLINE>
                            % [Music_Voice measure 2]                                                %! baca.SegmentMaker._comment_measure_numbers()
                            \set Staff.shortInstrumentName =                                         %! baca.margin_markup():baca.IndicatorCommand._call():baca.SegmentMaker._set_status_tag():REDUNDANT_MARGIN_MARKUP
                            \markup { I+II }                                                         %! baca.margin_markup():baca.IndicatorCommand._call():baca.SegmentMaker._set_status_tag():REDUNDANT_MARGIN_MARKUP
                            \once \override Staff.InstrumentName.color = #(x11-color 'DeepPink1)     %! baca.SegmentMaker._attach_color_literal(2):REDUNDANT_MARGIN_MARKUP_COLOR
                    %@% \baca-not-yet-pitched-coloring                                               %! baca.SegmentMaker._color_not_yet_pitched():NOT_YET_PITCHED_COLORING
                            b'2                                                                      %! baca.make_notes()
                            ^ \baca-redundant-indicator-markup "[“I+II”]"                            %! REDUNDANT_MARGIN_MARKUP_ALERT:baca.SegmentMaker._attach_latent_indicator_alert()
                            \override Staff.InstrumentName.color = #(x11-color 'DeepPink4)           %! baca.SegmentMaker._attach_color_literal(2):REDRAWN_REDUNDANT_MARGIN_MARKUP_COLOR
                            \set Staff.shortInstrumentName =                                         %! baca.margin_markup():baca.IndicatorCommand._call():baca.SegmentMaker._treat_persistent_wrapper(3):baca.SegmentMaker._set_status_tag():REDRAWN_REDUNDANT_MARGIN_MARKUP
                            \markup { I+II }                                                         %! baca.margin_markup():baca.IndicatorCommand._call():baca.SegmentMaker._treat_persistent_wrapper(3):baca.SegmentMaker._set_status_tag():REDRAWN_REDUNDANT_MARGIN_MARKUP
            <BLANKLINE>
                            % [Music_Voice measure 3]                                                %! baca.SegmentMaker._comment_measure_numbers()
                    %@% \baca-not-yet-pitched-coloring                                               %! baca.SegmentMaker._color_not_yet_pitched():NOT_YET_PITCHED_COLORING
                            b'2                                                                      %! baca.make_notes()
            <BLANKLINE>
                            <<                                                                       %! baca.SegmentMaker._make_multimeasure_rest_container(7):PHANTOM
            <BLANKLINE>
                                \context Voice = "Music_Voice"                                       %! baca.SegmentMaker._make_multimeasure_rest_container(4):PHANTOM
                                {                                                                    %! baca.SegmentMaker._make_multimeasure_rest_container(4):PHANTOM
            <BLANKLINE>
                                    % [Music_Voice measure 4]                                        %! baca.SegmentMaker._comment_measure_numbers():baca.SegmentMaker._style_phantom_measures(5):PHANTOM
                                    \abjad-invisible-music-coloring                                  %! baca.SegmentMaker._make_multimeasure_rest_container(2):PHANTOM:NOTE:INVISIBLE_MUSIC_COLORING:baca.SegmentMaker._style_phantom_measures(5)
                            %@% \abjad-invisible-music                                               %! baca.SegmentMaker._make_multimeasure_rest_container(3):PHANTOM:NOTE:INVISIBLE_MUSIC_COMMAND:baca.SegmentMaker._style_phantom_measures(5)
                            %@% \baca-not-yet-pitched-coloring                                       %! baca.SegmentMaker._color_not_yet_pitched():NOT_YET_PITCHED_COLORING:HIDDEN:NOTE:baca.SegmentMaker._style_phantom_measures(5):PHANTOM
                                    b'1 * 1/4                                                        %! baca.SegmentMaker._make_multimeasure_rest_container(1):PHANTOM:HIDDEN:NOTE
                            %@% ^ \baca-duration-multiplier-markup #"1" #"4"                         %! baca.SegmentMaker._label_duration_multipliers():DURATION_MULTIPLIER:HIDDEN:NOTE:PHANTOM:baca.SegmentMaker._style_phantom_measures(5)
            <BLANKLINE>
                                }                                                                    %! baca.SegmentMaker._make_multimeasure_rest_container(4):PHANTOM
            <BLANKLINE>
                                \context Voice = "Rest_Voice"                                        %! baca.SegmentMaker._make_multimeasure_rest_container(6):PHANTOM
                                {                                                                    %! baca.SegmentMaker._make_multimeasure_rest_container(6):PHANTOM
            <BLANKLINE>
                                    % [Rest_Voice measure 4]                                         %! baca.SegmentMaker._comment_measure_numbers():baca.SegmentMaker._style_phantom_measures(5):PHANTOM
                                    \once \override Score.TimeSignature.X-extent = ##f               %! baca.SegmentMaker._style_phantom_measures(6):PHANTOM
                                    \once \override MultiMeasureRest.transparent = ##t               %! baca.SegmentMaker._style_phantom_measures(7):PHANTOM
                                    \stopStaff                                                       %! baca.SegmentMaker._style_phantom_measures(8):PHANTOM
                                    \once \override Staff.StaffSymbol.transparent = ##t              %! baca.SegmentMaker._style_phantom_measures(8):PHANTOM
                                    \startStaff                                                      %! baca.SegmentMaker._style_phantom_measures(8):PHANTOM
                                    R1 * 1/4                                                         %! baca.SegmentMaker._make_multimeasure_rest_container(5):PHANTOM:REST_VOICE:MULTIMEASURE_REST
                            %@% ^ \baca-duration-multiplier-markup #"1" #"4"                         %! baca.SegmentMaker._label_duration_multipliers():DURATION_MULTIPLIER:MULTIMEASURE_REST:PHANTOM:REST_VOICE:baca.SegmentMaker._style_phantom_measures(5)
            <BLANKLINE>
                                }                                                                    %! baca.SegmentMaker._make_multimeasure_rest_container(6):PHANTOM
            <BLANKLINE>
                            >>                                                                       %! baca.SegmentMaker._make_multimeasure_rest_container(7):PHANTOM
            <BLANKLINE>
                        }                                                                            %! baca.SingleStaffScoreTemplate.__call__()
            <BLANKLINE>
                    }                                                                                %! baca.SingleStaffScoreTemplate.__call__()
            <BLANKLINE>
                >>                                                                                   %! baca.SingleStaffScoreTemplate.__call__()
            <BLANKLINE>
            >>                                                                                       %! baca.SingleStaffScoreTemplate.__call__()

        Even at the beginning of a segment:

        >>> breaks = baca.breaks(
        ...     baca.page(
        ...         [1, 0, (11,)],
        ...         [2, 15, (11,)],
        ...         ),
        ...     )
        >>> maker = baca.SegmentMaker(
        ...     breaks=breaks,
        ...     deactivate=[abjad.tags.NOT_YET_PITCHED_COLORING],
        ...     margin_markups=margin_markups,
        ...     score_template=baca.SingleStaffScoreTemplate(),
        ...     spacing=baca.minimum_duration((1, 24)),
        ...     time_signatures=[(3, 8), (3, 8)],
        ...     )
        >>> maker(
        ...     'Music_Voice',
        ...     baca.margin_markup(margin_markups['I+II']),
        ...     baca.make_notes(),
        ...     )

        >>> metadata, persist = {}, {}
        >>> persist['persistent_indicators'] = {}
        >>> persist['persistent_indicators']['Music_Staff'] = [
        ...     abjad.Momento(
        ...         context='Music_Voice',
        ...         manifest='margin_markups',
        ...         value='I+II',
        ...         )
        ...     ]
        >>> metadata['segment_number'] = 1
        >>> lilypond_file = maker.run(
        ...     environment='docs',
        ...     previous_metadata=metadata,
        ...     previous_persist=persist,
        ...     )
        >>> block = abjad.Block(name='layout')
        >>> block.indent = 0
        >>> lilypond_file.items.insert(0, block)
        >>> abjad.show(lilypond_file, strict=89) # doctest: +SKIP

        ..  docs::

            >>> abjad.f(lilypond_file[abjad.Score], strict=89)
            <BLANKLINE>
            \context Score = "Score"                                                                 %! baca.SingleStaffScoreTemplate.__call__()
            <<                                                                                       %! baca.SingleStaffScoreTemplate.__call__()
            <BLANKLINE>
                \context GlobalContext = "Global_Context"                                            %! abjad.ScoreTemplate._make_global_context()
                <<                                                                                   %! abjad.ScoreTemplate._make_global_context()
            <BLANKLINE>
                    \context GlobalSkips = "Global_Skips"                                            %! abjad.ScoreTemplate._make_global_context()
                    {                                                                                %! abjad.ScoreTemplate._make_global_context()
            <BLANKLINE>
                        % [Global_Skips measure 1]                                                   %! baca.SegmentMaker._comment_measure_numbers()
                        \baca-new-spacing-section #1 #24                                             %! SPACING_COMMAND:baca.HorizontalSpacingSpecifier.__call__(1)
                        \autoPageBreaksOff                                                           %! BREAK:baca.BreakMeasureMap.__call__(1)
                        \noBreak                                                                     %! BREAK:baca.BreakMeasureMap.__call__(2)
                        \baca-lbsd #0 #'(11)                                                         %! BREAK:baca.IndicatorCommand._call()
                        \time 3/8                                                                    %! baca.SegmentMaker._make_global_skips(2):baca.SegmentMaker._set_status_tag():EXPLICIT_TIME_SIGNATURE
                        \bar ""                                                                      %! EMPTY_START_BAR:+SEGMENT:baca.SegmentMaker._make_global_skips(4)
                        \baca-time-signature-color #'blue                                            %! baca.SegmentMaker._attach_color_literal(2):EXPLICIT_TIME_SIGNATURE_COLOR
                        \pageBreak                                                                   %! BREAK:baca.IndicatorCommand._call()
                        s1 * 3/8                                                                     %! baca.SegmentMaker._make_global_skips(1)
            <BLANKLINE>
                        % [Global_Skips measure 2]                                                   %! baca.SegmentMaker._comment_measure_numbers()
                        \baca-new-spacing-section #1 #24                                             %! SPACING_COMMAND:baca.HorizontalSpacingSpecifier.__call__(1)
                        \noBreak                                                                     %! BREAK:baca.BreakMeasureMap.__call__(2)
                        \baca-lbsd #15 #'(11)                                                        %! BREAK:baca.IndicatorCommand._call()
                        \break                                                                       %! BREAK:baca.IndicatorCommand._call()
                        s1 * 3/8                                                                     %! baca.SegmentMaker._make_global_skips(1)
            <BLANKLINE>
                        % [Global_Skips measure 3]                                                   %! baca.SegmentMaker._comment_measure_numbers():baca.SegmentMaker._style_phantom_measures(1):PHANTOM
                        \baca-new-spacing-section #1 #4                                              %! SPACING_COMMAND:baca.HorizontalSpacingSpecifier.__call__(1):baca.SegmentMaker._style_phantom_measures(1):PHANTOM
                        \noBreak                                                                     %! BREAK:baca.BreakMeasureMap.__call__(2):baca.SegmentMaker._style_phantom_measures(1):PHANTOM
                        \time 1/4                                                                    %! baca.SegmentMaker._make_global_skips(3):PHANTOM:baca.SegmentMaker._set_status_tag():EXPLICIT_TIME_SIGNATURE:baca.SegmentMaker._style_phantom_measures(1)
                        \baca-time-signature-transparent                                             %! baca.SegmentMaker._style_phantom_measures(2):PHANTOM
                        s1 * 1/4                                                                     %! baca.SegmentMaker._make_global_skips(3):PHANTOM
                        \once \override Score.BarLine.transparent = ##t                              %! baca.SegmentMaker._style_phantom_measures(3):PHANTOM
                        \once \override Score.SpanBar.transparent = ##t                              %! baca.SegmentMaker._style_phantom_measures(3):PHANTOM
            <BLANKLINE>
                    }                                                                                %! abjad.ScoreTemplate._make_global_context()
            <BLANKLINE>
                >>                                                                                   %! abjad.ScoreTemplate._make_global_context()
            <BLANKLINE>
                \context MusicContext = "Music_Context"                                              %! baca.SingleStaffScoreTemplate.__call__()
                <<                                                                                   %! baca.SingleStaffScoreTemplate.__call__()
            <BLANKLINE>
                    \context Staff = "Music_Staff"                                                   %! baca.SingleStaffScoreTemplate.__call__()
                    {                                                                                %! baca.SingleStaffScoreTemplate.__call__()
            <BLANKLINE>
                        \context Voice = "Music_Voice"                                               %! baca.SingleStaffScoreTemplate.__call__()
                        {                                                                            %! baca.SingleStaffScoreTemplate.__call__()
            <BLANKLINE>
                            % [Music_Voice measure 1]                                                %! baca.SegmentMaker._comment_measure_numbers()
                            \set Staff.shortInstrumentName =                                         %! baca.margin_markup():baca.IndicatorCommand._call():baca.SegmentMaker._set_status_tag():REDUNDANT_MARGIN_MARKUP
                            \markup { I+II }                                                         %! baca.margin_markup():baca.IndicatorCommand._call():baca.SegmentMaker._set_status_tag():REDUNDANT_MARGIN_MARKUP
                            \set Staff.instrumentName =                                              %! baca.SegmentMaker._clone_segment_initial_short_instrument_name()
                            \markup { I+II }                                                         %! baca.SegmentMaker._clone_segment_initial_short_instrument_name()
                            \once \override Staff.InstrumentName.color = #(x11-color 'DeepPink1)     %! baca.SegmentMaker._attach_color_literal(2):REDUNDANT_MARGIN_MARKUP_COLOR
                        %@% \baca-not-yet-pitched-coloring                                           %! baca.SegmentMaker._color_not_yet_pitched():NOT_YET_PITCHED_COLORING
                            b'4.                                                                     %! baca.make_notes()
                            ^ \baca-redundant-indicator-markup "[“I+II”]"                            %! REDUNDANT_MARGIN_MARKUP_ALERT:baca.SegmentMaker._attach_latent_indicator_alert()
                            \override Staff.InstrumentName.color = #(x11-color 'DeepPink4)           %! baca.SegmentMaker._attach_color_literal(2):REDRAWN_REDUNDANT_MARGIN_MARKUP_COLOR
                            \set Staff.shortInstrumentName =                                         %! baca.margin_markup():baca.IndicatorCommand._call():baca.SegmentMaker._treat_persistent_wrapper(3):baca.SegmentMaker._set_status_tag():REDRAWN_REDUNDANT_MARGIN_MARKUP
                            \markup { I+II }                                                         %! baca.margin_markup():baca.IndicatorCommand._call():baca.SegmentMaker._treat_persistent_wrapper(3):baca.SegmentMaker._set_status_tag():REDRAWN_REDUNDANT_MARGIN_MARKUP
            <BLANKLINE>
                            % [Music_Voice measure 2]                                                %! baca.SegmentMaker._comment_measure_numbers()
                        %@% \baca-not-yet-pitched-coloring                                           %! baca.SegmentMaker._color_not_yet_pitched():NOT_YET_PITCHED_COLORING
                            b'4.                                                                     %! baca.make_notes()
            <BLANKLINE>
                            <<                                                                       %! baca.SegmentMaker._make_multimeasure_rest_container(7):PHANTOM
            <BLANKLINE>
                                \context Voice = "Music_Voice"                                       %! baca.SegmentMaker._make_multimeasure_rest_container(4):PHANTOM
                                {                                                                    %! baca.SegmentMaker._make_multimeasure_rest_container(4):PHANTOM
            <BLANKLINE>
                                    % [Music_Voice measure 3]                                        %! baca.SegmentMaker._comment_measure_numbers():baca.SegmentMaker._style_phantom_measures(5):PHANTOM
                                    \abjad-invisible-music-coloring                                  %! baca.SegmentMaker._make_multimeasure_rest_container(2):PHANTOM:NOTE:INVISIBLE_MUSIC_COLORING:baca.SegmentMaker._style_phantom_measures(5)
                                %@% \abjad-invisible-music                                           %! baca.SegmentMaker._make_multimeasure_rest_container(3):PHANTOM:NOTE:INVISIBLE_MUSIC_COMMAND:baca.SegmentMaker._style_phantom_measures(5)
                                %@% \baca-not-yet-pitched-coloring                                   %! baca.SegmentMaker._color_not_yet_pitched():NOT_YET_PITCHED_COLORING:HIDDEN:NOTE:baca.SegmentMaker._style_phantom_measures(5):PHANTOM
                                    b'1 * 1/4                                                        %! baca.SegmentMaker._make_multimeasure_rest_container(1):PHANTOM:HIDDEN:NOTE
                                %@% ^ \baca-duration-multiplier-markup #"1" #"4"                     %! baca.SegmentMaker._label_duration_multipliers():DURATION_MULTIPLIER:HIDDEN:NOTE:PHANTOM:baca.SegmentMaker._style_phantom_measures(5)
            <BLANKLINE>
                                }                                                                    %! baca.SegmentMaker._make_multimeasure_rest_container(4):PHANTOM
            <BLANKLINE>
                                \context Voice = "Rest_Voice"                                        %! baca.SegmentMaker._make_multimeasure_rest_container(6):PHANTOM
                                {                                                                    %! baca.SegmentMaker._make_multimeasure_rest_container(6):PHANTOM
            <BLANKLINE>
                                    % [Rest_Voice measure 3]                                         %! baca.SegmentMaker._comment_measure_numbers():baca.SegmentMaker._style_phantom_measures(5):PHANTOM
                                    \once \override Score.TimeSignature.X-extent = ##f               %! baca.SegmentMaker._style_phantom_measures(6):PHANTOM
                                    \once \override MultiMeasureRest.transparent = ##t               %! baca.SegmentMaker._style_phantom_measures(7):PHANTOM
                                    \stopStaff                                                       %! baca.SegmentMaker._style_phantom_measures(8):PHANTOM
                                    \once \override Staff.StaffSymbol.transparent = ##t              %! baca.SegmentMaker._style_phantom_measures(8):PHANTOM
                                    \startStaff                                                      %! baca.SegmentMaker._style_phantom_measures(8):PHANTOM
                                    R1 * 1/4                                                         %! baca.SegmentMaker._make_multimeasure_rest_container(5):PHANTOM:REST_VOICE:MULTIMEASURE_REST
                                %@% ^ \baca-duration-multiplier-markup #"1" #"4"                     %! baca.SegmentMaker._label_duration_multipliers():DURATION_MULTIPLIER:MULTIMEASURE_REST:PHANTOM:REST_VOICE:baca.SegmentMaker._style_phantom_measures(5)
            <BLANKLINE>
                                }                                                                    %! baca.SegmentMaker._make_multimeasure_rest_container(6):PHANTOM
            <BLANKLINE>
                            >>                                                                       %! baca.SegmentMaker._make_multimeasure_rest_container(7):PHANTOM
            <BLANKLINE>
                        }                                                                            %! baca.SingleStaffScoreTemplate.__call__()
            <BLANKLINE>
                    }                                                                                %! baca.SingleStaffScoreTemplate.__call__()
            <BLANKLINE>
                >>                                                                                   %! baca.SingleStaffScoreTemplate.__call__()
            <BLANKLINE>
            >>                                                                                       %! baca.SingleStaffScoreTemplate.__call__()

        >>> score = lilypond_file[abjad.Score]
        >>> text = format(score, 'lilypond')
        >>> text = abjad.LilyPondFormatManager.left_shift_tags(text)
        >>> tags_ = abjad.tags.margin_markup_color_tags()
        >>> match = lambda tags: bool(set(tags) & set(tags_))
        >>> text, count = abjad.deactivate(text, match)
        >>> text = abjad.LilyPondFormatManager.left_shift_tags(text, 89)
        >>> lines = [_.strip('\n') for _ in text.split('\n')]
        >>> lilypond_file.score_block.items[:] = lines
        >>> abjad.show(lilypond_file, strict=89) # doctest: +SKIP

        ..  docs::

            >>> print(text)
            <BLANKLINE>
            \context Score = "Score"                                                                 %! baca.SingleStaffScoreTemplate.__call__()
            <<                                                                                       %! baca.SingleStaffScoreTemplate.__call__()
            <BLANKLINE>
                \context GlobalContext = "Global_Context"                                            %! abjad.ScoreTemplate._make_global_context()
                <<                                                                                   %! abjad.ScoreTemplate._make_global_context()
            <BLANKLINE>
                    \context GlobalSkips = "Global_Skips"                                            %! abjad.ScoreTemplate._make_global_context()
                    {                                                                                %! abjad.ScoreTemplate._make_global_context()
            <BLANKLINE>
                        % [Global_Skips measure 1]                                                   %! baca.SegmentMaker._comment_measure_numbers()
                        \baca-new-spacing-section #1 #24                                             %! SPACING_COMMAND:baca.HorizontalSpacingSpecifier.__call__(1)
                        \autoPageBreaksOff                                                           %! BREAK:baca.BreakMeasureMap.__call__(1)
                        \noBreak                                                                     %! BREAK:baca.BreakMeasureMap.__call__(2)
                        \baca-lbsd #0 #'(11)                                                         %! BREAK:baca.IndicatorCommand._call()
                        \time 3/8                                                                    %! baca.SegmentMaker._make_global_skips(2):baca.SegmentMaker._set_status_tag():EXPLICIT_TIME_SIGNATURE
                        \bar ""                                                                      %! EMPTY_START_BAR:+SEGMENT:baca.SegmentMaker._make_global_skips(4)
                        \baca-time-signature-color #'blue                                            %! baca.SegmentMaker._attach_color_literal(2):EXPLICIT_TIME_SIGNATURE_COLOR
                        \pageBreak                                                                   %! BREAK:baca.IndicatorCommand._call()
                        s1 * 3/8                                                                     %! baca.SegmentMaker._make_global_skips(1)
            <BLANKLINE>
                        % [Global_Skips measure 2]                                                   %! baca.SegmentMaker._comment_measure_numbers()
                        \baca-new-spacing-section #1 #24                                             %! SPACING_COMMAND:baca.HorizontalSpacingSpecifier.__call__(1)
                        \noBreak                                                                     %! BREAK:baca.BreakMeasureMap.__call__(2)
                        \baca-lbsd #15 #'(11)                                                        %! BREAK:baca.IndicatorCommand._call()
                        \break                                                                       %! BREAK:baca.IndicatorCommand._call()
                        s1 * 3/8                                                                     %! baca.SegmentMaker._make_global_skips(1)
            <BLANKLINE>
                        % [Global_Skips measure 3]                                                   %! baca.SegmentMaker._comment_measure_numbers():baca.SegmentMaker._style_phantom_measures(1):PHANTOM
                        \baca-new-spacing-section #1 #4                                              %! SPACING_COMMAND:baca.HorizontalSpacingSpecifier.__call__(1):baca.SegmentMaker._style_phantom_measures(1):PHANTOM
                        \noBreak                                                                     %! BREAK:baca.BreakMeasureMap.__call__(2):baca.SegmentMaker._style_phantom_measures(1):PHANTOM
                        \time 1/4                                                                    %! baca.SegmentMaker._make_global_skips(3):PHANTOM:baca.SegmentMaker._set_status_tag():EXPLICIT_TIME_SIGNATURE:baca.SegmentMaker._style_phantom_measures(1)
                        \baca-time-signature-transparent                                             %! baca.SegmentMaker._style_phantom_measures(2):PHANTOM
                        s1 * 1/4                                                                     %! baca.SegmentMaker._make_global_skips(3):PHANTOM
                        \once \override Score.BarLine.transparent = ##t                              %! baca.SegmentMaker._style_phantom_measures(3):PHANTOM
                        \once \override Score.SpanBar.transparent = ##t                              %! baca.SegmentMaker._style_phantom_measures(3):PHANTOM
            <BLANKLINE>
                    }                                                                                %! abjad.ScoreTemplate._make_global_context()
            <BLANKLINE>
                >>                                                                                   %! abjad.ScoreTemplate._make_global_context()
            <BLANKLINE>
                \context MusicContext = "Music_Context"                                              %! baca.SingleStaffScoreTemplate.__call__()
                <<                                                                                   %! baca.SingleStaffScoreTemplate.__call__()
            <BLANKLINE>
                    \context Staff = "Music_Staff"                                                   %! baca.SingleStaffScoreTemplate.__call__()
                    {                                                                                %! baca.SingleStaffScoreTemplate.__call__()
            <BLANKLINE>
                        \context Voice = "Music_Voice"                                               %! baca.SingleStaffScoreTemplate.__call__()
                        {                                                                            %! baca.SingleStaffScoreTemplate.__call__()
            <BLANKLINE>
                            % [Music_Voice measure 1]                                                %! baca.SegmentMaker._comment_measure_numbers()
                            \set Staff.shortInstrumentName =                                         %! baca.margin_markup():baca.IndicatorCommand._call():baca.SegmentMaker._set_status_tag():REDUNDANT_MARGIN_MARKUP
                            \markup { I+II }                                                         %! baca.margin_markup():baca.IndicatorCommand._call():baca.SegmentMaker._set_status_tag():REDUNDANT_MARGIN_MARKUP
                            \set Staff.instrumentName =                                              %! baca.SegmentMaker._clone_segment_initial_short_instrument_name()
                            \markup { I+II }                                                         %! baca.SegmentMaker._clone_segment_initial_short_instrument_name()
                        %%% \once \override Staff.InstrumentName.color = #(x11-color 'DeepPink1)     %! baca.SegmentMaker._attach_color_literal(2):REDUNDANT_MARGIN_MARKUP_COLOR
                    %@% \baca-not-yet-pitched-coloring                                               %! baca.SegmentMaker._color_not_yet_pitched():NOT_YET_PITCHED_COLORING
                            b'4.                                                                     %! baca.make_notes()
                        %%% ^ \baca-redundant-indicator-markup "[“I+II”]"                            %! REDUNDANT_MARGIN_MARKUP_ALERT:baca.SegmentMaker._attach_latent_indicator_alert()
                        %%% \override Staff.InstrumentName.color = #(x11-color 'DeepPink4)           %! baca.SegmentMaker._attach_color_literal(2):REDRAWN_REDUNDANT_MARGIN_MARKUP_COLOR
                            \set Staff.shortInstrumentName =                                         %! baca.margin_markup():baca.IndicatorCommand._call():baca.SegmentMaker._treat_persistent_wrapper(3):baca.SegmentMaker._set_status_tag():REDRAWN_REDUNDANT_MARGIN_MARKUP
                            \markup { I+II }                                                         %! baca.margin_markup():baca.IndicatorCommand._call():baca.SegmentMaker._treat_persistent_wrapper(3):baca.SegmentMaker._set_status_tag():REDRAWN_REDUNDANT_MARGIN_MARKUP
            <BLANKLINE>
                            % [Music_Voice measure 2]                                                %! baca.SegmentMaker._comment_measure_numbers()
                    %@% \baca-not-yet-pitched-coloring                                               %! baca.SegmentMaker._color_not_yet_pitched():NOT_YET_PITCHED_COLORING
                            b'4.                                                                     %! baca.make_notes()
            <BLANKLINE>
                            <<                                                                       %! baca.SegmentMaker._make_multimeasure_rest_container(7):PHANTOM
            <BLANKLINE>
                                \context Voice = "Music_Voice"                                       %! baca.SegmentMaker._make_multimeasure_rest_container(4):PHANTOM
                                {                                                                    %! baca.SegmentMaker._make_multimeasure_rest_container(4):PHANTOM
            <BLANKLINE>
                                    % [Music_Voice measure 3]                                        %! baca.SegmentMaker._comment_measure_numbers():baca.SegmentMaker._style_phantom_measures(5):PHANTOM
                                    \abjad-invisible-music-coloring                                  %! baca.SegmentMaker._make_multimeasure_rest_container(2):PHANTOM:NOTE:INVISIBLE_MUSIC_COLORING:baca.SegmentMaker._style_phantom_measures(5)
                            %@% \abjad-invisible-music                                               %! baca.SegmentMaker._make_multimeasure_rest_container(3):PHANTOM:NOTE:INVISIBLE_MUSIC_COMMAND:baca.SegmentMaker._style_phantom_measures(5)
                            %@% \baca-not-yet-pitched-coloring                                       %! baca.SegmentMaker._color_not_yet_pitched():NOT_YET_PITCHED_COLORING:HIDDEN:NOTE:baca.SegmentMaker._style_phantom_measures(5):PHANTOM
                                    b'1 * 1/4                                                        %! baca.SegmentMaker._make_multimeasure_rest_container(1):PHANTOM:HIDDEN:NOTE
                            %@% ^ \baca-duration-multiplier-markup #"1" #"4"                         %! baca.SegmentMaker._label_duration_multipliers():DURATION_MULTIPLIER:HIDDEN:NOTE:PHANTOM:baca.SegmentMaker._style_phantom_measures(5)
            <BLANKLINE>
                                }                                                                    %! baca.SegmentMaker._make_multimeasure_rest_container(4):PHANTOM
            <BLANKLINE>
                                \context Voice = "Rest_Voice"                                        %! baca.SegmentMaker._make_multimeasure_rest_container(6):PHANTOM
                                {                                                                    %! baca.SegmentMaker._make_multimeasure_rest_container(6):PHANTOM
            <BLANKLINE>
                                    % [Rest_Voice measure 3]                                         %! baca.SegmentMaker._comment_measure_numbers():baca.SegmentMaker._style_phantom_measures(5):PHANTOM
                                    \once \override Score.TimeSignature.X-extent = ##f               %! baca.SegmentMaker._style_phantom_measures(6):PHANTOM
                                    \once \override MultiMeasureRest.transparent = ##t               %! baca.SegmentMaker._style_phantom_measures(7):PHANTOM
                                    \stopStaff                                                       %! baca.SegmentMaker._style_phantom_measures(8):PHANTOM
                                    \once \override Staff.StaffSymbol.transparent = ##t              %! baca.SegmentMaker._style_phantom_measures(8):PHANTOM
                                    \startStaff                                                      %! baca.SegmentMaker._style_phantom_measures(8):PHANTOM
                                    R1 * 1/4                                                         %! baca.SegmentMaker._make_multimeasure_rest_container(5):PHANTOM:REST_VOICE:MULTIMEASURE_REST
                            %@% ^ \baca-duration-multiplier-markup #"1" #"4"                         %! baca.SegmentMaker._label_duration_multipliers():DURATION_MULTIPLIER:MULTIMEASURE_REST:PHANTOM:REST_VOICE:baca.SegmentMaker._style_phantom_measures(5)
            <BLANKLINE>
                                }                                                                    %! baca.SegmentMaker._make_multimeasure_rest_container(6):PHANTOM
            <BLANKLINE>
                            >>                                                                       %! baca.SegmentMaker._make_multimeasure_rest_container(7):PHANTOM
            <BLANKLINE>
                        }                                                                            %! baca.SingleStaffScoreTemplate.__call__()
            <BLANKLINE>
                    }                                                                                %! baca.SingleStaffScoreTemplate.__call__()
            <BLANKLINE>
                >>                                                                                   %! baca.SingleStaffScoreTemplate.__call__()
            <BLANKLINE>
            >>                                                                                       %! baca.SingleStaffScoreTemplate.__call__()

        >>> tags_ = abjad.tags.margin_markup_color_tags()
        >>> match = lambda tags: bool(set(tags) & set(tags_))
        >>> text, count = abjad.activate(text, match)
        >>> lines = [_.strip('\n') for _ in text.split('\n')]
        >>> lilypond_file.score_block.items[:] = lines
        >>> abjad.show(lilypond_file, strict=89) # doctest: +SKIP

        ..  docs::

            >>> print(text)
            <BLANKLINE>
            \context Score = "Score"                                                                 %! baca.SingleStaffScoreTemplate.__call__()
            <<                                                                                       %! baca.SingleStaffScoreTemplate.__call__()
            <BLANKLINE>
                \context GlobalContext = "Global_Context"                                            %! abjad.ScoreTemplate._make_global_context()
                <<                                                                                   %! abjad.ScoreTemplate._make_global_context()
            <BLANKLINE>
                    \context GlobalSkips = "Global_Skips"                                            %! abjad.ScoreTemplate._make_global_context()
                    {                                                                                %! abjad.ScoreTemplate._make_global_context()
            <BLANKLINE>
                        % [Global_Skips measure 1]                                                   %! baca.SegmentMaker._comment_measure_numbers()
                        \baca-new-spacing-section #1 #24                                             %! SPACING_COMMAND:baca.HorizontalSpacingSpecifier.__call__(1)
                        \autoPageBreaksOff                                                           %! BREAK:baca.BreakMeasureMap.__call__(1)
                        \noBreak                                                                     %! BREAK:baca.BreakMeasureMap.__call__(2)
                        \baca-lbsd #0 #'(11)                                                         %! BREAK:baca.IndicatorCommand._call()
                        \time 3/8                                                                    %! baca.SegmentMaker._make_global_skips(2):baca.SegmentMaker._set_status_tag():EXPLICIT_TIME_SIGNATURE
                        \bar ""                                                                      %! EMPTY_START_BAR:+SEGMENT:baca.SegmentMaker._make_global_skips(4)
                        \baca-time-signature-color #'blue                                            %! baca.SegmentMaker._attach_color_literal(2):EXPLICIT_TIME_SIGNATURE_COLOR
                        \pageBreak                                                                   %! BREAK:baca.IndicatorCommand._call()
                        s1 * 3/8                                                                     %! baca.SegmentMaker._make_global_skips(1)
            <BLANKLINE>
                        % [Global_Skips measure 2]                                                   %! baca.SegmentMaker._comment_measure_numbers()
                        \baca-new-spacing-section #1 #24                                             %! SPACING_COMMAND:baca.HorizontalSpacingSpecifier.__call__(1)
                        \noBreak                                                                     %! BREAK:baca.BreakMeasureMap.__call__(2)
                        \baca-lbsd #15 #'(11)                                                        %! BREAK:baca.IndicatorCommand._call()
                        \break                                                                       %! BREAK:baca.IndicatorCommand._call()
                        s1 * 3/8                                                                     %! baca.SegmentMaker._make_global_skips(1)
            <BLANKLINE>
                        % [Global_Skips measure 3]                                                   %! baca.SegmentMaker._comment_measure_numbers():baca.SegmentMaker._style_phantom_measures(1):PHANTOM
                        \baca-new-spacing-section #1 #4                                              %! SPACING_COMMAND:baca.HorizontalSpacingSpecifier.__call__(1):baca.SegmentMaker._style_phantom_measures(1):PHANTOM
                        \noBreak                                                                     %! BREAK:baca.BreakMeasureMap.__call__(2):baca.SegmentMaker._style_phantom_measures(1):PHANTOM
                        \time 1/4                                                                    %! baca.SegmentMaker._make_global_skips(3):PHANTOM:baca.SegmentMaker._set_status_tag():EXPLICIT_TIME_SIGNATURE:baca.SegmentMaker._style_phantom_measures(1)
                        \baca-time-signature-transparent                                             %! baca.SegmentMaker._style_phantom_measures(2):PHANTOM
                        s1 * 1/4                                                                     %! baca.SegmentMaker._make_global_skips(3):PHANTOM
                        \once \override Score.BarLine.transparent = ##t                              %! baca.SegmentMaker._style_phantom_measures(3):PHANTOM
                        \once \override Score.SpanBar.transparent = ##t                              %! baca.SegmentMaker._style_phantom_measures(3):PHANTOM
            <BLANKLINE>
                    }                                                                                %! abjad.ScoreTemplate._make_global_context()
            <BLANKLINE>
                >>                                                                                   %! abjad.ScoreTemplate._make_global_context()
            <BLANKLINE>
                \context MusicContext = "Music_Context"                                              %! baca.SingleStaffScoreTemplate.__call__()
                <<                                                                                   %! baca.SingleStaffScoreTemplate.__call__()
            <BLANKLINE>
                    \context Staff = "Music_Staff"                                                   %! baca.SingleStaffScoreTemplate.__call__()
                    {                                                                                %! baca.SingleStaffScoreTemplate.__call__()
            <BLANKLINE>
                        \context Voice = "Music_Voice"                                               %! baca.SingleStaffScoreTemplate.__call__()
                        {                                                                            %! baca.SingleStaffScoreTemplate.__call__()
            <BLANKLINE>
                            % [Music_Voice measure 1]                                                %! baca.SegmentMaker._comment_measure_numbers()
                            \set Staff.shortInstrumentName =                                         %! baca.margin_markup():baca.IndicatorCommand._call():baca.SegmentMaker._set_status_tag():REDUNDANT_MARGIN_MARKUP
                            \markup { I+II }                                                         %! baca.margin_markup():baca.IndicatorCommand._call():baca.SegmentMaker._set_status_tag():REDUNDANT_MARGIN_MARKUP
                            \set Staff.instrumentName =                                              %! baca.SegmentMaker._clone_segment_initial_short_instrument_name()
                            \markup { I+II }                                                         %! baca.SegmentMaker._clone_segment_initial_short_instrument_name()
                            \once \override Staff.InstrumentName.color = #(x11-color 'DeepPink1)     %! baca.SegmentMaker._attach_color_literal(2):REDUNDANT_MARGIN_MARKUP_COLOR
                    %@% \baca-not-yet-pitched-coloring                                               %! baca.SegmentMaker._color_not_yet_pitched():NOT_YET_PITCHED_COLORING
                            b'4.                                                                     %! baca.make_notes()
                            ^ \baca-redundant-indicator-markup "[“I+II”]"                            %! REDUNDANT_MARGIN_MARKUP_ALERT:baca.SegmentMaker._attach_latent_indicator_alert()
                            \override Staff.InstrumentName.color = #(x11-color 'DeepPink4)           %! baca.SegmentMaker._attach_color_literal(2):REDRAWN_REDUNDANT_MARGIN_MARKUP_COLOR
                            \set Staff.shortInstrumentName =                                         %! baca.margin_markup():baca.IndicatorCommand._call():baca.SegmentMaker._treat_persistent_wrapper(3):baca.SegmentMaker._set_status_tag():REDRAWN_REDUNDANT_MARGIN_MARKUP
                            \markup { I+II }                                                         %! baca.margin_markup():baca.IndicatorCommand._call():baca.SegmentMaker._treat_persistent_wrapper(3):baca.SegmentMaker._set_status_tag():REDRAWN_REDUNDANT_MARGIN_MARKUP
            <BLANKLINE>
                            % [Music_Voice measure 2]                                                %! baca.SegmentMaker._comment_measure_numbers()
                    %@% \baca-not-yet-pitched-coloring                                               %! baca.SegmentMaker._color_not_yet_pitched():NOT_YET_PITCHED_COLORING
                            b'4.                                                                     %! baca.make_notes()
            <BLANKLINE>
                            <<                                                                       %! baca.SegmentMaker._make_multimeasure_rest_container(7):PHANTOM
            <BLANKLINE>
                                \context Voice = "Music_Voice"                                       %! baca.SegmentMaker._make_multimeasure_rest_container(4):PHANTOM
                                {                                                                    %! baca.SegmentMaker._make_multimeasure_rest_container(4):PHANTOM
            <BLANKLINE>
                                    % [Music_Voice measure 3]                                        %! baca.SegmentMaker._comment_measure_numbers():baca.SegmentMaker._style_phantom_measures(5):PHANTOM
                                    \abjad-invisible-music-coloring                                  %! baca.SegmentMaker._make_multimeasure_rest_container(2):PHANTOM:NOTE:INVISIBLE_MUSIC_COLORING:baca.SegmentMaker._style_phantom_measures(5)
                            %@% \abjad-invisible-music                                               %! baca.SegmentMaker._make_multimeasure_rest_container(3):PHANTOM:NOTE:INVISIBLE_MUSIC_COMMAND:baca.SegmentMaker._style_phantom_measures(5)
                            %@% \baca-not-yet-pitched-coloring                                       %! baca.SegmentMaker._color_not_yet_pitched():NOT_YET_PITCHED_COLORING:HIDDEN:NOTE:baca.SegmentMaker._style_phantom_measures(5):PHANTOM
                                    b'1 * 1/4                                                        %! baca.SegmentMaker._make_multimeasure_rest_container(1):PHANTOM:HIDDEN:NOTE
                            %@% ^ \baca-duration-multiplier-markup #"1" #"4"                         %! baca.SegmentMaker._label_duration_multipliers():DURATION_MULTIPLIER:HIDDEN:NOTE:PHANTOM:baca.SegmentMaker._style_phantom_measures(5)
            <BLANKLINE>
                                }                                                                    %! baca.SegmentMaker._make_multimeasure_rest_container(4):PHANTOM
            <BLANKLINE>
                                \context Voice = "Rest_Voice"                                        %! baca.SegmentMaker._make_multimeasure_rest_container(6):PHANTOM
                                {                                                                    %! baca.SegmentMaker._make_multimeasure_rest_container(6):PHANTOM
            <BLANKLINE>
                                    % [Rest_Voice measure 3]                                         %! baca.SegmentMaker._comment_measure_numbers():baca.SegmentMaker._style_phantom_measures(5):PHANTOM
                                    \once \override Score.TimeSignature.X-extent = ##f               %! baca.SegmentMaker._style_phantom_measures(6):PHANTOM
                                    \once \override MultiMeasureRest.transparent = ##t               %! baca.SegmentMaker._style_phantom_measures(7):PHANTOM
                                    \stopStaff                                                       %! baca.SegmentMaker._style_phantom_measures(8):PHANTOM
                                    \once \override Staff.StaffSymbol.transparent = ##t              %! baca.SegmentMaker._style_phantom_measures(8):PHANTOM
                                    \startStaff                                                      %! baca.SegmentMaker._style_phantom_measures(8):PHANTOM
                                    R1 * 1/4                                                         %! baca.SegmentMaker._make_multimeasure_rest_container(5):PHANTOM:REST_VOICE:MULTIMEASURE_REST
                            %@% ^ \baca-duration-multiplier-markup #"1" #"4"                         %! baca.SegmentMaker._label_duration_multipliers():DURATION_MULTIPLIER:MULTIMEASURE_REST:PHANTOM:REST_VOICE:baca.SegmentMaker._style_phantom_measures(5)
            <BLANKLINE>
                                }                                                                    %! baca.SegmentMaker._make_multimeasure_rest_container(6):PHANTOM
            <BLANKLINE>
                            >>                                                                       %! baca.SegmentMaker._make_multimeasure_rest_container(7):PHANTOM
            <BLANKLINE>
                        }                                                                            %! baca.SingleStaffScoreTemplate.__call__()
            <BLANKLINE>
                    }                                                                                %! baca.SingleStaffScoreTemplate.__call__()
            <BLANKLINE>
                >>                                                                                   %! baca.SingleStaffScoreTemplate.__call__()
            <BLANKLINE>
            >>                                                                                       %! baca.SingleStaffScoreTemplate.__call__()

    ..  container:: example

        Multiple margin markup are allowed so long as only one is active:

        >>> breaks = baca.breaks(
        ...     baca.page(
        ...         [1, 0, (11,)],
        ...         [2, 15, (11,)],
        ...         ),
        ...     )
        >>> maker = baca.SegmentMaker(
        ...     breaks=breaks,
        ...     deactivate=[abjad.tags.NOT_YET_PITCHED_COLORING],
        ...     margin_markups=margin_markups,
        ...     score_template=baca.SingleStaffScoreTemplate(),
        ...     spacing=baca.minimum_duration((1, 24)),
        ...     time_signatures=[(4, 8), (4, 8), (4, 8)],
        ...     )
        >>> maker(
        ...     'Music_Voice',
        ...     baca.tag(
        ...         abjad.tags.NOT_PARTS,
        ...         baca.margin_markup(margin_markups['I+II']),
        ...         ),
        ...     baca.tag(
        ...         abjad.tags.NOT_PARTS,
        ...         baca.margin_markup(margin_markups['III+IV']),
        ...         deactivate=True,
        ...         ),
        ...     baca.tag(
        ...         abjad.tags.NOT_PARTS,
        ...         baca.margin_markup(margin_markups['III+IV']),
        ...         deactivate=True,
        ...         ),
        ...     baca.make_notes(),
        ...     )

        >>> lilypond_file = maker.run(environment='docs')
        >>> block = abjad.Block(name='layout')
        >>> block.indent = 0
        >>> lilypond_file.items.insert(0, block)
        >>> abjad.show(lilypond_file, strict=89) # doctest: +SKIP

        ..  docs::

            >>> abjad.f(lilypond_file[abjad.Score], strict=89)
            <BLANKLINE>
            \context Score = "Score"                                                                 %! baca.SingleStaffScoreTemplate.__call__()
            <<                                                                                       %! baca.SingleStaffScoreTemplate.__call__()
            <BLANKLINE>
                \context GlobalContext = "Global_Context"                                            %! abjad.ScoreTemplate._make_global_context()
                <<                                                                                   %! abjad.ScoreTemplate._make_global_context()
            <BLANKLINE>
                    \context GlobalSkips = "Global_Skips"                                            %! abjad.ScoreTemplate._make_global_context()
                    {                                                                                %! abjad.ScoreTemplate._make_global_context()
            <BLANKLINE>
                        % [Global_Skips measure 1]                                                   %! baca.SegmentMaker._comment_measure_numbers()
                        \baca-new-spacing-section #1 #24                                             %! SPACING_COMMAND:baca.HorizontalSpacingSpecifier.__call__(1)
                        \autoPageBreaksOff                                                           %! BREAK:baca.BreakMeasureMap.__call__(1)
                        \noBreak                                                                     %! BREAK:baca.BreakMeasureMap.__call__(2)
                        \baca-lbsd #0 #'(11)                                                         %! BREAK:baca.IndicatorCommand._call()
                        \time 4/8                                                                    %! baca.SegmentMaker._make_global_skips(2):baca.SegmentMaker._set_status_tag():EXPLICIT_TIME_SIGNATURE
                        \baca-time-signature-color #'blue                                            %! baca.SegmentMaker._attach_color_literal(2):EXPLICIT_TIME_SIGNATURE_COLOR
                        \pageBreak                                                                   %! BREAK:baca.IndicatorCommand._call()
                        s1 * 1/2                                                                     %! baca.SegmentMaker._make_global_skips(1)
            <BLANKLINE>
                        % [Global_Skips measure 2]                                                   %! baca.SegmentMaker._comment_measure_numbers()
                        \baca-new-spacing-section #1 #24                                             %! SPACING_COMMAND:baca.HorizontalSpacingSpecifier.__call__(1)
                        \noBreak                                                                     %! BREAK:baca.BreakMeasureMap.__call__(2)
                        \baca-lbsd #15 #'(11)                                                        %! BREAK:baca.IndicatorCommand._call()
                        \break                                                                       %! BREAK:baca.IndicatorCommand._call()
                        s1 * 1/2                                                                     %! baca.SegmentMaker._make_global_skips(1)
            <BLANKLINE>
                        % [Global_Skips measure 3]                                                   %! baca.SegmentMaker._comment_measure_numbers()
                        \baca-new-spacing-section #1 #24                                             %! SPACING_COMMAND:baca.HorizontalSpacingSpecifier.__call__(1)
                        \noBreak                                                                     %! BREAK:baca.BreakMeasureMap.__call__(2)
                        s1 * 1/2                                                                     %! baca.SegmentMaker._make_global_skips(1)
            <BLANKLINE>
                        % [Global_Skips measure 4]                                                   %! baca.SegmentMaker._comment_measure_numbers():baca.SegmentMaker._style_phantom_measures(1):PHANTOM
                        \baca-new-spacing-section #1 #4                                              %! SPACING_COMMAND:baca.HorizontalSpacingSpecifier.__call__(1):baca.SegmentMaker._style_phantom_measures(1):PHANTOM
                        \noBreak                                                                     %! BREAK:baca.BreakMeasureMap.__call__(2):baca.SegmentMaker._style_phantom_measures(1):PHANTOM
                        \time 1/4                                                                    %! baca.SegmentMaker._make_global_skips(3):PHANTOM:baca.SegmentMaker._set_status_tag():EXPLICIT_TIME_SIGNATURE:baca.SegmentMaker._style_phantom_measures(1)
                        \baca-time-signature-transparent                                             %! baca.SegmentMaker._style_phantom_measures(2):PHANTOM
                        s1 * 1/4                                                                     %! baca.SegmentMaker._make_global_skips(3):PHANTOM
                        \once \override Score.BarLine.transparent = ##t                              %! baca.SegmentMaker._style_phantom_measures(3):PHANTOM
                        \once \override Score.SpanBar.transparent = ##t                              %! baca.SegmentMaker._style_phantom_measures(3):PHANTOM
            <BLANKLINE>
                    }                                                                                %! abjad.ScoreTemplate._make_global_context()
            <BLANKLINE>
                >>                                                                                   %! abjad.ScoreTemplate._make_global_context()
            <BLANKLINE>
                \context MusicContext = "Music_Context"                                              %! baca.SingleStaffScoreTemplate.__call__()
                <<                                                                                   %! baca.SingleStaffScoreTemplate.__call__()
            <BLANKLINE>
                    \context Staff = "Music_Staff"                                                   %! baca.SingleStaffScoreTemplate.__call__()
                    {                                                                                %! baca.SingleStaffScoreTemplate.__call__()
            <BLANKLINE>
                        \context Voice = "Music_Voice"                                               %! baca.SingleStaffScoreTemplate.__call__()
                        {                                                                            %! baca.SingleStaffScoreTemplate.__call__()
            <BLANKLINE>
                            % [Music_Voice measure 1]                                                %! baca.SegmentMaker._comment_measure_numbers()
                            \set Staff.shortInstrumentName =                                         %! baca.margin_markup():-PARTS:baca.IndicatorCommand._call():baca.SegmentMaker._set_status_tag():EXPLICIT_MARGIN_MARKUP
                            \markup { I+II }                                                         %! baca.margin_markup():-PARTS:baca.IndicatorCommand._call():baca.SegmentMaker._set_status_tag():EXPLICIT_MARGIN_MARKUP
                        %@% \set Staff.shortInstrumentName =                                         %! baca.margin_markup():-PARTS:baca.IndicatorCommand._call():baca.SegmentMaker._set_status_tag():EXPLICIT_MARGIN_MARKUP
                        %@% \markup { III+IV }                                                       %! baca.margin_markup():-PARTS:baca.IndicatorCommand._call():baca.SegmentMaker._set_status_tag():EXPLICIT_MARGIN_MARKUP
                            \once \override Staff.InstrumentName.color = #(x11-color 'blue)          %! baca.SegmentMaker._attach_color_literal(2):EXPLICIT_MARGIN_MARKUP_COLOR
                        %@% \once \override Staff.InstrumentName.color = #(x11-color 'blue)          %! baca.SegmentMaker._attach_color_literal(2):EXPLICIT_MARGIN_MARKUP_COLOR
                        %@% \baca-not-yet-pitched-coloring                                           %! baca.SegmentMaker._color_not_yet_pitched():NOT_YET_PITCHED_COLORING
                            b'2                                                                      %! baca.make_notes()
                            ^ \baca-explicit-indicator-markup "[“I+II”]"                             %! EXPLICIT_MARGIN_MARKUP_ALERT:baca.SegmentMaker._attach_latent_indicator_alert()
                        %@% ^ \baca-explicit-indicator-markup "[“III+IV”]"                           %! EXPLICIT_MARGIN_MARKUP_ALERT:baca.SegmentMaker._attach_latent_indicator_alert()
                            \override Staff.InstrumentName.color = #(x11-color 'DeepSkyBlue2)        %! baca.SegmentMaker._attach_color_literal(2):REDRAWN_EXPLICIT_MARGIN_MARKUP_COLOR
                            \set Staff.shortInstrumentName =                                         %! baca.margin_markup():-PARTS:baca.IndicatorCommand._call():baca.SegmentMaker._treat_persistent_wrapper(3):baca.SegmentMaker._set_status_tag():REDRAWN_EXPLICIT_MARGIN_MARKUP
                            \markup { I+II }                                                         %! baca.margin_markup():-PARTS:baca.IndicatorCommand._call():baca.SegmentMaker._treat_persistent_wrapper(3):baca.SegmentMaker._set_status_tag():REDRAWN_EXPLICIT_MARGIN_MARKUP
                        %@% \override Staff.InstrumentName.color = #(x11-color 'DeepSkyBlue2)        %! baca.SegmentMaker._attach_color_literal(2):REDRAWN_EXPLICIT_MARGIN_MARKUP_COLOR
                            \set Staff.shortInstrumentName =                                         %! baca.margin_markup():-PARTS:baca.IndicatorCommand._call():baca.SegmentMaker._treat_persistent_wrapper(3):baca.SegmentMaker._set_status_tag():REDRAWN_EXPLICIT_MARGIN_MARKUP
                            \markup { III+IV }                                                       %! baca.margin_markup():-PARTS:baca.IndicatorCommand._call():baca.SegmentMaker._treat_persistent_wrapper(3):baca.SegmentMaker._set_status_tag():REDRAWN_EXPLICIT_MARGIN_MARKUP
            <BLANKLINE>
                            % [Music_Voice measure 2]                                                %! baca.SegmentMaker._comment_measure_numbers()
                        %@% \baca-not-yet-pitched-coloring                                           %! baca.SegmentMaker._color_not_yet_pitched():NOT_YET_PITCHED_COLORING
                            b'2                                                                      %! baca.make_notes()
            <BLANKLINE>
                            % [Music_Voice measure 3]                                                %! baca.SegmentMaker._comment_measure_numbers()
                        %@% \baca-not-yet-pitched-coloring                                           %! baca.SegmentMaker._color_not_yet_pitched():NOT_YET_PITCHED_COLORING
                            b'2                                                                      %! baca.make_notes()
            <BLANKLINE>
                            <<                                                                       %! baca.SegmentMaker._make_multimeasure_rest_container(7):PHANTOM
            <BLANKLINE>
                                \context Voice = "Music_Voice"                                       %! baca.SegmentMaker._make_multimeasure_rest_container(4):PHANTOM
                                {                                                                    %! baca.SegmentMaker._make_multimeasure_rest_container(4):PHANTOM
            <BLANKLINE>
                                    % [Music_Voice measure 4]                                        %! baca.SegmentMaker._comment_measure_numbers():baca.SegmentMaker._style_phantom_measures(5):PHANTOM
                                    \abjad-invisible-music-coloring                                  %! baca.SegmentMaker._make_multimeasure_rest_container(2):PHANTOM:NOTE:INVISIBLE_MUSIC_COLORING:baca.SegmentMaker._style_phantom_measures(5)
                                %@% \abjad-invisible-music                                           %! baca.SegmentMaker._make_multimeasure_rest_container(3):PHANTOM:NOTE:INVISIBLE_MUSIC_COMMAND:baca.SegmentMaker._style_phantom_measures(5)
                                %@% \baca-not-yet-pitched-coloring                                   %! baca.SegmentMaker._color_not_yet_pitched():NOT_YET_PITCHED_COLORING:HIDDEN:NOTE:baca.SegmentMaker._style_phantom_measures(5):PHANTOM
                                    b'1 * 1/4                                                        %! baca.SegmentMaker._make_multimeasure_rest_container(1):PHANTOM:HIDDEN:NOTE
                                %@% ^ \baca-duration-multiplier-markup #"1" #"4"                     %! baca.SegmentMaker._label_duration_multipliers():DURATION_MULTIPLIER:HIDDEN:NOTE:PHANTOM:baca.SegmentMaker._style_phantom_measures(5)
            <BLANKLINE>
                                }                                                                    %! baca.SegmentMaker._make_multimeasure_rest_container(4):PHANTOM
            <BLANKLINE>
                                \context Voice = "Rest_Voice"                                        %! baca.SegmentMaker._make_multimeasure_rest_container(6):PHANTOM
                                {                                                                    %! baca.SegmentMaker._make_multimeasure_rest_container(6):PHANTOM
            <BLANKLINE>
                                    % [Rest_Voice measure 4]                                         %! baca.SegmentMaker._comment_measure_numbers():baca.SegmentMaker._style_phantom_measures(5):PHANTOM
                                    \once \override Score.TimeSignature.X-extent = ##f               %! baca.SegmentMaker._style_phantom_measures(6):PHANTOM
                                    \once \override MultiMeasureRest.transparent = ##t               %! baca.SegmentMaker._style_phantom_measures(7):PHANTOM
                                    \stopStaff                                                       %! baca.SegmentMaker._style_phantom_measures(8):PHANTOM
                                    \once \override Staff.StaffSymbol.transparent = ##t              %! baca.SegmentMaker._style_phantom_measures(8):PHANTOM
                                    \startStaff                                                      %! baca.SegmentMaker._style_phantom_measures(8):PHANTOM
                                    R1 * 1/4                                                         %! baca.SegmentMaker._make_multimeasure_rest_container(5):PHANTOM:REST_VOICE:MULTIMEASURE_REST
                                %@% ^ \baca-duration-multiplier-markup #"1" #"4"                     %! baca.SegmentMaker._label_duration_multipliers():DURATION_MULTIPLIER:MULTIMEASURE_REST:PHANTOM:REST_VOICE:baca.SegmentMaker._style_phantom_measures(5)
            <BLANKLINE>
                                }                                                                    %! baca.SegmentMaker._make_multimeasure_rest_container(6):PHANTOM
            <BLANKLINE>
                            >>                                                                       %! baca.SegmentMaker._make_multimeasure_rest_container(7):PHANTOM
            <BLANKLINE>
                        }                                                                            %! baca.SingleStaffScoreTemplate.__call__()
            <BLANKLINE>
                    }                                                                                %! baca.SingleStaffScoreTemplate.__call__()
            <BLANKLINE>
                >>                                                                                   %! baca.SingleStaffScoreTemplate.__call__()
            <BLANKLINE>
            >>                                                                                       %! baca.SingleStaffScoreTemplate.__call__()

..  container:: example

    Metronome marks.

    ..  container:: example

        >>> breaks = baca.breaks(baca.page([1, 4, (8,)]))
        >>> metronome_marks = abjad.OrderedDict()
        >>> metronome_marks['90'] = abjad.MetronomeMark((1, 4), 90)
        >>> metronome_marks['112'] = abjad.MetronomeMark((1, 4), 112)

    ..  container:: example

        Explicit metronome marks color blue:

        >>> maker = baca.SegmentMaker(
        ...     breaks=breaks,
        ...     deactivate=[abjad.tags.NOT_YET_PITCHED_COLORING],
        ...     metronome_marks=metronome_marks,
        ...     score_template=baca.SingleStaffScoreTemplate(),
        ...     spacing=baca.minimum_duration((1, 25)),
        ...     time_signatures=[(3, 8), (3, 8)],
        ...     )
        >>> maker(
        ...     'Global_Skips',
        ...     baca.metronome_mark('112'),
        ...     )
        >>> maker(
        ...     'Music_Voice',
        ...     baca.make_notes(),
        ...     )

        >>> lilypond_file = maker.run(environment='docs')
        >>> block = abjad.Block(name='layout')
        >>> block.indent = 0
        >>> lilypond_file.items.insert(0, block)
        >>> abjad.show(lilypond_file, strict=89) # doctest: +SKIP

        ..  docs::

            >>> abjad.f(lilypond_file[abjad.Score], strict=89)
            <BLANKLINE>
            \context Score = "Score"                                                                 %! baca.SingleStaffScoreTemplate.__call__()
            <<                                                                                       %! baca.SingleStaffScoreTemplate.__call__()
            <BLANKLINE>
                \context GlobalContext = "Global_Context"                                            %! abjad.ScoreTemplate._make_global_context()
                <<                                                                                   %! abjad.ScoreTemplate._make_global_context()
            <BLANKLINE>
                    \context GlobalSkips = "Global_Skips"                                            %! abjad.ScoreTemplate._make_global_context()
                    {                                                                                %! abjad.ScoreTemplate._make_global_context()
            <BLANKLINE>
                        % [Global_Skips measure 1]                                                   %! baca.SegmentMaker._comment_measure_numbers()
                        \baca-new-spacing-section #1 #25                                             %! SPACING_COMMAND:baca.HorizontalSpacingSpecifier.__call__(1)
                        \autoPageBreaksOff                                                           %! BREAK:baca.BreakMeasureMap.__call__(1)
                        \noBreak                                                                     %! BREAK:baca.BreakMeasureMap.__call__(2)
                        \baca-lbsd #4 #'(8)                                                          %! BREAK:baca.IndicatorCommand._call()
                        \time 3/8                                                                    %! baca.SegmentMaker._make_global_skips(2):baca.SegmentMaker._set_status_tag():EXPLICIT_TIME_SIGNATURE
                        \baca-time-signature-color #'blue                                            %! baca.SegmentMaker._attach_color_literal(2):EXPLICIT_TIME_SIGNATURE_COLOR
                        \pageBreak                                                                   %! BREAK:baca.IndicatorCommand._call()
                        s1 * 3/8                                                                     %! baca.SegmentMaker._make_global_skips(1)
                    %@% - \abjad-invisible-line                                                      %! baca.SegmentMaker._set_status_tag():EXPLICIT_METRONOME_MARK:baca.SegmentMaker._attach_metronome_marks(2)
                    %@% - \baca-metronome-mark-spanner-left-text 2 0 1 "112"                         %! baca.SegmentMaker._set_status_tag():EXPLICIT_METRONOME_MARK:baca.SegmentMaker._attach_metronome_marks(2)
                    %@% \bacaStartTextSpanMM                                                         %! baca.SegmentMaker._set_status_tag():EXPLICIT_METRONOME_MARK:baca.SegmentMaker._attach_metronome_marks(2)
                        - \abjad-invisible-line                                                      %! EXPLICIT_METRONOME_MARK_WITH_COLOR:baca.SegmentMaker._attach_metronome_marks(3)
                        - \baca-metronome-mark-spanner-colored-left-text 2 0 1 "112" #'blue          %! EXPLICIT_METRONOME_MARK_WITH_COLOR:baca.SegmentMaker._attach_metronome_marks(3)
                        \bacaStartTextSpanMM                                                         %! EXPLICIT_METRONOME_MARK_WITH_COLOR:baca.SegmentMaker._attach_metronome_marks(3)
            <BLANKLINE>
                        % [Global_Skips measure 2]                                                   %! baca.SegmentMaker._comment_measure_numbers()
                        \baca-new-spacing-section #1 #25                                             %! SPACING_COMMAND:baca.HorizontalSpacingSpecifier.__call__(1)
                        \noBreak                                                                     %! BREAK:baca.BreakMeasureMap.__call__(2)
                        s1 * 3/8                                                                     %! baca.SegmentMaker._make_global_skips(1)
            <BLANKLINE>
                        % [Global_Skips measure 3]                                                   %! baca.SegmentMaker._comment_measure_numbers():baca.SegmentMaker._style_phantom_measures(1):PHANTOM
                        \baca-new-spacing-section #1 #4                                              %! SPACING_COMMAND:baca.HorizontalSpacingSpecifier.__call__(1):baca.SegmentMaker._style_phantom_measures(1):PHANTOM
                        \noBreak                                                                     %! BREAK:baca.BreakMeasureMap.__call__(2):baca.SegmentMaker._style_phantom_measures(1):PHANTOM
                        \time 1/4                                                                    %! baca.SegmentMaker._make_global_skips(3):PHANTOM:baca.SegmentMaker._set_status_tag():EXPLICIT_TIME_SIGNATURE:baca.SegmentMaker._style_phantom_measures(1)
                        \baca-time-signature-transparent                                             %! baca.SegmentMaker._style_phantom_measures(2):PHANTOM
                        s1 * 1/4                                                                     %! baca.SegmentMaker._make_global_skips(3):PHANTOM
                        \bacaStopTextSpanMM                                                          %! EOS_STOP_MM_SPANNER:baca.SegmentMaker._attach_metronome_marks(4):baca.SegmentMaker._style_phantom_measures(1):PHANTOM
                        \once \override Score.BarLine.transparent = ##t                              %! baca.SegmentMaker._style_phantom_measures(3):PHANTOM
                        \once \override Score.SpanBar.transparent = ##t                              %! baca.SegmentMaker._style_phantom_measures(3):PHANTOM
            <BLANKLINE>
                    }                                                                                %! abjad.ScoreTemplate._make_global_context()
            <BLANKLINE>
                >>                                                                                   %! abjad.ScoreTemplate._make_global_context()
            <BLANKLINE>
                \context MusicContext = "Music_Context"                                              %! baca.SingleStaffScoreTemplate.__call__()
                <<                                                                                   %! baca.SingleStaffScoreTemplate.__call__()
            <BLANKLINE>
                    \context Staff = "Music_Staff"                                                   %! baca.SingleStaffScoreTemplate.__call__()
                    {                                                                                %! baca.SingleStaffScoreTemplate.__call__()
            <BLANKLINE>
                        \context Voice = "Music_Voice"                                               %! baca.SingleStaffScoreTemplate.__call__()
                        {                                                                            %! baca.SingleStaffScoreTemplate.__call__()
            <BLANKLINE>
                            % [Music_Voice measure 1]                                                %! baca.SegmentMaker._comment_measure_numbers()
                        %@% \baca-not-yet-pitched-coloring                                           %! baca.SegmentMaker._color_not_yet_pitched():NOT_YET_PITCHED_COLORING
                            b'4.                                                                     %! baca.make_notes()
            <BLANKLINE>
                            % [Music_Voice measure 2]                                                %! baca.SegmentMaker._comment_measure_numbers()
                        %@% \baca-not-yet-pitched-coloring                                           %! baca.SegmentMaker._color_not_yet_pitched():NOT_YET_PITCHED_COLORING
                            b'4.                                                                     %! baca.make_notes()
            <BLANKLINE>
                            <<                                                                       %! baca.SegmentMaker._make_multimeasure_rest_container(7):PHANTOM
            <BLANKLINE>
                                \context Voice = "Music_Voice"                                       %! baca.SegmentMaker._make_multimeasure_rest_container(4):PHANTOM
                                {                                                                    %! baca.SegmentMaker._make_multimeasure_rest_container(4):PHANTOM
            <BLANKLINE>
                                    % [Music_Voice measure 3]                                        %! baca.SegmentMaker._comment_measure_numbers():baca.SegmentMaker._style_phantom_measures(5):PHANTOM
                                    \abjad-invisible-music-coloring                                  %! baca.SegmentMaker._make_multimeasure_rest_container(2):PHANTOM:NOTE:INVISIBLE_MUSIC_COLORING:baca.SegmentMaker._style_phantom_measures(5)
                                %@% \abjad-invisible-music                                           %! baca.SegmentMaker._make_multimeasure_rest_container(3):PHANTOM:NOTE:INVISIBLE_MUSIC_COMMAND:baca.SegmentMaker._style_phantom_measures(5)
                                %@% \baca-not-yet-pitched-coloring                                   %! baca.SegmentMaker._color_not_yet_pitched():NOT_YET_PITCHED_COLORING:HIDDEN:NOTE:baca.SegmentMaker._style_phantom_measures(5):PHANTOM
                                    b'1 * 1/4                                                        %! baca.SegmentMaker._make_multimeasure_rest_container(1):PHANTOM:HIDDEN:NOTE
                                %@% ^ \baca-duration-multiplier-markup #"1" #"4"                     %! baca.SegmentMaker._label_duration_multipliers():DURATION_MULTIPLIER:HIDDEN:NOTE:PHANTOM:baca.SegmentMaker._style_phantom_measures(5)
            <BLANKLINE>
                                }                                                                    %! baca.SegmentMaker._make_multimeasure_rest_container(4):PHANTOM
            <BLANKLINE>
                                \context Voice = "Rest_Voice"                                        %! baca.SegmentMaker._make_multimeasure_rest_container(6):PHANTOM
                                {                                                                    %! baca.SegmentMaker._make_multimeasure_rest_container(6):PHANTOM
            <BLANKLINE>
                                    % [Rest_Voice measure 3]                                         %! baca.SegmentMaker._comment_measure_numbers():baca.SegmentMaker._style_phantom_measures(5):PHANTOM
                                    \once \override Score.TimeSignature.X-extent = ##f               %! baca.SegmentMaker._style_phantom_measures(6):PHANTOM
                                    \once \override MultiMeasureRest.transparent = ##t               %! baca.SegmentMaker._style_phantom_measures(7):PHANTOM
                                    \stopStaff                                                       %! baca.SegmentMaker._style_phantom_measures(8):PHANTOM
                                    \once \override Staff.StaffSymbol.transparent = ##t              %! baca.SegmentMaker._style_phantom_measures(8):PHANTOM
                                    \startStaff                                                      %! baca.SegmentMaker._style_phantom_measures(8):PHANTOM
                                    R1 * 1/4                                                         %! baca.SegmentMaker._make_multimeasure_rest_container(5):PHANTOM:REST_VOICE:MULTIMEASURE_REST
                                %@% ^ \baca-duration-multiplier-markup #"1" #"4"                     %! baca.SegmentMaker._label_duration_multipliers():DURATION_MULTIPLIER:MULTIMEASURE_REST:PHANTOM:REST_VOICE:baca.SegmentMaker._style_phantom_measures(5)
            <BLANKLINE>
                                }                                                                    %! baca.SegmentMaker._make_multimeasure_rest_container(6):PHANTOM
            <BLANKLINE>
                            >>                                                                       %! baca.SegmentMaker._make_multimeasure_rest_container(7):PHANTOM
            <BLANKLINE>
                        }                                                                            %! baca.SingleStaffScoreTemplate.__call__()
            <BLANKLINE>
                    }                                                                                %! baca.SingleStaffScoreTemplate.__call__()
            <BLANKLINE>
                >>                                                                                   %! baca.SingleStaffScoreTemplate.__call__()
            <BLANKLINE>
            >>                                                                                       %! baca.SingleStaffScoreTemplate.__call__()

        Even after a previous metronome mark:

        >>> maker = baca.SegmentMaker(
        ...     breaks=breaks,
        ...     deactivate=[abjad.tags.NOT_YET_PITCHED_COLORING],
        ...     metronome_marks=metronome_marks,
        ...     score_template=baca.SingleStaffScoreTemplate(),
        ...     spacing=baca.minimum_duration((1, 24)),
        ...     time_signatures=[(3, 8), (3, 8)],
        ...     )
        >>> maker(
        ...     'Global_Skips',
        ...     baca.metronome_mark('112'),
        ...     baca.text_spanner_staff_padding(4),
        ...     )
        >>> maker(
        ...     'Music_Voice',
        ...     baca.make_notes(),
        ...     )

        >>> metadata, persist = {}, {}
        >>> persist['persistent_indicators'] = {}
        >>> persist['persistent_indicators']['Score'] = [
        ...     abjad.Momento(
        ...         context='Global_Skips',
        ...         manifest='metronome_marks',
        ...         value='90',
        ...         )
        ...     ]
        >>> metadata['segment_number'] = 1
        >>> lilypond_file = maker.run(
        ...     environment='docs',
        ...     previous_metadata=metadata,
        ...     previous_persist=persist,
        ...     )
        >>> block = abjad.Block(name='layout')
        >>> block.indent = 0
        >>> lilypond_file.items.insert(0, block)
        >>> abjad.show(lilypond_file, strict=89) # doctest: +SKIP

        ..  docs::

            >>> abjad.f(lilypond_file[abjad.Score], strict=89)
            <BLANKLINE>
            \context Score = "Score"                                                                 %! baca.SingleStaffScoreTemplate.__call__()
            <<                                                                                       %! baca.SingleStaffScoreTemplate.__call__()
            <BLANKLINE>
                \context GlobalContext = "Global_Context"                                            %! abjad.ScoreTemplate._make_global_context()
                <<                                                                                   %! abjad.ScoreTemplate._make_global_context()
            <BLANKLINE>
                    \context GlobalSkips = "Global_Skips"                                            %! abjad.ScoreTemplate._make_global_context()
                    {                                                                                %! abjad.ScoreTemplate._make_global_context()
            <BLANKLINE>
                        % [Global_Skips measure 1]                                                   %! baca.SegmentMaker._comment_measure_numbers()
                        \baca-new-spacing-section #1 #24                                             %! SPACING_COMMAND:baca.HorizontalSpacingSpecifier.__call__(1)
                        \override TextSpanner.staff-padding = #4                                     %! baca.text_spanner_staff_padding():baca.OverrideCommand._call(1)
                        \autoPageBreaksOff                                                           %! BREAK:baca.BreakMeasureMap.__call__(1)
                        \noBreak                                                                     %! BREAK:baca.BreakMeasureMap.__call__(2)
                        \baca-lbsd #4 #'(8)                                                          %! BREAK:baca.IndicatorCommand._call()
                        \time 3/8                                                                    %! baca.SegmentMaker._make_global_skips(2):baca.SegmentMaker._set_status_tag():EXPLICIT_TIME_SIGNATURE
                        \bar ""                                                                      %! EMPTY_START_BAR:+SEGMENT:baca.SegmentMaker._make_global_skips(4)
                        \baca-time-signature-color #'blue                                            %! baca.SegmentMaker._attach_color_literal(2):EXPLICIT_TIME_SIGNATURE_COLOR
                        \pageBreak                                                                   %! BREAK:baca.IndicatorCommand._call()
                        s1 * 3/8                                                                     %! baca.SegmentMaker._make_global_skips(1)
                    %@% - \abjad-invisible-line                                                      %! baca.SegmentMaker._set_status_tag():EXPLICIT_METRONOME_MARK:baca.SegmentMaker._attach_metronome_marks(2)
                    %@% - \baca-metronome-mark-spanner-left-text 2 0 1 "112"                         %! baca.SegmentMaker._set_status_tag():EXPLICIT_METRONOME_MARK:baca.SegmentMaker._attach_metronome_marks(2)
                    %@% \bacaStartTextSpanMM                                                         %! baca.SegmentMaker._set_status_tag():EXPLICIT_METRONOME_MARK:baca.SegmentMaker._attach_metronome_marks(2)
                        - \abjad-invisible-line                                                      %! EXPLICIT_METRONOME_MARK_WITH_COLOR:baca.SegmentMaker._attach_metronome_marks(3)
                        - \baca-metronome-mark-spanner-colored-left-text 2 0 1 "112" #'blue          %! EXPLICIT_METRONOME_MARK_WITH_COLOR:baca.SegmentMaker._attach_metronome_marks(3)
                        \bacaStartTextSpanMM                                                         %! EXPLICIT_METRONOME_MARK_WITH_COLOR:baca.SegmentMaker._attach_metronome_marks(3)
            <BLANKLINE>
                        % [Global_Skips measure 2]                                                   %! baca.SegmentMaker._comment_measure_numbers()
                        \baca-new-spacing-section #1 #24                                             %! SPACING_COMMAND:baca.HorizontalSpacingSpecifier.__call__(1)
                        \noBreak                                                                     %! BREAK:baca.BreakMeasureMap.__call__(2)
                        s1 * 3/8                                                                     %! baca.SegmentMaker._make_global_skips(1)
                        \revert TextSpanner.staff-padding                                            %! baca.text_spanner_staff_padding():baca.OverrideCommand._call(2)
            <BLANKLINE>
                        % [Global_Skips measure 3]                                                   %! baca.SegmentMaker._comment_measure_numbers():baca.SegmentMaker._style_phantom_measures(1):PHANTOM
                        \baca-new-spacing-section #1 #4                                              %! SPACING_COMMAND:baca.HorizontalSpacingSpecifier.__call__(1):baca.SegmentMaker._style_phantom_measures(1):PHANTOM
                        \noBreak                                                                     %! BREAK:baca.BreakMeasureMap.__call__(2):baca.SegmentMaker._style_phantom_measures(1):PHANTOM
                        \time 1/4                                                                    %! baca.SegmentMaker._make_global_skips(3):PHANTOM:baca.SegmentMaker._set_status_tag():EXPLICIT_TIME_SIGNATURE:baca.SegmentMaker._style_phantom_measures(1)
                        \baca-time-signature-transparent                                             %! baca.SegmentMaker._style_phantom_measures(2):PHANTOM
                        s1 * 1/4                                                                     %! baca.SegmentMaker._make_global_skips(3):PHANTOM
                        \bacaStopTextSpanMM                                                          %! EOS_STOP_MM_SPANNER:baca.SegmentMaker._attach_metronome_marks(4):baca.SegmentMaker._style_phantom_measures(1):PHANTOM
                        \once \override Score.BarLine.transparent = ##t                              %! baca.SegmentMaker._style_phantom_measures(3):PHANTOM
                        \once \override Score.SpanBar.transparent = ##t                              %! baca.SegmentMaker._style_phantom_measures(3):PHANTOM
            <BLANKLINE>
                    }                                                                                %! abjad.ScoreTemplate._make_global_context()
            <BLANKLINE>
                >>                                                                                   %! abjad.ScoreTemplate._make_global_context()
            <BLANKLINE>
                \context MusicContext = "Music_Context"                                              %! baca.SingleStaffScoreTemplate.__call__()
                <<                                                                                   %! baca.SingleStaffScoreTemplate.__call__()
            <BLANKLINE>
                    \context Staff = "Music_Staff"                                                   %! baca.SingleStaffScoreTemplate.__call__()
                    {                                                                                %! baca.SingleStaffScoreTemplate.__call__()
            <BLANKLINE>
                        \context Voice = "Music_Voice"                                               %! baca.SingleStaffScoreTemplate.__call__()
                        {                                                                            %! baca.SingleStaffScoreTemplate.__call__()
            <BLANKLINE>
                            % [Music_Voice measure 1]                                                %! baca.SegmentMaker._comment_measure_numbers()
                        %@% \baca-not-yet-pitched-coloring                                           %! baca.SegmentMaker._color_not_yet_pitched():NOT_YET_PITCHED_COLORING
                            b'4.                                                                     %! baca.make_notes()
            <BLANKLINE>
                            % [Music_Voice measure 2]                                                %! baca.SegmentMaker._comment_measure_numbers()
                        %@% \baca-not-yet-pitched-coloring                                           %! baca.SegmentMaker._color_not_yet_pitched():NOT_YET_PITCHED_COLORING
                            b'4.                                                                     %! baca.make_notes()
            <BLANKLINE>
                            <<                                                                       %! baca.SegmentMaker._make_multimeasure_rest_container(7):PHANTOM
            <BLANKLINE>
                                \context Voice = "Music_Voice"                                       %! baca.SegmentMaker._make_multimeasure_rest_container(4):PHANTOM
                                {                                                                    %! baca.SegmentMaker._make_multimeasure_rest_container(4):PHANTOM
            <BLANKLINE>
                                    % [Music_Voice measure 3]                                        %! baca.SegmentMaker._comment_measure_numbers():baca.SegmentMaker._style_phantom_measures(5):PHANTOM
                                    \abjad-invisible-music-coloring                                  %! baca.SegmentMaker._make_multimeasure_rest_container(2):PHANTOM:NOTE:INVISIBLE_MUSIC_COLORING:baca.SegmentMaker._style_phantom_measures(5)
                                %@% \abjad-invisible-music                                           %! baca.SegmentMaker._make_multimeasure_rest_container(3):PHANTOM:NOTE:INVISIBLE_MUSIC_COMMAND:baca.SegmentMaker._style_phantom_measures(5)
                                %@% \baca-not-yet-pitched-coloring                                   %! baca.SegmentMaker._color_not_yet_pitched():NOT_YET_PITCHED_COLORING:HIDDEN:NOTE:baca.SegmentMaker._style_phantom_measures(5):PHANTOM
                                    b'1 * 1/4                                                        %! baca.SegmentMaker._make_multimeasure_rest_container(1):PHANTOM:HIDDEN:NOTE
                                %@% ^ \baca-duration-multiplier-markup #"1" #"4"                     %! baca.SegmentMaker._label_duration_multipliers():DURATION_MULTIPLIER:HIDDEN:NOTE:PHANTOM:baca.SegmentMaker._style_phantom_measures(5)
            <BLANKLINE>
                                }                                                                    %! baca.SegmentMaker._make_multimeasure_rest_container(4):PHANTOM
            <BLANKLINE>
                                \context Voice = "Rest_Voice"                                        %! baca.SegmentMaker._make_multimeasure_rest_container(6):PHANTOM
                                {                                                                    %! baca.SegmentMaker._make_multimeasure_rest_container(6):PHANTOM
            <BLANKLINE>
                                    % [Rest_Voice measure 3]                                         %! baca.SegmentMaker._comment_measure_numbers():baca.SegmentMaker._style_phantom_measures(5):PHANTOM
                                    \once \override Score.TimeSignature.X-extent = ##f               %! baca.SegmentMaker._style_phantom_measures(6):PHANTOM
                                    \once \override MultiMeasureRest.transparent = ##t               %! baca.SegmentMaker._style_phantom_measures(7):PHANTOM
                                    \stopStaff                                                       %! baca.SegmentMaker._style_phantom_measures(8):PHANTOM
                                    \once \override Staff.StaffSymbol.transparent = ##t              %! baca.SegmentMaker._style_phantom_measures(8):PHANTOM
                                    \startStaff                                                      %! baca.SegmentMaker._style_phantom_measures(8):PHANTOM
                                    R1 * 1/4                                                         %! baca.SegmentMaker._make_multimeasure_rest_container(5):PHANTOM:REST_VOICE:MULTIMEASURE_REST
                                %@% ^ \baca-duration-multiplier-markup #"1" #"4"                     %! baca.SegmentMaker._label_duration_multipliers():DURATION_MULTIPLIER:MULTIMEASURE_REST:PHANTOM:REST_VOICE:baca.SegmentMaker._style_phantom_measures(5)
            <BLANKLINE>
                                }                                                                    %! baca.SegmentMaker._make_multimeasure_rest_container(6):PHANTOM
            <BLANKLINE>
                            >>                                                                       %! baca.SegmentMaker._make_multimeasure_rest_container(7):PHANTOM
            <BLANKLINE>
                        }                                                                            %! baca.SingleStaffScoreTemplate.__call__()
            <BLANKLINE>
                    }                                                                                %! baca.SingleStaffScoreTemplate.__call__()
            <BLANKLINE>
                >>                                                                                   %! baca.SingleStaffScoreTemplate.__call__()
            <BLANKLINE>
            >>                                                                                       %! baca.SingleStaffScoreTemplate.__call__()

    ..  container:: example

        Reapplied metronome marks color green:

        >>> maker = baca.SegmentMaker(
        ...     breaks=breaks,
        ...     deactivate=[abjad.tags.NOT_YET_PITCHED_COLORING],
        ...     metronome_marks=metronome_marks,
        ...     score_template=baca.SingleStaffScoreTemplate(),
        ...     spacing=baca.minimum_duration((1, 24)),
        ...     time_signatures=[(3, 8), (3, 8)],
        ...     )
        >>> maker(
        ...     'Music_Voice',
        ...     baca.make_notes(),
        ...     )
        >>> maker(
        ...     'Global_Skips',
        ...     baca.text_spanner_staff_padding(4),
        ...     )

        >>> metadata, persist = {}, {}
        >>> persist['persistent_indicators'] = {}
        >>> persist['persistent_indicators']['Score'] = [
        ...     abjad.Momento(
        ...         context='Global_Skips',
        ...         manifest='metronome_marks',
        ...         value='90',
        ...         )
        ...     ]
        >>> metadata['segment_number'] = 1
        >>> lilypond_file = maker.run(
        ...     environment='docs',
        ...     previous_metadata=metadata,
        ...     previous_persist=persist,
        ...     )
        >>> block = abjad.Block(name='layout')
        >>> block.indent = 0
        >>> lilypond_file.items.insert(0, block)
        >>> abjad.show(lilypond_file, strict=89) # doctest: +SKIP

        ..  docs::

            >>> abjad.f(lilypond_file[abjad.Score], strict=89)
            <BLANKLINE>
            \context Score = "Score"                                                                 %! baca.SingleStaffScoreTemplate.__call__()
            <<                                                                                       %! baca.SingleStaffScoreTemplate.__call__()
            <BLANKLINE>
                \context GlobalContext = "Global_Context"                                            %! abjad.ScoreTemplate._make_global_context()
                <<                                                                                   %! abjad.ScoreTemplate._make_global_context()
            <BLANKLINE>
                    \context GlobalSkips = "Global_Skips"                                            %! abjad.ScoreTemplate._make_global_context()
                    {                                                                                %! abjad.ScoreTemplate._make_global_context()
            <BLANKLINE>
                        % [Global_Skips measure 1]                                                   %! baca.SegmentMaker._comment_measure_numbers()
                        \baca-new-spacing-section #1 #24                                             %! SPACING_COMMAND:baca.HorizontalSpacingSpecifier.__call__(1)
                        \override TextSpanner.staff-padding = #4                                     %! baca.text_spanner_staff_padding():baca.OverrideCommand._call(1)
                        \autoPageBreaksOff                                                           %! BREAK:baca.BreakMeasureMap.__call__(1)
                        \noBreak                                                                     %! BREAK:baca.BreakMeasureMap.__call__(2)
                        \baca-lbsd #4 #'(8)                                                          %! BREAK:baca.IndicatorCommand._call()
                        \time 3/8                                                                    %! baca.SegmentMaker._make_global_skips(2):baca.SegmentMaker._set_status_tag():EXPLICIT_TIME_SIGNATURE
                        \bar ""                                                                      %! EMPTY_START_BAR:+SEGMENT:baca.SegmentMaker._make_global_skips(4)
                        \baca-time-signature-color #'blue                                            %! baca.SegmentMaker._attach_color_literal(2):EXPLICIT_TIME_SIGNATURE_COLOR
                        \pageBreak                                                                   %! BREAK:baca.IndicatorCommand._call()
                        s1 * 3/8                                                                     %! baca.SegmentMaker._make_global_skips(1)
                    %@% - \abjad-invisible-line                                                      %! baca.SegmentMaker._reapply_persistent_indicators(2):baca.SegmentMaker._set_status_tag():REAPPLIED_METRONOME_MARK:baca.SegmentMaker._attach_metronome_marks(2)
                    %@% - \baca-metronome-mark-spanner-left-text 2 0 1 "90"                          %! baca.SegmentMaker._reapply_persistent_indicators(2):baca.SegmentMaker._set_status_tag():REAPPLIED_METRONOME_MARK:baca.SegmentMaker._attach_metronome_marks(2)
                    %@% \bacaStartTextSpanMM                                                         %! baca.SegmentMaker._reapply_persistent_indicators(2):baca.SegmentMaker._set_status_tag():REAPPLIED_METRONOME_MARK:baca.SegmentMaker._attach_metronome_marks(2)
                        - \abjad-invisible-line                                                      %! REAPPLIED_METRONOME_MARK_WITH_COLOR:baca.SegmentMaker._attach_metronome_marks(3)
                        - \baca-metronome-mark-spanner-colored-left-text 2 0 1 "90" #'green4         %! REAPPLIED_METRONOME_MARK_WITH_COLOR:baca.SegmentMaker._attach_metronome_marks(3)
                        \bacaStartTextSpanMM                                                         %! REAPPLIED_METRONOME_MARK_WITH_COLOR:baca.SegmentMaker._attach_metronome_marks(3)
            <BLANKLINE>
                        % [Global_Skips measure 2]                                                   %! baca.SegmentMaker._comment_measure_numbers()
                        \baca-new-spacing-section #1 #24                                             %! SPACING_COMMAND:baca.HorizontalSpacingSpecifier.__call__(1)
                        \noBreak                                                                     %! BREAK:baca.BreakMeasureMap.__call__(2)
                        s1 * 3/8                                                                     %! baca.SegmentMaker._make_global_skips(1)
                        \revert TextSpanner.staff-padding                                            %! baca.text_spanner_staff_padding():baca.OverrideCommand._call(2)
            <BLANKLINE>
                        % [Global_Skips measure 3]                                                   %! baca.SegmentMaker._comment_measure_numbers():baca.SegmentMaker._style_phantom_measures(1):PHANTOM
                        \baca-new-spacing-section #1 #4                                              %! SPACING_COMMAND:baca.HorizontalSpacingSpecifier.__call__(1):baca.SegmentMaker._style_phantom_measures(1):PHANTOM
                        \noBreak                                                                     %! BREAK:baca.BreakMeasureMap.__call__(2):baca.SegmentMaker._style_phantom_measures(1):PHANTOM
                        \time 1/4                                                                    %! baca.SegmentMaker._make_global_skips(3):PHANTOM:baca.SegmentMaker._set_status_tag():EXPLICIT_TIME_SIGNATURE:baca.SegmentMaker._style_phantom_measures(1)
                        \baca-time-signature-transparent                                             %! baca.SegmentMaker._style_phantom_measures(2):PHANTOM
                        s1 * 1/4                                                                     %! baca.SegmentMaker._make_global_skips(3):PHANTOM
                        \bacaStopTextSpanMM                                                          %! EOS_STOP_MM_SPANNER:baca.SegmentMaker._attach_metronome_marks(4):baca.SegmentMaker._style_phantom_measures(1):PHANTOM
                        \once \override Score.BarLine.transparent = ##t                              %! baca.SegmentMaker._style_phantom_measures(3):PHANTOM
                        \once \override Score.SpanBar.transparent = ##t                              %! baca.SegmentMaker._style_phantom_measures(3):PHANTOM
            <BLANKLINE>
                    }                                                                                %! abjad.ScoreTemplate._make_global_context()
            <BLANKLINE>
                >>                                                                                   %! abjad.ScoreTemplate._make_global_context()
            <BLANKLINE>
                \context MusicContext = "Music_Context"                                              %! baca.SingleStaffScoreTemplate.__call__()
                <<                                                                                   %! baca.SingleStaffScoreTemplate.__call__()
            <BLANKLINE>
                    \context Staff = "Music_Staff"                                                   %! baca.SingleStaffScoreTemplate.__call__()
                    {                                                                                %! baca.SingleStaffScoreTemplate.__call__()
            <BLANKLINE>
                        \context Voice = "Music_Voice"                                               %! baca.SingleStaffScoreTemplate.__call__()
                        {                                                                            %! baca.SingleStaffScoreTemplate.__call__()
            <BLANKLINE>
                            % [Music_Voice measure 1]                                                %! baca.SegmentMaker._comment_measure_numbers()
                        %@% \baca-not-yet-pitched-coloring                                           %! baca.SegmentMaker._color_not_yet_pitched():NOT_YET_PITCHED_COLORING
                            b'4.                                                                     %! baca.make_notes()
            <BLANKLINE>
                            % [Music_Voice measure 2]                                                %! baca.SegmentMaker._comment_measure_numbers()
                        %@% \baca-not-yet-pitched-coloring                                           %! baca.SegmentMaker._color_not_yet_pitched():NOT_YET_PITCHED_COLORING
                            b'4.                                                                     %! baca.make_notes()
            <BLANKLINE>
                            <<                                                                       %! baca.SegmentMaker._make_multimeasure_rest_container(7):PHANTOM
            <BLANKLINE>
                                \context Voice = "Music_Voice"                                       %! baca.SegmentMaker._make_multimeasure_rest_container(4):PHANTOM
                                {                                                                    %! baca.SegmentMaker._make_multimeasure_rest_container(4):PHANTOM
            <BLANKLINE>
                                    % [Music_Voice measure 3]                                        %! baca.SegmentMaker._comment_measure_numbers():baca.SegmentMaker._style_phantom_measures(5):PHANTOM
                                    \abjad-invisible-music-coloring                                  %! baca.SegmentMaker._make_multimeasure_rest_container(2):PHANTOM:NOTE:INVISIBLE_MUSIC_COLORING:baca.SegmentMaker._style_phantom_measures(5)
                                %@% \abjad-invisible-music                                           %! baca.SegmentMaker._make_multimeasure_rest_container(3):PHANTOM:NOTE:INVISIBLE_MUSIC_COMMAND:baca.SegmentMaker._style_phantom_measures(5)
                                %@% \baca-not-yet-pitched-coloring                                   %! baca.SegmentMaker._color_not_yet_pitched():NOT_YET_PITCHED_COLORING:HIDDEN:NOTE:baca.SegmentMaker._style_phantom_measures(5):PHANTOM
                                    b'1 * 1/4                                                        %! baca.SegmentMaker._make_multimeasure_rest_container(1):PHANTOM:HIDDEN:NOTE
                                %@% ^ \baca-duration-multiplier-markup #"1" #"4"                     %! baca.SegmentMaker._label_duration_multipliers():DURATION_MULTIPLIER:HIDDEN:NOTE:PHANTOM:baca.SegmentMaker._style_phantom_measures(5)
            <BLANKLINE>
                                }                                                                    %! baca.SegmentMaker._make_multimeasure_rest_container(4):PHANTOM
            <BLANKLINE>
                                \context Voice = "Rest_Voice"                                        %! baca.SegmentMaker._make_multimeasure_rest_container(6):PHANTOM
                                {                                                                    %! baca.SegmentMaker._make_multimeasure_rest_container(6):PHANTOM
            <BLANKLINE>
                                    % [Rest_Voice measure 3]                                         %! baca.SegmentMaker._comment_measure_numbers():baca.SegmentMaker._style_phantom_measures(5):PHANTOM
                                    \once \override Score.TimeSignature.X-extent = ##f               %! baca.SegmentMaker._style_phantom_measures(6):PHANTOM
                                    \once \override MultiMeasureRest.transparent = ##t               %! baca.SegmentMaker._style_phantom_measures(7):PHANTOM
                                    \stopStaff                                                       %! baca.SegmentMaker._style_phantom_measures(8):PHANTOM
                                    \once \override Staff.StaffSymbol.transparent = ##t              %! baca.SegmentMaker._style_phantom_measures(8):PHANTOM
                                    \startStaff                                                      %! baca.SegmentMaker._style_phantom_measures(8):PHANTOM
                                    R1 * 1/4                                                         %! baca.SegmentMaker._make_multimeasure_rest_container(5):PHANTOM:REST_VOICE:MULTIMEASURE_REST
                                %@% ^ \baca-duration-multiplier-markup #"1" #"4"                     %! baca.SegmentMaker._label_duration_multipliers():DURATION_MULTIPLIER:MULTIMEASURE_REST:PHANTOM:REST_VOICE:baca.SegmentMaker._style_phantom_measures(5)
            <BLANKLINE>
                                }                                                                    %! baca.SegmentMaker._make_multimeasure_rest_container(6):PHANTOM
            <BLANKLINE>
                            >>                                                                       %! baca.SegmentMaker._make_multimeasure_rest_container(7):PHANTOM
            <BLANKLINE>
                        }                                                                            %! baca.SingleStaffScoreTemplate.__call__()
            <BLANKLINE>
                    }                                                                                %! baca.SingleStaffScoreTemplate.__call__()
            <BLANKLINE>
                >>                                                                                   %! baca.SingleStaffScoreTemplate.__call__()
            <BLANKLINE>
            >>                                                                                       %! baca.SingleStaffScoreTemplate.__call__()

    ..  container:: example

        Redundant metronome marks color pink:

        >>> maker = baca.SegmentMaker(
        ...     breaks=breaks,
        ...     deactivate=[abjad.tags.NOT_YET_PITCHED_COLORING],
        ...     metronome_marks=metronome_marks,
        ...     score_template=baca.SingleStaffScoreTemplate(),
        ...     spacing=baca.minimum_duration((1, 24)),
        ...     time_signatures=[(3, 8), (3, 8)],
        ...     )
        >>> maker(
        ...     'Global_Skips',
        ...     baca.metronome_mark('112'),
        ...     baca.metronome_mark('112', selector=baca.leaf(1)),
        ...     )
        >>> maker(
        ...     'Music_Voice',
        ...     baca.make_notes(),
        ...     )

        >>> lilypond_file = maker.run(environment='docs')
        >>> block = abjad.Block(name='layout')
        >>> block.indent = 0
        >>> lilypond_file.items.insert(0, block)
        >>> abjad.show(lilypond_file, strict=89) # doctest: +SKIP

        ..  docs::

            >>> abjad.f(lilypond_file[abjad.Score], strict=89)
            <BLANKLINE>
            \context Score = "Score"                                                                 %! baca.SingleStaffScoreTemplate.__call__()
            <<                                                                                       %! baca.SingleStaffScoreTemplate.__call__()
            <BLANKLINE>
                \context GlobalContext = "Global_Context"                                            %! abjad.ScoreTemplate._make_global_context()
                <<                                                                                   %! abjad.ScoreTemplate._make_global_context()
            <BLANKLINE>
                    \context GlobalSkips = "Global_Skips"                                            %! abjad.ScoreTemplate._make_global_context()
                    {                                                                                %! abjad.ScoreTemplate._make_global_context()
            <BLANKLINE>
                        % [Global_Skips measure 1]                                                   %! baca.SegmentMaker._comment_measure_numbers()
                        \baca-new-spacing-section #1 #24                                             %! SPACING_COMMAND:baca.HorizontalSpacingSpecifier.__call__(1)
                        \autoPageBreaksOff                                                           %! BREAK:baca.BreakMeasureMap.__call__(1)
                        \noBreak                                                                     %! BREAK:baca.BreakMeasureMap.__call__(2)
                        \baca-lbsd #4 #'(8)                                                          %! BREAK:baca.IndicatorCommand._call()
                        \time 3/8                                                                    %! baca.SegmentMaker._make_global_skips(2):baca.SegmentMaker._set_status_tag():EXPLICIT_TIME_SIGNATURE
                        \baca-time-signature-color #'blue                                            %! baca.SegmentMaker._attach_color_literal(2):EXPLICIT_TIME_SIGNATURE_COLOR
                        \pageBreak                                                                   %! BREAK:baca.IndicatorCommand._call()
                        s1 * 3/8                                                                     %! baca.SegmentMaker._make_global_skips(1)
                    %@% - \abjad-invisible-line                                                      %! baca.SegmentMaker._set_status_tag():EXPLICIT_METRONOME_MARK:baca.SegmentMaker._attach_metronome_marks(2)
                    %@% - \baca-metronome-mark-spanner-left-text 2 0 1 "112"                         %! baca.SegmentMaker._set_status_tag():EXPLICIT_METRONOME_MARK:baca.SegmentMaker._attach_metronome_marks(2)
                    %@% \bacaStartTextSpanMM                                                         %! baca.SegmentMaker._set_status_tag():EXPLICIT_METRONOME_MARK:baca.SegmentMaker._attach_metronome_marks(2)
                        - \abjad-invisible-line                                                      %! EXPLICIT_METRONOME_MARK_WITH_COLOR:baca.SegmentMaker._attach_metronome_marks(3)
                        - \baca-metronome-mark-spanner-colored-left-text 2 0 1 "112" #'blue          %! EXPLICIT_METRONOME_MARK_WITH_COLOR:baca.SegmentMaker._attach_metronome_marks(3)
                        \bacaStartTextSpanMM                                                         %! EXPLICIT_METRONOME_MARK_WITH_COLOR:baca.SegmentMaker._attach_metronome_marks(3)
            <BLANKLINE>
                        % [Global_Skips measure 2]                                                   %! baca.SegmentMaker._comment_measure_numbers()
                        \baca-new-spacing-section #1 #24                                             %! SPACING_COMMAND:baca.HorizontalSpacingSpecifier.__call__(1)
                        \noBreak                                                                     %! BREAK:baca.BreakMeasureMap.__call__(2)
                        s1 * 3/8                                                                     %! baca.SegmentMaker._make_global_skips(1)
                        \bacaStopTextSpanMM                                                          %! baca.SegmentMaker._attach_metronome_marks(1)
                    %@% - \abjad-invisible-line                                                      %! baca.SegmentMaker._set_status_tag():REDUNDANT_METRONOME_MARK:baca.SegmentMaker._attach_metronome_marks(2)
                    %@% - \baca-metronome-mark-spanner-left-text 2 0 1 "112"                         %! baca.SegmentMaker._set_status_tag():REDUNDANT_METRONOME_MARK:baca.SegmentMaker._attach_metronome_marks(2)
                    %@% \bacaStartTextSpanMM                                                         %! baca.SegmentMaker._set_status_tag():REDUNDANT_METRONOME_MARK:baca.SegmentMaker._attach_metronome_marks(2)
                        - \abjad-invisible-line                                                      %! REDUNDANT_METRONOME_MARK_WITH_COLOR:baca.SegmentMaker._attach_metronome_marks(3)
                        - \baca-metronome-mark-spanner-colored-left-text 2 0 1 "112" #'DeepPink1     %! REDUNDANT_METRONOME_MARK_WITH_COLOR:baca.SegmentMaker._attach_metronome_marks(3)
                        \bacaStartTextSpanMM                                                         %! REDUNDANT_METRONOME_MARK_WITH_COLOR:baca.SegmentMaker._attach_metronome_marks(3)
            <BLANKLINE>
                        % [Global_Skips measure 3]                                                   %! baca.SegmentMaker._comment_measure_numbers():baca.SegmentMaker._style_phantom_measures(1):PHANTOM
                        \baca-new-spacing-section #1 #4                                              %! SPACING_COMMAND:baca.HorizontalSpacingSpecifier.__call__(1):baca.SegmentMaker._style_phantom_measures(1):PHANTOM
                        \noBreak                                                                     %! BREAK:baca.BreakMeasureMap.__call__(2):baca.SegmentMaker._style_phantom_measures(1):PHANTOM
                        \time 1/4                                                                    %! baca.SegmentMaker._make_global_skips(3):PHANTOM:baca.SegmentMaker._set_status_tag():EXPLICIT_TIME_SIGNATURE:baca.SegmentMaker._style_phantom_measures(1)
                        \baca-time-signature-transparent                                             %! baca.SegmentMaker._style_phantom_measures(2):PHANTOM
                        s1 * 1/4                                                                     %! baca.SegmentMaker._make_global_skips(3):PHANTOM
                        \bacaStopTextSpanMM                                                          %! EOS_STOP_MM_SPANNER:baca.SegmentMaker._attach_metronome_marks(4):baca.SegmentMaker._style_phantom_measures(1):PHANTOM
                        \once \override Score.BarLine.transparent = ##t                              %! baca.SegmentMaker._style_phantom_measures(3):PHANTOM
                        \once \override Score.SpanBar.transparent = ##t                              %! baca.SegmentMaker._style_phantom_measures(3):PHANTOM
            <BLANKLINE>
                    }                                                                                %! abjad.ScoreTemplate._make_global_context()
            <BLANKLINE>
                >>                                                                                   %! abjad.ScoreTemplate._make_global_context()
            <BLANKLINE>
                \context MusicContext = "Music_Context"                                              %! baca.SingleStaffScoreTemplate.__call__()
                <<                                                                                   %! baca.SingleStaffScoreTemplate.__call__()
            <BLANKLINE>
                    \context Staff = "Music_Staff"                                                   %! baca.SingleStaffScoreTemplate.__call__()
                    {                                                                                %! baca.SingleStaffScoreTemplate.__call__()
            <BLANKLINE>
                        \context Voice = "Music_Voice"                                               %! baca.SingleStaffScoreTemplate.__call__()
                        {                                                                            %! baca.SingleStaffScoreTemplate.__call__()
            <BLANKLINE>
                            % [Music_Voice measure 1]                                                %! baca.SegmentMaker._comment_measure_numbers()
                        %@% \baca-not-yet-pitched-coloring                                           %! baca.SegmentMaker._color_not_yet_pitched():NOT_YET_PITCHED_COLORING
                            b'4.                                                                     %! baca.make_notes()
            <BLANKLINE>
                            % [Music_Voice measure 2]                                                %! baca.SegmentMaker._comment_measure_numbers()
                        %@% \baca-not-yet-pitched-coloring                                           %! baca.SegmentMaker._color_not_yet_pitched():NOT_YET_PITCHED_COLORING
                            b'4.                                                                     %! baca.make_notes()
            <BLANKLINE>
                            <<                                                                       %! baca.SegmentMaker._make_multimeasure_rest_container(7):PHANTOM
            <BLANKLINE>
                                \context Voice = "Music_Voice"                                       %! baca.SegmentMaker._make_multimeasure_rest_container(4):PHANTOM
                                {                                                                    %! baca.SegmentMaker._make_multimeasure_rest_container(4):PHANTOM
            <BLANKLINE>
                                    % [Music_Voice measure 3]                                        %! baca.SegmentMaker._comment_measure_numbers():baca.SegmentMaker._style_phantom_measures(5):PHANTOM
                                    \abjad-invisible-music-coloring                                  %! baca.SegmentMaker._make_multimeasure_rest_container(2):PHANTOM:NOTE:INVISIBLE_MUSIC_COLORING:baca.SegmentMaker._style_phantom_measures(5)
                                %@% \abjad-invisible-music                                           %! baca.SegmentMaker._make_multimeasure_rest_container(3):PHANTOM:NOTE:INVISIBLE_MUSIC_COMMAND:baca.SegmentMaker._style_phantom_measures(5)
                                %@% \baca-not-yet-pitched-coloring                                   %! baca.SegmentMaker._color_not_yet_pitched():NOT_YET_PITCHED_COLORING:HIDDEN:NOTE:baca.SegmentMaker._style_phantom_measures(5):PHANTOM
                                    b'1 * 1/4                                                        %! baca.SegmentMaker._make_multimeasure_rest_container(1):PHANTOM:HIDDEN:NOTE
                                %@% ^ \baca-duration-multiplier-markup #"1" #"4"                     %! baca.SegmentMaker._label_duration_multipliers():DURATION_MULTIPLIER:HIDDEN:NOTE:PHANTOM:baca.SegmentMaker._style_phantom_measures(5)
            <BLANKLINE>
                                }                                                                    %! baca.SegmentMaker._make_multimeasure_rest_container(4):PHANTOM
            <BLANKLINE>
                                \context Voice = "Rest_Voice"                                        %! baca.SegmentMaker._make_multimeasure_rest_container(6):PHANTOM
                                {                                                                    %! baca.SegmentMaker._make_multimeasure_rest_container(6):PHANTOM
            <BLANKLINE>
                                    % [Rest_Voice measure 3]                                         %! baca.SegmentMaker._comment_measure_numbers():baca.SegmentMaker._style_phantom_measures(5):PHANTOM
                                    \once \override Score.TimeSignature.X-extent = ##f               %! baca.SegmentMaker._style_phantom_measures(6):PHANTOM
                                    \once \override MultiMeasureRest.transparent = ##t               %! baca.SegmentMaker._style_phantom_measures(7):PHANTOM
                                    \stopStaff                                                       %! baca.SegmentMaker._style_phantom_measures(8):PHANTOM
                                    \once \override Staff.StaffSymbol.transparent = ##t              %! baca.SegmentMaker._style_phantom_measures(8):PHANTOM
                                    \startStaff                                                      %! baca.SegmentMaker._style_phantom_measures(8):PHANTOM
                                    R1 * 1/4                                                         %! baca.SegmentMaker._make_multimeasure_rest_container(5):PHANTOM:REST_VOICE:MULTIMEASURE_REST
                                %@% ^ \baca-duration-multiplier-markup #"1" #"4"                     %! baca.SegmentMaker._label_duration_multipliers():DURATION_MULTIPLIER:MULTIMEASURE_REST:PHANTOM:REST_VOICE:baca.SegmentMaker._style_phantom_measures(5)
            <BLANKLINE>
                                }                                                                    %! baca.SegmentMaker._make_multimeasure_rest_container(6):PHANTOM
            <BLANKLINE>
                            >>                                                                       %! baca.SegmentMaker._make_multimeasure_rest_container(7):PHANTOM
            <BLANKLINE>
                        }                                                                            %! baca.SingleStaffScoreTemplate.__call__()
            <BLANKLINE>
                    }                                                                                %! baca.SingleStaffScoreTemplate.__call__()
            <BLANKLINE>
                >>                                                                                   %! baca.SingleStaffScoreTemplate.__call__()
            <BLANKLINE>
            >>                                                                                       %! baca.SingleStaffScoreTemplate.__call__()

        Even at the beginning of a segment:

        >>> maker = baca.SegmentMaker(
        ...     breaks=breaks,
        ...     deactivate=[abjad.tags.NOT_YET_PITCHED_COLORING],
        ...     metronome_marks=metronome_marks,
        ...     score_template=baca.SingleStaffScoreTemplate(),
        ...     spacing=baca.minimum_duration((1, 24)),
        ...     time_signatures=[(3, 8), (3, 8)],
        ...     )
        >>> maker(
        ...     'Global_Skips',
        ...     baca.metronome_mark('112'),
        ...     baca.text_spanner_staff_padding(4),
        ...     )
        >>> maker(
        ...     'Music_Voice',
        ...     baca.make_notes(),
        ...     )

        >>> metadata, persist = {}, {}
        >>> persist['persistent_indicators'] = {}
        >>> persist['persistent_indicators']['Score'] = [
        ...     abjad.Momento(
        ...         context='Global_Skips',
        ...         manifest='metronome_marks',
        ...         value='112',
        ...         )
        ...     ]
        >>> metadata['segment_number'] = 1
        >>> lilypond_file = maker.run(
        ...     environment='docs',
        ...     previous_metadata=metadata,
        ...     previous_persist=persist,
        ...     )
        >>> block = abjad.Block(name='layout')
        >>> block.indent = 0
        >>> lilypond_file.items.insert(0, block)
        >>> abjad.show(lilypond_file, strict=89) # doctest: +SKIP

        ..  docs::

            >>> abjad.f(lilypond_file[abjad.Score], strict=89)
            <BLANKLINE>
            \context Score = "Score"                                                                 %! baca.SingleStaffScoreTemplate.__call__()
            <<                                                                                       %! baca.SingleStaffScoreTemplate.__call__()
            <BLANKLINE>
                \context GlobalContext = "Global_Context"                                            %! abjad.ScoreTemplate._make_global_context()
                <<                                                                                   %! abjad.ScoreTemplate._make_global_context()
            <BLANKLINE>
                    \context GlobalSkips = "Global_Skips"                                            %! abjad.ScoreTemplate._make_global_context()
                    {                                                                                %! abjad.ScoreTemplate._make_global_context()
            <BLANKLINE>
                        % [Global_Skips measure 1]                                                   %! baca.SegmentMaker._comment_measure_numbers()
                        \baca-new-spacing-section #1 #24                                             %! SPACING_COMMAND:baca.HorizontalSpacingSpecifier.__call__(1)
                        \override TextSpanner.staff-padding = #4                                     %! baca.text_spanner_staff_padding():baca.OverrideCommand._call(1)
                        \autoPageBreaksOff                                                           %! BREAK:baca.BreakMeasureMap.__call__(1)
                        \noBreak                                                                     %! BREAK:baca.BreakMeasureMap.__call__(2)
                        \baca-lbsd #4 #'(8)                                                          %! BREAK:baca.IndicatorCommand._call()
                        \time 3/8                                                                    %! baca.SegmentMaker._make_global_skips(2):baca.SegmentMaker._set_status_tag():EXPLICIT_TIME_SIGNATURE
                        \bar ""                                                                      %! EMPTY_START_BAR:+SEGMENT:baca.SegmentMaker._make_global_skips(4)
                        \baca-time-signature-color #'blue                                            %! baca.SegmentMaker._attach_color_literal(2):EXPLICIT_TIME_SIGNATURE_COLOR
                        \pageBreak                                                                   %! BREAK:baca.IndicatorCommand._call()
                        s1 * 3/8                                                                     %! baca.SegmentMaker._make_global_skips(1)
                    %@% - \abjad-invisible-line                                                      %! baca.SegmentMaker._set_status_tag():REDUNDANT_METRONOME_MARK:baca.SegmentMaker._attach_metronome_marks(2)
                    %@% - \baca-metronome-mark-spanner-left-text 2 0 1 "112"                         %! baca.SegmentMaker._set_status_tag():REDUNDANT_METRONOME_MARK:baca.SegmentMaker._attach_metronome_marks(2)
                    %@% \bacaStartTextSpanMM                                                         %! baca.SegmentMaker._set_status_tag():REDUNDANT_METRONOME_MARK:baca.SegmentMaker._attach_metronome_marks(2)
                        - \abjad-invisible-line                                                      %! REDUNDANT_METRONOME_MARK_WITH_COLOR:baca.SegmentMaker._attach_metronome_marks(3)
                        - \baca-metronome-mark-spanner-colored-left-text 2 0 1 "112" #'DeepPink1     %! REDUNDANT_METRONOME_MARK_WITH_COLOR:baca.SegmentMaker._attach_metronome_marks(3)
                        \bacaStartTextSpanMM                                                         %! REDUNDANT_METRONOME_MARK_WITH_COLOR:baca.SegmentMaker._attach_metronome_marks(3)
            <BLANKLINE>
                        % [Global_Skips measure 2]                                                   %! baca.SegmentMaker._comment_measure_numbers()
                        \baca-new-spacing-section #1 #24                                             %! SPACING_COMMAND:baca.HorizontalSpacingSpecifier.__call__(1)
                        \noBreak                                                                     %! BREAK:baca.BreakMeasureMap.__call__(2)
                        s1 * 3/8                                                                     %! baca.SegmentMaker._make_global_skips(1)
                        \revert TextSpanner.staff-padding                                            %! baca.text_spanner_staff_padding():baca.OverrideCommand._call(2)
            <BLANKLINE>
                        % [Global_Skips measure 3]                                                   %! baca.SegmentMaker._comment_measure_numbers():baca.SegmentMaker._style_phantom_measures(1):PHANTOM
                        \baca-new-spacing-section #1 #4                                              %! SPACING_COMMAND:baca.HorizontalSpacingSpecifier.__call__(1):baca.SegmentMaker._style_phantom_measures(1):PHANTOM
                        \noBreak                                                                     %! BREAK:baca.BreakMeasureMap.__call__(2):baca.SegmentMaker._style_phantom_measures(1):PHANTOM
                        \time 1/4                                                                    %! baca.SegmentMaker._make_global_skips(3):PHANTOM:baca.SegmentMaker._set_status_tag():EXPLICIT_TIME_SIGNATURE:baca.SegmentMaker._style_phantom_measures(1)
                        \baca-time-signature-transparent                                             %! baca.SegmentMaker._style_phantom_measures(2):PHANTOM
                        s1 * 1/4                                                                     %! baca.SegmentMaker._make_global_skips(3):PHANTOM
                        \bacaStopTextSpanMM                                                          %! EOS_STOP_MM_SPANNER:baca.SegmentMaker._attach_metronome_marks(4):baca.SegmentMaker._style_phantom_measures(1):PHANTOM
                        \once \override Score.BarLine.transparent = ##t                              %! baca.SegmentMaker._style_phantom_measures(3):PHANTOM
                        \once \override Score.SpanBar.transparent = ##t                              %! baca.SegmentMaker._style_phantom_measures(3):PHANTOM
            <BLANKLINE>
                    }                                                                                %! abjad.ScoreTemplate._make_global_context()
            <BLANKLINE>
                >>                                                                                   %! abjad.ScoreTemplate._make_global_context()
            <BLANKLINE>
                \context MusicContext = "Music_Context"                                              %! baca.SingleStaffScoreTemplate.__call__()
                <<                                                                                   %! baca.SingleStaffScoreTemplate.__call__()
            <BLANKLINE>
                    \context Staff = "Music_Staff"                                                   %! baca.SingleStaffScoreTemplate.__call__()
                    {                                                                                %! baca.SingleStaffScoreTemplate.__call__()
            <BLANKLINE>
                        \context Voice = "Music_Voice"                                               %! baca.SingleStaffScoreTemplate.__call__()
                        {                                                                            %! baca.SingleStaffScoreTemplate.__call__()
            <BLANKLINE>
                            % [Music_Voice measure 1]                                                %! baca.SegmentMaker._comment_measure_numbers()
                        %@% \baca-not-yet-pitched-coloring                                           %! baca.SegmentMaker._color_not_yet_pitched():NOT_YET_PITCHED_COLORING
                            b'4.                                                                     %! baca.make_notes()
            <BLANKLINE>
                            % [Music_Voice measure 2]                                                %! baca.SegmentMaker._comment_measure_numbers()
                        %@% \baca-not-yet-pitched-coloring                                           %! baca.SegmentMaker._color_not_yet_pitched():NOT_YET_PITCHED_COLORING
                            b'4.                                                                     %! baca.make_notes()
            <BLANKLINE>
                            <<                                                                       %! baca.SegmentMaker._make_multimeasure_rest_container(7):PHANTOM
            <BLANKLINE>
                                \context Voice = "Music_Voice"                                       %! baca.SegmentMaker._make_multimeasure_rest_container(4):PHANTOM
                                {                                                                    %! baca.SegmentMaker._make_multimeasure_rest_container(4):PHANTOM
            <BLANKLINE>
                                    % [Music_Voice measure 3]                                        %! baca.SegmentMaker._comment_measure_numbers():baca.SegmentMaker._style_phantom_measures(5):PHANTOM
                                    \abjad-invisible-music-coloring                                  %! baca.SegmentMaker._make_multimeasure_rest_container(2):PHANTOM:NOTE:INVISIBLE_MUSIC_COLORING:baca.SegmentMaker._style_phantom_measures(5)
                                %@% \abjad-invisible-music                                           %! baca.SegmentMaker._make_multimeasure_rest_container(3):PHANTOM:NOTE:INVISIBLE_MUSIC_COMMAND:baca.SegmentMaker._style_phantom_measures(5)
                                %@% \baca-not-yet-pitched-coloring                                   %! baca.SegmentMaker._color_not_yet_pitched():NOT_YET_PITCHED_COLORING:HIDDEN:NOTE:baca.SegmentMaker._style_phantom_measures(5):PHANTOM
                                    b'1 * 1/4                                                        %! baca.SegmentMaker._make_multimeasure_rest_container(1):PHANTOM:HIDDEN:NOTE
                                %@% ^ \baca-duration-multiplier-markup #"1" #"4"                     %! baca.SegmentMaker._label_duration_multipliers():DURATION_MULTIPLIER:HIDDEN:NOTE:PHANTOM:baca.SegmentMaker._style_phantom_measures(5)
            <BLANKLINE>
                                }                                                                    %! baca.SegmentMaker._make_multimeasure_rest_container(4):PHANTOM
            <BLANKLINE>
                                \context Voice = "Rest_Voice"                                        %! baca.SegmentMaker._make_multimeasure_rest_container(6):PHANTOM
                                {                                                                    %! baca.SegmentMaker._make_multimeasure_rest_container(6):PHANTOM
            <BLANKLINE>
                                    % [Rest_Voice measure 3]                                         %! baca.SegmentMaker._comment_measure_numbers():baca.SegmentMaker._style_phantom_measures(5):PHANTOM
                                    \once \override Score.TimeSignature.X-extent = ##f               %! baca.SegmentMaker._style_phantom_measures(6):PHANTOM
                                    \once \override MultiMeasureRest.transparent = ##t               %! baca.SegmentMaker._style_phantom_measures(7):PHANTOM
                                    \stopStaff                                                       %! baca.SegmentMaker._style_phantom_measures(8):PHANTOM
                                    \once \override Staff.StaffSymbol.transparent = ##t              %! baca.SegmentMaker._style_phantom_measures(8):PHANTOM
                                    \startStaff                                                      %! baca.SegmentMaker._style_phantom_measures(8):PHANTOM
                                    R1 * 1/4                                                         %! baca.SegmentMaker._make_multimeasure_rest_container(5):PHANTOM:REST_VOICE:MULTIMEASURE_REST
                                %@% ^ \baca-duration-multiplier-markup #"1" #"4"                     %! baca.SegmentMaker._label_duration_multipliers():DURATION_MULTIPLIER:MULTIMEASURE_REST:PHANTOM:REST_VOICE:baca.SegmentMaker._style_phantom_measures(5)
            <BLANKLINE>
                                }                                                                    %! baca.SegmentMaker._make_multimeasure_rest_container(6):PHANTOM
            <BLANKLINE>
                            >>                                                                       %! baca.SegmentMaker._make_multimeasure_rest_container(7):PHANTOM
            <BLANKLINE>
                        }                                                                            %! baca.SingleStaffScoreTemplate.__call__()
            <BLANKLINE>
                    }                                                                                %! baca.SingleStaffScoreTemplate.__call__()
            <BLANKLINE>
                >>                                                                                   %! baca.SingleStaffScoreTemplate.__call__()
            <BLANKLINE>
            >>                                                                                       %! baca.SingleStaffScoreTemplate.__call__()

..  container:: example

    Persistent overrides.

    ..  container:: example

        Explicit persistent overrides work but do not color:

        >>> maker = baca.SegmentMaker(
        ...     score_template=baca.SingleStaffScoreTemplate(),
        ...     spacing=baca.minimum_duration((1, 24)),
        ...     time_signatures=[(3, 8), (3, 8)],
        ...     )
        >>> override = abjad.PersistentOverride(
        ...     attribute="bar_extent",
        ...     context="Staff",
        ...     grob="bar_line",
        ...     value=(0, 0),
        ... )
        >>> tag = "baca.bar_extent_persistent"
        >>> command = IndicatorCommand(
        ...     indicators=[override], selector=baca.leaf(0), tags=[tag]
        ... )

        >>> maker(
        ...     'Music_Voice',
        ...     command,
        ...     baca.make_notes(),
        ...     baca.staff_lines(1),
        ...     baca.staff_position(0),
        ...     )

        >>> lilypond_file = maker.run(environment='docs')
        >>> block = abjad.Block(name='layout')
        >>> block.indent = 0
        >>> lilypond_file.items.insert(0, block)
        >>> abjad.show(lilypond_file, strict=89) # doctest: +SKIP

        ..  docs::

            >>> abjad.f(lilypond_file[abjad.Score], strict=89)
            <BLANKLINE>
            \context Score = "Score"                                                                 %! baca.SingleStaffScoreTemplate.__call__()
            <<                                                                                       %! baca.SingleStaffScoreTemplate.__call__()
            <BLANKLINE>
                \context GlobalContext = "Global_Context"                                            %! abjad.ScoreTemplate._make_global_context()
                <<                                                                                   %! abjad.ScoreTemplate._make_global_context()
            <BLANKLINE>
                    \context GlobalSkips = "Global_Skips"                                            %! abjad.ScoreTemplate._make_global_context()
                    {                                                                                %! abjad.ScoreTemplate._make_global_context()
            <BLANKLINE>
                        % [Global_Skips measure 1]                                                   %! baca.SegmentMaker._comment_measure_numbers()
                        \baca-new-spacing-section #1 #24                                             %! SPACING_COMMAND:baca.HorizontalSpacingSpecifier.__call__(1)
                        \time 3/8                                                                    %! baca.SegmentMaker._make_global_skips(2):baca.SegmentMaker._set_status_tag():EXPLICIT_TIME_SIGNATURE
                        \baca-time-signature-color #'blue                                            %! baca.SegmentMaker._attach_color_literal(2):EXPLICIT_TIME_SIGNATURE_COLOR
                        s1 * 3/8                                                                     %! baca.SegmentMaker._make_global_skips(1)
            <BLANKLINE>
                        % [Global_Skips measure 2]                                                   %! baca.SegmentMaker._comment_measure_numbers()
                        \baca-new-spacing-section #1 #24                                             %! SPACING_COMMAND:baca.HorizontalSpacingSpecifier.__call__(1)
                        s1 * 3/8                                                                     %! baca.SegmentMaker._make_global_skips(1)
            <BLANKLINE>
                        % [Global_Skips measure 3]                                                   %! baca.SegmentMaker._comment_measure_numbers():baca.SegmentMaker._style_phantom_measures(1):PHANTOM
                        \baca-new-spacing-section #1 #4                                              %! SPACING_COMMAND:baca.HorizontalSpacingSpecifier.__call__(1):baca.SegmentMaker._style_phantom_measures(1):PHANTOM
                        \time 1/4                                                                    %! baca.SegmentMaker._make_global_skips(3):PHANTOM:baca.SegmentMaker._set_status_tag():EXPLICIT_TIME_SIGNATURE:baca.SegmentMaker._style_phantom_measures(1)
                        \baca-time-signature-transparent                                             %! baca.SegmentMaker._style_phantom_measures(2):PHANTOM
                        s1 * 1/4                                                                     %! baca.SegmentMaker._make_global_skips(3):PHANTOM
                        \once \override Score.BarLine.transparent = ##t                              %! baca.SegmentMaker._style_phantom_measures(3):PHANTOM
                        \once \override Score.SpanBar.transparent = ##t                              %! baca.SegmentMaker._style_phantom_measures(3):PHANTOM
            <BLANKLINE>
                    }                                                                                %! abjad.ScoreTemplate._make_global_context()
            <BLANKLINE>
                >>                                                                                   %! abjad.ScoreTemplate._make_global_context()
            <BLANKLINE>
                \context MusicContext = "Music_Context"                                              %! baca.SingleStaffScoreTemplate.__call__()
                <<                                                                                   %! baca.SingleStaffScoreTemplate.__call__()
            <BLANKLINE>
                    \context Staff = "Music_Staff"                                                   %! baca.SingleStaffScoreTemplate.__call__()
                    {                                                                                %! baca.SingleStaffScoreTemplate.__call__()
            <BLANKLINE>
                        \context Voice = "Music_Voice"                                               %! baca.SingleStaffScoreTemplate.__call__()
                        {                                                                            %! baca.SingleStaffScoreTemplate.__call__()
            <BLANKLINE>
                            % [Music_Voice measure 1]                                                %! baca.SegmentMaker._comment_measure_numbers()
                            \override Staff.BarLine.bar-extent = #'(0 . 0)                           %! baca.bar_extent_persistent:baca.IndicatorCommand._call():baca.SegmentMaker._set_status_tag():EXPLICIT_PERSISTENT_OVERRIDE
                            \override Staff.BarLine.bar-extent = #'(0 . 0)                           %! -PARTS:baca.IndicatorCommand._call():baca.SegmentMaker._set_status_tag():EXPLICIT_BAR_EXTENT
                            \stopStaff                                                               %! baca.staff_lines():baca.IndicatorCommand._call():baca.SegmentMaker._set_status_tag():EXPLICIT_STAFF_LINES
                            \once \override Staff.StaffSymbol.line-count = 1                         %! baca.staff_lines():baca.IndicatorCommand._call():baca.SegmentMaker._set_status_tag():EXPLICIT_STAFF_LINES
                            \startStaff                                                              %! baca.staff_lines():baca.IndicatorCommand._call():baca.SegmentMaker._set_status_tag():EXPLICIT_STAFF_LINES
                            \once \override Staff.StaffSymbol.color = #(x11-color 'blue)             %! baca.SegmentMaker._attach_color_literal(2):EXPLICIT_STAFF_LINES_COLOR
                            b'4.                                                                     %! baca.make_notes()
            <BLANKLINE>
                            % [Music_Voice measure 2]                                                %! baca.SegmentMaker._comment_measure_numbers()
                            b'4.                                                                     %! baca.make_notes()
            <BLANKLINE>
                            <<                                                                       %! baca.SegmentMaker._make_multimeasure_rest_container(7):PHANTOM
            <BLANKLINE>
                                \context Voice = "Music_Voice"                                       %! baca.SegmentMaker._make_multimeasure_rest_container(4):PHANTOM
                                {                                                                    %! baca.SegmentMaker._make_multimeasure_rest_container(4):PHANTOM
            <BLANKLINE>
                                    % [Music_Voice measure 3]                                        %! baca.SegmentMaker._comment_measure_numbers():baca.SegmentMaker._style_phantom_measures(5):PHANTOM
                                    \abjad-invisible-music-coloring                                  %! baca.SegmentMaker._make_multimeasure_rest_container(2):PHANTOM:NOTE:INVISIBLE_MUSIC_COLORING:baca.SegmentMaker._style_phantom_measures(5)
                                %@% \abjad-invisible-music                                           %! baca.SegmentMaker._make_multimeasure_rest_container(3):PHANTOM:NOTE:INVISIBLE_MUSIC_COMMAND:baca.SegmentMaker._style_phantom_measures(5)
                                    \baca-not-yet-pitched-coloring                                   %! baca.SegmentMaker._color_not_yet_pitched():NOT_YET_PITCHED_COLORING:HIDDEN:NOTE:baca.SegmentMaker._style_phantom_measures(5):PHANTOM
                                    b'1 * 1/4                                                        %! baca.SegmentMaker._make_multimeasure_rest_container(1):PHANTOM:HIDDEN:NOTE
                                %@% ^ \baca-duration-multiplier-markup #"1" #"4"                     %! baca.SegmentMaker._label_duration_multipliers():DURATION_MULTIPLIER:HIDDEN:NOTE:PHANTOM:baca.SegmentMaker._style_phantom_measures(5)
            <BLANKLINE>
                                }                                                                    %! baca.SegmentMaker._make_multimeasure_rest_container(4):PHANTOM
            <BLANKLINE>
                                \context Voice = "Rest_Voice"                                        %! baca.SegmentMaker._make_multimeasure_rest_container(6):PHANTOM
                                {                                                                    %! baca.SegmentMaker._make_multimeasure_rest_container(6):PHANTOM
            <BLANKLINE>
                                    % [Rest_Voice measure 3]                                         %! baca.SegmentMaker._comment_measure_numbers():baca.SegmentMaker._style_phantom_measures(5):PHANTOM
                                    \once \override Score.TimeSignature.X-extent = ##f               %! baca.SegmentMaker._style_phantom_measures(6):PHANTOM
                                    \once \override MultiMeasureRest.transparent = ##t               %! baca.SegmentMaker._style_phantom_measures(7):PHANTOM
                                    \stopStaff                                                       %! baca.SegmentMaker._style_phantom_measures(8):PHANTOM
                                    \once \override Staff.StaffSymbol.transparent = ##t              %! baca.SegmentMaker._style_phantom_measures(8):PHANTOM
                                    \startStaff                                                      %! baca.SegmentMaker._style_phantom_measures(8):PHANTOM
                                    R1 * 1/4                                                         %! baca.SegmentMaker._make_multimeasure_rest_container(5):PHANTOM:REST_VOICE:MULTIMEASURE_REST
                                %@% ^ \baca-duration-multiplier-markup #"1" #"4"                     %! baca.SegmentMaker._label_duration_multipliers():DURATION_MULTIPLIER:MULTIMEASURE_REST:PHANTOM:REST_VOICE:baca.SegmentMaker._style_phantom_measures(5)
            <BLANKLINE>
                                }                                                                    %! baca.SegmentMaker._make_multimeasure_rest_container(6):PHANTOM
            <BLANKLINE>
                            >>                                                                       %! baca.SegmentMaker._make_multimeasure_rest_container(7):PHANTOM
            <BLANKLINE>
                        }                                                                            %! baca.SingleStaffScoreTemplate.__call__()
            <BLANKLINE>
                    }                                                                                %! baca.SingleStaffScoreTemplate.__call__()
            <BLANKLINE>
                >>                                                                                   %! baca.SingleStaffScoreTemplate.__call__()
            <BLANKLINE>
            >>                                                                                       %! baca.SingleStaffScoreTemplate.__call__()

        Persistent overrides also appear in segment metadata:

        >>> abjad.f(maker.persist['persistent_indicators'])
        abjad.OrderedDict(
            [
                (
                    'Music_Staff',
                    [
                        abjad.Momento(
                            context='Music_Voice',
                            edition=abjad.Tag('-PARTS'),
                            prototype='baca.BarExtent',
                            value=1,
                            ),
                        abjad.Momento(
                            context='Music_Voice',
                            prototype='abjad.PersistentOverride',
                            value=abjad.PersistentOverride(
                                attribute='bar_extent',
                                context='Staff',
                                grob='bar_line',
                                value=(0, 0),
                                ),
                            ),
                        abjad.Momento(
                            context='Music_Voice',
                            prototype='baca.StaffLines',
                            value=1,
                            ),
                        ],
                    ),
                (
                    'Score',
                    [
                        abjad.Momento(
                            context='Global_Skips',
                            prototype='abjad.TimeSignature',
                            value='3/8',
                            ),
                        ],
                    ),
                ]
            )


    ..  container:: example

        Reapplied persistent overrides work but do not color:

        >>> maker = baca.SegmentMaker(
        ...     score_template=baca.SingleStaffScoreTemplate(),
        ...     spacing=baca.minimum_duration((1, 24)),
        ...     time_signatures=[(3, 8), (3, 8)],
        ...     )
        >>> maker(
        ...     'Music_Voice',
        ...     baca.make_notes(),
        ...     )

        >>> metadata, persist = {}, {}
        >>> persist['persistent_indicators'] = {}
        >>> persist['persistent_indicators']['Music_Voice'] = [
        ...     abjad.Momento(
        ...         context='Music_Voice',
        ...         prototype='abjad.PersistentOverride',
        ...         value=abjad.PersistentOverride(
        ...             after=True,
        ...             attribute='bar_extent',
        ...             context='Staff',
        ...             grob='bar_line',
        ...             value=(0, 0),
        ...             ),
        ...         )
        ...     ]
        >>> metadata['segment_number'] = 1
        >>> lilypond_file = maker.run(
        ...     environment='docs',
        ...     previous_metadata=metadata,
        ...     previous_persist=persist,
        ...     )
        >>> block = abjad.Block(name='layout')
        >>> block.indent = 0
        >>> lilypond_file.items.insert(0, block)
        >>> abjad.show(lilypond_file, strict=89) # doctest: +SKIP

        ..  docs::

            >>> abjad.f(lilypond_file[abjad.Score], strict=89)
            <BLANKLINE>
            \context Score = "Score"                                                                 %! baca.SingleStaffScoreTemplate.__call__()
            <<                                                                                       %! baca.SingleStaffScoreTemplate.__call__()
            <BLANKLINE>
                \context GlobalContext = "Global_Context"                                            %! abjad.ScoreTemplate._make_global_context()
                <<                                                                                   %! abjad.ScoreTemplate._make_global_context()
            <BLANKLINE>
                    \context GlobalSkips = "Global_Skips"                                            %! abjad.ScoreTemplate._make_global_context()
                    {                                                                                %! abjad.ScoreTemplate._make_global_context()
            <BLANKLINE>
                        % [Global_Skips measure 1]                                                   %! baca.SegmentMaker._comment_measure_numbers()
                        \baca-new-spacing-section #1 #24                                             %! SPACING_COMMAND:baca.HorizontalSpacingSpecifier.__call__(1)
                        \time 3/8                                                                    %! baca.SegmentMaker._make_global_skips(2):baca.SegmentMaker._set_status_tag():EXPLICIT_TIME_SIGNATURE
                        \bar ""                                                                      %! EMPTY_START_BAR:+SEGMENT:baca.SegmentMaker._make_global_skips(4)
                        \baca-time-signature-color #'blue                                            %! baca.SegmentMaker._attach_color_literal(2):EXPLICIT_TIME_SIGNATURE_COLOR
                        s1 * 3/8                                                                     %! baca.SegmentMaker._make_global_skips(1)
            <BLANKLINE>
                        % [Global_Skips measure 2]                                                   %! baca.SegmentMaker._comment_measure_numbers()
                        \baca-new-spacing-section #1 #24                                             %! SPACING_COMMAND:baca.HorizontalSpacingSpecifier.__call__(1)
                        s1 * 3/8                                                                     %! baca.SegmentMaker._make_global_skips(1)
            <BLANKLINE>
                        % [Global_Skips measure 3]                                                   %! baca.SegmentMaker._comment_measure_numbers():baca.SegmentMaker._style_phantom_measures(1):PHANTOM
                        \baca-new-spacing-section #1 #4                                              %! SPACING_COMMAND:baca.HorizontalSpacingSpecifier.__call__(1):baca.SegmentMaker._style_phantom_measures(1):PHANTOM
                        \time 1/4                                                                    %! baca.SegmentMaker._make_global_skips(3):PHANTOM:baca.SegmentMaker._set_status_tag():EXPLICIT_TIME_SIGNATURE:baca.SegmentMaker._style_phantom_measures(1)
                        \baca-time-signature-transparent                                             %! baca.SegmentMaker._style_phantom_measures(2):PHANTOM
                        s1 * 1/4                                                                     %! baca.SegmentMaker._make_global_skips(3):PHANTOM
                        \once \override Score.BarLine.transparent = ##t                              %! baca.SegmentMaker._style_phantom_measures(3):PHANTOM
                        \once \override Score.SpanBar.transparent = ##t                              %! baca.SegmentMaker._style_phantom_measures(3):PHANTOM
            <BLANKLINE>
                    }                                                                                %! abjad.ScoreTemplate._make_global_context()
            <BLANKLINE>
                >>                                                                                   %! abjad.ScoreTemplate._make_global_context()
            <BLANKLINE>
                \context MusicContext = "Music_Context"                                              %! baca.SingleStaffScoreTemplate.__call__()
                <<                                                                                   %! baca.SingleStaffScoreTemplate.__call__()
            <BLANKLINE>
                    \context Staff = "Music_Staff"                                                   %! baca.SingleStaffScoreTemplate.__call__()
                    {                                                                                %! baca.SingleStaffScoreTemplate.__call__()
            <BLANKLINE>
                        \context Voice = "Music_Voice"                                               %! baca.SingleStaffScoreTemplate.__call__()
                        {                                                                            %! baca.SingleStaffScoreTemplate.__call__()
            <BLANKLINE>
                            % [Music_Voice measure 1]                                                %! baca.SegmentMaker._comment_measure_numbers()
                            \baca-not-yet-pitched-coloring                                           %! baca.SegmentMaker._color_not_yet_pitched():NOT_YET_PITCHED_COLORING
                            b'4.                                                                     %! baca.make_notes()
                            \override Staff.BarLine.bar-extent = #'(0 . 0)                           %! baca.SegmentMaker._reapply_persistent_indicators(3):baca.SegmentMaker._set_status_tag():REAPPLIED_PERSISTENT_OVERRIDE
            <BLANKLINE>
                            % [Music_Voice measure 2]                                                %! baca.SegmentMaker._comment_measure_numbers()
                            \baca-not-yet-pitched-coloring                                           %! baca.SegmentMaker._color_not_yet_pitched():NOT_YET_PITCHED_COLORING
                            b'4.                                                                     %! baca.make_notes()
            <BLANKLINE>
                            <<                                                                       %! baca.SegmentMaker._make_multimeasure_rest_container(7):PHANTOM
            <BLANKLINE>
                                \context Voice = "Music_Voice"                                       %! baca.SegmentMaker._make_multimeasure_rest_container(4):PHANTOM
                                {                                                                    %! baca.SegmentMaker._make_multimeasure_rest_container(4):PHANTOM
            <BLANKLINE>
                                    % [Music_Voice measure 3]                                        %! baca.SegmentMaker._comment_measure_numbers():baca.SegmentMaker._style_phantom_measures(5):PHANTOM
                                    \abjad-invisible-music-coloring                                  %! baca.SegmentMaker._make_multimeasure_rest_container(2):PHANTOM:NOTE:INVISIBLE_MUSIC_COLORING:baca.SegmentMaker._style_phantom_measures(5)
                                %@% \abjad-invisible-music                                           %! baca.SegmentMaker._make_multimeasure_rest_container(3):PHANTOM:NOTE:INVISIBLE_MUSIC_COMMAND:baca.SegmentMaker._style_phantom_measures(5)
                                    \baca-not-yet-pitched-coloring                                   %! baca.SegmentMaker._color_not_yet_pitched():NOT_YET_PITCHED_COLORING:HIDDEN:NOTE:baca.SegmentMaker._style_phantom_measures(5):PHANTOM
                                    b'1 * 1/4                                                        %! baca.SegmentMaker._make_multimeasure_rest_container(1):PHANTOM:HIDDEN:NOTE
                                %@% ^ \baca-duration-multiplier-markup #"1" #"4"                     %! baca.SegmentMaker._label_duration_multipliers():DURATION_MULTIPLIER:HIDDEN:NOTE:PHANTOM:baca.SegmentMaker._style_phantom_measures(5)
            <BLANKLINE>
                                }                                                                    %! baca.SegmentMaker._make_multimeasure_rest_container(4):PHANTOM
            <BLANKLINE>
                                \context Voice = "Rest_Voice"                                        %! baca.SegmentMaker._make_multimeasure_rest_container(6):PHANTOM
                                {                                                                    %! baca.SegmentMaker._make_multimeasure_rest_container(6):PHANTOM
            <BLANKLINE>
                                    % [Rest_Voice measure 3]                                         %! baca.SegmentMaker._comment_measure_numbers():baca.SegmentMaker._style_phantom_measures(5):PHANTOM
                                    \once \override Score.TimeSignature.X-extent = ##f               %! baca.SegmentMaker._style_phantom_measures(6):PHANTOM
                                    \once \override MultiMeasureRest.transparent = ##t               %! baca.SegmentMaker._style_phantom_measures(7):PHANTOM
                                    \stopStaff                                                       %! baca.SegmentMaker._style_phantom_measures(8):PHANTOM
                                    \once \override Staff.StaffSymbol.transparent = ##t              %! baca.SegmentMaker._style_phantom_measures(8):PHANTOM
                                    \startStaff                                                      %! baca.SegmentMaker._style_phantom_measures(8):PHANTOM
                                    R1 * 1/4                                                         %! baca.SegmentMaker._make_multimeasure_rest_container(5):PHANTOM:REST_VOICE:MULTIMEASURE_REST
                                %@% ^ \baca-duration-multiplier-markup #"1" #"4"                     %! baca.SegmentMaker._label_duration_multipliers():DURATION_MULTIPLIER:MULTIMEASURE_REST:PHANTOM:REST_VOICE:baca.SegmentMaker._style_phantom_measures(5)
            <BLANKLINE>
                                }                                                                    %! baca.SegmentMaker._make_multimeasure_rest_container(6):PHANTOM
            <BLANKLINE>
                            >>                                                                       %! baca.SegmentMaker._make_multimeasure_rest_container(7):PHANTOM
            <BLANKLINE>
                        }                                                                            %! baca.SingleStaffScoreTemplate.__call__()
            <BLANKLINE>
                    }                                                                                %! baca.SingleStaffScoreTemplate.__call__()
            <BLANKLINE>
                >>                                                                                   %! baca.SingleStaffScoreTemplate.__call__()
            <BLANKLINE>
            >>                                                                                       %! baca.SingleStaffScoreTemplate.__call__()

        Even at the beginning of a segment:

        >>> maker = baca.SegmentMaker(
        ...     score_template=baca.SingleStaffScoreTemplate(),
        ...     spacing=baca.minimum_duration((1, 24)),
        ...     time_signatures=[(3, 8), (3, 8)],
        ...     )
        >>> override = abjad.PersistentOverride(
        ...     attribute="bar_extent",
        ...     context="Staff",
        ...     grob="bar_line",
        ...     value=(0, 0),
        ... )
        >>> tag = "baca.bar_extent_persistent"
        >>> command = IndicatorCommand(
        ...     indicators=[override], selector=baca.leaf(0), tags=[tag]
        ... )
        >>> maker(
        ...     'Music_Voice',
        ...     command,
        ...     baca.make_notes(),
        ...     )

        >>> metadata, persist = {}, {}
        >>> persist['persistent_indicators'] = {}
        >>> persist['persistent_indicators']['Music_Voice'] = [
        ...     abjad.Momento(
        ...         context='Music_Voice',
        ...         prototype='abjad.PersistentOverride',
        ...         value=abjad.PersistentOverride(
        ...             after=True,
        ...             attribute='bar_extent',
        ...             context='Staff',
        ...             grob='bar_line',
        ...             value=(0, 0),
        ...             ),
        ...         )
        ...     ]
        >>> metadata['segment_number'] = 1
        >>> lilypond_file = maker.run(
        ...     environment='docs',
        ...     previous_metadata=metadata,
        ...     previous_persist=persist,
        ...     )
        >>> block = abjad.Block(name='layout')
        >>> block.indent = 0
        >>> lilypond_file.items.insert(0, block)
        >>> abjad.show(lilypond_file, strict=89) # doctest: +SKIP

        ..  docs::

            >>> abjad.f(lilypond_file[abjad.Score], strict=89)
            <BLANKLINE>
            \context Score = "Score"                                                                 %! baca.SingleStaffScoreTemplate.__call__()
            <<                                                                                       %! baca.SingleStaffScoreTemplate.__call__()
            <BLANKLINE>
                \context GlobalContext = "Global_Context"                                            %! abjad.ScoreTemplate._make_global_context()
                <<                                                                                   %! abjad.ScoreTemplate._make_global_context()
            <BLANKLINE>
                    \context GlobalSkips = "Global_Skips"                                            %! abjad.ScoreTemplate._make_global_context()
                    {                                                                                %! abjad.ScoreTemplate._make_global_context()
            <BLANKLINE>
                        % [Global_Skips measure 1]                                                   %! baca.SegmentMaker._comment_measure_numbers()
                        \baca-new-spacing-section #1 #24                                             %! SPACING_COMMAND:baca.HorizontalSpacingSpecifier.__call__(1)
                        \time 3/8                                                                    %! baca.SegmentMaker._make_global_skips(2):baca.SegmentMaker._set_status_tag():EXPLICIT_TIME_SIGNATURE
                        \bar ""                                                                      %! EMPTY_START_BAR:+SEGMENT:baca.SegmentMaker._make_global_skips(4)
                        \baca-time-signature-color #'blue                                            %! baca.SegmentMaker._attach_color_literal(2):EXPLICIT_TIME_SIGNATURE_COLOR
                        s1 * 3/8                                                                     %! baca.SegmentMaker._make_global_skips(1)
            <BLANKLINE>
                        % [Global_Skips measure 2]                                                   %! baca.SegmentMaker._comment_measure_numbers()
                        \baca-new-spacing-section #1 #24                                             %! SPACING_COMMAND:baca.HorizontalSpacingSpecifier.__call__(1)
                        s1 * 3/8                                                                     %! baca.SegmentMaker._make_global_skips(1)
            <BLANKLINE>
                        % [Global_Skips measure 3]                                                   %! baca.SegmentMaker._comment_measure_numbers():baca.SegmentMaker._style_phantom_measures(1):PHANTOM
                        \baca-new-spacing-section #1 #4                                              %! SPACING_COMMAND:baca.HorizontalSpacingSpecifier.__call__(1):baca.SegmentMaker._style_phantom_measures(1):PHANTOM
                        \time 1/4                                                                    %! baca.SegmentMaker._make_global_skips(3):PHANTOM:baca.SegmentMaker._set_status_tag():EXPLICIT_TIME_SIGNATURE:baca.SegmentMaker._style_phantom_measures(1)
                        \baca-time-signature-transparent                                             %! baca.SegmentMaker._style_phantom_measures(2):PHANTOM
                        s1 * 1/4                                                                     %! baca.SegmentMaker._make_global_skips(3):PHANTOM
                        \once \override Score.BarLine.transparent = ##t                              %! baca.SegmentMaker._style_phantom_measures(3):PHANTOM
                        \once \override Score.SpanBar.transparent = ##t                              %! baca.SegmentMaker._style_phantom_measures(3):PHANTOM
            <BLANKLINE>
                    }                                                                                %! abjad.ScoreTemplate._make_global_context()
            <BLANKLINE>
                >>                                                                                   %! abjad.ScoreTemplate._make_global_context()
            <BLANKLINE>
                \context MusicContext = "Music_Context"                                              %! baca.SingleStaffScoreTemplate.__call__()
                <<                                                                                   %! baca.SingleStaffScoreTemplate.__call__()
            <BLANKLINE>
                    \context Staff = "Music_Staff"                                                   %! baca.SingleStaffScoreTemplate.__call__()
                    {                                                                                %! baca.SingleStaffScoreTemplate.__call__()
            <BLANKLINE>
                        \context Voice = "Music_Voice"                                               %! baca.SingleStaffScoreTemplate.__call__()
                        {                                                                            %! baca.SingleStaffScoreTemplate.__call__()
            <BLANKLINE>
                            % [Music_Voice measure 1]                                                %! baca.SegmentMaker._comment_measure_numbers()
                            \override Staff.BarLine.bar-extent = #'(0 . 0)                           %! baca.bar_extent_persistent:baca.IndicatorCommand._call():baca.SegmentMaker._set_status_tag():REDUNDANT_PERSISTENT_OVERRIDE
                            \baca-not-yet-pitched-coloring                                           %! baca.SegmentMaker._color_not_yet_pitched():NOT_YET_PITCHED_COLORING
                            b'4.                                                                     %! baca.make_notes()
            <BLANKLINE>
                            % [Music_Voice measure 2]                                                %! baca.SegmentMaker._comment_measure_numbers()
                            \baca-not-yet-pitched-coloring                                           %! baca.SegmentMaker._color_not_yet_pitched():NOT_YET_PITCHED_COLORING
                            b'4.                                                                     %! baca.make_notes()
            <BLANKLINE>
                            <<                                                                       %! baca.SegmentMaker._make_multimeasure_rest_container(7):PHANTOM
            <BLANKLINE>
                                \context Voice = "Music_Voice"                                       %! baca.SegmentMaker._make_multimeasure_rest_container(4):PHANTOM
                                {                                                                    %! baca.SegmentMaker._make_multimeasure_rest_container(4):PHANTOM
            <BLANKLINE>
                                    % [Music_Voice measure 3]                                        %! baca.SegmentMaker._comment_measure_numbers():baca.SegmentMaker._style_phantom_measures(5):PHANTOM
                                    \abjad-invisible-music-coloring                                  %! baca.SegmentMaker._make_multimeasure_rest_container(2):PHANTOM:NOTE:INVISIBLE_MUSIC_COLORING:baca.SegmentMaker._style_phantom_measures(5)
                                %@% \abjad-invisible-music                                           %! baca.SegmentMaker._make_multimeasure_rest_container(3):PHANTOM:NOTE:INVISIBLE_MUSIC_COMMAND:baca.SegmentMaker._style_phantom_measures(5)
                                    \baca-not-yet-pitched-coloring                                   %! baca.SegmentMaker._color_not_yet_pitched():NOT_YET_PITCHED_COLORING:HIDDEN:NOTE:baca.SegmentMaker._style_phantom_measures(5):PHANTOM
                                    b'1 * 1/4                                                        %! baca.SegmentMaker._make_multimeasure_rest_container(1):PHANTOM:HIDDEN:NOTE
                                %@% ^ \baca-duration-multiplier-markup #"1" #"4"                     %! baca.SegmentMaker._label_duration_multipliers():DURATION_MULTIPLIER:HIDDEN:NOTE:PHANTOM:baca.SegmentMaker._style_phantom_measures(5)
            <BLANKLINE>
                                }                                                                    %! baca.SegmentMaker._make_multimeasure_rest_container(4):PHANTOM
            <BLANKLINE>
                                \context Voice = "Rest_Voice"                                        %! baca.SegmentMaker._make_multimeasure_rest_container(6):PHANTOM
                                {                                                                    %! baca.SegmentMaker._make_multimeasure_rest_container(6):PHANTOM
            <BLANKLINE>
                                    % [Rest_Voice measure 3]                                         %! baca.SegmentMaker._comment_measure_numbers():baca.SegmentMaker._style_phantom_measures(5):PHANTOM
                                    \once \override Score.TimeSignature.X-extent = ##f               %! baca.SegmentMaker._style_phantom_measures(6):PHANTOM
                                    \once \override MultiMeasureRest.transparent = ##t               %! baca.SegmentMaker._style_phantom_measures(7):PHANTOM
                                    \stopStaff                                                       %! baca.SegmentMaker._style_phantom_measures(8):PHANTOM
                                    \once \override Staff.StaffSymbol.transparent = ##t              %! baca.SegmentMaker._style_phantom_measures(8):PHANTOM
                                    \startStaff                                                      %! baca.SegmentMaker._style_phantom_measures(8):PHANTOM
                                    R1 * 1/4                                                         %! baca.SegmentMaker._make_multimeasure_rest_container(5):PHANTOM:REST_VOICE:MULTIMEASURE_REST
                                %@% ^ \baca-duration-multiplier-markup #"1" #"4"                     %! baca.SegmentMaker._label_duration_multipliers():DURATION_MULTIPLIER:MULTIMEASURE_REST:PHANTOM:REST_VOICE:baca.SegmentMaker._style_phantom_measures(5)
            <BLANKLINE>
                                }                                                                    %! baca.SegmentMaker._make_multimeasure_rest_container(6):PHANTOM
            <BLANKLINE>
                            >>                                                                       %! baca.SegmentMaker._make_multimeasure_rest_container(7):PHANTOM
            <BLANKLINE>
                        }                                                                            %! baca.SingleStaffScoreTemplate.__call__()
            <BLANKLINE>
                    }                                                                                %! baca.SingleStaffScoreTemplate.__call__()
            <BLANKLINE>
                >>                                                                                   %! baca.SingleStaffScoreTemplate.__call__()
            <BLANKLINE>
            >>                                                                                       %! baca.SingleStaffScoreTemplate.__call__()

..  container:: example

    Staff lines.

    ..  container:: example

        Explicit staff lines color blue:

        >>> maker = baca.SegmentMaker(
        ...     deactivate=[abjad.tags.NOT_YET_PITCHED_COLORING],
        ...     score_template=baca.SingleStaffScoreTemplate(),
        ...     spacing=baca.minimum_duration((1, 24)),
        ...     time_signatures=[(3, 8), (3, 8)],
        ...     )
        >>> maker(
        ...     'Music_Voice',
        ...     baca.make_notes(),
        ...     baca.staff_lines(5),
        ...     )

        >>> lilypond_file = maker.run(environment='docs')
        >>> block = abjad.Block(name='layout')
        >>> block.indent = 0
        >>> lilypond_file.items.insert(0, block)
        >>> abjad.show(lilypond_file, strict=89) # doctest: +SKIP

        ..  docs::

            >>> abjad.f(lilypond_file[abjad.Score], strict=89)
            <BLANKLINE>
            \context Score = "Score"                                                                 %! baca.SingleStaffScoreTemplate.__call__()
            <<                                                                                       %! baca.SingleStaffScoreTemplate.__call__()
            <BLANKLINE>
                \context GlobalContext = "Global_Context"                                            %! abjad.ScoreTemplate._make_global_context()
                <<                                                                                   %! abjad.ScoreTemplate._make_global_context()
            <BLANKLINE>
                    \context GlobalSkips = "Global_Skips"                                            %! abjad.ScoreTemplate._make_global_context()
                    {                                                                                %! abjad.ScoreTemplate._make_global_context()
            <BLANKLINE>
                        % [Global_Skips measure 1]                                                   %! baca.SegmentMaker._comment_measure_numbers()
                        \baca-new-spacing-section #1 #24                                             %! SPACING_COMMAND:baca.HorizontalSpacingSpecifier.__call__(1)
                        \time 3/8                                                                    %! baca.SegmentMaker._make_global_skips(2):baca.SegmentMaker._set_status_tag():EXPLICIT_TIME_SIGNATURE
                        \baca-time-signature-color #'blue                                            %! baca.SegmentMaker._attach_color_literal(2):EXPLICIT_TIME_SIGNATURE_COLOR
                        s1 * 3/8                                                                     %! baca.SegmentMaker._make_global_skips(1)
            <BLANKLINE>
                        % [Global_Skips measure 2]                                                   %! baca.SegmentMaker._comment_measure_numbers()
                        \baca-new-spacing-section #1 #24                                             %! SPACING_COMMAND:baca.HorizontalSpacingSpecifier.__call__(1)
                        s1 * 3/8                                                                     %! baca.SegmentMaker._make_global_skips(1)
            <BLANKLINE>
                        % [Global_Skips measure 3]                                                   %! baca.SegmentMaker._comment_measure_numbers():baca.SegmentMaker._style_phantom_measures(1):PHANTOM
                        \baca-new-spacing-section #1 #4                                              %! SPACING_COMMAND:baca.HorizontalSpacingSpecifier.__call__(1):baca.SegmentMaker._style_phantom_measures(1):PHANTOM
                        \time 1/4                                                                    %! baca.SegmentMaker._make_global_skips(3):PHANTOM:baca.SegmentMaker._set_status_tag():EXPLICIT_TIME_SIGNATURE:baca.SegmentMaker._style_phantom_measures(1)
                        \baca-time-signature-transparent                                             %! baca.SegmentMaker._style_phantom_measures(2):PHANTOM
                        s1 * 1/4                                                                     %! baca.SegmentMaker._make_global_skips(3):PHANTOM
                        \once \override Score.BarLine.transparent = ##t                              %! baca.SegmentMaker._style_phantom_measures(3):PHANTOM
                        \once \override Score.SpanBar.transparent = ##t                              %! baca.SegmentMaker._style_phantom_measures(3):PHANTOM
            <BLANKLINE>
                    }                                                                                %! abjad.ScoreTemplate._make_global_context()
            <BLANKLINE>
                >>                                                                                   %! abjad.ScoreTemplate._make_global_context()
            <BLANKLINE>
                \context MusicContext = "Music_Context"                                              %! baca.SingleStaffScoreTemplate.__call__()
                <<                                                                                   %! baca.SingleStaffScoreTemplate.__call__()
            <BLANKLINE>
                    \context Staff = "Music_Staff"                                                   %! baca.SingleStaffScoreTemplate.__call__()
                    {                                                                                %! baca.SingleStaffScoreTemplate.__call__()
            <BLANKLINE>
                        \context Voice = "Music_Voice"                                               %! baca.SingleStaffScoreTemplate.__call__()
                        {                                                                            %! baca.SingleStaffScoreTemplate.__call__()
            <BLANKLINE>
                            % [Music_Voice measure 1]                                                %! baca.SegmentMaker._comment_measure_numbers()
                            \override Staff.BarLine.bar-extent = #'(-2 . 2)                          %! -PARTS:baca.IndicatorCommand._call():baca.SegmentMaker._set_status_tag():EXPLICIT_BAR_EXTENT
                            \stopStaff                                                               %! baca.staff_lines():baca.IndicatorCommand._call():baca.SegmentMaker._set_status_tag():EXPLICIT_STAFF_LINES
                            \once \override Staff.StaffSymbol.line-count = 5                         %! baca.staff_lines():baca.IndicatorCommand._call():baca.SegmentMaker._set_status_tag():EXPLICIT_STAFF_LINES
                            \startStaff                                                              %! baca.staff_lines():baca.IndicatorCommand._call():baca.SegmentMaker._set_status_tag():EXPLICIT_STAFF_LINES
                            \once \override Staff.StaffSymbol.color = #(x11-color 'blue)             %! baca.SegmentMaker._attach_color_literal(2):EXPLICIT_STAFF_LINES_COLOR
                        %@% \baca-not-yet-pitched-coloring                                           %! baca.SegmentMaker._color_not_yet_pitched():NOT_YET_PITCHED_COLORING
                            b'4.                                                                     %! baca.make_notes()
            <BLANKLINE>
                            % [Music_Voice measure 2]                                                %! baca.SegmentMaker._comment_measure_numbers()
                        %@% \baca-not-yet-pitched-coloring                                           %! baca.SegmentMaker._color_not_yet_pitched():NOT_YET_PITCHED_COLORING
                            b'4.                                                                     %! baca.make_notes()
            <BLANKLINE>
                            <<                                                                       %! baca.SegmentMaker._make_multimeasure_rest_container(7):PHANTOM
            <BLANKLINE>
                                \context Voice = "Music_Voice"                                       %! baca.SegmentMaker._make_multimeasure_rest_container(4):PHANTOM
                                {                                                                    %! baca.SegmentMaker._make_multimeasure_rest_container(4):PHANTOM
            <BLANKLINE>
                                    % [Music_Voice measure 3]                                        %! baca.SegmentMaker._comment_measure_numbers():baca.SegmentMaker._style_phantom_measures(5):PHANTOM
                                    \abjad-invisible-music-coloring                                  %! baca.SegmentMaker._make_multimeasure_rest_container(2):PHANTOM:NOTE:INVISIBLE_MUSIC_COLORING:baca.SegmentMaker._style_phantom_measures(5)
                                %@% \abjad-invisible-music                                           %! baca.SegmentMaker._make_multimeasure_rest_container(3):PHANTOM:NOTE:INVISIBLE_MUSIC_COMMAND:baca.SegmentMaker._style_phantom_measures(5)
                                %@% \baca-not-yet-pitched-coloring                                   %! baca.SegmentMaker._color_not_yet_pitched():NOT_YET_PITCHED_COLORING:HIDDEN:NOTE:baca.SegmentMaker._style_phantom_measures(5):PHANTOM
                                    b'1 * 1/4                                                        %! baca.SegmentMaker._make_multimeasure_rest_container(1):PHANTOM:HIDDEN:NOTE
                                %@% ^ \baca-duration-multiplier-markup #"1" #"4"                     %! baca.SegmentMaker._label_duration_multipliers():DURATION_MULTIPLIER:HIDDEN:NOTE:PHANTOM:baca.SegmentMaker._style_phantom_measures(5)
            <BLANKLINE>
                                }                                                                    %! baca.SegmentMaker._make_multimeasure_rest_container(4):PHANTOM
            <BLANKLINE>
                                \context Voice = "Rest_Voice"                                        %! baca.SegmentMaker._make_multimeasure_rest_container(6):PHANTOM
                                {                                                                    %! baca.SegmentMaker._make_multimeasure_rest_container(6):PHANTOM
            <BLANKLINE>
                                    % [Rest_Voice measure 3]                                         %! baca.SegmentMaker._comment_measure_numbers():baca.SegmentMaker._style_phantom_measures(5):PHANTOM
                                    \once \override Score.TimeSignature.X-extent = ##f               %! baca.SegmentMaker._style_phantom_measures(6):PHANTOM
                                    \once \override MultiMeasureRest.transparent = ##t               %! baca.SegmentMaker._style_phantom_measures(7):PHANTOM
                                    \stopStaff                                                       %! baca.SegmentMaker._style_phantom_measures(8):PHANTOM
                                    \once \override Staff.StaffSymbol.transparent = ##t              %! baca.SegmentMaker._style_phantom_measures(8):PHANTOM
                                    \startStaff                                                      %! baca.SegmentMaker._style_phantom_measures(8):PHANTOM
                                    R1 * 1/4                                                         %! baca.SegmentMaker._make_multimeasure_rest_container(5):PHANTOM:REST_VOICE:MULTIMEASURE_REST
                                %@% ^ \baca-duration-multiplier-markup #"1" #"4"                     %! baca.SegmentMaker._label_duration_multipliers():DURATION_MULTIPLIER:MULTIMEASURE_REST:PHANTOM:REST_VOICE:baca.SegmentMaker._style_phantom_measures(5)
            <BLANKLINE>
                                }                                                                    %! baca.SegmentMaker._make_multimeasure_rest_container(6):PHANTOM
            <BLANKLINE>
                            >>                                                                       %! baca.SegmentMaker._make_multimeasure_rest_container(7):PHANTOM
            <BLANKLINE>
                        }                                                                            %! baca.SingleStaffScoreTemplate.__call__()
            <BLANKLINE>
                    }                                                                                %! baca.SingleStaffScoreTemplate.__call__()
            <BLANKLINE>
                >>                                                                                   %! baca.SingleStaffScoreTemplate.__call__()
            <BLANKLINE>
            >>                                                                                       %! baca.SingleStaffScoreTemplate.__call__()

        Even after previous staff lines:

        >>> maker = baca.SegmentMaker(
        ...     deactivate=[abjad.tags.NOT_YET_PITCHED_COLORING],
        ...     score_template=baca.SingleStaffScoreTemplate(),
        ...     spacing=baca.minimum_duration((1, 24)),
        ...     time_signatures=[(3, 8), (3, 8)],
        ...     )
        >>> maker(
        ...     'Music_Voice',
        ...     baca.make_notes(),
        ...     baca.staff_lines(1),
        ...     )

        >>> metadata, persist = {}, {}
        >>> persist['persistent_indicators'] = {}
        >>> persist['persistent_indicators']['Music_Staff'] = [
        ...     abjad.Momento(
        ...         context='Music_Voice',
        ...         prototype='baca.StaffLines',
        ...         value=5,
        ...         )
        ...     ]
        >>> metadata['segment_number'] = 1
        >>> lilypond_file = maker.run(
        ...     environment='docs',
        ...     previous_metadata=metadata,
        ...     previous_persist=persist,
        ...     )
        >>> block = abjad.Block(name='layout')
        >>> block.indent = 0
        >>> lilypond_file.items.insert(0, block)
        >>> abjad.show(lilypond_file, strict=89) # doctest: +SKIP

        ..  docs::

            >>> abjad.f(lilypond_file[abjad.Score], strict=89)
            <BLANKLINE>
            \context Score = "Score"                                                                 %! baca.SingleStaffScoreTemplate.__call__()
            <<                                                                                       %! baca.SingleStaffScoreTemplate.__call__()
            <BLANKLINE>
                \context GlobalContext = "Global_Context"                                            %! abjad.ScoreTemplate._make_global_context()
                <<                                                                                   %! abjad.ScoreTemplate._make_global_context()
            <BLANKLINE>
                    \context GlobalSkips = "Global_Skips"                                            %! abjad.ScoreTemplate._make_global_context()
                    {                                                                                %! abjad.ScoreTemplate._make_global_context()
            <BLANKLINE>
                        % [Global_Skips measure 1]                                                   %! baca.SegmentMaker._comment_measure_numbers()
                        \baca-new-spacing-section #1 #24                                             %! SPACING_COMMAND:baca.HorizontalSpacingSpecifier.__call__(1)
                        \time 3/8                                                                    %! baca.SegmentMaker._make_global_skips(2):baca.SegmentMaker._set_status_tag():EXPLICIT_TIME_SIGNATURE
                        \bar ""                                                                      %! EMPTY_START_BAR:+SEGMENT:baca.SegmentMaker._make_global_skips(4)
                        \baca-time-signature-color #'blue                                            %! baca.SegmentMaker._attach_color_literal(2):EXPLICIT_TIME_SIGNATURE_COLOR
                        s1 * 3/8                                                                     %! baca.SegmentMaker._make_global_skips(1)
            <BLANKLINE>
                        % [Global_Skips measure 2]                                                   %! baca.SegmentMaker._comment_measure_numbers()
                        \baca-new-spacing-section #1 #24                                             %! SPACING_COMMAND:baca.HorizontalSpacingSpecifier.__call__(1)
                        s1 * 3/8                                                                     %! baca.SegmentMaker._make_global_skips(1)
            <BLANKLINE>
                        % [Global_Skips measure 3]                                                   %! baca.SegmentMaker._comment_measure_numbers():baca.SegmentMaker._style_phantom_measures(1):PHANTOM
                        \baca-new-spacing-section #1 #4                                              %! SPACING_COMMAND:baca.HorizontalSpacingSpecifier.__call__(1):baca.SegmentMaker._style_phantom_measures(1):PHANTOM
                        \time 1/4                                                                    %! baca.SegmentMaker._make_global_skips(3):PHANTOM:baca.SegmentMaker._set_status_tag():EXPLICIT_TIME_SIGNATURE:baca.SegmentMaker._style_phantom_measures(1)
                        \baca-time-signature-transparent                                             %! baca.SegmentMaker._style_phantom_measures(2):PHANTOM
                        s1 * 1/4                                                                     %! baca.SegmentMaker._make_global_skips(3):PHANTOM
                        \once \override Score.BarLine.transparent = ##t                              %! baca.SegmentMaker._style_phantom_measures(3):PHANTOM
                        \once \override Score.SpanBar.transparent = ##t                              %! baca.SegmentMaker._style_phantom_measures(3):PHANTOM
            <BLANKLINE>
                    }                                                                                %! abjad.ScoreTemplate._make_global_context()
            <BLANKLINE>
                >>                                                                                   %! abjad.ScoreTemplate._make_global_context()
            <BLANKLINE>
                \context MusicContext = "Music_Context"                                              %! baca.SingleStaffScoreTemplate.__call__()
                <<                                                                                   %! baca.SingleStaffScoreTemplate.__call__()
            <BLANKLINE>
                    \context Staff = "Music_Staff"                                                   %! baca.SingleStaffScoreTemplate.__call__()
                    {                                                                                %! baca.SingleStaffScoreTemplate.__call__()
            <BLANKLINE>
                        \context Voice = "Music_Voice"                                               %! baca.SingleStaffScoreTemplate.__call__()
                        {                                                                            %! baca.SingleStaffScoreTemplate.__call__()
            <BLANKLINE>
                            % [Music_Voice measure 1]                                                %! baca.SegmentMaker._comment_measure_numbers()
                            \override Staff.BarLine.bar-extent = #'(0 . 0)                           %! -PARTS:baca.IndicatorCommand._call():baca.SegmentMaker._set_status_tag():EXPLICIT_BAR_EXTENT
                            \stopStaff                                                               %! baca.staff_lines():baca.IndicatorCommand._call():baca.SegmentMaker._set_status_tag():EXPLICIT_STAFF_LINES
                            \once \override Staff.StaffSymbol.line-count = 1                         %! baca.staff_lines():baca.IndicatorCommand._call():baca.SegmentMaker._set_status_tag():EXPLICIT_STAFF_LINES
                            \startStaff                                                              %! baca.staff_lines():baca.IndicatorCommand._call():baca.SegmentMaker._set_status_tag():EXPLICIT_STAFF_LINES
                            \once \override Staff.StaffSymbol.color = #(x11-color 'blue)             %! baca.SegmentMaker._attach_color_literal(2):EXPLICIT_STAFF_LINES_COLOR
                        %@% \baca-not-yet-pitched-coloring                                           %! baca.SegmentMaker._color_not_yet_pitched():NOT_YET_PITCHED_COLORING
                            b'4.                                                                     %! baca.make_notes()
            <BLANKLINE>
                            % [Music_Voice measure 2]                                                %! baca.SegmentMaker._comment_measure_numbers()
                        %@% \baca-not-yet-pitched-coloring                                           %! baca.SegmentMaker._color_not_yet_pitched():NOT_YET_PITCHED_COLORING
                            b'4.                                                                     %! baca.make_notes()
            <BLANKLINE>
                            <<                                                                       %! baca.SegmentMaker._make_multimeasure_rest_container(7):PHANTOM
            <BLANKLINE>
                                \context Voice = "Music_Voice"                                       %! baca.SegmentMaker._make_multimeasure_rest_container(4):PHANTOM
                                {                                                                    %! baca.SegmentMaker._make_multimeasure_rest_container(4):PHANTOM
            <BLANKLINE>
                                    % [Music_Voice measure 3]                                        %! baca.SegmentMaker._comment_measure_numbers():baca.SegmentMaker._style_phantom_measures(5):PHANTOM
                                    \abjad-invisible-music-coloring                                  %! baca.SegmentMaker._make_multimeasure_rest_container(2):PHANTOM:NOTE:INVISIBLE_MUSIC_COLORING:baca.SegmentMaker._style_phantom_measures(5)
                                %@% \abjad-invisible-music                                           %! baca.SegmentMaker._make_multimeasure_rest_container(3):PHANTOM:NOTE:INVISIBLE_MUSIC_COMMAND:baca.SegmentMaker._style_phantom_measures(5)
                                %@% \baca-not-yet-pitched-coloring                                   %! baca.SegmentMaker._color_not_yet_pitched():NOT_YET_PITCHED_COLORING:HIDDEN:NOTE:baca.SegmentMaker._style_phantom_measures(5):PHANTOM
                                    b'1 * 1/4                                                        %! baca.SegmentMaker._make_multimeasure_rest_container(1):PHANTOM:HIDDEN:NOTE
                                %@% ^ \baca-duration-multiplier-markup #"1" #"4"                     %! baca.SegmentMaker._label_duration_multipliers():DURATION_MULTIPLIER:HIDDEN:NOTE:PHANTOM:baca.SegmentMaker._style_phantom_measures(5)
            <BLANKLINE>
                                }                                                                    %! baca.SegmentMaker._make_multimeasure_rest_container(4):PHANTOM
            <BLANKLINE>
                                \context Voice = "Rest_Voice"                                        %! baca.SegmentMaker._make_multimeasure_rest_container(6):PHANTOM
                                {                                                                    %! baca.SegmentMaker._make_multimeasure_rest_container(6):PHANTOM
            <BLANKLINE>
                                    % [Rest_Voice measure 3]                                         %! baca.SegmentMaker._comment_measure_numbers():baca.SegmentMaker._style_phantom_measures(5):PHANTOM
                                    \once \override Score.TimeSignature.X-extent = ##f               %! baca.SegmentMaker._style_phantom_measures(6):PHANTOM
                                    \once \override MultiMeasureRest.transparent = ##t               %! baca.SegmentMaker._style_phantom_measures(7):PHANTOM
                                    \stopStaff                                                       %! baca.SegmentMaker._style_phantom_measures(8):PHANTOM
                                    \once \override Staff.StaffSymbol.transparent = ##t              %! baca.SegmentMaker._style_phantom_measures(8):PHANTOM
                                    \startStaff                                                      %! baca.SegmentMaker._style_phantom_measures(8):PHANTOM
                                    R1 * 1/4                                                         %! baca.SegmentMaker._make_multimeasure_rest_container(5):PHANTOM:REST_VOICE:MULTIMEASURE_REST
                                %@% ^ \baca-duration-multiplier-markup #"1" #"4"                     %! baca.SegmentMaker._label_duration_multipliers():DURATION_MULTIPLIER:MULTIMEASURE_REST:PHANTOM:REST_VOICE:baca.SegmentMaker._style_phantom_measures(5)
            <BLANKLINE>
                                }                                                                    %! baca.SegmentMaker._make_multimeasure_rest_container(6):PHANTOM
            <BLANKLINE>
                            >>                                                                       %! baca.SegmentMaker._make_multimeasure_rest_container(7):PHANTOM
            <BLANKLINE>
                        }                                                                            %! baca.SingleStaffScoreTemplate.__call__()
            <BLANKLINE>
                    }                                                                                %! baca.SingleStaffScoreTemplate.__call__()
            <BLANKLINE>
                >>                                                                                   %! baca.SingleStaffScoreTemplate.__call__()
            <BLANKLINE>
            >>                                                                                       %! baca.SingleStaffScoreTemplate.__call__()

    ..  container:: example

        Reapplied staff lines color green:

        >>> maker = baca.SegmentMaker(
        ...     deactivate=[abjad.tags.NOT_YET_PITCHED_COLORING],
        ...     score_template=baca.SingleStaffScoreTemplate(),
        ...     spacing=baca.minimum_duration((1, 24)),
        ...     time_signatures=[(3, 8), (3, 8)],
        ...     )
        >>> maker(
        ...     'Music_Voice',
        ...     baca.make_notes(),
        ...     )

        >>> metadata, persist = {}, {}
        >>> persist['persistent_indicators'] = {}
        >>> persist['persistent_indicators']['Music_Staff'] = [
        ...     abjad.Momento(
        ...         context='Music_Voice',
        ...         prototype='baca.StaffLines',
        ...         value=5,
        ...         )
        ...     ]
        >>> metadata['segment_number'] = 1
        >>> lilypond_file = maker.run(
        ...     environment='docs',
        ...     previous_metadata=metadata,
        ...     previous_persist=persist,
        ...     )
        >>> block = abjad.Block(name='layout')
        >>> block.indent = 0
        >>> lilypond_file.items.insert(0, block)
        >>> abjad.show(lilypond_file, strict=89) # doctest: +SKIP

        ..  docs::

            >>> abjad.f(lilypond_file[abjad.Score], strict=89)
            <BLANKLINE>
            \context Score = "Score"                                                                 %! baca.SingleStaffScoreTemplate.__call__()
            <<                                                                                       %! baca.SingleStaffScoreTemplate.__call__()
            <BLANKLINE>
                \context GlobalContext = "Global_Context"                                            %! abjad.ScoreTemplate._make_global_context()
                <<                                                                                   %! abjad.ScoreTemplate._make_global_context()
            <BLANKLINE>
                    \context GlobalSkips = "Global_Skips"                                            %! abjad.ScoreTemplate._make_global_context()
                    {                                                                                %! abjad.ScoreTemplate._make_global_context()
            <BLANKLINE>
                        % [Global_Skips measure 1]                                                   %! baca.SegmentMaker._comment_measure_numbers()
                        \baca-new-spacing-section #1 #24                                             %! SPACING_COMMAND:baca.HorizontalSpacingSpecifier.__call__(1)
                        \time 3/8                                                                    %! baca.SegmentMaker._make_global_skips(2):baca.SegmentMaker._set_status_tag():EXPLICIT_TIME_SIGNATURE
                        \bar ""                                                                      %! EMPTY_START_BAR:+SEGMENT:baca.SegmentMaker._make_global_skips(4)
                        \baca-time-signature-color #'blue                                            %! baca.SegmentMaker._attach_color_literal(2):EXPLICIT_TIME_SIGNATURE_COLOR
                        s1 * 3/8                                                                     %! baca.SegmentMaker._make_global_skips(1)
            <BLANKLINE>
                        % [Global_Skips measure 2]                                                   %! baca.SegmentMaker._comment_measure_numbers()
                        \baca-new-spacing-section #1 #24                                             %! SPACING_COMMAND:baca.HorizontalSpacingSpecifier.__call__(1)
                        s1 * 3/8                                                                     %! baca.SegmentMaker._make_global_skips(1)
            <BLANKLINE>
                        % [Global_Skips measure 3]                                                   %! baca.SegmentMaker._comment_measure_numbers():baca.SegmentMaker._style_phantom_measures(1):PHANTOM
                        \baca-new-spacing-section #1 #4                                              %! SPACING_COMMAND:baca.HorizontalSpacingSpecifier.__call__(1):baca.SegmentMaker._style_phantom_measures(1):PHANTOM
                        \time 1/4                                                                    %! baca.SegmentMaker._make_global_skips(3):PHANTOM:baca.SegmentMaker._set_status_tag():EXPLICIT_TIME_SIGNATURE:baca.SegmentMaker._style_phantom_measures(1)
                        \baca-time-signature-transparent                                             %! baca.SegmentMaker._style_phantom_measures(2):PHANTOM
                        s1 * 1/4                                                                     %! baca.SegmentMaker._make_global_skips(3):PHANTOM
                        \once \override Score.BarLine.transparent = ##t                              %! baca.SegmentMaker._style_phantom_measures(3):PHANTOM
                        \once \override Score.SpanBar.transparent = ##t                              %! baca.SegmentMaker._style_phantom_measures(3):PHANTOM
            <BLANKLINE>
                    }                                                                                %! abjad.ScoreTemplate._make_global_context()
            <BLANKLINE>
                >>                                                                                   %! abjad.ScoreTemplate._make_global_context()
            <BLANKLINE>
                \context MusicContext = "Music_Context"                                              %! baca.SingleStaffScoreTemplate.__call__()
                <<                                                                                   %! baca.SingleStaffScoreTemplate.__call__()
            <BLANKLINE>
                    \context Staff = "Music_Staff"                                                   %! baca.SingleStaffScoreTemplate.__call__()
                    {                                                                                %! baca.SingleStaffScoreTemplate.__call__()
            <BLANKLINE>
                        \context Voice = "Music_Voice"                                               %! baca.SingleStaffScoreTemplate.__call__()
                        {                                                                            %! baca.SingleStaffScoreTemplate.__call__()
            <BLANKLINE>
                            % [Music_Voice measure 1]                                                %! baca.SegmentMaker._comment_measure_numbers()
                            \stopStaff                                                               %! baca.SegmentMaker._reapply_persistent_indicators(3):baca.SegmentMaker._set_status_tag():REAPPLIED_STAFF_LINES
                            \once \override Staff.StaffSymbol.line-count = 5                         %! baca.SegmentMaker._reapply_persistent_indicators(3):baca.SegmentMaker._set_status_tag():REAPPLIED_STAFF_LINES
                            \startStaff                                                              %! baca.SegmentMaker._reapply_persistent_indicators(3):baca.SegmentMaker._set_status_tag():REAPPLIED_STAFF_LINES
                            \once \override Staff.StaffSymbol.color = #(x11-color 'green4)           %! baca.SegmentMaker._attach_color_literal(2):REAPPLIED_STAFF_LINES_COLOR
                        %@% \baca-not-yet-pitched-coloring                                           %! baca.SegmentMaker._color_not_yet_pitched():NOT_YET_PITCHED_COLORING
                            b'4.                                                                     %! baca.make_notes()
            <BLANKLINE>
                            % [Music_Voice measure 2]                                                %! baca.SegmentMaker._comment_measure_numbers()
                        %@% \baca-not-yet-pitched-coloring                                           %! baca.SegmentMaker._color_not_yet_pitched():NOT_YET_PITCHED_COLORING
                            b'4.                                                                     %! baca.make_notes()
            <BLANKLINE>
                            <<                                                                       %! baca.SegmentMaker._make_multimeasure_rest_container(7):PHANTOM
            <BLANKLINE>
                                \context Voice = "Music_Voice"                                       %! baca.SegmentMaker._make_multimeasure_rest_container(4):PHANTOM
                                {                                                                    %! baca.SegmentMaker._make_multimeasure_rest_container(4):PHANTOM
            <BLANKLINE>
                                    % [Music_Voice measure 3]                                        %! baca.SegmentMaker._comment_measure_numbers():baca.SegmentMaker._style_phantom_measures(5):PHANTOM
                                    \abjad-invisible-music-coloring                                  %! baca.SegmentMaker._make_multimeasure_rest_container(2):PHANTOM:NOTE:INVISIBLE_MUSIC_COLORING:baca.SegmentMaker._style_phantom_measures(5)
                                %@% \abjad-invisible-music                                           %! baca.SegmentMaker._make_multimeasure_rest_container(3):PHANTOM:NOTE:INVISIBLE_MUSIC_COMMAND:baca.SegmentMaker._style_phantom_measures(5)
                                %@% \baca-not-yet-pitched-coloring                                   %! baca.SegmentMaker._color_not_yet_pitched():NOT_YET_PITCHED_COLORING:HIDDEN:NOTE:baca.SegmentMaker._style_phantom_measures(5):PHANTOM
                                    b'1 * 1/4                                                        %! baca.SegmentMaker._make_multimeasure_rest_container(1):PHANTOM:HIDDEN:NOTE
                                %@% ^ \baca-duration-multiplier-markup #"1" #"4"                     %! baca.SegmentMaker._label_duration_multipliers():DURATION_MULTIPLIER:HIDDEN:NOTE:PHANTOM:baca.SegmentMaker._style_phantom_measures(5)
            <BLANKLINE>
                                }                                                                    %! baca.SegmentMaker._make_multimeasure_rest_container(4):PHANTOM
            <BLANKLINE>
                                \context Voice = "Rest_Voice"                                        %! baca.SegmentMaker._make_multimeasure_rest_container(6):PHANTOM
                                {                                                                    %! baca.SegmentMaker._make_multimeasure_rest_container(6):PHANTOM
            <BLANKLINE>
                                    % [Rest_Voice measure 3]                                         %! baca.SegmentMaker._comment_measure_numbers():baca.SegmentMaker._style_phantom_measures(5):PHANTOM
                                    \once \override Score.TimeSignature.X-extent = ##f               %! baca.SegmentMaker._style_phantom_measures(6):PHANTOM
                                    \once \override MultiMeasureRest.transparent = ##t               %! baca.SegmentMaker._style_phantom_measures(7):PHANTOM
                                    \stopStaff                                                       %! baca.SegmentMaker._style_phantom_measures(8):PHANTOM
                                    \once \override Staff.StaffSymbol.transparent = ##t              %! baca.SegmentMaker._style_phantom_measures(8):PHANTOM
                                    \startStaff                                                      %! baca.SegmentMaker._style_phantom_measures(8):PHANTOM
                                    R1 * 1/4                                                         %! baca.SegmentMaker._make_multimeasure_rest_container(5):PHANTOM:REST_VOICE:MULTIMEASURE_REST
                                %@% ^ \baca-duration-multiplier-markup #"1" #"4"                     %! baca.SegmentMaker._label_duration_multipliers():DURATION_MULTIPLIER:MULTIMEASURE_REST:PHANTOM:REST_VOICE:baca.SegmentMaker._style_phantom_measures(5)
            <BLANKLINE>
                                }                                                                    %! baca.SegmentMaker._make_multimeasure_rest_container(6):PHANTOM
            <BLANKLINE>
                            >>                                                                       %! baca.SegmentMaker._make_multimeasure_rest_container(7):PHANTOM
            <BLANKLINE>
                        }                                                                            %! baca.SingleStaffScoreTemplate.__call__()
            <BLANKLINE>
                    }                                                                                %! baca.SingleStaffScoreTemplate.__call__()
            <BLANKLINE>
                >>                                                                                   %! baca.SingleStaffScoreTemplate.__call__()
            <BLANKLINE>
            >>                                                                                       %! baca.SingleStaffScoreTemplate.__call__()

    ..  container:: example

        Redundant staff lines color pink:

        >>> maker = baca.SegmentMaker(
        ...     deactivate=[abjad.tags.NOT_YET_PITCHED_COLORING],
        ...     score_template=baca.SingleStaffScoreTemplate(),
        ...     spacing=baca.minimum_duration((1, 24)),
        ...     time_signatures=[(3, 8), (3, 8)],
        ...     )
        >>> maker(
        ...     'Music_Voice',
        ...     baca.make_notes(),
        ...     baca.staff_lines(5),
        ...     baca.staff_lines(5, selector=baca.leaf(1)),
        ...     )

        >>> lilypond_file = maker.run(environment='docs')
        >>> block = abjad.Block(name='layout')
        >>> block.indent = 0
        >>> lilypond_file.items.insert(0, block)
        >>> abjad.show(lilypond_file, strict=89) # doctest: +SKIP

        ..  docs::

            >>> abjad.f(lilypond_file[abjad.Score], strict=89)
            <BLANKLINE>
            \context Score = "Score"                                                                 %! baca.SingleStaffScoreTemplate.__call__()
            <<                                                                                       %! baca.SingleStaffScoreTemplate.__call__()
            <BLANKLINE>
                \context GlobalContext = "Global_Context"                                            %! abjad.ScoreTemplate._make_global_context()
                <<                                                                                   %! abjad.ScoreTemplate._make_global_context()
            <BLANKLINE>
                    \context GlobalSkips = "Global_Skips"                                            %! abjad.ScoreTemplate._make_global_context()
                    {                                                                                %! abjad.ScoreTemplate._make_global_context()
            <BLANKLINE>
                        % [Global_Skips measure 1]                                                   %! baca.SegmentMaker._comment_measure_numbers()
                        \baca-new-spacing-section #1 #24                                             %! SPACING_COMMAND:baca.HorizontalSpacingSpecifier.__call__(1)
                        \time 3/8                                                                    %! baca.SegmentMaker._make_global_skips(2):baca.SegmentMaker._set_status_tag():EXPLICIT_TIME_SIGNATURE
                        \baca-time-signature-color #'blue                                            %! baca.SegmentMaker._attach_color_literal(2):EXPLICIT_TIME_SIGNATURE_COLOR
                        s1 * 3/8                                                                     %! baca.SegmentMaker._make_global_skips(1)
            <BLANKLINE>
                        % [Global_Skips measure 2]                                                   %! baca.SegmentMaker._comment_measure_numbers()
                        \baca-new-spacing-section #1 #24                                             %! SPACING_COMMAND:baca.HorizontalSpacingSpecifier.__call__(1)
                        s1 * 3/8                                                                     %! baca.SegmentMaker._make_global_skips(1)
            <BLANKLINE>
                        % [Global_Skips measure 3]                                                   %! baca.SegmentMaker._comment_measure_numbers():baca.SegmentMaker._style_phantom_measures(1):PHANTOM
                        \baca-new-spacing-section #1 #4                                              %! SPACING_COMMAND:baca.HorizontalSpacingSpecifier.__call__(1):baca.SegmentMaker._style_phantom_measures(1):PHANTOM
                        \time 1/4                                                                    %! baca.SegmentMaker._make_global_skips(3):PHANTOM:baca.SegmentMaker._set_status_tag():EXPLICIT_TIME_SIGNATURE:baca.SegmentMaker._style_phantom_measures(1)
                        \baca-time-signature-transparent                                             %! baca.SegmentMaker._style_phantom_measures(2):PHANTOM
                        s1 * 1/4                                                                     %! baca.SegmentMaker._make_global_skips(3):PHANTOM
                        \once \override Score.BarLine.transparent = ##t                              %! baca.SegmentMaker._style_phantom_measures(3):PHANTOM
                        \once \override Score.SpanBar.transparent = ##t                              %! baca.SegmentMaker._style_phantom_measures(3):PHANTOM
            <BLANKLINE>
                    }                                                                                %! abjad.ScoreTemplate._make_global_context()
            <BLANKLINE>
                >>                                                                                   %! abjad.ScoreTemplate._make_global_context()
            <BLANKLINE>
                \context MusicContext = "Music_Context"                                              %! baca.SingleStaffScoreTemplate.__call__()
                <<                                                                                   %! baca.SingleStaffScoreTemplate.__call__()
            <BLANKLINE>
                    \context Staff = "Music_Staff"                                                   %! baca.SingleStaffScoreTemplate.__call__()
                    {                                                                                %! baca.SingleStaffScoreTemplate.__call__()
            <BLANKLINE>
                        \context Voice = "Music_Voice"                                               %! baca.SingleStaffScoreTemplate.__call__()
                        {                                                                            %! baca.SingleStaffScoreTemplate.__call__()
            <BLANKLINE>
                            % [Music_Voice measure 1]                                                %! baca.SegmentMaker._comment_measure_numbers()
                            \override Staff.BarLine.bar-extent = #'(-2 . 2)                          %! -PARTS:baca.IndicatorCommand._call():baca.SegmentMaker._set_status_tag():EXPLICIT_BAR_EXTENT
                            \stopStaff                                                               %! baca.staff_lines():baca.IndicatorCommand._call():baca.SegmentMaker._set_status_tag():EXPLICIT_STAFF_LINES
                            \once \override Staff.StaffSymbol.line-count = 5                         %! baca.staff_lines():baca.IndicatorCommand._call():baca.SegmentMaker._set_status_tag():EXPLICIT_STAFF_LINES
                            \startStaff                                                              %! baca.staff_lines():baca.IndicatorCommand._call():baca.SegmentMaker._set_status_tag():EXPLICIT_STAFF_LINES
                            \once \override Staff.StaffSymbol.color = #(x11-color 'blue)             %! baca.SegmentMaker._attach_color_literal(2):EXPLICIT_STAFF_LINES_COLOR
                        %@% \baca-not-yet-pitched-coloring                                           %! baca.SegmentMaker._color_not_yet_pitched():NOT_YET_PITCHED_COLORING
                            b'4.                                                                     %! baca.make_notes()
            <BLANKLINE>
                            % [Music_Voice measure 2]                                                %! baca.SegmentMaker._comment_measure_numbers()
                            \override Staff.BarLine.bar-extent = #'(-2 . 2)                          %! -PARTS:baca.IndicatorCommand._call():baca.SegmentMaker._set_status_tag():REDUNDANT_BAR_EXTENT
                            \stopStaff                                                               %! baca.staff_lines():baca.IndicatorCommand._call():baca.SegmentMaker._set_status_tag():REDUNDANT_STAFF_LINES
                            \once \override Staff.StaffSymbol.line-count = 5                         %! baca.staff_lines():baca.IndicatorCommand._call():baca.SegmentMaker._set_status_tag():REDUNDANT_STAFF_LINES
                            \startStaff                                                              %! baca.staff_lines():baca.IndicatorCommand._call():baca.SegmentMaker._set_status_tag():REDUNDANT_STAFF_LINES
                            \once \override Staff.StaffSymbol.color = #(x11-color 'DeepPink1)        %! baca.SegmentMaker._attach_color_literal(2):REDUNDANT_STAFF_LINES_COLOR
                        %@% \baca-not-yet-pitched-coloring                                           %! baca.SegmentMaker._color_not_yet_pitched():NOT_YET_PITCHED_COLORING
                            b'4.                                                                     %! baca.make_notes()
            <BLANKLINE>
                            <<                                                                       %! baca.SegmentMaker._make_multimeasure_rest_container(7):PHANTOM
            <BLANKLINE>
                                \context Voice = "Music_Voice"                                       %! baca.SegmentMaker._make_multimeasure_rest_container(4):PHANTOM
                                {                                                                    %! baca.SegmentMaker._make_multimeasure_rest_container(4):PHANTOM
            <BLANKLINE>
                                    % [Music_Voice measure 3]                                        %! baca.SegmentMaker._comment_measure_numbers():baca.SegmentMaker._style_phantom_measures(5):PHANTOM
                                    \abjad-invisible-music-coloring                                  %! baca.SegmentMaker._make_multimeasure_rest_container(2):PHANTOM:NOTE:INVISIBLE_MUSIC_COLORING:baca.SegmentMaker._style_phantom_measures(5)
                                %@% \abjad-invisible-music                                           %! baca.SegmentMaker._make_multimeasure_rest_container(3):PHANTOM:NOTE:INVISIBLE_MUSIC_COMMAND:baca.SegmentMaker._style_phantom_measures(5)
                                %@% \baca-not-yet-pitched-coloring                                   %! baca.SegmentMaker._color_not_yet_pitched():NOT_YET_PITCHED_COLORING:HIDDEN:NOTE:baca.SegmentMaker._style_phantom_measures(5):PHANTOM
                                    b'1 * 1/4                                                        %! baca.SegmentMaker._make_multimeasure_rest_container(1):PHANTOM:HIDDEN:NOTE
                                %@% ^ \baca-duration-multiplier-markup #"1" #"4"                     %! baca.SegmentMaker._label_duration_multipliers():DURATION_MULTIPLIER:HIDDEN:NOTE:PHANTOM:baca.SegmentMaker._style_phantom_measures(5)
            <BLANKLINE>
                                }                                                                    %! baca.SegmentMaker._make_multimeasure_rest_container(4):PHANTOM
            <BLANKLINE>
                                \context Voice = "Rest_Voice"                                        %! baca.SegmentMaker._make_multimeasure_rest_container(6):PHANTOM
                                {                                                                    %! baca.SegmentMaker._make_multimeasure_rest_container(6):PHANTOM
            <BLANKLINE>
                                    % [Rest_Voice measure 3]                                         %! baca.SegmentMaker._comment_measure_numbers():baca.SegmentMaker._style_phantom_measures(5):PHANTOM
                                    \once \override Score.TimeSignature.X-extent = ##f               %! baca.SegmentMaker._style_phantom_measures(6):PHANTOM
                                    \once \override MultiMeasureRest.transparent = ##t               %! baca.SegmentMaker._style_phantom_measures(7):PHANTOM
                                    \stopStaff                                                       %! baca.SegmentMaker._style_phantom_measures(8):PHANTOM
                                    \once \override Staff.StaffSymbol.transparent = ##t              %! baca.SegmentMaker._style_phantom_measures(8):PHANTOM
                                    \startStaff                                                      %! baca.SegmentMaker._style_phantom_measures(8):PHANTOM
                                    R1 * 1/4                                                         %! baca.SegmentMaker._make_multimeasure_rest_container(5):PHANTOM:REST_VOICE:MULTIMEASURE_REST
                                %@% ^ \baca-duration-multiplier-markup #"1" #"4"                     %! baca.SegmentMaker._label_duration_multipliers():DURATION_MULTIPLIER:MULTIMEASURE_REST:PHANTOM:REST_VOICE:baca.SegmentMaker._style_phantom_measures(5)
            <BLANKLINE>
                                }                                                                    %! baca.SegmentMaker._make_multimeasure_rest_container(6):PHANTOM
            <BLANKLINE>
                            >>                                                                       %! baca.SegmentMaker._make_multimeasure_rest_container(7):PHANTOM
            <BLANKLINE>
                        }                                                                            %! baca.SingleStaffScoreTemplate.__call__()
            <BLANKLINE>
                    }                                                                                %! baca.SingleStaffScoreTemplate.__call__()
            <BLANKLINE>
                >>                                                                                   %! baca.SingleStaffScoreTemplate.__call__()
            <BLANKLINE>
            >>                                                                                       %! baca.SingleStaffScoreTemplate.__call__()

        Even at the beginning of a segment:

        >>> maker = baca.SegmentMaker(
        ...     deactivate=[abjad.tags.NOT_YET_PITCHED_COLORING],
        ...     score_template=baca.SingleStaffScoreTemplate(),
        ...     spacing=baca.minimum_duration((1, 24)),
        ...     time_signatures=[(3, 8), (3, 8)],
        ...     )
        >>> maker(
        ...     'Music_Voice',
        ...     baca.make_notes(),
        ...     baca.staff_lines(5),
        ...     )

        >>> metadata, persist = {}, {}
        >>> persist['persistent_indicators'] = {}
        >>> persist['persistent_indicators']['Music_Staff'] = [
        ...     abjad.Momento(
        ...         context='Music_Voice',
        ...         prototype='baca.StaffLines',
        ...         value=5,
        ...         )
        ...     ]
        >>> metadata['segment_number'] = 1
        >>> lilypond_file = maker.run(
        ...     environment='docs',
        ...     previous_metadata=metadata,
        ...     previous_persist=persist,
        ...     )
        >>> block = abjad.Block(name='layout')
        >>> block.indent = 0
        >>> lilypond_file.items.insert(0, block)
        >>> abjad.show(lilypond_file, strict=89) # doctest: +SKIP

        ..  docs::

            >>> abjad.f(lilypond_file[abjad.Score], strict=89)
            <BLANKLINE>
            \context Score = "Score"                                                                 %! baca.SingleStaffScoreTemplate.__call__()
            <<                                                                                       %! baca.SingleStaffScoreTemplate.__call__()
            <BLANKLINE>
                \context GlobalContext = "Global_Context"                                            %! abjad.ScoreTemplate._make_global_context()
                <<                                                                                   %! abjad.ScoreTemplate._make_global_context()
            <BLANKLINE>
                    \context GlobalSkips = "Global_Skips"                                            %! abjad.ScoreTemplate._make_global_context()
                    {                                                                                %! abjad.ScoreTemplate._make_global_context()
            <BLANKLINE>
                        % [Global_Skips measure 1]                                                   %! baca.SegmentMaker._comment_measure_numbers()
                        \baca-new-spacing-section #1 #24                                             %! SPACING_COMMAND:baca.HorizontalSpacingSpecifier.__call__(1)
                        \time 3/8                                                                    %! baca.SegmentMaker._make_global_skips(2):baca.SegmentMaker._set_status_tag():EXPLICIT_TIME_SIGNATURE
                        \bar ""                                                                      %! EMPTY_START_BAR:+SEGMENT:baca.SegmentMaker._make_global_skips(4)
                        \baca-time-signature-color #'blue                                            %! baca.SegmentMaker._attach_color_literal(2):EXPLICIT_TIME_SIGNATURE_COLOR
                        s1 * 3/8                                                                     %! baca.SegmentMaker._make_global_skips(1)
            <BLANKLINE>
                        % [Global_Skips measure 2]                                                   %! baca.SegmentMaker._comment_measure_numbers()
                        \baca-new-spacing-section #1 #24                                             %! SPACING_COMMAND:baca.HorizontalSpacingSpecifier.__call__(1)
                        s1 * 3/8                                                                     %! baca.SegmentMaker._make_global_skips(1)
            <BLANKLINE>
                        % [Global_Skips measure 3]                                                   %! baca.SegmentMaker._comment_measure_numbers():baca.SegmentMaker._style_phantom_measures(1):PHANTOM
                        \baca-new-spacing-section #1 #4                                              %! SPACING_COMMAND:baca.HorizontalSpacingSpecifier.__call__(1):baca.SegmentMaker._style_phantom_measures(1):PHANTOM
                        \time 1/4                                                                    %! baca.SegmentMaker._make_global_skips(3):PHANTOM:baca.SegmentMaker._set_status_tag():EXPLICIT_TIME_SIGNATURE:baca.SegmentMaker._style_phantom_measures(1)
                        \baca-time-signature-transparent                                             %! baca.SegmentMaker._style_phantom_measures(2):PHANTOM
                        s1 * 1/4                                                                     %! baca.SegmentMaker._make_global_skips(3):PHANTOM
                        \once \override Score.BarLine.transparent = ##t                              %! baca.SegmentMaker._style_phantom_measures(3):PHANTOM
                        \once \override Score.SpanBar.transparent = ##t                              %! baca.SegmentMaker._style_phantom_measures(3):PHANTOM
            <BLANKLINE>
                    }                                                                                %! abjad.ScoreTemplate._make_global_context()
            <BLANKLINE>
                >>                                                                                   %! abjad.ScoreTemplate._make_global_context()
            <BLANKLINE>
                \context MusicContext = "Music_Context"                                              %! baca.SingleStaffScoreTemplate.__call__()
                <<                                                                                   %! baca.SingleStaffScoreTemplate.__call__()
            <BLANKLINE>
                    \context Staff = "Music_Staff"                                                   %! baca.SingleStaffScoreTemplate.__call__()
                    {                                                                                %! baca.SingleStaffScoreTemplate.__call__()
            <BLANKLINE>
                        \context Voice = "Music_Voice"                                               %! baca.SingleStaffScoreTemplate.__call__()
                        {                                                                            %! baca.SingleStaffScoreTemplate.__call__()
            <BLANKLINE>
                            % [Music_Voice measure 1]                                                %! baca.SegmentMaker._comment_measure_numbers()
                            \override Staff.BarLine.bar-extent = #'(-2 . 2)                          %! -PARTS:baca.IndicatorCommand._call():baca.SegmentMaker._set_status_tag():EXPLICIT_BAR_EXTENT
                            \stopStaff                                                               %! baca.staff_lines():baca.IndicatorCommand._call():baca.SegmentMaker._set_status_tag():REDUNDANT_STAFF_LINES
                            \once \override Staff.StaffSymbol.line-count = 5                         %! baca.staff_lines():baca.IndicatorCommand._call():baca.SegmentMaker._set_status_tag():REDUNDANT_STAFF_LINES
                            \startStaff                                                              %! baca.staff_lines():baca.IndicatorCommand._call():baca.SegmentMaker._set_status_tag():REDUNDANT_STAFF_LINES
                            \once \override Staff.StaffSymbol.color = #(x11-color 'DeepPink1)        %! baca.SegmentMaker._attach_color_literal(2):REDUNDANT_STAFF_LINES_COLOR
                        %@% \baca-not-yet-pitched-coloring                                           %! baca.SegmentMaker._color_not_yet_pitched():NOT_YET_PITCHED_COLORING
                            b'4.                                                                     %! baca.make_notes()
            <BLANKLINE>
                            % [Music_Voice measure 2]                                                %! baca.SegmentMaker._comment_measure_numbers()
                        %@% \baca-not-yet-pitched-coloring                                           %! baca.SegmentMaker._color_not_yet_pitched():NOT_YET_PITCHED_COLORING
                            b'4.                                                                     %! baca.make_notes()
            <BLANKLINE>
                            <<                                                                       %! baca.SegmentMaker._make_multimeasure_rest_container(7):PHANTOM
            <BLANKLINE>
                                \context Voice = "Music_Voice"                                       %! baca.SegmentMaker._make_multimeasure_rest_container(4):PHANTOM
                                {                                                                    %! baca.SegmentMaker._make_multimeasure_rest_container(4):PHANTOM
            <BLANKLINE>
                                    % [Music_Voice measure 3]                                        %! baca.SegmentMaker._comment_measure_numbers():baca.SegmentMaker._style_phantom_measures(5):PHANTOM
                                    \abjad-invisible-music-coloring                                  %! baca.SegmentMaker._make_multimeasure_rest_container(2):PHANTOM:NOTE:INVISIBLE_MUSIC_COLORING:baca.SegmentMaker._style_phantom_measures(5)
                                %@% \abjad-invisible-music                                           %! baca.SegmentMaker._make_multimeasure_rest_container(3):PHANTOM:NOTE:INVISIBLE_MUSIC_COMMAND:baca.SegmentMaker._style_phantom_measures(5)
                                %@% \baca-not-yet-pitched-coloring                                   %! baca.SegmentMaker._color_not_yet_pitched():NOT_YET_PITCHED_COLORING:HIDDEN:NOTE:baca.SegmentMaker._style_phantom_measures(5):PHANTOM
                                    b'1 * 1/4                                                        %! baca.SegmentMaker._make_multimeasure_rest_container(1):PHANTOM:HIDDEN:NOTE
                                %@% ^ \baca-duration-multiplier-markup #"1" #"4"                     %! baca.SegmentMaker._label_duration_multipliers():DURATION_MULTIPLIER:HIDDEN:NOTE:PHANTOM:baca.SegmentMaker._style_phantom_measures(5)
            <BLANKLINE>
                                }                                                                    %! baca.SegmentMaker._make_multimeasure_rest_container(4):PHANTOM
            <BLANKLINE>
                                \context Voice = "Rest_Voice"                                        %! baca.SegmentMaker._make_multimeasure_rest_container(6):PHANTOM
                                {                                                                    %! baca.SegmentMaker._make_multimeasure_rest_container(6):PHANTOM
            <BLANKLINE>
                                    % [Rest_Voice measure 3]                                         %! baca.SegmentMaker._comment_measure_numbers():baca.SegmentMaker._style_phantom_measures(5):PHANTOM
                                    \once \override Score.TimeSignature.X-extent = ##f               %! baca.SegmentMaker._style_phantom_measures(6):PHANTOM
                                    \once \override MultiMeasureRest.transparent = ##t               %! baca.SegmentMaker._style_phantom_measures(7):PHANTOM
                                    \stopStaff                                                       %! baca.SegmentMaker._style_phantom_measures(8):PHANTOM
                                    \once \override Staff.StaffSymbol.transparent = ##t              %! baca.SegmentMaker._style_phantom_measures(8):PHANTOM
                                    \startStaff                                                      %! baca.SegmentMaker._style_phantom_measures(8):PHANTOM
                                    R1 * 1/4                                                         %! baca.SegmentMaker._make_multimeasure_rest_container(5):PHANTOM:REST_VOICE:MULTIMEASURE_REST
                                %@% ^ \baca-duration-multiplier-markup #"1" #"4"                     %! baca.SegmentMaker._label_duration_multipliers():DURATION_MULTIPLIER:MULTIMEASURE_REST:PHANTOM:REST_VOICE:baca.SegmentMaker._style_phantom_measures(5)
            <BLANKLINE>
                                }                                                                    %! baca.SegmentMaker._make_multimeasure_rest_container(6):PHANTOM
            <BLANKLINE>
                            >>                                                                       %! baca.SegmentMaker._make_multimeasure_rest_container(7):PHANTOM
            <BLANKLINE>
                        }                                                                            %! baca.SingleStaffScoreTemplate.__call__()
            <BLANKLINE>
                    }                                                                                %! baca.SingleStaffScoreTemplate.__call__()
            <BLANKLINE>
                >>                                                                                   %! baca.SingleStaffScoreTemplate.__call__()
            <BLANKLINE>
            >>                                                                                       %! baca.SingleStaffScoreTemplate.__call__()

..  container:: example

    Tempo trends.

    ..  container:: example

        >>> breaks = baca.breaks(baca.page([1, 4, (8,)]))
        >>> metronome_marks = abjad.OrderedDict()
        >>> metronome_marks['90'] = abjad.MetronomeMark((1, 4), 90)
        >>> metronome_marks['112'] = abjad.MetronomeMark((1, 4), 112)

    ..  container:: example

        Explicit tempo trends color blue:

        >>> maker = baca.SegmentMaker(
        ...     breaks=breaks,
        ...     deactivate=[abjad.tags.NOT_YET_PITCHED_COLORING],
        ...     metronome_marks=metronome_marks,
        ...     score_template=baca.SingleStaffScoreTemplate(),
        ...     spacing=baca.minimum_duration((1, 25)),
        ...     time_signatures=[(3, 8), (3, 8)],
        ...     )
        >>> maker(
        ...     'Global_Skips',
        ...     baca.metronome_mark(baca.Accelerando()),
        ...     )
        >>> maker(
        ...     'Music_Voice',
        ...     baca.make_notes(),
        ...     )

        >>> lilypond_file = maker.run(environment='docs')
        >>> block = abjad.Block(name='layout')
        >>> block.indent = 0
        >>> lilypond_file.items.insert(0, block)
        >>> abjad.show(lilypond_file, strict=89) # doctest: +SKIP

        ..  docs::

            >>> abjad.f(lilypond_file[abjad.Score], strict=89)
            <BLANKLINE>
            \context Score = "Score"                                                                 %! baca.SingleStaffScoreTemplate.__call__()
            <<                                                                                       %! baca.SingleStaffScoreTemplate.__call__()
            <BLANKLINE>
                \context GlobalContext = "Global_Context"                                            %! abjad.ScoreTemplate._make_global_context()
                <<                                                                                   %! abjad.ScoreTemplate._make_global_context()
            <BLANKLINE>
                    \context GlobalSkips = "Global_Skips"                                            %! abjad.ScoreTemplate._make_global_context()
                    {                                                                                %! abjad.ScoreTemplate._make_global_context()
            <BLANKLINE>
                        % [Global_Skips measure 1]                                                   %! baca.SegmentMaker._comment_measure_numbers()
                        \baca-new-spacing-section #1 #25                                             %! SPACING_COMMAND:baca.HorizontalSpacingSpecifier.__call__(1)
                        \autoPageBreaksOff                                                           %! BREAK:baca.BreakMeasureMap.__call__(1)
                        \noBreak                                                                     %! BREAK:baca.BreakMeasureMap.__call__(2)
                        \baca-lbsd #4 #'(8)                                                          %! BREAK:baca.IndicatorCommand._call()
                        \time 3/8                                                                    %! baca.SegmentMaker._make_global_skips(2):baca.SegmentMaker._set_status_tag():EXPLICIT_TIME_SIGNATURE
                        \baca-time-signature-color #'blue                                            %! baca.SegmentMaker._attach_color_literal(2):EXPLICIT_TIME_SIGNATURE_COLOR
                        \pageBreak                                                                   %! BREAK:baca.IndicatorCommand._call()
                        s1 * 3/8                                                                     %! baca.SegmentMaker._make_global_skips(1)
                    %@% - \abjad-dashed-line-with-arrow                                              %! baca.SegmentMaker._set_status_tag():EXPLICIT_METRONOME_MARK:baca.SegmentMaker._attach_metronome_marks(2)
                    %@% - \tweak bound-details.left.text \markup {                                   %! baca.SegmentMaker._set_status_tag():EXPLICIT_METRONOME_MARK:baca.SegmentMaker._attach_metronome_marks(2)
                    %@%     \concat                                                                  %! baca.SegmentMaker._set_status_tag():EXPLICIT_METRONOME_MARK:baca.SegmentMaker._attach_metronome_marks(2)
                    %@%         {                                                                    %! baca.SegmentMaker._set_status_tag():EXPLICIT_METRONOME_MARK:baca.SegmentMaker._attach_metronome_marks(2)
                    %@%             \large                                                           %! baca.SegmentMaker._set_status_tag():EXPLICIT_METRONOME_MARK:baca.SegmentMaker._attach_metronome_marks(2)
                    %@%                 \upright                                                     %! baca.SegmentMaker._set_status_tag():EXPLICIT_METRONOME_MARK:baca.SegmentMaker._attach_metronome_marks(2)
                    %@%                     accel.                                                   %! baca.SegmentMaker._set_status_tag():EXPLICIT_METRONOME_MARK:baca.SegmentMaker._attach_metronome_marks(2)
                    %@%             \hspace                                                          %! baca.SegmentMaker._set_status_tag():EXPLICIT_METRONOME_MARK:baca.SegmentMaker._attach_metronome_marks(2)
                    %@%                 #0.5                                                         %! baca.SegmentMaker._set_status_tag():EXPLICIT_METRONOME_MARK:baca.SegmentMaker._attach_metronome_marks(2)
                    %@%         }                                                                    %! baca.SegmentMaker._set_status_tag():EXPLICIT_METRONOME_MARK:baca.SegmentMaker._attach_metronome_marks(2)
                    %@%     }                                                                        %! baca.SegmentMaker._set_status_tag():EXPLICIT_METRONOME_MARK:baca.SegmentMaker._attach_metronome_marks(2)
                    %@% \bacaStartTextSpanMM                                                         %! baca.SegmentMaker._set_status_tag():EXPLICIT_METRONOME_MARK:baca.SegmentMaker._attach_metronome_marks(2)
                        - \abjad-dashed-line-with-arrow                                              %! EXPLICIT_METRONOME_MARK_WITH_COLOR:baca.SegmentMaker._attach_metronome_marks(3)
                        - \tweak bound-details.left.text \markup {                                   %! EXPLICIT_METRONOME_MARK_WITH_COLOR:baca.SegmentMaker._attach_metronome_marks(3)
                            \concat                                                                  %! EXPLICIT_METRONOME_MARK_WITH_COLOR:baca.SegmentMaker._attach_metronome_marks(3)
                                {                                                                    %! EXPLICIT_METRONOME_MARK_WITH_COLOR:baca.SegmentMaker._attach_metronome_marks(3)
                                    \with-color                                                      %! EXPLICIT_METRONOME_MARK_WITH_COLOR:baca.SegmentMaker._attach_metronome_marks(3)
                                        #(x11-color 'blue)                                           %! EXPLICIT_METRONOME_MARK_WITH_COLOR:baca.SegmentMaker._attach_metronome_marks(3)
                                        \large                                                       %! EXPLICIT_METRONOME_MARK_WITH_COLOR:baca.SegmentMaker._attach_metronome_marks(3)
                                            \upright                                                 %! EXPLICIT_METRONOME_MARK_WITH_COLOR:baca.SegmentMaker._attach_metronome_marks(3)
                                                accel.                                               %! EXPLICIT_METRONOME_MARK_WITH_COLOR:baca.SegmentMaker._attach_metronome_marks(3)
                                    \hspace                                                          %! EXPLICIT_METRONOME_MARK_WITH_COLOR:baca.SegmentMaker._attach_metronome_marks(3)
                                        #0.5                                                         %! EXPLICIT_METRONOME_MARK_WITH_COLOR:baca.SegmentMaker._attach_metronome_marks(3)
                                }                                                                    %! EXPLICIT_METRONOME_MARK_WITH_COLOR:baca.SegmentMaker._attach_metronome_marks(3)
                            }                                                                        %! EXPLICIT_METRONOME_MARK_WITH_COLOR:baca.SegmentMaker._attach_metronome_marks(3)
                        \bacaStartTextSpanMM                                                         %! EXPLICIT_METRONOME_MARK_WITH_COLOR:baca.SegmentMaker._attach_metronome_marks(3)
            <BLANKLINE>
                        % [Global_Skips measure 2]                                                   %! baca.SegmentMaker._comment_measure_numbers()
                        \baca-new-spacing-section #1 #25                                             %! SPACING_COMMAND:baca.HorizontalSpacingSpecifier.__call__(1)
                        \noBreak                                                                     %! BREAK:baca.BreakMeasureMap.__call__(2)
                        s1 * 3/8                                                                     %! baca.SegmentMaker._make_global_skips(1)
            <BLANKLINE>
                        % [Global_Skips measure 3]                                                   %! baca.SegmentMaker._comment_measure_numbers():baca.SegmentMaker._style_phantom_measures(1):PHANTOM
                        \baca-new-spacing-section #1 #4                                              %! SPACING_COMMAND:baca.HorizontalSpacingSpecifier.__call__(1):baca.SegmentMaker._style_phantom_measures(1):PHANTOM
                        \noBreak                                                                     %! BREAK:baca.BreakMeasureMap.__call__(2):baca.SegmentMaker._style_phantom_measures(1):PHANTOM
                        \time 1/4                                                                    %! baca.SegmentMaker._make_global_skips(3):PHANTOM:baca.SegmentMaker._set_status_tag():EXPLICIT_TIME_SIGNATURE:baca.SegmentMaker._style_phantom_measures(1)
                        \baca-time-signature-transparent                                             %! baca.SegmentMaker._style_phantom_measures(2):PHANTOM
                        s1 * 1/4                                                                     %! baca.SegmentMaker._make_global_skips(3):PHANTOM
                        \bacaStopTextSpanMM                                                          %! EOS_STOP_MM_SPANNER:baca.SegmentMaker._attach_metronome_marks(4):baca.SegmentMaker._style_phantom_measures(1):PHANTOM
                        \once \override Score.BarLine.transparent = ##t                              %! baca.SegmentMaker._style_phantom_measures(3):PHANTOM
                        \once \override Score.SpanBar.transparent = ##t                              %! baca.SegmentMaker._style_phantom_measures(3):PHANTOM
            <BLANKLINE>
                    }                                                                                %! abjad.ScoreTemplate._make_global_context()
            <BLANKLINE>
                >>                                                                                   %! abjad.ScoreTemplate._make_global_context()
            <BLANKLINE>
                \context MusicContext = "Music_Context"                                              %! baca.SingleStaffScoreTemplate.__call__()
                <<                                                                                   %! baca.SingleStaffScoreTemplate.__call__()
            <BLANKLINE>
                    \context Staff = "Music_Staff"                                                   %! baca.SingleStaffScoreTemplate.__call__()
                    {                                                                                %! baca.SingleStaffScoreTemplate.__call__()
            <BLANKLINE>
                        \context Voice = "Music_Voice"                                               %! baca.SingleStaffScoreTemplate.__call__()
                        {                                                                            %! baca.SingleStaffScoreTemplate.__call__()
            <BLANKLINE>
                            % [Music_Voice measure 1]                                                %! baca.SegmentMaker._comment_measure_numbers()
                        %@% \baca-not-yet-pitched-coloring                                           %! baca.SegmentMaker._color_not_yet_pitched():NOT_YET_PITCHED_COLORING
                            b'4.                                                                     %! baca.make_notes()
            <BLANKLINE>
                            % [Music_Voice measure 2]                                                %! baca.SegmentMaker._comment_measure_numbers()
                        %@% \baca-not-yet-pitched-coloring                                           %! baca.SegmentMaker._color_not_yet_pitched():NOT_YET_PITCHED_COLORING
                            b'4.                                                                     %! baca.make_notes()
            <BLANKLINE>
                            <<                                                                       %! baca.SegmentMaker._make_multimeasure_rest_container(7):PHANTOM
            <BLANKLINE>
                                \context Voice = "Music_Voice"                                       %! baca.SegmentMaker._make_multimeasure_rest_container(4):PHANTOM
                                {                                                                    %! baca.SegmentMaker._make_multimeasure_rest_container(4):PHANTOM
            <BLANKLINE>
                                    % [Music_Voice measure 3]                                        %! baca.SegmentMaker._comment_measure_numbers():baca.SegmentMaker._style_phantom_measures(5):PHANTOM
                                    \abjad-invisible-music-coloring                                  %! baca.SegmentMaker._make_multimeasure_rest_container(2):PHANTOM:NOTE:INVISIBLE_MUSIC_COLORING:baca.SegmentMaker._style_phantom_measures(5)
                                %@% \abjad-invisible-music                                           %! baca.SegmentMaker._make_multimeasure_rest_container(3):PHANTOM:NOTE:INVISIBLE_MUSIC_COMMAND:baca.SegmentMaker._style_phantom_measures(5)
                                %@% \baca-not-yet-pitched-coloring                                   %! baca.SegmentMaker._color_not_yet_pitched():NOT_YET_PITCHED_COLORING:HIDDEN:NOTE:baca.SegmentMaker._style_phantom_measures(5):PHANTOM
                                    b'1 * 1/4                                                        %! baca.SegmentMaker._make_multimeasure_rest_container(1):PHANTOM:HIDDEN:NOTE
                                %@% ^ \baca-duration-multiplier-markup #"1" #"4"                     %! baca.SegmentMaker._label_duration_multipliers():DURATION_MULTIPLIER:HIDDEN:NOTE:PHANTOM:baca.SegmentMaker._style_phantom_measures(5)
            <BLANKLINE>
                                }                                                                    %! baca.SegmentMaker._make_multimeasure_rest_container(4):PHANTOM
            <BLANKLINE>
                                \context Voice = "Rest_Voice"                                        %! baca.SegmentMaker._make_multimeasure_rest_container(6):PHANTOM
                                {                                                                    %! baca.SegmentMaker._make_multimeasure_rest_container(6):PHANTOM
            <BLANKLINE>
                                    % [Rest_Voice measure 3]                                         %! baca.SegmentMaker._comment_measure_numbers():baca.SegmentMaker._style_phantom_measures(5):PHANTOM
                                    \once \override Score.TimeSignature.X-extent = ##f               %! baca.SegmentMaker._style_phantom_measures(6):PHANTOM
                                    \once \override MultiMeasureRest.transparent = ##t               %! baca.SegmentMaker._style_phantom_measures(7):PHANTOM
                                    \stopStaff                                                       %! baca.SegmentMaker._style_phantom_measures(8):PHANTOM
                                    \once \override Staff.StaffSymbol.transparent = ##t              %! baca.SegmentMaker._style_phantom_measures(8):PHANTOM
                                    \startStaff                                                      %! baca.SegmentMaker._style_phantom_measures(8):PHANTOM
                                    R1 * 1/4                                                         %! baca.SegmentMaker._make_multimeasure_rest_container(5):PHANTOM:REST_VOICE:MULTIMEASURE_REST
                                %@% ^ \baca-duration-multiplier-markup #"1" #"4"                     %! baca.SegmentMaker._label_duration_multipliers():DURATION_MULTIPLIER:MULTIMEASURE_REST:PHANTOM:REST_VOICE:baca.SegmentMaker._style_phantom_measures(5)
            <BLANKLINE>
                                }                                                                    %! baca.SegmentMaker._make_multimeasure_rest_container(6):PHANTOM
            <BLANKLINE>
                            >>                                                                       %! baca.SegmentMaker._make_multimeasure_rest_container(7):PHANTOM
            <BLANKLINE>
                        }                                                                            %! baca.SingleStaffScoreTemplate.__call__()
            <BLANKLINE>
                    }                                                                                %! baca.SingleStaffScoreTemplate.__call__()
            <BLANKLINE>
                >>                                                                                   %! baca.SingleStaffScoreTemplate.__call__()
            <BLANKLINE>
            >>                                                                                       %! baca.SingleStaffScoreTemplate.__call__()

        Even after a previous tempo trend:

        >>> maker = baca.SegmentMaker(
        ...     breaks=breaks,
        ...     deactivate=[abjad.tags.NOT_YET_PITCHED_COLORING],
        ...     metronome_marks=metronome_marks,
        ...     score_template=baca.SingleStaffScoreTemplate(),
        ...     spacing=baca.minimum_duration((1, 24)),
        ...     time_signatures=[(3, 8), (3, 8)],
        ...     )
        >>> maker(
        ...     'Global_Skips',
        ...     baca.metronome_mark(baca.Accelerando()),
        ...     baca.text_spanner_staff_padding(4),
        ...     )
        >>> maker(
        ...     'Music_Voice',
        ...     baca.make_notes(),
        ...     )

        >>> metadata, persist = {}, {}
        >>> persist['persistent_indicators'] = {}
        >>> persist['persistent_indicators']['Score'] = [
        ...     abjad.Momento(
        ...         context='Global_Skips',
        ...         prototype='baca.Ritardando',
        ...         )
        ...     ]
        >>> metadata['segment_number'] = 1
        >>> lilypond_file = maker.run(
        ...     environment='docs',
        ...     previous_metadata=metadata,
        ...     previous_persist=persist,
        ...     )
        >>> block = abjad.Block(name='layout')
        >>> block.indent = 0
        >>> lilypond_file.items.insert(0, block)
        >>> abjad.show(lilypond_file, strict=89) # doctest: +SKIP

        ..  docs::

            >>> abjad.f(lilypond_file[abjad.Score], strict=89)
            <BLANKLINE>
            \context Score = "Score"                                                                 %! baca.SingleStaffScoreTemplate.__call__()
            <<                                                                                       %! baca.SingleStaffScoreTemplate.__call__()
            <BLANKLINE>
                \context GlobalContext = "Global_Context"                                            %! abjad.ScoreTemplate._make_global_context()
                <<                                                                                   %! abjad.ScoreTemplate._make_global_context()
            <BLANKLINE>
                    \context GlobalSkips = "Global_Skips"                                            %! abjad.ScoreTemplate._make_global_context()
                    {                                                                                %! abjad.ScoreTemplate._make_global_context()
            <BLANKLINE>
                        % [Global_Skips measure 1]                                                   %! baca.SegmentMaker._comment_measure_numbers()
                        \baca-new-spacing-section #1 #24                                             %! SPACING_COMMAND:baca.HorizontalSpacingSpecifier.__call__(1)
                        \override TextSpanner.staff-padding = #4                                     %! baca.text_spanner_staff_padding():baca.OverrideCommand._call(1)
                        \autoPageBreaksOff                                                           %! BREAK:baca.BreakMeasureMap.__call__(1)
                        \noBreak                                                                     %! BREAK:baca.BreakMeasureMap.__call__(2)
                        \baca-lbsd #4 #'(8)                                                          %! BREAK:baca.IndicatorCommand._call()
                        \time 3/8                                                                    %! baca.SegmentMaker._make_global_skips(2):baca.SegmentMaker._set_status_tag():EXPLICIT_TIME_SIGNATURE
                        \bar ""                                                                      %! EMPTY_START_BAR:+SEGMENT:baca.SegmentMaker._make_global_skips(4)
                        \baca-time-signature-color #'blue                                            %! baca.SegmentMaker._attach_color_literal(2):EXPLICIT_TIME_SIGNATURE_COLOR
                        \pageBreak                                                                   %! BREAK:baca.IndicatorCommand._call()
                        s1 * 3/8                                                                     %! baca.SegmentMaker._make_global_skips(1)
                    %@% - \abjad-dashed-line-with-arrow                                              %! baca.SegmentMaker._set_status_tag():EXPLICIT_METRONOME_MARK:baca.SegmentMaker._attach_metronome_marks(2)
                    %@% - \tweak bound-details.left.text \markup {                                   %! baca.SegmentMaker._set_status_tag():EXPLICIT_METRONOME_MARK:baca.SegmentMaker._attach_metronome_marks(2)
                    %@%     \concat                                                                  %! baca.SegmentMaker._set_status_tag():EXPLICIT_METRONOME_MARK:baca.SegmentMaker._attach_metronome_marks(2)
                    %@%         {                                                                    %! baca.SegmentMaker._set_status_tag():EXPLICIT_METRONOME_MARK:baca.SegmentMaker._attach_metronome_marks(2)
                    %@%             \large                                                           %! baca.SegmentMaker._set_status_tag():EXPLICIT_METRONOME_MARK:baca.SegmentMaker._attach_metronome_marks(2)
                    %@%                 \upright                                                     %! baca.SegmentMaker._set_status_tag():EXPLICIT_METRONOME_MARK:baca.SegmentMaker._attach_metronome_marks(2)
                    %@%                     accel.                                                   %! baca.SegmentMaker._set_status_tag():EXPLICIT_METRONOME_MARK:baca.SegmentMaker._attach_metronome_marks(2)
                    %@%             \hspace                                                          %! baca.SegmentMaker._set_status_tag():EXPLICIT_METRONOME_MARK:baca.SegmentMaker._attach_metronome_marks(2)
                    %@%                 #0.5                                                         %! baca.SegmentMaker._set_status_tag():EXPLICIT_METRONOME_MARK:baca.SegmentMaker._attach_metronome_marks(2)
                    %@%         }                                                                    %! baca.SegmentMaker._set_status_tag():EXPLICIT_METRONOME_MARK:baca.SegmentMaker._attach_metronome_marks(2)
                    %@%     }                                                                        %! baca.SegmentMaker._set_status_tag():EXPLICIT_METRONOME_MARK:baca.SegmentMaker._attach_metronome_marks(2)
                    %@% \bacaStartTextSpanMM                                                         %! baca.SegmentMaker._set_status_tag():EXPLICIT_METRONOME_MARK:baca.SegmentMaker._attach_metronome_marks(2)
                        - \abjad-dashed-line-with-arrow                                              %! EXPLICIT_METRONOME_MARK_WITH_COLOR:baca.SegmentMaker._attach_metronome_marks(3)
                        - \tweak bound-details.left.text \markup {                                   %! EXPLICIT_METRONOME_MARK_WITH_COLOR:baca.SegmentMaker._attach_metronome_marks(3)
                            \concat                                                                  %! EXPLICIT_METRONOME_MARK_WITH_COLOR:baca.SegmentMaker._attach_metronome_marks(3)
                                {                                                                    %! EXPLICIT_METRONOME_MARK_WITH_COLOR:baca.SegmentMaker._attach_metronome_marks(3)
                                    \with-color                                                      %! EXPLICIT_METRONOME_MARK_WITH_COLOR:baca.SegmentMaker._attach_metronome_marks(3)
                                        #(x11-color 'blue)                                           %! EXPLICIT_METRONOME_MARK_WITH_COLOR:baca.SegmentMaker._attach_metronome_marks(3)
                                        \large                                                       %! EXPLICIT_METRONOME_MARK_WITH_COLOR:baca.SegmentMaker._attach_metronome_marks(3)
                                            \upright                                                 %! EXPLICIT_METRONOME_MARK_WITH_COLOR:baca.SegmentMaker._attach_metronome_marks(3)
                                                accel.                                               %! EXPLICIT_METRONOME_MARK_WITH_COLOR:baca.SegmentMaker._attach_metronome_marks(3)
                                    \hspace                                                          %! EXPLICIT_METRONOME_MARK_WITH_COLOR:baca.SegmentMaker._attach_metronome_marks(3)
                                        #0.5                                                         %! EXPLICIT_METRONOME_MARK_WITH_COLOR:baca.SegmentMaker._attach_metronome_marks(3)
                                }                                                                    %! EXPLICIT_METRONOME_MARK_WITH_COLOR:baca.SegmentMaker._attach_metronome_marks(3)
                            }                                                                        %! EXPLICIT_METRONOME_MARK_WITH_COLOR:baca.SegmentMaker._attach_metronome_marks(3)
                        \bacaStartTextSpanMM                                                         %! EXPLICIT_METRONOME_MARK_WITH_COLOR:baca.SegmentMaker._attach_metronome_marks(3)
            <BLANKLINE>
                        % [Global_Skips measure 2]                                                   %! baca.SegmentMaker._comment_measure_numbers()
                        \baca-new-spacing-section #1 #24                                             %! SPACING_COMMAND:baca.HorizontalSpacingSpecifier.__call__(1)
                        \noBreak                                                                     %! BREAK:baca.BreakMeasureMap.__call__(2)
                        s1 * 3/8                                                                     %! baca.SegmentMaker._make_global_skips(1)
                        \revert TextSpanner.staff-padding                                            %! baca.text_spanner_staff_padding():baca.OverrideCommand._call(2)
            <BLANKLINE>
                        % [Global_Skips measure 3]                                                   %! baca.SegmentMaker._comment_measure_numbers():baca.SegmentMaker._style_phantom_measures(1):PHANTOM
                        \baca-new-spacing-section #1 #4                                              %! SPACING_COMMAND:baca.HorizontalSpacingSpecifier.__call__(1):baca.SegmentMaker._style_phantom_measures(1):PHANTOM
                        \noBreak                                                                     %! BREAK:baca.BreakMeasureMap.__call__(2):baca.SegmentMaker._style_phantom_measures(1):PHANTOM
                        \time 1/4                                                                    %! baca.SegmentMaker._make_global_skips(3):PHANTOM:baca.SegmentMaker._set_status_tag():EXPLICIT_TIME_SIGNATURE:baca.SegmentMaker._style_phantom_measures(1)
                        \baca-time-signature-transparent                                             %! baca.SegmentMaker._style_phantom_measures(2):PHANTOM
                        s1 * 1/4                                                                     %! baca.SegmentMaker._make_global_skips(3):PHANTOM
                        \bacaStopTextSpanMM                                                          %! EOS_STOP_MM_SPANNER:baca.SegmentMaker._attach_metronome_marks(4):baca.SegmentMaker._style_phantom_measures(1):PHANTOM
                        \once \override Score.BarLine.transparent = ##t                              %! baca.SegmentMaker._style_phantom_measures(3):PHANTOM
                        \once \override Score.SpanBar.transparent = ##t                              %! baca.SegmentMaker._style_phantom_measures(3):PHANTOM
            <BLANKLINE>
                    }                                                                                %! abjad.ScoreTemplate._make_global_context()
            <BLANKLINE>
                >>                                                                                   %! abjad.ScoreTemplate._make_global_context()
            <BLANKLINE>
                \context MusicContext = "Music_Context"                                              %! baca.SingleStaffScoreTemplate.__call__()
                <<                                                                                   %! baca.SingleStaffScoreTemplate.__call__()
            <BLANKLINE>
                    \context Staff = "Music_Staff"                                                   %! baca.SingleStaffScoreTemplate.__call__()
                    {                                                                                %! baca.SingleStaffScoreTemplate.__call__()
            <BLANKLINE>
                        \context Voice = "Music_Voice"                                               %! baca.SingleStaffScoreTemplate.__call__()
                        {                                                                            %! baca.SingleStaffScoreTemplate.__call__()
            <BLANKLINE>
                            % [Music_Voice measure 1]                                                %! baca.SegmentMaker._comment_measure_numbers()
                        %@% \baca-not-yet-pitched-coloring                                           %! baca.SegmentMaker._color_not_yet_pitched():NOT_YET_PITCHED_COLORING
                            b'4.                                                                     %! baca.make_notes()
            <BLANKLINE>
                            % [Music_Voice measure 2]                                                %! baca.SegmentMaker._comment_measure_numbers()
                        %@% \baca-not-yet-pitched-coloring                                           %! baca.SegmentMaker._color_not_yet_pitched():NOT_YET_PITCHED_COLORING
                            b'4.                                                                     %! baca.make_notes()
            <BLANKLINE>
                            <<                                                                       %! baca.SegmentMaker._make_multimeasure_rest_container(7):PHANTOM
            <BLANKLINE>
                                \context Voice = "Music_Voice"                                       %! baca.SegmentMaker._make_multimeasure_rest_container(4):PHANTOM
                                {                                                                    %! baca.SegmentMaker._make_multimeasure_rest_container(4):PHANTOM
            <BLANKLINE>
                                    % [Music_Voice measure 3]                                        %! baca.SegmentMaker._comment_measure_numbers():baca.SegmentMaker._style_phantom_measures(5):PHANTOM
                                    \abjad-invisible-music-coloring                                  %! baca.SegmentMaker._make_multimeasure_rest_container(2):PHANTOM:NOTE:INVISIBLE_MUSIC_COLORING:baca.SegmentMaker._style_phantom_measures(5)
                                %@% \abjad-invisible-music                                           %! baca.SegmentMaker._make_multimeasure_rest_container(3):PHANTOM:NOTE:INVISIBLE_MUSIC_COMMAND:baca.SegmentMaker._style_phantom_measures(5)
                                %@% \baca-not-yet-pitched-coloring                                   %! baca.SegmentMaker._color_not_yet_pitched():NOT_YET_PITCHED_COLORING:HIDDEN:NOTE:baca.SegmentMaker._style_phantom_measures(5):PHANTOM
                                    b'1 * 1/4                                                        %! baca.SegmentMaker._make_multimeasure_rest_container(1):PHANTOM:HIDDEN:NOTE
                                %@% ^ \baca-duration-multiplier-markup #"1" #"4"                     %! baca.SegmentMaker._label_duration_multipliers():DURATION_MULTIPLIER:HIDDEN:NOTE:PHANTOM:baca.SegmentMaker._style_phantom_measures(5)
            <BLANKLINE>
                                }                                                                    %! baca.SegmentMaker._make_multimeasure_rest_container(4):PHANTOM
            <BLANKLINE>
                                \context Voice = "Rest_Voice"                                        %! baca.SegmentMaker._make_multimeasure_rest_container(6):PHANTOM
                                {                                                                    %! baca.SegmentMaker._make_multimeasure_rest_container(6):PHANTOM
            <BLANKLINE>
                                    % [Rest_Voice measure 3]                                         %! baca.SegmentMaker._comment_measure_numbers():baca.SegmentMaker._style_phantom_measures(5):PHANTOM
                                    \once \override Score.TimeSignature.X-extent = ##f               %! baca.SegmentMaker._style_phantom_measures(6):PHANTOM
                                    \once \override MultiMeasureRest.transparent = ##t               %! baca.SegmentMaker._style_phantom_measures(7):PHANTOM
                                    \stopStaff                                                       %! baca.SegmentMaker._style_phantom_measures(8):PHANTOM
                                    \once \override Staff.StaffSymbol.transparent = ##t              %! baca.SegmentMaker._style_phantom_measures(8):PHANTOM
                                    \startStaff                                                      %! baca.SegmentMaker._style_phantom_measures(8):PHANTOM
                                    R1 * 1/4                                                         %! baca.SegmentMaker._make_multimeasure_rest_container(5):PHANTOM:REST_VOICE:MULTIMEASURE_REST
                                %@% ^ \baca-duration-multiplier-markup #"1" #"4"                     %! baca.SegmentMaker._label_duration_multipliers():DURATION_MULTIPLIER:MULTIMEASURE_REST:PHANTOM:REST_VOICE:baca.SegmentMaker._style_phantom_measures(5)
            <BLANKLINE>
                                }                                                                    %! baca.SegmentMaker._make_multimeasure_rest_container(6):PHANTOM
            <BLANKLINE>
                            >>                                                                       %! baca.SegmentMaker._make_multimeasure_rest_container(7):PHANTOM
            <BLANKLINE>
                        }                                                                            %! baca.SingleStaffScoreTemplate.__call__()
            <BLANKLINE>
                    }                                                                                %! baca.SingleStaffScoreTemplate.__call__()
            <BLANKLINE>
                >>                                                                                   %! baca.SingleStaffScoreTemplate.__call__()
            <BLANKLINE>
            >>                                                                                       %! baca.SingleStaffScoreTemplate.__call__()

    ..  container:: example

        Reapplied tempo trends color green:

        >>> maker = baca.SegmentMaker(
        ...     breaks=breaks,
        ...     deactivate=[abjad.tags.NOT_YET_PITCHED_COLORING],
        ...     metronome_marks=metronome_marks,
        ...     score_template=baca.SingleStaffScoreTemplate(),
        ...     spacing=baca.minimum_duration((1, 24)),
        ...     time_signatures=[(3, 8), (3, 8)],
        ...     )
        >>> maker(
        ...     'Music_Voice',
        ...     baca.make_notes(),
        ...     )
        >>> maker(
        ...     'Global_Skips',
        ...     baca.text_spanner_staff_padding(4),
        ...     )

        >>> metadata, persist = {}, {}
        >>> persist['persistent_indicators'] = {}
        >>> persist['persistent_indicators']['Score'] = [
        ...     abjad.Momento(
        ...         context='Global_Skips',
        ...         prototype='baca.Accelerando',
        ...         )
        ...     ]
        >>> metadata['segment_number'] = 1
        >>> lilypond_file = maker.run(
        ...     environment='docs',
        ...     previous_metadata=metadata,
        ...     previous_persist=persist,
        ...     )
        >>> block = abjad.Block(name='layout')
        >>> block.indent = 0
        >>> lilypond_file.items.insert(0, block)
        >>> abjad.show(lilypond_file, strict=89) # doctest: +SKIP

        ..  docs::

            >>> abjad.f(lilypond_file[abjad.Score], strict=89)
            <BLANKLINE>
            \context Score = "Score"                                                                 %! baca.SingleStaffScoreTemplate.__call__()
            <<                                                                                       %! baca.SingleStaffScoreTemplate.__call__()
            <BLANKLINE>
                \context GlobalContext = "Global_Context"                                            %! abjad.ScoreTemplate._make_global_context()
                <<                                                                                   %! abjad.ScoreTemplate._make_global_context()
            <BLANKLINE>
                    \context GlobalSkips = "Global_Skips"                                            %! abjad.ScoreTemplate._make_global_context()
                    {                                                                                %! abjad.ScoreTemplate._make_global_context()
            <BLANKLINE>
                        % [Global_Skips measure 1]                                                   %! baca.SegmentMaker._comment_measure_numbers()
                        \baca-new-spacing-section #1 #24                                             %! SPACING_COMMAND:baca.HorizontalSpacingSpecifier.__call__(1)
                        \override TextSpanner.staff-padding = #4                                     %! baca.text_spanner_staff_padding():baca.OverrideCommand._call(1)
                        \autoPageBreaksOff                                                           %! BREAK:baca.BreakMeasureMap.__call__(1)
                        \noBreak                                                                     %! BREAK:baca.BreakMeasureMap.__call__(2)
                        \baca-lbsd #4 #'(8)                                                          %! BREAK:baca.IndicatorCommand._call()
                        \time 3/8                                                                    %! baca.SegmentMaker._make_global_skips(2):baca.SegmentMaker._set_status_tag():EXPLICIT_TIME_SIGNATURE
                        \bar ""                                                                      %! EMPTY_START_BAR:+SEGMENT:baca.SegmentMaker._make_global_skips(4)
                        \baca-time-signature-color #'blue                                            %! baca.SegmentMaker._attach_color_literal(2):EXPLICIT_TIME_SIGNATURE_COLOR
                        \pageBreak                                                                   %! BREAK:baca.IndicatorCommand._call()
                        s1 * 3/8                                                                     %! baca.SegmentMaker._make_global_skips(1)
                    %@% - \abjad-dashed-line-with-arrow                                              %! baca.SegmentMaker._reapply_persistent_indicators(2):baca.SegmentMaker._set_status_tag():REAPPLIED_METRONOME_MARK:baca.SegmentMaker._attach_metronome_marks(2)
                    %@% - \tweak bound-details.left.text \markup {                                   %! baca.SegmentMaker._reapply_persistent_indicators(2):baca.SegmentMaker._set_status_tag():REAPPLIED_METRONOME_MARK:baca.SegmentMaker._attach_metronome_marks(2)
                    %@%     \concat                                                                  %! baca.SegmentMaker._reapply_persistent_indicators(2):baca.SegmentMaker._set_status_tag():REAPPLIED_METRONOME_MARK:baca.SegmentMaker._attach_metronome_marks(2)
                    %@%         {                                                                    %! baca.SegmentMaker._reapply_persistent_indicators(2):baca.SegmentMaker._set_status_tag():REAPPLIED_METRONOME_MARK:baca.SegmentMaker._attach_metronome_marks(2)
                    %@%             \large                                                           %! baca.SegmentMaker._reapply_persistent_indicators(2):baca.SegmentMaker._set_status_tag():REAPPLIED_METRONOME_MARK:baca.SegmentMaker._attach_metronome_marks(2)
                    %@%                 \upright                                                     %! baca.SegmentMaker._reapply_persistent_indicators(2):baca.SegmentMaker._set_status_tag():REAPPLIED_METRONOME_MARK:baca.SegmentMaker._attach_metronome_marks(2)
                    %@%                     accel.                                                   %! baca.SegmentMaker._reapply_persistent_indicators(2):baca.SegmentMaker._set_status_tag():REAPPLIED_METRONOME_MARK:baca.SegmentMaker._attach_metronome_marks(2)
                    %@%             \hspace                                                          %! baca.SegmentMaker._reapply_persistent_indicators(2):baca.SegmentMaker._set_status_tag():REAPPLIED_METRONOME_MARK:baca.SegmentMaker._attach_metronome_marks(2)
                    %@%                 #0.5                                                         %! baca.SegmentMaker._reapply_persistent_indicators(2):baca.SegmentMaker._set_status_tag():REAPPLIED_METRONOME_MARK:baca.SegmentMaker._attach_metronome_marks(2)
                    %@%         }                                                                    %! baca.SegmentMaker._reapply_persistent_indicators(2):baca.SegmentMaker._set_status_tag():REAPPLIED_METRONOME_MARK:baca.SegmentMaker._attach_metronome_marks(2)
                    %@%     }                                                                        %! baca.SegmentMaker._reapply_persistent_indicators(2):baca.SegmentMaker._set_status_tag():REAPPLIED_METRONOME_MARK:baca.SegmentMaker._attach_metronome_marks(2)
                    %@% \bacaStartTextSpanMM                                                         %! baca.SegmentMaker._reapply_persistent_indicators(2):baca.SegmentMaker._set_status_tag():REAPPLIED_METRONOME_MARK:baca.SegmentMaker._attach_metronome_marks(2)
                        - \abjad-dashed-line-with-arrow                                              %! REAPPLIED_METRONOME_MARK_WITH_COLOR:baca.SegmentMaker._attach_metronome_marks(3)
                        - \tweak bound-details.left.text \markup {                                   %! REAPPLIED_METRONOME_MARK_WITH_COLOR:baca.SegmentMaker._attach_metronome_marks(3)
                            \concat                                                                  %! REAPPLIED_METRONOME_MARK_WITH_COLOR:baca.SegmentMaker._attach_metronome_marks(3)
                                {                                                                    %! REAPPLIED_METRONOME_MARK_WITH_COLOR:baca.SegmentMaker._attach_metronome_marks(3)
                                    \with-color                                                      %! REAPPLIED_METRONOME_MARK_WITH_COLOR:baca.SegmentMaker._attach_metronome_marks(3)
                                        #(x11-color 'green4)                                         %! REAPPLIED_METRONOME_MARK_WITH_COLOR:baca.SegmentMaker._attach_metronome_marks(3)
                                        \large                                                       %! REAPPLIED_METRONOME_MARK_WITH_COLOR:baca.SegmentMaker._attach_metronome_marks(3)
                                            \upright                                                 %! REAPPLIED_METRONOME_MARK_WITH_COLOR:baca.SegmentMaker._attach_metronome_marks(3)
                                                accel.                                               %! REAPPLIED_METRONOME_MARK_WITH_COLOR:baca.SegmentMaker._attach_metronome_marks(3)
                                    \hspace                                                          %! REAPPLIED_METRONOME_MARK_WITH_COLOR:baca.SegmentMaker._attach_metronome_marks(3)
                                        #0.5                                                         %! REAPPLIED_METRONOME_MARK_WITH_COLOR:baca.SegmentMaker._attach_metronome_marks(3)
                                }                                                                    %! REAPPLIED_METRONOME_MARK_WITH_COLOR:baca.SegmentMaker._attach_metronome_marks(3)
                            }                                                                        %! REAPPLIED_METRONOME_MARK_WITH_COLOR:baca.SegmentMaker._attach_metronome_marks(3)
                        \bacaStartTextSpanMM                                                         %! REAPPLIED_METRONOME_MARK_WITH_COLOR:baca.SegmentMaker._attach_metronome_marks(3)
            <BLANKLINE>
                        % [Global_Skips measure 2]                                                   %! baca.SegmentMaker._comment_measure_numbers()
                        \baca-new-spacing-section #1 #24                                             %! SPACING_COMMAND:baca.HorizontalSpacingSpecifier.__call__(1)
                        \noBreak                                                                     %! BREAK:baca.BreakMeasureMap.__call__(2)
                        s1 * 3/8                                                                     %! baca.SegmentMaker._make_global_skips(1)
                        \revert TextSpanner.staff-padding                                            %! baca.text_spanner_staff_padding():baca.OverrideCommand._call(2)
            <BLANKLINE>
                        % [Global_Skips measure 3]                                                   %! baca.SegmentMaker._comment_measure_numbers():baca.SegmentMaker._style_phantom_measures(1):PHANTOM
                        \baca-new-spacing-section #1 #4                                              %! SPACING_COMMAND:baca.HorizontalSpacingSpecifier.__call__(1):baca.SegmentMaker._style_phantom_measures(1):PHANTOM
                        \noBreak                                                                     %! BREAK:baca.BreakMeasureMap.__call__(2):baca.SegmentMaker._style_phantom_measures(1):PHANTOM
                        \time 1/4                                                                    %! baca.SegmentMaker._make_global_skips(3):PHANTOM:baca.SegmentMaker._set_status_tag():EXPLICIT_TIME_SIGNATURE:baca.SegmentMaker._style_phantom_measures(1)
                        \baca-time-signature-transparent                                             %! baca.SegmentMaker._style_phantom_measures(2):PHANTOM
                        s1 * 1/4                                                                     %! baca.SegmentMaker._make_global_skips(3):PHANTOM
                        \bacaStopTextSpanMM                                                          %! EOS_STOP_MM_SPANNER:baca.SegmentMaker._attach_metronome_marks(4):baca.SegmentMaker._style_phantom_measures(1):PHANTOM
                        \once \override Score.BarLine.transparent = ##t                              %! baca.SegmentMaker._style_phantom_measures(3):PHANTOM
                        \once \override Score.SpanBar.transparent = ##t                              %! baca.SegmentMaker._style_phantom_measures(3):PHANTOM
            <BLANKLINE>
                    }                                                                                %! abjad.ScoreTemplate._make_global_context()
            <BLANKLINE>
                >>                                                                                   %! abjad.ScoreTemplate._make_global_context()
            <BLANKLINE>
                \context MusicContext = "Music_Context"                                              %! baca.SingleStaffScoreTemplate.__call__()
                <<                                                                                   %! baca.SingleStaffScoreTemplate.__call__()
            <BLANKLINE>
                    \context Staff = "Music_Staff"                                                   %! baca.SingleStaffScoreTemplate.__call__()
                    {                                                                                %! baca.SingleStaffScoreTemplate.__call__()
            <BLANKLINE>
                        \context Voice = "Music_Voice"                                               %! baca.SingleStaffScoreTemplate.__call__()
                        {                                                                            %! baca.SingleStaffScoreTemplate.__call__()
            <BLANKLINE>
                            % [Music_Voice measure 1]                                                %! baca.SegmentMaker._comment_measure_numbers()
                        %@% \baca-not-yet-pitched-coloring                                           %! baca.SegmentMaker._color_not_yet_pitched():NOT_YET_PITCHED_COLORING
                            b'4.                                                                     %! baca.make_notes()
            <BLANKLINE>
                            % [Music_Voice measure 2]                                                %! baca.SegmentMaker._comment_measure_numbers()
                        %@% \baca-not-yet-pitched-coloring                                           %! baca.SegmentMaker._color_not_yet_pitched():NOT_YET_PITCHED_COLORING
                            b'4.                                                                     %! baca.make_notes()
            <BLANKLINE>
                            <<                                                                       %! baca.SegmentMaker._make_multimeasure_rest_container(7):PHANTOM
            <BLANKLINE>
                                \context Voice = "Music_Voice"                                       %! baca.SegmentMaker._make_multimeasure_rest_container(4):PHANTOM
                                {                                                                    %! baca.SegmentMaker._make_multimeasure_rest_container(4):PHANTOM
            <BLANKLINE>
                                    % [Music_Voice measure 3]                                        %! baca.SegmentMaker._comment_measure_numbers():baca.SegmentMaker._style_phantom_measures(5):PHANTOM
                                    \abjad-invisible-music-coloring                                  %! baca.SegmentMaker._make_multimeasure_rest_container(2):PHANTOM:NOTE:INVISIBLE_MUSIC_COLORING:baca.SegmentMaker._style_phantom_measures(5)
                                %@% \abjad-invisible-music                                           %! baca.SegmentMaker._make_multimeasure_rest_container(3):PHANTOM:NOTE:INVISIBLE_MUSIC_COMMAND:baca.SegmentMaker._style_phantom_measures(5)
                                %@% \baca-not-yet-pitched-coloring                                   %! baca.SegmentMaker._color_not_yet_pitched():NOT_YET_PITCHED_COLORING:HIDDEN:NOTE:baca.SegmentMaker._style_phantom_measures(5):PHANTOM
                                    b'1 * 1/4                                                        %! baca.SegmentMaker._make_multimeasure_rest_container(1):PHANTOM:HIDDEN:NOTE
                                %@% ^ \baca-duration-multiplier-markup #"1" #"4"                     %! baca.SegmentMaker._label_duration_multipliers():DURATION_MULTIPLIER:HIDDEN:NOTE:PHANTOM:baca.SegmentMaker._style_phantom_measures(5)
            <BLANKLINE>
                                }                                                                    %! baca.SegmentMaker._make_multimeasure_rest_container(4):PHANTOM
            <BLANKLINE>
                                \context Voice = "Rest_Voice"                                        %! baca.SegmentMaker._make_multimeasure_rest_container(6):PHANTOM
                                {                                                                    %! baca.SegmentMaker._make_multimeasure_rest_container(6):PHANTOM
            <BLANKLINE>
                                    % [Rest_Voice measure 3]                                         %! baca.SegmentMaker._comment_measure_numbers():baca.SegmentMaker._style_phantom_measures(5):PHANTOM
                                    \once \override Score.TimeSignature.X-extent = ##f               %! baca.SegmentMaker._style_phantom_measures(6):PHANTOM
                                    \once \override MultiMeasureRest.transparent = ##t               %! baca.SegmentMaker._style_phantom_measures(7):PHANTOM
                                    \stopStaff                                                       %! baca.SegmentMaker._style_phantom_measures(8):PHANTOM
                                    \once \override Staff.StaffSymbol.transparent = ##t              %! baca.SegmentMaker._style_phantom_measures(8):PHANTOM
                                    \startStaff                                                      %! baca.SegmentMaker._style_phantom_measures(8):PHANTOM
                                    R1 * 1/4                                                         %! baca.SegmentMaker._make_multimeasure_rest_container(5):PHANTOM:REST_VOICE:MULTIMEASURE_REST
                                %@% ^ \baca-duration-multiplier-markup #"1" #"4"                     %! baca.SegmentMaker._label_duration_multipliers():DURATION_MULTIPLIER:MULTIMEASURE_REST:PHANTOM:REST_VOICE:baca.SegmentMaker._style_phantom_measures(5)
            <BLANKLINE>
                                }                                                                    %! baca.SegmentMaker._make_multimeasure_rest_container(6):PHANTOM
            <BLANKLINE>
                            >>                                                                       %! baca.SegmentMaker._make_multimeasure_rest_container(7):PHANTOM
            <BLANKLINE>
                        }                                                                            %! baca.SingleStaffScoreTemplate.__call__()
            <BLANKLINE>
                    }                                                                                %! baca.SingleStaffScoreTemplate.__call__()
            <BLANKLINE>
                >>                                                                                   %! baca.SingleStaffScoreTemplate.__call__()
            <BLANKLINE>
            >>                                                                                       %! baca.SingleStaffScoreTemplate.__call__()
            
    ..  container:: example

        Redundant tempo trends color pink:

        >>> maker = baca.SegmentMaker(
        ...     breaks=breaks,
        ...     deactivate=[abjad.tags.NOT_YET_PITCHED_COLORING],
        ...     metronome_marks=metronome_marks,
        ...     score_template=baca.SingleStaffScoreTemplate(),
        ...     spacing=baca.minimum_duration((1, 24)),
        ...     time_signatures=[(3, 8), (3, 8), (3, 8)],
        ...     )
        >>> maker(
        ...     'Global_Skips',
        ...     baca.metronome_mark(baca.Accelerando()),
        ...     baca.metronome_mark(
        ...         baca.Accelerando(),
        ...         selector=baca.leaf(1),
        ...         ),
        ...     )
        >>> maker(
        ...     'Music_Voice',
        ...     baca.make_notes(),
        ...     )

        >>> lilypond_file = maker.run(environment='docs')
        >>> block = abjad.Block(name='layout')
        >>> block.indent = 0
        >>> lilypond_file.items.insert(0, block)
        >>> abjad.show(lilypond_file, strict=89) # doctest: +SKIP

        ..  docs::

            >>> abjad.f(lilypond_file[abjad.Score], strict=89)
            <BLANKLINE>
            \context Score = "Score"                                                                 %! baca.SingleStaffScoreTemplate.__call__()
            <<                                                                                       %! baca.SingleStaffScoreTemplate.__call__()
            <BLANKLINE>
                \context GlobalContext = "Global_Context"                                            %! abjad.ScoreTemplate._make_global_context()
                <<                                                                                   %! abjad.ScoreTemplate._make_global_context()
            <BLANKLINE>
                    \context GlobalSkips = "Global_Skips"                                            %! abjad.ScoreTemplate._make_global_context()
                    {                                                                                %! abjad.ScoreTemplate._make_global_context()
            <BLANKLINE>
                        % [Global_Skips measure 1]                                                   %! baca.SegmentMaker._comment_measure_numbers()
                        \baca-new-spacing-section #1 #24                                             %! SPACING_COMMAND:baca.HorizontalSpacingSpecifier.__call__(1)
                        \autoPageBreaksOff                                                           %! BREAK:baca.BreakMeasureMap.__call__(1)
                        \noBreak                                                                     %! BREAK:baca.BreakMeasureMap.__call__(2)
                        \baca-lbsd #4 #'(8)                                                          %! BREAK:baca.IndicatorCommand._call()
                        \time 3/8                                                                    %! baca.SegmentMaker._make_global_skips(2):baca.SegmentMaker._set_status_tag():EXPLICIT_TIME_SIGNATURE
                        \baca-time-signature-color #'blue                                            %! baca.SegmentMaker._attach_color_literal(2):EXPLICIT_TIME_SIGNATURE_COLOR
                        \pageBreak                                                                   %! BREAK:baca.IndicatorCommand._call()
                        s1 * 3/8                                                                     %! baca.SegmentMaker._make_global_skips(1)
                    %@% - \abjad-dashed-line-with-arrow                                              %! baca.SegmentMaker._set_status_tag():EXPLICIT_METRONOME_MARK:baca.SegmentMaker._attach_metronome_marks(2)
                    %@% - \tweak bound-details.left.text \markup {                                   %! baca.SegmentMaker._set_status_tag():EXPLICIT_METRONOME_MARK:baca.SegmentMaker._attach_metronome_marks(2)
                    %@%     \concat                                                                  %! baca.SegmentMaker._set_status_tag():EXPLICIT_METRONOME_MARK:baca.SegmentMaker._attach_metronome_marks(2)
                    %@%         {                                                                    %! baca.SegmentMaker._set_status_tag():EXPLICIT_METRONOME_MARK:baca.SegmentMaker._attach_metronome_marks(2)
                    %@%             \large                                                           %! baca.SegmentMaker._set_status_tag():EXPLICIT_METRONOME_MARK:baca.SegmentMaker._attach_metronome_marks(2)
                    %@%                 \upright                                                     %! baca.SegmentMaker._set_status_tag():EXPLICIT_METRONOME_MARK:baca.SegmentMaker._attach_metronome_marks(2)
                    %@%                     accel.                                                   %! baca.SegmentMaker._set_status_tag():EXPLICIT_METRONOME_MARK:baca.SegmentMaker._attach_metronome_marks(2)
                    %@%             \hspace                                                          %! baca.SegmentMaker._set_status_tag():EXPLICIT_METRONOME_MARK:baca.SegmentMaker._attach_metronome_marks(2)
                    %@%                 #0.5                                                         %! baca.SegmentMaker._set_status_tag():EXPLICIT_METRONOME_MARK:baca.SegmentMaker._attach_metronome_marks(2)
                    %@%         }                                                                    %! baca.SegmentMaker._set_status_tag():EXPLICIT_METRONOME_MARK:baca.SegmentMaker._attach_metronome_marks(2)
                    %@%     }                                                                        %! baca.SegmentMaker._set_status_tag():EXPLICIT_METRONOME_MARK:baca.SegmentMaker._attach_metronome_marks(2)
                    %@% \bacaStartTextSpanMM                                                         %! baca.SegmentMaker._set_status_tag():EXPLICIT_METRONOME_MARK:baca.SegmentMaker._attach_metronome_marks(2)
                        - \abjad-dashed-line-with-arrow                                              %! EXPLICIT_METRONOME_MARK_WITH_COLOR:baca.SegmentMaker._attach_metronome_marks(3)
                        - \tweak bound-details.left.text \markup {                                   %! EXPLICIT_METRONOME_MARK_WITH_COLOR:baca.SegmentMaker._attach_metronome_marks(3)
                            \concat                                                                  %! EXPLICIT_METRONOME_MARK_WITH_COLOR:baca.SegmentMaker._attach_metronome_marks(3)
                                {                                                                    %! EXPLICIT_METRONOME_MARK_WITH_COLOR:baca.SegmentMaker._attach_metronome_marks(3)
                                    \with-color                                                      %! EXPLICIT_METRONOME_MARK_WITH_COLOR:baca.SegmentMaker._attach_metronome_marks(3)
                                        #(x11-color 'blue)                                           %! EXPLICIT_METRONOME_MARK_WITH_COLOR:baca.SegmentMaker._attach_metronome_marks(3)
                                        \large                                                       %! EXPLICIT_METRONOME_MARK_WITH_COLOR:baca.SegmentMaker._attach_metronome_marks(3)
                                            \upright                                                 %! EXPLICIT_METRONOME_MARK_WITH_COLOR:baca.SegmentMaker._attach_metronome_marks(3)
                                                accel.                                               %! EXPLICIT_METRONOME_MARK_WITH_COLOR:baca.SegmentMaker._attach_metronome_marks(3)
                                    \hspace                                                          %! EXPLICIT_METRONOME_MARK_WITH_COLOR:baca.SegmentMaker._attach_metronome_marks(3)
                                        #0.5                                                         %! EXPLICIT_METRONOME_MARK_WITH_COLOR:baca.SegmentMaker._attach_metronome_marks(3)
                                }                                                                    %! EXPLICIT_METRONOME_MARK_WITH_COLOR:baca.SegmentMaker._attach_metronome_marks(3)
                            }                                                                        %! EXPLICIT_METRONOME_MARK_WITH_COLOR:baca.SegmentMaker._attach_metronome_marks(3)
                        \bacaStartTextSpanMM                                                         %! EXPLICIT_METRONOME_MARK_WITH_COLOR:baca.SegmentMaker._attach_metronome_marks(3)
            <BLANKLINE>
                        % [Global_Skips measure 2]                                                   %! baca.SegmentMaker._comment_measure_numbers()
                        \baca-new-spacing-section #1 #24                                             %! SPACING_COMMAND:baca.HorizontalSpacingSpecifier.__call__(1)
                        \noBreak                                                                     %! BREAK:baca.BreakMeasureMap.__call__(2)
                        s1 * 3/8                                                                     %! baca.SegmentMaker._make_global_skips(1)
                        \bacaStopTextSpanMM                                                          %! baca.SegmentMaker._attach_metronome_marks(1)
                    %@% - \abjad-dashed-line-with-arrow                                              %! baca.SegmentMaker._set_status_tag():REDUNDANT_METRONOME_MARK:baca.SegmentMaker._attach_metronome_marks(2)
                    %@% - \tweak bound-details.left.text \markup {                                   %! baca.SegmentMaker._set_status_tag():REDUNDANT_METRONOME_MARK:baca.SegmentMaker._attach_metronome_marks(2)
                    %@%     \concat                                                                  %! baca.SegmentMaker._set_status_tag():REDUNDANT_METRONOME_MARK:baca.SegmentMaker._attach_metronome_marks(2)
                    %@%         {                                                                    %! baca.SegmentMaker._set_status_tag():REDUNDANT_METRONOME_MARK:baca.SegmentMaker._attach_metronome_marks(2)
                    %@%             \large                                                           %! baca.SegmentMaker._set_status_tag():REDUNDANT_METRONOME_MARK:baca.SegmentMaker._attach_metronome_marks(2)
                    %@%                 \upright                                                     %! baca.SegmentMaker._set_status_tag():REDUNDANT_METRONOME_MARK:baca.SegmentMaker._attach_metronome_marks(2)
                    %@%                     accel.                                                   %! baca.SegmentMaker._set_status_tag():REDUNDANT_METRONOME_MARK:baca.SegmentMaker._attach_metronome_marks(2)
                    %@%             \hspace                                                          %! baca.SegmentMaker._set_status_tag():REDUNDANT_METRONOME_MARK:baca.SegmentMaker._attach_metronome_marks(2)
                    %@%                 #0.5                                                         %! baca.SegmentMaker._set_status_tag():REDUNDANT_METRONOME_MARK:baca.SegmentMaker._attach_metronome_marks(2)
                    %@%         }                                                                    %! baca.SegmentMaker._set_status_tag():REDUNDANT_METRONOME_MARK:baca.SegmentMaker._attach_metronome_marks(2)
                    %@%     }                                                                        %! baca.SegmentMaker._set_status_tag():REDUNDANT_METRONOME_MARK:baca.SegmentMaker._attach_metronome_marks(2)
                    %@% \bacaStartTextSpanMM                                                         %! baca.SegmentMaker._set_status_tag():REDUNDANT_METRONOME_MARK:baca.SegmentMaker._attach_metronome_marks(2)
                        - \abjad-dashed-line-with-arrow                                              %! REDUNDANT_METRONOME_MARK_WITH_COLOR:baca.SegmentMaker._attach_metronome_marks(3)
                        - \tweak bound-details.left.text \markup {                                   %! REDUNDANT_METRONOME_MARK_WITH_COLOR:baca.SegmentMaker._attach_metronome_marks(3)
                            \concat                                                                  %! REDUNDANT_METRONOME_MARK_WITH_COLOR:baca.SegmentMaker._attach_metronome_marks(3)
                                {                                                                    %! REDUNDANT_METRONOME_MARK_WITH_COLOR:baca.SegmentMaker._attach_metronome_marks(3)
                                    \with-color                                                      %! REDUNDANT_METRONOME_MARK_WITH_COLOR:baca.SegmentMaker._attach_metronome_marks(3)
                                        #(x11-color 'DeepPink1)                                      %! REDUNDANT_METRONOME_MARK_WITH_COLOR:baca.SegmentMaker._attach_metronome_marks(3)
                                        \large                                                       %! REDUNDANT_METRONOME_MARK_WITH_COLOR:baca.SegmentMaker._attach_metronome_marks(3)
                                            \upright                                                 %! REDUNDANT_METRONOME_MARK_WITH_COLOR:baca.SegmentMaker._attach_metronome_marks(3)
                                                accel.                                               %! REDUNDANT_METRONOME_MARK_WITH_COLOR:baca.SegmentMaker._attach_metronome_marks(3)
                                    \hspace                                                          %! REDUNDANT_METRONOME_MARK_WITH_COLOR:baca.SegmentMaker._attach_metronome_marks(3)
                                        #0.5                                                         %! REDUNDANT_METRONOME_MARK_WITH_COLOR:baca.SegmentMaker._attach_metronome_marks(3)
                                }                                                                    %! REDUNDANT_METRONOME_MARK_WITH_COLOR:baca.SegmentMaker._attach_metronome_marks(3)
                            }                                                                        %! REDUNDANT_METRONOME_MARK_WITH_COLOR:baca.SegmentMaker._attach_metronome_marks(3)
                        \bacaStartTextSpanMM                                                         %! REDUNDANT_METRONOME_MARK_WITH_COLOR:baca.SegmentMaker._attach_metronome_marks(3)
            <BLANKLINE>
                        % [Global_Skips measure 3]                                                   %! baca.SegmentMaker._comment_measure_numbers()
                        \baca-new-spacing-section #1 #24                                             %! SPACING_COMMAND:baca.HorizontalSpacingSpecifier.__call__(1)
                        \noBreak                                                                     %! BREAK:baca.BreakMeasureMap.__call__(2)
                        s1 * 3/8                                                                     %! baca.SegmentMaker._make_global_skips(1)
            <BLANKLINE>
                        % [Global_Skips measure 4]                                                   %! baca.SegmentMaker._comment_measure_numbers():baca.SegmentMaker._style_phantom_measures(1):PHANTOM
                        \baca-new-spacing-section #1 #4                                              %! SPACING_COMMAND:baca.HorizontalSpacingSpecifier.__call__(1):baca.SegmentMaker._style_phantom_measures(1):PHANTOM
                        \noBreak                                                                     %! BREAK:baca.BreakMeasureMap.__call__(2):baca.SegmentMaker._style_phantom_measures(1):PHANTOM
                        \time 1/4                                                                    %! baca.SegmentMaker._make_global_skips(3):PHANTOM:baca.SegmentMaker._set_status_tag():EXPLICIT_TIME_SIGNATURE:baca.SegmentMaker._style_phantom_measures(1)
                        \baca-time-signature-transparent                                             %! baca.SegmentMaker._style_phantom_measures(2):PHANTOM
                        s1 * 1/4                                                                     %! baca.SegmentMaker._make_global_skips(3):PHANTOM
                        \bacaStopTextSpanMM                                                          %! EOS_STOP_MM_SPANNER:baca.SegmentMaker._attach_metronome_marks(4):baca.SegmentMaker._style_phantom_measures(1):PHANTOM
                        \once \override Score.BarLine.transparent = ##t                              %! baca.SegmentMaker._style_phantom_measures(3):PHANTOM
                        \once \override Score.SpanBar.transparent = ##t                              %! baca.SegmentMaker._style_phantom_measures(3):PHANTOM
            <BLANKLINE>
                    }                                                                                %! abjad.ScoreTemplate._make_global_context()
            <BLANKLINE>
                >>                                                                                   %! abjad.ScoreTemplate._make_global_context()
            <BLANKLINE>
                \context MusicContext = "Music_Context"                                              %! baca.SingleStaffScoreTemplate.__call__()
                <<                                                                                   %! baca.SingleStaffScoreTemplate.__call__()
            <BLANKLINE>
                    \context Staff = "Music_Staff"                                                   %! baca.SingleStaffScoreTemplate.__call__()
                    {                                                                                %! baca.SingleStaffScoreTemplate.__call__()
            <BLANKLINE>
                        \context Voice = "Music_Voice"                                               %! baca.SingleStaffScoreTemplate.__call__()
                        {                                                                            %! baca.SingleStaffScoreTemplate.__call__()
            <BLANKLINE>
                            % [Music_Voice measure 1]                                                %! baca.SegmentMaker._comment_measure_numbers()
                        %@% \baca-not-yet-pitched-coloring                                           %! baca.SegmentMaker._color_not_yet_pitched():NOT_YET_PITCHED_COLORING
                            b'4.                                                                     %! baca.make_notes()
            <BLANKLINE>
                            % [Music_Voice measure 2]                                                %! baca.SegmentMaker._comment_measure_numbers()
                        %@% \baca-not-yet-pitched-coloring                                           %! baca.SegmentMaker._color_not_yet_pitched():NOT_YET_PITCHED_COLORING
                            b'4.                                                                     %! baca.make_notes()
            <BLANKLINE>
                            % [Music_Voice measure 3]                                                %! baca.SegmentMaker._comment_measure_numbers()
                        %@% \baca-not-yet-pitched-coloring                                           %! baca.SegmentMaker._color_not_yet_pitched():NOT_YET_PITCHED_COLORING
                            b'4.                                                                     %! baca.make_notes()
            <BLANKLINE>
                            <<                                                                       %! baca.SegmentMaker._make_multimeasure_rest_container(7):PHANTOM
            <BLANKLINE>
                                \context Voice = "Music_Voice"                                       %! baca.SegmentMaker._make_multimeasure_rest_container(4):PHANTOM
                                {                                                                    %! baca.SegmentMaker._make_multimeasure_rest_container(4):PHANTOM
            <BLANKLINE>
                                    % [Music_Voice measure 4]                                        %! baca.SegmentMaker._comment_measure_numbers():baca.SegmentMaker._style_phantom_measures(5):PHANTOM
                                    \abjad-invisible-music-coloring                                  %! baca.SegmentMaker._make_multimeasure_rest_container(2):PHANTOM:NOTE:INVISIBLE_MUSIC_COLORING:baca.SegmentMaker._style_phantom_measures(5)
                                %@% \abjad-invisible-music                                           %! baca.SegmentMaker._make_multimeasure_rest_container(3):PHANTOM:NOTE:INVISIBLE_MUSIC_COMMAND:baca.SegmentMaker._style_phantom_measures(5)
                                %@% \baca-not-yet-pitched-coloring                                   %! baca.SegmentMaker._color_not_yet_pitched():NOT_YET_PITCHED_COLORING:HIDDEN:NOTE:baca.SegmentMaker._style_phantom_measures(5):PHANTOM
                                    b'1 * 1/4                                                        %! baca.SegmentMaker._make_multimeasure_rest_container(1):PHANTOM:HIDDEN:NOTE
                                %@% ^ \baca-duration-multiplier-markup #"1" #"4"                     %! baca.SegmentMaker._label_duration_multipliers():DURATION_MULTIPLIER:HIDDEN:NOTE:PHANTOM:baca.SegmentMaker._style_phantom_measures(5)
            <BLANKLINE>
                                }                                                                    %! baca.SegmentMaker._make_multimeasure_rest_container(4):PHANTOM
            <BLANKLINE>
                                \context Voice = "Rest_Voice"                                        %! baca.SegmentMaker._make_multimeasure_rest_container(6):PHANTOM
                                {                                                                    %! baca.SegmentMaker._make_multimeasure_rest_container(6):PHANTOM
            <BLANKLINE>
                                    % [Rest_Voice measure 4]                                         %! baca.SegmentMaker._comment_measure_numbers():baca.SegmentMaker._style_phantom_measures(5):PHANTOM
                                    \once \override Score.TimeSignature.X-extent = ##f               %! baca.SegmentMaker._style_phantom_measures(6):PHANTOM
                                    \once \override MultiMeasureRest.transparent = ##t               %! baca.SegmentMaker._style_phantom_measures(7):PHANTOM
                                    \stopStaff                                                       %! baca.SegmentMaker._style_phantom_measures(8):PHANTOM
                                    \once \override Staff.StaffSymbol.transparent = ##t              %! baca.SegmentMaker._style_phantom_measures(8):PHANTOM
                                    \startStaff                                                      %! baca.SegmentMaker._style_phantom_measures(8):PHANTOM
                                    R1 * 1/4                                                         %! baca.SegmentMaker._make_multimeasure_rest_container(5):PHANTOM:REST_VOICE:MULTIMEASURE_REST
                                %@% ^ \baca-duration-multiplier-markup #"1" #"4"                     %! baca.SegmentMaker._label_duration_multipliers():DURATION_MULTIPLIER:MULTIMEASURE_REST:PHANTOM:REST_VOICE:baca.SegmentMaker._style_phantom_measures(5)
            <BLANKLINE>
                                }                                                                    %! baca.SegmentMaker._make_multimeasure_rest_container(6):PHANTOM
            <BLANKLINE>
                            >>                                                                       %! baca.SegmentMaker._make_multimeasure_rest_container(7):PHANTOM
            <BLANKLINE>
                        }                                                                            %! baca.SingleStaffScoreTemplate.__call__()
            <BLANKLINE>
                    }                                                                                %! baca.SingleStaffScoreTemplate.__call__()
            <BLANKLINE>
                >>                                                                                   %! baca.SingleStaffScoreTemplate.__call__()
            <BLANKLINE>
            >>                                                                                       %! baca.SingleStaffScoreTemplate.__call__()

        Even at the beginning of a segment:

        >>> maker = baca.SegmentMaker(
        ...     breaks=breaks,
        ...     deactivate=[abjad.tags.NOT_YET_PITCHED_COLORING],
        ...     metronome_marks=metronome_marks,
        ...     score_template=baca.SingleStaffScoreTemplate(),
        ...     spacing=baca.minimum_duration((1, 24)),
        ...     time_signatures=[(3, 8), (3, 8)],
        ...     )
        >>> maker(
        ...     'Global_Skips',
        ...     baca.metronome_mark(baca.Accelerando()),
        ...     baca.text_spanner_staff_padding(4),
        ...     )
        >>> maker(
        ...     'Music_Voice',
        ...     baca.make_notes(),
        ...     )

        >>> metadata, persist = {}, {}
        >>> persist['persistent_indicators'] = {}
        >>> persist['persistent_indicators']['Score'] = [
        ...     abjad.Momento(
        ...         context='Global_Skips',
        ...         prototype='baca.Accelerando',
        ...         )
        ...     ]
        >>> metadata['segment_number'] = 1
        >>> lilypond_file = maker.run(
        ...     environment='docs',
        ...     previous_metadata=metadata,
        ...     previous_persist=persist,
        ...     )
        >>> block = abjad.Block(name='layout')
        >>> block.indent = 0
        >>> lilypond_file.items.insert(0, block)
        >>> abjad.show(lilypond_file, strict=89) # doctest: +SKIP

        ..  docs::

            >>> abjad.f(lilypond_file[abjad.Score], strict=89)
            <BLANKLINE>
            \context Score = "Score"                                                                 %! baca.SingleStaffScoreTemplate.__call__()
            <<                                                                                       %! baca.SingleStaffScoreTemplate.__call__()
            <BLANKLINE>
                \context GlobalContext = "Global_Context"                                            %! abjad.ScoreTemplate._make_global_context()
                <<                                                                                   %! abjad.ScoreTemplate._make_global_context()
            <BLANKLINE>
                    \context GlobalSkips = "Global_Skips"                                            %! abjad.ScoreTemplate._make_global_context()
                    {                                                                                %! abjad.ScoreTemplate._make_global_context()
            <BLANKLINE>
                        % [Global_Skips measure 1]                                                   %! baca.SegmentMaker._comment_measure_numbers()
                        \baca-new-spacing-section #1 #24                                             %! SPACING_COMMAND:baca.HorizontalSpacingSpecifier.__call__(1)
                        \override TextSpanner.staff-padding = #4                                     %! baca.text_spanner_staff_padding():baca.OverrideCommand._call(1)
                        \autoPageBreaksOff                                                           %! BREAK:baca.BreakMeasureMap.__call__(1)
                        \noBreak                                                                     %! BREAK:baca.BreakMeasureMap.__call__(2)
                        \baca-lbsd #4 #'(8)                                                          %! BREAK:baca.IndicatorCommand._call()
                        \time 3/8                                                                    %! baca.SegmentMaker._make_global_skips(2):baca.SegmentMaker._set_status_tag():EXPLICIT_TIME_SIGNATURE
                        \bar ""                                                                      %! EMPTY_START_BAR:+SEGMENT:baca.SegmentMaker._make_global_skips(4)
                        \baca-time-signature-color #'blue                                            %! baca.SegmentMaker._attach_color_literal(2):EXPLICIT_TIME_SIGNATURE_COLOR
                        \pageBreak                                                                   %! BREAK:baca.IndicatorCommand._call()
                        s1 * 3/8                                                                     %! baca.SegmentMaker._make_global_skips(1)
                    %@% - \abjad-dashed-line-with-arrow                                              %! baca.SegmentMaker._set_status_tag():REDUNDANT_METRONOME_MARK:baca.SegmentMaker._attach_metronome_marks(2)
                    %@% - \tweak bound-details.left.text \markup {                                   %! baca.SegmentMaker._set_status_tag():REDUNDANT_METRONOME_MARK:baca.SegmentMaker._attach_metronome_marks(2)
                    %@%     \concat                                                                  %! baca.SegmentMaker._set_status_tag():REDUNDANT_METRONOME_MARK:baca.SegmentMaker._attach_metronome_marks(2)
                    %@%         {                                                                    %! baca.SegmentMaker._set_status_tag():REDUNDANT_METRONOME_MARK:baca.SegmentMaker._attach_metronome_marks(2)
                    %@%             \large                                                           %! baca.SegmentMaker._set_status_tag():REDUNDANT_METRONOME_MARK:baca.SegmentMaker._attach_metronome_marks(2)
                    %@%                 \upright                                                     %! baca.SegmentMaker._set_status_tag():REDUNDANT_METRONOME_MARK:baca.SegmentMaker._attach_metronome_marks(2)
                    %@%                     accel.                                                   %! baca.SegmentMaker._set_status_tag():REDUNDANT_METRONOME_MARK:baca.SegmentMaker._attach_metronome_marks(2)
                    %@%             \hspace                                                          %! baca.SegmentMaker._set_status_tag():REDUNDANT_METRONOME_MARK:baca.SegmentMaker._attach_metronome_marks(2)
                    %@%                 #0.5                                                         %! baca.SegmentMaker._set_status_tag():REDUNDANT_METRONOME_MARK:baca.SegmentMaker._attach_metronome_marks(2)
                    %@%         }                                                                    %! baca.SegmentMaker._set_status_tag():REDUNDANT_METRONOME_MARK:baca.SegmentMaker._attach_metronome_marks(2)
                    %@%     }                                                                        %! baca.SegmentMaker._set_status_tag():REDUNDANT_METRONOME_MARK:baca.SegmentMaker._attach_metronome_marks(2)
                    %@% \bacaStartTextSpanMM                                                         %! baca.SegmentMaker._set_status_tag():REDUNDANT_METRONOME_MARK:baca.SegmentMaker._attach_metronome_marks(2)
                        - \abjad-dashed-line-with-arrow                                              %! REDUNDANT_METRONOME_MARK_WITH_COLOR:baca.SegmentMaker._attach_metronome_marks(3)
                        - \tweak bound-details.left.text \markup {                                   %! REDUNDANT_METRONOME_MARK_WITH_COLOR:baca.SegmentMaker._attach_metronome_marks(3)
                            \concat                                                                  %! REDUNDANT_METRONOME_MARK_WITH_COLOR:baca.SegmentMaker._attach_metronome_marks(3)
                                {                                                                    %! REDUNDANT_METRONOME_MARK_WITH_COLOR:baca.SegmentMaker._attach_metronome_marks(3)
                                    \with-color                                                      %! REDUNDANT_METRONOME_MARK_WITH_COLOR:baca.SegmentMaker._attach_metronome_marks(3)
                                        #(x11-color 'DeepPink1)                                      %! REDUNDANT_METRONOME_MARK_WITH_COLOR:baca.SegmentMaker._attach_metronome_marks(3)
                                        \large                                                       %! REDUNDANT_METRONOME_MARK_WITH_COLOR:baca.SegmentMaker._attach_metronome_marks(3)
                                            \upright                                                 %! REDUNDANT_METRONOME_MARK_WITH_COLOR:baca.SegmentMaker._attach_metronome_marks(3)
                                                accel.                                               %! REDUNDANT_METRONOME_MARK_WITH_COLOR:baca.SegmentMaker._attach_metronome_marks(3)
                                    \hspace                                                          %! REDUNDANT_METRONOME_MARK_WITH_COLOR:baca.SegmentMaker._attach_metronome_marks(3)
                                        #0.5                                                         %! REDUNDANT_METRONOME_MARK_WITH_COLOR:baca.SegmentMaker._attach_metronome_marks(3)
                                }                                                                    %! REDUNDANT_METRONOME_MARK_WITH_COLOR:baca.SegmentMaker._attach_metronome_marks(3)
                            }                                                                        %! REDUNDANT_METRONOME_MARK_WITH_COLOR:baca.SegmentMaker._attach_metronome_marks(3)
                        \bacaStartTextSpanMM                                                         %! REDUNDANT_METRONOME_MARK_WITH_COLOR:baca.SegmentMaker._attach_metronome_marks(3)
            <BLANKLINE>
                        % [Global_Skips measure 2]                                                   %! baca.SegmentMaker._comment_measure_numbers()
                        \baca-new-spacing-section #1 #24                                             %! SPACING_COMMAND:baca.HorizontalSpacingSpecifier.__call__(1)
                        \noBreak                                                                     %! BREAK:baca.BreakMeasureMap.__call__(2)
                        s1 * 3/8                                                                     %! baca.SegmentMaker._make_global_skips(1)
                        \revert TextSpanner.staff-padding                                            %! baca.text_spanner_staff_padding():baca.OverrideCommand._call(2)
            <BLANKLINE>
                        % [Global_Skips measure 3]                                                   %! baca.SegmentMaker._comment_measure_numbers():baca.SegmentMaker._style_phantom_measures(1):PHANTOM
                        \baca-new-spacing-section #1 #4                                              %! SPACING_COMMAND:baca.HorizontalSpacingSpecifier.__call__(1):baca.SegmentMaker._style_phantom_measures(1):PHANTOM
                        \noBreak                                                                     %! BREAK:baca.BreakMeasureMap.__call__(2):baca.SegmentMaker._style_phantom_measures(1):PHANTOM
                        \time 1/4                                                                    %! baca.SegmentMaker._make_global_skips(3):PHANTOM:baca.SegmentMaker._set_status_tag():EXPLICIT_TIME_SIGNATURE:baca.SegmentMaker._style_phantom_measures(1)
                        \baca-time-signature-transparent                                             %! baca.SegmentMaker._style_phantom_measures(2):PHANTOM
                        s1 * 1/4                                                                     %! baca.SegmentMaker._make_global_skips(3):PHANTOM
                        \bacaStopTextSpanMM                                                          %! EOS_STOP_MM_SPANNER:baca.SegmentMaker._attach_metronome_marks(4):baca.SegmentMaker._style_phantom_measures(1):PHANTOM
                        \once \override Score.BarLine.transparent = ##t                              %! baca.SegmentMaker._style_phantom_measures(3):PHANTOM
                        \once \override Score.SpanBar.transparent = ##t                              %! baca.SegmentMaker._style_phantom_measures(3):PHANTOM
            <BLANKLINE>
                    }                                                                                %! abjad.ScoreTemplate._make_global_context()
            <BLANKLINE>
                >>                                                                                   %! abjad.ScoreTemplate._make_global_context()
            <BLANKLINE>
                \context MusicContext = "Music_Context"                                              %! baca.SingleStaffScoreTemplate.__call__()
                <<                                                                                   %! baca.SingleStaffScoreTemplate.__call__()
            <BLANKLINE>
                    \context Staff = "Music_Staff"                                                   %! baca.SingleStaffScoreTemplate.__call__()
                    {                                                                                %! baca.SingleStaffScoreTemplate.__call__()
            <BLANKLINE>
                        \context Voice = "Music_Voice"                                               %! baca.SingleStaffScoreTemplate.__call__()
                        {                                                                            %! baca.SingleStaffScoreTemplate.__call__()
            <BLANKLINE>
                            % [Music_Voice measure 1]                                                %! baca.SegmentMaker._comment_measure_numbers()
                        %@% \baca-not-yet-pitched-coloring                                           %! baca.SegmentMaker._color_not_yet_pitched():NOT_YET_PITCHED_COLORING
                            b'4.                                                                     %! baca.make_notes()
            <BLANKLINE>
                            % [Music_Voice measure 2]                                                %! baca.SegmentMaker._comment_measure_numbers()
                        %@% \baca-not-yet-pitched-coloring                                           %! baca.SegmentMaker._color_not_yet_pitched():NOT_YET_PITCHED_COLORING
                            b'4.                                                                     %! baca.make_notes()
            <BLANKLINE>
                            <<                                                                       %! baca.SegmentMaker._make_multimeasure_rest_container(7):PHANTOM
            <BLANKLINE>
                                \context Voice = "Music_Voice"                                       %! baca.SegmentMaker._make_multimeasure_rest_container(4):PHANTOM
                                {                                                                    %! baca.SegmentMaker._make_multimeasure_rest_container(4):PHANTOM
            <BLANKLINE>
                                    % [Music_Voice measure 3]                                        %! baca.SegmentMaker._comment_measure_numbers():baca.SegmentMaker._style_phantom_measures(5):PHANTOM
                                    \abjad-invisible-music-coloring                                  %! baca.SegmentMaker._make_multimeasure_rest_container(2):PHANTOM:NOTE:INVISIBLE_MUSIC_COLORING:baca.SegmentMaker._style_phantom_measures(5)
                                %@% \abjad-invisible-music                                           %! baca.SegmentMaker._make_multimeasure_rest_container(3):PHANTOM:NOTE:INVISIBLE_MUSIC_COMMAND:baca.SegmentMaker._style_phantom_measures(5)
                                %@% \baca-not-yet-pitched-coloring                                   %! baca.SegmentMaker._color_not_yet_pitched():NOT_YET_PITCHED_COLORING:HIDDEN:NOTE:baca.SegmentMaker._style_phantom_measures(5):PHANTOM
                                    b'1 * 1/4                                                        %! baca.SegmentMaker._make_multimeasure_rest_container(1):PHANTOM:HIDDEN:NOTE
                                %@% ^ \baca-duration-multiplier-markup #"1" #"4"                     %! baca.SegmentMaker._label_duration_multipliers():DURATION_MULTIPLIER:HIDDEN:NOTE:PHANTOM:baca.SegmentMaker._style_phantom_measures(5)
            <BLANKLINE>
                                }                                                                    %! baca.SegmentMaker._make_multimeasure_rest_container(4):PHANTOM
            <BLANKLINE>
                                \context Voice = "Rest_Voice"                                        %! baca.SegmentMaker._make_multimeasure_rest_container(6):PHANTOM
                                {                                                                    %! baca.SegmentMaker._make_multimeasure_rest_container(6):PHANTOM
            <BLANKLINE>
                                    % [Rest_Voice measure 3]                                         %! baca.SegmentMaker._comment_measure_numbers():baca.SegmentMaker._style_phantom_measures(5):PHANTOM
                                    \once \override Score.TimeSignature.X-extent = ##f               %! baca.SegmentMaker._style_phantom_measures(6):PHANTOM
                                    \once \override MultiMeasureRest.transparent = ##t               %! baca.SegmentMaker._style_phantom_measures(7):PHANTOM
                                    \stopStaff                                                       %! baca.SegmentMaker._style_phantom_measures(8):PHANTOM
                                    \once \override Staff.StaffSymbol.transparent = ##t              %! baca.SegmentMaker._style_phantom_measures(8):PHANTOM
                                    \startStaff                                                      %! baca.SegmentMaker._style_phantom_measures(8):PHANTOM
                                    R1 * 1/4                                                         %! baca.SegmentMaker._make_multimeasure_rest_container(5):PHANTOM:REST_VOICE:MULTIMEASURE_REST
                                %@% ^ \baca-duration-multiplier-markup #"1" #"4"                     %! baca.SegmentMaker._label_duration_multipliers():DURATION_MULTIPLIER:MULTIMEASURE_REST:PHANTOM:REST_VOICE:baca.SegmentMaker._style_phantom_measures(5)
            <BLANKLINE>
                                }                                                                    %! baca.SegmentMaker._make_multimeasure_rest_container(6):PHANTOM
            <BLANKLINE>
                            >>                                                                       %! baca.SegmentMaker._make_multimeasure_rest_container(7):PHANTOM
            <BLANKLINE>
                        }                                                                            %! baca.SingleStaffScoreTemplate.__call__()
            <BLANKLINE>
                    }                                                                                %! baca.SingleStaffScoreTemplate.__call__()
            <BLANKLINE>
                >>                                                                                   %! baca.SingleStaffScoreTemplate.__call__()
            <BLANKLINE>
            >>                                                                                       %! baca.SingleStaffScoreTemplate.__call__()

"""


def persistence():
    """
    Read module-level examples.
    """
    pass
