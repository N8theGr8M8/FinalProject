from django.urls import path
from . import views
urlpatterns = [
    path('ticketmaster/', views.index, name="ticketmaster-base"),
    path('eventlist/', views.lister, name="ticketmaster-list"),
    #path('ticketmaster/', views.index, name="ticketmaster-index")
]