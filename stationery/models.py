from django.core import files
from django.db import models
from users.models import User
from django.shortcuts import reverse
from .choices import CATEGORY, SERVICES, TASKS
# from multiselectfield import MultiSelectField


class Stationery(models.Model):    
    name         = models.CharField(max_length = 100, primary_key=True)
    profile      = models.ImageField(upload_to = 'stationery/', blank = False)
    location     = models.CharField(max_length = 100)
    motto        = models.TextField(default='Welcome to our worth stationery ever, get service on time. Here we value your choice')
    owner        = models.ForeignKey(User, on_delete=models.CASCADE, null=True )
    pub_date     = models.DateTimeField(auto_now_add = True)
    status       = models.BooleanField(default = False)#mainly to approve the stationery
    
    def __str__(self):
        return self.name
    
    @staticmethod
    def get_stationery_by_status(status):
        return Stationery.objects.filter(status = True).order_by('-pub_date')
        
    class Meta:
        verbose_name_plural = 'Stationeries'
    
    def get_absolute_url(self):
        return reverse('home')

#creating manager to approve the stationery
class PendingStationeryManager(models.Manager):
     def get_queryset(self):
          return super().get_queryset().filter(pending=True)

#proxy model for pending company
class PendingStationery(Stationery):

        objects = PendingStationeryManager()
        class Meta:
             proxy = True

class Location(models.Model):
    locatio_name    = models.CharField(max_length=255)
    cost            = models.PositiveIntegerField(default = 0)

    def __str__(self):
        return self.locatio_name

class Category(models.Model):
    category_name   = models.CharField(max_length=255, choices = CATEGORY, primary_key=True)

    def __str__(self):
        return self.category_name
    
    class Meta:
        verbose_name_plural = 'Categories'

class Product(models.Model):
    stat_name       = models.ForeignKey(Stationery, related_name="products_posted", on_delete=models.CASCADE)
    item_name       = models.CharField(max_length=100)
    item_desc       = models.TextField()
    item_img        = models.ImageField(upload_to = 'products/', blank = False)
    item_available  = models.PositiveIntegerField(default=0)
    item_category   = models.ForeignKey(Category, on_delete=models.CASCADE)
    item_price      = models.PositiveIntegerField()
    post_date       = models.DateTimeField(auto_now_add=True)
    view_count      = models.PositiveIntegerField(default = 0)

    def __str__(self):
        return self.item_name

    def get_absolute_url(self):
        return reverse('stock', kwargs={"pk": self.stat_name})
    
class Cart(models.Model):
    customer        = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank = True)
    total           = models.PositiveIntegerField(default= 0)
    timestamp       = models.DateTimeField(auto_now_add= True, auto_now = False)

    def __str__(self):
        return "Cart: " + str(self.id)

class CartItem(models.Model):
    cart            = models.ForeignKey(Cart, on_delete = models.CASCADE, blank = True, null = True)
    product         = models.ForeignKey(Product, on_delete = models.CASCADE)
    quantity        = models.PositiveIntegerField(default=1)
    rate            = models.PositiveIntegerField()
    subtotal        = models.PositiveBigIntegerField(null=True, blank = True)
    
    def __str__(self):
        return "Cart: " + str(self.cart.id) + " CartItem: " + str(self.id)

ORDER_STATUS =(
    ("order pending","order pending"),
    ("order received","order received"),
    ("order processing","order processing"),
    ("order completed","order completed"),
    ("order cancelled","order cancelled"),
)
class Order(models.Model):
    cart            = models.OneToOneField(Cart, on_delete=models.CASCADE, blank = True, null = True)
    customer        = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    full_name       = models.CharField(max_length=100) 
    email           = models.EmailField()
    phone           = models.PositiveIntegerField(null=True)
    destination     = models.CharField(max_length=100, blank=True) 
    order_date      = models.DateTimeField(auto_now_add=True)
    totalpay        = models.PositiveIntegerField()
    status          = models.CharField(max_length=255, choices=ORDER_STATUS, default=ORDER_STATUS[1][1])
    
    def __str__(self):
        return "Order: " + str(self.id)
        
delivery_choice = (
    ('self taking','self taking'),
    ('Nakutunuku','Nakutunuku'),
    ('LT1','LT1'),
    ('Library','Library'),
    )


BOOKING = (
    ('pending','pending'),
    ('received','received'),
    ('complete','complete'),
    )

class Booking(models.Model):
    customer        = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    stationery      = models.ForeignKey(Stationery, on_delete=models.CASCADE)
    file            = models.FileField(upload_to = 'documents/')
    service_type    = models.CharField(max_length=100, choices = SERVICES)
    doc_cost        = models.PositiveIntegerField()
    booking_date    = models.DateTimeField(auto_now_add=True)
    booking_status  = models.CharField(choices = BOOKING, max_length=255, default = BOOKING[0][0])
    delivery_mode   = models.CharField(choices=delivery_choice, default=delivery_choice[0][0], max_length=255)
    
    def __str__(self):
        return "Booking " + str(self.customer) +" " + str(self.service_type) +" "+ str(self.pk)

# class Payment(models.Model):
#     user        = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
#     amount      = models.PositiveIntegerField()
#     booking     = models.ForeignKey(Booking, on_delete=models.CASCADE, null=True, blank=True)
#     due_data    = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return "Tsh." + str(self.amount) + '/- payed by ' + str(self.user)



# class Report(models.Model):
#     stationery      = models.ForeignKey(Stationery, on_delete=models.CASCADE)
#     pdf             = models.CharField(max_length=255)

#     def __str__(self):
#         return self.id

# class Approve(models.Model):
#     pass 
#     def __str__(self):
#         return self.id