import requests
from bs4 import BeautifulSoup
<<<<<<< HEAD
=======
import re, datetime
>>>>>>> 186a9af3817ba20b5409fa67799347aec304285e
from django.shortcuts import render, render_to_response

# Create your views here.
def client_form(request):
	print request.user.password
	print request.user.username
	return render(request,'client.html')

def home_page(request):
	return render(request,'/login/')

def rainfall_watch(request):
	html = requests.get("http://hydrology.gov.np/new/bull3/index.php/hydrology/rainfall_watch")
	soup =  BeautifulSoup(html.text)

	trs = soup.find_all(style="background-color:#35d929")

	results = []

	for tr in trs:
		tds = tr.find_all('td')

		result = []

		for i,td in enumerate(tds):
			if td.find('table'):
				pass
			else:
				text1 = td.get_text()
				print text1
				if i == 1:
					result.append(text1)
				elif i == 3:
					result.append(text1)
				elif i == 10:
					result.append(text1)

		if result != []:
			results.append(result)

		count=len(results)
	# print results
	return render(request, "client.html",{'results': results})

def google_map(request):
	return render(request,"googleMap.html")

<<<<<<< HEAD
=======
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
>>>>>>> 186a9af3817ba20b5409fa67799347aec304285e
