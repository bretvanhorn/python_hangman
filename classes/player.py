class Player:

	def __init__(self, name):
		self.name = ''
		self.wins = 0
		self.losses = 0

	def getName(self):
		return self.name

	def incrementWins(self):
		self.wins += 1

	def incrementLosses(self):
    		self.losses += 1

