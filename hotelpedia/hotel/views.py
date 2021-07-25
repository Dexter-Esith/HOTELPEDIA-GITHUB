from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Apartment, AddHotelStep1, AddHotelStep2
from .forms import AddHotelStep1Form, AddHotelStep2Form, ApartmentForm, SingleRoomForm, DoubleRoomForm
import random

def home(request):
    hotels = AddHotelStep1.objects.all()
    apartments = Apartment.objects.all()
    top_hotels = ()
    for hotel in hotels:
        if str(hotel.star) == str(5) and len(top_hotels) < 4:
            top_hotels += (hotel,)
    context = {'hotels':hotels, 'apartments':apartments, 'top_hotels':top_hotels}
    return render(request, 'home.html', context)

def hotels_page(request):
    hotels = AddHotelStep1.objects.all()
    apartments = Apartment.objects.all()
    properties = []
    for hotel in hotels:
        properties.append(hotel)
    for apartment in apartments:
        properties.append(apartment)
    random.shuffle(properties)
    context = {'properties':properties}
    return render(request, 'hotels_page.html', context)


def seemore(request, property_id):

    hotel_seemore = AddHotelStep1.objects.get(id = property_id)
    hotel_seemore.hotel_view = hotel_seemore.hotel_view + 1
    hotel_seemore.save()

    # apartment_seemore = Apartment.objects.get(id = property_id)
    # apartment_seemore.apartment_view = apartment_seemore.apartment_view + 1
    # apartment_seemore.save()

    context = {'hotel_seemore':hotel_seemore,}
    return render(request, 'seemore.html', context)


@login_required
def list_property(request):
    return render(request, 'list_property.html')


@login_required
def add_hotel(request):
    form = AddHotelStep1Form()
    if request.method == "POST":
        form = AddHotelStep1Form(request.POST, request.FILES)
        if form.is_valid():
            data = form.save(commit=False)
            data.customer = request.user      # daloginebuli user-it rom daematos sastumro (customer wamogebulia models.py-dan)
            data.save()
            if data.hotel_type == "Single":
                return redirect('hotel:addhotel2', data.id)

    context = {'form':form,}
    return render(request, 'add_hotel.html', context)

@login_required
def add_hotel_2(request, id):
    form = AddHotelStep2Form()
    if request.method == "POST":
        form = AddHotelStep2Form(request.POST, request.FILES)
        if form.is_valid():
            data = form.save(commit=False)
            data.customer = request.user      # daloginebuli user-it rom daematos sastumro (customer wamogebulia models.py-dan)
            data.save()
            if data.hotel_type == "Single":
                return redirect('hotel:single_room', data.id)
            else:
                return redirect('hotel:double_room', data.id)

    context = {'form':form,}
    return render(request, 'add_hotel_2.html', context)


@login_required
def single_room(request, id):
    hotel = AddHotelStep1.objects.get(id=id)
    form = SingleRoomForm()
    if request.method == "POST":
        form = SingleRoomForm(request.POST, request.FILES)
        if form.is_valid():
            data = form.save(commit=False)
            data.hotel_name = hotel
            data.save()
            return redirect('hotel:home')

    context = {'form':form,}
    return render(request, 'single_room.html', context)

@login_required
def double_room(request, id):
    form = DoubleRoomForm()
    if request.method == "POST":
        form = DoubleRoomForm(request.POST, request.FILES)
        if form.is_valid():
            data = form.save(commit=False)
            data.save()
            return redirect('hotel:home')

    context = {'form':form,}
    return render(request, 'double_room.html', context)

@login_required
def add_apartment(request):
    form = ApartmentForm()
    if request.method == "POST":
        form = ApartmentForm(request.POST, request.FILES)
        if form.is_valid():
            data = form.save(commit=False)
            data.customer = request.user      # daloginebuli user-it rom daematos sastumro (customer wamogebulia models.py-dan)
            data.save()
            return redirect('hotel:home')


    context = {'form':form,}
    return render(request, 'add_apartment.html', context)

@login_required
def edit_hotel(request, id):
    edit = AddHotelStep1.objects.get(id=id)
    form = AddHotelStep1Form(instance=edit)
    if request.method == "POST":
        form = AddHotelStep1Form(request.POST, request.FILES, instance=edit)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'form':form}
    return render(request, 'add_hotel.html', context)


@login_required
def delete_page(request):
    return render(request, 'myhotels.html')

@login_required
def delete_property(request, id):
    hotel = AddHotelStep1.objects.get(id=id)
    if request.method == "POST":
        hotel.delete()
        return redirect('/', id)
    context = {'hotel':hotel}
    return render(request, 'delete_property.html', context)



@login_required
def my_hotels(request):
    hotels = AddHotelStep1.objects.all()
    context = {'hotels':hotels}
    return render(request, 'myhotels.html', context)
