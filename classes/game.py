from random_words import RandomWords
from colorama import Fore, Back, Style
from .player import Player
from .message import Message
import states
import pyfiglet

class Game:
	def __init__(self):
		self.word = ''
		self.mask = ''
		self.guesses = list()
		self.guessed = list()
		self.currentState = 0
		self.states = states.states
		self.messenger = Message()
		self.player = Player('')

	def start(self):
		tmp = self.player.name
		self.__init__()
		self.getWord()
		self.printIntro()
		if tmp == '':
			self.getPlayer()
		else:
			self.player.name = tmp
		self.getGuess()

	def getWord(self):
		rw = RandomWords()
		self.word = rw.random_word()
		self.guesses = len(self.word)
		self.currentState = (len(self.states)-1) - self.guesses
		self.buildMask()

	def printIntro(self):
		result = pyfiglet.figlet_format("HANGMAN!")
		self.messenger.output('GREEN', result, True, False, False)
		self.messenger.output('GREEN', 'Welcome to HANGMAN! Your word to guess is below. It is ' + str(len(self.word)) + ' characters long. You have ' + str(self.guesses) + ' guesses. Good luck!', True, False, False)
		self.messenger.output('WHITE', self.states[self.currentState], True, True, False)
		self.messenger.output('BLUE', 'Your word: ' + self.mask, True, True, True)

	def getPlayer(self):
		name = input(Fore.GREEN + 'What\'s your name? ')
		if name != '':
			self.player.name = name
			self.messenger.output('BLUE', 'Welcome, ' + self.player.name + '! Good luck!')

	def buildMask(self):
		tmp = ''
		for i in range(0, len(self.word)):
			tmp += '_'
		self.mask = tmp

	def updateMask(self, pos, char):
		tmp = list(self.mask)
		for i in range (0, len(pos)):
			tmp[pos[i]] = char
		self.mask = "".join(tmp)

	def printMask(self):
		self.messenger.output('BLUE', self.mask + '\n')

	def findGuessInWord(self, guess):
		indexes = list()
		for i  in range(0, len(self.word)):
		    if self.word[i] == guess:
		        indexes.append(i)
		return indexes

	def notifyAlreadyGuessed(self, guess):
		self.messenger.output('RED', 'You already tried ' + guess + '. Please try another. Here is a list of what you\'ve tried so far:')
		self.messenger.output('WHITE', ", ".join(self.guessed) + '\n')

	def guessedCorrect(self, pos, guess):
		self.messenger.output('GREEN', 'Score! You found ' + guess + '! Great job. Keep it up!\n', True, True, True)
		self.updateMask(pos, guess)
		self.printMask()
		self.getGuess()

	def winOrLose(self):
		if self.mask == self.word:
			result = pyfiglet.figlet_format("WINNER!")
			self.messenger.printRule('GREEN')
			self.messenger.output('BLUE', result, True, True, True)
			self.messenger.printRule('GREEN')
		else:
			self.messenger.output('RED', 'Oh shoot! You didn\'t get it this time. The word was: ' + self.word + '\n', True, True, True)

		tryAgain = input('Try again? y/n \n')

		if tryAgain == 'y':
			self.start()
		else:
			exit()

	def updateGuessed(self, guess):
		if guess not in self.guessed:
			self.guessed.append(guess)

	def getGuess(self):
		if self.mask != self.word:
			guess = input('Enter a letter to guess: \n')
			pos = self.findGuessInWord(guess)
			alreadyGuessed = guess in self.guessed

			self.updateGuessed(guess)

			if alreadyGuessed:
				self.notifyAlreadyGuessed(guess)
				self.getGuess()
			else:
				if len(pos) > 0:
					self.guessedCorrect(pos, guess)
				else:
					self.guesses -= 1
					self.currentState += 1
					self.messenger.output('RED', 'Not found! ' + str(self.guesses) + ' guesses left!')
					self.messenger.output('WHITE', self.states[self.currentState])

					if self.guesses > 0 and self.mask != self.word:
						self.printMask()
						self.getGuess()
					else:
						self.winOrLose()
		else:
			self.winOrLose()
