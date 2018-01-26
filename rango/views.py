from django.shortcuts import render
from django.shortcuts import HttpResponse

def index(request):
	context_dict = {'boldmessage' : "Crunchy, creamy, cookie, candy, cupcake!"}
	return render(request, 'rango/index.html', context=context_dict)