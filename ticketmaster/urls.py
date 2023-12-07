from django.urls import path, include

import accounts
from . import views
urlpatterns = [
    path('', views.index, name="ticketmaster-base"),
    path('favorites/', views.view_favorites, name="view_favorites"),
    path('add', views.create_favorite, name='create_favorite'),
    path('update/<int:id>', views.update_favorite, name='update_favorite'),
    path('delete/<int:id>', views.delete_favorite, name='delete_favorite'),
]