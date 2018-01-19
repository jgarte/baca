import abc
import abjad
import baca


class Command(abjad.AbjadObject):
    r'''Command.
    '''

    ### CLASS VARIABLES ###

    __documentation_section__ = '(4) Commands'

    __slots__ = (
        '_deactivate',
        '_manifests',
        '_selector',
        '_site',
        '_tag',
        )

    _publish_storage_format = True

    ### INITIALIZER ###

    def __init__(
        self,
        deactivate=None,
        selector=None,
        site:str=None,
        tag=None,
        ):
        self._deactivate = deactivate
        self._manifests = None
        if isinstance(selector, str):
            selector = eval(selector)
        if selector is not None:
            prototype = (abjad.Expression, baca.MapCommand)
            assert isinstance(selector, prototype), repr(selector)
        self._selector = selector
        if site is not None:
            assert isinstance(site, str)
        self._site = site
        if tag is not None:
            assert isinstance(tag, str)
        self._tag = tag

    ### SPECIAL METHODS ###

    @abc.abstractmethod
    def __call__(self, argument=None):
        r'''Calls command on `argument`.

        Returns none.
        '''
        pass

    ### PRIVATE METHODS ###

    @staticmethod
    def _are_valid_tags(tags):
        assert isinstance(tags, list), repr(tags)
        assert '' not in tags, repr(tags)
        assert not any(':' in _ for _ in tags), repr(tags)
        return True

    @staticmethod
    def _is_signed_document_name(string:str):
        if not isinstance(string, str):
            return False
        if string[0] not in ('+', '-'):
            return False
        return abjad.String(string[1:]).is_shout_case()

    ### PUBLIC PROPERTIES ###

    @property
    def deactivate(self):
        r'''Is true when tag should write deactivated.

        Returns true, false or none.
        '''
        return self._deactivate

    @property
    def selector(self):
        r'''Gets selector.

        Defaults to none.

        Set to selector or none.

        Returns selector or none.
        '''
        return self._selector

    @property
    def site(self):
        r'''Gets site.

        Defaults to none.

        Set to string or none.

        Returns string or none.
        '''
        return self._site

    @property
    def tag(self):
        r'''Gets tag.

        Defaults to none.

        Set to string or none.

        Returns string or none.
        '''
        return self._tag

    @property
    def tags(self):
        r'''Gets tags.

        Returns list of strings.
        '''
        assert self._are_valid_tags(self._tags)
        return self._tags
