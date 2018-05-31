import abjad
import baca
import typing
from abjadext import rmakers
from .MusicMaker import MusicMaker


class MusicAccumulator(abjad.AbjadObject):
    """
    Music-accumulator.
    """

    ### CLASS VARIABLES ###

    __documentation_section__ = '(2) Makers'

    __slots__ = (
        '_current_offset',
        '_figure_index',
        '_figure_names',
        '_floating_selections',
        '_music_maker',
        '_score_stop_offset',
        '_score_template',
        '_time_signatures',
        '_voice_names',
        )

    ### INITIALIZER ###

    def __init__(
        self,
        score_template: abjad.ScoreTemplate,
        ) -> None:
        self._score_template = score_template
        voice_names = []
        dummy_score = score_template()
        for voice in abjad.iterate(dummy_score).components(abjad.Voice):
            voice_names.append(voice.name)
        self._voice_names = voice_names
        self._current_offset = abjad.Offset(0)
        self._figure_index = 0
        self._music_maker = self._make_default_figure_maker()
        self._figure_names: typing.List[str] = []
        self._floating_selections = self._make_voice_dictionary()
        self._score_stop_offset = abjad.Offset(0)
        self._time_signatures: typing.List[abjad.TimeSignature] = []

    ### SPECIAL METHODS ###

    def __call__(self, music_contribution=None):
        r"""
        Calls figure-accumulator on ``music_contribution``.

        Raises exception on duplicate figure name.

        ..  container:: example

            >>> score_template = baca.StringTrioScoreTemplate()
            >>> accumulator = baca.MusicAccumulator(score_template=score_template)
            >>> accumulator(
            ...     accumulator.music_maker(
            ...         'ViolinMusicVoice',
            ...         [[0, 1, 2, 3]],
            ...         figure_name='D',
            ...         ),
            ...     )

            >>> accumulator(
            ...     accumulator.music_maker(
            ...         'ViolinMusicVoice',
            ...         [[4, 5, 6, 7]],
            ...         figure_name='D',
            ...         ),
            ...     )
            Traceback (most recent call last):
                ...
            Exception: duplicate figure name: 'D'.

        Returns none.
        """
        self._cache_figure_name(music_contribution)
        self._cache_floating_selection(music_contribution)
        self._cache_time_signature(music_contribution)
        self._figure_index += 1

    ### PRIVATE METHODS ###

    def _cache_figure_name(self, music_contribution):
        if music_contribution.figure_name is None:
            return
        if music_contribution.figure_name in self._figure_names:
            name = music_contribution.figure_name
            raise Exception(f'duplicate figure name: {name!r}.')
        self._figure_names.append(music_contribution.figure_name)

    def _cache_floating_selection(self, music_contribution):
        for voice_name in music_contribution:
            voice_name = self.score_template.voice_abbreviations.get(
                voice_name,
                voice_name,
                )
            selection = music_contribution[voice_name]
            if not selection:
                continue
            start_offset = self._get_start_offset(
                selection,
                music_contribution,
                )
            stop_offset = start_offset + abjad.inspect(selection).get_duration()
            timespan = abjad.Timespan(start_offset, stop_offset)
            floating_selection = abjad.AnnotatedTimespan(
                timespan.start_offset,
                timespan.stop_offset,
                annotation=selection,
                )
            self._floating_selections[voice_name].append(floating_selection)
        self._current_offset = stop_offset
        self._score_stop_offset = max(self._score_stop_offset, stop_offset)

    def _cache_time_signature(self, music_contribution):
        if music_contribution.hide_time_signature:
            return
        if (music_contribution.anchor is None or
            music_contribution.hide_time_signature is False or
            (music_contribution.anchor and
            music_contribution.anchor.remote_voice_name is None)):
            self.time_signatures.append(music_contribution.time_signature)

    def _get_figure_start_offset(self, figure_name):
        for voice_name in sorted(self._floating_selections.keys()):
            for floating_selection in self._floating_selections[voice_name]:
                leaf_start_offset = floating_selection.start_offset
                leaves = abjad.iterate(floating_selection.annotation).leaves()
                for leaf in leaves:
                    markup = abjad.inspect(leaf).get_indicators(abjad.Markup)
                    for markup_ in markup:
                        if (isinstance(markup_._annotation, str) and
                            markup_._annotation.startswith('figure name: ')):
                            figure_name_ = markup_._annotation
                            figure_name_ = figure_name_.replace(
                                'figure name: ',
                                '',
                                )
                            if figure_name_ == figure_name:
                                return leaf_start_offset
                    leaf_duration = abjad.inspect(leaf).get_duration()
                    leaf_start_offset += leaf_duration
        raise Exception(f'can not find figure {figure_name!r}.')

    def _get_leaf_timespan(self, leaf, floating_selections):
        found_leaf = False
        for floating_selection in floating_selections:
            leaf_start_offset = abjad.Offset(0)
            for leaf_ in abjad.iterate(floating_selection.annotation).leaves():
                leaf_duration = abjad.inspect(leaf_).get_duration()
                if leaf_ is leaf:
                    found_leaf = True
                    break
                leaf_start_offset += leaf_duration
            if found_leaf:
                break
        if not found_leaf:
            raise Exception(f'can not find {leaf!r} in floating selections.')
        selection_start_offset = floating_selection.start_offset
        leaf_start_offset = selection_start_offset + leaf_start_offset
        leaf_stop_offset = leaf_start_offset + leaf_duration
        return abjad.Timespan(leaf_start_offset, leaf_stop_offset)

    def _get_start_offset(self, selection, music_contribution):
        if (music_contribution.anchor is not None and
            music_contribution.anchor.figure_name is not None):
            figure_name = music_contribution.anchor.figure_name
            start_offset = self._get_figure_start_offset(figure_name)
            return start_offset
        anchored = False
        if music_contribution.anchor is not None:
            remote_voice_name = music_contribution.anchor.remote_voice_name
            remote_selector = music_contribution.anchor.remote_selector
            use_remote_stop_offset = \
                music_contribution.anchor.use_remote_stop_offset
            anchored = True
        else:
            remote_voice_name = None
            remote_selector = None
            use_remote_stop_offset = None
        if not anchored:
            return self._current_offset
        if anchored and remote_voice_name is None:
            return self._score_stop_offset
        remote_selector = remote_selector or baca.leaf(0)
        floating_selections = self._floating_selections[remote_voice_name]
        selections = [_.annotation for _ in floating_selections]
        result = remote_selector(selections)
        selected_leaves = list(abjad.iterate(result).leaves())
        first_selected_leaf = selected_leaves[0]
        timespan = self._get_leaf_timespan(
            first_selected_leaf,
            floating_selections,
            )
        if use_remote_stop_offset:
            remote_anchor_offset = timespan.stop_offset
        else:
            remote_anchor_offset = timespan.start_offset
        local_anchor_offset = abjad.Offset(0)
        if music_contribution.anchor is not None:
            local_selector = music_contribution.anchor.local_selector
        else:
            local_selector = None
        if local_selector is not None:
            result = local_selector(selection)
            selected_leaves = list(abjad.iterate(result).leaves())
            first_selected_leaf = selected_leaves[0]
            dummy_container = abjad.Container(selection)
            timespan = abjad.inspect(first_selected_leaf).get_timespan()
            del(dummy_container[:])
            local_anchor_offset = timespan.start_offset
        start_offset = remote_anchor_offset - local_anchor_offset
        return start_offset

    @staticmethod
    def _insert_skips(floating_selections, voice_name):
        for floating_selection in floating_selections:
            assert isinstance(floating_selection, abjad.AnnotatedTimespan)
        floating_selections = list(floating_selections)
        floating_selections.sort()
        try:
            first_start_offset = floating_selections[0].start_offset
        except:
            raise Exception(floating_selections, voice_name)
        timespans = abjad.TimespanList(floating_selections)
        gaps = ~timespans
        if 0 < first_start_offset:
            first_gap = abjad.Timespan(0, first_start_offset)
            gaps.append(first_gap)
        selections = floating_selections + list(gaps)
        selections.sort()
        fused_selection = []
        for selection in selections:
            if isinstance(selection, abjad.AnnotatedTimespan):
                fused_selection.extend(selection.annotation)
            else:
                assert isinstance(selection, abjad.Timespan)
                multiplier = abjad.Multiplier(selection.duration)
                skip = abjad.Skip(1)
                abjad.attach(multiplier, skip)
                fused_selection.append(skip)
        fused_selection = abjad.select(fused_selection)
        return fused_selection

    @staticmethod
    def _make_default_figure_maker():
        return MusicMaker(
            rmakers.BeamSpecifier(
                beam_divisions_together=True,
                ),
            baca.PitchFirstRhythmCommand(
                rhythm_maker=baca.PitchFirstRhythmMaker(
                    talea=rmakers.Talea(
                        counts=[1],
                        denominator=16,
                        ),
                    ),
                ),
            color_unregistered_pitches=True,
            denominator=16,
            )

    def _make_voice_dictionary(self):
        return dict([(_, []) for _ in self._voice_names])

    ### PUBLIC PROPERTIES ###

    @property
    def music_maker(self) -> MusicMaker:
        """
        Gets default music-maker.
        """
        return self._music_maker

    @property
    def score_template(self) -> abjad.ScoreTemplate:
        """
        Gets score template.
        """
        return self._score_template

    @property
    def time_signatures(self) -> typing.List[abjad.TimeSignature]:
        """
        Gets time signatures.
        """
        return self._time_signatures

    ### PUBLIC METHODS ###

    def assemble(self, voice_name):
        """
        Assembles complete selection for ``voice_name``.

        Returns selection or none.
        """
        floating_selections = self._floating_selections[voice_name]
        if not floating_selections:
            return
        selection = self._insert_skips(floating_selections, voice_name)
        assert isinstance(selection, abjad.Selection), repr(selection)
        return selection

    def populate_segment_maker(self, segment_maker):
        """
        Populates ``segment_maker``.

        Returns none.
        """
        for voice_name in sorted(self._floating_selections):
            selection = self.assemble(voice_name)
            if selection:
                segment_maker(
                    (voice_name, 1),
                    baca.make_rhythm(selection)
                    )

    @staticmethod
    def show(contribution, time_signatures):
        """
        Makes rhythm-maker-style LilyPond file for documentation examples.

        Returns LilyPond file.
        """
        return abjad.LilyPondFile.rhythm(
            contribution,
            divisions=time_signatures,
            pitched_staff=True,
            )