from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.views import generic, View
from django.http import HttpResponseRedirect
from .models import Listing
from .forms import CommentForm
from django.views.generic import CreateView, DeleteView, UpdateView

from .forms import ListingForm
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib import messages
from django.urls import reverse_lazy, reverse

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

        price = listing.price
        currency = listing.price

        return render(
            request,
            "listing_detail.html",
            {
                "listing": listing,
                "description": listing.description,
                "comments": comments,
                "commented": False,
                "liked": liked,
                "comment_form": CommentForm(),
                "price": price,
                "currency": currency,
            },
        )

    def post(self, request, slug, *args, **kwargs):
        queryset = Listing.objects.filter(status=1)
        listing = get_object_or_404(queryset, slug=slug)
        comments = listing.comments.filter(approved=True).order_by('created_on')
        liked = False
        if listing.likes.filter(id=self.request.user.id).exists():
            liked = True

        comment_form = CommentForm(data=request.POST)

        if comment_form.is_valid():
            comment_form.instance.email = request.user.email
            comment_form.instance.name = request.user.username
            comment = comment_form.save(commit=False)
            comment.listing = listing
            comment.save()
        else:
            comment_form = CommentForm()

        return render(
            request,
            "listing_detail.html",
            {
                "listing": listing,
                "description": listing.description,
                "comments": comments,
                "commented": True,
                "liked": liked,
                "comment_form": CommentForm()
            },
        )

class ListingLike(View):

    def post(self, request, slug):
        listing = get_object_or_404(Listing, slug=slug)

        if listing.likes.filter(id=request.user.id).exists():
            listing.likes.remove(request.user)
        else:
            listing.likes.add(request.user)

        return HttpResponseRedirect(reverse('listing_detail', args=[slug]))

class AddListing(LoginRequiredMixin, CreateView):
    template_name = 'trade/add_listing.html'
    model = Listing
    form_class = ListingForm
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.instance.seller = self.request.user
        messages.success(self.request, 'Listing created. Waiting for approval.')
        return super(AddListing, self).form_valid(form)

class EditListing(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    template_name = "templates/edit_listing.html"
    model = Listing
    form_class = ListingForm
    success_url = reverse_lazy('home')

    def test_func(self):
        listing = self.get_object()
        return self.request.user == listing.seller

class DeleteListing(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Listing
    success_url = reverse_lazy('home')
    template_name = "templates/listing_confirm_delete.html"

    def test_func(self):
        listing = self.get_object()
        return self.request.user == listing.seller