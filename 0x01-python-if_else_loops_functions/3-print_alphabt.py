#!/usr/bin/python3
ascii_val = 97
while ascii_val < 123:
	if (chr(ascii_val) != 'e') & (chr(ascii_val) != 'q'):
		print("{}".format(chr(ascii_val)), end='')
	ascii_val += 1