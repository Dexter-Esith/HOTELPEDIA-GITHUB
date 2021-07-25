from django.db import models
from django.db.models.fields import IntegerField, TextField
import multiselectfield
from account.models import Account
from multiselectfield import MultiSelectField
from phonenumber_field.modelfields import PhoneNumberField
from django_countries.fields import CountryField


############## START [ADD HOTEL STEP 1 CLASS] ##############
class AddHotelStep1(models.Model):
    customer = models.ForeignKey(Account, on_delete=models.CASCADE)
    # =========== START [INFO] ===========#
    hotel_name = models.CharField(max_length=50)
    short_description = models.TextField(max_length=250)
    long_description = models.TextField(max_length=2000)
    HOTEL_STAR = (
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5')
    )
    star = models.TextField(max_length=1, default=5, choices=HOTEL_STAR, null=True)
    created = models.DateTimeField(auto_now_add=True)
    # =========== END [INFO] ===========#

    # =========== START [LOCATION] ===========#
    street_address = models.CharField(max_length=100)
    address_line_2 = models.CharField(max_length=100, blank=True, null=True)
    country = CountryField(blank_label="Select the country/region you're from")
    city = models.CharField(max_length=100)
    post_code = models.IntegerField(null=True)
    # =========== END [LOCATION] ===========#

    picture = models.ImageField(upload_to='images/%Y/%m/%d/', default="images/default.jpg", blank=True)

    # =========== START [VIEW COUNTER] ===========#
    hotel_view = models.IntegerField(default=0)

    # =========== END [VIEW COUNTER] ===========#

    def __str__(self):
        return str(self.hotel_name)


############## END [ADD HOTEL STEP 1 CLASS] ##############


############## START [ADD HOTEL STEP 2 CLASS] ##############
class AddHotelStep2(models.Model):
    hotel_name_2 = models.ForeignKey(AddHotelStep1, on_delete=models.CASCADE)

    # =========== START [CONTACT] ===========#
    contact_name = models.CharField(max_length=50)
    contact_mobile_number = PhoneNumberField()
    alternative_contact_mobile_number = PhoneNumberField(blank=True)
    HOTEL_OWNER = (
        ('Yes', 'Yes'),
        ('No', 'No'),
    )
    owner = models.TextField(max_length=3, default='No', choices=HOTEL_OWNER)
    # =========== END [CONTACT] ===========#

    # =========== START [HOTEL TYPE] ===========#
    HOTEL_TYPE = (
        ('Single', 'Single'),
        ('Double', 'Double'),
        ('Twin', 'Twin'),
        ('Family', 'Family'),
        ('Studio', 'Studio')
    )
    hotel_type = models.TextField(max_length=10, choices=HOTEL_TYPE)
    # =========== END [HOTEL TYPE] ===========#


############## END [ADD HOTEL STEP 2 CLASS] ##############


############## START [SINGLE ROOM CLASS] ##############
class SingleRoom(models.Model):
    hotel_name_3 = models.ForeignKey(AddHotelStep2, on_delete=models.CASCADE)

    SIGNLE_ROOM_NAME = (
        ('Budget_single_room', 'Budget Single Room'),
        ('Standard_single_room', 'Standard Single Room'),
        ('Superior_single_room', 'Superior Single Room'),
        ('Deluxe_single_room', 'Deluxe Single Room'),
    )
    single_room_name = models.TextField(max_length=30, choices=SIGNLE_ROOM_NAME)

    SINGLE_ROOM_SMOKE = (
        ('Smoking', 'Smoking'),
        ('Non-Smoking', 'Non-Smoking'),
    )
    smoke = models.TextField(max_length=15, choices=SINGLE_ROOM_SMOKE)

    room_size = models.IntegerField()

    def __str__(self):
        return f'{self.single_room_name}'


############## END [SINGLE ROOM CLASS] ##############


############## START [DOUBLE ROOM CLASS] ##############
class DoubleRoom(models.Model):
    hotel_name_4 = models.ForeignKey(AddHotelStep2, on_delete=models.CASCADE)

    DOUBLE_ROOM_NAME = (
        ('Budget_Double_room', 'Budget Double Room'),
        ('Standard_Double_room', 'Standard Double Room'),
        ('Superior_Double_room', 'Superior Double Room'),
        ('Deluxe_Double_room', 'Deluxe Double Room'),
    )
    double_room_name = models.TextField(max_length=30, choices=DOUBLE_ROOM_NAME)

    DOUBLE_ROOM_SMOKE = (
        ('Smoking', 'Smoking'),
        ('Non-Smoking', 'Non-Smoking'),
    )
    smoke = models.TextField(max_length=15, choices=DOUBLE_ROOM_SMOKE)

    SINGLE_BED_SIZE = (
        ('Single_bed_90_130_1', 'Single Bed / 90-130 cm wide / 1 quantity'),
        ('Single_bed_90_130_2', 'Single Bed / 90-130 cm wide / 2 quantity'),
        ('Single_bed_90_130_3', 'Single Bed / 90-130 cm wide / 3 quantity'),
        ('Single_bed_90_130_4', 'Single Bed / 90-130 cm wide / 4 quantity'),
        ('Single_bed_90_130_5', 'Single Bed / 90-130 cm wide / 5 quantity'),
    )
    single_bed_size = TextField(choices=SINGLE_BED_SIZE)

    DOUBLE_BED_SIZE = (
        ('Double_bed_131_150_1', 'Double Bed / 131-150 cm wide / 1 quantity'),
        ('Double_bed_131_150_2', 'Double Bed / 131-150 cm wide / 2 quantity'),
        ('Double_bed_131_150_3', 'Double Bed / 131-150 cm wide / 3 quantity'),
        ('Double_bed_131_150_4', 'Double Bed / 131-150 cm wide / 4 quantity'),
        ('Double_bed_131_150_5', 'Double Bed / 131-150 cm wide / 5 quantity'),
    )
    double_bed_size = TextField(choices=DOUBLE_BED_SIZE)

    LARGE_BED_SIZE = (
        ('Large_bed_king_size_151_180_1', 'Large Bed (King Size) / 151-180 cm wide / 1 quantity'),
        ('Large_bed_king_size_151_180_2', 'Large Bed (King Size) / 151-180 cm wide / 2 quantity'),
        ('Large_bed_king_size_151_180_3', 'Large Bed (King Size) / 151-180 cm wide / 3 quantity'),
        ('Large_bed_king_size_151_180_4', 'Large Bed (King Size) / 151-180 cm wide / 4 quantity'),
        ('Large_bed_king_size_151_180_5', 'Large Bed (King Size) / 151-180 cm wide / 5 quantity'),
    )
    large_bed_size = TextField(choices=LARGE_BED_SIZE)

    capacity = models.IntegerField()

    room_size = models.IntegerField()

    def __str__(self):
        return f'{self.double_room_name}'


############## END [DOUBLE ROOM CLASS] ##############


############## START [APARTMENT CLASS] ##############
class Apartment(models.Model):
    customer = models.ForeignKey(Account, null=True, on_delete=models.CASCADE)
    apartment_view = models.IntegerField(default=0)
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=100, null=True)
    short_description = models.TextField(max_length=250)
    long_description = models.TextField(max_length=2000, null=True)
    picture = models.ImageField(upload_to='images/%Y/%m/%d/', default="images/default.jpg", blank=True)
    created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return str(self.name)
############## END [APARTMENT CLASS] ##############
