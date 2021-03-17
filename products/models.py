from django.db import models
from django.utils.translation import gettext_lazy as _
from django.conf import settings
from accounts.models import Address

class Category(models.Model):
    name = models.CharField(_("category name"), max_length=100)


class Product(models.Model):
    name = models.CharField(_("product name"), max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    description = models.CharField(_("product name"), max_length=100)
    price = models.IntegerField(_("product price"), default=0)
    image = models.ImageField(upload_to='images/', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Order(models.Model):
    STATUS = [
        ('pending', 'Pending'), ('accepted', 'Accepted'),
        ('delivered', 'Delivered'), ('declined', 'Declined'),
        ('cancelled', 'Cancelled'), ('picked_up', 'Picked Up')
    ]
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    address = models.ForeignKey(Address, on_delete=models.CASCADE)
    status = models.CharField(_('Status'), max_length=20, default='pending', choices=STATUS)
    amount = models.IntegerField(_("product price"), default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    
class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(_("item quantity"), default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    
class CartItem(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(_("item quantity"), default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)