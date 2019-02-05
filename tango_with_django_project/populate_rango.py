import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','tango_with_django_project.settings')

import django
django.setup()
from rango.models import Category, Page

def populate():

    python_pages = [
            {"title":"Official python tutorial",
                "url":"http://docs.python.org/2/tutorial/",
                "views":"67"},
            {"title":"how to think like a computer scientist",
                "url":"http://www.greenteapress.com/thinkpython/",
                "views":"66"},
            {"title":"learn python in 10 minutes",
                "url":"http://www/korokithakis.net/tutorials/python/",
                "views":"68"}]
    
    django_pages = [
            {"title":"official django tutorial",
                "url":"https//docs.djangoproject.com/en/1.9/intro/tutorial01/",
                "views":"10"},
            {"title":"django rocks",
                "url":"http://www.djangorocks.com/",
                "views":"15"},
            {"title":"how to tango with django",
                "url":"http://www.tangowithdjango.com/",
                "views":"20"}]

    other_pages = [
            {"title":"bottle",
                "url":"http://bottlepy.org/docs/dev/",
                "views":"49"},
            {"title":"flask",
                "url":"http://flask.pocoo.org",
                "views":"29"}]

    cats = {"python": {"pages": python_pages, "views":'128', "likes":'64'},
            "django": {"pages": django_pages, "views":'64', "likes": '32'},
            "other frameworks": {"pages": other_pages, "views":'32', "likes":'16'}}

    for cat, cat_data in cats.items():
        c = add_cat(cat, cat_data["views"], cat_data["likes"])
        for p in cat_data["pages"]:
            add_page(c, p["title"], p["url"], p["views"])

    for c in Category.objects.all():
        for p in Page.objects.filter(category=c):
            print("- {0} -{1}".format(str(c), str(p)))
          
def add_page(cat, title, url, views):
    p = Page.objects.get_or_create(category=cat, title=title)[0]
    p.url = url
    p.views = views
    p.save()
    return p

def add_cat(name, views, likes):
    c = Category.objects.get_or_create(name=name)[0]
    c.views = views
    c.likes = likes
    c.save()
    print(c)
    print(Category.objects.get_or_create(name=name))
    return c

if __name__ == '__main__':
    print("Strating Rango population script...")
    populate()
