from django.shortcuts import render

# Create your views here.

tasks = [("Müll raus", 1), ("trinken", 2), ("essen", 3)]

def index(request):
    return render(request, "tasks/index.html", {"tasks":tasks})

def add(request):
    return render(reqeust, "tasks/add.html")
