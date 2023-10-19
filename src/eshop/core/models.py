from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here
class Role(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
    
class User(AbstractUser):
    # user_name = models.CharField(max_length=50)
    # password_hash = models.TextChoices()

    # role can have many users
    role = models.ForeignKey(Role, related_name='role', on_delete=models.CASCADE, null=True)

    # first_name = models.CharField(max_length=127)
    # last_name = models.CharField(max_length=127)
    address = models.CharField(max_length=255)
    phone = models.CharField(max_length=20)
    # email = models.EmailField()

class Category(models.Model):
    name = models.CharField(max_length=255)
    
    class Meta:
        verbose_name_plural='Categories'

    def __str__(self):
        return self.name

class Item(models.Model):
        
    class ItemType(models.TextChoices):
        AVAILABLE = 'Available'
        UNAVAILABLE = 'Unavailable'

    status = models.BooleanField()
    #category may have many items
    category = models.ForeignKey(Category, related_name='items', on_delete=models.CASCADE)

    type = models.CharField(choices=ItemType.choices, default=ItemType.UNAVAILABLE, max_length=50)
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True,null=True)
    quantity = models.PositiveIntegerField()
    price = models.FloatField()
    #user may own a lot of items
    owner = models.ForeignKey(User, related_name='items', on_delete=models.CASCADE)

    #
    added_to_cart_by = models.ManyToManyField(User, related_name='cart_items')
    wished_by = models.ManyToManyField(User, related_name='wished_items')

class Discount(models.Model):
    percentage = models.IntegerField(validators=[
            MinValueValidator(limit_value=0, message="Percentage cannot be less than 0."),
            MaxValueValidator(limit_value=100, message="Percentage cannot be greater than 100.")
        ])
    
    #user can create many discounts
    user = models.ForeignKey(User,related_name='discounts', on_delete=models.CASCADE)
    item = models.OneToOneField(Item, related_name='discount', on_delete=models.CASCADE)

class Order(models.Model):

    class OrderType(models.TextChoices):
        ACTIVE = 'Active'
        COMPLETED = 'Completed'

    price = models.FloatField(validators=[
            MinValueValidator(limit_value=0, message="Price cannot be less than 0."),
        ])
    ordered_at = models.DateTimeField(auto_now_add=True)
    type = models.CharField(choices=OrderType.choices, default=OrderType.ACTIVE, max_length=50)

    ordered_by = models.ForeignKey(User, related_name='orders', on_delete=models.CASCADE)



class DeliveryData(models.Model):

    class DeliveryDataType(models.TextChoices):
        EXPRESS = 'Express'
        ORDINARY = 'Ordinary'

    address = models.CharField(max_length=255)
    type = models.CharField(choices=DeliveryDataType.choices, default=DeliveryDataType.ORDINARY, max_length=50)
    
    #one order can have one deliverydata
    order = models.OneToOneField(Order, related_name='delivery_data', on_delete=models.CASCADE)
    #use can have many delivery datas
    user = models.ForeignKey(User, related_name='delivery_datas', on_delete=models.CASCADE)