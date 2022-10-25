from django.contrib import admin
from .models import CarMake, CarModel

# Register your models here.
#admin.site.register(CarMake)
#admin.site.register(CarModel)

# CarModelInline class
class CarModelInline(admin.StackedInline):
    model = CarModel
    extra = 5

#CarModelAdmin class
class CarModelAdmin(admin.ModelAdmin):
    fields = ('dealerID', 'model_name', 'car_type', 'make', 'year')

# CarMakeAdmin class with CarModelInline
class CarMakeAdmin(admin.ModelAdmin):
    fields = ['description', 'maker_name']
    inlines = [CarModelInline]

# Register models here
admin.site.register(CarMake,CarMakeAdmin)
admin.site.register(CarModel,CarModelAdmin)
