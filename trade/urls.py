from . import views
from django.urls import path, include
from .views import AddListing


urlpatterns = [
    path('listings/', AddListing.as_view(), name='add_listing'),
    path('home/', views.ListingList.as_view(), name='home'),
    path('<slug:slug>/', views.ListingDetail.as_view(), name='listing_detail'),
    path('like/<slug:slug>/', views.ListingLike.as_view(), name='listing_like'),
]