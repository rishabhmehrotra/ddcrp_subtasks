import gensim, nltk, sklearn, pickle, sys, string, collections
from gensim.models import word2vec
from sklearn.cluster import KMeans
from ast import literal_eval
from nltk import word_tokenize
from nltk.stem import PorterStemmer
from nltk.corpus import stopwords
import numpy as np

ii = 1
queries = [" "]

filee = "data/"+str(ii)+".allQueries.freq.nUsers.txt"
with open(filee) as infile:
	for line in infile:
		query = line.split("\t")[0]
		queries.append(query)
size = len(queries)+1
distances = np.full((size,size),float(-1))
i=0;j=0;
filee = "data/"+str(ii)+".distances.txt"
with open(filee) as infile:
	for line in infile:
		row = line.strip().split(' ')
		for v in row:
			distances[i][j] = float(row[j])
			j+=1
		j=0;i+=1

cmap = {"":[]}
cmap1 = {"":""}
custmap = {"":[]}
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
		cust = int(q[2])
		custmap[idx] = cust
		print ("%d %d %f"%(idx,cust,distances[idx+1][cust+1]))
		if cl in cmap1:
			qlist = cmap[cl]
			qliststr = cmap1[cl]
			qliststr += (str(queries[idx])+"("+str(idx)+") ")
			qlist.append(queries[idx])
			cmap[cl] = qlist
			cmap1[cl] = qliststr
		else:
			qlist = [queries[idx]]
			qliststr = str(queries[idx])+"("+str(idx)+") "
			cmap[cl] = qlist
			cmap1[cl] = qliststr

fileout = "data/"+str(ii)+".viewCluster.txt"
oFile = open(fileout, 'w')
for (k,v) in cmap.items():
	oFile.write(str(k)+"\t"+str(cmap1[k])+"\n")
oFile.close()





