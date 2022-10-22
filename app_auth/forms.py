from django import forms
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User
from .models import UserProfile, UserSettings
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

class CustomUserCreationForm(UserCreationForm):
    
    email = forms.EmailField(required=False)
    some_parameter = forms.CharField(required=False)
     
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2', 'email']
        
    def __init__(self, *args, **kwargs):
        super(CustomUserCreationForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'class': 'form-control', 'placeholder': _('Enter username...')})
        self.fields['password1'].widget.attrs.update({'class': 'form-control', 'placeholder': _('Enter password...')})
        self.fields['password2'].widget.attrs.update({'class': 'form-control', 'placeholder': _('Confirm password...')})
        self.fields['email'].widget.attrs.update({'class': 'form-control', 'placeholder': _('Enter your email...')})
        self.fields['some_parameter'].widget.attrs.update({'class': 'form-control', 'placeholder': _('Enter some parameter...')})

class CustomAuthenticationForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ['username', 'password']
        
    def __init__(self, *args, **kwargs):
        super(CustomAuthenticationForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'class': 'form-control', 'placeholder': _('Enter username...')})
        self.fields['password'].widget.attrs.update({'class': 'form-control', 'placeholder': _('Enter password...')})
  
class UserProfileUpdateForm(forms.ModelForm):
    
    email = forms.EmailField(required=False)
    
    class Meta:
        model = UserProfile
        fields = ['email']  
    
    def __init__(self, *args, **kwargs):
        super(UserProfileUpdateForm, self).__init__(*args, **kwargs)
        self.fields['email'].widget.attrs.update({'class': 'form-control', 'placeholder': _('Enter username...')})
                      
class UserSettingsUpdateForm(forms.ModelForm):
    
    some_parameter = forms.CharField(required=False)
    
    class Meta:
        model = UserSettings
        fields = ['some_parameter']  
    
    def __init__(self, *args, **kwargs):
        super(UserSettingsUpdateForm, self).__init__(*args, **kwargs)
        self.fields['some_parameter'].widget.attrs.update({'class': 'form-control', 'placeholder': _('Enter username...')})
    
