from django.urls import path
from .import views

app_name = 'account'

urlpatterns = [
    path('register', views.register, name='register'),
    path('signin', views.sign_in, name='signin'),
    path('signout', views.signout, name='signout'),
    path('manageaccount', views.manage_account, name='manageaccount'),
    path('editprofile/<int:id>', views.edit_profile, name='editprofile'),
    path('changepassword', views.change_password, name='changepassword'),

]