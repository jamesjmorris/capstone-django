from django.urls import path
from . import views

urlpatterns = [
    path('events/', views.EventList.as_view(), name='event-list'),
    path('events/<int:pk>/', views.EventDetail.as_view(), name='event-detail'),
    path('donations/', views.DonationList.as_view(), name='donation-list'),
    path('donations/<int:pk>/', views.DonationDetail.as_view(), name='donation-detail'),
]