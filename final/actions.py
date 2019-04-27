import datetime
import json
import time
from firebase import firebase
from services import relay_helper
from services import ir_helper


class action:
    def __init__(self, id, name, para1,para2):
        self.id=id
        self.name=name
        self.para1=para1
        self.para2=para2

fb = firebase.FirebaseApplication('https://vassist-99157.firebaseio.com/', None)

while(True):
    faction=fb.get('/actions', None)
    for key,val in faction.items():
        print(key,val)
        obj=action(key,str(val['name']),str(val['para1']),str(val['para2']))
        if (obj.name=="i"):
            ir_helper.send_code(obj.para1,obj.para2)
            print("ir")
        elif(obj.name=="s"):
            relay_helper.change_state(obj.para1,obj.para2)
            print("relay")
        fb.delete('/actions', obj.id)
    

    
    print(".")
    time.sleep(30)