from django.http import HttpResponse
from django.shortcuts import render
import googlemaps
import os

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
gmaps = googlemaps.Client(key=GOOGLE_API_KEY)


def index(request):
    return render(request, "index.html")


def js(request):
    return render(request, "auto-js.html")

def raw(request):
    return
