import nltk
#nltk.download('punkt')
from nltk.stem.porter import PorterStemmer

def tokenize(sentence):
	nltk.word_tokenize(sentence)

def stem(word,stemmer):
	return stemmer.stem(word.lower())


def bag_of_words(tokenized_sentence,all_words):
	pass 


if __name__ == '__main__':
	stemmer=PorterStemmer()
	
	test_words=['visualized','visualizing','visualizes']
	stemmed_words=[stem(word,stemmer) for word in test_words]
	print(stemmed_words)
