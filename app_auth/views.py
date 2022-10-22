from django.shortcuts import render, redirect
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import CustomAuthenticationForm, CustomUserCreationForm, UserProfileUpdateForm, UserSettingsUpdateForm
from .models import UserProfile, UserSettings
from django.contrib import messages

def load_userprofile(user):
    try:
        return user.userprofile
    except:  # this is not great, but trying to keep it simple
        obj = UserProfile.objects.create(user=user)
        return obj

def load_usersettings(user):
    try:
        return user.usersettings
    except:  # this is not great, but trying to keep it simple
        obj = UserSettings.objects.create(user=user)
        return obj

@login_required(login_url='login_user')
def user_page(request):
    profile_instance = load_userprofile(request.user)
    settings_instance = load_usersettings(request.user)       
    
    if request.method == 'POST':
        data = request.POST
        profile_form = UserProfileUpdateForm(data, instance=profile_instance)
        settings_form = UserSettingsUpdateForm(data, instance=settings_instance)
    
        if profile_form.is_valid() and settings_form.is_valid():
            profile_form.save()
            settings_form.save()
            messages.success(request, _('The changes have been saved.'))
    
    else:
        profile_form = UserProfileUpdateForm(instance=profile_instance)
        settings_form = UserSettingsUpdateForm(instance=settings_instance)
        
    context = { 'title':            _('User page'), 
                'content_title':    _('User page'),
                'active':           'auth',
                'profile_form':     profile_form, 
                'settings_form':    settings_form,
                }
                     
    return render(request, 'auth/user_page.html', context)
    
def login_user(request):
    next = request.GET.get('next')
    form = CustomAuthenticationForm()    
    if request.method == 'POST':
        data = request.POST
        form = CustomAuthenticationForm(request=request, data=data)

        if form.is_valid(): 
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')                      
            user = authenticate(username=username, password=password)
            
            if user is not None:
                login(request, user)
                if next:
                    return redirect(next)                 
                return redirect('index')
 
    context = { 'title':            _('Login'), 
                'content_title':    _('Login'),
                'active':           'auth', 
                'form':             form,
                }
    
    return render(request, "auth/login.html", context)

def registration(request):
    next = request.GET.get('next')
    form = CustomUserCreationForm()    
    if request.method == 'POST':
        data = request.POST
        form = CustomUserCreationForm(data)

        if form.is_valid():
            user = form.save(commit=False)
            user.save()
       
            user_auth = authenticate(
                request, username=user.username, password=data['password1'])
            
            if user_auth is not None:
                
                user_profile = UserProfile()
                user_profile.user = user_auth
                user_profile.email = data['email']
                user_profile.save()
                
                user_settings = UserSettings()
                user_settings.user = user_auth
                user_settings.some_parameter = data['some_parameter']
                user_settings.save()                
                
                login(request, user_auth)
                if next:
                    return redirect(next)    
                return redirect('index')  
                
    
    context = { 'title':            _('Registration'), 
                'content_title':    _('Registration'),
                'active':           'auth', 
                'form':             form,
                }
    return render(request, "auth/registration.html", context)
    
    
def logout_user(request):
    logout(request)
    return redirect('index')    
