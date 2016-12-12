from nltk.tokenize import RegexpTokenizer
from stop_words import get_stop_words
from nltk.stem.porter import PorterStemmer
import gensim
from gensim import corpora, models




def tokenize(dataset, lines_num = -1):
	'''
	:type lines_num: int
	# default set to read all lines in files

	'''	
	tokenizer = RegexpTokenizer(r'[a-zA-Z0-9^\']+')
	i = 0
	testList=[]
	rawList=[]
	bidList=[]
	for line in dataset:
		if i>=1:
			raw = line[23:].lower()
			tokens = tokenizer.tokenize(raw)
			rawList.append(tokens)
			bidList.append(line[:22])
		i+=1
		if i%1000==0:
			print(i)
		if i==lines_num:
			break
	print('tokenization finished')
	return [bidList,rawList]

def stop_words(rawList, lines_num = -1):
	en_stop = get_stop_words('en')
	i=0
	stopped_result=[]
	for item in rawList:
		stopped_tokens = [i for i in item if not i in en_stop]
		stopped_result.append(stopped_tokens)
		i+=1
		if i%1000==0:
			print(i)
		if i==lines_num:
			break
	print('stop words finished')
	return stopped_result

def stem(stopped_result,lines_num=-1):
	p_stemmer = PorterStemmer()
	stem_result=[]
	i=0
	for item in stopped_result:
		texts = [p_stemmer.stem(i) for i in item]
		stem_result.append(texts)
		i+=1
		if i%1000==0:
			print(i)
		if i==lines_num:
			break
	print('stemming finished')
	return stem_result

def doc_term_matrix(processed_data):
	corpusList=[]
	dictionary = corpora.Dictionary(processed_data)
	corpus = [dictionary.doc2bow(text) for text in processed_data]
	return [corpus, dictionary]
	