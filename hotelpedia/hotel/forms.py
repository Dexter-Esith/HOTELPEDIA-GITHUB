from django.forms import ModelForm
from .models import AddHotelStep1, AddHotelStep2, Apartment, SingleRoom, DoubleRoom

class AddHotelStep1Form(ModelForm):
    class Meta:
        model = AddHotelStep1
        exclude = ('customer', 'hotel_view') # sastumros damatebisas user-is saxeli rom ar chandes

class AddHotelStep2Form(ModelForm):
    class Meta:
        model = AddHotelStep2
        exclude = ('hotel_name',) # sastumros damatebisas user-is saxeli rom ar chandes

class SingleRoomForm(ModelForm):
    class Meta:
        model = SingleRoom
        exclude = ('hotel_name',) # sastumros damatebisas user-is saxeli rom ar chandes


class DoubleRoomForm(ModelForm):
    class Meta:
        model = DoubleRoom
        exclude = ('hotel_name',) # sastumros damatebisas user-is saxeli rom ar chandes


class ApartmentForm(ModelForm):
    class Meta:
        model = Apartment
        exclude = ('customer', 'apartment_view') # sastumros damatebisas user-is saxeli rom ar chandes