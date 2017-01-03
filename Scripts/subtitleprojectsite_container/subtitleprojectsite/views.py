import datetime
from django.http import HttpResponse  
from django.template.loader import get_template
from django.template import Context


def current_datetime(request):
    now = datetime.datetime.now()
    t = get_template('current_datetime.html')
    c = Context({
     'current_date': now,
     'app_name':'subtitle project'
     })
    html = t.render(c)
    return HttpResponse(html)


def hello(request):
    return HttpResponse("Hello world")
          
def hi(request):
    return HttpResponse("Hi there")

def hours_ahead(request, offset):
    offset = int(offset)
    dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
    # assert False
    html = "In %s hour(s), it will be %s." % (offset, dt)
    return HttpResponse(html)
    