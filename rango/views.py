from django.shortcuts import render
from django.shortcuts import HttpResponse
from rango.models import Category 
from rango.models import Page
def index(request): 
	# Query the database for a list of ALL categories currently stored. 
	# Order the categories by no. likes in descending order. 
	# Retrieve the top 5 only - or all if less than 5. 
	# Place the list in our context_dict dictionary 
	# that will be passed to the template engine.
	category_list = Category.objects.order_by('-likes')[:5]
	context_dict = {'categories': category_list}
	for category in category_list:
		category.url = category.name.replace(' ', '_')
	# Render the response and send it back! 
	return render(request, 'rango/index.html', context_dict)

