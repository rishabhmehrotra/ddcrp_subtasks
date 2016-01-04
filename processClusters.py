import gensim, nltk, sklearn, pickle, sys, string, collections
from gensim.models import word2vec
from sklearn.cluster import KMeans
from ast import literal_eval
from nltk import word_tokenize
from nltk.stem import PorterStemmer
from nltk.corpus import stopwords
import numpy as np

ii = 1
queries = []
filee = "data/"+str(ii)+".allQueries.freq.nUsers.txt"
with open(filee) as infile:
	for line in infile:
		query = line.split("\t")[0]
		queries.append(query)
cmap = {"":[]}
c=0
filee = "data/"+str(ii)+".cluster.txt"
with open(filee) as infile:
	for line in infile:
		c+=1
		if c%1000==0:
			print c
		q = line.split(" ")
		cl = int(q[1])
		idx = int(q[0])
		if cl in cmap:
			qlist = cmap[cl]
			qlist.append(queries[idx])
			cmap[cl] = qlist
		else:
			qlist = [queries[idx]]
			cmap[cl] = qlist

fileout = "data/"+str(ii)+".viewCluster.txt"
oFile = open(fileout, 'w')
for (k,v) in cmap.items():
	oFile.write(str(k)+"\t"+str(cmap[k])+"\n")
oFile.close()





