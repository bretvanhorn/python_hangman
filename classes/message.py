from colorama import Fore, Back, Style

class Message:

	def __init__(self):
		pass

	def output (self, color, message, resetStyle = True, beforeRule = False, afterRule = False):
		c = self.setColor(color)
		if beforeRule:
			self.printRule(c)

		print(c + message)

		if afterRule:
			self.printRule(c)

		self.resetStyles()

	def printRule(self, color):
		print(self.setColor(color) + '------------------------------------------------------------------')

	def resetStyles(self):
		print(Style.RESET_ALL)

	def setColor(self, color):
		if color == 'GREEN':
			return Fore.GREEN
		elif color == 'RED':
			return Fore.RED
		elif color == 'BLUE':
			return Fore.BLUE
		else:
			return Fore.WHITE
