from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render


# Create your views here.
def index(request: HttpResponse) -> HttpResponse:
    return render(request, "home/index.html")
