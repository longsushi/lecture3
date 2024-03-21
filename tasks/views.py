from django.shortcuts import render
from django import forms#
from django.urls import reverse
from django.http import HttpResponseRedirect

# Create your views here.

class NewTaskForm(forms.Form):
    task = forms.CharField(
        label="",
        widget=forms.TextInput(attrs={'placeholder': 'Aufgabe:'}))
    priority = forms.IntegerField(
        label="<br />",
        widget=forms.TextInput(attrs={'placeholder': 'Priorität:'}),
        min_value = 1, max_value = 5
        )


tasks = [("Müll raus", 1), ("trinken", 2), ("essen", 3)]

def index(request):
    return render(request, "tasks/index.html", {"tasks":tasks})

def add(request):
    if request.method == "POST":
        form = NewTaskForm(request.POST)
        if form.is_valid():
            tasks.append((form.cleaned_data["task"], form.cleaned_data["priority"]))
            return HttpResponseRedirect(reverse("tasks:index"))
        else:
            return render(request, {"form": form})
    return render(request, "tasks/add.html", {"form": NewTaskForm()})
