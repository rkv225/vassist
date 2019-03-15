from firebase import firebase
import json

fb = firebase.FirebaseApplication('https://vassist-99157.firebaseio.com/', None)

def create(hours, minutes, ap):
    data = {"hours": hours, "minutes": minutes, "ap": ap}
    fb.post('/alarms', data)
    return "alarm set successfully"