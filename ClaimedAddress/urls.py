from django.urls import path
from . import views

app_name = "ClaimedAddress"

urlpatterns = [
    path('claim/', views.claim_address, name='claim_address'),
    path('saved/', views.saved_addresses, name='saved_addresses'),
    path('unclaim/<int:id>/', views.unclaim_address, name='unclaim_address'),
]
