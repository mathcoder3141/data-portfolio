#Randall Hall
#A Python program to translate Pig Latin to English while ignoring words that are not in Pig Latin

#Pig Latin --> English

sentence = input('Enter a sentence in Pig Latin: ')
word = sentence.split()
word_count = len(word)

print("There are %s words in this sentence" % (word_count))

vowel = 'a', 'e', 'i', 'o', 'u'
pcg = 'ay'
pvg = 'way'

for word in sentence.split():
	
	if pvg in word and word != pvg:
		new_word2 = word[0:-3]
		print ("%s --> %s" % (word, new_word2))
	
	elif pcg in word and word != pcg:
		new_word = word[0:-3]
		first = word[-3]
		new_word = first + new_word
		print ("%s --> %s" % (word, new_word))
