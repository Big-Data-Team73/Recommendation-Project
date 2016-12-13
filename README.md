# Yelp-Personalized-Recommendation

## LDA
1.Put a the dataset in the LDA folder and run buildmodel.py

2.Only 1000 lda results has been generated and saved in 'outfile'. User pickle to open it and join with the origin bid from the csv dataset. The whole dataset has more than 19000 results.

3.Some words does not make sense because of stemming. Still working on this

4.For classification:
Built the clasification model already but need formatted data for the model input.
Need to convert the pickle list format into the scipy.sparse.csr_matrix.
Need to add the labels for each topic. For example, the data will contain two part. The first part is feature data which means all the key words which belongs to the same topic. The second part is label data which means the topic index. I put the example like below:

feature:                                 
dentist sour dental                    
beautiful pretty cute   

label:
1
2

For the example above, the feature data contains all the key words of the topics as matrix, the labels indicate that the topic #1, topic #2 as arrays.
