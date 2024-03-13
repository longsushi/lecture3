from django.shortcuts import render
import datetime
from django.http import HttpResponse

# Create your views here.


def index(request):
    return render(request, "newyear/index.html", {"newyear":newyear()})


def newyear():
    now = datetime.datetime.now()
    if now.month == 3 and now.day == 12:
        return True
    else:
        return False
