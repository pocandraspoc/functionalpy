def clean(text):
	if text is None:
		return text
	try:
		ret = text.replace("$", "").replace(",", "")
		return ret
	except InvalidOperation:
		return text
'''
obj = clean("hello, my name is $ Joe, what do you think")
print(obj)
'''


'''
Because of The None type in clean i tried something out
obj = None
print(type(print(obj)))

What Gave an interesting result:
None
<class 'NoneType'>

SO
the inner print WAS evaluated,
THEN
the outer print got evaluated!
end type of print(None) IS NoneType 

Well lets take a look on 
obj = type(print("a"))
print(obj)

a
<class 'NoneType'>

WooooW,
So type(print(f(x)))
IS NoneType!
'''

