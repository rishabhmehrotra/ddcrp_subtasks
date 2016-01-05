import gensim, nltk, sklearn, pickle, sys, string, collections
from gensim.models import word2vec
from sklearn.cluster import KMeans
from ast import literal_eval
from nltk import word_tokenize
from nltk.stem import PorterStemmer
from nltk.corpus import stopwords
import numpy as np
import json
from scipy import spatial


print sklearn.__version__

#model = gensim.models.word2vec.Word2Vec.load_word2vec_format('../entity/GoogleNews-vectors-negative300.bin', binary=True)

def distance(e1, e2):
	return spatial.distance.cosine(e1,e2)


ii = 6
while ii>=0:
	print (ii)
	c=0;
	queries = []
	embeddings = []
	filee = "data/"+str(ii)+".allQueries.freq.nUsers.txt"
	#filee = "data/allTasks.queries.freq.nUsers.txt"
	with open(filee) as infile:
		for line in infile:
			c+=1
			if c%1000==0:
				print c
			q = line.split("\t")[0]
			q = q.translate(None, string.punctuation)
			queries.append(q)
	#now for each query, get the word2vec representation
	'''
	#this part uses the word2vec embeddings to find representations of the queries & saves it to file
	for q in queries:
		text = q.translate(None, string.punctuation)
		tokens = word_tokenize(text)
		#print "No of tokens in query%s: %d"%(q,len(tokens))
		tt = 1
		error=0
		vec = [0]*300
		for t in tokens:
			try:
				#print "finding representation for %s"%t
				vect = model[t]
				vec = np.add(vec, vect)
				tt+=1
			except:
				#print "or"
				error+=1
		if tt>1:
			tt-=1
		vec = [v/tt for v in vec]
		embeddings.append(vec)
	'''
	file2 = "data/embeddings/"+str(ii)+".vectors.txt"
	'''
	with open(file2,'w') as myfile:
		json.dump(embeddings,myfile)
	'''
	# this part re-uses the query word2vec embeddings by loading them from the file and computes Q-Q distances & saves it to file
	with open(file2,'r') as infile:
		embeddings = json.load(infile)
	#print embeddings
	
	print ("No of queries: %d"%len(queries))
	print ("No of embeddings: %d"%len(embeddings))
	print("finding distances now")
	size = len(embeddings)
	distances = np.full((size,size),float(100))
	for i in range(0,size):
		if i%100 == 0:
			print i
		q1 = queries[i]
		e1 = embeddings[i]
		distances[i][i]=0
		#for j in range(i+1,size):
		for j in range(0,i):
			q2 = queries[j]
			e2 = embeddings[j]
			dist = distance(e1,e2)
			distances[i][j]=dist
			distances[j][i]=dist
	print "ending distance computations"
	fileout = "data/"+str(ii)+".distances.embeddings.txt"
	oFile = open(fileout, 'w')
	print "size of matrix: %d"%size
	for i in range(0,size):
		for j in range(0,size):
			oFile.write(str(distances[i][j])+" ")
		oFile.write("\n")
	oFile.close()
	ii-=1

