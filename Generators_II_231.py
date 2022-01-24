#Write a program to lazily rewrap text from the filename passed so that it fits an 80 column window without breaking any words. Use a generator that yields the next lines of text, each containing as many words as possible.

import sys
import textwrap
	
def lazy_wrap(char_count):
	def get_file():
		try:
			i = (sys.argv[1])
		except IndexError:
			i = input ("Please enter a file name: ")
		try:
			global item
			item = open (i , "r").read()
		except FileNotFoundError:
			print ("Please try again with a valid file name.")
	get_file()
	global item	
	wrapper = textwrap.TextWrapper(break_long_words = True,replace_whitespace = True,width=char_count)
	final_item = wrapper.fill(item)
	delimiter = ""
	string_item = delimiter.join(map(str, final_item))
	count = 0
	limit = char_count
	while limit <= len (string_item):
		yield string_item.replace('\n','').replace(',','') [count:limit] 
		count += char_count
		limit += char_count

lz = lazy_wrap(80)

print ([next(lz) for lines in range(5)])
