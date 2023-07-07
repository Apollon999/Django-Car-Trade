from .models import Comment
from django import forms
from djrichtextfield.widgets import RichTextWidget
from .models import Listing



class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields =('body',)

class ListingForm(forms.ModelForm):
    class Meta:
        model = Listing
        fields = ['title', 'seller', 'price', 'currency', 'engine', 'fuel', 'year', 'description', 'featured_image',]

        engine = forms.CharField(widget=RichTextWidget())
        fuel = forms.CharField(widget=RichTextWidget())

        widget = {
            'description': forms.Textarea(attrs={'rows': 5}),
        }

        labels = {
            'title': 'Listing Title',
            'description': 'Description',
            'seller': 'Seller',
            'price': 'Listing Price',
            'currency': 'Currency',
            'engine': 'Vehicle Engine',
            'fuel': 'Fuel',
            'year': 'Production Year',
            'featured_image': 'Vehicle Image',
        }


