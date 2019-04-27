import re
import pandas as pd 
import numpy as np 
from collections import defaultdict
import pickle
import req_file_nb
import os

######################### Loading Training Dataset ############################

data = pd.read_csv("raw_data.csv",sep=',')

train_data=data['Command'].values
train_labels=data['Category'].values

train_data=[req_file_nb.preprocess_string(train_str) for train_str in train_data]#data cleaning

from sklearn.feature_extraction.text import CountVectorizer #simply import CountVectorizer
count_vect = CountVectorizer() #instantiate it's object
X_train_counts = count_vect.fit_transform(train_data) #builds a term-document matrix ands return it

from sklearn.naive_bayes import MultinomialNB #importing the Sklearn's NB Fucntionality
clf = MultinomialNB() #simply instantiate a Multinomial Naive Bayes object
clf.fit(X_train_counts, train_labels)  #calling the fit method trains it

model = req_file_nb.Model(clf, count_vect)

print ("Training Completed")

pickle_out=open(os.path.join(os.pardir,"model_sav_nb.pickle"), "wb")

pickle.dump(model, pickle_out)
pickle_out.close()

print ("Model Saved")