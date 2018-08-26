%%% BCP SPANNER %%%

bacaStartTextSpanBCP = #(
    make-music 'TextSpanEvent 'span-direction START 'spanner-id "BCP"
    )

bacaStopTextSpanBCP = #(
    make-music 'TextSpanEvent 'span-direction STOP 'spanner-id "BCP"
    )

#(define-markup-command
    (baca-bcp-left layout props n d) (number? number?)
    (interpret-markup layout props
    #{
    \markup \concat {
        \upright \fraction #(number->string n) #(number->string d)
        \hspace #0.5
        }
    #})
    )

baca-bcp-spanner-left-text = #(
    define-music-function
    (parser location n d music)
    (number? number? ly:music?)
    #{
    \tweak bound-details.left.text \markup \baca-bcp-left #n #d
    $music
    #}
    )

#(define-markup-command
    (baca-bcp-right layout props n d)
    (number? number?)
    (interpret-markup layout props
    #{
    \markup \upright \fraction #(number->string n) #(number->string d)
    #})
    )

baca-bcp-spanner-right-text = #(
    define-music-function
    (parser location n d music)
    (number? number? ly:music?)
    #{
    \tweak bound-details.right.text \markup \baca-bcp-right #n #d
    $music
    #}
    ) 

%%% LOCAL MEASURE INDEX SPANNER %%%

bacaStartTextSpanLMI = #(
    make-music 'TextSpanEvent 'span-direction START 'spanner-id "LMI"
    )

bacaStopTextSpanLMI = #(
    make-music 'TextSpanEvent 'span-direction STOP 'spanner-id "LMI"
    )

#(define-markup-command
    (baca-lmi-left-markup layout props lmi)
    (string?)
    (interpret-markup layout props
        #{
        \markup
        \with-color #(x11-color 'DarkCyan)
        \fontsize #-3
        \upright
        \concat { "<"  #lmi ">" \hspace #0.5 }
        #}
        )
    )

baca-lmi-left-text-tweak = #(
    define-music-function
    (parser location left music)
    (string? ly:music?)
    #{
    \tweak bound-details.left.text \markup \baca-lmi-left-markup #left
    $music
    #}
    )

#(define-markup-command
    (baca-lmi-right-markup layout props lmi)
    (string?)
    (interpret-markup layout props
        #{
        \markup 
        \with-color #(x11-color 'DarkCyan)
        \fontsize #-3
        \upright
        \concat { "<" #lmi ">" }
        #}
        )
    )

baca-lmi-right-text-tweak = #(
    define-music-function
    (parser location right music)
    (string? ly:music?)
    #{
    \tweak bound-details.right.text \markup \baca-lmi-right-markup #right
    $music
    #}
    ) 

baca-start-lmi-left-only = #(
    define-music-function
    (parser location left music)
    (string? ly:music?)
    #{
    - \abjad-invisible-line
    - \baca-lmi-left-text-tweak #left
    - \tweak extra-offset #'(0 . 9)
    $music
    #}
    )

baca-start-lmi-both = #(
    define-music-function
    (parser location left right music)
    (string? string? ly:music?)
    #{
    - \abjad-invisible-line
    - \baca-lmi-left-text-tweak #left
    - \baca-lmi-right-text-tweak #right
    - \tweak extra-offset #'(0 . 9)
    $music
    #}
    )

%%% LOCAL MEASURE NUMBER SPANNER %%%

bacaStartTextSpanLMN = #(
    make-music 'TextSpanEvent 'span-direction START 'spanner-id "LMN"
    )

bacaStopTextSpanLMN = #(
    make-music 'TextSpanEvent 'span-direction STOP 'spanner-id "LMN"
    )

#(define-markup-command
    (baca-lmn-left-markup layout props lmn)
    (string?)
    (interpret-markup layout props
        #{
        \markup
        \with-color #(x11-color 'DarkCyan)
        \fontsize #-3
        \upright
        \concat { "(("  #lmn "))" \hspace #0.5 }
        #}
        )
    )

baca-lmn-left-text-tweak = #(
    define-music-function
    (parser location left music)
    (string? ly:music?)
    #{
    \tweak bound-details.left.text \markup \baca-lmn-left-markup #left
    $music
    #}
    )

#(define-markup-command
    (baca-lmn-right-markup layout props lmn)
    (string?)
    (interpret-markup layout props
        #{
        \markup 
        \with-color #(x11-color 'DarkCyan)
        \fontsize #-3
        \upright
        \concat { "<" #lmn ">" }
        #}
        )
    )

baca-lmn-right-text-tweak = #(
    define-music-function
    (parser location right music)
    (string? ly:music?)
    #{
    \tweak bound-details.right.text \markup \baca-lmn-right-markup #right
    $music
    #}
    ) 

baca-start-lmn-left-only = #(
    define-music-function
    (parser location left music)
    (string? ly:music?)
    #{
    - \abjad-invisible-line
    - \baca-lmn-left-text-tweak #left
    - \tweak extra-offset #'(0 . 9)
    $music
    #}
    )

baca-start-lmn-both = #(
    define-music-function
    (parser location left right music)
    (string? string? ly:music?)
    #{
    - \abjad-invisible-line
    - \baca-lmn-left-text-tweak #left
    - \baca-lmn-right-text-tweak #right
    - \tweak extra-offset #'(0 . 9)
    $music
    #}
    )

%%% MEASURE NUMBER SPANNER %%%

bacaStartTextSpanMN = #(
    make-music 'TextSpanEvent 'span-direction START 'spanner-id "MN"
    )

bacaStopTextSpanMN = #(
    make-music 'TextSpanEvent 'span-direction STOP 'spanner-id "MN"
    )

#(define-markup-command
    (baca-mn-left-markup layout props mn)
    (string?)
    (interpret-markup layout props
        #{
        \markup
        \with-color #(x11-color 'DarkCyan)
        \fontsize #-3
        \upright
        \concat { "("  #mn ")" \hspace #0.5 }
        #}
        )
    )

baca-mn-left-text-tweak = #(
    define-music-function
    (parser location left music)
    (string? ly:music?)
    #{
    \tweak bound-details.left.text \markup \baca-mn-left-markup #left
    $music
    #}
    )

#(define-markup-command
    (baca-mn-right-markup layout props mn)
    (string?)
    (interpret-markup layout props
        #{
        \markup 
        \with-color #(x11-color 'DarkCyan)
        \fontsize #-3
        \upright
        \concat { "(" #mn ")" }
        #}
        )
    )

baca-mn-right-text-tweak = #(
    define-music-function
    (parser location right music)
    (string? ly:music?)
    #{
    \tweak bound-details.right.text \markup \baca-mn-right-markup #right
    $music
    #}
    ) 

baca-start-mn-left-only = #(
    define-music-function
    (parser location left music)
    (string? ly:music?)
    #{
    - \abjad-invisible-line
    - \baca-mn-left-text-tweak #left
    - \tweak extra-offset #'(0 . 12)
    $music
    #}
    )

baca-start-mn-both = #(
    define-music-function
    (parser location left right music)
    (string? string? ly:music?)
    #{
    - \abjad-invisible-line
    - \baca-mn-left-text-tweak #left
    - \baca-mn-right-text-tweak #right
    - \tweak extra-offset #'(0 . 12)
    $music
    #}
    )

%%% METRONOME MARK SPANNER %%%

baca-metronome-mark-spanner-colored-left-text = #(
    define-music-function
    (parser location log dots stem string color music)
    (number? number? number? string? symbol? ly:music?)
    #{
    \tweak bound-details.left.text \markup \concat {
        \with-color #(x11-color color)
        \abjad-metronome-mark-markup #log #dots #stem #string
        \hspace #0.5
        }
    $music
    #}
    )

baca-metronome-mark-spanner-left-text = #(
    define-music-function
    (parser location log dots stem string music)
    (number? number? number? string? ly:music?)
    #{
    \tweak bound-details.left.text \markup \concat {
        \abjad-metronome-mark-markup #log #dots #stem #string
        \hspace #0.5
        }
    $music
    #}
    )

%%% TEXT SPANNER %%%

baca-text-spanner-left-markup = #(
    define-music-function
    (parser location markup music)
    (markup? ly:music?)
    #{
    \tweak bound-details.left.text \markup \concat {
        \upright #markup \hspace #0.5
        }
    $music
    #}
    )

baca-text-spanner-left-text = #(
    define-music-function
    (parser location string music)
    (string? ly:music?)
    #{
    \tweak bound-details.left.text \markup \concat {
        \upright #string \hspace #0.5
        }
    $music
    #}
    )

baca-text-spanner-right-markup = #(
    define-music-function
    (parser location markup music)
    (markup? ly:music?)
    #{
    \tweak bound-details.right.text \markup \upright #markup
    $music
    #}
    )

baca-text-spanner-right-text = #(
    define-music-function
    (parser location string music)
    (string? ly:music?)
    #{
    \tweak bound-details.right.text \markup \upright #string
    $music
    #}
    )
