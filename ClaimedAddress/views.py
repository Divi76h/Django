from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
import json
from .models import ClaimedAddress

@csrf_exempt
@login_required(login_url='/users/login/')
def claim_address(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        address = data.get('address')

        if not address:
            return JsonResponse({'error': 'Address is required'}, status=400)

        # Avoid duplicate claims
        ClaimedAddress.objects.get_or_create(user=request.user, address=address)

        return JsonResponse({'message': f'Address "{address}" claimed successfully'})
    return None

@login_required(login_url='/users/login/')
def saved_addresses(request):
    addresses = ClaimedAddress.objects.filter(user=request.user)
    return render(request, 'saved.html', {'addresses': addresses})