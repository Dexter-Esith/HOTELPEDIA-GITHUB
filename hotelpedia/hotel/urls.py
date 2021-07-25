from django.urls import path
from .import views

app_name = 'hotel'

urlpatterns = [

# SEE PROPERTIES
    path('', views.home, name="home"),                                                                 # Main Page
    path('hotels', views.hotels_page, name="hotels_page"),                                             # Hotels
    # path('apartments', views.apartments_page, name="apartments_page"),                                 # Apartments
    # path('hotel/<int:hotel_id>', views.seemore_hotel, name='seemore_hotel'),                           # seemore Hotel
    # path('apartment/<int:apartment_id>', views.seemore_apartment, name='seemore_apartment'),           # seemore Apartment
    path('seemore/<int:property_id>', views.seemore, name='seemore'),                           # seemore


# ADD PROPERTY TO THE SITE
    path('listproperty', views.list_property, name='listproperty'),                                    # list Property
    # HOTEL
    path('addhotel', views.add_hotel, name='addhotel'),                                                # add new Hotel
    path('addhotel2/<int:id>', views.add_hotel_2, name='addhotel2'),                                      # add new Hotel Step 2
    path('single/<int:id>', views.single_room, name='single_room'),                                    # add single type Hotel
    path('double/<int:id>', views.double_room, name='double_room'),                                    # add double type Hotel
    # APARTMENT
    path('addapartment', views.add_apartment, name='addapartment'),                                    # add new Apartment

# OWN PROPERTIES / EDIT / DELETE
    path('edithotel/<int:id>', views.edit_hotel, name='edithotel'),                                    # edit Hotel
    path('myhotels', views.my_hotels, name='myhotels'),                                                # my Properties
    path('delete_property/<int:id>', views.delete_property, name='delete_property'),                   # delete Property





]