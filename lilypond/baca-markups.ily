%%% BOWSTROKE MARKUP %%%

baca-full-downbow-markup = \markup {
    \combine
        \musicglyph #"scripts.downbow"
        \path #0.15 
        #'(
            (moveto 0.7375 0.05)
            (rlineto 1 0)
            (closepath)
            )
    }

baca-full-upbow-markup = \markup {
    \combine
        \musicglyph #"scripts.upbow"
        \path #0.15 
        #'(
            (moveto 0.62 2.005)
            (rlineto 1 0)
            (closepath)
            )
    }

baca-stop-on-string-markup = \markup {
    \path #0.15 
    #'(
        (moveto 0 0)
        (rlineto 1 0)
        (closepath)
        (rmoveto 1 0.3)
        (rlineto 0 -0.6)
        (closepath)
        )
    }

baca-stop-on-string-full-downbow-markup = \markup {
    \combine
        \musicglyph #"scripts.downbow"
        \path #0.15 
        #'(
            (moveto 0.7375 0.05)
            (rlineto 1 0)
            (closepath)
            (rmoveto 1 0.3)
            (rlineto 0 -0.6)
            (closepath)
            )
    }

baca-stop-on-string-full-upbow-markup = \markup {
    \combine
        \musicglyph #"scripts.upbow"
        \path #0.15 
        #'(
            (moveto 0.62 2.005)
            (rlineto 1 0)
            (closepath)
            (rmoveto 1 0.3)
            (rlineto 0 -0.6)
            (closepath)
            )
    }

%%% CIRCLE BOWING MARKUP %%%

baca-circle-bowing-markup = \markup
    \translate #'(0.6 . 0)
    \scale #'(0.35 . 0.35)
    \concat {
        \draw-circle #2 #0.4 ##f
        \hspace #-4.5
        \raise #0.75
        \with-color #white
        \scale #'(0.35 . 0.35)
        \draw-circle #1 #1 ##t
        \hspace #-1.5
        \raise #-0.75
        \scale #'(0.75 . 0.75)
        \triangle ##t
        \hspace #-1
        \raise #1.35
        \with-color #white
        \rotate #45
        \filled-box #'(-0.35 . 0.35) #'(-0.35 . 0.35) #0
    }

%%% DAMP MARKUP %%%

baca-damp-markup = \markup {
    \scale #'(0.75 . 0.75)
    \combine
    \bold \override #'(font-name . "Times") "O"
    \path #0.15
    #'(
        (moveto -.4 .7)
        (rlineto 2.4 0)
        (closepath)
        (moveto .8 -.5)
        (rlineto 0 2.4)
        )
    }

baca-damp-half-clt-markup = \markup {
    \raise #0.25 \baca-damp-markup ½ clt
    }

%%% DIAMOND MARKUP %%%

baca-black-diamond-markup = \markup
{
    \scale #'(0.75 . 0.75)
    \musicglyph #"noteheads.s2harmonic"
}

baca-diamond-markup = \markup
{
    \scale #'(0.75 . 0.75)
    \musicglyph #"noteheads.s0harmonic"
}

baca-double-black-diamond-markup = \markup
{
    \override #'(baseline-skip . 1.75)
    \scale #'(0.75 . 0.75)
    \column
    {
        \musicglyph #"noteheads.s2harmonic"
        \musicglyph #"noteheads.s2harmonic"
    }
}

baca-double-diamond-markup = \markup
{
    \override #'(baseline-skip . 1.75)
    \scale #'(0.75 . 0.75)
    \column
    {
        \musicglyph #"noteheads.s0harmonic"
        \musicglyph #"noteheads.s0harmonic"
    }
}

baca-triple-black-diamond-markup = \markup
{
    \override #'(baseline-skip . 1.75)
    \scale #'(0.75 . 0.75)
    \column
    {
        \musicglyph #"noteheads.s2harmonic"
        \musicglyph #"noteheads.s2harmonic"
        \musicglyph #"noteheads.s2harmonic"
    }
}

baca-triple-diamond-markup = \markup
{
    \override #'(baseline-skip . 1.75)
    \scale #'(0.75 . 0.75)
    \column
    {
        \musicglyph #"noteheads.s0harmonic"
        \musicglyph #"noteheads.s0harmonic"
        \musicglyph #"noteheads.s0harmonic"
    }
}

%%% FERMATA MARKUP %%%

baca-fermata-markup = \markup { \musicglyph #"scripts.ufermata" }

baca-long-fermata-markup = \markup { \musicglyph #"scripts.ulongfermata" }

baca-short-fermata-markup = \markup { \musicglyph #"scripts.ushortfermata" }

baca-very-long-fermata-markup = \markup {
    \musicglyph #"scripts.uverylongfermata"
    }
