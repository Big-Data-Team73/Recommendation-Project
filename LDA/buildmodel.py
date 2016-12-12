from preprocess import tokenize,stop_words,stem,doc_term_matrix
from lda import lda
import pickle




def build_model(lines_num = -1):
	dataset = open('rawdata.csv', 'r')

	[bidList,rawList]=tokenize(dataset,lines_num)

	stopped_result = stop_words(rawList,lines_num)

	stem_result = stem(stopped_result,lines_num)

	[corpus,dictionary] = doc_term_matrix(stem_result)
	# it seems like without stem the words makes more sense, still working on it
	
	################
	####  LDA  #####
	################
	ldaList = lda(corpus, dictionary,lines_num)
	
	print("load data...")
	
	with open('outfile','wb') as fp:
		pickle.dump(ldaList,fp)

if __name__ == '__main__':
	build_model(1000)
