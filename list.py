list = ['7', '5', '3', '10', '45', '0', '16', '51', '22', '97', '34', '87', '78', '91', '4', '7', '2']
searchSymb = input('Введите число, которое хотите найти: ')
print(list.index(searchSymb))
def lineSearch(list, x):
	result = None
	for index, string in enumerate(list):
		print(index, string)
		if string == x:
			result = index
	return result