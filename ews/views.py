import re,datetime
from django.shortcuts import render, render_to_response
import json
import time

# Create your views here.
def client_form(request):
	farmer_notificantion()
	return render(request,'client.html')

def farmer_notificantion():
	rice = {'avg_rain' :  80, 'min_humidity':60, 'max_humidity':80, 'min_temp':12, 'max_temp':24 }
	maize = {'avg_rain' : 80, 'min_humidity':60, 'max_humidity':80, 'min_temp':12, 'max_temp':24 }
	sugarcane = {'avg_rain' : 80, 'min_humidity':60, 'max_humidity':80, 'min_temp':12, 'max_temp':24 }

	files  =  open('/home/bijay/hackathon/hackathon/ews/sample_rain_data.json')
	data = json.load(files)

	for i, x in enumerate(data):
		if i%3:
			from_date = x['date']
			conv = time.strptime(from_date, "%y-%m-%r")
			print time.strftime("")
			d=datetime.datetime(*map(int, re.split('[^\d]', s)[:-1]))



