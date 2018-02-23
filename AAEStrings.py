def clean(text):
	if text is None:
		return text
	try:
		ret = text.replace("$", "").replace(",", "")
		return ret
	except InvalidOperation:
		return text

obj = clean_decimal("hello, my name is $ Joe, what do you think")
print(obj)
