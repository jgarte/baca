import abjad
import roman


class ScoreTemplate(abjad.ScoreTemplate):
    r'''Score template
    '''

    ### CLASS VARIABLES ###

    __documentation_section__ = '(5) Utilities'

    voice_colors = {
        }

    ### PRIVATE METHODS ###

    @staticmethod
    def _assert_lilypond_identifiers(score):
        for context in abjad.iterate(score).components(abjad.Context):
            if not abjad.String(context.name).is_lilypond_identifier():
                message = f'invalid LilyPond identifier: {context.name!r}'
                raise Exception(message)
        
    @staticmethod
    def _assert_matching_custom_context_names(score):
        for context in abjad.iterate(score).components(abjad.Context):
            if context.context_name in abjad.Context.lilypond_context_names:
                continue
            if context.name != context.context_name:
                message = f'context {context.context_name}'
                message += f' has name {context.name!r}.'
                raise Exception(message)

    @staticmethod
    def _assert_unique_context_names(score):
        names = []
        for context in abjad.iterate(score).components(abjad.Context):
            if context.name in names:
                raise Exception(f'duplicate context name: {context.name!r}.')

    def _attach_tag(self, tag, context):
        for tag_ in tag.split('.'):
            if not abjad.String(tag_).is_lilypond_identifier():
                raise Exception(f'invalid LilyPond identifier: {tag_!r}.')
            if self.parts and tag_ not in self.parts:
                raise Exception(f'not listed in parts manifest: {tag_!r}.')
        literal = abjad.LilyPondLiteral(fr'\tag {tag}', 'before')
        abjad.attach(literal, context)

    def _make_global_context(self):
        global_context_multimeasure_rests = abjad.Context(
            context_name='GlobalRests',
            name='GlobalRests',
            )
        global_context_skips = abjad.Context(
            context_name='GlobalSkips',
            name='GlobalSkips',
            )
        global_context = abjad.Context(
            [
                global_context_multimeasure_rests,
                global_context_skips,
            ],
            context_name='GlobalContext',
            is_simultaneous=True,
            name='GlobalContext',
            )
        return global_context

    @staticmethod
    def _set_square_delimiter(staff_group):
        abjad.setting(staff_group).system_start_delimiter = 'SystemStartSquare'

    @staticmethod
    def _to_roman(n):
        return roman.toRoman(n)

    def _validate_voice_names(self, score):
        voice_names = []
        for voice in abjad.iterate(score).components(abjad.Voice):
            voice_names.append(voice.name)
        for voice_name in sorted(self.voice_colors):
            if voice_name not in voice_names:
                raise Exception(f'voice not in score: {voice_name!r}.')

    ### PUBLIC METHODS ###

    def group_families(self, *families):
        r'''Groups `families` only when more than one family is passed in.

        Returns list of zero or more contexts.
        '''
        families_ = []
        for family in families:
            if family is not None:
                if any(_ for _ in family[1:] if _ is not None):
                    families_.append(family)
        families = families_
        contexts = []
        if len(families) == 0:
            pass
        elif len(families) == 1:
            family = families[0]
            contexts.extend([_ for _ in family[1:] if _ is not None])
        else:
            for family in families:
                if not isinstance(family, tuple):
                    assert isinstance(family, abjad.Context)
                    contexts.append(family)
                    continue
                square_staff_group = self.make_square_staff_group(*family)
                assert square_staff_group is not None
                contexts.append(square_staff_group)
        return contexts

    def make_music_context(self, *contexts):
        contexts = [_ for _ in contexts if _ is not None]
        return abjad.Context(
            contexts,
            context_name='MusicContext',
            is_simultaneous=True,
            name='MusicContext',
            )

    def make_piano_staff(self, stem, *contexts):
        if not isinstance(stem, str):
            raise Exception(f'stem must be string: {stem!r}.')
        contexts = [_ for _ in contexts if _ is not None]
        if contexts:
            piano_staff = abjad.StaffGroup(contexts, name=f'{stem}PianoStaff')
            return piano_staff

    def make_square_staff_group(self, stem, *contexts):
        if not isinstance(stem, str):
            raise Exception(f'stem must be string: {stem!r}.')
        contexts = [_ for _ in contexts if _ is not None]
        if len(contexts) == 1:
            return contexts[0]
        elif 1 < len(contexts):
            staff_group = abjad.StaffGroup(
                contexts,
                name=f'{stem}SquareStaffGroup',
                )
            self._set_square_delimiter(staff_group)
            return staff_group

    def make_staff_group(self, stem, *contexts):
        if not isinstance(stem, str):
            raise Exception(f'stem must be string: {stem!r}.')
        contexts = [_ for _ in contexts if _ is not None]
#        # flatten redundant staff group
#        if len(contexts) == 1 and isinstance(contexts[0], abjad.StaffGroup):
#            contexts_ = abjad.mutate(contexts[0]).eject_contents()
#            staff_group = abjad.StaffGroup(
#                contexts_,
#                name=f'{stem}StaffGroup',
#                )
#            return staff_group
#        elif 1 < len(contexts):
        if contexts:
            staff_group = abjad.StaffGroup(contexts, name=f'{stem}StaffGroup')
            return staff_group
