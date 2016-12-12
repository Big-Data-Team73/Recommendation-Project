import gensim
from gensim import corpora, models

def lda(corpus, dictionary, lines_num=-1):
	i = 0
	ldaList=[]
	for item in corpus:
		ldamodel = gensim.models.ldamodel.LdaModel([corpus[i]], num_topics=3, id2word = dictionary, passes=20)
		print(i)
		ldaList.append(ldamodel.print_topics(num_topics=3, num_words=4))
		print(ldaList[i])
		i = i+1
		if i==lines_num:
			break
	print("LDA finished")
	return ldaList