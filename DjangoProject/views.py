from django.http import HttpResponse
from django.shortcuts import render
import googlemaps
from django.views.decorators.http import require_GET
from django.http import JsonResponse
import os
from dotenv import load_dotenv

load_dotenv()


GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
gmaps = googlemaps.Client(key=GOOGLE_API_KEY)

def autocomplete(request):
    return render(request, "autocomplete.html")

def test(request):
    return render(request, "test.html")

@require_GET
def autocomplete_address(request):
    query = request.GET.get('query', '')
    results = []

    if query:
        try:
            predictions = gmaps.places_autocomplete(query)
            results = [p['description'] for p in predictions]
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)

    return JsonResponse({'suggestions': results})
