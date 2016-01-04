import gensim, nltk, sklearn, pickle, sys, string, collections
from gensim.models import word2vec
from sklearn.cluster import KMeans
from ast import literal_eval
from nltk import word_tokenize
from nltk.stem import PorterStemmer
from nltk.corpus import stopwords
import numpy as np

allQ = []
ii1 = 6
while ii1>0:
	c=0;
	queries = []
	filee = "data/"+str(ii1)+".allQueries.freq.nUsers.txt"
	with open(filee) as infile:
		for line in infile:
			c+=1
			if c%1000==0:
				print c
			q = line.split("\t")[0]
			q = q.translate(None, string.punctuation)
			queries.append(q)

	size = len(queries)
	str1 = ""
	for ii in range(0,size/4):
		str1 = str1 + queries[ii]
	allQ.append(str1)
	str1 = ""
	for ii in range(size/4,2*size/4):
		str1 = str1 + queries[ii]
	allQ.append(str1)
	str1 = ""
	for ii in range(2*size/4,3*size/4):
		str1 = str1 + queries[ii]
	allQ.append(str1)
	str1 = ""
	for ii in range(3*size/4,4*size/4):
		str1 = str1 + queries[ii]
	allQ.append(str1)
	ii1-=1
print len(allQ)
size = len(allQ)
fileout = "data/allTasks.queries.freq.nUsers.txt"
oFile = open(fileout, 'w')
for ii in range(0,size):
	oFile.write(allQ[ii]+"\t0\t0"+"\n")
oFile.close()