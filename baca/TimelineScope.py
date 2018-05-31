import abjad
import baca
import functools
import typing
from .Scope import Scope


class TimelineScope(abjad.AbjadObject):
    """
    Timeline scope.

    ..  container:: example

        >>> scope = baca.timeline([
        ...     ('PianoMusicVoice', (5, 9)),
        ...     ('ClarinetMusicVoice', (7, 12)),
        ...     ('ViolinMusicVoice', (8, 12)),
        ...     ('OboeMusicVoice', (9, 12)),
        ...     ])

        >>> abjad.f(scope, strict=89)
        baca.TimelineScope(
            scopes=(
                baca.Scope(
                    stages=(5, 9),
                    voice_name='PianoMusicVoice',
                    ),
                baca.Scope(
                    stages=(7, 12),
                    voice_name='ClarinetMusicVoice',
                    ),
                baca.Scope(
                    stages=(8, 12),
                    voice_name='ViolinMusicVoice',
                    ),
                baca.Scope(
                    stages=(9, 12),
                    voice_name='OboeMusicVoice',
                    ),
                ),
            )

        ..  container:: example

            >>> baca.TimelineScope()
            TimelineScope()

    """

    ### CLASS VARIABLES ###

    __documentation_section__ = '(5) Utilities'

    __slots__ = (
        '_scopes',
        )

    _publish_storage_format = True

    ### INITIALIZER ###

    def __init__(
        self,
        *,
        scopes=None,
        ):
        if scopes is not None:
            assert isinstance(scopes, (tuple, list))
            scopes_ = []
            for scope in scopes:
                if not isinstance(scope, baca.Scope):
                    scope = baca.Scope(*scope)
                scopes_.append(scope)
            scopes = scopes_
            scopes = tuple(scopes)
        self._scopes = scopes

    ### PRIVATE METHODS ###

    @staticmethod
    def _sort_by_timeline(leaves):
        assert leaves.are_leaves(), repr(leaves)
        def compare(leaf_1, leaf_2):
            start_offset_1 = abjad.inspect(leaf_1).get_timespan().start_offset
            start_offset_2 = abjad.inspect(leaf_2).get_timespan().start_offset
            if start_offset_1 < start_offset_2:
                return -1
            if start_offset_2 < start_offset_1:
                return 1
            index_1 = abjad.inspect(leaf_1).get_parentage().score_index
            index_2 = abjad.inspect(leaf_2).get_parentage().score_index
            if index_1 < index_2:
                return -1
            if index_2 < index_1:
                return 1
            return 0
        leaves = list(leaves)
        leaves.sort(key=functools.cmp_to_key(compare))
        return abjad.select(leaves)

    ### PUBLIC PROPERTIES ###

    @property
    def scopes(self) -> typing.Tuple[Scope]:
        """
        Gets scopes.
        """
        return self._scopes

    @property
    def voice_name(self) -> str:
        """
        Returns ``'TimelineScope'``.
        """
        return 'TimelineScope'