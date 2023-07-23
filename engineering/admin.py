from django.contrib import admin
from .models import *

@admin.register(Tour)
class TourAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'country', 'img','date_of_start', 'date_of_end', 'price', 'category')
    list_display_links = ('id', 'title',)
    search_fields = ('title', 'price','category')

    def __str__(self) -> str:
        return self.Type
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title',)
    def __str__(self) -> str:
        return self.Type

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('id', 'customer', 'tour', 'book_date', 'status')
    list_display_links = ('id', 'customer',)
    search_fields = ('customer','status')
    # list_filter = ('last_name',)

    def __str__(self) -> str:
        return self.Type
    
@admin.register(Review)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('id', 'customer', 'tour', 'text', 'ranking')
    list_display_links = ('id', 'customer',)
    search_fields = ('customer','tour')

    def __str__(self) -> str:
        return self.Type
    
@admin.register(Clicks)
class CliksAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'number')

    def __str__(self) -> str:
        return self.Type
    
@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title',)
    list_display_links = ('id', 'title',)

    def __str__(self) -> str:
        return self.Type
    
@admin.register(CategoryHotel)
class CategoryHotelAdmin(admin.ModelAdmin):
    list_display = ('id', 'value',)
    list_display_links = ('id', 'value',)

    def __str__(self) -> str:
        return self.Type
    
@admin.register(Hotel)
class HotelAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'country', 'category', 'contact', 'price')
    list_display_links = ('id', 'title')

    def __str__(self) -> str:
        return self.Type
    
@admin.register(Attractions)
class AttractionsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'country')
    list_display_links = ('id', 'title')

    def __str__(self) -> str:
        return self.Type
    
@admin.register(DIY)
class DIYAdmin(admin.ModelAdmin):
    list_display = ('id', 'customer', 'country', 'cust_number', 'date_of_start', 'date_of_end','hotel')
    list_display_links = ('id',)
    def __str__(self) -> str:
        return self.Type
