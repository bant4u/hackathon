import requests
from bs4 import BeautifulSoup
from django.shortcuts import render, render_to_response, HttpResponse, HttpResponseRedirect
from django.core.mail import send_mail
import json
import datetime
import calendar


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

	updated_at = soup.find(id='date_time').get_text()

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
					print text1
					if text1 != "Below Warning Level":
						send_email()
					result.append(text1)

		if result != []:
			results.append(result)

		count=len(results)
	# print results
	return render(request, "client.html",{'results': results, 'updated_at': updated_at})


def google_map(request):
	return render(request,"googleMap.html")



def farmer_notification(request):
	#required parameters for various crop
	#rice = {'avg_rain' :  80, 'min_humidity':60, 'max_humidity':80, 'min_temp':12, 'max_temp':24 }
	maize = {'avg_rain' : 80, 'min_humidity':60, 'max_humidity':80, 'min_temp':12, 'max_temp':24 }
	sugarcane = {'avg_rain' : 80, 'min_humidity':60, 'max_humidity':80, 'min_temp':12, 'max_temp':24 }

	#calculated temperature varying
	crops = [{'crop': 'Rice/Paddy','start_month': 6, 'end_month':7 ,'avg_rain' :  80, 'min_humidity':60, 'max_humidity':80, 'min_temp':12, 'max_temp':45, 'date':'2014-07-01' },
			{'crop': 'Maize','start_month': 6, 'end_month':7 ,'avg_rain' :  80, 'min_humidity':60, 'max_humidity':80, 'min_temp':12, 'max_temp':45, 'date':'2014-07-01' },
			{'crop': 'Wheat','start_month': 3, 'end_month':4 ,'avg_rain' :  80, 'min_humidity':60, 'max_humidity':80, 'min_temp':12, 'max_temp':45, 'date':'2014-07-01' },
		]

	files = open('sample_rain_data.json')
	data = json.load(files)
	for crop in crops:
		for i, x in enumerate(data):
			if i%3 == 0:
				string_date = x['date']
				date = datetime.datetime.strptime(string_date, "%Y-%m-%d %H:%M:%S")
				if date.month == crop['start_month'] or date.month==crop['end_month']:
					crop['message'] = "Nice time to cultivate"
					break

	return render(request, 'farmer.html', {"crops": crops} )


def send_email(request):
	sender = "krishna.poudel19@gmail.com"

	emailto = request.POST['emailto']
	subject = request.POST['subject']
	message = request.POST['message']

	print emailto

	#Send the mail
	send_mail(subject, message, sender, (emailto,), fail_silently=False)
	return HttpResponseRedirect('/')
