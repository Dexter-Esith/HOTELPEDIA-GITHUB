from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.db.models.fields import CharField
from django.forms import widgets
from phonenumber_field.formfields import PhoneNumberField
from phonenumber_field.widgets import PhoneNumberPrefixWidget
from pkg_resources import require
from .models import Account
from django_countries.widgets import CountrySelectWidget
from django import forms
from phonenumber_field.formfields import PhoneNumberField


class RegistrationForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = ('email', 'fname', 'lname')

    email = forms.CharField(widget=forms.EmailInput(attrs={'class': 'form-control',
                                                           'placeholder': 'Email'}))

    fname = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control',
                                                          'placeholder': 'First Name'}))

    lname = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control',
                                                          'placeholder': 'Last Name'}))

    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control',
                                                                  'placeholder': 'Password'}))

    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control',
                                                                  'placeholder': 'Confirmation Password'}))

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class UserCreationForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = ('email', 'name', 'surname', 'phone', 'bday', 'picture',)

    email = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control',
                                                          'placeholder': 'Email'}))

    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control',
                                                         'placeholder': 'Name'}))

    surname = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control',
                                                            'placeholder': 'Surname'}))

    phone = PhoneNumberField(widget=PhoneNumberPrefixWidget(initial='GE'))

    # bday = forms.CharField(widget=DatePickerInput(attrs={'class':'form-control', 'placeholder':'Birth Date'}))

    picture = forms.FileField(widget=forms.ClearableFileInput(attrs={'class': 'form-control'}))

    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'form-control',
                                                                                    'placeholder': 'Passowrd'}))

    password2 = forms.CharField(label='Password confirmation',
                                widget=forms.PasswordInput(attrs={'class': 'form-control',
                                                                  'placeholder': 'Passowrd'}))

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class UserChangeForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = ('email', 'fname', 'lname', 'phone', 'bday', 'country', 'gender', 'picture')

    email = forms.CharField(widget=forms.EmailInput(attrs={'name': 'email', 'class': 'form-control'}))
    # fname = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Name'}))
    # lname = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Surname'}))
    phone = PhoneNumberField(widget=PhoneNumberPrefixWidget(initial='GE'), required=False)
    phone.error_messages['invalid'] = 'Incorrect international code or Phone number!'

    # bday = forms.CharField(widget=DatePickerInput(attrs={'class':'form-control', 'placeholder':'Birth Date'}))
    # country = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Country'}))
    # gender = forms.ChoiceField(choices=Account.GENDER_CHOICES, widget=forms.Select(attrs={'class':'regDropDown'}))
    # picture = forms.FileField(widget=forms.ClearableFileInput(attrs={'class':'form-control'}))

    def clean_password(self):
        # Regardless of what the user provides, return the initial value.
        # This is done here, rather than on the field, because the
        # field does not have access to the initial value
        return self.initial["password"]


class AdminChangeForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = ('email', 'name', 'surname', 'phone', 'date_of_birth', 'picture',)

    email = forms.CharField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Name'}))
    surname = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Surname'}))
    phone = PhoneNumberField(widget=PhoneNumberPrefixWidget(initial='GE'))
    date_of_birth = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control datepickers', 'type': 'text', 'placeholder': 'dd-mm-yyyy',
               'autocomplete': 'off'}))
    picture = forms.FileField(widget=forms.ClearableFileInput())

    def clean_password(self):
        # Regardless of what the user provides, return the initial value.
        # This is done here, rather than on the field, because the
        # field does not have access to the initial value
        return self.initial["password"]


class LoginForm(forms.Form):
    email = forms.CharField(widget=forms.EmailInput(attrs={'class': "form-control",
                                                           'id': 'email',
                                                           "placeholder": "Email",
                                                           "type": "email",
                                                           "name": "email"}))

    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': "form-control",
                                                                 'id': 'password',
                                                                 "placeholder": "Password",
                                                                 "type": "password",
                                                                 "name": "password"}))


class ChangePasswordForm(forms.Form):
    current_password = forms.CharField(widget=forms.PasswordInput)
    new_password = forms.CharField(widget=forms.PasswordInput)
    repeat_password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = Account
        fields = ('current_password', 'new_password', 'repeat_password',)

