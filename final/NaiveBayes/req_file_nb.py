import re

class Model:
    def __init__(self, m, v):
        self.p_clf = m
        self.p_count_vect = v

def preprocess_string(str_arg):
    cleaned_str=re.sub('[^a-z\s]+',' ',str_arg,flags=re.IGNORECASE) #every char except alphabets is replaced
    cleaned_str=re.sub('(\s+)',' ',cleaned_str) #multiple spaces are replaced by single space
    cleaned_str=cleaned_str.lower() #converting the cleaned string to lower case
    return cleaned_str # returning the preprocessed string in tokenized form