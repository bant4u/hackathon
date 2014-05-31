import requests
from bs4 import BeautifulSoup
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
	return render(request, "client.html",{'results': results},  {"count" : count })

def google_map(request):
	return render(request,"googleMap.html")

