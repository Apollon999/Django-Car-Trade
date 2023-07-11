from . import views
from django.urls import path, include
from .views import AddListing, DeleteListing


urlpatterns = [
    path('', views.ListingList.as_view(), name='home'),
    path('listings/', AddListing.as_view(), name='add_listing'),
  #  path('home/', views.ListingList.as_view(), name='home'),
    path('<slug:slug>/', views.ListingDetail.as_view(), name='listing_detail'),
    path('like/<slug:slug>/', views.ListingLike.as_view(), name='listing_like'),
    path('delete/<slug:slug>/', DeleteListing.as_view(), name='delete_listing'),
]