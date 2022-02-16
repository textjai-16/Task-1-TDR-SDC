# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
import string

same_words = 0
gases = 10
warnings = 3
letters_guessed = []
count = 0

WORDLIST_FILENAME = "words.txt"

def score(secret_word):
    distinct = set(secret_word)
    return gases * len(distinct)
    

def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist



def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
    
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):
    global count
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    for i in secret_word:
        if i in letters_guessed:
            count += 1
        if count == len(secret_word):
            return True
        else:
            return False



def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    ans_str = ''
    for i in secret_word:
        if i in letters_guessed:
            ans_str += i
        else:
            ans_str += "_ "
    return ans_str



def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    rem_str = ''
    for i in string.ascii_lowercase:
        if i not in letters_guessed:
            rem_str += i
    return rem_str
    
    

def hangman(secret_word):
    global warnings
    global gases
    global letters_guessed
    vowels = 'aeiou'
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!
    
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
    
    Follows the other limitations detailed in the problem write-up.
    '''
    
    print('Welcome to the game Hangman!')
    print('I am thinking of a word that is', len(secret_word), 'letters long.')


    while True:
        
        print('--------------')
        print('You have', gases, 'guesses left.')
        print('Available letters:', get_available_letters(letters_guessed))
        
        letter = input('Please guess a letter: ')

        while letter.isalpha() != True:
            warnings -= 1
            if warnings == -1:
                print('Sorry, you ran out of guesses. The word was ', secret_word, '.', sep = '' )
                return
            print('Oops! That is not a valid letter. You have', warnings, 'warnings left: ', end = '')
            letter = input()

        while letter in letters_guessed:
            warnings -= 1
            if warnings == -1:
                print('Sorry, you ran out of guesses. The word was ', secret_word, '.', sep = '' )
                return 
            print("Oops! You've already guessed that letter. You have", warnings, 'warnings left: ', end = '')
            letter = input()
            
        letters_guessed += letter.lower()

        for i in secret_word:
            r = 0
            if i == letter.lower():
                r += 1
                if r == 1:
                    print('Good guess: ', get_guessed_word(secret_word, letters_guessed))

        if is_word_guessed(secret_word, letters_guessed):
            print('Congratulations, you won!')
            print('Your total score for this game is: ', score(secret_word))
            break

        if letter.lower() not in secret_word:
            print('Oops! That letter is not in my word: ', get_guessed_word(secret_word, letters_guessed))
            if letter.lower() in vowels:
                gases -= 2
            else:
                gases -= 1
        
        if gases == 0:
            print('Sorry, you ran out of guesses. The word was ', secret_word, '.', sep = '' )
            break

        


            
        
    



# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
#(hint: you might want to pick your own
# secret_word while you're doing your own testing)


# -----------------------------------



def match_with_gaps(my_word, other_word):
    global same_words
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the 
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise: 
    '''
    word = ''
    for i in my_word:
        if i == ' ':
            continue
        else:
            word += i
    if len(word) == len(other_word):
        for i in range(len(word)):
            if word[i] != '_':
                if word[i] == other_word[i]:
                    if other_word[i] not in letters_guessed:
                        if i == len(word) - 1:
                            print(other_word, end = ' ')
                            same_words += 1
                            return True
                        else:
                            continue
                    else:
                        continue
                else:
                    return False
            else:
                if i == len(word) - 1:
                    same_words += 1
                    print(other_word, end = ' ')
                    return True
                continue
    else:
        return False

def show_possible_matches(my_word):
    global same_words
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    '''
    for i in wordlist:
        match_with_gaps(my_word, i)
        

    if same_words == 0:
        print('No matches found')
            




def hangman_with_hints(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses
    
    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter
      
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
      
    * If the guess is the symbol *, print out all words in wordlist that
      matches the current guessed word. 
    
    Follows the other limitations detailed in the problem write-up.
    '''
    global warnings
    global gases
    global letters_guessed
    vowels = 'aeiou'

    print('Welcome to the game Hangman!')
    print('I am thinking of a word that is', len(secret_word), 'letters long.')


    while True:
        
        print('--------------')
        print('You have', gases, 'guesses left.')
        print('Available letters:', get_available_letters(letters_guessed))
        
        letter = input('Please guess a letter: ')

        if letter == '*':
            print(get_guessed_word(secret_word, letters_guessed))
            show_possible_matches(get_guessed_word(secret_word, letters_guessed))
            continue

        while letter.isalpha() != True:
            warnings -= 1
            if warnings == -1:
                print('Sorry, you ran out of guesses. The word was ', secret_word, '.', sep = '' )
                return
            print('Oops! That is not a valid letter. You have', warnings, 'warnings left: ', end = '')
            letter = input()

        while letter in letters_guessed:
            warnings -= 1
            if warnings == -1:
                print('Sorry, you ran out of guesses. The word was ', secret_word, '.', sep = '' )
                return 
            print("Oops! You've already guessed that letter. You have", warnings, 'warnings left: ', end = '')
            letter = input()
            
        letters_guessed += letter.lower()

        r = 0
        for i in secret_word:
            if i == letter.lower():
                r += 1
                if r == 1:
                    print('Good guess: ', get_guessed_word(secret_word, letters_guessed))

        if is_word_guessed(secret_word, letters_guessed):
            print('Congratulations, you won!')
            print('Your total score for this game is: ', score(secret_word))
            break

        if letter.lower() not in secret_word:
            print('Oops! That letter is not in my word: ', get_guessed_word(secret_word, letters_guessed))
            if letter.lower() in vowels:
                gases -= 2
            else:
                gases -= 1
        
        if gases == 0:
            print('Sorry, you ran out of guesses. The word was ', secret_word, '.', sep = '' )
            break

        



# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.





if __name__ == "__main__":
    pass
    # pass

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.


    secret_word = choose_word(wordlist)
    print(secret_word)
    hangman(secret_word)

###############
    
    # To test part 3 re-comment out the above lines and 
    # uncomment the following two lines. 
##    
##    secret_word = choose_word(wordlist)
##    hangman_with_hints(secret_word)
