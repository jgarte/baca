import abjad
import baca
import collections
import copy
from .Command import Command


class PiecewiseCommand(Command):
    r'''Piecewise command.
    '''

    ### CLASS VARIABLES ###

    __slots__ = (
        '_bookend',
        '_indicators',
        '_selector',
        '_spanner',
        )

    ### INITIALIZER ###

    def __init__(
        self,
        bookend=None,
        indicators=None,
        selector=None,
        spanner=None,
        ):
        Command.__init__(self, selector=selector)
        if bookend is not None:
            bookend = bool(bookend)
        self._bookend = bookend
        if indicators is not None:
            indicators = abjad.CyclicTuple(indicators)
        self._indicators = indicators
        if spanner is not None:
            assert isinstance(spanner, (abjad.Spanner, baca.SpannerCommand))
        self._spanner = spanner

    ### SPECIAL METHODS ###

    def __call__(self, argument=None):
        r'''Calls command on `argument`.

        Returns none.
        '''
        if self.spanner is None:
            return
        if not self.indicators:
            return
        if argument is None:
            return
        if self.selector is not None:
            argument = self.selector(argument)
        if isinstance(self.spanner, abjad.Spanner):
            spanner = copy.copy(self.spanner)
            leaves = abjad.select(argument).leaves()
            abjad.attach(spanner, leaves)
        else:
            spanner = self.spanner(argument)
        for i, item in enumerate(argument):
            leaf = baca.select(item).leaf(0)
            indicator = self.indicators[i]
            self._attach_indicators(spanner, indicator, leaf)
            if not self.bookend:
                continue
            if len(item) <= 1:
                continue
            leaf = baca.select(item).leaf(-1)
            if leaf not in spanner:
                continue
            indicator = self.indicators[i + 1]
            self._attach_indicators(spanner, indicator, leaf)

    ### PRIVATE METHODS ###

    @staticmethod
    def _attach_indicators(spanner, argument, leaf):
        if not isinstance(argument, tuple):
            argument = (argument,)
        for argument_ in argument:
            if isinstance(argument_, baca.IndicatorCommand):
                for indicator in argument_.arguments:
                    spanner.attach(indicator, leaf)
            else:
                spanner.attach(argument_, leaf)

    ### PUBLIC PROPERTIES ###

    @property
    def bookend(self):
        r'''Is true when command bookend-attaches indicators.

        Returns true, false or none.
        '''
        return self._bookend

    @property
    def indicators(self):
        r'''Gets indicators.

        Returns cyclic tuple or none.
        '''
        return self._indicators

    @property
    def selector(self):
        r'''Gets selector.

        Returns selector or none.
        '''
        return self._selector

    @property
    def spanner(self):
        r'''Gets spanner command.

        Returns spanner command or none.
        '''
        return self._spanner
