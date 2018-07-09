import abjad


class Expression(abjad.Expression):
    """
    Expression.

    ..  container:: example expression

        Transposes collections:

        >>> collections = [
        ...     abjad.PitchClassSegment([0, 1, 2, 3]),
        ...     abjad.PitchClassSegment([6, 7, 8, 9]),
        ...     ]

        >>> transposition = baca.Expression()
        >>> transposition = transposition.pitch_class_segment()
        >>> transposition = transposition.transpose(n=3)
        >>> expression = baca.sequence(name='J')
        >>> expression = expression.map(transposition)

        >>> for collection in expression(collections):
        ...     collection
        ...
        PitchClassSegment([3, 4, 5, 6])
        PitchClassSegment([9, 10, 11, 0])

        >>> expression.get_string()
        'T3(X) /@ J'

        >>> markup = expression.get_markup()
        >>> abjad.show(markup, strict=89) # doctest: +SKIP

        ..  docs::

            >>> abjad.f(markup, strict=89)
            \markup {
                \line
                    {
                        \concat
                            {
                                T
                                \sub
                                    3
                                \bold
                                    X
                            }
                        /@
                        \bold
                            J
                    }
                }

    ..  container:: example expression

        Transposes and joins:

        >>> collections = [
        ...     abjad.PitchClassSegment([0, 1, 2, 3]),
        ...     abjad.PitchClassSegment([6, 7, 8, 9]),
        ...     ]

        >>> transposition = baca.Expression()
        >>> transposition = transposition.pitch_class_segment()
        >>> transposition = transposition.transpose(n=3)
        >>> expression = baca.sequence(name='J')
        >>> expression = expression.map(transposition)
        >>> expression = expression.join()

        >>> expression(collections)
        Sequence([PitchClassSegment([3, 4, 5, 6, 9, 10, 11, 0])])

        >>> expression.get_string()
        'join(T3(X) /@ J)'

        >>> markup = expression.get_markup()
        >>> abjad.show(markup, strict=89) # doctest: +SKIP

        ..  docs::

            >>> abjad.f(markup, strict=89)
            \markup {
                \concat
                    {
                        join(
                        \line
                            {
                                \concat
                                    {
                                        T
                                        \sub
                                            3
                                        \bold
                                            X
                                    }
                                /@
                                \bold
                                    J
                            }
                        )
                    }
                }

    ..  container:: example expression

        Transposes and flattens:

        >>> collections = [
        ...     abjad.PitchClassSegment([0, 1, 2, 3]),
        ...     abjad.PitchClassSegment([6, 7, 8, 9]),
        ...     ]

        >>> transposition = baca.Expression()
        >>> transposition = transposition.pitch_class_segment()
        >>> transposition = transposition.transpose(n=3)
        >>> expression = baca.sequence(name='J')
        >>> expression = expression.map(transposition)
        >>> expression = expression.flatten(depth=-1)

        >>> for collection in expression(collections):
        ...     collection
        ...
        NumberedPitchClass(3)
        NumberedPitchClass(4)
        NumberedPitchClass(5)
        NumberedPitchClass(6)
        NumberedPitchClass(9)
        NumberedPitchClass(10)
        NumberedPitchClass(11)
        NumberedPitchClass(0)

        >>> expression.get_string()
        'flatten(T3(X) /@ J, depth=-1)'

        >>> markup = expression.get_markup()
        >>> abjad.show(markup, strict=89) # doctest: +SKIP

        ..  docs::

            >>> abjad.f(markup, strict=89)
            \markup {
                \concat
                    {
                        flatten(
                        \line
                            {
                                \concat
                                    {
                                        T
                                        \sub
                                            3
                                        \bold
                                            X
                                    }
                                /@
                                \bold
                                    J
                            }
                        ", depth=-1)"
                    }
                }

    ..  container:: example expression

        Transposes and repartitions:

        >>> collections = [
        ...     abjad.PitchClassSegment([0, 1, 2, 3]),
        ...     abjad.PitchClassSegment([6, 7, 8, 9]),
        ...     ]

        >>> transposition = baca.pitch_class_segment().transpose(n=3)
        >>> expression = baca.sequence(name='J').map(transposition)
        >>> expression = expression.flatten(depth=-1).partition([3])
        >>> expression = expression.pitch_class_segments()

        >>> for collection in expression(collections):
        ...     collection
        ...
        PitchClassSegment([3, 4, 5])
        PitchClassSegment([6, 9, 10])
        PitchClassSegment([11, 0])

        >>> expression.get_string()
        'X /@ P[3](flatten(T3(X) /@ J, depth=-1))'

        >>> markup = expression.get_markup()
        >>> abjad.show(markup, strict=89) # doctest: +SKIP

        ..  docs::

            >>> abjad.f(markup, strict=89)
            \markup {
                \line
                    {
                        \bold
                            X
                        /@
                        \concat
                            {
                                P
                                \sub
                                    [3]
                                \concat
                                    {
                                        flatten(
                                        \line
                                            {
                                                \concat
                                                    {
                                                        T
                                                        \sub
                                                            3
                                                        \bold
                                                            X
                                                    }
                                                /@
                                                \bold
                                                    J
                                            }
                                        ", depth=-1)"
                                    }
                            }
                    }
                }

    ..  container:: example expression

        Transposes, repartitions and ox-plows:

        >>> collections = [
        ...     abjad.PitchClassSegment([0, 1, 2, 3]),
        ...     abjad.PitchClassSegment([6, 7, 8, 9]),
        ...     ]

        >>> transposition = baca.pitch_class_segment().transpose(n=3)
        >>> expression = baca.sequence(name='J').map(transposition)
        >>> expression = expression.flatten(depth=-1).partition([3])
        >>> expression = expression.pitch_class_segments()
        >>> expression = expression.boustrophedon()

        >>> for collection in expression(collections):
        ...     collection
        ...
        PitchClassSegment([3, 4, 5])
        PitchClassSegment([6, 9, 10])
        PitchClassSegment([11, 0])
        PitchClassSegment([11])
        PitchClassSegment([10, 9, 6])
        PitchClassSegment([5, 4, 3])

        >>> expression.get_string()
        'β2(X /@ P[3](flatten(T3(X) /@ J, depth=-1)))'

        >>> markup = expression.get_markup()
        >>> abjad.show(markup, strict=89) # doctest: +SKIP

        ..  docs::

            >>> abjad.f(markup, strict=89)
            \markup {
                \concat
                    {
                        β
                        \super
                            2
                        \line
                            {
                                \bold
                                    X
                                /@
                                \concat
                                    {
                                        P
                                        \sub
                                            [3]
                                        \concat
                                            {
                                                flatten(
                                                \line
                                                    {
                                                        \concat
                                                            {
                                                                T
                                                                \sub
                                                                    3
                                                                \bold
                                                                    X
                                                            }
                                                        /@
                                                        \bold
                                                            J
                                                    }
                                                ", depth=-1)"
                                            }
                                    }
                            }
                    }
                }
    """

    ### CLASS VARIABLES ###

    __documentation_section__ = None

    ### PRIVATE METHODS ###

    def _evaluate_accumulate(self, *arguments):
        import baca
        assert len(arguments) == 1, repr(arguments)
        globals_ = self._make_globals()
        assert '__argument_0' not in globals_
        __argument_0 = arguments[0]
        assert isinstance(__argument_0, baca.Sequence), repr(__argument_0)
        class_ = type(__argument_0)
        operands = self.map_operand
        globals_['__argument_0'] = __argument_0
        globals_['class_'] = class_
        globals_['operands'] = operands
        statement = '__argument_0.accumulate(operands=operands)'
        try:
            result = eval(statement, globals_)
        except (NameError, SyntaxError, TypeError) as e:
            raise Exception(f'{statement!r} raises {e!r}.')
        return result

    ### PUBLIC METHODS ###

    def pitch_class_segment(self, **keywords):
        r"""Makes pitch-class segment subclass expression.

        ..  container:: example

            Makes expression to apply alpha transform to pitch-class segment:

            >>> baca.PitchClassSegment([-2, -1.5, 6, 7, -1.5, 7])
            PitchClassSegment([10, 10.5, 6, 7, 10.5, 7])

            >>> segment = baca.PitchClassSegment([-2, -1.5, 6, 7, -1.5, 7])
            >>> abjad.show(segment, strict=89) # doctest: +SKIP

            ..  container:: example expression

                >>> expression = baca.Expression(name='J')
                >>> expression = expression.pitch_class_segment()
                >>> expression = expression.alpha()

                >>> expression([-2, -1.5, 6, 7, -1.5, 7])
                PitchClassSegment([11, 11.5, 7, 6, 11.5, 6])

                >>> segment = expression([-2, -1.5, 6, 7, -1.5, 7])
                >>> markup = expression.get_markup()
                >>> abjad.show(segment, figure_name=markup) # doctest: +SKIP

                ..  docs::

                    >>> lilypond_file = segment.__illustrate__(
                    ...     figure_name=markup,
                    ...     )
                    >>> abjad.f(lilypond_file[abjad.Staff])
                    \new Staff
                    {
                        \new Voice
                        {
                            b'8
                            ^ \markup {
                                \concat
                                    {
                                        A
                                        \bold
                                            J
                                    }
                                }
                            bqs'8
                            g'8
                            fs'8
                            bqs'8
                            fs'8
                            \bar "|." %! SCORE1
                            \override Score.BarLine.transparent = ##f
                        }
                    }

        Returns expression.
        """
        import baca
        class_ = baca.PitchClassSegment
        callback = self._make_initializer_callback(
            class_,
            module_names=['baca'],
            string_template='{}',
            **keywords
            )
        expression = self.append_callback(callback)
        return abjad.new(expression, proxy_class=class_)

    def pitch_class_segments(self):
        """
        Maps pitch-class segment subclass initializer to expression.
        """
        initializer = Expression().pitch_class_segment()
        return self.map(initializer)

    def select(self, **keywords):
        r"""Makes select expression.

        ..  container:: example

            Makes expression to select leaves:

            ..  container:: example

                >>> staff = abjad.Staff()
                >>> staff.append(abjad.Measure((2, 8), "<c' bf'>8 <g' a'>8"))
                >>> staff.append(abjad.Measure((2, 8), "af'8 r8"))
                >>> staff.append(abjad.Measure((2, 8), "r8 gf'8"))
                >>> abjad.show(staff, strict=89) # doctest: +SKIP

                ..  docs::

                    >>> abjad.f(staff, strict=89)
                    \new Staff
                    {
                        {   % measure
                            \time 2/8
                            <c' bf'>8
                            <g' a'>8
                        }   % measure
                        {   % measure
                            af'8
                            r8
                        }   % measure
                        {   % measure
                            r8
                            gf'8
                        }   % measure
                    }

            ..  container:: example expression

                >>> expression = baca.Expression()
                >>> expression = expression.select()
                >>> expression = expression.leaves()

                >>> for leaf in expression(staff):
                ...     leaf
                ...
                Chord("<c' bf'>8")
                Chord("<g' a'>8")
                Note("af'8")
                Rest('r8')
                Rest('r8')
                Note("gf'8")

        Returns expression.
        """
        import baca
        class_ = baca.Selection
        callback = self._make_initializer_callback(
            class_,
            module_names=['baca'],
            **keywords
            )
        expression = self.append_callback(callback)
        return abjad.new(
            expression,
            proxy_class=class_,
            template='baca',
            )
