from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

STATUS = ((0, "Draft"), (1, "Published"))

#Defining the structure and attributes of the Listing model.
class Listing(models.Model): 
    
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=200, unique=True)
    seller = models.ForeignKey(User, on_delete=models.CASCADE, related_name="trade_listings")
    updated_on = models.DateTimeField(auto_now=True)
    description = models.TextField()
    featured_image = CloudinaryField('image', default='placeholder')
    excerpt = models.TextField(blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    likes = models.ManyToManyField(User, related_name='trade_likes', blank=True)

    # Deciding a descending order to each listing on the feed.
    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title

    # Calculates and returns number of likes on each listing.
    def number_of_likes(self):
        return self.likes.count()

# Defining the structure and attributes for the Comment model.
class Comment(models.Model):

    listing = models.ForeignKey(Listing, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    # Customizes and controls how the Comment model will be displayed.
    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return f"comment {self.body} by {self.name}"



