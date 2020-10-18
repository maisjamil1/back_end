from django.db import models
    
class Shop(models.Model):
    title = models.CharField(max_length=64)
    class Type(models.TextChoices):
        cars =  "cars"
        Electronics = "Electronics"
        Games = "Games"
        Fashion = "Fashion"
        Furniture ="Furniture"
        Real_Estate = "Real Estate"
        Food ="Food"
        Equipment = "Equipment"
        Books = "Books"
        pets = "pets"
        Business = "Business - Industrial"
        CraftsmenJobs = " Craftsmen"
        Electrician = "Electrician services"
        Travel = "Travel - Tourism"
        Medical = "Medical Services"
        Events = "Events Services"
        Teaching ="Teaching & Training"
        Others = "Others"
    type = models.CharField(
        max_length=1200,
        choices=Type.choices,
        default=Type.Others
    )
    # type = models.CharField(max_length=64)
    description= models.TextField()
    class Category(models.TextChoices):
        goods =  "goods"
        services = "services"
    category = models.CharField(
        max_length=200,
        choices=Category.choices,
        default=Category.goods 
    )
    owner = models.ForeignKey('auth.user', on_delete=models.CASCADE)
    phone = models.CharField(max_length=64)
    email = models.CharField(max_length=64)
    address = models.CharField(max_length=64)
    price = models.CharField(max_length=64)
    img = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.title    