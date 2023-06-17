from django.contrib import admin
from .models import Listing
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Listing)
class ListingAdmin(SummernoteModelAdmin):

    summernote_fields = ('description')

