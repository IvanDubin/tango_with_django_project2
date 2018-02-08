from django.shortcuts import render
from django.http import HttpResponse
from rango.models import Category
from rango.models import Page

def index(request):
    #Construct a dictionary to pass to the template engine its context
	#Note the key boldmessage is the same as {{boldmessage}} in the template!
	
	category_list = Category.objects.order_by('-likes')[:5]
	context_dict = {'categories': category_list}
	response = render(request, 'rango/index.html', context=context_dict)
	
	return response


def about(request):
         return render(request, 'rango/about.html',{})
        


def show_category(request, category_name_slug):
        context_dict= {}

        try:
                category = Category.objects.get(slug=category_name_slug)
                pages = Page.objects.filter(category=category)
                context_dict['pages'] = pages
                context_dict['category'] = category

        except Category.DoesNotExist:
                context_dict['category'] = None
                context_dict['pages'] = None

        return render(request, 'rango/category.html', context_dict)

def add_category(request):
        form = CategoryForm()

        if request.method == 'POST':
                form = CategoryForm(request.POST)

                if form.is_valid():
                        form.save(commit=True)
                        return index(request)
                else:
                        print form.errors

        return render(request, 'rango/add_category.html', {'form': form})
        
        