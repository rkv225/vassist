import pandas as pd 
import numpy as np 
from collections import defaultdict
import pickle
import req_file_nb

def classify(input_text):
    model = pickle.load(open("model_sav_nb.pickle", "rb"))#reloading the pickled model

    clf = model.p_clf
    count_vect = model.p_count_vect

    test_data=[]
    test_data.append(input_text)

    test_data=[req_file_nb.preprocess_string(test_str) for test_str in test_data] #need to preporcess the test set as well!!

    X_test_counts=count_vect.transform(test_data) #transforms test data to numerical form

    #here first check whether the probabilty of naive bayes is sufficiently high then assign 
    #class from 1 to 10 else send to seq model returning class 11

    probability = clf.predict_proba(X_test_counts)
    max_probability = max(probability[0])

    if(max_probability > 0):#replace zero with your threshold value
        predicted_class=clf.predict(X_test_counts)
        ret_class = predicted_class[0]
    else:
        ret_class = 11

    return ret_class