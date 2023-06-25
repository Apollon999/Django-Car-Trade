from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from .models import Listing
from .forms import CommentForm


class ListingList(generic.ListView):
    model = Listing
    queryset = Listing.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'
    paginate_by = 15


class ListingDetail(View):

    def get(self, request, slug, *args, **kwargs):
        queryset = Listing.objects.filter(status=1)
        listing = get_object_or_404(queryset, slug=slug)
        comments = listing.comments.filter(approved=True).order_by('created_on')
        liked = False
        if listing.likes.filter(id=self.request.user.id).exists():
            liked = True

        return render(
            request,
            "listing_detail.html",
            {
                "listing": listing,
                "comments": comments,
                "liked": liked,
                "comment_form": CommentForm()
            },
        )
