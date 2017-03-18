# -*- coding: utf-8 -*-
import abjad
import baca
import collections
import copy


class MusicMaker(abjad.abctools.AbjadObject):
    r'''Music-maker.

    ::

        >>> import abjad
        >>> import baca

    ..  container:: example

        Default music-maker:

        ::

            >>> music_maker = baca.MusicMaker()

        ::

            >>> collections = [[0, 2, 10], [18, 16, 15, 20, 19], [9]]
            >>> contribution = music_maker('Voice 1', collections)
            >>> lilypond_file = music_maker.show(contribution)
            >>> show(lilypond_file) # doctest: +SKIP

        ..  doctest::

            >>> f(lilypond_file[abjad.Staff])
            \new Staff <<
                \context Voice = "Voice 1" {
                    \voiceOne
                    {
                        {
                            c'16 [
                            d'16
                            bf'16 ]
                        }
                        {
                            fs''16 [
                            e''16
                            ef''16
                            af''16
                            g''16 ]
                        }
                        {
                            a'16
                        }
                    }
                }
            >>

    '''

    ### CLASS VARIABLES ###

    __documentation_section__ = 'Music'

    __slots__ = (
        '_allow_repeat_pitches',
        '_color_unregistered_pitches',
        '_denominator',
        '_next_figure',
        '_specifiers',
        '_thread',
        '_voice_names',
        )

    _extend_beam_tag = 'extend beam'

    _foreshadow_tag = 'foreshadow'

    _incomplete_tag = 'incomplete'

    _publish_storage_format = True

    _recollection_tag = 'recollection'

    _repeat_pitch_allowed_string = 'repeat pitch allowed'

    _state_variables = (
        '_next_figure',
        )

    ### INITIALIZER ###

    def __init__(
        self,
        *specifiers,
        allow_repeat_pitches=None,
        color_unregistered_pitches=None,
        denominator=None,
        thread=None,
        voice_names=None
        ):
        if allow_repeat_pitches is not None:
            allow_repeat_pitches = bool(allow_repeat_pitches)
        self._allow_repeat_pitches = allow_repeat_pitches
        if color_unregistered_pitches is not None:
            color_unregistered_pitches = bool(color_unregistered_pitches)
        self._color_unregistered_pitches = color_unregistered_pitches
        if denominator is not None:
            assert abjad.mathtools.is_positive_integer(denominator)
        self._denominator = denominator
        self._next_figure = 0
        self._specifiers = specifiers
        if thread is not None:
            thread = bool(thread)
        self._thread = thread
        if voice_names is not None:
            assert all([isinstance(_, str) for _ in voice_names])
        self._voice_names = voice_names

    ### SPECIAL METHODS ###

    def __call__(
        self,
        voice_name,
        collections,
        *specifiers,
        allow_repeat_pitches=None,
        color_unregistered_pitches=None,
        division_masks=None,
        exhaustive=None,
        extend_beam=None,
        figure_name=None,
        hide_time_signature=None,
        imbrication_map=None,
        is_foreshadow=None,
        is_incomplete=None,
        is_recollection=None,
        logical_tie_masks=None,
        denominator=None,
        state_manifest=None,
        talea_counts=None,
        talea_denominator=None,
        thread=None,
        time_treatments=None
        ):
        r'''Calls music-maker on `collections` with keywords.

        ..  container:: example

            Default music-maker:

            ::

                >>> music_maker = baca.MusicMaker()

            ::

                >>> collections = [[0, 2, 10], [18, 16, 15, 20, 19], [9]]
                >>> contribution = music_maker('Voice 1', collections)
                >>> lilypond_file = music_maker.show(contribution)
                >>> show(lilypond_file) # doctest: +SKIP

            ..  doctest::

                >>> f(lilypond_file[abjad.Staff])
                \new Staff <<
                    \context Voice = "Voice 1" {
                        \voiceOne
                        {
                            {
                                c'16 [
                                d'16
                                bf'16 ]
                            }
                            {
                                fs''16 [
                                e''16
                                ef''16
                                af''16
                                g''16 ]
                            }
                            {
                                a'16
                            }
                        }
                    }
                >>

        ..  container:: example

            Calltime counts:

            ::

                >>> music_maker = baca.MusicMaker()

            ::

                >>> collections = [[0, 2, 10], [18, 16, 15, 20, 19], [9]]
                >>> contribution = music_maker(
                ...     'Voice 1',
                ...     collections,
                ...     talea_counts=[1, 2],
                ...     )
                >>> lilypond_file = music_maker.show(contribution)
                >>> show(lilypond_file) # doctest: +SKIP

            ..  doctest::

                >>> f(lilypond_file[abjad.Staff])
                \new Staff <<
                    \context Voice = "Voice 1" {
                        \voiceOne
                        {
                            {
                                c'16 [
                                d'8
                                bf'16 ]
                            }
                            {
                                fs''16 [
                                e''8
                                ef''16
                                af''8
                                g''16 ]
                            }
                            {
                                a'16
                            }
                        }
                    }
                >>
                
        ..  container:: example

            Calltime denominator:

            ::

                >>> music_maker = baca.MusicMaker()

            ::

                >>> collections = [[0, 2, 10], [18, 16, 15, 20, 19], [9]]
                >>> contribution = music_maker(
                ...     'Voice 1',
                ...     collections,
                ...     talea_denominator=32,
                ...     )
                >>> lilypond_file = music_maker.show(contribution)
                >>> show(lilypond_file) # doctest: +SKIP

            ..  doctest::

                >>> f(lilypond_file[abjad.Staff])
                \new Staff <<
                    \context Voice = "Voice 1" {
                        \voiceOne
                        {
                            {
                                c'32 [
                                d'32
                                bf'32 ]
                            }
                            {
                                fs''32 [
                                e''32
                                ef''32
                                af''32
                                g''32 ]
                            }
                            {
                                a'32
                            }
                        }
                    }
                >>

        ..  container:: example

            Calltime time treatments:

            ::

                >>> music_maker = baca.MusicMaker()

            ::

                >>> collections = [[0, 2, 10], [18, 16, 15, 20, 19], [9]]
                >>> contribution = music_maker(
                ...     'Voice 1',
                ...     collections,
                ...     time_treatments=[1],
                ...     )
                >>> lilypond_file = music_maker.show(contribution)
                >>> show(lilypond_file) # doctest: +SKIP

            ..  doctest::

                >>> f(lilypond_file[abjad.Staff])
                \new Staff <<
                    \context Voice = "Voice 1" {
                        \voiceOne
                        {
                            \tweak text #tuplet-number::calc-fraction-text
                            \times 4/3 {
                                c'16 [
                                d'16
                                bf'16 ]
                            }
                            \tweak text #tuplet-number::calc-fraction-text
                            \times 6/5 {
                                fs''16 [
                                e''16
                                ef''16
                                af''16
                                g''16 ]
                            }
                            {
                                a'16
                            }
                        }
                    }
                >>

        ..  container:: example

            Rest input:

            ::

                >>> music_maker = baca.MusicMaker()

            ::

                >>> collections = [[0, 2, 10], [18, 16, 15, 20, 19], [9]]
                >>> contribution = music_maker(
                ...     'Voice 1',
                ...     [abjad.Rest((3, 8)), abjad.Rest((3, 8))],
                ...     baca.nest('+1/8'),
                ...     )
                >>> lilypond_file = music_maker.show(contribution)
                >>> show(lilypond_file) # doctest: +SKIP

            ..  doctest::

                >>> f(lilypond_file[abjad.Staff])
                \new Staff <<
                    \context Voice = "Voice 1" {
                        \voiceOne
                        {
                            \tweak text #tuplet-number::calc-fraction-text
                            \times 7/6 {
                                {
                                    r4.
                                    r4.
                                }
                            }
                        }
                    }
                >>

        ..  container:: example

            The following negative-valued talea count patterns work:

            ::

                >>> music_maker = baca.MusicMaker()

            ::

                >>> contribution = music_maker(
                ...     'Voice 1',
                ...     [[18, 16, 15, 20, 19]],
                ...     talea_counts=[2, -1],
                ...     )
                >>> lilypond_file = music_maker.show(contribution)
                >>> show(lilypond_file) # doctest: +SKIP

            ..  doctest::

                >>> f(lilypond_file[abjad.Staff])
                \new Staff <<
                    \context Voice = "Voice 1" {
                        \voiceOne
                        {
                            {
                                fs''8
                                r16
                                e''8
                                r16
                                ef''8
                                r16
                                af''8
                                r16
                                g''8
                                r16
                            }
                        }
                    }
                >>

            ::

                >>> contribution = music_maker(
                ...     'Voice 1',
                ...     [[18, 16, 15, 20, 19]],
                ...     talea_counts=[2, -1, -1],
                ...     )
                >>> lilypond_file = music_maker.show(contribution)
                >>> show(lilypond_file) # doctest: +SKIP

            ..  doctest::

                >>> f(lilypond_file[abjad.Staff])
                \new Staff <<
                    \context Voice = "Voice 1" {
                        \voiceOne
                        {
                            {
                                fs''8
                                r16
                                r16
                                e''8
                                r16
                                r16
                                ef''8
                                r16
                                r16
                                af''8
                                r16
                                r16
                                g''8
                                r16
                                r16
                            }
                        }
                    }
                >>

            ::

                >>> contribution = music_maker(
                ...     'Voice 1',
                ...     [[18, 16, 15, 20, 19]],
                ...     talea_counts=[-1, 2],
                ...     )
                >>> lilypond_file = music_maker.show(contribution)
                >>> show(lilypond_file) # doctest: +SKIP

            ..  doctest::

                >>> f(lilypond_file[abjad.Staff])
                \new Staff <<
                    \context Voice = "Voice 1" {
                        \voiceOne
                        {
                            {
                                r16
                                fs''8
                                r16
                                e''8
                                r16
                                ef''8
                                r16
                                af''8
                                r16
                                g''8
                            }
                        }
                    }
                >>

            ::

                >>> contribution = music_maker(
                ...     'Voice 1',
                ...     [[18, 16, 15, 20, 19]],
                ...     talea_counts=[-1, -1, 2],
                ...     )
                >>> lilypond_file = music_maker.show(contribution)
                >>> show(lilypond_file) # doctest: +SKIP

            ..  doctest::

                >>> f(lilypond_file[abjad.Staff])
                \new Staff <<
                    \context Voice = "Voice 1" {
                        \voiceOne
                        {
                            {
                                r16
                                r16
                                fs''8
                                r16
                                r16
                                e''8
                                r16
                                r16
                                ef''8
                                r16
                                r16
                                af''8
                                r16
                                r16
                                g''8
                            }
                        }
                    }
                >>

            ::

                >>> contribution = music_maker(
                ...     'Voice 1',
                ...     [[18, 16, 15, 20, 19]],
                ...     talea_counts=[-1, -1, 2, -2, -2],
                ...     )
                >>> lilypond_file = music_maker.show(contribution)
                >>> show(lilypond_file) # doctest: +SKIP

            ..  doctest::

                >>> f(lilypond_file[abjad.Staff])
                \new Staff <<
                    \context Voice = "Voice 1" {
                        \voiceOne
                        {
                            {
                                r16
                                r16
                                fs''8
                                r8
                                r8
                                r16
                                r16
                                e''8
                                r8
                                r8
                                r16
                                r16
                                ef''8
                                r8
                                r8
                                r16
                                r16
                                af''8
                                r8
                                r8
                                r16
                                r16
                                g''8
                                r8
                                r8
                            }
                        }
                    }
                >>

        ..  note:: Write hide_time_signature calltime examples.


        ..  container:: example

            Works with chords:

            ::

                >>> music_maker = baca.MusicMaker()

            ::

                >>> collections = [
                ...     {0, 2, 10},
                ...     [18, 16, 15, 20, 19],
                ...     [9],
                ...     ]
                >>> contribution = music_maker('Voice 1', collections)
                >>> lilypond_file = music_maker.show(contribution)
                >>> show(lilypond_file) # doctest: +SKIP

            ..  doctest::

                >>> f(lilypond_file[abjad.Staff])
                \new Staff <<
                    \context Voice = "Voice 1" {
                        \voiceOne
                        {
                            {
                                <c' d' bf'>16
                            }
                            {
                                fs''16 [
                                e''16
                                ef''16
                                af''16
                                g''16 ]
                            }
                            {
                                a'16
                            }
                        }
                    }
                >>

        Returns selection, time signature, state manifest.
        '''
        if self._is_pitch_input(collections):
            color_unregistered_pitches = False
        self._validate_voice_name(voice_name)
        self._apply_state_manifest(state_manifest)
        specifiers = list(self.specifiers or []) + list(specifiers)
        if all(isinstance(_, abjad.Rest) for _ in collections):
            tuplet = abjad.Tuplet((1, 1), collections)
            selections = [abjad.select(tuplet)]
            specifiers = [
                _ for _ in specifiers
                if not isinstance(_, baca.tools.MusicRhythmSpecifier)
                ]
        else:
            collections = self._coerce_collections(collections)
            collections, specifiers = self._apply_figure_pitch_specifiers(
                collections,
                specifiers,
                )
            collections, specifiers = self._apply_spacing_specifiers(
                collections,
                specifiers,
                )
            selections, specifiers = self._apply_rhythm_specifiers(
                collections,
                specifiers,
                division_masks=division_masks,
                logical_tie_masks=logical_tie_masks,
                talea_counts=talea_counts,
                talea_denominator=talea_denominator,
                thread=thread,
                time_treatments=time_treatments,
                )
        anchor, specifiers = self._get_anchor_specifier(specifiers)
        container = abjad.Container(selections)
        self._color_unregistered_pitches_(
            container,
            color_unregistered_pitches=color_unregistered_pitches,
            )
        specifiers = self._apply_tie_specifiers(selections, specifiers)
        specifiers = self._apply_cluster_specifiers(selections, specifiers)
        specifiers = self._apply_nesting_specifiers(selections, specifiers)
        specifiers = self._apply_register_specifiers(selections, specifiers)
        imbricated_selections, specifiers = self._apply_imbrication_specifiers(
            container,
            specifiers,
            )
        specifiers, color_selector_result = self._apply_color_specifiers(
            selections,
            specifiers,
            )
        self._apply_remaining_specifiers(selections, specifiers)
        self._label_figure_name_(container, figure_name)
        self._annotate_collection_list(container, collections)
        self._annotate_deployment(
            container,
            is_foreshadow=is_foreshadow,
            is_recollection=is_recollection,
            )
        self._annotate_repeat_pitches(container)
        self._extend_beam_(container, extend_beam)
        self._check_well_formedness(container)
        state_manifest = self._make_state_manifest()
        selection = abjad.select([container])
        time_signature = self._make_time_signature(
            selection,
            denominator=denominator,
            )
        selections = {voice_name: selection}
        selections.update(imbricated_selections)
        for value in selections.values():
            assert isinstance(value, abjad.Selection), repr(value)
        return baca.tools.MusicContribution(
            anchor=anchor,
            color_selector_result=color_selector_result,
            figure_name=figure_name,
            hide_time_signature=hide_time_signature,
            selections=selections,
            state_manifest=state_manifest,
            time_signature=time_signature,
            )

    ### PRIVATE METHODS ###

    @staticmethod
    def _all_are_selections(argument):
        prototype = abjad.Selection
        return all(isinstance(_, prototype) for _ in argument)

    @staticmethod
    def _annotate_collection_list(container, collections):
        for leaf in abjad.iterate(container).by_leaf():
            collections_ = copy.deepcopy(collections)
            abjad.attach(collections_, leaf)

    def _annotate_deployment(
        self,
        argument,
        is_foreshadow=False,
        is_incomplete=False,
        is_recollection=False,
        ):
        if not is_foreshadow and not is_recollection and not is_incomplete:
            return
        for leaf in abjad.iterate(argument).by_leaf():
            if is_foreshadow:
                abjad.attach(self._foreshadow_tag, leaf)
            if is_incomplete:
                abjad.attach(self._incomplete_tag, leaf)
            if is_recollection:
                abjad.attach(self._recollection_tag, leaf)

    def _annotate_repeat_pitches(self, container):
        if not self.allow_repeat_pitches:
            return
        for leaf in abjad.iterate(container).by_leaf(pitched=True):
            abjad.attach(self._repeat_pitch_allowed_string, leaf)

    def _apply_cluster_specifiers(self, selections, specifiers):
        assert self._all_are_selections(selections), repr(selections)
        specifiers_ = []
        for specifier in specifiers:
            if isinstance(specifier, baca.tools.ClusterSpecifier):
                specifier(selections)
            else:
                specifiers_.append(specifier)
        return specifiers_

    def _apply_color_specifiers(self, selections, specifiers):
        assert self._all_are_selections(selections), repr(selections)
        specifiers_ = []
        color_selector_result = None
        for specifier in specifiers:
            if isinstance(specifier, baca.tools.ColorSpecifier):
                color_selector_result = specifier(selections)
            else:
                specifiers_.append(specifier)
        return specifiers_, color_selector_result

    def _apply_figure_pitch_specifiers(self, collections, specifiers):
        prototype = (baca.CollectionList, list, abjad.Sequence)
        assert isinstance(collections, prototype), repr(collections)
        specifiers_, unused_specifiers = [], []
        for specifier in specifiers:
            if isinstance(specifier, baca.tools.MusicPitchSpecifier):
                collections = specifier(collections)
            else:
                unused_specifiers.append(specifier)
        return collections, unused_specifiers

    def _apply_imbrication_specifiers(self, container, specifiers):
        unused_specifiers = []
        imbricated_selections = {}
        for specifier in specifiers:
            if not isinstance(specifier, baca.tools.ImbricationSpecifier):
                unused_specifiers.append(specifier)
                continue
            imbricated_selection = specifier(container)
            imbricated_selections.update(imbricated_selection)
        return imbricated_selections, unused_specifiers
        
    def _apply_nesting_specifiers(self, selections, specifiers):
        assert self._all_are_selections(selections), repr(selections)
        specifiers_ = []
        for specifier in specifiers:
            if isinstance(specifier, baca.tools.NestingSpecifier):
                specifier(selections)
            else:
                specifiers_.append(specifier)
        return specifiers_

    def _apply_register_specifiers(self, selections, specifiers):
        assert self._all_are_selections(selections), repr(selections)
        specifiers_ = []
        prototype = (
            baca.tools.RegisterSpecifier,
            baca.tools.RegisterInterpolationSpecifier,
            baca.tools.RegisterToOctaveSpecifier,
            baca.tools.RegisterTransitionSpecifier,
            )
        for specifier in specifiers:
            if isinstance(specifier, prototype):
                specifier(selections)
            else:
                specifiers_.append(specifier)
        return specifiers_

    def _apply_remaining_specifiers(self, selections, specifiers):
        assert self._all_are_selections(selections), repr(selections)
        for specifier in specifiers:
            if isinstance(specifier, abjad.rhythmmakertools.BeamSpecifier):
                specifier._detach_all_beams(selections)
            specifier(selections)

    def _apply_rhythm_specifiers(
        self,
        collections,
        specifiers,
        division_masks=None,
        logical_tie_masks=None,
        talea_counts=None,
        talea_denominator=None,
        thread=None,
        time_treatments=None,
        ):
        selections = len(collections) * [None]
        rhythm_specifiers, rest_affix_specifiers, specifiers_ = [], [], []
        for specifier in specifiers:
            if isinstance(specifier, baca.tools.MusicRhythmSpecifier):
                rhythm_specifiers.append(specifier)
            elif isinstance(specifier, baca.tools.RestAffixSpecifier):
                rest_affix_specifiers.append(specifier)
            else:
                specifiers_.append(specifier)
        if not rhythm_specifiers:
            rhythm_specifiers.append(self._make_default_rhythm_specifier())
        if not rest_affix_specifiers:
            rest_affix_specifier = None
        elif len(rest_affix_specifiers) == 1:
            rest_affix_specifier = rest_affix_specifiers[0]
        else:
            message = 'no more than 1 rest affix specifier allowed: {!r}.'
            message = message.format(rest_affix_specifiers)
            raise Exception(message)
        thread = thread or self.thread
        for specifier in rhythm_specifiers:
            specifier(
                collections=collections,
                selections=selections,
                division_masks=division_masks,
                logical_tie_masks=logical_tie_masks,
                rest_affix_specifier=rest_affix_specifier,
                talea_counts=talea_counts,
                talea_denominator=talea_denominator,
                thread=thread,
                time_treatments=time_treatments,
                )
        return selections, specifiers_

    def _apply_spacing_specifiers(self, collections, specifiers):
        prototype = (baca.CollectionList, list, abjad.Sequence)
        assert isinstance(collections, prototype), repr(collections)
        specifiers_, unused_specifiers = [], []
        prototype = (
            baca.tools.ArpeggiationSpacingSpecifier,
            baca.tools.ChordalSpacingSpecifier,
            )
        for specifier in specifiers:
            if isinstance(specifier, prototype):
                collections = specifier(collections)
            else:
                unused_specifiers.append(specifier)
        return collections, unused_specifiers

    def _apply_state_manifest(self, state_manifest=None):
        state_manifest = state_manifest or {}
        assert isinstance(state_manifest, dict), repr(state_manifest)
        for key in state_manifest:
            value = state_manifest[key]
            setattr(self, key, value)

    def _apply_tie_specifiers(self, selections, specifiers):
        assert self._all_are_selections(selections), repr(selections)
        specifiers_ = []
        for specifier in specifiers:
            if (isinstance(specifier, baca.tools.SpannerSpecifier) and
                isinstance(specifier.spanner, abjad.Tie)):
                specifier(selections)
            else:
                specifiers_.append(specifier)
        return specifiers_

    @staticmethod
    def _check_well_formedness(selections):
        for component in abjad.iterate(selections).by_class():
            inspector = abjad.inspect_(component)
            if not inspector.is_well_formed():
                report = inspector.tabulate_well_formedness_violations()
                report = repr(component) + '\n' + report
                raise Exception(report)

    @staticmethod
    def _coerce_collections(collections):
        prototype = (abjad.pitchtools.Segment, abjad.pitchtools.Set)
        if isinstance(collections, prototype):
            return baca.CollectionList(collections=[collections])
        item_class = abjad.NumberedPitch
        for collection in collections:
            for item in collection:
                if isinstance(item, str):
                    item_class = abjad.NamedPitch
                    break
        return baca.CollectionList(
            collections=collections,
            item_class=item_class,
            )

    def _color_unregistered_pitches_(
        self,
        argument,
        color_unregistered_pitches=None,
        ):
        if color_unregistered_pitches is None:
            color_unregistered_pitches = self.color_unregistered_pitches
        if not color_unregistered_pitches:
            return
        prototype = (abjad.Note, abjad.Chord)
        agent = abjad.iterate(argument)
        for note in agent.by_leaf(prototype, with_grace_notes=True):
            abjad.attach('not yet registered', note)

    @staticmethod
    def _exactly_double(selections):
        length = len(selections)
        if length % 2 == 1:
            return False
        half_length = int(length / 2)
        for index in range(half_length):
            first_selection = selections[index]
            second_selection = selections[index+half_length]
            first_format = format(first_selection, 'lilypond') 
            second_format = format(second_selection, 'lilypond') 
            if not first_format == second_format:
                return False
        return True

    def _extend_beam_(self, selections, extend_beam):
        if not extend_beam:
            return
        leaves = list(abjad.iterate(selections).by_leaf())
        last_leaf = leaves[-1]
        abjad.attach(self._extend_beam_tag, last_leaf)

    @staticmethod
    def _get_anchor_specifier(specifiers):
        anchor_specifiers, specifiers_ = [], []
        for specifier in specifiers:
            if isinstance(specifier, baca.tools.AnchorSpecifier):
                anchor_specifiers.append(specifier)
            else:
                specifiers_.append(specifier)
        if not anchor_specifiers:
            anchor_specifier = None
        elif len(anchor_specifiers) == 1:
            anchor_specifier = anchor_specifiers[0]
        else:
            message = 'only one anchor specifier allowed: {!r}.'
            message = message.format(anchor_specifiers)
            raise Exception(message)
        return anchor_specifier, specifiers_

    def _get_storage_format_specification(self):
        agent = abjad.systemtools.StorageFormatAgent(self)
        keyword_argument_names = agent.signature_keyword_names
        positional_argument_values = self.specifiers
        return abjad.systemtools.StorageFormatSpecification(
            self,
            keyword_argument_names=keyword_argument_names,
            positional_argument_values=positional_argument_values,
            )

    def _is_pitch_input(self, collections):
        prototype = (abjad.PitchSegment, abjad.PitchSet)
        if isinstance(collections, prototype):
            return True
        try:
            if isinstance(collections[0], prototype):
                return True
        except (IndexError, TypeError):
            pass
        return False

    @staticmethod
    def _label_figure_name_(container, figure_name):
        if figure_name is None:
            return
        figure_name = str(figure_name)
        original_figure_name = figure_name
        parts = figure_name.split('_')
        if len(parts) == 1:
            body = parts[0]
            figure_name = abjad.Markup(body)
        elif len(parts) == 2:
            body, subscript = parts
            figure_name = abjad.Markup.concat([
                abjad.Markup(body),
                abjad.Markup(subscript).sub(),
                ])
        else:
            message = 'unrecognized figure name: {!r}.'
            message = message.format(figure_name)
            raise Exception(figure_name)
        figure_name = abjad.Markup.concat([
            '[',
            figure_name,
            ']',
            ])
        figure_name = figure_name.fontsize(3)
        figure_name = abjad.Markup(figure_name, direction=Up)
        annotation = 'figure name: {}'.format(original_figure_name)
        figure_name._annotation = annotation
        leaves = list(abjad.iterate(container).by_leaf())
        abjad.attach(figure_name, leaves[0])

    @staticmethod
    def _make_default_rhythm_specifier():
        return baca.tools.MusicRhythmSpecifier(
            rhythm_maker=baca.tools.MusicRhythmMaker(),
            )

    def _make_state_manifest(self):
        state_manifest = {}
        for name in self._state_variables:
            value = getattr(self, name)
            state_manifest[name] = value
        return state_manifest

    def _make_time_signature(self, selection, denominator=None):
        if denominator is None:
            denominator = self.denominator
        duration = selection.get_duration()
        if denominator is not None:
            duration = duration.with_denominator(denominator)
        time_signature = abjad.TimeSignature(duration)
        return time_signature

    @staticmethod
    def _normalize_selections(argument):
        if not argument:
            selections = []
        elif isinstance(argument, abjad.Component):
            selections = [abjad.select(argument)]
        elif (isinstance(argument, collections.Iterable) and
            isinstance(argument[0], abjad.Selection)):
            selections = list(argument)
        elif isinstance(argument, abjad.Selection):
            selections = [argument]
        else:
            message = 'unrecognized argument: {!r}.'
            message = message.format(argument)
            raise TypeError(message)
        assert isinstance(selections, list), repr(selections)
        assert all(isinstance(_, abjad.Selection) for _ in selections)
        return selections

    def _print_state_manifest(self):
        state_manifest = self._make_state_manifest()
        for key in sorted(state_manifest):
            value = state_manifest[key]
            message = '{}: {}'
            message = message.format(key, value)
            print(message)

    @staticmethod
    def _to_pitch_item_class(item_class):
        if item_class in (abjad.NamedPitch, abjad.NumberedPitch):
            return item_class
        elif item_class is abjad.NamedPitchClass:
            return abjad.NamedPitch
        elif item_class is abjad.NumberedPitchClass:
            return abjad.NumberedPitch
        else:
            raise TypeError(item_class)

    def _validate_voice_name(self, voice_name): 
        if not isinstance(voice_name, str):
            message = 'voice name must be string: {!r}.'
            message = message.format(voice_name)
            raise TypeError(message)
        if self.voice_names and voice_name not in self.voice_names:
            message = 'unknown voice name: {!r}.'
            message = message.format(voice_name)
            raise ValueError(message)

    ### PUBLIC PROPERTIES ###

    @property
    def allow_repeat_pitches(self):
        r'''Is true when music-maker allows repeat pitches.

        Defaults to none.

        Set to true, false or none.

        Returns true, false or none.
        '''
        return self._allow_repeat_pitches

    @property
    def color_unregistered_pitches(self):
        r'''Is true when music-maker colors unregistered pitches.

        Defaults to none.

        Set to true, false or none.

        Returns true, false or none.
        '''
        return self._color_unregistered_pitches

    @property
    def denominator(self):
        r'''Gets denominator.

        ..  container:: example

            No denominator by default:

            ::

                >>> music_maker = baca.MusicMaker()

            ::

                >>> collections = [
                ...     [0, 2, 10, 18],
                ...     [16, 15, 23, 17],
                ...     [19, 13, 9, 8],
                ...     ]
                >>> contribution = music_maker('Voice 1', collections)
                >>> lilypond_file = music_maker.show(contribution)
                >>> show(lilypond_file) # doctest: +SKIP

            ..  doctest::

                >>> f(lilypond_file[abjad.Staff])
                \new Staff <<
                    \context Voice = "Voice 1" {
                        \voiceOne
                        {
                            {
                                c'16 [
                                d'16
                                bf'16
                                fs''16 ]
                            }
                            {
                                e''16 [
                                ef''16
                                b''16
                                f''16 ]
                            }
                            {
                                g''16 [
                                cs''16
                                a'16
                                af'16 ]
                            }
                        }
                    }
                >>

        ..  container:: example

            Denominator supplied at configuration time:

            ::

                >>> music_maker = baca.MusicMaker(
                ...     denominator=16,
                ...     )

            ::

                >>> collections = [
                ...     [0, 2, 10, 18],
                ...     [16, 15, 23, 17],
                ...     [19, 13, 9, 8],
                ...     ]
                >>> contribution = music_maker('Voice 1', collections)
                >>> lilypond_file = music_maker.show(
                ...     contribution,
                ...     time_signatures=[contribution.time_signature],
                ...     )
                >>> show(lilypond_file) # doctest: +SKIP

            ..  doctest::

                >>> f(lilypond_file[abjad.Staff])
                \new Staff <<
                    \context Voice = "Voice 1" {
                        \voiceOne
                        {
                            {
                                c'16 [
                                d'16
                                bf'16
                                fs''16 ]
                            }
                            {
                                e''16 [
                                ef''16
                                b''16
                                f''16 ]
                            }
                            {
                                g''16 [
                                cs''16
                                a'16
                                af'16 ]
                            }
                        }
                    }
                >>

        ..  container:: example

            Denominator supplied at call time:

            ::

                >>> music_maker = baca.MusicMaker()

            ::

                >>> collections = [
                ...     [0, 2, 10, 18],
                ...     [16, 15, 23, 17],
                ...     [19, 13, 9, 8],
                ...     ]
                >>> contribution = music_maker(
                ...     'Voice 1',
                ...     collections,
                ...     denominator=8,
                ...     )
                >>> lilypond_file = music_maker.show(
                ...     contribution,
                ...     time_signatures=[contribution.time_signature],
                ...     )
                >>> show(lilypond_file) # doctest: +SKIP

            ..  doctest::

                >>> f(lilypond_file[abjad.Staff])
                \new Staff <<
                    \context Voice = "Voice 1" {
                        \voiceOne
                        {
                            {
                                c'16 [
                                d'16
                                bf'16
                                fs''16 ]
                            }
                            {
                                e''16 [
                                ef''16
                                b''16
                                f''16 ]
                            }
                            {
                                g''16 [
                                cs''16
                                a'16
                                af'16 ]
                            }
                        }
                    }
                >>

        ..  container:: example

            Denominator supplied at call time overrides denominator supplied at
            configuration time:

            ::

                >>> music_maker = baca.MusicMaker(
                ...     denominator=16,
                ...     )

            ::

                >>> collections = [
                ...     [0, 2, 10, 18],
                ...     [16, 15, 23, 17],
                ...     [19, 13, 9, 8],
                ...     ]
                >>> contribution = music_maker(
                ...     'Voice 1',
                ...     collections,
                ...     denominator=8,
                ...     )
                >>> lilypond_file = music_maker.show(
                ...     contribution,
                ...     time_signatures=[contribution.time_signature],
                ...     )
                >>> show(lilypond_file) # doctest: +SKIP

            ..  doctest::

                >>> f(lilypond_file[abjad.Staff])
                \new Staff <<
                    \context Voice = "Voice 1" {
                        \voiceOne
                        {
                            {
                                c'16 [
                                d'16
                                bf'16
                                fs''16 ]
                            }
                            {
                                e''16 [
                                ef''16
                                b''16
                                f''16 ]
                            }
                            {
                                g''16 [
                                cs''16
                                a'16
                                af'16 ]
                            }
                        }
                    }
                >>

        Defaults to none.

        Set to positive integer or none.

        Returns positive integer or none.
        '''
        return self._denominator 

    @property
    def specifiers(self):
        r'''Gets specifiers.

        ..  container:: example

            Articulation specifier:

            ::

                >>> music_maker = baca.MusicMaker(
                ...     baca.tools.ArticulationSpecifier(
                ...         articulations=['.'],
                ...         selector=abjad.select().
                ...             by_class(abjad.Note, flatten=True),
                ...         ),
                ...     )

            ::

                >>> collections = [[0, 2, 10], [18, 16, 15, 20, 19], [9]]
                >>> contribution = music_maker('Voice 1', collections)
                >>> lilypond_file = music_maker.show(contribution)
                >>> show(lilypond_file) # doctest: +SKIP

            ..  doctest::

                >>> f(lilypond_file[abjad.Staff])
                \new Staff <<
                    \context Voice = "Voice 1" {
                        \voiceOne
                        {
                            {
                                c'16 -\staccato [
                                d'16 -\staccato
                                bf'16 -\staccato ]
                            }
                            {
                                fs''16 -\staccato [
                                e''16 -\staccato
                                ef''16 -\staccato
                                af''16 -\staccato
                                g''16 -\staccato ]
                            }
                            {
                                a'16 -\staccato
                            }
                        }
                    }
                >>

        ..  container:: example

            Articulation specifier selects notes of nonfirst and nonlast
            tuplets:

            ::

                >>> music_maker = baca.MusicMaker(
                ...     baca.tools.ArticulationSpecifier(
                ...         articulations=[('.', '-')],
                ...         selector=abjad.select().
                ...             by_class(abjad.Tuplet).
                ...             get_slice(
                ...                 start=1, stop=-1, apply_to_each=True).
                ...             by_class(abjad.Note, flatten=True),
                ...         ),
                ...     )

            ::

                >>> collections = [[0, 2, 10], [18, 16, 15, 20, 19], [9]]
                >>> contribution = music_maker('Voice 1', collections)
                >>> lilypond_file = music_maker.show(contribution)
                >>> show(lilypond_file) # doctest: +SKIP

            ..  doctest::

                >>> f(lilypond_file[abjad.Staff])
                \new Staff <<
                    \context Voice = "Voice 1" {
                        \voiceOne
                        {
                            {
                                c'16 [
                                d'16
                                bf'16 ]
                            }
                            {
                                fs''16 -\staccato -\tenuto [
                                e''16 -\staccato -\tenuto
                                ef''16 -\staccato -\tenuto
                                af''16 -\staccato -\tenuto
                                g''16 -\staccato -\tenuto ]
                            }
                            {
                                a'16
                            }
                        }
                    }
                >>

        ..  container:: example

            Register specifier transposes to octave rooted on F#3:

            ::

                >>> music_maker = baca.MusicMaker(
                ...     baca.tools.RegisterSpecifier(
                ...         registration=abjad.Registration(
                ...             [('[A0, C8]', -6)],
                ...             ),
                ...         ),
                ...     )

            ::

                >>> collections = [[0, 2, 10], [18, 16, 15, 20, 19], [9]]
                >>> contribution = music_maker('Voice 1', collections)
                >>> lilypond_file = music_maker.show(contribution)
                >>> show(lilypond_file) # doctest: +SKIP

            ..  doctest::

                >>> f(lilypond_file[abjad.Staff])
                \new Staff <<
                    \context Voice = "Voice 1" {
                        \voiceOne
                        {
                            {
                                c'16 [
                                d'16
                                bf16 ]
                            }
                            {
                                fs16 [
                                e'16
                                ef'16
                                af16
                                g16 ]
                            }
                            {
                                a16
                            }
                        }
                    }
                >>

        ..  container:: example

            Register transition specifier transposes from octave of C4 to
            octave of C5:

            ::

                >>> music_maker = baca.MusicMaker(
                ...     baca.tools.RegisterTransitionSpecifier(
                ...         start_registration=abjad.Registration(
                ...             [('[A0, C8]', 0)],
                ...             ),
                ...         stop_registration=abjad.Registration(
                ...             [('[A0, C8]', 12)],
                ...             ),
                ...         ),
                ...     )

            ::

                >>> collections = [[0, 2, 10], [18, 16, 15, 20, 19], [9]]
                >>> contribution = music_maker('Voice 1', collections)
                >>> lilypond_file = music_maker.show(contribution)
                >>> show(lilypond_file) # doctest: +SKIP

            ..  doctest::

                >>> f(lilypond_file[abjad.Staff])
                \new Staff <<
                    \context Voice = "Voice 1" {
                        \voiceOne
                        {
                            {
                                c'16 [
                                d'16
                                bf'16 ]
                            }
                            {
                                fs'16 [
                                e''16
                                ef''16
                                af'16
                                g''16 ]
                            }
                            {
                                a''16
                            }
                        }
                    }
                >>

        ..  container:: example

            Hairpin specifier selects all leaves:

            ::

                >>> music_maker = baca.MusicMaker(
                ...     baca.tools.DynamicSpecifier(
                ...         dynamic=abjad.Hairpin('p < f'),
                ...         ),
                ...     )

            ::

                >>> collections = [
                ...     [0, 2, 10, 18],
                ...     [16, 15, 23],
                ...     [19, 13, 9, 8],
                ...     ]
                >>> contribution = music_maker('Voice 1', collections)
                >>> lilypond_file = music_maker.show(contribution)
                >>> staff = lilypond_file[abjad.Staff]
                >>> abjad.override(staff).dynamic_line_spanner.staff_padding = 4.5
                >>> show(lilypond_file) # doctest: +SKIP

            ..  doctest::

                >>> f(lilypond_file[abjad.Staff])
                \new Staff \with {
                    \override DynamicLineSpanner.staff-padding = #4.5
                } <<
                    \context Voice = "Voice 1" {
                        \voiceOne
                        {
                            {
                                c'16 \< \p [
                                d'16
                                bf'16
                                fs''16 ]
                            }
                            {
                                e''16 [
                                ef''16
                                b''16 ]
                            }
                            {
                                g''16 [
                                cs''16
                                a'16
                                af'16 \f ]
                            }
                        }
                    }
                >>

        ..  container:: example

            Hairpin specifier selects runs of notes:

            ::

                >>> music_maker = baca.MusicMaker(
                ...     baca.tools.DynamicSpecifier(
                ...         dynamic=abjad.Hairpin('p < f'),
                ...         selector=abjad.select().
                ...             by_leaf().
                ...             by_run(abjad.Note),
                ...         ),
                ...     )

            ::

                >>> collections = [
                ...     [0, 2, 10, 18],
                ...     [15, 23],
                ...     [19, 13, 9, 8],
                ...     ]
                >>> contribution = music_maker(
                ...     'Voice 1',
                ...     collections,
                ...     baca.tools.RestAffixSpecifier(
                ...         pattern=abjad.Pattern(
                ...             indices=[0, -1],
                ...             inverted=True,
                ...             ),
                ...         prefix=[1],
                ...         ),
                ...     )
                >>> lilypond_file = music_maker.show(contribution)
                >>> staff = lilypond_file[abjad.Staff]
                >>> abjad.override(staff).dynamic_line_spanner.staff_padding = 4.5
                >>> show(lilypond_file) # doctest: +SKIP

            ..  doctest::

                >>> f(lilypond_file[abjad.Staff])
                \new Staff \with {
                    \override DynamicLineSpanner.staff-padding = #4.5
                } <<
                    \context Voice = "Voice 1" {
                        \voiceOne
                        {
                            {
                                c'16 \< \p [
                                d'16
                                bf'16
                                fs''16 \f ]
                            }
                            {
                                r16
                                ef''16 \< \p [
                                b''16 ]
                            }
                            {
                                g''16 [
                                cs''16
                                a'16
                                af'16 \f ]
                            }
                        }
                    }
                >>

        ..  container:: example

            Hairpin specifiers select notes of first and last tuplet:

            ::

                >>> music_maker = baca.MusicMaker(
                ...     baca.tools.DynamicSpecifier(
                ...         dynamic=abjad.Hairpin('p < f'),
                ...         selector=abjad.select().
                ...             by_class(abjad.Tuplet).
                ...             get_item(0, apply_to_each=True),
                ...         ),
                ...     baca.tools.DynamicSpecifier(
                ...         dynamic=abjad.Hairpin('f > p'),
                ...         selector=abjad.select().
                ...             by_class(abjad.Tuplet).
                ...             get_item(-1, apply_to_each=True),
                ...         ),
                ...     )

            ::

                >>> collections = [
                ...     [0, 2, 10, 18],
                ...     [16, 15, 23],
                ...     [19, 13, 9, 8],
                ...     ]
                >>> contribution = music_maker('Voice 1', collections)
                >>> lilypond_file = music_maker.show(contribution)
                >>> staff = lilypond_file[abjad.Staff]
                >>> abjad.override(staff).dynamic_line_spanner.staff_padding = 4.5
                >>> show(lilypond_file) # doctest: +SKIP

            ..  doctest::

                >>> f(lilypond_file[abjad.Staff])
                \new Staff \with {
                    \override DynamicLineSpanner.staff-padding = #4.5
                } <<
                    \context Voice = "Voice 1" {
                        \voiceOne
                        {
                            {
                                c'16 \< \p [
                                d'16
                                bf'16
                                fs''16 \f ]
                            }
                            {
                                e''16 [
                                ef''16
                                b''16 ]
                            }
                            {
                                g''16 \> \f [
                                cs''16
                                a'16
                                af'16 \p ]
                            }
                        }
                    }
                >>

        ..  container:: example

            Hairpin specifiers treat first two tuplets and then the rest:

            ::

                >>> music_maker = baca.MusicMaker(
                ...     baca.tools.DynamicSpecifier(
                ...         dynamic=abjad.Hairpin('p < f'),
                ...         selector=abjad.select().
                ...             by_class(abjad.Tuplet).
                ...             get_slice(stop=2, apply_to_each=True).
                ...             by_leaf(),
                ...         ),
                ...     baca.tools.DynamicSpecifier(
                ...         dynamic=abjad.Hairpin('f > p'),
                ...         selector=abjad.select().
                ...             by_class(abjad.Tuplet).
                ...             get_slice(start=2, apply_to_each=True).
                ...             by_leaf(),
                ...         ),
                ...     )

            ::

                >>> collections = [
                ...     [0, 2, 10, 18],
                ...     [16, 15, 23],
                ...     [19, 13, 9, 8],
                ...     ]
                >>> contribution = music_maker('Voice 1', collections)
                >>> lilypond_file = music_maker.show(contribution)
                >>> staff = lilypond_file[abjad.Staff]
                >>> abjad.override(staff).dynamic_line_spanner.staff_padding = 6
                >>> show(lilypond_file) # doctest: +SKIP

            ..  doctest::

                >>> f(lilypond_file[abjad.Staff])
                \new Staff \with {
                    \override DynamicLineSpanner.staff-padding = #6
                } <<
                    \context Voice = "Voice 1" {
                        \voiceOne
                        {
                            {
                                c'16 \< \p [
                                d'16
                                bf'16
                                fs''16 ]
                            }
                            {
                                e''16 [
                                ef''16
                                b''16 \f ]
                            }
                            {
                                g''16 \> \f [
                                cs''16
                                a'16
                                af'16 \p ]
                            }
                        }
                    }
                >>

        ..  container:: example

            Spanner specifier selects all leaves by default:

            ::

                >>> music_maker = baca.MusicMaker(
                ...     baca.tools.SpannerSpecifier(
                ...         spanner=abjad.Slur(),
                ...         ),
                ...     )

            ::

                >>> collections = [
                ...     [0, 2, 10, 18],
                ...     [16, 15, 23],
                ...     [19, 13, 9, 8],
                ...     ]
                >>> contribution = music_maker('Voice 1', collections)
                >>> lilypond_file = music_maker.show(contribution)
                >>> staff = lilypond_file[abjad.Staff]
                >>> abjad.override(staff).stem.direction = Down
                >>> show(lilypond_file) # doctest: +SKIP

            ..  doctest::

                >>> f(lilypond_file[abjad.Staff])
                \new Staff \with {
                    \override Stem.direction = #down
                } <<
                    \context Voice = "Voice 1" {
                        \voiceOne
                        {
                            {
                                c'16 [ (
                                d'16
                                bf'16
                                fs''16 ]
                            }
                            {
                                e''16 [
                                ef''16
                                b''16 ]
                            }
                            {
                                g''16 [
                                cs''16
                                a'16
                                af'16 ] )
                            }
                        }
                    }
                >>

        ..  container:: example

            Slur specifier selects all components in each tuplet:

            ::

                >>> music_maker = baca.MusicMaker(
                ...     baca.tools.SpannerSpecifier(
                ...         selector=abjad.select().
                ...             by_class(abjad.Tuplet, flatten=True).
                ...             get_slice(apply_to_each=True),
                ...         spanner=abjad.Slur(),
                ...         ),
                ...     )

            ::

                >>> collections = [
                ...     [0, 2, 10, 18],
                ...     [16, 15, 23],
                ...     [19, 13, 9, 8],
                ...     ]
                >>> contribution = music_maker('Voice 1', collections)
                >>> lilypond_file = music_maker.show(contribution)
                >>> staff = lilypond_file[abjad.Staff]
                >>> abjad.override(staff).stem.direction = Down
                >>> show(lilypond_file) # doctest: +SKIP

            ..  doctest::

                >>> f(lilypond_file[abjad.Staff])
                \new Staff \with {
                    \override Stem.direction = #down
                } <<
                    \context Voice = "Voice 1" {
                        \voiceOne
                        {
                            {
                                c'16 [ (
                                d'16
                                bf'16
                                fs''16 ] )
                            }
                            {
                                e''16 [ (
                                ef''16
                                b''16 ] )
                            }
                            {
                                g''16 [ (
                                cs''16
                                a'16
                                af'16 ] )
                            }
                        }
                    }
                >>

        ..  container:: example

            Slur specifier selects first two components of each tuplet:

            ::

                >>> music_maker = baca.MusicMaker(
                ...     baca.tools.SpannerSpecifier(
                ...         selector=abjad.select().
                ...             by_class(abjad.Tuplet, flatten=True).
                ...             get_slice(stop=2, apply_to_each=True),
                ...         spanner=abjad.Slur(),
                ...         ),
                ...     )

            ::

                >>> collections = [
                ...     [0, 2, 10, 18],
                ...     [16, 15, 23],
                ...     [19, 13, 9, 8],
                ...     ]
                >>> contribution = music_maker('Voice 1', collections)
                >>> lilypond_file = music_maker.show(contribution)
                >>> staff = lilypond_file[abjad.Staff]
                >>> abjad.override(staff).stem.direction = Down
                >>> show(lilypond_file) # doctest: +SKIP

            ..  doctest::

                >>> f(lilypond_file[abjad.Staff])
                \new Staff \with {
                    \override Stem.direction = #down
                } <<
                    \context Voice = "Voice 1" {
                        \voiceOne
                        {
                            {
                                c'16 [ (
                                d'16 )
                                bf'16
                                fs''16 ]
                            }
                            {
                                e''16 [ (
                                ef''16 )
                                b''16 ]
                            }
                            {
                                g''16 [ (
                                cs''16 )
                                a'16
                                af'16 ]
                            }
                        }
                    }
                >>

        ..  container:: example

            Slur specifier selects last two components of each tuplet:

            ::

                >>> music_maker = baca.MusicMaker(
                ...     baca.tools.SpannerSpecifier(
                ...         selector=abjad.select().
                ...             by_class(abjad.Tuplet, flatten=True).
                ...             get_slice(start=-2, apply_to_each=True),
                ...         spanner=abjad.Slur(),
                ...         ),
                ...     )

            ::

                >>> collections = [
                ...     [0, 2, 10, 18],
                ...     [16, 15, 23],
                ...     [19, 13, 9, 8],
                ...     ]
                >>> contribution = music_maker('Voice 1', collections)
                >>> lilypond_file = music_maker.show(contribution)
                >>> staff = lilypond_file[abjad.Staff]
                >>> abjad.override(staff).stem.direction = Down
                >>> show(lilypond_file) # doctest: +SKIP

            ..  doctest::

                >>> f(lilypond_file[abjad.Staff])
                \new Staff \with {
                    \override Stem.direction = #down
                } <<
                    \context Voice = "Voice 1" {
                        \voiceOne
                        {
                            {
                                c'16 [
                                d'16
                                bf'16 (
                                fs''16 ] )
                            }
                            {
                                e''16 [
                                ef''16 (
                                b''16 ] )
                            }
                            {
                                g''16 [
                                cs''16
                                a'16 (
                                af'16 ] )
                            }
                        }
                    }
                >>

        ..  container:: example

            Slur and articulation specifiers:

            ::

                >>> music_maker = baca.MusicMaker(
                ...     baca.tools.ArticulationSpecifier(
                ...         articulations=['.'],
                ...         selector=abjad.select().
                ...             by_class(abjad.Tuplet, flatten=True).
                ...             get_slice(start=1, apply_to_each=True).
                ...             by_class(abjad.Note, flatten=True),
                ...         ),
                ...     baca.tools.SpannerSpecifier(
                ...         selector=abjad.select().
                ...             by_class(abjad.Tuplet, flatten=True).
                ...             get_slice(stop=2, apply_to_each=True),
                ...         spanner=abjad.Slur(),
                ...         ),
                ...     abjad.rhythmmakertools.BeamSpecifier(
                ...         beam_divisions_together=True,
                ...         ),
                ...     )

            ::

                >>> collections = [
                ...     [0, 2, 10, 18],
                ...     [16, 15, 23],
                ...     [19, 13, 9, 8],
                ...     ]
                >>> contribution = music_maker('Voice 1', collections)
                >>> lilypond_file = music_maker.show(contribution)
                >>> staff = lilypond_file[abjad.Staff]
                >>> abjad.override(staff).stem.direction = Down
                >>> show(lilypond_file) # doctest: +SKIP

            ..  doctest::

                >>> f(lilypond_file[abjad.Staff])
                \new Staff \with {
                    \override Stem.direction = #down
                } <<
                    \context Voice = "Voice 1" {
                        \voiceOne
                        {
                            {
                                \set stemLeftBeamCount = #0
                                \set stemRightBeamCount = #2
                                c'16 [ (
                                \set stemLeftBeamCount = #2
                                \set stemRightBeamCount = #2
                                d'16 -\staccato )
                                \set stemLeftBeamCount = #2
                                \set stemRightBeamCount = #2
                                bf'16 -\staccato
                                \set stemLeftBeamCount = #2
                                \set stemRightBeamCount = #1
                                fs''16 -\staccato
                            }
                            {
                                \set stemLeftBeamCount = #1
                                \set stemRightBeamCount = #2
                                e''16 (
                                \set stemLeftBeamCount = #2
                                \set stemRightBeamCount = #2
                                ef''16 -\staccato )
                                \set stemLeftBeamCount = #2
                                \set stemRightBeamCount = #1
                                b''16 -\staccato
                            }
                            {
                                \set stemLeftBeamCount = #1
                                \set stemRightBeamCount = #2
                                g''16 (
                                \set stemLeftBeamCount = #2
                                \set stemRightBeamCount = #2
                                cs''16 -\staccato )
                                \set stemLeftBeamCount = #2
                                \set stemRightBeamCount = #2
                                a'16 -\staccato
                                \set stemLeftBeamCount = #2
                                \set stemRightBeamCount = #0
                                af'16 -\staccato ]
                            }
                        }
                    }
                >>

        ..  container:: example

            Slur specifier selects leaves of first tuplet plus following leaf:

            ::

                >>> music_maker = baca.MusicMaker(
                ...     baca.tools.SpannerSpecifier(
                ...         selector=abjad.select().
                ...             by_class(abjad.Tuplet).
                ...             get_slice(stop=1).
                ...             by_leaf(flatten=False).
                ...             with_next_leaf(),
                ...         spanner=abjad.Slur(),
                ...         ),
                ...     )

            ::

                >>> collections = [
                ...     [0, 2, 10, 18],
                ...     [16, 15, 23],
                ...     [19, 13, 9, 8],
                ...     ]
                >>> contribution = music_maker('Voice 1', collections)
                >>> lilypond_file = music_maker.show(contribution)
                >>> staff = lilypond_file[abjad.Staff]
                >>> abjad.override(staff).stem.direction = Down
                >>> show(lilypond_file) # doctest: +SKIP

            ..  doctest::

                >>> f(lilypond_file[abjad.Staff])
                \new Staff \with {
                    \override Stem.direction = #down
                } <<
                    \context Voice = "Voice 1" {
                        \voiceOne
                        {
                            {
                                c'16 [ (
                                d'16
                                bf'16
                                fs''16 ]
                            }
                            {
                                e''16 ) [
                                ef''16
                                b''16 ]
                            }
                            {
                                g''16 [
                                cs''16
                                a'16
                                af'16 ]
                            }
                        }
                    }
                >>

        ..  container:: example

            Beam specifier beams divisions together:

            ::

                >>> music_maker = baca.MusicMaker(
                ...     abjad.rhythmmakertools.BeamSpecifier(
                ...         beam_divisions_together=True,
                ...         ),
                ...     )

            ::

                >>> collections = [
                ...     [0, 2, 10, 18],
                ...     [16, 15, 23],
                ...     [19, 13, 9, 8],
                ...     ]
                >>> contribution = music_maker('Voice 1', collections)
                >>> lilypond_file = music_maker.show(contribution)
                >>> staff = lilypond_file[abjad.Staff]
                >>> abjad.override(staff).beam.positions = (-6, -6)
                >>> show(lilypond_file) # doctest: +SKIP

            ..  doctest::

                >>> f(lilypond_file[abjad.Staff])
                \new Staff \with {
                    \override Beam.positions = #'(-6 . -6)
                } <<
                    \context Voice = "Voice 1" {
                        \voiceOne
                        {
                            {
                                \set stemLeftBeamCount = #0
                                \set stemRightBeamCount = #2
                                c'16 [
                                \set stemLeftBeamCount = #2
                                \set stemRightBeamCount = #2
                                d'16
                                \set stemLeftBeamCount = #2
                                \set stemRightBeamCount = #2
                                bf'16
                                \set stemLeftBeamCount = #2
                                \set stemRightBeamCount = #1
                                fs''16
                            }
                            {
                                \set stemLeftBeamCount = #1
                                \set stemRightBeamCount = #2
                                e''16
                                \set stemLeftBeamCount = #2
                                \set stemRightBeamCount = #2
                                ef''16
                                \set stemLeftBeamCount = #2
                                \set stemRightBeamCount = #1
                                b''16
                            }
                            {
                                \set stemLeftBeamCount = #1
                                \set stemRightBeamCount = #2
                                g''16
                                \set stemLeftBeamCount = #2
                                \set stemRightBeamCount = #2
                                cs''16
                                \set stemLeftBeamCount = #2
                                \set stemRightBeamCount = #2
                                a'16
                                \set stemLeftBeamCount = #2
                                \set stemRightBeamCount = #0
                                af'16 ]
                            }
                        }
                    }
                >>

        ..  container:: example

            Beam specifier beams nothing:

            ::

                >>> music_maker = baca.MusicMaker(
                ...     abjad.rhythmmakertools.BeamSpecifier(
                ...         beam_each_division=False,
                ...         ),
                ...     )

            ::

                >>> collections = [
                ...     [0, 2, 10, 18],
                ...     [16, 15, 23],
                ...     [19, 13, 9, 8],
                ...     ]
                >>> contribution = music_maker('Voice 1', collections)
                >>> lilypond_file = music_maker.show(contribution)
                >>> show(lilypond_file) # doctest: +SKIP

            ..  doctest::

                >>> f(lilypond_file[abjad.Staff])
                \new Staff <<
                    \context Voice = "Voice 1" {
                        \voiceOne
                        {
                            {
                                c'16
                                d'16
                                bf'16
                                fs''16
                            }
                            {
                                e''16
                                ef''16
                                b''16
                            }
                            {
                                g''16
                                cs''16
                                a'16
                                af'16
                            }
                        }
                    }
                >>

        ..  container:: example

            Nesting specifier augments one sixteenth:

            ::

                >>> music_maker = baca.MusicMaker(
                ...     baca.tools.NestingSpecifier(
                ...         time_treatments=['+1/16'],
                ...         ),
                ...     abjad.rhythmmakertools.BeamSpecifier(
                ...         beam_divisions_together=True,
                ...         ),
                ...     )

            ::

                >>> collections = [
                ...     [0, 2, 10, 18],
                ...     [16, 15, 23],
                ...     [19, 13, 9, 8],
                ...     ]
                >>> contribution = music_maker('Voice 1', collections)
                >>> lilypond_file = music_maker.show(contribution)
                >>> staff = lilypond_file[abjad.Staff]
                >>> abjad.override(staff).beam.positions = (-5.5, -5.5)
                >>> show(lilypond_file) # doctest: +SKIP

            ..  doctest::

                >>> f(lilypond_file[abjad.Staff])
                \new Staff \with {
                    \override Beam.positions = #'(-5.5 . -5.5)
                } <<
                    \context Voice = "Voice 1" {
                        \voiceOne
                        {
                            \tweak text #tuplet-number::calc-fraction-text
                            \times 12/11 {
                                {
                                    \set stemLeftBeamCount = #0
                                    \set stemRightBeamCount = #2
                                    c'16 [
                                    \set stemLeftBeamCount = #2
                                    \set stemRightBeamCount = #2
                                    d'16
                                    \set stemLeftBeamCount = #2
                                    \set stemRightBeamCount = #2
                                    bf'16
                                    \set stemLeftBeamCount = #2
                                    \set stemRightBeamCount = #1
                                    fs''16
                                }
                                {
                                    \set stemLeftBeamCount = #1
                                    \set stemRightBeamCount = #2
                                    e''16
                                    \set stemLeftBeamCount = #2
                                    \set stemRightBeamCount = #2
                                    ef''16
                                    \set stemLeftBeamCount = #2
                                    \set stemRightBeamCount = #1
                                    b''16
                                }
                                {
                                    \set stemLeftBeamCount = #1
                                    \set stemRightBeamCount = #2
                                    g''16
                                    \set stemLeftBeamCount = #2
                                    \set stemRightBeamCount = #2
                                    cs''16
                                    \set stemLeftBeamCount = #2
                                    \set stemRightBeamCount = #2
                                    a'16
                                    \set stemLeftBeamCount = #2
                                    \set stemRightBeamCount = #0
                                    af'16 ]
                                }
                            }
                        }
                    }
                >>

        ..  container:: example

            Nesting specifier augments first two collections one sixteenth:

            ::

                >>> music_maker = baca.MusicMaker(
                ...     baca.tools.NestingSpecifier(
                ...         lmr_specifier=baca.tools.LMRSpecifier(
                ...             left_length=2,
                ...             ),
                ...         time_treatments=['+1/16', None],
                ...         ),
                ...     abjad.rhythmmakertools.BeamSpecifier(
                ...         beam_divisions_together=True,
                ...         ),
                ...     )

            ::

                >>> collections = [
                ...     [0, 2, 10, 18],
                ...     [16, 15, 23],
                ...     [19, 13, 9, 8],
                ...     ]
                >>> contribution = music_maker('Voice 1', collections)
                >>> lilypond_file = music_maker.show(contribution)
                >>> staff = lilypond_file[abjad.Staff]
                >>> abjad.override(staff).beam.positions = (-5.5, -5.5)
                >>> show(lilypond_file) # doctest: +SKIP

            ..  doctest::

                >>> f(lilypond_file[abjad.Staff])
                \new Staff \with {
                    \override Beam.positions = #'(-5.5 . -5.5)
                } <<
                    \context Voice = "Voice 1" {
                        \voiceOne
                        {
                            \tweak text #tuplet-number::calc-fraction-text
                            \times 8/7 {
                                {
                                    \set stemLeftBeamCount = #0
                                    \set stemRightBeamCount = #2
                                    c'16 [
                                    \set stemLeftBeamCount = #2
                                    \set stemRightBeamCount = #2
                                    d'16
                                    \set stemLeftBeamCount = #2
                                    \set stemRightBeamCount = #2
                                    bf'16
                                    \set stemLeftBeamCount = #2
                                    \set stemRightBeamCount = #1
                                    fs''16
                                }
                                {
                                    \set stemLeftBeamCount = #1
                                    \set stemRightBeamCount = #2
                                    e''16
                                    \set stemLeftBeamCount = #2
                                    \set stemRightBeamCount = #2
                                    ef''16
                                    \set stemLeftBeamCount = #2
                                    \set stemRightBeamCount = #1
                                    b''16
                                }
                            }
                            {
                                \set stemLeftBeamCount = #1
                                \set stemRightBeamCount = #2
                                g''16
                                \set stemLeftBeamCount = #2
                                \set stemRightBeamCount = #2
                                cs''16
                                \set stemLeftBeamCount = #2
                                \set stemRightBeamCount = #2
                                a'16
                                \set stemLeftBeamCount = #2
                                \set stemRightBeamCount = #0
                                af'16 ]
                            }
                        }
                    }
                >>

        ..  container:: example

            Sixteenths followed by eighths:

            ::

                >>> music_maker = baca.MusicMaker(
                ...     baca.tools.MusicRhythmSpecifier(
                ...         rhythm_maker=baca.tools.MusicRhythmMaker(
                ...             talea=abjad.rhythmmakertools.Talea(
                ...                 counts=[1],
                ...                 denominator=8,
                ...                 ),
                ...             ),
                ...         ),
                ...     baca.tools.MusicRhythmSpecifier(
                ...         pattern=abjad.select_first(),
                ...         rhythm_maker=baca.tools.MusicRhythmMaker(
                ...             talea=abjad.rhythmmakertools.Talea(
                ...                 counts=[1],
                ...                 denominator=16,
                ...                 ),
                ...             ),
                ...         ),
                ...     )

            ::

                >>> collections = [[0, 2, 10], [18, 16, 15, 20, 19], [9]]
                >>> contribution = music_maker('Voice 1', collections)
                >>> lilypond_file = music_maker.show(contribution)
                >>> show(lilypond_file) # doctest: +SKIP

            ..  doctest::

                >>> f(lilypond_file[abjad.Staff])
                \new Staff <<
                    \context Voice = "Voice 1" {
                        \voiceOne
                        {
                            {
                                c'16 [
                                d'16
                                bf'16 ]
                            }
                            {
                                fs''8 [
                                e''8
                                ef''8
                                af''8
                                g''8 ]
                            }
                            {
                                a'8
                            }
                        }
                    }
                >>

        ..  container:: example

            Sixteenths surrounding dotted eighths:

            ::

                >>> music_maker = baca.MusicMaker(
                ...     baca.tools.MusicRhythmSpecifier(
                ...         rhythm_maker=baca.tools.MusicRhythmMaker(
                ...             talea=abjad.rhythmmakertools.Talea(
                ...                 counts=[3],
                ...                 denominator=16,
                ...                 ),
                ...             ),
                ...         ),
                ...     baca.tools.MusicRhythmSpecifier(
                ...         pattern=abjad.Pattern(indices=[0, -1]),
                ...         rhythm_maker=baca.tools.MusicRhythmMaker(
                ...             talea=abjad.rhythmmakertools.Talea(
                ...                 counts=[1],
                ...                 denominator=16,
                ...                 ),
                ...             ),
                ...         ),
                ...     )

            ::

                >>> collections = [[0, 2, 10], [18, 16, 15, 20, 19], [9]]
                >>> contribution = music_maker('Voice 1', collections)
                >>> lilypond_file = music_maker.show(contribution)
                >>> show(lilypond_file) # doctest: +SKIP

            ..  doctest::

                >>> f(lilypond_file[abjad.Staff])
                \new Staff <<
                    \context Voice = "Voice 1" {
                        \voiceOne
                        {
                            {
                                c'16 [
                                d'16
                                bf'16 ]
                            }
                            {
                                fs''8. [
                                e''8.
                                ef''8.
                                af''8.
                                g''8. ]
                            }
                            {
                                a'16
                            }
                        }
                    }
                >>

        ..  container:: example

            Sixteenths surrounding argumented dotted eighths:

            ::

                >>> music_maker = baca.MusicMaker(
                ...     baca.tools.MusicRhythmSpecifier(
                ...         rhythm_maker=baca.tools.MusicRhythmMaker(
                ...             talea=abjad.rhythmmakertools.Talea(
                ...                 counts=[3],
                ...                 denominator=16,
                ...                 ),
                ...             time_treatments=[1],
                ...             ),
                ...         ),
                ...     baca.tools.MusicRhythmSpecifier(
                ...         pattern=abjad.Pattern(indices=[0, -1]),
                ...         rhythm_maker=baca.tools.MusicRhythmMaker(
                ...             talea=abjad.rhythmmakertools.Talea(
                ...                 counts=[1],
                ...                 denominator=16,
                ...                 ),
                ...             ),
                ...         ),
                ...     )

            ::

                >>> collections = [[0, 2, 10], [18, 16, 15, 20, 19], [9]]
                >>> contribution = music_maker('Voice 1', collections)
                >>> lilypond_file = music_maker.show(contribution)
                >>> show(lilypond_file) # doctest: +SKIP

            ..  doctest::

                >>> f(lilypond_file[abjad.Staff])
                \new Staff <<
                    \context Voice = "Voice 1" {
                        \voiceOne
                        {
                            {
                                c'16 [
                                d'16
                                bf'16 ]
                            }
                            \tweak text #tuplet-number::calc-fraction-text
                            \times 16/15 {
                                fs''8. [
                                e''8.
                                ef''8.
                                af''8.
                                g''8. ]
                            }
                            {
                                a'16
                            }
                        }
                    }
                >>

        ..  container:: example

            Augmented sixteenths surrounding dotted eighths:

            ::

                >>> music_maker = baca.MusicMaker(
                ...     baca.tools.MusicRhythmSpecifier(
                ...         rhythm_maker=baca.tools.MusicRhythmMaker(
                ...             talea=abjad.rhythmmakertools.Talea(
                ...                 counts=[3],
                ...                 denominator=16,
                ...                 ),
                ...             ),
                ...         ),
                ...     baca.tools.MusicRhythmSpecifier(
                ...         pattern=abjad.Pattern(indices=[0, -1]),
                ...         rhythm_maker=baca.tools.MusicRhythmMaker(
                ...             talea=abjad.rhythmmakertools.Talea(
                ...                 counts=[1],
                ...                 denominator=16,
                ...                 ),
                ...             time_treatments=[1],
                ...             ),
                ...         ),
                ...     )

            ::

                >>> collections = [[0, 2, 10], [18, 16, 15, 20, 19], [9]]
                >>> contribution = music_maker('Voice 1', collections)
                >>> lilypond_file = music_maker.show(contribution)
                >>> show(lilypond_file) # doctest: +SKIP

            ..  doctest::

                >>> f(lilypond_file[abjad.Staff])
                \new Staff <<
                    \context Voice = "Voice 1" {
                        \voiceOne
                        {
                            \tweak text #tuplet-number::calc-fraction-text
                            \times 4/3 {
                                c'16 [
                                d'16
                                bf'16 ]
                            }
                            {
                                fs''8. [
                                e''8.
                                ef''8.
                                af''8.
                                g''8. ]
                            }
                            {
                                a'16
                            }
                        }
                    }
                >>

        ..  container:: example

            Diminished sixteenths surrounding dotted eighths:

            ::

                >>> music_maker = baca.MusicMaker(
                ...     baca.tools.MusicRhythmSpecifier(
                ...         rhythm_maker=baca.tools.MusicRhythmMaker(
                ...             talea=abjad.rhythmmakertools.Talea(
                ...                 counts=[3],
                ...                 denominator=16,
                ...                 ),
                ...             ),
                ...         ),
                ...     baca.tools.MusicRhythmSpecifier(
                ...         pattern=abjad.Pattern(indices=[0, -1]),
                ...         rhythm_maker=baca.tools.MusicRhythmMaker(
                ...             talea=abjad.rhythmmakertools.Talea(
                ...                 counts=[1],
                ...                 denominator=16,
                ...                 ),
                ...             time_treatments=[-1],
                ...             ),
                ...         ),
                ...     )

            ::

                >>> collections = [[0, 2, 10], [18, 16, 15, 20, 19], [9]]
                >>> contribution = music_maker('Voice 1', collections)
                >>> lilypond_file = music_maker.show(contribution)
                >>> show(lilypond_file) # doctest: +SKIP

            ..  doctest::

                >>> f(lilypond_file[abjad.Staff])
                \new Staff <<
                    \context Voice = "Voice 1" {
                        \voiceOne
                        {
                            \times 2/3 {
                                c'16 [
                                d'16
                                bf'16 ]
                            }
                            {
                                fs''8. [
                                e''8.
                                ef''8.
                                af''8.
                                g''8. ]
                            }
                            {
                                a'16
                            }
                        }
                    }
                >>

        Defaults to none.

        Set to specifiers or none.

        Returns specifiers or none.
        '''
        return self._specifiers

    @property
    def thread(self):
        r'''Is true when music-maker threads rhythm-maker over collections.

        ..  container:: example

            Does not thread rhythm-maker over collections:

            ::

                >>> music_maker = baca.MusicMaker()

            ::

                >>> collections = [[0, 2, 10], [18, 16, 15, 20, 19], [9]]
                >>> contribution = music_maker(
                ...     'Voice 1',
                ...     collections,
                ...     talea_counts=[1, 2, 3],
                ...     )
                >>> lilypond_file = music_maker.show(contribution)
                >>> show(lilypond_file) # doctest: +SKIP

            ..  doctest::

                >>> f(lilypond_file[abjad.Staff])
                \new Staff <<
                    \context Voice = "Voice 1" {
                        \voiceOne
                        {
                            {
                                c'16 [
                                d'8
                                bf'8. ]
                            }
                            {
                                fs''16 [
                                e''8
                                ef''8.
                                af''16
                                g''8 ]
                            }
                            {
                                a'16
                            }
                        }
                    }
                >>

            Does thread rhythm-maker over collections:

            ::

                >>> collections = [[0, 2, 10], [18, 16, 15, 20, 19], [9]]
                >>> contribution = music_maker(
                ...     'Voice 1',
                ...     collections,
                ...     talea_counts=[1, 2, 3],
                ...     thread=True,
                ...     )
                >>> lilypond_file = music_maker.show(contribution)
                >>> show(lilypond_file) # doctest: +SKIP

            ..  doctest::

                >>> f(lilypond_file[abjad.Staff])
                \new Staff <<
                    \context Voice = "Voice 1" {
                        \voiceOne
                        {
                            {
                                c'16 [
                                d'8
                                bf'8. ]
                            }
                            {
                                fs''16 [
                                e''8
                                ef''8.
                                af''16
                                g''8 ]
                            }
                            {
                                a'8.
                            }
                        }
                    }
                >>

        Set to true, false or none.

        Defaults to none.

        Returns true, false or none.
        '''
        return self._thread

    @property
    def voice_names(self):
        r'''Gets voice names.

        Used to check call-time voice names.

        Defaults to none.

        Set to list of strings or none.

        Returns list or strings or none.
        '''
        if self._voice_names:
            return list(self._voice_names)

    ### PUBLIC METHODS ###

    @staticmethod
    def show(figure_contribution, time_signatures=None):
        r'''Makes rhythm-maker-style LilyPond file for documentation examples.

        Returns LilyPond file.
        '''
        assert isinstance(figure_contribution, baca.tools.MusicContribution)
        return abjad.rhythmmakertools.make_lilypond_file(
            figure_contribution.selections,
            time_signatures=time_signatures,
            attach_lilypond_voice_commands=True,
            )
