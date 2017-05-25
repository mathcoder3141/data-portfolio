#Randall Hall
#A Python program to translate English to Pig Latin


# below English --> Pig Latin
sentence = input('Enter a sentence in English:')
word = sentence.split()
word_count = len(word)

print ("There are {} words in this sentence".format(word_count))

vowel = 'a', 'e', 'i', 'o', 'u'
pcg = 'ay'
pvg = 'way'

for word in sentence.split():
	
	if  word.startswith(vowel):
		print ("{} --> {}{}".format(word, word, pvg))

	elif len(word) > 0 and word.isalpha():
		new_word = word[1:len(word)]
		first = word[0]
		new_word = new_word + first + pcg
		print ("{} --> {}".format(word, new_word))
	else:
		print("Input is not valid")
