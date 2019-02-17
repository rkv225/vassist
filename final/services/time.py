from datetime import datetime

def tell():
    return "The time is " + datetime.strftime(datetime.now(), '%H:%M:%S')    