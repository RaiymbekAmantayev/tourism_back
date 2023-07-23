from django.db import models
from django.contrib.auth.models import User

class Model(models.Model):
    id = models.AutoField(primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        abstract = True
        
class Country(Model):
    title=models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.title
    
    class Meta:
        verbose_name_plural = 'Страны'

class CategoryHotel(Model):
    value=models.CharField(max_length=255)

    def __str__(self)->str:
        return self.value

class Hotel(Model):
    title=models.CharField(max_length=255)
    country = models.ForeignKey(Country, on_delete=models.CASCADE, null=True)   
    category = models.ForeignKey(CategoryHotel, on_delete=models.CASCADE, null=True)
    img=models.ImageField(null=True)
    contact = models.BigIntegerField()
    price = models.IntegerField()

    def __str__(self) -> str:
        return self.title

class Category(Model):
    title=models.CharField(max_length=255, null=True)
    def __str__(self) -> str:
        return self.title
    class Meta:
        verbose_name_plural = 'Категории'



class Tour(Model):
    title=models.CharField(max_length=255)
    country=models.ForeignKey(Country, on_delete=models.CASCADE, null=True)
    img = models.ImageField(null=True)
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE, null=True)
    date_of_start=models.DateField()
    date_of_end=models.DateField()
    price=models.IntegerField()
    category=models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    def __str__(self) -> str:
        return self.title
    
    
    class Meta:
        verbose_name_plural = 'Туры'

class Booking(Model):
        customer=models.ForeignKey(User, on_delete=models.CASCADE, null=True)
        tour=models.ForeignKey(Tour, on_delete=models.CASCADE, null=True)
        book_date=models.DateField()
        status=models.BooleanField(default=True)
        def __str__(self) -> str:
            return self.customer
    
        class Meta:
            verbose_name_plural = 'Бронь'

class Review(Model):
        customer=models.ForeignKey(User, on_delete=models.CASCADE, null=True)
        tour=models.ForeignKey(Tour, on_delete=models.CASCADE, null=True)
        text=models.TextField()
        ranking=models.IntegerField(default=True)
        def __str__(self) -> str:
            return self.customer
    
        class Meta:
            verbose_name_plural = 'Отзывы'


class Clicks(Model):
    first_name = models.CharField(max_length=255)
    number = models.BigIntegerField()

    class Meta:
        verbose_name_plural = "Заявки"

class Attractions(Model):
    title = models.CharField(max_length=255)
    country = models.ForeignKey(Country, related_name="attraction", on_delete=models.CASCADE, null=True)

    def __str__(self) -> str:
        return self.title

class DIY(Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE, null=True, default=None)
    country = models.ForeignKey(Country, on_delete=models.CASCADE, null=True)
    cust_number = models.BigIntegerField(verbose_name="номер клиента")
    date_of_start=models.DateField()
    date_of_end=models.DateField()
    attraction= models.ManyToManyField(Attractions)
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE, null=True)
    class Meta:
        verbose_name_plural = 'Do it yourself'