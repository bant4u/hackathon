from django.shortcuts import render, render_to_response

# Create your views here.
def client_form(request):
	print request.user.password
	print request.user.username
	return render(request,'client.html')

def home_page(request):
	return render(request,'/login/')
