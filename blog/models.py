from django.db import models
import uuid
from .types import ProductCategories,AVAILABILITY,ORDER_STATUS,PAYMENT_MODE
# Create your models here.
class User(models.Model):
    Email_id = models.EmailField(unique = True)
    Created_at =  models.DateTimeField(auto_now_add=True, editable=False)
    Modified_at = models.DateTimeField(auto_now_add=True, editable=False)
    user_name = models.CharField(max_length=155,blank=False)
    password = models.CharField(max_length=155,blank=False)
    phone_number = models.CharField(max_length=10)
    address = models.JSONField(blank=True, null=True)
    slug = models.SlugField(max_length=255)
    def __str__(self):
        return self.user_name  

class Seller(models.Model): 
    Email_id = models.EmailField(unique = True)
    Created_at =  models.DateTimeField(auto_now_add=True, editable=False)
    Modified_at = models.DateTimeField(auto_now_add=True, editable=False)
    user_name = models.CharField(max_length=155,blank=False)
    password = models.CharField(max_length=155,blank=False)
    rating = models.FloatField(default=0)
    phone_number = models.CharField(max_length=10)
    address = models.JSONField(blank=True, null=True)
    def __str__(self):
        return self.user_name 

class Product(models.Model):
    CATERGORY_CHOICES = (
        (ProductCategories.ELECTRONICS, "Electronics"),
        (ProductCategories.CLOTHING, "Clothing"),
        (ProductCategories.BOOKS, "Books"),
        (ProductCategories.BEAUTY, "Beauty"),
        (ProductCategories.GROCERIES, "Groceries"),
        (ProductCategories.SPORTS,"Sports"),
    )
    AVAILABILITY_CHOICES = (
        (AVAILABILITY.FEW_LEFT,"FEW LEFT"),
        (AVAILABILITY.IN_STOCK,"IN STOCK"),
        (AVAILABILITY.OUT_OF_STOCK,"OUT OF STOCK"),
    )
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, serialize=True)
    name = models.CharField(max_length=255,blank=False)
    Category = models.PositiveIntegerField(choices=CATERGORY_CHOICES,blank=False)
    rating  = models.FloatField(default=0)
    seller = models.ForeignKey("blog.Seller", related_name="products", on_delete=models.CASCADE)
    count = models.PositiveIntegerField(default=0)
    description = models.CharField(max_length=5000)
    availability = models.PositiveIntegerField(choices=AVAILABILITY_CHOICES,blank=False)
    def __str__(self):
        return self.name

class Review(models.Model):
    content = models.CharField(max_length=1000)
    Product = models.ForeignKey("blog.Product",related_name="reviews",on_delete=models.CASCADE)
    users = models.ForeignKey("blog.User",related_name="reviews",on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    modified_at = models.DateTimeField(auto_now=True, editable=False)
    def __str__(self):
        return self.content
    
class Wishlist(models.Model):
    user = models.ForeignKey("blog.User",related_name="wishlists",on_delete=models.CASCADE)
    product = models.ForeignKey("blog.Product",related_name="wishlists",on_delete=models.CASCADE)

class OrderProduct(models.Model):
    order = models.ForeignKey("blog.Order",on_delete=models.CASCADE)
    product = models.ForeignKey("blog.Product",on_delete=models.CASCADE)

class Order(models.Model):
    STATUS_CHOICES = (
        (ORDER_STATUS.DELIVERED,"DELIVERED"),
        (ORDER_STATUS.OUT_FOR_DELIVERY,"OUT_FOR_DELIVERY"),
        (ORDER_STATUS.SHIPPED,"SHIPPED"),
    )
    created_at = models.DateTimeField(auto_now_add=True,editable=False)
    modified_at = models.DateTimeField(auto_now=True, editable=False)
    def get_default_request_name():
        order_count = Order.objects.count()
        order_count += 1
        return " Order {}".format(order_count)
    name = models.CharField(max_length=255,blank=False,null=False,default=get_default_request_name,)
    user = models.ForeignKey("blog.User",related_name="orders",on_delete=models.CASCADE)
    products = models.ManyToManyField("blog.Product",through=OrderProduct,related_name="orders") 
    status = models.PositiveIntegerField(choices = STATUS_CHOICES,default=ORDER_STATUS.SHIPPED)
    def __str__(self):
        return self.name
    
class Query(models.Model):
    user = models.ForeignKey("blog.User",related_name="queries",on_delete=models.CASCADE)
    product = models.ForeignKey("blog.Product",related_name="queries",on_delete=models.CASCADE)
    def __str__(self):
        return self.user.user_name

class Payment(models.Model):
    PAYMENT_MODE_CHOICES =  (
        (PAYMENT_MODE.OFFLINE,"OFFLINE"),
        (PAYMENT_MODE.ONLINE,"ONLINE"),
        (PAYMENT_MODE.OTHER,"OTHER"),
    )
    user = models.ForeignKey("blog.User",related_name="payments",on_delete=models.CASCADE)
    order = models.OneToOneField("blog.Order",related_name="payment",on_delete=models.CASCADE)
    card_no = models.CharField(blank = True,null = True,max_length=20)
    mode = models.IntegerField(choices=PAYMENT_MODE_CHOICES,default=PAYMENT_MODE.ONLINE)
