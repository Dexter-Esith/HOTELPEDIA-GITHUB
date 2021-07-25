from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages
from .forms import RegistrationForm, LoginForm, UserChangeForm, ChangePasswordForm
from .models import Account


# Registration
@csrf_exempt
def register(request):
    form = RegistrationForm()
    context = {'form': form}
    if request.method == "POST":
        form = RegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            data = form.save(commit=False)
            data.save()
            new_user = authenticate(email=form.cleaned_data['email'],
                                    password=form.cleaned_data['password1'], )
            login(request, new_user)
            messages.success(request, 'Account has succesfully created.')
            return redirect('hotel:home')
        else:
            messages.warning(request, 'Email or password is not correct.')
    return render(request, "register.html", context)


# Login
@csrf_exempt
def sign_in(request):
    form = LoginForm()
    context = {'form': form}
    if request.method == "POST":
        form = LoginForm(request.POST or None)
        try:
            Account.objects.get(email=request.POST.get('email'))
            if form.is_valid():
                data = form.cleaned_data
                user = authenticate(email=str(data['email']), password=str(data['password']))

                if user is not None:
                    login(request, user)
                    return redirect('hotel:home')  # succesfully logged in
                else:
                    messages.warning(request, 'Email or password is not correct.')

        except:
            messages.warning(request, 'Email or password is not correct.')

    return render(request, 'login.html', context)


# Sign Out
@login_required
def signout(request):
    logout(request)
    return redirect('/')


# Manage Account
@login_required
def manage_account(request):
    return render(request, 'manage_account.html')


# Edit Profile
@login_required
def edit_profile(request, id):
    account = Account.objects.get(id=id)
    # context['DATA_UPLOAD_MAX_MEMORY_SIZE'] = settings.DATA_UPLOAD_MAX_MEMORY_SIZE
    user = Account.objects.get(id=id)
    form = UserChangeForm(instance=user)
    if request.method == "POST":
        form = UserChangeForm(request.POST, files=request.FILES, instance=user)
        if form.is_valid():
            post_email = form.cleaned_data.get('email')  # Extracting the email value from the form
            if Account.objects.filter(email=post_email).exists():
                if str(account) == str(post_email):
                    data = form.save(commit=False)
                    data.is_active = True
                    data.save()
                    messages.warning(request, "Personal data succesfully updated.")
                    return redirect('account:editprofile', id)
            else:
                data = form.save(commit=False)
                data.is_active = True
                data.save()
                messages.warning(request, "Personal data succesfully updated.")
                return redirect('account:editprofile', id)
        else:
            post_email = form.data.get('email')  # Extracting the email value from the form
            if Account.objects.filter(email=post_email).exists():
                if str(account) != str(post_email):
                    messages.warning(request, "Email already exists")
    context = {'form': form, 'user': user}
    return render(request, 'edit_profile.html', context)


# Change Password
@login_required
def change_password(request):
    reset_form = ChangePasswordForm()
    if request.method == "POST":
        reset_form = ChangePasswordForm(request.POST)
        user = Account.objects.get(id=request.user.id)
        if request.user.check_password(request.POST.get('current_password')):
            if reset_form.is_valid():
                if request.POST.get('new_password') == request.POST.get('repeat_password'):
                    password = reset_form.cleaned_data['new_password']
                    user.set_password(password)
                    user.save()
                    update_session_auth_hash(request, user)
                    messages.success(request, 'Password has succesfully changed.')
                    return redirect('account:changepassword')
                else:
                    messages.warning(request, 'New password do not match.')
        else:
            messages.warning(request, 'Old password is not correct.')

    context = {'reset_form': reset_form, }
    return render(request, 'change_password.html', context)