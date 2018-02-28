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

def test_Int(self):
    self.assertTrue(type(self) is int)
    self.assertIs(type(self), int)
    self.assertIsInstance(self, int)

inp = 11
print(test_Int(inp))
print(valueInt(100))
print(valueDicOrString("hello"))
print(dict(["he"]))

print(None == None)
print(type(type(None)))