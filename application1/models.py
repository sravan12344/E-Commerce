from django.db import models
from datetime import datetime
from ckeditor.fields import RichTextField

# models.py
from django.db import models
from django.contrib.auth.models import User

class WishlistItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    course_name = models.CharField(max_length=255)
    added_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username}'s Wishlist: {self.course_name}"


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Product(models.Model):
    image = models.ImageField(null=False, blank=False)
    name = models.CharField(max_length=200, null=False, blank=False)
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, default=True, null=False
    )
    price = models.DecimalField(max_digits=5, decimal_places=2)
    description = models.TextField()
    is_published = models.BooleanField()
    created_at = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.name


class ck(models.Model):
    name=models.CharField(max_length=30,null=True)
    des = RichTextField()

# Create your models here.
