from firebase import firebase
import pyowm

def get_report():
    owm = pyowm.OWM('41eab5d8b70ccc628f23215bcf704b72')  #  API key from openweathermap
    fb = firebase.FirebaseApplication('https://vassist-99157.firebaseio.com/', None)
    profile = fb.get('/profile',None)
    loc = profile['city'] + ',' + profile['country']
    observation = owm.weather_at_place(loc)
    w = observation.get_weather()
    w_status = w.get_detailed_status()
    w_wind = w.get_wind()
    w_wind_speed = int(w_wind['speed'])
    w_temp_all = w.get_temperature('celsius')
    w_temp_cur = int(w_temp_all['temp'])
    output='Currently in ' + profile['city'] + ' its ' + w_status + ' with ' + str(w_temp_cur) + ' degree celsius' + ' and wind speed is ' + str(w_wind_speed) + ' meters per second'
    return output