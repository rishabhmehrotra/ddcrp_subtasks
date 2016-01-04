import gensim, nltk, sklearn, pickle, sys, string, collections
from gensim.models import word2vec
from sklearn.cluster import KMeans
from ast import literal_eval
from nltk import word_tokenize
from nltk.stem import PorterStemmer
from nltk.corpus import stopwords
import numpy as np

print sklearn.__version__

#model = gensim.models.word2vec.Word2Vec.load_word2vec_format('../../entity/GoogleNews-vectors-negative300.bin', binary=True)

def distance(str1, str2):
	words1 = str1.lower().split()
	words2 = str2.lower().split()
	common = set(words1) & set(words2)
	return len(common)

ii = 1
while ii>0:
	c=0;
	queries = []
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

	print len(queries)
	size = len(queries)
	distances = np.full((size,size),float(-1))
	#print distances
	print "starting distance computations"
	for i in range(0,size):
		if i%100 == 0:
			print i
		q1 = queries[i]
		distances[i][i]=0
		#for j in range(i+1,size):
		for j in range(0,i):
			q2 = queries[j]
			dist = distance(q1,q2)
			distances[i][j]=dist
			distances[j][i]=dist
			#if i%100==0 and j%100==0:
			#	print "str1: %s\nstr2: %s\ndist= %d"%(q1,q2,dist)
	
	for i in range(0, size):
		if i%100 == 0:
			print i
		maxd = 0
		for j in range(0,i):
			if distances[i][j]>maxd and distances[i][j]<10000:
				maxd = distances[i][j]
				#print ("distance = %f"%distances[i][j])
			#print ("maxd = %f"%maxd)
		for j in range(0,i):
			if distances[i][j]<10000:
				if maxd<10000 and maxd>0:
					#print("111111")
					distances[i][j] = 100*(1-distances[i][j]/maxd)
					distances[j][i] = distances[i][j]
				if maxd == 0:
					#print("222222")
					distances[i][j] = 200
					distances[j][i] = 200
	
	print "ending distance computations"
	i=0
	fileout = "data/"+str(ii)+".distances.txt"
	#fileout = "data/allTasks.distances.txt"
	oFile = open(fileout, 'w')
	print "size of matrix: %d"%size
	for i in range(0,size):
		for j in range(0,size):
			oFile.write(str(distances[i][j])+" ")
		oFile.write("\n")
	oFile.close()
	ii-=1



