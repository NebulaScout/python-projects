#!python3
# pigLatin2.py - translate the input to pig latin

'''Pig Latin is a silly made-up language that alters English words.\
 If a word begins with a vowel, the word 'yay' is added to the end of it.\
 If a word begins with a consonant or consonant cluster (like ch or gr), that consonant or cluster is moved to the end of the word followed by 'ay'.'''

message = input("Enter a message to translate to pigLatin:\n")

VOWELS = ("a", "e", "i", "o", "u", "y")

pigLatin = [] # Stores the translated words
for word in message.split(): # Convert the message to a list
	# Separates the non-letter characters that are infront of a word
	prefixNonLetters = ""
	while len(word) > 0 and not word[0].isalpha():
		prefixNonLetters += word[0]
		word = word[1: ]
	# Appends the non-letter characters if the word is complete
	if len(word) == 0:
		pigLatin.append(prefixNonLetters)
		continue

	# Separates the non-lettter characters at the end of a word
	suffixNonLetters = ""
	while not word[-1].isalpha():
		suffixNonLetters = word[-1] + suffixNonLetters
		word = word[: -1]

	# checks the original case of the word
	wasUpper = word.isupper()
	wasTitle = word.istitle()

	word = word.lower() # words are changed to lower case for uniformity
	
	# Separates consonants infront of a word
	prefixConsonant = ""
	while len(word) > 0 and not word[0] in VOWELS:
		prefixConsonant += word[0]
		word = word[1: ] 
	
	# Appends 'ay' or 'yay' depending on the met condition
	if prefixConsonant != "":
		word += prefixConsonant + "ay"
	else:
		word += "yay"

	# Converts the word back to its original letter case
	if wasUpper:
		word = word.upper()
	if wasTitle:
		word = word.title()

	pigLatin.append(prefixNonLetters + word + suffixNonLetters)

print(" ".join(pigLatin)) # convert list back to a string
