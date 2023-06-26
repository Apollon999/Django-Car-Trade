from . import views
from django.urls import path


urlpatterns = [
    path('', views.ListingList.as_view(), name='home'),
    path('<slug:slug>/', views.ListingDetail.as_view(), name='listing_detail'),
    path('like/<slug:slug>', views.ListingLike.as_view(), name='listing_like'),
]