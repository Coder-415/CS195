#write a program only one statement long (it can span multiple lines) that prints the number of palindromes in /users/abrick/resources/english

list_of_palindromes = list(filter(lambda word: word == word [::-1], open("/users/abrick/resources/english","r").read().splitlines()))

filtered_list = list(filter(lambda word: len (word) > 1, list_of_palindromes))

print('\n',"This is the number of palindromes in the file:", len(list_of_palindromes))
print('\n', "These are the palindromes in the file:\n",list_of_palindromes,'\n')

print('\n',"If one does not count single characters as palindromes, this is the number of palindromes in the file:", len(filtered_list))
print ('\n', "If one does not count single characters as palindromes, these are the palindromes in the file:\n", filtered_list,'\n')
