from firebase import firebase
import os

fb = firebase.FirebaseApplication('https://vassist-99157.firebaseio.com/', None)

def get_key(r_name, f_name):
    f_name = f_name.replace(' ','_')
    try:
        key=fb.get('/remotes/' + r_name + '/' + f_name, None)
        return key
    except:
        return False

def send_code(r_name, key):
    print("Sending IR code")
    print(key)
    os.system("irsend SEND_ONCE " + str(r_name) + " " + str(key))