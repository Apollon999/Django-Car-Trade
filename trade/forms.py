from .models import Comment
from django import forms
from .models import Listing


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields =('body',)

class ListingForm(forms.ModelForm):
