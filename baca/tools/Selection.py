import abjad
import baca
import inspect


class Selection(abjad.Selection):
    r'''Selection.

    ..  container:: example

        >>> baca.select()
        baca

    '''

    ### CLASS VARIABLES ###

    __documentation_section__ = '(5) Utilities'

    __slots__ = (
        )

    ### PUBLIC METHODS ###

    def chead(self, n):
        r'''Selects chord head `n`.

        ..  container:: example

            Selects chord head -1:

            ..  container:: example

                >>> tuplets = [
                ...     "r16 bf'16 <a'' b''>16 c'16 <d' e'>4 ~ <d' e'>16",
                ...     "r16 bf'16 <a'' b''>16 d'16 <e' fs'>4 ~ <e' fs'>16",
                ...     "r16 bf'16 <a'' b''>16 e'16 <fs' gs'>4 ~ <fs' gs'>16",
                ...     ]
                >>> tuplets = zip([(10, 9), (8, 9), (10, 9)], tuplets)
                >>> tuplets = [abjad.Tuplet(*_) for _ in tuplets]
                >>> tuplets = [abjad.select(tuplets)]
                >>> lilypond_file = abjad.LilyPondFile.rhythm(tuplets)
                >>> staff = lilypond_file[abjad.Staff]
                >>> abjad.override(staff).tuplet_bracket.direction = abjad.Up
                >>> abjad.override(staff).tuplet_bracket.staff_padding = 3
                >>> abjad.show(lilypond_file) # doctest: +SKIP

                >>> result = baca.select(staff).chead(-1)

                >>> result
                Chord("<fs' gs'>4")

            ..  container:: example expression

                >>> selector = baca.chead(-1)
                >>> result = selector(staff)

                >>> selector.print(result)
                Chord("<fs' gs'>4")

                >>> selector.color(result)
                >>> abjad.show(lilypond_file) # doctest: +SKIP

            ..  docs::

                >>> abjad.f(staff)
                \new Staff \with {
                    \override TupletBracket.direction = #up
                    \override TupletBracket.staff-padding = #3
                } {
                    {
                        \time 7/4
                        \tweak text #tuplet-number::calc-fraction-text
                        \times 10/9 {
                            r16
                            bf'16
                            <a'' b''>16
                            c'16
                            <d' e'>4 ~
                            <d' e'>16
                        }
                        \times 8/9 {
                            r16
                            bf'16
                            <a'' b''>16
                            d'16
                            <e' fs'>4 ~
                            <e' fs'>16
                        }
                        \tweak text #tuplet-number::calc-fraction-text
                        \times 10/9 {
                            r16
                            bf'16
                            <a'' b''>16
                            e'16
                            \once \override Accidental.color = #green
                            \once \override Beam.color = #green
                            \once \override Dots.color = #green
                            \once \override NoteHead.color = #green
                            \once \override Stem.color = #green
                            <fs' gs'>4 ~
                            <fs' gs'>16
                        }
                    }
                }

        '''
        if self._expression:
            return self._update_expression(inspect.currentframe(), lone=True)
        return self.cheads()[n]

    def cheads(self):
        r'''Selects chord heads.

        ..  container:: example

            Selects chord heads:

            ..  container:: example

                >>> tuplets = [
                ...     "r16 bf'16 <a'' b''>16 c'16 <d' e'>4 ~ <d' e'>16",
                ...     "r16 bf'16 <a'' b''>16 d'16 <e' fs'>4 ~ <e' fs'>16",
                ...     "r16 bf'16 <a'' b''>16 e'16 <fs' gs'>4 ~ <fs' gs'>16",
                ...     ]
                >>> tuplets = zip([(10, 9), (8, 9), (10, 9)], tuplets)
                >>> tuplets = [abjad.Tuplet(*_) for _ in tuplets]
                >>> tuplets = [abjad.select(tuplets)]
                >>> lilypond_file = abjad.LilyPondFile.rhythm(tuplets)
                >>> staff = lilypond_file[abjad.Staff]
                >>> abjad.override(staff).tuplet_bracket.direction = abjad.Up
                >>> abjad.override(staff).tuplet_bracket.staff_padding = 3
                >>> abjad.show(lilypond_file) # doctest: +SKIP

                >>> result = baca.select(staff).cheads()

                >>> for item in result:
                ...     item
                ...
                Chord("<a'' b''>16")
                Chord("<d' e'>4")
                Chord("<a'' b''>16")
                Chord("<e' fs'>4")
                Chord("<a'' b''>16")
                Chord("<fs' gs'>4")

            ..  container:: example expression

                >>> selector = baca.cheads()
                >>> result = selector(staff)

                >>> selector.print(result)
                Chord("<a'' b''>16")
                Chord("<d' e'>4")
                Chord("<a'' b''>16")
                Chord("<e' fs'>4")
                Chord("<a'' b''>16")
                Chord("<fs' gs'>4")

                >>> selector.color(result)
                >>> abjad.show(lilypond_file) # doctest: +SKIP

            ..  docs::

                >>> abjad.f(staff)
                \new Staff \with {
                    \override TupletBracket.direction = #up
                    \override TupletBracket.staff-padding = #3
                } {
                    {
                        \time 7/4
                        \tweak text #tuplet-number::calc-fraction-text
                        \times 10/9 {
                            r16
                            bf'16
                            \once \override Accidental.color = #red
                            \once \override Beam.color = #red
                            \once \override Dots.color = #red
                            \once \override NoteHead.color = #red
                            \once \override Stem.color = #red
                            <a'' b''>16
                            c'16
                            \once \override Accidental.color = #blue
                            \once \override Beam.color = #blue
                            \once \override Dots.color = #blue
                            \once \override NoteHead.color = #blue
                            \once \override Stem.color = #blue
                            <d' e'>4 ~
                            <d' e'>16
                        }
                        \times 8/9 {
                            r16
                            bf'16
                            \once \override Accidental.color = #red
                            \once \override Beam.color = #red
                            \once \override Dots.color = #red
                            \once \override NoteHead.color = #red
                            \once \override Stem.color = #red
                            <a'' b''>16
                            d'16
                            \once \override Accidental.color = #blue
                            \once \override Beam.color = #blue
                            \once \override Dots.color = #blue
                            \once \override NoteHead.color = #blue
                            \once \override Stem.color = #blue
                            <e' fs'>4 ~
                            <e' fs'>16
                        }
                        \tweak text #tuplet-number::calc-fraction-text
                        \times 10/9 {
                            r16
                            bf'16
                            \once \override Accidental.color = #red
                            \once \override Beam.color = #red
                            \once \override Dots.color = #red
                            \once \override NoteHead.color = #red
                            \once \override Stem.color = #red
                            <a'' b''>16
                            e'16
                            \once \override Accidental.color = #blue
                            \once \override Beam.color = #blue
                            \once \override Dots.color = #blue
                            \once \override NoteHead.color = #blue
                            \once \override Stem.color = #blue
                            <fs' gs'>4 ~
                            <fs' gs'>16
                        }
                    }
                }

        '''
        if self._expression:
            return self._update_expression(inspect.currentframe())
        return super(Selection, self).leaves(
            abjad.Chord,
            head=True,
            grace_notes=False,
            )

    def enchain(self, counts):
        r'''Enchains selection.

        Returns new selection.
        '''
        if self._expression:
            return self._update_expression(inspect.currentframe())
        return self.partition_by_counts(
            counts=counts,
            cyclic=True,
            enchain=True,
            overhang=True,
            )

    def group(self):
        r'''Groups selection.

        Returns new selection (or expression).
        '''
        if self._expression:
            return self._update_expression(inspect.currentframe(), lone=True)
        return self.group_by()

    def lleak(self):
        r'''Leaks to the left.

        Returns new selection.
        '''
        if self._expression:
            return self._update_expression(inspect.currentframe())
        return self.with_previous_leaf()

    def lleaves(self):
        r'''Selects leaves, leaked to the left.

        ..  container:: example

            Selects leaves (leaked to the left) in tuplet 1:

            ..  container:: example

                >>> tuplets = [
                ...     "r16 bf'16 <a'' b''>16 c'16 <d' e'>4 ~ <d' e'>16",
                ...     "r16 bf'16 <a'' b''>16 d'16 <e' fs'>4 ~ <e' fs'>16",
                ...     "r16 bf'16 <a'' b''>16 e'16 <fs' gs'>4 ~ <fs' gs'>16",
                ...     ]
                >>> tuplets = zip([(10, 9), (8, 9), (10, 9)], tuplets)
                >>> tuplets = [abjad.Tuplet(*_) for _ in tuplets]
                >>> tuplets = [abjad.select(tuplets)]
                >>> lilypond_file = abjad.LilyPondFile.rhythm(tuplets)
                >>> staff = lilypond_file[abjad.Staff]
                >>> abjad.override(staff).tuplet_bracket.direction = abjad.Up
                >>> abjad.override(staff).tuplet_bracket.staff_padding = 3
                >>> abjad.show(lilypond_file) # doctest: +SKIP

                >>> result = baca.select(staff).tuplets()[1:2].lleaves()

                >>> for item in result:
                ...     item
                ...
                Chord("<d' e'>16")
                Rest('r16')
                Note("bf'16")
                Chord("<a'' b''>16")
                Note("d'16")
                Chord("<e' fs'>4")
                Chord("<e' fs'>16")

            ..  container:: example expression

                >>> selector = baca.tuplets()[1:2].lleaves()
                >>> result = selector(staff)

                >>> selector.print(result)
                Chord("<d' e'>16")
                Rest('r16')
                Note("bf'16")
                Chord("<a'' b''>16")
                Note("d'16")
                Chord("<e' fs'>4")
                Chord("<e' fs'>16")

                >>> selector.color(result)
                >>> abjad.show(lilypond_file) # doctest: +SKIP

            ..  docs::

                >>> abjad.f(staff)
                \new Staff \with {
                    \override TupletBracket.direction = #up
                    \override TupletBracket.staff-padding = #3
                } {
                    {
                        \time 7/4
                        \tweak text #tuplet-number::calc-fraction-text
                        \times 10/9 {
                            r16
                            bf'16
                            <a'' b''>16
                            c'16
                            <d' e'>4 ~
                            \once \override Accidental.color = #red
                            \once \override Beam.color = #red
                            \once \override Dots.color = #red
                            \once \override NoteHead.color = #red
                            \once \override Stem.color = #red
                            <d' e'>16
                        }
                        \times 8/9 {
                            \once \override Dots.color = #blue
                            \once \override Rest.color = #blue
                            r16
                            \once \override Accidental.color = #red
                            \once \override Beam.color = #red
                            \once \override Dots.color = #red
                            \once \override NoteHead.color = #red
                            \once \override Stem.color = #red
                            bf'16
                            \once \override Accidental.color = #blue
                            \once \override Beam.color = #blue
                            \once \override Dots.color = #blue
                            \once \override NoteHead.color = #blue
                            \once \override Stem.color = #blue
                            <a'' b''>16
                            \once \override Accidental.color = #red
                            \once \override Beam.color = #red
                            \once \override Dots.color = #red
                            \once \override NoteHead.color = #red
                            \once \override Stem.color = #red
                            d'16
                            \once \override Accidental.color = #blue
                            \once \override Beam.color = #blue
                            \once \override Dots.color = #blue
                            \once \override NoteHead.color = #blue
                            \once \override Stem.color = #blue
                            <e' fs'>4 ~
                            \once \override Accidental.color = #red
                            \once \override Beam.color = #red
                            \once \override Dots.color = #red
                            \once \override NoteHead.color = #red
                            \once \override Stem.color = #red
                            <e' fs'>16
                        }
                        \tweak text #tuplet-number::calc-fraction-text
                        \times 10/9 {
                            r16
                            bf'16
                            <a'' b''>16
                            e'16
                            <fs' gs'>4 ~
                            <fs' gs'>16
                        }
                    }
                }

        '''
        if self._expression:
            return self._update_expression(inspect.currentframe())
        return self.leaves().with_previous_leaf()

    def lm(self, n):
        r'''Selects logical measure `n`.

        '''
        if self._expression:
            return self._update_expression(inspect.currentframe())
        return self.group_by_measure()[n]

    def lt(self, n):
        r'''Selects logical tie `n`.

        ..  container:: example

            Selects logical tie -1:

            ..  container:: example

                >>> tuplets = [
                ...     "r16 bf'16 <a'' b''>16 c'16 <d' e'>4 ~ <d' e'>16",
                ...     "r16 bf'16 <a'' b''>16 d'16 <e' fs'>4 ~ <e' fs'>16",
                ...     "r16 bf'16 <a'' b''>16 e'16 <fs' gs'>4 ~ <fs' gs'>16",
                ...     ]
                >>> tuplets = zip([(10, 9), (8, 9), (10, 9)], tuplets)
                >>> tuplets = [abjad.Tuplet(*_) for _ in tuplets]
                >>> tuplets = [abjad.select(tuplets)]
                >>> lilypond_file = abjad.LilyPondFile.rhythm(tuplets)
                >>> staff = lilypond_file[abjad.Staff]
                >>> abjad.override(staff).tuplet_bracket.direction = abjad.Up
                >>> abjad.override(staff).tuplet_bracket.staff_padding = 3
                >>> abjad.show(lilypond_file) # doctest: +SKIP

                >>> result = baca.select(staff).lt(-1)

                >>> result
                LogicalTie([Chord("<fs' gs'>4"), Chord("<fs' gs'>16")])

            ..  container:: example expression

                >>> selector = baca.lt(-1)
                >>> result = selector(staff)

                >>> selector.print(result)
                LogicalTie([Chord("<fs' gs'>4"), Chord("<fs' gs'>16")])

                >>> selector.color(result)
                >>> abjad.show(lilypond_file) # doctest: +SKIP

            ..  docs::

                >>> abjad.f(staff)
                \new Staff \with {
                    \override TupletBracket.direction = #up
                    \override TupletBracket.staff-padding = #3
                } {
                    {
                        \time 7/4
                        \tweak text #tuplet-number::calc-fraction-text
                        \times 10/9 {
                            r16
                            bf'16
                            <a'' b''>16
                            c'16
                            <d' e'>4 ~
                            <d' e'>16
                        }
                        \times 8/9 {
                            r16
                            bf'16
                            <a'' b''>16
                            d'16
                            <e' fs'>4 ~
                            <e' fs'>16
                        }
                        \tweak text #tuplet-number::calc-fraction-text
                        \times 10/9 {
                            r16
                            bf'16
                            <a'' b''>16
                            e'16
                            \once \override Accidental.color = #green
                            \once \override Beam.color = #green
                            \once \override Dots.color = #green
                            \once \override NoteHead.color = #green
                            \once \override Stem.color = #green
                            <fs' gs'>4 ~
                            \once \override Accidental.color = #green
                            \once \override Beam.color = #green
                            \once \override Dots.color = #green
                            \once \override NoteHead.color = #green
                            \once \override Stem.color = #green
                            <fs' gs'>16
                        }
                    }
                }

        '''
        if self._expression:
            return self._update_expression(inspect.currentframe(), lone=True)
        return self.lts()[n]

    def ltqrun(self, n):
        r'''Selects logical tie equipitch run `n`.

        ..  container:: example

            Selects logical tie equipitch run -1:

            ..  container:: example

                >>> tuplets = [
                ...     "r16 c'16 c'16 c'16 <d' e'>4 ~ <d' e'>16",
                ...     "r16 d'16 d'16 d'16 <e' fs'>4 ~ <e' fs'>16",
                ...     "r16 e'16 e'16 e'16 <fs' gs'>4 ~ <fs' gs'>16",
                ...     ]
                >>> tuplets = zip([(10, 9), (8, 9), (10, 9)], tuplets)
                >>> tuplets = [abjad.Tuplet(*_) for _ in tuplets]
                >>> tuplets = [abjad.select(tuplets)]
                >>> lilypond_file = abjad.LilyPondFile.rhythm(tuplets)
                >>> staff = lilypond_file[abjad.Staff]
                >>> abjad.override(staff).tuplet_bracket.direction = abjad.Up
                >>> abjad.override(staff).tuplet_bracket.staff_padding = 3
                >>> abjad.show(lilypond_file) # doctest: +SKIP

                >>> result = baca.select(staff).ltqrun(-1)

                >>> result
                Run([LogicalTie([Chord("<fs' gs'>4"), Chord("<fs' gs'>16")])])

            ..  container:: example expression

                >>> selector = baca.ltqrun(-1)
                >>> result = selector(staff)

                >>> selector.print(result)
                Run([LogicalTie([Chord("<fs' gs'>4"), Chord("<fs' gs'>16")])])

                >>> selector.color(result)
                >>> abjad.show(lilypond_file) # doctest: +SKIP

            ..  docs::

                >>> abjad.f(staff)
                \new Staff \with {
                    \override TupletBracket.direction = #up
                    \override TupletBracket.staff-padding = #3
                } {
                    {
                        \time 7/4
                        \tweak text #tuplet-number::calc-fraction-text
                        \times 10/9 {
                            r16
                            c'16
                            c'16
                            c'16
                            <d' e'>4 ~
                            <d' e'>16
                        }
                        \times 8/9 {
                            r16
                            d'16
                            d'16
                            d'16
                            <e' fs'>4 ~
                            <e' fs'>16
                        }
                        \tweak text #tuplet-number::calc-fraction-text
                        \times 10/9 {
                            r16
                            e'16
                            e'16
                            e'16
                            \once \override Accidental.color = #green
                            \once \override Beam.color = #green
                            \once \override Dots.color = #green
                            \once \override NoteHead.color = #green
                            \once \override Stem.color = #green
                            <fs' gs'>4 ~
                            \once \override Accidental.color = #green
                            \once \override Beam.color = #green
                            \once \override Dots.color = #green
                            \once \override NoteHead.color = #green
                            \once \override Stem.color = #green
                            <fs' gs'>16
                        }
                    }
                }

        '''
        if self._expression:
            return self._update_expression(inspect.currentframe(), lone=True)
        return self.ltqruns()[n]

    def ltqruns(self):
        r'''Selects logical tie equipitch runs.

        ..  container:: example

            Selects logical tie equipitch runs:

            ..  container:: example

                >>> tuplets = [
                ...     "r16 c'16 c'16 c'16 <d' e'>4 ~ <d' e'>16",
                ...     "r16 d'16 d'16 d'16 <e' fs'>4 ~ <e' fs'>16",
                ...     "r16 e'16 e'16 e'16 <fs' gs'>4 ~ <fs' gs'>16",
                ...     ]
                >>> tuplets = zip([(10, 9), (8, 9), (10, 9)], tuplets)
                >>> tuplets = [abjad.Tuplet(*_) for _ in tuplets]
                >>> tuplets = [abjad.select(tuplets)]
                >>> lilypond_file = abjad.LilyPondFile.rhythm(tuplets)
                >>> staff = lilypond_file[abjad.Staff]
                >>> abjad.override(staff).tuplet_bracket.direction = abjad.Up
                >>> abjad.override(staff).tuplet_bracket.staff_padding = 3
                >>> abjad.show(lilypond_file) # doctest: +SKIP

                >>> result = baca.select(staff).ltqruns()

                >>> for item in result:
                ...     item
                ...
                Run([LogicalTie([Note("c'16")]), LogicalTie([Note("c'16")]), LogicalTie([Note("c'16")])])
                Run([LogicalTie([Chord("<d' e'>4"), Chord("<d' e'>16")])])
                Run([LogicalTie([Note("d'16")]), LogicalTie([Note("d'16")]), LogicalTie([Note("d'16")])])
                Run([LogicalTie([Chord("<e' fs'>4"), Chord("<e' fs'>16")])])
                Run([LogicalTie([Note("e'16")]), LogicalTie([Note("e'16")]), LogicalTie([Note("e'16")])])
                Run([LogicalTie([Chord("<fs' gs'>4"), Chord("<fs' gs'>16")])])

            ..  container:: example expression

                >>> selector = baca.ltqruns()
                >>> result = selector(staff)

                >>> selector.print(result)
                Run([LogicalTie([Note("c'16")]), LogicalTie([Note("c'16")]), LogicalTie([Note("c'16")])])
                Run([LogicalTie([Chord("<d' e'>4"), Chord("<d' e'>16")])])
                Run([LogicalTie([Note("d'16")]), LogicalTie([Note("d'16")]), LogicalTie([Note("d'16")])])
                Run([LogicalTie([Chord("<e' fs'>4"), Chord("<e' fs'>16")])])
                Run([LogicalTie([Note("e'16")]), LogicalTie([Note("e'16")]), LogicalTie([Note("e'16")])])
                Run([LogicalTie([Chord("<fs' gs'>4"), Chord("<fs' gs'>16")])])

                >>> selector.color(result)
                >>> abjad.show(lilypond_file) # doctest: +SKIP

            ..  docs::

                >>> abjad.f(staff)
                \new Staff \with {
                    \override TupletBracket.direction = #up
                    \override TupletBracket.staff-padding = #3
                } {
                    {
                        \time 7/4
                        \tweak text #tuplet-number::calc-fraction-text
                        \times 10/9 {
                            r16
                            \once \override Accidental.color = #red
                            \once \override Beam.color = #red
                            \once \override Dots.color = #red
                            \once \override NoteHead.color = #red
                            \once \override Stem.color = #red
                            c'16
                            \once \override Accidental.color = #red
                            \once \override Beam.color = #red
                            \once \override Dots.color = #red
                            \once \override NoteHead.color = #red
                            \once \override Stem.color = #red
                            c'16
                            \once \override Accidental.color = #red
                            \once \override Beam.color = #red
                            \once \override Dots.color = #red
                            \once \override NoteHead.color = #red
                            \once \override Stem.color = #red
                            c'16
                            \once \override Accidental.color = #blue
                            \once \override Beam.color = #blue
                            \once \override Dots.color = #blue
                            \once \override NoteHead.color = #blue
                            \once \override Stem.color = #blue
                            <d' e'>4 ~
                            \once \override Accidental.color = #blue
                            \once \override Beam.color = #blue
                            \once \override Dots.color = #blue
                            \once \override NoteHead.color = #blue
                            \once \override Stem.color = #blue
                            <d' e'>16
                        }
                        \times 8/9 {
                            r16
                            \once \override Accidental.color = #red
                            \once \override Beam.color = #red
                            \once \override Dots.color = #red
                            \once \override NoteHead.color = #red
                            \once \override Stem.color = #red
                            d'16
                            \once \override Accidental.color = #red
                            \once \override Beam.color = #red
                            \once \override Dots.color = #red
                            \once \override NoteHead.color = #red
                            \once \override Stem.color = #red
                            d'16
                            \once \override Accidental.color = #red
                            \once \override Beam.color = #red
                            \once \override Dots.color = #red
                            \once \override NoteHead.color = #red
                            \once \override Stem.color = #red
                            d'16
                            \once \override Accidental.color = #blue
                            \once \override Beam.color = #blue
                            \once \override Dots.color = #blue
                            \once \override NoteHead.color = #blue
                            \once \override Stem.color = #blue
                            <e' fs'>4 ~
                            \once \override Accidental.color = #blue
                            \once \override Beam.color = #blue
                            \once \override Dots.color = #blue
                            \once \override NoteHead.color = #blue
                            \once \override Stem.color = #blue
                            <e' fs'>16
                        }
                        \tweak text #tuplet-number::calc-fraction-text
                        \times 10/9 {
                            r16
                            \once \override Accidental.color = #red
                            \once \override Beam.color = #red
                            \once \override Dots.color = #red
                            \once \override NoteHead.color = #red
                            \once \override Stem.color = #red
                            e'16
                            \once \override Accidental.color = #red
                            \once \override Beam.color = #red
                            \once \override Dots.color = #red
                            \once \override NoteHead.color = #red
                            \once \override Stem.color = #red
                            e'16
                            \once \override Accidental.color = #red
                            \once \override Beam.color = #red
                            \once \override Dots.color = #red
                            \once \override NoteHead.color = #red
                            \once \override Stem.color = #red
                            e'16
                            \once \override Accidental.color = #blue
                            \once \override Beam.color = #blue
                            \once \override Dots.color = #blue
                            \once \override NoteHead.color = #blue
                            \once \override Stem.color = #blue
                            <fs' gs'>4 ~
                            \once \override Accidental.color = #blue
                            \once \override Beam.color = #blue
                            \once \override Dots.color = #blue
                            \once \override NoteHead.color = #blue
                            \once \override Stem.color = #blue
                            <fs' gs'>16
                        }
                    }
                }

        '''
        if self._expression:
            return self._update_expression(inspect.currentframe())
        result = self.plts()
        result = result.group_by_pitch()
        result = result.map(baca.group_by_contiguity())
        result = result.flatten(depth=1)
        result = result.map(abjad.Run)
        return result

    def ltrun(self, n):
        r'''Selects logical tie run `n`.

        ..  container:: example

            Selects logical tie run -1:

            ..  container:: example

                >>> tuplets = [
                ...     "r16 c'16 c'16 c'16 <d' e'>4 ~ <d' e'>16",
                ...     "r16 d'16 d'16 d'16 <e' fs'>4 ~ <e' fs'>16",
                ...     "r16 e'16 e'16 e'16 <fs' gs'>4 ~ <fs' gs'>16",
                ...     ]
                >>> tuplets = zip([(10, 9), (8, 9), (10, 9)], tuplets)
                >>> tuplets = [abjad.Tuplet(*_) for _ in tuplets]
                >>> tuplets = [abjad.select(tuplets)]
                >>> lilypond_file = abjad.LilyPondFile.rhythm(tuplets)
                >>> staff = lilypond_file[abjad.Staff]
                >>> abjad.override(staff).tuplet_bracket.direction = abjad.Up
                >>> abjad.override(staff).tuplet_bracket.staff_padding = 3
                >>> abjad.show(lilypond_file) # doctest: +SKIP

                >>> result = baca.select(staff).ltrun(-1)

                >>> result
                Run([LogicalTie([Note("e'16")]), LogicalTie([Note("e'16")]), LogicalTie([Note("e'16")]), LogicalTie([Chord("<fs' gs'>4"), Chord("<fs' gs'>16")])])

            ..  container:: example expression

                >>> selector = baca.ltrun(-1)
                >>> result = selector(staff)

                >>> selector.print(result)
                Run([LogicalTie([Note("e'16")]), LogicalTie([Note("e'16")]), LogicalTie([Note("e'16")]), LogicalTie([Chord("<fs' gs'>4"), Chord("<fs' gs'>16")])])

                >>> selector.color(result)
                >>> abjad.show(lilypond_file) # doctest: +SKIP

            ..  docs::

                >>> abjad.f(staff)
                \new Staff \with {
                    \override TupletBracket.direction = #up
                    \override TupletBracket.staff-padding = #3
                } {
                    {
                        \time 7/4
                        \tweak text #tuplet-number::calc-fraction-text
                        \times 10/9 {
                            r16
                            c'16
                            c'16
                            c'16
                            <d' e'>4 ~
                            <d' e'>16
                        }
                        \times 8/9 {
                            r16
                            d'16
                            d'16
                            d'16
                            <e' fs'>4 ~
                            <e' fs'>16
                        }
                        \tweak text #tuplet-number::calc-fraction-text
                        \times 10/9 {
                            r16
                            \once \override Accidental.color = #green
                            \once \override Beam.color = #green
                            \once \override Dots.color = #green
                            \once \override NoteHead.color = #green
                            \once \override Stem.color = #green
                            e'16
                            \once \override Accidental.color = #green
                            \once \override Beam.color = #green
                            \once \override Dots.color = #green
                            \once \override NoteHead.color = #green
                            \once \override Stem.color = #green
                            e'16
                            \once \override Accidental.color = #green
                            \once \override Beam.color = #green
                            \once \override Dots.color = #green
                            \once \override NoteHead.color = #green
                            \once \override Stem.color = #green
                            e'16
                            \once \override Accidental.color = #green
                            \once \override Beam.color = #green
                            \once \override Dots.color = #green
                            \once \override NoteHead.color = #green
                            \once \override Stem.color = #green
                            <fs' gs'>4 ~
                            \once \override Accidental.color = #green
                            \once \override Beam.color = #green
                            \once \override Dots.color = #green
                            \once \override NoteHead.color = #green
                            \once \override Stem.color = #green
                            <fs' gs'>16
                        }
                    }
                }

        '''
        if self._expression:
            return self._update_expression(inspect.currentframe(), lone=True)
        return self.ltruns()[n]

    def ltruns(self):
        r'''Selects logical tie runs.

        ..  container:: example

            Selects logical tie runs:

            ..  container:: example

                >>> tuplets = [
                ...     "r16 c'16 c'16 c'16 <d' e'>4 ~ <d' e'>16",
                ...     "r16 d'16 d'16 d'16 <e' fs'>4 ~ <e' fs'>16",
                ...     "r16 e'16 e'16 e'16 <fs' gs'>4 ~ <fs' gs'>16",
                ...     ]
                >>> tuplets = zip([(10, 9), (8, 9), (10, 9)], tuplets)
                >>> tuplets = [abjad.Tuplet(*_) for _ in tuplets]
                >>> tuplets = [abjad.select(tuplets)]
                >>> lilypond_file = abjad.LilyPondFile.rhythm(tuplets)
                >>> staff = lilypond_file[abjad.Staff]
                >>> abjad.override(staff).tuplet_bracket.direction = abjad.Up
                >>> abjad.override(staff).tuplet_bracket.staff_padding = 3
                >>> abjad.show(lilypond_file) # doctest: +SKIP

                >>> result = baca.select(staff).ltruns()

                >>> for item in result:
                ...     item
                ...
                Run([LogicalTie([Note("c'16")]), LogicalTie([Note("c'16")]), LogicalTie([Note("c'16")]), LogicalTie([Chord("<d' e'>4"), Chord("<d' e'>16")])])
                Run([LogicalTie([Note("d'16")]), LogicalTie([Note("d'16")]), LogicalTie([Note("d'16")]), LogicalTie([Chord("<e' fs'>4"), Chord("<e' fs'>16")])])
                Run([LogicalTie([Note("e'16")]), LogicalTie([Note("e'16")]), LogicalTie([Note("e'16")]), LogicalTie([Chord("<fs' gs'>4"), Chord("<fs' gs'>16")])])

            ..  container:: example expression

                >>> selector = baca.ltruns()
                >>> result = selector(staff)

                >>> selector.print(result)
                Run([LogicalTie([Note("c'16")]), LogicalTie([Note("c'16")]), LogicalTie([Note("c'16")]), LogicalTie([Chord("<d' e'>4"), Chord("<d' e'>16")])])
                Run([LogicalTie([Note("d'16")]), LogicalTie([Note("d'16")]), LogicalTie([Note("d'16")]), LogicalTie([Chord("<e' fs'>4"), Chord("<e' fs'>16")])])
                Run([LogicalTie([Note("e'16")]), LogicalTie([Note("e'16")]), LogicalTie([Note("e'16")]), LogicalTie([Chord("<fs' gs'>4"), Chord("<fs' gs'>16")])])

                >>> selector.color(result)
                >>> abjad.show(lilypond_file) # doctest: +SKIP

            ..  docs::

                >>> abjad.f(staff)
                \new Staff \with {
                    \override TupletBracket.direction = #up
                    \override TupletBracket.staff-padding = #3
                } {
                    {
                        \time 7/4
                        \tweak text #tuplet-number::calc-fraction-text
                        \times 10/9 {
                            r16
                            \once \override Accidental.color = #red
                            \once \override Beam.color = #red
                            \once \override Dots.color = #red
                            \once \override NoteHead.color = #red
                            \once \override Stem.color = #red
                            c'16
                            \once \override Accidental.color = #red
                            \once \override Beam.color = #red
                            \once \override Dots.color = #red
                            \once \override NoteHead.color = #red
                            \once \override Stem.color = #red
                            c'16
                            \once \override Accidental.color = #red
                            \once \override Beam.color = #red
                            \once \override Dots.color = #red
                            \once \override NoteHead.color = #red
                            \once \override Stem.color = #red
                            c'16
                            \once \override Accidental.color = #red
                            \once \override Beam.color = #red
                            \once \override Dots.color = #red
                            \once \override NoteHead.color = #red
                            \once \override Stem.color = #red
                            <d' e'>4 ~
                            \once \override Accidental.color = #red
                            \once \override Beam.color = #red
                            \once \override Dots.color = #red
                            \once \override NoteHead.color = #red
                            \once \override Stem.color = #red
                            <d' e'>16
                        }
                        \times 8/9 {
                            r16
                            \once \override Accidental.color = #blue
                            \once \override Beam.color = #blue
                            \once \override Dots.color = #blue
                            \once \override NoteHead.color = #blue
                            \once \override Stem.color = #blue
                            d'16
                            \once \override Accidental.color = #blue
                            \once \override Beam.color = #blue
                            \once \override Dots.color = #blue
                            \once \override NoteHead.color = #blue
                            \once \override Stem.color = #blue
                            d'16
                            \once \override Accidental.color = #blue
                            \once \override Beam.color = #blue
                            \once \override Dots.color = #blue
                            \once \override NoteHead.color = #blue
                            \once \override Stem.color = #blue
                            d'16
                            \once \override Accidental.color = #blue
                            \once \override Beam.color = #blue
                            \once \override Dots.color = #blue
                            \once \override NoteHead.color = #blue
                            \once \override Stem.color = #blue
                            <e' fs'>4 ~
                            \once \override Accidental.color = #blue
                            \once \override Beam.color = #blue
                            \once \override Dots.color = #blue
                            \once \override NoteHead.color = #blue
                            \once \override Stem.color = #blue
                            <e' fs'>16
                        }
                        \tweak text #tuplet-number::calc-fraction-text
                        \times 10/9 {
                            r16
                            \once \override Accidental.color = #red
                            \once \override Beam.color = #red
                            \once \override Dots.color = #red
                            \once \override NoteHead.color = #red
                            \once \override Stem.color = #red
                            e'16
                            \once \override Accidental.color = #red
                            \once \override Beam.color = #red
                            \once \override Dots.color = #red
                            \once \override NoteHead.color = #red
                            \once \override Stem.color = #red
                            e'16
                            \once \override Accidental.color = #red
                            \once \override Beam.color = #red
                            \once \override Dots.color = #red
                            \once \override NoteHead.color = #red
                            \once \override Stem.color = #red
                            e'16
                            \once \override Accidental.color = #red
                            \once \override Beam.color = #red
                            \once \override Dots.color = #red
                            \once \override NoteHead.color = #red
                            \once \override Stem.color = #red
                            <fs' gs'>4 ~
                            \once \override Accidental.color = #red
                            \once \override Beam.color = #red
                            \once \override Dots.color = #red
                            \once \override NoteHead.color = #red
                            \once \override Stem.color = #red
                            <fs' gs'>16
                        }
                    }
                }

        '''
        if self._expression:
            return self._update_expression(inspect.currentframe())
        result = self.logical_ties(pitched=True).group_by_contiguity()
        return result.map(abjad.Run)

    def lts(self):
        r'''Selects logical ties.

        ..  container:: example

            Selects logical ties:

            ..  container:: example

                >>> tuplets = [
                ...     "r16 bf'16 <a'' b''>16 c'16 <d' e'>4 ~ <d' e'>16",
                ...     "r16 bf'16 <a'' b''>16 d'16 <e' fs'>4 ~ <e' fs'>16",
                ...     "r16 bf'16 <a'' b''>16 e'16 <fs' gs'>4 ~ <fs' gs'>16",
                ...     ]
                >>> tuplets = zip([(10, 9), (8, 9), (10, 9)], tuplets)
                >>> tuplets = [abjad.Tuplet(*_) for _ in tuplets]
                >>> tuplets = [abjad.select(tuplets)]
                >>> lilypond_file = abjad.LilyPondFile.rhythm(tuplets)
                >>> staff = lilypond_file[abjad.Staff]
                >>> abjad.override(staff).tuplet_bracket.direction = abjad.Up
                >>> abjad.override(staff).tuplet_bracket.staff_padding = 3
                >>> abjad.show(lilypond_file) # doctest: +SKIP

                >>> result = baca.select(staff).lts()

                >>> for item in result:
                ...     item
                ...
                LogicalTie([Rest('r16')])
                LogicalTie([Note("bf'16")])
                LogicalTie([Chord("<a'' b''>16")])
                LogicalTie([Note("c'16")])
                LogicalTie([Chord("<d' e'>4"), Chord("<d' e'>16")])
                LogicalTie([Rest('r16')])
                LogicalTie([Note("bf'16")])
                LogicalTie([Chord("<a'' b''>16")])
                LogicalTie([Note("d'16")])
                LogicalTie([Chord("<e' fs'>4"), Chord("<e' fs'>16")])
                LogicalTie([Rest('r16')])
                LogicalTie([Note("bf'16")])
                LogicalTie([Chord("<a'' b''>16")])
                LogicalTie([Note("e'16")])
                LogicalTie([Chord("<fs' gs'>4"), Chord("<fs' gs'>16")])

            ..  container:: example expression

                >>> selector = baca.lts()
                >>> result = selector(staff)

                >>> selector.print(result)
                LogicalTie([Rest('r16')])
                LogicalTie([Note("bf'16")])
                LogicalTie([Chord("<a'' b''>16")])
                LogicalTie([Note("c'16")])
                LogicalTie([Chord("<d' e'>4"), Chord("<d' e'>16")])
                LogicalTie([Rest('r16')])
                LogicalTie([Note("bf'16")])
                LogicalTie([Chord("<a'' b''>16")])
                LogicalTie([Note("d'16")])
                LogicalTie([Chord("<e' fs'>4"), Chord("<e' fs'>16")])
                LogicalTie([Rest('r16')])
                LogicalTie([Note("bf'16")])
                LogicalTie([Chord("<a'' b''>16")])
                LogicalTie([Note("e'16")])
                LogicalTie([Chord("<fs' gs'>4"), Chord("<fs' gs'>16")])

                >>> selector.color(result)
                >>> abjad.show(lilypond_file) # doctest: +SKIP

            ..  docs::

                >>> abjad.f(staff)
                \new Staff \with {
                    \override TupletBracket.direction = #up
                    \override TupletBracket.staff-padding = #3
                } {
                    {
                        \time 7/4
                        \tweak text #tuplet-number::calc-fraction-text
                        \times 10/9 {
                            \once \override Dots.color = #red
                            \once \override Rest.color = #red
                            r16
                            \once \override Accidental.color = #blue
                            \once \override Beam.color = #blue
                            \once \override Dots.color = #blue
                            \once \override NoteHead.color = #blue
                            \once \override Stem.color = #blue
                            bf'16
                            \once \override Accidental.color = #red
                            \once \override Beam.color = #red
                            \once \override Dots.color = #red
                            \once \override NoteHead.color = #red
                            \once \override Stem.color = #red
                            <a'' b''>16
                            \once \override Accidental.color = #blue
                            \once \override Beam.color = #blue
                            \once \override Dots.color = #blue
                            \once \override NoteHead.color = #blue
                            \once \override Stem.color = #blue
                            c'16
                            \once \override Accidental.color = #red
                            \once \override Beam.color = #red
                            \once \override Dots.color = #red
                            \once \override NoteHead.color = #red
                            \once \override Stem.color = #red
                            <d' e'>4 ~
                            \once \override Accidental.color = #red
                            \once \override Beam.color = #red
                            \once \override Dots.color = #red
                            \once \override NoteHead.color = #red
                            \once \override Stem.color = #red
                            <d' e'>16
                        }
                        \times 8/9 {
                            \once \override Dots.color = #blue
                            \once \override Rest.color = #blue
                            r16
                            \once \override Accidental.color = #red
                            \once \override Beam.color = #red
                            \once \override Dots.color = #red
                            \once \override NoteHead.color = #red
                            \once \override Stem.color = #red
                            bf'16
                            \once \override Accidental.color = #blue
                            \once \override Beam.color = #blue
                            \once \override Dots.color = #blue
                            \once \override NoteHead.color = #blue
                            \once \override Stem.color = #blue
                            <a'' b''>16
                            \once \override Accidental.color = #red
                            \once \override Beam.color = #red
                            \once \override Dots.color = #red
                            \once \override NoteHead.color = #red
                            \once \override Stem.color = #red
                            d'16
                            \once \override Accidental.color = #blue
                            \once \override Beam.color = #blue
                            \once \override Dots.color = #blue
                            \once \override NoteHead.color = #blue
                            \once \override Stem.color = #blue
                            <e' fs'>4 ~
                            \once \override Accidental.color = #blue
                            \once \override Beam.color = #blue
                            \once \override Dots.color = #blue
                            \once \override NoteHead.color = #blue
                            \once \override Stem.color = #blue
                            <e' fs'>16
                        }
                        \tweak text #tuplet-number::calc-fraction-text
                        \times 10/9 {
                            \once \override Dots.color = #red
                            \once \override Rest.color = #red
                            r16
                            \once \override Accidental.color = #blue
                            \once \override Beam.color = #blue
                            \once \override Dots.color = #blue
                            \once \override NoteHead.color = #blue
                            \once \override Stem.color = #blue
                            bf'16
                            \once \override Accidental.color = #red
                            \once \override Beam.color = #red
                            \once \override Dots.color = #red
                            \once \override NoteHead.color = #red
                            \once \override Stem.color = #red
                            <a'' b''>16
                            \once \override Accidental.color = #blue
                            \once \override Beam.color = #blue
                            \once \override Dots.color = #blue
                            \once \override NoteHead.color = #blue
                            \once \override Stem.color = #blue
                            e'16
                            \once \override Accidental.color = #red
                            \once \override Beam.color = #red
                            \once \override Dots.color = #red
                            \once \override NoteHead.color = #red
                            \once \override Stem.color = #red
                            <fs' gs'>4 ~
                            \once \override Accidental.color = #red
                            \once \override Beam.color = #red
                            \once \override Dots.color = #red
                            \once \override NoteHead.color = #red
                            \once \override Stem.color = #red
                            <fs' gs'>16
                        }
                    }
                }

        '''
        if self._expression:
            return self._update_expression(inspect.currentframe())
        return self.logical_ties(grace_notes=None)

    def measure(self, n):
        r'''Selects measure `n`.
        '''
        if self._expression:
            return self._update_expression(inspect.currentframe())
        return self.measures()[n]

    def measures(self):
        r'''Selects measures.
        '''
        if self._expression:
            return self._update_expression(inspect.currentframe())
        return self.components(abjad.Measure)

    def ntruns(self):
        r'''Selects nontrivial runs.

        ..  container:: example

            Selects nontrivial runs:

            ..  container:: example

                >>> tuplets = [
                ...     "r16 c'16 c'16 c'16 <d' e'>4 ~ <d' e'>16",
                ...     "r16 d'16 d'16 d'16 <e' fs'>4 ~ <e' fs'>16",
                ...     "r16 e'16 e'16 e'16 <fs' gs'>4 ~ <fs' gs'>16",
                ...     ]
                >>> tuplets = zip([(10, 9), (8, 9), (10, 9)], tuplets)
                >>> tuplets = [abjad.Tuplet(*_) for _ in tuplets]
                >>> tuplets = [abjad.select(tuplets)]
                >>> lilypond_file = abjad.LilyPondFile.rhythm(tuplets)
                >>> staff = lilypond_file[abjad.Staff]
                >>> abjad.override(staff).tuplet_bracket.direction = abjad.Up
                >>> abjad.override(staff).tuplet_bracket.staff_padding = 3
                >>> abjad.show(lilypond_file) # doctest: +SKIP

                >>> result = baca.select(staff).ntruns()

                >>> for item in result:
                ...     item
                ...
                Run([Note("c'16"), Note("c'16"), Note("c'16"), Chord("<d' e'>4"), Chord("<d' e'>16")])
                Run([Note("d'16"), Note("d'16"), Note("d'16"), Chord("<e' fs'>4"), Chord("<e' fs'>16")])
                Run([Note("e'16"), Note("e'16"), Note("e'16"), Chord("<fs' gs'>4"), Chord("<fs' gs'>16")])

            ..  container:: example expression

                >>> selector = baca.ntruns()
                >>> result = selector(staff)

                >>> selector.print(result)
                Run([Note("c'16"), Note("c'16"), Note("c'16"), Chord("<d' e'>4"), Chord("<d' e'>16")])
                Run([Note("d'16"), Note("d'16"), Note("d'16"), Chord("<e' fs'>4"), Chord("<e' fs'>16")])
                Run([Note("e'16"), Note("e'16"), Note("e'16"), Chord("<fs' gs'>4"), Chord("<fs' gs'>16")])

                >>> selector.color(result)
                >>> abjad.show(lilypond_file) # doctest: +SKIP

            ..  docs::

                >>> abjad.f(staff)
                \new Staff \with {
                    \override TupletBracket.direction = #up
                    \override TupletBracket.staff-padding = #3
                } {
                    {
                        \time 7/4
                        \tweak text #tuplet-number::calc-fraction-text
                        \times 10/9 {
                            r16
                            \once \override Accidental.color = #red
                            \once \override Beam.color = #red
                            \once \override Dots.color = #red
                            \once \override NoteHead.color = #red
                            \once \override Stem.color = #red
                            c'16
                            \once \override Accidental.color = #red
                            \once \override Beam.color = #red
                            \once \override Dots.color = #red
                            \once \override NoteHead.color = #red
                            \once \override Stem.color = #red
                            c'16
                            \once \override Accidental.color = #red
                            \once \override Beam.color = #red
                            \once \override Dots.color = #red
                            \once \override NoteHead.color = #red
                            \once \override Stem.color = #red
                            c'16
                            \once \override Accidental.color = #red
                            \once \override Beam.color = #red
                            \once \override Dots.color = #red
                            \once \override NoteHead.color = #red
                            \once \override Stem.color = #red
                            <d' e'>4 ~
                            \once \override Accidental.color = #red
                            \once \override Beam.color = #red
                            \once \override Dots.color = #red
                            \once \override NoteHead.color = #red
                            \once \override Stem.color = #red
                            <d' e'>16
                        }
                        \times 8/9 {
                            r16
                            \once \override Accidental.color = #blue
                            \once \override Beam.color = #blue
                            \once \override Dots.color = #blue
                            \once \override NoteHead.color = #blue
                            \once \override Stem.color = #blue
                            d'16
                            \once \override Accidental.color = #blue
                            \once \override Beam.color = #blue
                            \once \override Dots.color = #blue
                            \once \override NoteHead.color = #blue
                            \once \override Stem.color = #blue
                            d'16
                            \once \override Accidental.color = #blue
                            \once \override Beam.color = #blue
                            \once \override Dots.color = #blue
                            \once \override NoteHead.color = #blue
                            \once \override Stem.color = #blue
                            d'16
                            \once \override Accidental.color = #blue
                            \once \override Beam.color = #blue
                            \once \override Dots.color = #blue
                            \once \override NoteHead.color = #blue
                            \once \override Stem.color = #blue
                            <e' fs'>4 ~
                            \once \override Accidental.color = #blue
                            \once \override Beam.color = #blue
                            \once \override Dots.color = #blue
                            \once \override NoteHead.color = #blue
                            \once \override Stem.color = #blue
                            <e' fs'>16
                        }
                        \tweak text #tuplet-number::calc-fraction-text
                        \times 10/9 {
                            r16
                            \once \override Accidental.color = #red
                            \once \override Beam.color = #red
                            \once \override Dots.color = #red
                            \once \override NoteHead.color = #red
                            \once \override Stem.color = #red
                            e'16
                            \once \override Accidental.color = #red
                            \once \override Beam.color = #red
                            \once \override Dots.color = #red
                            \once \override NoteHead.color = #red
                            \once \override Stem.color = #red
                            e'16
                            \once \override Accidental.color = #red
                            \once \override Beam.color = #red
                            \once \override Dots.color = #red
                            \once \override NoteHead.color = #red
                            \once \override Stem.color = #red
                            e'16
                            \once \override Accidental.color = #red
                            \once \override Beam.color = #red
                            \once \override Dots.color = #red
                            \once \override NoteHead.color = #red
                            \once \override Stem.color = #red
                            <fs' gs'>4 ~
                            \once \override Accidental.color = #red
                            \once \override Beam.color = #red
                            \once \override Dots.color = #red
                            \once \override NoteHead.color = #red
                            \once \override Stem.color = #red
                            <fs' gs'>16
                        }
                    }
                }

        '''
        if self._expression:
            return self._update_expression(inspect.currentframe())
        return self.runs().nontrivial()

    def phead(self, n):
        r'''Selects pitched head `n`.

        ..  container:: example

            Selects pitched head -1:

            ..  container:: example

                >>> tuplets = [
                ...     "r16 bf'16 <a'' b''>16 c'16 <d' e'>4 ~ <d' e'>16",
                ...     "r16 bf'16 <a'' b''>16 d'16 <e' fs'>4 ~ <e' fs'>16",
                ...     "r16 bf'16 <a'' b''>16 e'16 <fs' gs'>4 ~ <fs' gs'>16",
                ...     ]
                >>> tuplets = zip([(10, 9), (8, 9), (10, 9)], tuplets)
                >>> tuplets = [abjad.Tuplet(*_) for _ in tuplets]
                >>> tuplets = [abjad.select(tuplets)]
                >>> lilypond_file = abjad.LilyPondFile.rhythm(tuplets)
                >>> staff = lilypond_file[abjad.Staff]
                >>> abjad.override(staff).tuplet_bracket.direction = abjad.Up
                >>> abjad.override(staff).tuplet_bracket.staff_padding = 3
                >>> abjad.show(lilypond_file) # doctest: +SKIP

                >>> result = baca.select(staff).phead(-1)

                >>> result
                Chord("<fs' gs'>4")

            ..  container:: example expression

                >>> selector = baca.phead(-1)
                >>> result = selector(staff)

                >>> selector.print(result)
                Chord("<fs' gs'>4")

                >>> selector.color(result)
                >>> abjad.show(lilypond_file) # doctest: +SKIP

            ..  docs::

                >>> abjad.f(staff)
                \new Staff \with {
                    \override TupletBracket.direction = #up
                    \override TupletBracket.staff-padding = #3
                } {
                    {
                        \time 7/4
                        \tweak text #tuplet-number::calc-fraction-text
                        \times 10/9 {
                            r16
                            bf'16
                            <a'' b''>16
                            c'16
                            <d' e'>4 ~
                            <d' e'>16
                        }
                        \times 8/9 {
                            r16
                            bf'16
                            <a'' b''>16
                            d'16
                            <e' fs'>4 ~
                            <e' fs'>16
                        }
                        \tweak text #tuplet-number::calc-fraction-text
                        \times 10/9 {
                            r16
                            bf'16
                            <a'' b''>16
                            e'16
                            \once \override Accidental.color = #green
                            \once \override Beam.color = #green
                            \once \override Dots.color = #green
                            \once \override NoteHead.color = #green
                            \once \override Stem.color = #green
                            <fs' gs'>4 ~
                            <fs' gs'>16
                        }
                    }
                }

        '''
        if self._expression:
            return self._update_expression(inspect.currentframe(), lone=True)
        return self.pheads()[n]

    def pheads(self):
        r'''Selects pitched heads.

        ..  container:: example

            Selects pitched heads:

            ..  container:: example

                >>> tuplets = [
                ...     "r16 bf'16 <a'' b''>16 c'16 <d' e'>4 ~ <d' e'>16",
                ...     "r16 bf'16 <a'' b''>16 d'16 <e' fs'>4 ~ <e' fs'>16",
                ...     "r16 bf'16 <a'' b''>16 e'16 <fs' gs'>4 ~ <fs' gs'>16",
                ...     ]
                >>> tuplets = zip([(10, 9), (8, 9), (10, 9)], tuplets)
                >>> tuplets = [abjad.Tuplet(*_) for _ in tuplets]
                >>> tuplets = [abjad.select(tuplets)]
                >>> lilypond_file = abjad.LilyPondFile.rhythm(tuplets)
                >>> staff = lilypond_file[abjad.Staff]
                >>> abjad.override(staff).tuplet_bracket.direction = abjad.Up
                >>> abjad.override(staff).tuplet_bracket.staff_padding = 3
                >>> abjad.show(lilypond_file) # doctest: +SKIP

                >>> result = baca.select(staff).pheads()

                >>> for item in result:
                ...     item
                ...
                Note("bf'16")
                Chord("<a'' b''>16")
                Note("c'16")
                Chord("<d' e'>4")
                Note("bf'16")
                Chord("<a'' b''>16")
                Note("d'16")
                Chord("<e' fs'>4")
                Note("bf'16")
                Chord("<a'' b''>16")
                Note("e'16")
                Chord("<fs' gs'>4")

            ..  container:: example expression

                >>> selector = baca.pheads()
                >>> result = selector(staff)

                >>> selector.print(result)
                Note("bf'16")
                Chord("<a'' b''>16")
                Note("c'16")
                Chord("<d' e'>4")
                Note("bf'16")
                Chord("<a'' b''>16")
                Note("d'16")
                Chord("<e' fs'>4")
                Note("bf'16")
                Chord("<a'' b''>16")
                Note("e'16")
                Chord("<fs' gs'>4")

                >>> selector.color(result)
                >>> abjad.show(lilypond_file) # doctest: +SKIP

            ..  docs::

                >>> abjad.f(staff)
                \new Staff \with {
                    \override TupletBracket.direction = #up
                    \override TupletBracket.staff-padding = #3
                } {
                    {
                        \time 7/4
                        \tweak text #tuplet-number::calc-fraction-text
                        \times 10/9 {
                            r16
                            \once \override Accidental.color = #red
                            \once \override Beam.color = #red
                            \once \override Dots.color = #red
                            \once \override NoteHead.color = #red
                            \once \override Stem.color = #red
                            bf'16
                            \once \override Accidental.color = #blue
                            \once \override Beam.color = #blue
                            \once \override Dots.color = #blue
                            \once \override NoteHead.color = #blue
                            \once \override Stem.color = #blue
                            <a'' b''>16
                            \once \override Accidental.color = #red
                            \once \override Beam.color = #red
                            \once \override Dots.color = #red
                            \once \override NoteHead.color = #red
                            \once \override Stem.color = #red
                            c'16
                            \once \override Accidental.color = #blue
                            \once \override Beam.color = #blue
                            \once \override Dots.color = #blue
                            \once \override NoteHead.color = #blue
                            \once \override Stem.color = #blue
                            <d' e'>4 ~
                            <d' e'>16
                        }
                        \times 8/9 {
                            r16
                            \once \override Accidental.color = #red
                            \once \override Beam.color = #red
                            \once \override Dots.color = #red
                            \once \override NoteHead.color = #red
                            \once \override Stem.color = #red
                            bf'16
                            \once \override Accidental.color = #blue
                            \once \override Beam.color = #blue
                            \once \override Dots.color = #blue
                            \once \override NoteHead.color = #blue
                            \once \override Stem.color = #blue
                            <a'' b''>16
                            \once \override Accidental.color = #red
                            \once \override Beam.color = #red
                            \once \override Dots.color = #red
                            \once \override NoteHead.color = #red
                            \once \override Stem.color = #red
                            d'16
                            \once \override Accidental.color = #blue
                            \once \override Beam.color = #blue
                            \once \override Dots.color = #blue
                            \once \override NoteHead.color = #blue
                            \once \override Stem.color = #blue
                            <e' fs'>4 ~
                            <e' fs'>16
                        }
                        \tweak text #tuplet-number::calc-fraction-text
                        \times 10/9 {
                            r16
                            \once \override Accidental.color = #red
                            \once \override Beam.color = #red
                            \once \override Dots.color = #red
                            \once \override NoteHead.color = #red
                            \once \override Stem.color = #red
                            bf'16
                            \once \override Accidental.color = #blue
                            \once \override Beam.color = #blue
                            \once \override Dots.color = #blue
                            \once \override NoteHead.color = #blue
                            \once \override Stem.color = #blue
                            <a'' b''>16
                            \once \override Accidental.color = #red
                            \once \override Beam.color = #red
                            \once \override Dots.color = #red
                            \once \override NoteHead.color = #red
                            \once \override Stem.color = #red
                            e'16
                            \once \override Accidental.color = #blue
                            \once \override Beam.color = #blue
                            \once \override Dots.color = #blue
                            \once \override NoteHead.color = #blue
                            \once \override Stem.color = #blue
                            <fs' gs'>4 ~
                            <fs' gs'>16
                        }
                    }
                }

        '''
        if self._expression:
            return self._update_expression(inspect.currentframe())
        return self.plts().map(baca.select()[0])

    def pleaf(self, n):
        r'''Selects pitched leaf `n`.

        ..  container:: example

            Selects pitched leaf -1:

            ..  container:: example

                >>> tuplets = [
                ...     "r16 bf'16 <a'' b''>16 c'16 <d' e'>4 ~ <d' e'>16",
                ...     "r16 bf'16 <a'' b''>16 d'16 <e' fs'>4 ~ <e' fs'>16",
                ...     "r16 bf'16 <a'' b''>16 e'16 <fs' gs'>4 ~ <fs' gs'>16",
                ...     ]
                >>> tuplets = zip([(10, 9), (8, 9), (10, 9)], tuplets)
                >>> tuplets = [abjad.Tuplet(*_) for _ in tuplets]
                >>> tuplets = [abjad.select(tuplets)]
                >>> lilypond_file = abjad.LilyPondFile.rhythm(tuplets)
                >>> staff = lilypond_file[abjad.Staff]
                >>> abjad.override(staff).tuplet_bracket.direction = abjad.Up
                >>> abjad.override(staff).tuplet_bracket.staff_padding = 3
                >>> abjad.show(lilypond_file) # doctest: +SKIP

                >>> result = baca.select(staff).pleaf(-1)

                >>> result
                Chord("<fs' gs'>16")

            ..  container:: example expression

                >>> selector = baca.pleaf(-1)
                >>> result = selector(staff)

                >>> selector.print(result)
                Chord("<fs' gs'>16")

                >>> selector.color(result)
                >>> abjad.show(lilypond_file) # doctest: +SKIP

            ..  docs::

                >>> abjad.f(staff)
                \new Staff \with {
                    \override TupletBracket.direction = #up
                    \override TupletBracket.staff-padding = #3
                } {
                    {
                        \time 7/4
                        \tweak text #tuplet-number::calc-fraction-text
                        \times 10/9 {
                            r16
                            bf'16
                            <a'' b''>16
                            c'16
                            <d' e'>4 ~
                            <d' e'>16
                        }
                        \times 8/9 {
                            r16
                            bf'16
                            <a'' b''>16
                            d'16
                            <e' fs'>4 ~
                            <e' fs'>16
                        }
                        \tweak text #tuplet-number::calc-fraction-text
                        \times 10/9 {
                            r16
                            bf'16
                            <a'' b''>16
                            e'16
                            <fs' gs'>4 ~
                            \once \override Accidental.color = #green
                            \once \override Beam.color = #green
                            \once \override Dots.color = #green
                            \once \override NoteHead.color = #green
                            \once \override Stem.color = #green
                            <fs' gs'>16
                        }
                    }
                }

        '''
        if self._expression:
            return self._update_expression(inspect.currentframe(), lone=True)
        return self.pleaves()[n]

    def pleaves(self):
        r'''Selects pitched leaves.

        ..  container:: example

            Selects pitched leaves:

            ..  container:: example

                >>> tuplets = [
                ...     "r16 bf'16 <a'' b''>16 c'16 <d' e'>4 ~ <d' e'>16",
                ...     "r16 bf'16 <a'' b''>16 d'16 <e' fs'>4 ~ <e' fs'>16",
                ...     "r16 bf'16 <a'' b''>16 e'16 <fs' gs'>4 ~ <fs' gs'>16",
                ...     ]
                >>> tuplets = zip([(10, 9), (8, 9), (10, 9)], tuplets)
                >>> tuplets = [abjad.Tuplet(*_) for _ in tuplets]
                >>> tuplets = [abjad.select(tuplets)]
                >>> lilypond_file = abjad.LilyPondFile.rhythm(tuplets)
                >>> staff = lilypond_file[abjad.Staff]
                >>> abjad.override(staff).tuplet_bracket.direction = abjad.Up
                >>> abjad.override(staff).tuplet_bracket.staff_padding = 3
                >>> abjad.show(lilypond_file) # doctest: +SKIP

                >>> result = baca.select(staff).pleaves()

                >>> for item in result:
                ...     item
                ...
                Note("bf'16")
                Chord("<a'' b''>16")
                Note("c'16")
                Chord("<d' e'>4")
                Chord("<d' e'>16")
                Note("bf'16")
                Chord("<a'' b''>16")
                Note("d'16")
                Chord("<e' fs'>4")
                Chord("<e' fs'>16")
                Note("bf'16")
                Chord("<a'' b''>16")
                Note("e'16")
                Chord("<fs' gs'>4")
                Chord("<fs' gs'>16")

            ..  container:: example expression

                >>> selector = baca.pleaves()
                >>> result = selector(staff)

                >>> selector.print(result)
                Note("bf'16")
                Chord("<a'' b''>16")
                Note("c'16")
                Chord("<d' e'>4")
                Chord("<d' e'>16")
                Note("bf'16")
                Chord("<a'' b''>16")
                Note("d'16")
                Chord("<e' fs'>4")
                Chord("<e' fs'>16")
                Note("bf'16")
                Chord("<a'' b''>16")
                Note("e'16")
                Chord("<fs' gs'>4")
                Chord("<fs' gs'>16")

                >>> selector.color(result)
                >>> abjad.show(lilypond_file) # doctest: +SKIP

            ..  docs::

                >>> abjad.f(staff)
                \new Staff \with {
                    \override TupletBracket.direction = #up
                    \override TupletBracket.staff-padding = #3
                } {
                    {
                        \time 7/4
                        \tweak text #tuplet-number::calc-fraction-text
                        \times 10/9 {
                            r16
                            \once \override Accidental.color = #red
                            \once \override Beam.color = #red
                            \once \override Dots.color = #red
                            \once \override NoteHead.color = #red
                            \once \override Stem.color = #red
                            bf'16
                            \once \override Accidental.color = #blue
                            \once \override Beam.color = #blue
                            \once \override Dots.color = #blue
                            \once \override NoteHead.color = #blue
                            \once \override Stem.color = #blue
                            <a'' b''>16
                            \once \override Accidental.color = #red
                            \once \override Beam.color = #red
                            \once \override Dots.color = #red
                            \once \override NoteHead.color = #red
                            \once \override Stem.color = #red
                            c'16
                            \once \override Accidental.color = #blue
                            \once \override Beam.color = #blue
                            \once \override Dots.color = #blue
                            \once \override NoteHead.color = #blue
                            \once \override Stem.color = #blue
                            <d' e'>4 ~
                            \once \override Accidental.color = #red
                            \once \override Beam.color = #red
                            \once \override Dots.color = #red
                            \once \override NoteHead.color = #red
                            \once \override Stem.color = #red
                            <d' e'>16
                        }
                        \times 8/9 {
                            r16
                            \once \override Accidental.color = #blue
                            \once \override Beam.color = #blue
                            \once \override Dots.color = #blue
                            \once \override NoteHead.color = #blue
                            \once \override Stem.color = #blue
                            bf'16
                            \once \override Accidental.color = #red
                            \once \override Beam.color = #red
                            \once \override Dots.color = #red
                            \once \override NoteHead.color = #red
                            \once \override Stem.color = #red
                            <a'' b''>16
                            \once \override Accidental.color = #blue
                            \once \override Beam.color = #blue
                            \once \override Dots.color = #blue
                            \once \override NoteHead.color = #blue
                            \once \override Stem.color = #blue
                            d'16
                            \once \override Accidental.color = #red
                            \once \override Beam.color = #red
                            \once \override Dots.color = #red
                            \once \override NoteHead.color = #red
                            \once \override Stem.color = #red
                            <e' fs'>4 ~
                            \once \override Accidental.color = #blue
                            \once \override Beam.color = #blue
                            \once \override Dots.color = #blue
                            \once \override NoteHead.color = #blue
                            \once \override Stem.color = #blue
                            <e' fs'>16
                        }
                        \tweak text #tuplet-number::calc-fraction-text
                        \times 10/9 {
                            r16
                            \once \override Accidental.color = #red
                            \once \override Beam.color = #red
                            \once \override Dots.color = #red
                            \once \override NoteHead.color = #red
                            \once \override Stem.color = #red
                            bf'16
                            \once \override Accidental.color = #blue
                            \once \override Beam.color = #blue
                            \once \override Dots.color = #blue
                            \once \override NoteHead.color = #blue
                            \once \override Stem.color = #blue
                            <a'' b''>16
                            \once \override Accidental.color = #red
                            \once \override Beam.color = #red
                            \once \override Dots.color = #red
                            \once \override NoteHead.color = #red
                            \once \override Stem.color = #red
                            e'16
                            \once \override Accidental.color = #blue
                            \once \override Beam.color = #blue
                            \once \override Dots.color = #blue
                            \once \override NoteHead.color = #blue
                            \once \override Stem.color = #blue
                            <fs' gs'>4 ~
                            \once \override Accidental.color = #red
                            \once \override Beam.color = #red
                            \once \override Dots.color = #red
                            \once \override NoteHead.color = #red
                            \once \override Stem.color = #red
                            <fs' gs'>16
                        }
                    }
                }

        '''
        if self._expression:
            return self._update_expression(inspect.currentframe())
        return super(Selection, self).leaves(
            grace_notes=False,
            pitched=True,
            )

    def plt(self, n):
        r'''Selects pitched logical tie `n`.

        ..  container:: example

            Selects pitched logical tie -1:

            ..  container:: example

                >>> tuplets = [
                ...     "r16 bf'16 <a'' b''>16 c'16 <d' e'>4 ~ <d' e'>16",
                ...     "r16 bf'16 <a'' b''>16 d'16 <e' fs'>4 ~ <e' fs'>16",
                ...     "r16 bf'16 <a'' b''>16 e'16 <fs' gs'>4 ~ <fs' gs'>16",
                ...     ]
                >>> tuplets = zip([(10, 9), (8, 9), (10, 9)], tuplets)
                >>> tuplets = [abjad.Tuplet(*_) for _ in tuplets]
                >>> tuplets = [abjad.select(tuplets)]
                >>> lilypond_file = abjad.LilyPondFile.rhythm(tuplets)
                >>> staff = lilypond_file[abjad.Staff]
                >>> abjad.override(staff).tuplet_bracket.direction = abjad.Up
                >>> abjad.override(staff).tuplet_bracket.staff_padding = 3
                >>> abjad.show(lilypond_file) # doctest: +SKIP

                >>> result = baca.select(staff).plt(-1)

                >>> result
                LogicalTie([Chord("<fs' gs'>4"), Chord("<fs' gs'>16")])

            ..  container:: example expression

                >>> selector = baca.plt(-1)
                >>> result = selector(staff)

                >>> selector.print(result)
                LogicalTie([Chord("<fs' gs'>4"), Chord("<fs' gs'>16")])

                >>> selector.color(result)
                >>> abjad.show(lilypond_file) # doctest: +SKIP

            ..  docs::

                >>> abjad.f(staff)
                \new Staff \with {
                    \override TupletBracket.direction = #up
                    \override TupletBracket.staff-padding = #3
                } {
                    {
                        \time 7/4
                        \tweak text #tuplet-number::calc-fraction-text
                        \times 10/9 {
                            r16
                            bf'16
                            <a'' b''>16
                            c'16
                            <d' e'>4 ~
                            <d' e'>16
                        }
                        \times 8/9 {
                            r16
                            bf'16
                            <a'' b''>16
                            d'16
                            <e' fs'>4 ~
                            <e' fs'>16
                        }
                        \tweak text #tuplet-number::calc-fraction-text
                        \times 10/9 {
                            r16
                            bf'16
                            <a'' b''>16
                            e'16
                            \once \override Accidental.color = #green
                            \once \override Beam.color = #green
                            \once \override Dots.color = #green
                            \once \override NoteHead.color = #green
                            \once \override Stem.color = #green
                            <fs' gs'>4 ~
                            \once \override Accidental.color = #green
                            \once \override Beam.color = #green
                            \once \override Dots.color = #green
                            \once \override NoteHead.color = #green
                            \once \override Stem.color = #green
                            <fs' gs'>16
                        }
                    }
                }

        '''
        if self._expression:
            return self._update_expression(inspect.currentframe(), lone=True)
        return self.plts()[n]

    def plts(self):
        r'''Selects pitched logical ties.

        ..  container:: example

            Selects pitched logical ties:

            ..  container:: example

                >>> tuplets = [
                ...     "r16 bf'16 <a'' b''>16 c'16 <d' e'>4 ~ <d' e'>16",
                ...     "r16 bf'16 <a'' b''>16 d'16 <e' fs'>4 ~ <e' fs'>16",
                ...     "r16 bf'16 <a'' b''>16 e'16 <fs' gs'>4 ~ <fs' gs'>16",
                ...     ]
                >>> tuplets = zip([(10, 9), (8, 9), (10, 9)], tuplets)
                >>> tuplets = [abjad.Tuplet(*_) for _ in tuplets]
                >>> tuplets = [abjad.select(tuplets)]
                >>> lilypond_file = abjad.LilyPondFile.rhythm(tuplets)
                >>> staff = lilypond_file[abjad.Staff]
                >>> abjad.override(staff).tuplet_bracket.direction = abjad.Up
                >>> abjad.override(staff).tuplet_bracket.staff_padding = 3
                >>> abjad.show(lilypond_file) # doctest: +SKIP

                >>> result = baca.select(staff).plts()

                >>> for item in result:
                ...     item
                ...
                LogicalTie([Note("bf'16")])
                LogicalTie([Chord("<a'' b''>16")])
                LogicalTie([Note("c'16")])
                LogicalTie([Chord("<d' e'>4"), Chord("<d' e'>16")])
                LogicalTie([Note("bf'16")])
                LogicalTie([Chord("<a'' b''>16")])
                LogicalTie([Note("d'16")])
                LogicalTie([Chord("<e' fs'>4"), Chord("<e' fs'>16")])
                LogicalTie([Note("bf'16")])
                LogicalTie([Chord("<a'' b''>16")])
                LogicalTie([Note("e'16")])
                LogicalTie([Chord("<fs' gs'>4"), Chord("<fs' gs'>16")])

            ..  container:: example expression

                >>> selector = baca.plts()
                >>> result = selector(staff)

                >>> selector.print(result)
                LogicalTie([Note("bf'16")])
                LogicalTie([Chord("<a'' b''>16")])
                LogicalTie([Note("c'16")])
                LogicalTie([Chord("<d' e'>4"), Chord("<d' e'>16")])
                LogicalTie([Note("bf'16")])
                LogicalTie([Chord("<a'' b''>16")])
                LogicalTie([Note("d'16")])
                LogicalTie([Chord("<e' fs'>4"), Chord("<e' fs'>16")])
                LogicalTie([Note("bf'16")])
                LogicalTie([Chord("<a'' b''>16")])
                LogicalTie([Note("e'16")])
                LogicalTie([Chord("<fs' gs'>4"), Chord("<fs' gs'>16")])

                >>> selector.color(result)
                >>> abjad.show(lilypond_file) # doctest: +SKIP

            ..  docs::

                >>> abjad.f(staff)
                \new Staff \with {
                    \override TupletBracket.direction = #up
                    \override TupletBracket.staff-padding = #3
                } {
                    {
                        \time 7/4
                        \tweak text #tuplet-number::calc-fraction-text
                        \times 10/9 {
                            r16
                            \once \override Accidental.color = #red
                            \once \override Beam.color = #red
                            \once \override Dots.color = #red
                            \once \override NoteHead.color = #red
                            \once \override Stem.color = #red
                            bf'16
                            \once \override Accidental.color = #blue
                            \once \override Beam.color = #blue
                            \once \override Dots.color = #blue
                            \once \override NoteHead.color = #blue
                            \once \override Stem.color = #blue
                            <a'' b''>16
                            \once \override Accidental.color = #red
                            \once \override Beam.color = #red
                            \once \override Dots.color = #red
                            \once \override NoteHead.color = #red
                            \once \override Stem.color = #red
                            c'16
                            \once \override Accidental.color = #blue
                            \once \override Beam.color = #blue
                            \once \override Dots.color = #blue
                            \once \override NoteHead.color = #blue
                            \once \override Stem.color = #blue
                            <d' e'>4 ~
                            \once \override Accidental.color = #blue
                            \once \override Beam.color = #blue
                            \once \override Dots.color = #blue
                            \once \override NoteHead.color = #blue
                            \once \override Stem.color = #blue
                            <d' e'>16
                        }
                        \times 8/9 {
                            r16
                            \once \override Accidental.color = #red
                            \once \override Beam.color = #red
                            \once \override Dots.color = #red
                            \once \override NoteHead.color = #red
                            \once \override Stem.color = #red
                            bf'16
                            \once \override Accidental.color = #blue
                            \once \override Beam.color = #blue
                            \once \override Dots.color = #blue
                            \once \override NoteHead.color = #blue
                            \once \override Stem.color = #blue
                            <a'' b''>16
                            \once \override Accidental.color = #red
                            \once \override Beam.color = #red
                            \once \override Dots.color = #red
                            \once \override NoteHead.color = #red
                            \once \override Stem.color = #red
                            d'16
                            \once \override Accidental.color = #blue
                            \once \override Beam.color = #blue
                            \once \override Dots.color = #blue
                            \once \override NoteHead.color = #blue
                            \once \override Stem.color = #blue
                            <e' fs'>4 ~
                            \once \override Accidental.color = #blue
                            \once \override Beam.color = #blue
                            \once \override Dots.color = #blue
                            \once \override NoteHead.color = #blue
                            \once \override Stem.color = #blue
                            <e' fs'>16
                        }
                        \tweak text #tuplet-number::calc-fraction-text
                        \times 10/9 {
                            r16
                            \once \override Accidental.color = #red
                            \once \override Beam.color = #red
                            \once \override Dots.color = #red
                            \once \override NoteHead.color = #red
                            \once \override Stem.color = #red
                            bf'16
                            \once \override Accidental.color = #blue
                            \once \override Beam.color = #blue
                            \once \override Dots.color = #blue
                            \once \override NoteHead.color = #blue
                            \once \override Stem.color = #blue
                            <a'' b''>16
                            \once \override Accidental.color = #red
                            \once \override Beam.color = #red
                            \once \override Dots.color = #red
                            \once \override NoteHead.color = #red
                            \once \override Stem.color = #red
                            e'16
                            \once \override Accidental.color = #blue
                            \once \override Beam.color = #blue
                            \once \override Dots.color = #blue
                            \once \override NoteHead.color = #blue
                            \once \override Stem.color = #blue
                            <fs' gs'>4 ~
                            \once \override Accidental.color = #blue
                            \once \override Beam.color = #blue
                            \once \override Dots.color = #blue
                            \once \override NoteHead.color = #blue
                            \once \override Stem.color = #blue
                            <fs' gs'>16
                        }
                    }
                }

        '''
        if self._expression:
            return self._update_expression(inspect.currentframe())
        return self.logical_ties(pitched=True, grace_notes=None)

    def ptail(self, n):
        r'''Selects pitched tail `n`.

        ..  container:: example

            Selects pitched tail -1:

            ..  container:: example

                >>> tuplets = [
                ...     "r16 bf'16 <a'' b''>16 c'16 <d' e'>4 ~ <d' e'>16",
                ...     "r16 bf'16 <a'' b''>16 d'16 <e' fs'>4 ~ <e' fs'>16",
                ...     "r16 bf'16 <a'' b''>16 e'16 <fs' gs'>4 ~ <fs' gs'>16",
                ...     ]
                >>> tuplets = zip([(10, 9), (8, 9), (10, 9)], tuplets)
                >>> tuplets = [abjad.Tuplet(*_) for _ in tuplets]
                >>> tuplets = [abjad.select(tuplets)]
                >>> lilypond_file = abjad.LilyPondFile.rhythm(tuplets)
                >>> staff = lilypond_file[abjad.Staff]
                >>> abjad.override(staff).tuplet_bracket.direction = abjad.Up
                >>> abjad.override(staff).tuplet_bracket.staff_padding = 3
                >>> abjad.show(lilypond_file) # doctest: +SKIP

                >>> result = baca.select(staff).ptail(-1)

                >>> result
                Chord("<fs' gs'>16")

            ..  container:: example expression

                >>> selector = baca.ptail(-1)
                >>> result = selector(staff)

                >>> selector.print(result)
                Chord("<fs' gs'>16")

                >>> selector.color(result)
                >>> abjad.show(lilypond_file) # doctest: +SKIP

            ..  docs::

                >>> abjad.f(staff)
                \new Staff \with {
                    \override TupletBracket.direction = #up
                    \override TupletBracket.staff-padding = #3
                } {
                    {
                        \time 7/4
                        \tweak text #tuplet-number::calc-fraction-text
                        \times 10/9 {
                            r16
                            bf'16
                            <a'' b''>16
                            c'16
                            <d' e'>4 ~
                            <d' e'>16
                        }
                        \times 8/9 {
                            r16
                            bf'16
                            <a'' b''>16
                            d'16
                            <e' fs'>4 ~
                            <e' fs'>16
                        }
                        \tweak text #tuplet-number::calc-fraction-text
                        \times 10/9 {
                            r16
                            bf'16
                            <a'' b''>16
                            e'16
                            <fs' gs'>4 ~
                            \once \override Accidental.color = #green
                            \once \override Beam.color = #green
                            \once \override Dots.color = #green
                            \once \override NoteHead.color = #green
                            \once \override Stem.color = #green
                            <fs' gs'>16
                        }
                    }
                }

        '''
        if self._expression:
            return self._update_expression(inspect.currentframe(), lone=True)
        return self.ptails()[n]

    def ptails(self):
        r'''Selects pitched tails.

        ..  container:: example

            Selects pitched tails:

            ..  container:: example

                >>> tuplets = [
                ...     "r16 bf'16 <a'' b''>16 c'16 <d' e'>4 ~ <d' e'>16",
                ...     "r16 bf'16 <a'' b''>16 d'16 <e' fs'>4 ~ <e' fs'>16",
                ...     "r16 bf'16 <a'' b''>16 e'16 <fs' gs'>4 ~ <fs' gs'>16",
                ...     ]
                >>> tuplets = zip([(10, 9), (8, 9), (10, 9)], tuplets)
                >>> tuplets = [abjad.Tuplet(*_) for _ in tuplets]
                >>> tuplets = [abjad.select(tuplets)]
                >>> lilypond_file = abjad.LilyPondFile.rhythm(tuplets)
                >>> staff = lilypond_file[abjad.Staff]
                >>> abjad.override(staff).tuplet_bracket.direction = abjad.Up
                >>> abjad.override(staff).tuplet_bracket.staff_padding = 3
                >>> abjad.show(lilypond_file) # doctest: +SKIP

                >>> result = baca.select(staff).ptails()

                >>> for item in result:
                ...     item
                ...
                Note("bf'16")
                Chord("<a'' b''>16")
                Note("c'16")
                Chord("<d' e'>16")
                Note("bf'16")
                Chord("<a'' b''>16")
                Note("d'16")
                Chord("<e' fs'>16")
                Note("bf'16")
                Chord("<a'' b''>16")
                Note("e'16")
                Chord("<fs' gs'>16")

            ..  container:: example expression

                >>> selector = baca.ptails()
                >>> result = selector(staff)

                >>> selector.print(result)
                Note("bf'16")
                Chord("<a'' b''>16")
                Note("c'16")
                Chord("<d' e'>16")
                Note("bf'16")
                Chord("<a'' b''>16")
                Note("d'16")
                Chord("<e' fs'>16")
                Note("bf'16")
                Chord("<a'' b''>16")
                Note("e'16")
                Chord("<fs' gs'>16")

                >>> selector.color(result)
                >>> abjad.show(lilypond_file) # doctest: +SKIP

            ..  docs::

                >>> abjad.f(staff)
                \new Staff \with {
                    \override TupletBracket.direction = #up
                    \override TupletBracket.staff-padding = #3
                } {
                    {
                        \time 7/4
                        \tweak text #tuplet-number::calc-fraction-text
                        \times 10/9 {
                            r16
                            \once \override Accidental.color = #red
                            \once \override Beam.color = #red
                            \once \override Dots.color = #red
                            \once \override NoteHead.color = #red
                            \once \override Stem.color = #red
                            bf'16
                            \once \override Accidental.color = #blue
                            \once \override Beam.color = #blue
                            \once \override Dots.color = #blue
                            \once \override NoteHead.color = #blue
                            \once \override Stem.color = #blue
                            <a'' b''>16
                            \once \override Accidental.color = #red
                            \once \override Beam.color = #red
                            \once \override Dots.color = #red
                            \once \override NoteHead.color = #red
                            \once \override Stem.color = #red
                            c'16
                            <d' e'>4 ~
                            \once \override Accidental.color = #blue
                            \once \override Beam.color = #blue
                            \once \override Dots.color = #blue
                            \once \override NoteHead.color = #blue
                            \once \override Stem.color = #blue
                            <d' e'>16
                        }
                        \times 8/9 {
                            r16
                            \once \override Accidental.color = #red
                            \once \override Beam.color = #red
                            \once \override Dots.color = #red
                            \once \override NoteHead.color = #red
                            \once \override Stem.color = #red
                            bf'16
                            \once \override Accidental.color = #blue
                            \once \override Beam.color = #blue
                            \once \override Dots.color = #blue
                            \once \override NoteHead.color = #blue
                            \once \override Stem.color = #blue
                            <a'' b''>16
                            \once \override Accidental.color = #red
                            \once \override Beam.color = #red
                            \once \override Dots.color = #red
                            \once \override NoteHead.color = #red
                            \once \override Stem.color = #red
                            d'16
                            <e' fs'>4 ~
                            \once \override Accidental.color = #blue
                            \once \override Beam.color = #blue
                            \once \override Dots.color = #blue
                            \once \override NoteHead.color = #blue
                            \once \override Stem.color = #blue
                            <e' fs'>16
                        }
                        \tweak text #tuplet-number::calc-fraction-text
                        \times 10/9 {
                            r16
                            \once \override Accidental.color = #red
                            \once \override Beam.color = #red
                            \once \override Dots.color = #red
                            \once \override NoteHead.color = #red
                            \once \override Stem.color = #red
                            bf'16
                            \once \override Accidental.color = #blue
                            \once \override Beam.color = #blue
                            \once \override Dots.color = #blue
                            \once \override NoteHead.color = #blue
                            \once \override Stem.color = #blue
                            <a'' b''>16
                            \once \override Accidental.color = #red
                            \once \override Beam.color = #red
                            \once \override Dots.color = #red
                            \once \override NoteHead.color = #red
                            \once \override Stem.color = #red
                            e'16
                            <fs' gs'>4 ~
                            \once \override Accidental.color = #blue
                            \once \override Beam.color = #blue
                            \once \override Dots.color = #blue
                            \once \override NoteHead.color = #blue
                            \once \override Stem.color = #blue
                            <fs' gs'>16
                        }
                    }
                }

        '''
        if self._expression:
            return self._update_expression(inspect.currentframe())
        return self.plts().map(baca.select()[-1])

    def ptlt(self, n):
        r'''Selects pitched trivial logical tie `n`.

        ..  container:: example

            Selects pitched trivial logical tie -1:

            ..  container:: example

                >>> tuplets = [
                ...     "r16 bf'16 <a'' b''>16 c'16 <d' e'>4 ~ <d' e'>16",
                ...     "r16 bf'16 <a'' b''>16 d'16 <e' fs'>4 ~ <e' fs'>16",
                ...     "r16 bf'16 <a'' b''>16 e'16 <fs' gs'>4 ~ <fs' gs'>16",
                ...     ]
                >>> tuplets = zip([(10, 9), (8, 9), (10, 9)], tuplets)
                >>> tuplets = [abjad.Tuplet(*_) for _ in tuplets]
                >>> tuplets = [abjad.select(tuplets)]
                >>> lilypond_file = abjad.LilyPondFile.rhythm(tuplets)
                >>> staff = lilypond_file[abjad.Staff]
                >>> abjad.override(staff).tuplet_bracket.direction = abjad.Up
                >>> abjad.override(staff).tuplet_bracket.staff_padding = 3
                >>> abjad.show(lilypond_file) # doctest: +SKIP

                >>> result = baca.select(staff).ptlt(-1)

                >>> result
                LogicalTie([Note("e'16")])

            ..  container:: example expression

                >>> selector = baca.ptlt(-1)
                >>> result = selector(staff)

                >>> selector.print(result)
                LogicalTie([Note("e'16")])

                >>> selector.color(result)
                >>> abjad.show(lilypond_file) # doctest: +SKIP

            ..  docs::

                >>> abjad.f(staff)
                \new Staff \with {
                    \override TupletBracket.direction = #up
                    \override TupletBracket.staff-padding = #3
                } {
                    {
                        \time 7/4
                        \tweak text #tuplet-number::calc-fraction-text
                        \times 10/9 {
                            r16
                            bf'16
                            <a'' b''>16
                            c'16
                            <d' e'>4 ~
                            <d' e'>16
                        }
                        \times 8/9 {
                            r16
                            bf'16
                            <a'' b''>16
                            d'16
                            <e' fs'>4 ~
                            <e' fs'>16
                        }
                        \tweak text #tuplet-number::calc-fraction-text
                        \times 10/9 {
                            r16
                            bf'16
                            <a'' b''>16
                            \once \override Accidental.color = #green
                            \once \override Beam.color = #green
                            \once \override Dots.color = #green
                            \once \override NoteHead.color = #green
                            \once \override Stem.color = #green
                            e'16
                            <fs' gs'>4 ~
                            <fs' gs'>16
                        }
                    }
                }

        '''
        if self._expression:
            return self._update_expression(inspect.currentframe(), lone=True)
        return self.ptlts()[n]

    def ptlts(self):
        r'''Selects pitched trivial logical ties.

        ..  container:: example

            Selects pitched trivial logical ties:

            ..  container:: example

                >>> tuplets = [
                ...     "r16 bf'16 <a'' b''>16 c'16 <d' e'>4 ~ <d' e'>16",
                ...     "r16 bf'16 <a'' b''>16 d'16 <e' fs'>4 ~ <e' fs'>16",
                ...     "r16 bf'16 <a'' b''>16 e'16 <fs' gs'>4 ~ <fs' gs'>16",
                ...     ]
                >>> tuplets = zip([(10, 9), (8, 9), (10, 9)], tuplets)
                >>> tuplets = [abjad.Tuplet(*_) for _ in tuplets]
                >>> tuplets = [abjad.select(tuplets)]
                >>> lilypond_file = abjad.LilyPondFile.rhythm(tuplets)
                >>> staff = lilypond_file[abjad.Staff]
                >>> abjad.override(staff).tuplet_bracket.direction = abjad.Up
                >>> abjad.override(staff).tuplet_bracket.staff_padding = 3
                >>> abjad.show(lilypond_file) # doctest: +SKIP

                >>> result = baca.select(staff).ptlts()

                >>> for item in result:
                ...     item
                ...
                LogicalTie([Note("bf'16")])
                LogicalTie([Chord("<a'' b''>16")])
                LogicalTie([Note("c'16")])
                LogicalTie([Note("bf'16")])
                LogicalTie([Chord("<a'' b''>16")])
                LogicalTie([Note("d'16")])
                LogicalTie([Note("bf'16")])
                LogicalTie([Chord("<a'' b''>16")])
                LogicalTie([Note("e'16")])

            ..  container:: example expression

                >>> selector = baca.ptlts()
                >>> result = selector(staff)

                >>> selector.print(result)
                LogicalTie([Note("bf'16")])
                LogicalTie([Chord("<a'' b''>16")])
                LogicalTie([Note("c'16")])
                LogicalTie([Note("bf'16")])
                LogicalTie([Chord("<a'' b''>16")])
                LogicalTie([Note("d'16")])
                LogicalTie([Note("bf'16")])
                LogicalTie([Chord("<a'' b''>16")])
                LogicalTie([Note("e'16")])

                >>> selector.color(result)
                >>> abjad.show(lilypond_file) # doctest: +SKIP

            ..  docs::

                >>> abjad.f(staff)
                \new Staff \with {
                    \override TupletBracket.direction = #up
                    \override TupletBracket.staff-padding = #3
                } {
                    {
                        \time 7/4
                        \tweak text #tuplet-number::calc-fraction-text
                        \times 10/9 {
                            r16
                            \once \override Accidental.color = #red
                            \once \override Beam.color = #red
                            \once \override Dots.color = #red
                            \once \override NoteHead.color = #red
                            \once \override Stem.color = #red
                            bf'16
                            \once \override Accidental.color = #blue
                            \once \override Beam.color = #blue
                            \once \override Dots.color = #blue
                            \once \override NoteHead.color = #blue
                            \once \override Stem.color = #blue
                            <a'' b''>16
                            \once \override Accidental.color = #red
                            \once \override Beam.color = #red
                            \once \override Dots.color = #red
                            \once \override NoteHead.color = #red
                            \once \override Stem.color = #red
                            c'16
                            <d' e'>4 ~
                            <d' e'>16
                        }
                        \times 8/9 {
                            r16
                            \once \override Accidental.color = #blue
                            \once \override Beam.color = #blue
                            \once \override Dots.color = #blue
                            \once \override NoteHead.color = #blue
                            \once \override Stem.color = #blue
                            bf'16
                            \once \override Accidental.color = #red
                            \once \override Beam.color = #red
                            \once \override Dots.color = #red
                            \once \override NoteHead.color = #red
                            \once \override Stem.color = #red
                            <a'' b''>16
                            \once \override Accidental.color = #blue
                            \once \override Beam.color = #blue
                            \once \override Dots.color = #blue
                            \once \override NoteHead.color = #blue
                            \once \override Stem.color = #blue
                            d'16
                            <e' fs'>4 ~
                            <e' fs'>16
                        }
                        \tweak text #tuplet-number::calc-fraction-text
                        \times 10/9 {
                            r16
                            \once \override Accidental.color = #red
                            \once \override Beam.color = #red
                            \once \override Dots.color = #red
                            \once \override NoteHead.color = #red
                            \once \override Stem.color = #red
                            bf'16
                            \once \override Accidental.color = #blue
                            \once \override Beam.color = #blue
                            \once \override Dots.color = #blue
                            \once \override NoteHead.color = #blue
                            \once \override Stem.color = #blue
                            <a'' b''>16
                            \once \override Accidental.color = #red
                            \once \override Beam.color = #red
                            \once \override Dots.color = #red
                            \once \override NoteHead.color = #red
                            \once \override Stem.color = #red
                            e'16
                            <fs' gs'>4 ~
                            <fs' gs'>16
                        }
                    }
                }

        '''
        if self._expression:
            return self._update_expression(inspect.currentframe())
        return self.logical_ties(
            grace_notes=None,
            nontrivial=False,
            pitched=True,
            )

    def qrun(self, n):
        r'''Selects equipitch run `n`.

        ..  container:: example

            Selects equipitch run -1:

            ..  container:: example

                >>> tuplets = [
                ...     "r16 c'16 c'16 c'16 <d' e'>4 ~ <d' e'>16",
                ...     "r16 d'16 d'16 d'16 <e' fs'>4 ~ <e' fs'>16",
                ...     "r16 e'16 e'16 e'16 <fs' gs'>4 ~ <fs' gs'>16",
                ...     ]
                >>> tuplets = zip([(10, 9), (8, 9), (10, 9)], tuplets)
                >>> tuplets = [abjad.Tuplet(*_) for _ in tuplets]
                >>> tuplets = [abjad.select(tuplets)]
                >>> lilypond_file = abjad.LilyPondFile.rhythm(tuplets)
                >>> staff = lilypond_file[abjad.Staff]
                >>> abjad.override(staff).tuplet_bracket.direction = abjad.Up
                >>> abjad.override(staff).tuplet_bracket.staff_padding = 3
                >>> abjad.show(lilypond_file) # doctest: +SKIP

                >>> result = baca.select(staff).qrun(-1)

                >>> result
                Run([Chord("<fs' gs'>4"), Chord("<fs' gs'>16")])

            ..  container:: example expression

                >>> selector = baca.qrun(-1)
                >>> result = selector(staff)

                >>> selector.print(result)
                Run([Chord("<fs' gs'>4"), Chord("<fs' gs'>16")])

                >>> selector.color(result)
                >>> abjad.show(lilypond_file) # doctest: +SKIP

            ..  docs::

                >>> abjad.f(staff)
                \new Staff \with {
                    \override TupletBracket.direction = #up
                    \override TupletBracket.staff-padding = #3
                } {
                    {
                        \time 7/4
                        \tweak text #tuplet-number::calc-fraction-text
                        \times 10/9 {
                            r16
                            c'16
                            c'16
                            c'16
                            <d' e'>4 ~
                            <d' e'>16
                        }
                        \times 8/9 {
                            r16
                            d'16
                            d'16
                            d'16
                            <e' fs'>4 ~
                            <e' fs'>16
                        }
                        \tweak text #tuplet-number::calc-fraction-text
                        \times 10/9 {
                            r16
                            e'16
                            e'16
                            e'16
                            \once \override Accidental.color = #green
                            \once \override Beam.color = #green
                            \once \override Dots.color = #green
                            \once \override NoteHead.color = #green
                            \once \override Stem.color = #green
                            <fs' gs'>4 ~
                            \once \override Accidental.color = #green
                            \once \override Beam.color = #green
                            \once \override Dots.color = #green
                            \once \override NoteHead.color = #green
                            \once \override Stem.color = #green
                            <fs' gs'>16
                        }
                    }
                }

        '''
        if self._expression:
            return self._update_expression(inspect.currentframe(), lone=True)
        return self.qruns()[n]

    def qruns(self):
        r'''Selects equipitch runs.

        ..  container:: example

            Selects equipitch runs:

            ..  container:: example

                >>> tuplets = [
                ...     "r16 c'16 c'16 c'16 <d' e'>4 ~ <d' e'>16",
                ...     "r16 d'16 d'16 d'16 <e' fs'>4 ~ <e' fs'>16",
                ...     "r16 e'16 e'16 e'16 <fs' gs'>4 ~ <fs' gs'>16",
                ...     ]
                >>> tuplets = zip([(10, 9), (8, 9), (10, 9)], tuplets)
                >>> tuplets = [abjad.Tuplet(*_) for _ in tuplets]
                >>> tuplets = [abjad.select(tuplets)]
                >>> lilypond_file = abjad.LilyPondFile.rhythm(tuplets)
                >>> staff = lilypond_file[abjad.Staff]
                >>> abjad.override(staff).tuplet_bracket.direction = abjad.Up
                >>> abjad.override(staff).tuplet_bracket.staff_padding = 3
                >>> abjad.show(lilypond_file) # doctest: +SKIP

                >>> result = baca.select(staff).qruns()

                >>> for item in result:
                ...     item
                ...
                Run([Note("c'16"), Note("c'16"), Note("c'16")])
                Run([Chord("<d' e'>4"), Chord("<d' e'>16")])
                Run([Note("d'16"), Note("d'16"), Note("d'16")])
                Run([Chord("<e' fs'>4"), Chord("<e' fs'>16")])
                Run([Note("e'16"), Note("e'16"), Note("e'16")])
                Run([Chord("<fs' gs'>4"), Chord("<fs' gs'>16")])

            ..  container:: example expression

                >>> selector = baca.qruns()
                >>> result = selector(staff)

                >>> selector.print(result)
                Run([Note("c'16"), Note("c'16"), Note("c'16")])
                Run([Chord("<d' e'>4"), Chord("<d' e'>16")])
                Run([Note("d'16"), Note("d'16"), Note("d'16")])
                Run([Chord("<e' fs'>4"), Chord("<e' fs'>16")])
                Run([Note("e'16"), Note("e'16"), Note("e'16")])
                Run([Chord("<fs' gs'>4"), Chord("<fs' gs'>16")])

                >>> selector.color(result)
                >>> abjad.show(lilypond_file) # doctest: +SKIP

            ..  docs::

                >>> abjad.f(staff)
                \new Staff \with {
                    \override TupletBracket.direction = #up
                    \override TupletBracket.staff-padding = #3
                } {
                    {
                        \time 7/4
                        \tweak text #tuplet-number::calc-fraction-text
                        \times 10/9 {
                            r16
                            \once \override Accidental.color = #red
                            \once \override Beam.color = #red
                            \once \override Dots.color = #red
                            \once \override NoteHead.color = #red
                            \once \override Stem.color = #red
                            c'16
                            \once \override Accidental.color = #red
                            \once \override Beam.color = #red
                            \once \override Dots.color = #red
                            \once \override NoteHead.color = #red
                            \once \override Stem.color = #red
                            c'16
                            \once \override Accidental.color = #red
                            \once \override Beam.color = #red
                            \once \override Dots.color = #red
                            \once \override NoteHead.color = #red
                            \once \override Stem.color = #red
                            c'16
                            \once \override Accidental.color = #blue
                            \once \override Beam.color = #blue
                            \once \override Dots.color = #blue
                            \once \override NoteHead.color = #blue
                            \once \override Stem.color = #blue
                            <d' e'>4 ~
                            \once \override Accidental.color = #blue
                            \once \override Beam.color = #blue
                            \once \override Dots.color = #blue
                            \once \override NoteHead.color = #blue
                            \once \override Stem.color = #blue
                            <d' e'>16
                        }
                        \times 8/9 {
                            r16
                            \once \override Accidental.color = #red
                            \once \override Beam.color = #red
                            \once \override Dots.color = #red
                            \once \override NoteHead.color = #red
                            \once \override Stem.color = #red
                            d'16
                            \once \override Accidental.color = #red
                            \once \override Beam.color = #red
                            \once \override Dots.color = #red
                            \once \override NoteHead.color = #red
                            \once \override Stem.color = #red
                            d'16
                            \once \override Accidental.color = #red
                            \once \override Beam.color = #red
                            \once \override Dots.color = #red
                            \once \override NoteHead.color = #red
                            \once \override Stem.color = #red
                            d'16
                            \once \override Accidental.color = #blue
                            \once \override Beam.color = #blue
                            \once \override Dots.color = #blue
                            \once \override NoteHead.color = #blue
                            \once \override Stem.color = #blue
                            <e' fs'>4 ~
                            \once \override Accidental.color = #blue
                            \once \override Beam.color = #blue
                            \once \override Dots.color = #blue
                            \once \override NoteHead.color = #blue
                            \once \override Stem.color = #blue
                            <e' fs'>16
                        }
                        \tweak text #tuplet-number::calc-fraction-text
                        \times 10/9 {
                            r16
                            \once \override Accidental.color = #red
                            \once \override Beam.color = #red
                            \once \override Dots.color = #red
                            \once \override NoteHead.color = #red
                            \once \override Stem.color = #red
                            e'16
                            \once \override Accidental.color = #red
                            \once \override Beam.color = #red
                            \once \override Dots.color = #red
                            \once \override NoteHead.color = #red
                            \once \override Stem.color = #red
                            e'16
                            \once \override Accidental.color = #red
                            \once \override Beam.color = #red
                            \once \override Dots.color = #red
                            \once \override NoteHead.color = #red
                            \once \override Stem.color = #red
                            e'16
                            \once \override Accidental.color = #blue
                            \once \override Beam.color = #blue
                            \once \override Dots.color = #blue
                            \once \override NoteHead.color = #blue
                            \once \override Stem.color = #blue
                            <fs' gs'>4 ~
                            \once \override Accidental.color = #blue
                            \once \override Beam.color = #blue
                            \once \override Dots.color = #blue
                            \once \override NoteHead.color = #blue
                            \once \override Stem.color = #blue
                            <fs' gs'>16
                        }
                    }
                }

        '''
        if self._expression:
            return self._update_expression(inspect.currentframe())
        result = self.pleaves()
        result = result.group_by_pitch()
        result = result.map(baca.group_by_contiguity())
        result = result.flatten(depth=1)
        result = result.map(abjad.Run)
        return result

    def rleak(self):
        r'''Leaks to the right.

        Returns new selection.
        '''
        if self._expression:
            return self._update_expression(inspect.currentframe())
        return self.with_next_leaf()

    def rleaves(self):
        r'''Selects leaves, leaked to the right.

        ..  container:: example

            Selects leaves (leaked to the right) in tuplet 1:

            ..  container:: example

                >>> tuplets = [
                ...     "r16 bf'16 <a'' b''>16 c'16 <d' e'>4 ~ <d' e'>16",
                ...     "r16 bf'16 <a'' b''>16 d'16 <e' fs'>4 ~ <e' fs'>16",
                ...     "r16 bf'16 <a'' b''>16 e'16 <fs' gs'>4 ~ <fs' gs'>16",
                ...     ]
                >>> tuplets = zip([(10, 9), (8, 9), (10, 9)], tuplets)
                >>> tuplets = [abjad.Tuplet(*_) for _ in tuplets]
                >>> tuplets = [abjad.select(tuplets)]
                >>> lilypond_file = abjad.LilyPondFile.rhythm(tuplets)
                >>> staff = lilypond_file[abjad.Staff]
                >>> abjad.override(staff).tuplet_bracket.direction = abjad.Up
                >>> abjad.override(staff).tuplet_bracket.staff_padding = 3
                >>> abjad.show(lilypond_file) # doctest: +SKIP

                >>> result = baca.select(staff).tuplets()[1:2].rleaves()

                >>> for item in result:
                ...     item
                ...
                Rest('r16')
                Note("bf'16")
                Chord("<a'' b''>16")
                Note("d'16")
                Chord("<e' fs'>4")
                Chord("<e' fs'>16")
                Rest('r16')

            ..  container:: example expression

                >>> selector = baca.tuplets()[1:2].rleaves()
                >>> result = selector(staff)

                >>> selector.print(result)
                Rest('r16')
                Note("bf'16")
                Chord("<a'' b''>16")
                Note("d'16")
                Chord("<e' fs'>4")
                Chord("<e' fs'>16")
                Rest('r16')

                >>> selector.color(result)
                >>> abjad.show(lilypond_file) # doctest: +SKIP

            ..  docs::

                >>> abjad.f(staff)
                \new Staff \with {
                    \override TupletBracket.direction = #up
                    \override TupletBracket.staff-padding = #3
                } {
                    {
                        \time 7/4
                        \tweak text #tuplet-number::calc-fraction-text
                        \times 10/9 {
                            r16
                            bf'16
                            <a'' b''>16
                            c'16
                            <d' e'>4 ~
                            <d' e'>16
                        }
                        \times 8/9 {
                            \once \override Dots.color = #red
                            \once \override Rest.color = #red
                            r16
                            \once \override Accidental.color = #blue
                            \once \override Beam.color = #blue
                            \once \override Dots.color = #blue
                            \once \override NoteHead.color = #blue
                            \once \override Stem.color = #blue
                            bf'16
                            \once \override Accidental.color = #red
                            \once \override Beam.color = #red
                            \once \override Dots.color = #red
                            \once \override NoteHead.color = #red
                            \once \override Stem.color = #red
                            <a'' b''>16
                            \once \override Accidental.color = #blue
                            \once \override Beam.color = #blue
                            \once \override Dots.color = #blue
                            \once \override NoteHead.color = #blue
                            \once \override Stem.color = #blue
                            d'16
                            \once \override Accidental.color = #red
                            \once \override Beam.color = #red
                            \once \override Dots.color = #red
                            \once \override NoteHead.color = #red
                            \once \override Stem.color = #red
                            <e' fs'>4 ~
                            \once \override Accidental.color = #blue
                            \once \override Beam.color = #blue
                            \once \override Dots.color = #blue
                            \once \override NoteHead.color = #blue
                            \once \override Stem.color = #blue
                            <e' fs'>16
                        }
                        \tweak text #tuplet-number::calc-fraction-text
                        \times 10/9 {
                            \once \override Dots.color = #red
                            \once \override Rest.color = #red
                            r16
                            bf'16
                            <a'' b''>16
                            e'16
                            <fs' gs'>4 ~
                            <fs' gs'>16
                        }
                    }
                }

        '''
        if self._expression:
            return self._update_expression(inspect.currentframe())
        return self.leaves().with_next_leaf()

    def rrun(self, n):
        r'''Selects run `n` (leaked to the right).

        ..  container:: example

            Selects run 1 (leaked to the right):

            ..  container:: example

                >>> tuplets = [
                ...     "r16 c'16 c'16 c'16 <d' e'>4 ~ <d' e'>16",
                ...     "r16 d'16 d'16 d'16 <e' fs'>4 ~ <e' fs'>16",
                ...     "r16 e'16 e'16 e'16 <fs' gs'>4 ~ <fs' gs'>16",
                ...     ]
                >>> tuplets = zip([(10, 9), (8, 9), (10, 9)], tuplets)
                >>> tuplets = [abjad.Tuplet(*_) for _ in tuplets]
                >>> tuplets = [abjad.select(tuplets)]
                >>> lilypond_file = abjad.LilyPondFile.rhythm(tuplets)
                >>> staff = lilypond_file[abjad.Staff]
                >>> abjad.override(staff).tuplet_bracket.direction = abjad.Up
                >>> abjad.override(staff).tuplet_bracket.staff_padding = 3
                >>> abjad.show(lilypond_file) # doctest: +SKIP

                >>> result = baca.select(staff).rrun(1)

                >>> result
                Run([Note("d'16"), Note("d'16"), Note("d'16"), Chord("<e' fs'>4"), Chord("<e' fs'>16"), Rest('r16')])

            ..  container:: example expression

                >>> selector = baca.rrun(1)
                >>> result = selector(staff)

                >>> selector.print(result)
                Run([Note("d'16"), Note("d'16"), Note("d'16"), Chord("<e' fs'>4"), Chord("<e' fs'>16"), Rest('r16')])

                >>> selector.color(result)
                >>> abjad.show(lilypond_file) # doctest: +SKIP

            ..  docs::

                >>> abjad.f(staff)
                \new Staff \with {
                    \override TupletBracket.direction = #up
                    \override TupletBracket.staff-padding = #3
                } {
                    {
                        \time 7/4
                        \tweak text #tuplet-number::calc-fraction-text
                        \times 10/9 {
                            r16
                            c'16
                            c'16
                            c'16
                            <d' e'>4 ~
                            <d' e'>16
                        }
                        \times 8/9 {
                            r16
                            \once \override Accidental.color = #green
                            \once \override Beam.color = #green
                            \once \override Dots.color = #green
                            \once \override NoteHead.color = #green
                            \once \override Stem.color = #green
                            d'16
                            \once \override Accidental.color = #green
                            \once \override Beam.color = #green
                            \once \override Dots.color = #green
                            \once \override NoteHead.color = #green
                            \once \override Stem.color = #green
                            d'16
                            \once \override Accidental.color = #green
                            \once \override Beam.color = #green
                            \once \override Dots.color = #green
                            \once \override NoteHead.color = #green
                            \once \override Stem.color = #green
                            d'16
                            \once \override Accidental.color = #green
                            \once \override Beam.color = #green
                            \once \override Dots.color = #green
                            \once \override NoteHead.color = #green
                            \once \override Stem.color = #green
                            <e' fs'>4 ~
                            \once \override Accidental.color = #green
                            \once \override Beam.color = #green
                            \once \override Dots.color = #green
                            \once \override NoteHead.color = #green
                            \once \override Stem.color = #green
                            <e' fs'>16
                        }
                        \tweak text #tuplet-number::calc-fraction-text
                        \times 10/9 {
                            \once \override Dots.color = #green
                            \once \override Rest.color = #green
                            r16
                            e'16
                            e'16
                            e'16
                            <fs' gs'>4 ~
                            <fs' gs'>16
                        }
                    }
                }

        '''
        if self._expression:
            return self._update_expression(inspect.currentframe(), lone=True)
        return self.rruns()[n]

    def rruns(self):
        r'''Selects runs (leaked to the right).

        ..  container:: example

            Selects runs (leaked to the right):

            ..  container:: example

                >>> tuplets = [
                ...     "r16 c'16 c'16 c'16 <d' e'>4 ~ <d' e'>16",
                ...     "r16 d'16 d'16 d'16 <e' fs'>4 ~ <e' fs'>16",
                ...     "r16 e'16 e'16 e'16 <fs' gs'>4 ~ <fs' gs'>16",
                ...     ]
                >>> tuplets = zip([(10, 9), (8, 9), (10, 9)], tuplets)
                >>> tuplets = [abjad.Tuplet(*_) for _ in tuplets]
                >>> tuplets = [abjad.select(tuplets)]
                >>> lilypond_file = abjad.LilyPondFile.rhythm(tuplets)
                >>> staff = lilypond_file[abjad.Staff]
                >>> abjad.override(staff).tuplet_bracket.direction = abjad.Up
                >>> abjad.override(staff).tuplet_bracket.staff_padding = 3
                >>> abjad.show(lilypond_file) # doctest: +SKIP

                >>> result = baca.select(staff).rruns()

                >>> for item in result:
                ...     item
                ...
                Run([Note("c'16"), Note("c'16"), Note("c'16"), Chord("<d' e'>4"), Chord("<d' e'>16"), Rest('r16')])
                Run([Note("d'16"), Note("d'16"), Note("d'16"), Chord("<e' fs'>4"), Chord("<e' fs'>16"), Rest('r16')])
                Run([Note("e'16"), Note("e'16"), Note("e'16"), Chord("<fs' gs'>4"), Chord("<fs' gs'>16")])

            ..  container:: example expression

                >>> selector = baca.rruns()
                >>> result = selector(staff)

                >>> selector.print(result)
                Run([Note("c'16"), Note("c'16"), Note("c'16"), Chord("<d' e'>4"), Chord("<d' e'>16"), Rest('r16')])
                Run([Note("d'16"), Note("d'16"), Note("d'16"), Chord("<e' fs'>4"), Chord("<e' fs'>16"), Rest('r16')])
                Run([Note("e'16"), Note("e'16"), Note("e'16"), Chord("<fs' gs'>4"), Chord("<fs' gs'>16")])

                >>> selector.color(result)
                >>> abjad.show(lilypond_file) # doctest: +SKIP

            ..  docs::

                >>> abjad.f(staff)
                \new Staff \with {
                    \override TupletBracket.direction = #up
                    \override TupletBracket.staff-padding = #3
                } {
                    {
                        \time 7/4
                        \tweak text #tuplet-number::calc-fraction-text
                        \times 10/9 {
                            r16
                            \once \override Accidental.color = #red
                            \once \override Beam.color = #red
                            \once \override Dots.color = #red
                            \once \override NoteHead.color = #red
                            \once \override Stem.color = #red
                            c'16
                            \once \override Accidental.color = #red
                            \once \override Beam.color = #red
                            \once \override Dots.color = #red
                            \once \override NoteHead.color = #red
                            \once \override Stem.color = #red
                            c'16
                            \once \override Accidental.color = #red
                            \once \override Beam.color = #red
                            \once \override Dots.color = #red
                            \once \override NoteHead.color = #red
                            \once \override Stem.color = #red
                            c'16
                            \once \override Accidental.color = #red
                            \once \override Beam.color = #red
                            \once \override Dots.color = #red
                            \once \override NoteHead.color = #red
                            \once \override Stem.color = #red
                            <d' e'>4 ~
                            \once \override Accidental.color = #red
                            \once \override Beam.color = #red
                            \once \override Dots.color = #red
                            \once \override NoteHead.color = #red
                            \once \override Stem.color = #red
                            <d' e'>16
                        }
                        \times 8/9 {
                            \once \override Dots.color = #red
                            \once \override Rest.color = #red
                            r16
                            \once \override Accidental.color = #blue
                            \once \override Beam.color = #blue
                            \once \override Dots.color = #blue
                            \once \override NoteHead.color = #blue
                            \once \override Stem.color = #blue
                            d'16
                            \once \override Accidental.color = #blue
                            \once \override Beam.color = #blue
                            \once \override Dots.color = #blue
                            \once \override NoteHead.color = #blue
                            \once \override Stem.color = #blue
                            d'16
                            \once \override Accidental.color = #blue
                            \once \override Beam.color = #blue
                            \once \override Dots.color = #blue
                            \once \override NoteHead.color = #blue
                            \once \override Stem.color = #blue
                            d'16
                            \once \override Accidental.color = #blue
                            \once \override Beam.color = #blue
                            \once \override Dots.color = #blue
                            \once \override NoteHead.color = #blue
                            \once \override Stem.color = #blue
                            <e' fs'>4 ~
                            \once \override Accidental.color = #blue
                            \once \override Beam.color = #blue
                            \once \override Dots.color = #blue
                            \once \override NoteHead.color = #blue
                            \once \override Stem.color = #blue
                            <e' fs'>16
                        }
                        \tweak text #tuplet-number::calc-fraction-text
                        \times 10/9 {
                            \once \override Dots.color = #blue
                            \once \override Rest.color = #blue
                            r16
                            \once \override Accidental.color = #red
                            \once \override Beam.color = #red
                            \once \override Dots.color = #red
                            \once \override NoteHead.color = #red
                            \once \override Stem.color = #red
                            e'16
                            \once \override Accidental.color = #red
                            \once \override Beam.color = #red
                            \once \override Dots.color = #red
                            \once \override NoteHead.color = #red
                            \once \override Stem.color = #red
                            e'16
                            \once \override Accidental.color = #red
                            \once \override Beam.color = #red
                            \once \override Dots.color = #red
                            \once \override NoteHead.color = #red
                            \once \override Stem.color = #red
                            e'16
                            \once \override Accidental.color = #red
                            \once \override Beam.color = #red
                            \once \override Dots.color = #red
                            \once \override NoteHead.color = #red
                            \once \override Stem.color = #red
                            <fs' gs'>4 ~
                            \once \override Accidental.color = #red
                            \once \override Beam.color = #red
                            \once \override Dots.color = #red
                            \once \override NoteHead.color = #red
                            \once \override Stem.color = #red
                            <fs' gs'>16
                        }
                    }
                }

        '''
        if self._expression:
            return self._update_expression(inspect.currentframe())
        result = self.runs().map(baca.with_next_leaf())
        return result.map(abjad.Run)

    def skip(self, n):
        r'''Selects skip `n`.
        '''
        if self._expression:
            return self._update_expression(inspect.currentframe())
        return self.skips()[n]

    def skips(self):
        r'''Selects skips.
        '''
        if self._expression:
            return self._update_expression(inspect.currentframe())
        return self.components(abjad.Skip)

    def stage(self, n, stage_measure_map):
        r'''Selects group `n` of output grouped into stages.

        ..  container:: example

            Selects group 1 of leaves grouped into stages:

            ..  container:: example

                >>> stage_measure_map = baca.StageMeasureMap([1, 2, 1])
                >>> staff = abjad.Staff("c'8 d' e' f' g' a' b' c''")
                >>> abjad.attach(abjad.TimeSignature((2, 8)), staff[0])
                >>> abjad.attach(abjad.TimeSignature((3, 8)), staff[4])
                >>> abjad.attach(abjad.TimeSignature((1, 8)), staff[7])
                >>> abjad.show(staff) # doctest: +SKIP

                >>> result = baca.select(staff).leaves()
                >>> result = result.stage(1, stage_measure_map)

                >>> result
                Selection([Note("e'8"), Note("f'8"), Note("g'8"), Note("a'8"), Note("b'8")])

            ..  container:: example expression

                >>> selector = baca.select().leaves()
                >>> selector = selector.stage(1, stage_measure_map)
                >>> result = selector(staff)

                >>> selector.print(result)
                Selection([Note("e'8"), Note("f'8"), Note("g'8"), Note("a'8"), Note("b'8")])

                >>> selector.color(result)
                >>> abjad.setting(staff).auto_beaming = False
                >>> abjad.show(staff) # doctest: +SKIP

            ..  docs::

                >>> abjad.f(staff)
                \new Staff \with {
                    autoBeaming = ##f
                } {
                    \time 2/8
                    c'8
                    d'8
                    \once \override Accidental.color = #green
                    \once \override Beam.color = #green
                    \once \override Dots.color = #green
                    \once \override NoteHead.color = #green
                    \once \override Stem.color = #green
                    e'8
                    \once \override Accidental.color = #green
                    \once \override Beam.color = #green
                    \once \override Dots.color = #green
                    \once \override NoteHead.color = #green
                    \once \override Stem.color = #green
                    f'8
                    \once \override Accidental.color = #green
                    \once \override Beam.color = #green
                    \once \override Dots.color = #green
                    \once \override NoteHead.color = #green
                    \once \override Stem.color = #green
                    \time 3/8
                    g'8
                    \once \override Accidental.color = #green
                    \once \override Beam.color = #green
                    \once \override Dots.color = #green
                    \once \override NoteHead.color = #green
                    \once \override Stem.color = #green
                    a'8
                    \once \override Accidental.color = #green
                    \once \override Beam.color = #green
                    \once \override Dots.color = #green
                    \once \override NoteHead.color = #green
                    \once \override Stem.color = #green
                    b'8
                    \time 1/8
                    c''8
                }

        Returns selector.
        '''
        if self._expression:
            return self._update_expression(inspect.currentframe(), lone=True)
        return self.stages(stage_measure_map)[n]

    def stages(self, stage_measure_map):
        r'''Groups previous output into stages.

        ..  container:: example

            Groups leaves into stages:

            ..  container:: example

                >>> stage_measure_map = baca.StageMeasureMap([1, 2, 1])
                >>> staff = abjad.Staff("c'8 d' e' f' g' a' b' c''")
                >>> abjad.attach(abjad.TimeSignature((2, 8)), staff[0])
                >>> abjad.attach(abjad.TimeSignature((3, 8)), staff[4])
                >>> abjad.attach(abjad.TimeSignature((1, 8)), staff[7])
                >>> abjad.show(staff) # doctest: +SKIP

                >>> result = baca.select(staff).leaves()
                >>> result = result.stages(stage_measure_map)

                >>> for item in result:
                ...     item
                Selection([Note("c'8"), Note("d'8")])
                Selection([Note("e'8"), Note("f'8"), Note("g'8"), Note("a'8"), Note("b'8")])
                Selection([Note("c''8")])

            ..  container:: example expression

                >>> selector = baca.select().leaves()
                >>> selector = selector.stages(stage_measure_map)
                >>> result = selector(staff)

                >>> selector.print(result)
                Selection([Note("c'8"), Note("d'8")])
                Selection([Note("e'8"), Note("f'8"), Note("g'8"), Note("a'8"), Note("b'8")])
                Selection([Note("c''8")])

                >>> selector.color(result)
                >>> abjad.setting(staff).auto_beaming = False
                >>> abjad.show(staff) # doctest: +SKIP

            ..  docs::

                >>> abjad.f(staff)
                \new Staff \with {
                    autoBeaming = ##f
                } {
                    \once \override Accidental.color = #red
                    \once \override Beam.color = #red
                    \once \override Dots.color = #red
                    \once \override NoteHead.color = #red
                    \once \override Stem.color = #red
                    \time 2/8
                    c'8
                    \once \override Accidental.color = #red
                    \once \override Beam.color = #red
                    \once \override Dots.color = #red
                    \once \override NoteHead.color = #red
                    \once \override Stem.color = #red
                    d'8
                    \once \override Accidental.color = #blue
                    \once \override Beam.color = #blue
                    \once \override Dots.color = #blue
                    \once \override NoteHead.color = #blue
                    \once \override Stem.color = #blue
                    e'8
                    \once \override Accidental.color = #blue
                    \once \override Beam.color = #blue
                    \once \override Dots.color = #blue
                    \once \override NoteHead.color = #blue
                    \once \override Stem.color = #blue
                    f'8
                    \once \override Accidental.color = #blue
                    \once \override Beam.color = #blue
                    \once \override Dots.color = #blue
                    \once \override NoteHead.color = #blue
                    \once \override Stem.color = #blue
                    \time 3/8
                    g'8
                    \once \override Accidental.color = #blue
                    \once \override Beam.color = #blue
                    \once \override Dots.color = #blue
                    \once \override NoteHead.color = #blue
                    \once \override Stem.color = #blue
                    a'8
                    \once \override Accidental.color = #blue
                    \once \override Beam.color = #blue
                    \once \override Dots.color = #blue
                    \once \override NoteHead.color = #blue
                    \once \override Stem.color = #blue
                    b'8
                    \once \override Accidental.color = #red
                    \once \override Beam.color = #red
                    \once \override Dots.color = #red
                    \once \override NoteHead.color = #red
                    \once \override Stem.color = #red
                    \time 1/8
                    c''8
                }

        Returns selector.
        '''
        if self._expression:
            return self._update_expression(inspect.currentframe())
        counts = []
        for item in stage_measure_map:
            if isinstance(item, int):
                counts.append(item)
            elif isinstance(item, abjad.Fermata):
                counts.append(1)
            else:
                raise TypeError(item)
        measures = self.group_by_measure()
        if len(measures) != sum(counts):
            message = f'{len(measures)} measures found;'
            message += f' stage measure map gives {sum(counts)} instead.'
            raise Exception(message)
        measures = baca.sequence(measures)
        parts = measures.partition_by_counts(
            counts,
            overhang=abjad.Exact,
            )
        selections = []
        for part in parts:
            selection = []
            for measure in part:
                selection.extend(measure)
            selection = baca.select(selection)
            selections.append(selection)
        return baca.select(selections)

    def tleaves(self):
        r'''Selects trimmed leaves.

        ..  container:: example

            Selects trimmed leaves:

            ..  container:: example

                >>> tuplets = [
                ...     "r16 bf'16 <a'' b''>16 c'16 <d' e'>4 ~ <d' e'>16",
                ...     "r16 bf'16 <a'' b''>16 d'16 <e' fs'>4 ~ <e' fs'>16",
                ...     "r16 bf'16 <a'' b''>16 e'16 <fs' gs'>4 ~ <fs' gs'>16",
                ...     ]
                >>> tuplets = zip([(10, 9), (8, 9), (10, 9)], tuplets)
                >>> tuplets = [abjad.Tuplet(*_) for _ in tuplets]
                >>> tuplets = [abjad.select(tuplets)]
                >>> lilypond_file = abjad.LilyPondFile.rhythm(tuplets)
                >>> staff = lilypond_file[abjad.Staff]
                >>> abjad.override(staff).tuplet_bracket.direction = abjad.Up
                >>> abjad.override(staff).tuplet_bracket.staff_padding = 3
                >>> abjad.show(lilypond_file) # doctest: +SKIP

                >>> result = baca.select(staff).tleaves()

                >>> for item in result:
                ...     item
                ...
                Note("bf'16")
                Chord("<a'' b''>16")
                Note("c'16")
                Chord("<d' e'>4")
                Chord("<d' e'>16")
                Rest('r16')
                Note("bf'16")
                Chord("<a'' b''>16")
                Note("d'16")
                Chord("<e' fs'>4")
                Chord("<e' fs'>16")
                Rest('r16')
                Note("bf'16")
                Chord("<a'' b''>16")
                Note("e'16")
                Chord("<fs' gs'>4")
                Chord("<fs' gs'>16")

            ..  container:: example expression

                >>> selector = baca.tleaves()
                >>> result = selector(staff)

                >>> selector.print(result)
                Note("bf'16")
                Chord("<a'' b''>16")
                Note("c'16")
                Chord("<d' e'>4")
                Chord("<d' e'>16")
                Rest('r16')
                Note("bf'16")
                Chord("<a'' b''>16")
                Note("d'16")
                Chord("<e' fs'>4")
                Chord("<e' fs'>16")
                Rest('r16')
                Note("bf'16")
                Chord("<a'' b''>16")
                Note("e'16")
                Chord("<fs' gs'>4")
                Chord("<fs' gs'>16")

                >>> selector.color(result)
                >>> abjad.show(lilypond_file) # doctest: +SKIP

            ..  docs::

                >>> abjad.f(staff)
                \new Staff \with {
                    \override TupletBracket.direction = #up
                    \override TupletBracket.staff-padding = #3
                } {
                    {
                        \time 7/4
                        \tweak text #tuplet-number::calc-fraction-text
                        \times 10/9 {
                            r16
                            \once \override Accidental.color = #red
                            \once \override Beam.color = #red
                            \once \override Dots.color = #red
                            \once \override NoteHead.color = #red
                            \once \override Stem.color = #red
                            bf'16
                            \once \override Accidental.color = #blue
                            \once \override Beam.color = #blue
                            \once \override Dots.color = #blue
                            \once \override NoteHead.color = #blue
                            \once \override Stem.color = #blue
                            <a'' b''>16
                            \once \override Accidental.color = #red
                            \once \override Beam.color = #red
                            \once \override Dots.color = #red
                            \once \override NoteHead.color = #red
                            \once \override Stem.color = #red
                            c'16
                            \once \override Accidental.color = #blue
                            \once \override Beam.color = #blue
                            \once \override Dots.color = #blue
                            \once \override NoteHead.color = #blue
                            \once \override Stem.color = #blue
                            <d' e'>4 ~
                            \once \override Accidental.color = #red
                            \once \override Beam.color = #red
                            \once \override Dots.color = #red
                            \once \override NoteHead.color = #red
                            \once \override Stem.color = #red
                            <d' e'>16
                        }
                        \times 8/9 {
                            \once \override Dots.color = #blue
                            \once \override Rest.color = #blue
                            r16
                            \once \override Accidental.color = #red
                            \once \override Beam.color = #red
                            \once \override Dots.color = #red
                            \once \override NoteHead.color = #red
                            \once \override Stem.color = #red
                            bf'16
                            \once \override Accidental.color = #blue
                            \once \override Beam.color = #blue
                            \once \override Dots.color = #blue
                            \once \override NoteHead.color = #blue
                            \once \override Stem.color = #blue
                            <a'' b''>16
                            \once \override Accidental.color = #red
                            \once \override Beam.color = #red
                            \once \override Dots.color = #red
                            \once \override NoteHead.color = #red
                            \once \override Stem.color = #red
                            d'16
                            \once \override Accidental.color = #blue
                            \once \override Beam.color = #blue
                            \once \override Dots.color = #blue
                            \once \override NoteHead.color = #blue
                            \once \override Stem.color = #blue
                            <e' fs'>4 ~
                            \once \override Accidental.color = #red
                            \once \override Beam.color = #red
                            \once \override Dots.color = #red
                            \once \override NoteHead.color = #red
                            \once \override Stem.color = #red
                            <e' fs'>16
                        }
                        \tweak text #tuplet-number::calc-fraction-text
                        \times 10/9 {
                            \once \override Dots.color = #blue
                            \once \override Rest.color = #blue
                            r16
                            \once \override Accidental.color = #red
                            \once \override Beam.color = #red
                            \once \override Dots.color = #red
                            \once \override NoteHead.color = #red
                            \once \override Stem.color = #red
                            bf'16
                            \once \override Accidental.color = #blue
                            \once \override Beam.color = #blue
                            \once \override Dots.color = #blue
                            \once \override NoteHead.color = #blue
                            \once \override Stem.color = #blue
                            <a'' b''>16
                            \once \override Accidental.color = #red
                            \once \override Beam.color = #red
                            \once \override Dots.color = #red
                            \once \override NoteHead.color = #red
                            \once \override Stem.color = #red
                            e'16
                            \once \override Accidental.color = #blue
                            \once \override Beam.color = #blue
                            \once \override Dots.color = #blue
                            \once \override NoteHead.color = #blue
                            \once \override Stem.color = #blue
                            <fs' gs'>4 ~
                            \once \override Accidental.color = #red
                            \once \override Beam.color = #red
                            \once \override Dots.color = #red
                            \once \override NoteHead.color = #red
                            \once \override Stem.color = #red
                            <fs' gs'>16
                        }
                    }
                }

        '''
        if self._expression:
            return self._update_expression(inspect.currentframe())
        return super(Selection, self).leaves(trim=True, grace_notes=False)

    def tuplet_tleaves(self):
        r'''Selects trimmed leaves in each tuplet.
        '''
        if self._expression:
            return self._update_expression(inspect.currentframe())
        return self.tuplets().map(baca.tleaves())

    def wleaves(self):
        r'''Selects leaves, leaked "wide" (to both the left and right).

        ..  container:: example

            Selects leaves (leaked wide) in tuplet 1:

            ..  container:: example

                >>> tuplets = [
                ...     "r16 bf'16 <a'' b''>16 c'16 <d' e'>4 ~ <d' e'>16",
                ...     "r16 bf'16 <a'' b''>16 d'16 <e' fs'>4 ~ <e' fs'>16",
                ...     "r16 bf'16 <a'' b''>16 e'16 <fs' gs'>4 ~ <fs' gs'>16",
                ...     ]
                >>> tuplets = zip([(10, 9), (8, 9), (10, 9)], tuplets)
                >>> tuplets = [abjad.Tuplet(*_) for _ in tuplets]
                >>> tuplets = [abjad.select(tuplets)]
                >>> lilypond_file = abjad.LilyPondFile.rhythm(tuplets)
                >>> staff = lilypond_file[abjad.Staff]
                >>> abjad.override(staff).tuplet_bracket.direction = abjad.Up
                >>> abjad.override(staff).tuplet_bracket.staff_padding = 3
                >>> abjad.show(lilypond_file) # doctest: +SKIP

                >>> result = baca.select(staff).tuplets()[1:2].wleaves()

                >>> for item in result:
                ...     item
                ...
                Chord("<d' e'>16")
                Rest('r16')
                Note("bf'16")
                Chord("<a'' b''>16")
                Note("d'16")
                Chord("<e' fs'>4")
                Chord("<e' fs'>16")
                Rest('r16')

            ..  container:: example expression

                >>> selector = baca.tuplets()[1:2].wleaves()
                >>> result = selector(staff)

                >>> selector.print(result)
                Chord("<d' e'>16")
                Rest('r16')
                Note("bf'16")
                Chord("<a'' b''>16")
                Note("d'16")
                Chord("<e' fs'>4")
                Chord("<e' fs'>16")
                Rest('r16')

                >>> selector.color(result)
                >>> abjad.show(lilypond_file) # doctest: +SKIP

            ..  docs::

                >>> abjad.f(staff)
                \new Staff \with {
                    \override TupletBracket.direction = #up
                    \override TupletBracket.staff-padding = #3
                } {
                    {
                        \time 7/4
                        \tweak text #tuplet-number::calc-fraction-text
                        \times 10/9 {
                            r16
                            bf'16
                            <a'' b''>16
                            c'16
                            <d' e'>4 ~
                            \once \override Accidental.color = #red
                            \once \override Beam.color = #red
                            \once \override Dots.color = #red
                            \once \override NoteHead.color = #red
                            \once \override Stem.color = #red
                            <d' e'>16
                        }
                        \times 8/9 {
                            \once \override Dots.color = #blue
                            \once \override Rest.color = #blue
                            r16
                            \once \override Accidental.color = #red
                            \once \override Beam.color = #red
                            \once \override Dots.color = #red
                            \once \override NoteHead.color = #red
                            \once \override Stem.color = #red
                            bf'16
                            \once \override Accidental.color = #blue
                            \once \override Beam.color = #blue
                            \once \override Dots.color = #blue
                            \once \override NoteHead.color = #blue
                            \once \override Stem.color = #blue
                            <a'' b''>16
                            \once \override Accidental.color = #red
                            \once \override Beam.color = #red
                            \once \override Dots.color = #red
                            \once \override NoteHead.color = #red
                            \once \override Stem.color = #red
                            d'16
                            \once \override Accidental.color = #blue
                            \once \override Beam.color = #blue
                            \once \override Dots.color = #blue
                            \once \override NoteHead.color = #blue
                            \once \override Stem.color = #blue
                            <e' fs'>4 ~
                            \once \override Accidental.color = #red
                            \once \override Beam.color = #red
                            \once \override Dots.color = #red
                            \once \override NoteHead.color = #red
                            \once \override Stem.color = #red
                            <e' fs'>16
                        }
                        \tweak text #tuplet-number::calc-fraction-text
                        \times 10/9 {
                            \once \override Dots.color = #blue
                            \once \override Rest.color = #blue
                            r16
                            bf'16
                            <a'' b''>16
                            e'16
                            <fs' gs'>4 ~
                            <fs' gs'>16
                        }
                    }
                }

        '''
        if self._expression:
            return self._update_expression(inspect.currentframe())
        return self.leaves().with_previous_leaf().with_next_leaf()


def _select(items=None):
    if items is None:
        return baca.Expression().select()
    return baca.Selection(items=items)
