from . import views
from django.urls import path, include
from .views import AddListing, DeleteListing, EditListing

urlpatterns = [
    path('', views.ListingList.as_view(), name='home'),
    path('listings/', AddListing.as_view(), name='add_listing'),
  #  path('home/', views.ListingList.as_view(), name='home'),
    path('<slug:slug>/', views.ListingDetail.as_view(), name='listing_detail'),
    path('like/<slug:slug>/', views.ListingLike.as_view(), name='listing_like'),
    path('delete/<int:pk>/', DeleteListing.as_view(template_name='listing_confirm_delete.html'), name='delete_listing'),
    path('edit/<int:pk>/', EditListing.as_view(template_name='edit_listing.html'), name='edit_listing'),
]