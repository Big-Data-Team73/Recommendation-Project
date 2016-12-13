from sklearn.naive_bayes import MultinomialNB
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_extraction.text import CountVectorizer
import numpy as np
import pickle
outfile = pickle.load(open('outfile',"rb"))
print(type(outfile))
print(outfile[2])
# Need to convert pickle file into tfidf format, with all the keywords to be features, all the topics to be topics (being represented with 1,2,3 is OK)
# Train_feature = 
# Train_topic = 
# Test_feature =
# Test_topic = 

# count_vect = CountVectorizer()
# X_train_counts = count_vect.fit_transform(outfile)
# count_vect.vocabulary_.get(u'algorithm')

# tfidf_transformer = TfidfTransformer()
# Train_feature = tfidf_transformer.fit_transform(X_train_counts)
Train_feature = outfile
print(len(Train_feature))
Train_topic = np.zeros(shape=(1000,1))
clf = MultinomialNB().fit(Train_feature, Train_topic)


# predicted = clf.predict(Test_topic)

# for doc, category in zip(Test_topic, predicted):
# 	print('%r => %s' % (doc, predicted.target_names[category]))

