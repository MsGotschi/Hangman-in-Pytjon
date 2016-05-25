import random
#will need the random module to generate random numbers
debugwordlist=['red','sunny','aardvark','nice','oblong']
wordlist=['onomatapoeia', 'metaphor', 'catastrophe','computer','programming']

print('welcome to my hangman game\n')

lives = 10

while lives > 0:
	x=random.randint(0,len(debugwordlist))
	word = debugwordlist[x]
	dashes=''
	for i in word
		dashes.append('_ ')
	print('the word you have to guess looks like this:',dashes)
	print('DEBUG: the word is actually', word)
	print('you have', lives, ' guesses left')
	letter=input('guess a letter\n')

	lives = lives -1

print('the game is over')
