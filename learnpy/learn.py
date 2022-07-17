from sys import argv

class CustomType:
	def __init__(self, inp):
		self.inp = int(inp)

	def __bool__(self):
		return self.inp > 0

	def __str__(self):
		return 'number is allowed' if self.inp > 0 else 'not allowed'

	def __int__(self):
		return 1 if self.inp > 0 else -1

inp = argv[1]

custom_type = CustomType(inp)

isTrueOrFalse = bool(custom_type)
print(isTrueOrFalse)
 
string = str(custom_type)
print(string)

integer = int(custom_type)
print(integer)
