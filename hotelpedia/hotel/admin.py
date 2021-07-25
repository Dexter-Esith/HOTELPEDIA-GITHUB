from django.contrib import admin
from .models import AddHotelStep1, AddHotelStep2, Apartment, SingleRoom, DoubleRoom

# Register your models here.
admin.site.register(AddHotelStep1)
admin.site.register(AddHotelStep2)
admin.site.register(Apartment)
admin.site.register(SingleRoom)
admin.site.register(DoubleRoom)
