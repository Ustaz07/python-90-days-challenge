# Hangman game for beginner!!!
# flow chart...................................................
# chatgpt style hangman game flow chart........................

flowchart TD
    A([START]) --> B[Initialize Game\nSelect random word\nSet tries=6]
    B --> C[Display word blanks\nShow guessed letters\nShow tries left]
    C --> D[Player guesses a letter]
    D --> E{Valid input?}
    E -->|No| F[Prompt to try again]
    F --> D
    E -->|Yes| G{Already guessed?}
    G -->|Yes| F
    G -->|No| H[Add to guessed letters]
    H --> I{Letter in word?}
    I -->|No| J[Decrement tries\nUpdate hangman drawing]
    J --> K{Any tries left?}
    K -->|No| M([LOSE])
    I -->|Yes| L[Reveal letter positions]
    L --> N{Word complete?}
    N -->|Yes| O([WIN])
    N -->|No| C
    K -->|Yes| C
    O --> P([END])
    M --> P
