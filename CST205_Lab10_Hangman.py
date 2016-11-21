# Kyle Luoma and Shannon Davis
# CSUMB CST 205 Multimedia programming module 2
# Lab # 10: Manipulating Strings and Hangman

# ----- Warm Up -----

def warmUp():
  input = ""
  while not input == "stop":
    input = requestString("Enter a word. Type \"stop\" to exit the program.")
    printNow(input)

# ----- Hangman -----

import random

def main():
  random.seed()
  
# Main game loop. Runs until the quit boolean is made true.
  
  # Variables:
  quit = false
  wordLength = 7
  guesses = 6
  round = 1
  answer = pickWord(wordLength)
  mask = makeMask(len(answer), answer)
  correct = false
  welcomeMessage = """Welcome to hangman, the exciting game of letter guessing. You have six chances to guess the 
                      word I select before the man is hanged!"""
  
  incorrectGuesses = ""
  
  # Splash
  print(welcomeMessage)
  
  while not quit:
    # View
    header = "\n\n\n\n\n*************** HANGMAN Round " + str(round) + " ***************"
    print(header)
    print("Word so far:")
    printMask(mask)
    print("Incorrect guesses:\n" + incorrectGuesses + "\nYou have used " + str(6 - guesses) + " of six guesses")
    
    # Input
    gamePrompt = "Guess a letter by entering a character below\n You have " + str(guesses) + " guesses remaining.\n"
    guess = requestString(gamePrompt).lower()
    valid = validateInput(guess, incorrectGuesses)
    
    # Logic
    round += 1
    
    if valid:
      correct = checkGuess(guess, answer)
      
    if valid and correct:
      mask = updateMask(guess, mask, answer)
      print("Correct!")
    elif valid and not correct:
      guesses -= 1
      incorrectGuesses += guess
      print("Incorrect!")
      
    if mask == answer:
      printMask(mask)
      print("Congratulations you win!")
      quit = true

    if guesses == 0:
      print("Sorry, you lose. Better luck next time!")
      quit = true
      
      
    
def pickWord(wordLength):
# This function selects a game word from a list and returns
# a word of requested length
  wordList = None
  
  #Set word variable to a string to override word selection process
  word = None
  wordList = None

  sevenLetterWords = [ "zombies", \
                       "zooming", \
                       "pickups", \
                       "perplex", \
                       "cutback" ]
  
  sixLetterWords = [ "puzzle", \
                     "jumped", \
                     "jumble", \
                     "mixing", \
                     "frozen" ]
                     
  fiveLetterWords = [ "crazy", \
                      "jazzy", \
                      "jacks", \
                      "quack", \
                      "jammy" ]
                      
  if wordLength == 7:
    wordList = sevenLetterWords
  elif wordLength == 6:
    wordList = sixLetterWords
  elif wordLength == 5:
    wordList = fiveLetterWords
    
  if wordList != None and word == None:
    word = wordList[random.randrange(len(wordList))]

  return word
  
  
def makeMask(wordLength, answer):
# Creates a mask of underscore characters of a given length
# It should look like "______"
  mask = ""
  for i in range (0, wordLength):
    if answer[i] == " ":
      mask = mask + " "
    else:
      mask = mask + "_"
  return mask


def printMask(mask):
  #Prints the mask to the screen
  tempString = ""
  for char in mask:
    tempString += (char + " ")
  print tempString


def updateMask(guess, mask, answer):
# Checks the guess against the word and updates the mask
  for i in range(0, len(answer)):
    if guess == answer[i]:
      if i == 0:
        mask = guess + mask[1:len(mask)]
      else:
        mask = mask[0:i] + guess + mask[i + 1:len(mask)]
  return mask
  

def checkGuess(guess, answer):
# Checks if the user entered the correct letter
  correct = false
  if guess in answer:
    return true
  else:
    return false
    

def validateInput(guess, incorrectGuesses):
# Input validation function makes sure alpha character entered, guess not already guessed and 
# that the user entered a character.
  valid = true
  alreadyGuessed = false
  
  alreadyGuessed = guess in incorrectGuesses
  
  if not guess.isalpha():
    print("Letters only please!\n")
    valid = false
  
  if alreadyGuessed and len(guess) > 0:
    print("You already guessed the letter " + guess + ". Please enter a different letter.")
    valid = false
    
  if len(guess) == 0:
    print("Please enter a letter.")
    valid = false
    
  if len(guess) > 1:
    print("Please enter only one letter at a time.")
    valid = false
      
  return valid
  