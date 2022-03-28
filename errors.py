# Define exceptions for telegram chat-bot application

class Err(Exception):
	'''Base class for other user-defined exceptions 
	'''
	pass

class MenuEntryLevelError(Err):
	'''Raised when the application can not correctly parse a level
	of menu entry passed to menu constructor. 
	'''
	def __init__(self, lvl: str):
		msg: str = '''The first line of each menu entry must begin \
 from its hierarchical level represented by digits and periods, \
 and be separated from the rest of the line by a space .'''
		self.lvl = lvl
		self.msg = msg
		super().__init__(self.msg)
	
	def __str__(self):
		return f'{self.lvl} -> {self.msg}'


class DuplicateMenuEntryError(Err):
	'''Raised when a menu entry of the same level has been added to the menu earlier
	'''
	def __init__(self, lvl: str):
		self.lvl: str = lvl
		self.msg: str = f'A menu entry of the same level {self.lvl} has been added earlier.'
		super().__init__(self.msg)
	
	def __str__(self):
		return self.msg


