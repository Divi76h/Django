from django.http import HttpResponse
from django.shortcuts import render
import googlemaps
import os

GOOGLE_API_KEY = "AIzaSyCC8CkQ5cSJqeGljGyaDq-oUvAn2-au3nM"  # or hardcode temporarily

gmaps = googlemaps.Client(key=GOOGLE_API_KEY)


def index(request):
    return render(request, "index.html")


def js(request):
    return render(request, "auto-js.html")

def raw(request):
    return
