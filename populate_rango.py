import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tango_with_django_project.settings')

import django
django.setup()
from rango.models import Category, Page

def populate():
    python_pages = [
        {"title": "Official Python Tutorial",
         "url": "http://docs.python.org/2/tutorial/", "views": 32},
        {"title":"How to think like a Computer Scientist",
         "url":"http://www.greenteapress.com/thinkpython/", "views": 31}]

    django_pages = [
        {"title": "Django Rocks",
         "url":"http://www.djangorocks.com/", "views": 30},
        {"title":"How to Tango with Django",
         "url": "http://www.tangowithdjango.com/", "views": 29}
    ]

    other_pages = [
        {"title": "Bottle",
         "url":"http://bottlepy.org/docs/dev/", "views": 28}
    ]

    cats = {"Python": {"pages": python_pages, "views" : 100, "likes" : 20},
            "Django": {"pages": django_pages, "views" : 80, "likes" : 10},
            "Other Frameworks": {"pages": other_pages, "views" : 40, "likes" : 5}}

    for cat, cat_data in cats.items():
        c = add_cat(cat, cat_data["views"], cat_data["likes"])
        for p in cat_data["pages"]:
            add_page(c, p["title"], p["url"], p["views"])


    for c in Category.objects.all():
        for p in Page.objects.filter(category=c):
            print("- {0} - {1}".format(str(c), str(p)))


def add_page(cat, title, url, views=0):
    p = Page.objects.get_or_create(category = cat, title=title)[0]
    p.url=url
    p.views=views
    p.save()
    return p
    


   
def add_cat(name, views=0, likes=0):
    c = Category.objects.get_or_create(name=name)[0]
    c.views = views
    c.likes = likes
    c.save()
    return c
	

if __name__ == '__main__':
    print("Starting Rango population script...")
    populate()
