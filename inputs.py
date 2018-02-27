incomeStrig = 'string'

def valueInt(testThisValue):
	try:
		val = int(testThisValue)
		'''print("evaluatedString")'''
	except ValueError:
		print("That's not an int!")
	return testThisValue

def valueDicOrString(testThisValue):
	if isinstance(testThisValue, dict):
		return list(set(testThisValue.values()))
	elif isinstance(testThisValue, str):
		return [testThisValue]
	else:
		return None

print(valueInt(100))

print(valueDicOrString("hello"))