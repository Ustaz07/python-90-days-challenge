# Hangman game for beginner!!!
# problem structre ...........................................
# chatgpt style hangman game algorithm........................
1. secret_word = random word from list
2. guessed_letters = empty list
3. lives = 6
4. WHILE lives > 0:
      a. Display word with blanks/guessed letters
      b. IF no blanks left:
            PRINT "You win!"
            BREAK
      c. guess = input("Guess a letter: ")
      d. IF guess is invalid:
            Ask again
         ELSE IF guess in secret_word:
            Add to guessed_letters
         ELSE:
            lives -= 1
      e. IF lives == 0:
            PRINT "Game over! The word was: secret_word"