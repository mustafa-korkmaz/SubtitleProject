from django.http import HttpResponse  
import datetime

def hello(request):
    return HttpResponse("Hello world")
          
def hi(request):
    return HttpResponse("Hi there")

def current_datetime(request):
    now=datetime.datetime.now()
    html=" now it is %s" %now
    return HttpResponse(html)

def hours_ahead(request, offset):
    offset = int(offset)
    dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
    # assert False
    html = "In %s hour(s), it will be %s." % (offset, dt)
    return HttpResponse(html)
    